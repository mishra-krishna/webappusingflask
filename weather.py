import requests
import json
import os
from dotenv import load_dotenv
from dataclasses import dataclass

@dataclass
class WeatherData:
    temp: str
    icon: str
    description: str
    feels_like: str
    humidity: str


load_dotenv()
api_key = os.getenv("API_KEY")

# print(api_key)


def get_coordinates(city, state, country, api_key):
    response = requests.get(
        f"https://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&appid={api_key}&units=metric").json()
    lat = response[0]["lat"]
    lon = response[0]["lon"]
    return lat, lon


# Get coordinates and store the values in lat and lon
# lat, lon = get_coordinates("Lucknow", "UP", "India", api_key)

def get_weather(lat, lon, api_key):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric").json()

    temp = 'Current temperature: '+str(response["main"]["temp"])+"°C"
    icon = response["weather"][0]["icon"]
    description = response["weather"][0]["description"]
    feels_like = 'Feels Like: ' + str(response["main"]["feels_like"])+"°C"
    humidity = "Humidity: " + str(response["main"]["humidity"])+"%"
    data = WeatherData(temp, icon, description, feels_like, humidity)
    # print(temp, icon, description, feels_like, humidity)
    return data


def get_weather_by_city(city, state, country, api_key):
    lat, lon = get_coordinates(city, state, country, api_key)
    weather_data = get_weather(lat, lon, api_key)
    return weather_data


if __name__ == '__main__':
    lat, lon = get_coordinates("Lucknow", "UP", "India", api_key)
    print(get_weather(lat, lon, api_key))


