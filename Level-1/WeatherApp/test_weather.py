import unittest
import requests
from unittest.mock import patch, Mock
from main import safe_request, first_query, second_query

class TestWeatherApp(unittest.TestCase):

    @patch('requests.get')
    def test_safe_request_success(self, mock_get):
        # create a repeatative Mock, as a success response from API
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None  # simulates: no error
        mock_response.json.return_value = {"results": [{"latitude": 12.34, "longitude": 56.78}]}
        mock_get.return_value = mock_response
        
        city = 'Test City'
        response = safe_request(city)
        
        self.assertIsNotNone(response)
        self.assertTrue('results' in response.json())
        self.assertEqual(response.json()["results"][0]["latitude"], 12.34)
        self.assertEqual(response.json()["results"][0]["longitude"], 56.78)
    
    @patch('requests.get')
    def test_safe_request_failure(self, mock_get):
        # create a restore Mock as a respond with Error
        mock_get.side_effect = requests.exceptions.RequestException("API request failed")
        
        city = 'Test City'
        response = safe_request(city)
        
        self.assertIsNone(response)

    def test_first_query_success(self):
        # confirm check for lat & lon return
        mock_json = {
            "results": [{"latitude": 12.34, "longitude": 56.78}]
        }
        with patch('main.safe_request') as mock_safe_request:
            mock_safe_request.return_value.json.return_value = mock_json
            lat, lon = first_query('Test City')
            self.assertEqual(lat, 12.34)
            self.assertEqual(lon, 56.78)

    def test_first_query_failure(self):
        # checks if returns None when no results
        mock_json = {"results": []} # simulates empty results
        with patch('main.safe_request') as mock_safe_request:
            mock_safe_request.return_value.json.return_value = mock_json
            lat, lon = first_query('Invalid City')
            self.assertIsNone(lat)
            self.assertIsNone(lon)

    @patch('requests.get')
    def test_second_query(self, mock_get):
        # create a Mock for weather reading
        mock_response = Mock()
        mock_response.json.return_value = {
            "daily": {
                "relative_humidity_2m_mean": [80, 75, 72],
                "temperature_2m_min": [10, 11, 12],
                "temperature_2m_max": [20, 21, 22]
            }
        }
        mock_get.return_value = mock_response
        
        humids, max_tmp, min_tmp = second_query(56.78, 12.34)
        
        self.assertEqual(humids, [80, 75, 72])
        self.assertEqual(max_tmp, [20, 21, 22])
        self.assertEqual(min_tmp, [10, 11, 12])

if __name__ == '__main__':
    unittest.main()
