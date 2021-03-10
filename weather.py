import requests
import json

from env import open_weather_api_key, city


def get_weather_data():
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
        .format(city, open_weather_api_key))

    print(response)

    if not response.status_code == 200:
        return "I cannot tell the weather at this point of time. Please try again later."
    else:
        data = json.loads(response.content)
        temperature = data["main"]["temp"]

        return "The current temperature is {} degrees Celsius.".format(
            temperature)
