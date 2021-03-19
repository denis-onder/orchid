from gtts import gTTS
import speech_recognition as sr
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

import os

import weather
import music
import env

r = sr.Recognizer()
muted_testing = None

auth_manager = SpotifyOAuth(client_id=env.spotify_client_id,
                            client_secret=env.spotify_client_secret,
                            redirect_uri=env.spotify_redirect_uri,
                            scope=env.spotify_api_scope,
                            username=env.spotify_username)

spotify = Spotify(auth_manager=auth_manager)

devices = spotify.devices()

device_id = None
for d in devices['devices']:
    d['name'] = d['name'].replace('’', '\'')
    if d['name'] == env.spotify_device_name:
        device_id = d['id']
        break


def create_sound_file(text, file_name):
    tts = gTTS(text)
    tts.save(file_name)

    return file_name


def play_sound_file(file_name):
    # Check if the sound file exists
    if os.path.exists(file_name):
        # Play the file and delete it afterwards
        command = "mpg321 {file_name}"
        os.system(command.format(file_name=file_name))

        if not file_name == "hello":
            os.remove(file_name)


def handle_speech(result):
    text = result.lower().strip()

    if text.__contains__("orchid"):
        hello = create_sound_file("Hello", "hello")
        play_sound_file(hello)

    elif text.__contains__("tell me the weather"):
        notifier = create_sound_file("Getting the weather data.",
                                     "weather_notifier")
        play_sound_file(notifier)
        weather_report = weather.get_weather_data()
        report_file = create_sound_file(weather_report, "weather_report")
        play_sound_file(report_file)

    elif text.__contains__("play"):
        command_fragments = text.split("play ")
        track_uri = music.get_track_uri(command_fragments[1])
        music.play_track(track_uri)


def handle_speech_input():
    with sr.Microphone() as source:
        print("Talk")
        text = r.listen(source)

        try:
            result = r.recognize_google(text)
            print("Text: " + result)
            handle_speech(result)

        except:
            print("Talk again")
            handle_speech_input()


if __name__ == "__main__":
    muted_testing = False  # or False if not testing manually

    if muted_testing:
        # !MUTED TESTING
        handle_speech("play")
    else:
        handle_speech_input()
