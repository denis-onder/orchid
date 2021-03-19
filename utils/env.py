import os

from dotenv import load_dotenv

load_dotenv()

# --- OPENWEATHER ENVIRONMENTAL VARIABLES --- #
open_weather_api_key = os.getenv("OPEN_WEATHER_API_KEY")
city = os.getenv("CITY")
weather_units = os.getenv("WEATHER_UNITS")

# --- SPOTIFY ENVIRONMENTAL VARIABLES --- #
spotify_api_scope = os.getenv("SPOTIFY_API_SCOPE")
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
spotify_redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")
spotify_username = os.getenv("SPOTIFY_USERNAME")
spotify_device_name = os.getenv("SPOTIFY_DEVICE_NAME")
