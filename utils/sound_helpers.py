import os

from gtts import gTTS


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