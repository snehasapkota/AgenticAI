from dotenv import load_dotenv
from src.weather import get_coordinates, get_weather
from src.display import format_weather
load_dotenv()  # Load environment variables from .env file

def main():
    print("Welcome to the Weather App!")
    print("Enter a city name to get the current weather information, or type 'exit' to quit.")
    while True:
        city = input("City: ").strip()
        if city.lower() == 'exit':
            print("Exiting the Weather App. Goodbye!")
            break
        if city == "":
            print("Please enter a valid city name.")
            continue

        try:
            weather = get_weather(city)
            print(format_weather(weather), "\n")
        except Exception as e:
            print(f"An error occurred while fetching weather data: {e}\n")

if __name__ == "__main__":
    main()