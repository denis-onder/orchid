import speech_recognition as sr

from commands import music, weather, hello, stop

r = sr.Recognizer()
muted_testing = None


def handle_speech(result):
    text = result.lower().strip()

    if text.__contains__("orchid"):
        hello.say_hello()

    elif text.__contains__("tell me the weather"):
        weather.get_weather_data()

    elif text.__contains__("play"):
        music.play_track(text.split("play ")[1])

    elif text.__contains__("pause"):
        music.pause_playback()

    elif text.__contains__("resume"):
        music.resume_playback()

    elif text.__contains__("stop"):
        stop.stop_orchid()


def handle_speech_input():
    with sr.Microphone() as source:
        print("Talk")
        text = r.listen(source)

        try:
            result = r.recognize_google(text)
            print("Text: " + result)
            handle_speech(result)
            handle_speech_input()

        except:
            print("Talk again")
            handle_speech_input()


if __name__ == "__main__":
    muted_testing = False  # or False if not testing manually

    if muted_testing:
        # !MUTED TESTING
        handle_speech("Orchid")
    else:
        handle_speech_input()
