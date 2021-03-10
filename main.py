from gtts import gTTS
import speech_recognition as sr
import os

import weather

r = sr.Recognizer()
muted_testing = None


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
        play_sound_file("hello")

    elif text.__contains__("tell me the weather"):
        weather_report = weather.get_weather_data()
        report_file = create_sound_file(weather_report, "weather_report")
        play_sound_file(report_file)


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
    muted_testing = True  # or False if not testing manually

    if muted_testing:
        # !MUTED TESTING
        handle_speech("tell me the weather")
    else:
        handle_speech_input()
