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
    # print(response.text)
    # print(type(response.text))


    # data = response.json()
    # print(data["results"][0]["latitude"], data["results"][0]["longitude"])
    response.raise_for_status()
    results = response.json().get("results")
    if not results:
        return None
    top = results[0]
    return top["latitude"], top["longitude"], top["name"]

get_coordinates("kathmandu")



def get_weather(city):
    coords = get_coordinates(city)
    if coords is None:
        return None
    lat, long, resolved_name = coords

    response = requests.get(
        FORECAST_URL,
        params={
            "latitude": lat,
            "longitude": long,
            "current_weather": True,
        },
        timeout=10
    )
    response.raise_for_status()
    current = response.json().get("current_weather")

    return{
        
        "city": resolved_name,
        "temperature": current["temperature"],
        "windspeed": current["windspeed"],
    }
print(get_weather("kathmandu"))
