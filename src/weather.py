import os
import requests

API_KEY = os.getenv("WEATHER_API_KEY", "")

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


def get_coordinates(city):
    """Turn city name into latitude, longitude, resolved name.
    return none if the city cannot be found.
    """
    response = requests.get(GEOCODE_URL, params={"name": city, "count": 1}, timeout=10)
    data = response.json()
    print(data["results"][0]["latitude"], data["results"][0]["longitude"])
    # response.raise_for_status()
    # results = response.json().get("results")
    # if not results:
    #     return None
    # result = results[0]
    # return result["latitude"], result["longitude"], result["name"]


get_coordinates(city="New York")