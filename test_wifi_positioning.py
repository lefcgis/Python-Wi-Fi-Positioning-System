import unittest
import json
import os
import sys
import tempfile
from wifi_positioning_system import WifiScanner, GeolocationAPI, MapGenerator, prettify_json


class TestWifiPositioning(unittest.TestCase):
    """Unit tests for the Wi-Fi Positioning System."""

    def test_demo_data_loading(self):
        """Test that demo data can be loaded and formatted correctly."""
        with open('demo_data.json', 'r') as f:
            demo_data = json.load(f)
        wifi_data = [(ap['macAddress'], ap['signalStrength']) for ap in demo_data['wifiAccessPoints']]
        
        # Check that wifi_data is a list
        self.assertIsInstance(wifi_data, list)
        # Check that it's not empty
        self.assertGreater(len(wifi_data), 0)
        # Check that each item is a tuple with (str, int)
        for item in wifi_data:
            self.assertIsInstance(item, tuple)
            self.assertIsInstance(item[0], str)
            self.assertIsInstance(item[1], int)

    def test_prettify_json(self):
        """Test JSON prettifying function."""
        test_data = {"key1": "value1", "key2": {"subkey": "subvalue"}}
        
        # Test without prettify
        result = prettify_json(test_data, prettify=False)
        self.assertIsInstance(result, str)
        self.assertEqual(json.loads(result), test_data)
        
        # Test with prettify
        result = prettify_json(test_data, prettify=True)
        self.assertIsInstance(result, str)
        self.assertIn('\n', result)  # Prettified JSON should have newlines

    def test_map_generation(self):
        """Test that the map generation works correctly."""
        api_result = {
            'location': {'lat': -12.0464, 'lng': -77.0428},  # Lima, Perú
            'accuracy': 50.0
        }
        
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as tmp:
            filename = tmp.name
        
        try:
            MapGenerator.create_map(api_result, filename)
            
            # Check that the file was created
            self.assertTrue(os.path.exists(filename))
            
            # Check that the file is not empty
            with open(filename, 'r') as f:
                content = f.read()
                self.assertGreater(len(content), 0)
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_geolocation_api_google(self):
        """Test Google Geolocation API with mock data."""
        # This test will fail if the API key is invalid or if there's no internet connection
        # It's more of an integration test than a unit test
        wifi_data = [
            ('00-11-22-33-44-55', -40),
            ('AA-BB-CC-DD-EE-FF', -50)
        ]
        
        # Skip this test if no API key is provided
        api_key = os.environ.get('GOOGLE_API_KEY')
        if not api_key or api_key == 'YOUR_KEY':
            self.skipTest("No valid Google API key provided")
        
        geolocation = GeolocationAPI(api_key=api_key, provider='google')
        result = geolocation.get_location(wifi_data)
        
        # Check that the result contains the expected fields
        self.assertIn('location', result)
        self.assertIn('accuracy', result)

    def test_wifi_scanner_demo(self):
        """Test WifiScanner with demo data."""
        scanner = WifiScanner(os_type='demo')
        
        # This should raise NotImplementedError for demo OS type
        with self.assertRaises(NotImplementedError):
            scanner.scan()


if __name__ == '__main__':
    unittest.main()