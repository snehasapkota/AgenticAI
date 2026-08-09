from .weather import get_weather

def format_weather(weather):
    if weather is None:
        return "Weather information not available."
    return (
        f"City: {weather['city']}\n"
        f"Temperature: {weather['temperature']}°C\n"
        f"Windspeed: {weather['windspeed']} km/h"
    )