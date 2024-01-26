import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

print(api_key)


def get_coordinates(city, state, country, api_key):
    response = requests.get(
        f"https://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&appid={api_key}").json()

    print(response)


# get_coordinates("Lucknow", "UP", "India", api_key)

def get_weather(lat, lon, api_key):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}").json()

    print(response)



