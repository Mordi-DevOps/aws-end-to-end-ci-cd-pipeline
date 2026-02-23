"""docstring"""
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
