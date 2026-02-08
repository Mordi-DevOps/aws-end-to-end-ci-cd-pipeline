"""docstring"""
import boto3
from flask import Flask, render_template, request, jsonify
import requests
from botocore.exceptions import ClientError

app = Flask(__name__)

# Initialize the S3 client
# Note: If EC2 has an IAM Role - no need to provide keys here.
s3_client = boto3.client('s3', region_name='us-east-1')

def safe_request(city):
    """safe request"""
    try:
        first_request_url = f"https://geocoding-api.open-meteo.com/v1/search"
        try_to_get = requests.get(first_request_url, params={'name': city})
        try_to_get.raise_for_status()
        return try_to_get

    except requests.exceptions.RequestException:
        pass

    except ValueError:
        pass

def first_query(city):
    """first query"""
    json_data = safe_request(city).json()
    if not 'results' in json_data or len(json_data['results']) == 0:
        return (None, None)
    lat = json_data.get("results")[0]["latitude"]
    lon = json_data.get("results")[0]["longitude"]
    return (lat, lon)

def second_query(lon, lat):
    """second query"""
    second_request_url = f"https://api.open-meteo.com/v1/forecast"
    second_params = {'latitude':lat, 'longitude':lon, 'forecast_days':7,
               'daily':('temperature_2m_min','temperature_2m_max','relative_humidity_2m_mean')}
    call_results = requests.get(second_request_url, second_params).json()
    humids = call_results.get("daily")["relative_humidity_2m_mean"]
    min_tmp = call_results.get("daily")["temperature_2m_min"]
    max_tmp = call_results.get("daily")["temperature_2m_max"]
    return (humids, max_tmp, min_tmp)


@app.route('/', methods=["GET", "POST"])
def get_weather():
    """get weather"""
    min_temp = None
    max_temp = None
    humidity = None
    if 'city' in request.form:
        city = request.form['city']
        (lat, lon) = first_query(city)
        if not lon or not lat:
            return render_template("main.html", city="you entered a wrong value")
        (got_humids, got_max_tmp, got_min_tmp) = second_query(lon, lat)
        return render_template(
        "main.html",
            city = city,
            min_temp = got_min_tmp,
            max_temp = got_max_tmp,
            humidity = got_humids,
        )
    return render_template("main.html")

@app.route('/generate-download-url')
def generate_download_url():
    """Generates a temporary S3 link to download the sky image"""
    bucket_name = 'weather-assets-mordi' # <--- Change this to your bucket name
    object_name = 'my_sky_image.jpeg'       # <--- Ensure this matches your S3 file name
    
    try:
        # Generate the presigned URL
        response = s3_client.generate_presigned_url('get_object',
            Params={
                'Bucket': bucket_name,
                'Key': object_name,
                # This header tells the browser: "Download me, don't just show me"
                'ResponseContentDisposition': f'attachment; filename="{object_name}"'
            },
            ExpiresIn=300) # Link lasts 5 minutes
            
        return jsonify({"download_url": response})
    
    except ClientError as e:
        print(f"S3 Error: {e}")
        return jsonify({"error": "Could not generate link"}), 500
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
