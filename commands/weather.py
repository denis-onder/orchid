import requests
import json

from env import open_weather_api_key, city, weather_units
from utils import sound_helpers

units = {"metric": "Celsius", "imperial": "Fahrenheit"}[weather_units]


def get_weather_data():
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}"
        .format(city, open_weather_api_key, weather_units))

    print(response)

    notifier = sound_helpers.create_sound_file("Getting the weather data.",
                                               "weather_notifier")
    sound_helpers.play_sound_file(notifier)

    message = None

    if not response.status_code == 200:
        message = "I cannot tell the weather at this point of time. Please try again later."
    else:
        data = json.loads(response.content)
        temperature = data["main"]["temp"]

        message = "The current temperature is {} degrees {}.".format(
            temperature, units)

    report_file = sound_helpers.create_sound_file(message, "weather_report")
    sound_helpers.play_sound_file(report_file)
