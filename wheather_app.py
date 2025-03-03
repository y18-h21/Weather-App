import requests
import json

def get_weather(api_key, location):
    """
    Fetches and displays weather information for a given location.

    Args:
        api_key (str): Your OpenWeatherMap API key.
        location (str): The location to get weather for (e.g., "London", "New York").
    """

    base_url = "http://api.openweathermap.org/data/2.5/weather?q=Bengaluru,India&APPID=a9683b35dd79c621120a32eb0ec32d40"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        weather_data = response.json()

        # Extract relevant information
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        description = weather_data["weather"][0]["description"]

        print(f"Weather for {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description.capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError:
        print("Error: Could not parse weather data. Please check the location or API key.")

if __name__ == "__main__":
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key
    location = input("Enter location (city, country): ")

    get_weather(api_key, location)