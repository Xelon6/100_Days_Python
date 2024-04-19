import os
import requests
import json

# Constants
API_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT = 5
TIMEZONE = "CET"
LATITUDE = 47.800588
LONGITUDE = 16.280365

def get_weather_forecast():
    try:
        result = requests.get(f"{API_URL}?latitude={LATITUDE}&longitude={LONGITUDE}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={TIMEZONE.upper()}", timeout=TIMEOUT)
        result.raise_for_status()  # Raise an exception for bad status codes
        return result.json()
    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return None

def get_weather_description(weather_code, weather_codes):
    try:
        return weather_codes[str(weather_code)]
    except KeyError:
        return "Unknown"

def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # Load weather codes
    try:
        with open("weather_codes.json", "r", encoding="UTF-8") as f:
            weather_codes = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("Error loading weather codes")
        return

    # Get weather forecast
    weather_data = get_weather_forecast()
    if weather_data is None:
        return

    # Extract relevant information
    today = weather_data["daily"]["time"][0]
    weather_code = weather_data["daily"]["weathercode"][0]
    max_temp = weather_data["daily"]["temperature_2m_max"][0]
    min_temp = weather_data["daily"]["temperature_2m_min"][0]

    # Get weather description
    weather_description = get_weather_description(weather_code, weather_codes)

    # Print weather forecast
    print(f"This is the Weather Forecast for: {today}\n{weather_description}\nMax Temp.: {max_temp}°C\nMin Temp.: {min_temp}°C")

if __name__ == "__main__":
    main()
