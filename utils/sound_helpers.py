import os

from gtts import gTTS


def create_sound_file(text, file_name):
    tts = gTTS(text)
    tts.save("{}.mp3".format(file_name))

    return file_name


def play_sound_file(file_name):
    file_name += ".mp3"
    # Check if the sound file exists
    if os.path.exists(file_name):
        # Play the file and delete it afterwards
        command = "mpg321 {}".format(file_name)
        os.system(command)

        # Delete the file afterwards
        os.remove(file_name)