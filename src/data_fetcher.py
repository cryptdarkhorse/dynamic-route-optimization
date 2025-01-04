import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Fetch API keys from environment variables
TOMTOM_API_KEY = os.getenv('TOMTOM_API_KEY')
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
AQICN_API_KEY = os.getenv('AQICN_API_KEY')

# Function to fetch real-time traffic data
def get_traffic_data(origin, destination):
    url = f'https://api.tomtom.com/traffic/services/4/incidentDetails?bbox={origin},{destination}&key={TOMTOM_API_KEY}'
    response = requests.get(url)
    return response.json()

# Function to fetch weather data
def get_weather_data(origin, destination):
    # Call to AQICN for air quality data as an example
    url = f'http://api.waqi.info/feed/{origin}/?token={AQICN_API_KEY}'
    response = requests.get(url)
    return response.json()
