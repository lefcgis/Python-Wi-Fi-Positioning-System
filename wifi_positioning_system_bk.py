#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python Wi-Fi Positioning System - Wi-Fi geolocation script using the Google Maps Geolocation API

@author:     Julien Deudon, Luis Eduardo Ferrer Cruz
@copyright:  Copyright 2017-2026, Julien Deudon, Luis Eduardo Ferrer Cruz
@license:    GNU GPL 3.0
@contact:    initbrain@gmail.com, luis.ferrer.c@uni.pe
"""

import argparse
import json
import os
import re
import sys
import logging
import subprocess
from argparse import RawDescriptionHelpFormatter
import textwrap

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

try:
    import requests
except ImportError:
    print("Error: 'requests' library is required. Install it with: pip install requests")
    exit(1)

try:
    import folium
except ImportError:
    print("Warning: 'folium' library is not installed. Maps will not be generated. Install it with: pip install folium")

try:
    import pywifi
except ImportError:
    pass  # pywifi is only required for Windows

__version__ = "0.2.0"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('wifi_positioning.log')
    ]
)
logger = logging.getLogger(__name__)

# A Google Maps Geolocation API key is required
API_KEY = os.environ.get('GOOGLE_API_KEY') or 'YOUR_KEY'


class WifiScanner:
    """Class to scan Wi-Fi networks."""

    def __init__(self, interface=None, os_type=None):
        self.interface = interface
        self.os_type = os_type

    def scan(self):
        """Scan Wi-Fi networks based on the operating system."""
        if self.os_type == 'linux':
            return self._scan_linux()
        elif self.os_type == 'windows':
            return self._scan_windows()
        elif self.os_type == 'darwin':
            return self._scan_mac()
        elif self.os_type == 'openbsd':
            return self._scan_openbsd()
        else:
            raise NotImplementedError(f"Operating system {self.os_type} is not supported")

    def _scan_linux(self):
        """Scan Wi-Fi networks on Linux using iw."""
        iw_command = f"iw dev {self.interface} scan"
        result = subprocess.run(iw_command.split(), capture_output=True, text=True)

        if result.returncode != 0:
            logger.error(f"Unable to scan for Wi-Fi networks! Command: {iw_command}")
            logger.error(f"Error: {result.stderr}")
            exit(1)

        parsing_result = re.compile(
            r"BSS ([\w\d\:]+).*\n.*\n.*\n.*\n.*\n\tsignal: ([-\d]+)",
            re.MULTILINE
        ).findall(result.stdout)

        wifi_data = [(bss[0].replace(':', '-'), int(bss[1])) for bss in parsing_result]
        return wifi_data

    def _scan_windows(self):
        """Scan Wi-Fi networks on Windows using pywifi."""
        try:
            wifi = pywifi.PyWiFi()
            iface = wifi.interfaces()[0]
            iface.scan()
            results = iface.scan_results()

            wifi_data = []
            for network in results:
                if network.bssid and network.signal:
                    mac = network.bssid.replace(':', '-')
                    wifi_data.append((mac, network.signal))

            return wifi_data
        except Exception as e:
            logger.error(f"Error scanning Wi-Fi networks on Windows: {e}")
            exit(1)

    def _scan_mac(self):
        """Scan Wi-Fi networks on Mac OS X using airport."""
        airport_xml_cmd = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport --scan -x'
        result = subprocess.run(airport_xml_cmd.split(), capture_output=True, text=True)

        if result.returncode != 0:
            logger.error(f"Unable to scan for Wi-Fi networks! Command: {airport_xml_cmd}")
            logger.error(f"Error: {result.stderr}")
            exit(1)

        root = ET.fromstring(result.stdout)
        networks = root.getchildren()[0]
        wifi_data = [(network.find("string").text, abs(int(network.findall("integer")[7].text))) for network in networks]
        return wifi_data

    def _scan_openbsd(self):
        """Scan Wi-Fi networks on OpenBSD using ifconfig."""
        ifconfig_cmd = f'ifconfig {self.interface} scan'
        result = subprocess.run(ifconfig_cmd.split(), capture_output=True, text=True)

        if result.returncode != 0:
            logger.error(f"Unable to scan for Wi-Fi networks! Command: {ifconfig_cmd}")
            logger.error(f"Error: {result.stderr}")
            exit(1)

        parsing_result = re.compile(
            r"nwid\s+[\w-]+\s+chan\s+\d+\s+bssid\s+([\w\d\:]+)\s+([-\d]+)dBm",
            re.MULTILINE
        ).findall(result.stdout)

        wifi_data = [(bss[0].replace(':', '-'), int(bss[1])) for bss in parsing_result]
        return wifi_data


class GeolocationAPI:
    """Class to interact with geolocation APIs."""

    def __init__(self, api_key=None, provider='google'):
        self.api_key = api_key
        self.provider = provider

    def get_location(self, wifi_data):
        """Get location using the selected provider."""
        if self.provider == 'google':
            return self._get_location_google(wifi_data)
        elif self.provider == 'mozilla':
            return self._get_location_mozilla(wifi_data)
        else:
            raise NotImplementedError(f"Provider {self.provider} is not supported")

    def _get_location_google(self, wifi_data):
        """Use Google Geolocation API."""
        url = f"https://geolocation.googleapis.com/v1/geolocate?key={self.api_key}"
        location_request = {
            'considerIp': False,
            'wifiAccessPoints': [
                {"macAddress": mac, "signalStrength": signal}
                for mac, signal in wifi_data
            ]
        }

        try:
            response = requests.post(url, json=location_request, timeout=10)
            response.raise_for_status()
            api_result = response.json()

            if 'location' not in api_result or 'accuracy' not in api_result:
                raise ValueError("Invalid response from Google API")

            return api_result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error connecting to Google API: {e}")
            if "403" in str(e):
                logger.error("Check that your API key is valid and that you have not exceeded the request limit.")
            elif "timeout" in str(e).lower():
                logger.error("Request timed out. Check your internet connection.")
            exit(1)

    def _get_location_mozilla(self, wifi_data):
        """Use Mozilla Location Service API."""
        url = "https://location.services.mozilla.com/v1/geolocate"
        mls_request = {
            "data": {
                "wifi": [
                    {"macAddress": mac, "signalStrength": signal}
                    for mac, signal in wifi_data
                ]
            }
        }

        try:
            response = requests.post(url, json=mls_request, timeout=10)
            response.raise_for_status()
            result = response.json()
            if result is None:
                logger.error("Mozilla API returned no data. Check your request format.")
                return None
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error connecting to Mozilla API: {e}")
            return None


class MapGenerator:
    """Class to generate maps."""

    @staticmethod
    def create_map(api_result, filename='wifi_location.html'):
        """Create an interactive map using Folium."""
        try:
            lat = api_result['location']['lat']
            lng = api_result['location']['lng']
            accuracy = api_result['accuracy']

            m = folium.Map(location=[lat, lng], zoom_start=18)

            folium.Circle(
                radius=accuracy,
                location=[lat, lng],
                color='blue',
                fill=True,
                fill_color='blue',
                fill_opacity=0.3,
                popup=f"Accuracy: {accuracy} meters"
            ).add_to(m)

            folium.Marker(
                location=[lat, lng],
                popup=f"Latitude: {lat}, Longitude: {lng}"
            ).add_to(m)

            m.save(filename)
            logger.info(f"Map saved to {filename}")
        except Exception as e:
            logger.error(f"Error generating map: {e}")


def prettify_json(json_data, prettify=False):
    """Format JSON data for printing."""
    if prettify:
        return '\n'.join([l.rstrip() for l in json.dumps(json_data, sort_keys=True, indent=4*' ').splitlines()])
    else:
        return json.dumps(json_data)


def get_scriptpath():
    """Get the directory of the current script."""
    pathname = os.path.dirname(sys.argv[0])
    fullpath = os.path.abspath(pathname)
    if not fullpath.endswith('/'):
        fullpath += '/'
    return fullpath


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f'Error: {message}\n\n')
        self.print_usage()
        sys.exit(2)


def get_arguments(argv=None):
    """Parse command line arguments."""
    if argv is not None:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = f'v{__version__}'
    program_version_message = f'{program_name} {program_version}'
    program_shortdesc = __doc__.split("\n")[1] if __doc__ else "Python Wi-Fi Positioning System"
    program_copyright = 'Copyright (c) 2017-2026 Julien Deudon, Luis Eduardo Ferrer Cruz'

    program_license = f'''
{program_shortdesc}
{program_copyright}

Licensed under the GNU General Public License, version 3.0

This program comes with ABSOLUTELY NO WARRANTY; for details use '-L' or '--license'.
This is free software, and you are welcome to redistribute it under certain conditions.
'''

    detailed_license = f'''{program_shortdesc}
{program_copyright}

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Contact: initbrain@gmail.com, luis.ferrer.c@uni.pe'''

    parser = MyParser(
        description=program_license,
        formatter_class=RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
            additional informations:
              ROADMAP   displays the default road map view
              SATELLITE displays Google Earth satellite images
              HYBRID    displays a mixture of normal and satellite views
                        (this is the default map type)
              TERRAIN   displays a physical map based on terrain information''')
    )

    parser.add_argument('-V', '--version', action='version', version=program_version_message)
    parser.add_argument('-L', '--license', action='version', version=detailed_license,
                        help="show program's license details and exit")
    parser.add_argument('-v', '--verbose', action="store_true",
                        help='enable verbose messages',
                        default=False)
    parser.add_argument('-k', '--api-key', action="store", dest="api_key",
                        help='Google Maps Geolocation API key (could be hardcoded)',
                        default=None)
    parser.add_argument('-p', '--json-prettify', action="store_true",
                        help='prettify JSON output',
                        default=False)
    parser.add_argument('-o', '--with-overview', action="store_true",
                        help='generate an interactive map file',
                        default=False)
    parser.add_argument('-m', '--map-type', choices=['ROADMAP', 'SATELLITE', 'HYBRID', 'TERRAIN'],
                        help='map type for the overview file',
                        default='HYBRID')
    parser.add_argument('--api-provider', choices=['google', 'mozilla'], default='google',
                        help='geolocation API provider (google or mozilla)')

    # Windows mode
    if sys.platform == 'win32':
        parser.add_argument('--demo', action="store_true", help='demo mode - West Norwood (London)', default=False)
    else:
        required_parser = parser.add_argument_group('required arguments')
        required_parser = required_parser.add_mutually_exclusive_group(required=True)
        required_parser.add_argument('-i', action="store", dest="wifi_interface", help='specify Wi-Fi scan interface')
        required_parser.add_argument('--demo', action="store_true", help='demo mode - West Norwood (London)', default=False)

    return parser.parse_args()


def main():
    global args
    args = get_arguments()

    # Set API key
    if args.api_key:
        global API_KEY
        API_KEY = args.api_key

    # Solo validar la clave API si el proveedor es Google
    if args.api_provider == 'google' and (not API_KEY or API_KEY == 'YOUR_KEY'):
        logger.error("A Google Maps Geolocation API key is required. Get yours at: https://developers.google.com/maps/documentation/geolocation/intro")
        exit(1)

    # Demo mode
    if args.demo:
        logger.info("Using demo mode with sample data")
        try:
            with open('demo_data.json', 'r') as f:
                demo_data = json.load(f)
            wifi_data = [(ap['macAddress'], ap['signalStrength']) for ap in demo_data['wifiAccessPoints']]
        except FileNotFoundError:
            logger.warning("demo_data.json not found. Using default demo data.")
            wifi_data = [
                ('00-1f-f4-25-ee-30', -40),
                ('02-fe-f4-25-ee-30', -44),
                ('12-fe-f4-25-ee-30', -44),
                ('00-26-5a-7e-0d-02', -60),
                ('90-01-3b-30-04-29', -60),
                ('2c-b0-5d-bd-db-4a', -50)
            ]
    else:
        # Determine OS type
        if sys.platform == 'win32':
            os_type = 'windows'
        elif sys.platform.startswith('linux'):
            os_type = 'linux'
        elif sys.platform == 'darwin':
            os_type = 'darwin'
        elif sys.platform.startswith('openbsd'):
            os_type = 'openbsd'
        else:
            logger.error(f"Unsupported operating system: {sys.platform}")
            exit(1)

        # Scan Wi-Fi networks
        scanner = WifiScanner(interface=args.wifi_interface if hasattr(args, 'wifi_interface') else None, os_type=os_type)
        wifi_data = scanner.scan()

    # Get location using the selected API provider
    geolocation = GeolocationAPI(api_key=API_KEY, provider=args.api_provider)
    api_result = geolocation.get_location(wifi_data)

    # Print results
    if api_result is not None:
        logger.info("Geolocation result:")
        print(prettify_json(api_result, args.json_prettify))

        # Generate map if requested
        if args.with_overview:
            MapGenerator.create_map(api_result)

        # Print Google Maps link
        if 'location' in api_result:
            logger.info(f"Google Maps link: https://www.google.com/maps?q={api_result['location']['lat']},{api_result['location']['lng']}")
    else:
         logger.error("No geolocation data was returned. Check your API provider and connection.")


if __name__ == "__main__":
    main()
