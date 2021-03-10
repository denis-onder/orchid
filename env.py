import os

from dotenv import load_dotenv

load_dotenv()

open_weather_api_key = os.getenv("OPEN_WEATHER_API_KEY")
city = os.getenv("CITY")