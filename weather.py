import requests
import json

from env import open_weather_api_key, city, weather_units

units = {"metric": "Celsius", "imperial": "Fahrenheit"}[weather_units]


def get_weather_data():
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}"
        .format(city, open_weather_api_key, weather_units))

    print(response)

    if not response.status_code == 200:
        return "I cannot tell the weather at this point of time. Please try again later."
    else:
        data = json.loads(response.content)
        temperature = data["main"]["temp"]

        return "The current temperature is {} degrees {}.".format(
            temperature, units)
