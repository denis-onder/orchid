from gtts import gTTS
import speech_recognition as sr
import os
import vlc
import pafy
import random

r = sr.Recognizer()
muted_testing = None


def generate_random_file_name():
    random_string = ''

    for _ in range(10):
        # Considering only upper and lowercase letters
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        # Convert to lowercase if the flip bit is on
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
        # Keep appending random characters using chr(x)
        random_string += (chr(random_integer))

        return random_string


def get_youtube_play_url(url):
    video = pafy.new(url)
    metadata = video.getbest()
    return metadata.url


def create_media_player(play_url):
    instance = vlc.Instance()
    media = instance.media_new(play_url)
    player = instance.media_player_new()

    # Instanciate MRL
    media.get_mrl()
    player.set_media(media)

    # Return the player
    return player


def create_sound_file(text, file_name):
    tts = gTTS(text)
    tts.save(file_name)


def play_sound_file(file_name):
    # Check if the sound file exists
    if os.path.exists(file_name + ".mp3"):
        # Play the file and delete it afterwards
        command = "mpg321 {file_name}.mp3"
        os.system(command.format(file_name=file_name))


def download_mp3_from_youtube(url):
    file_name = generate_random_file_name()
    command = "youtube-dl -o \"{file_name}.mp3\" -x --audio-format mp3 {url}"
    formatted_command = command.format(file_name=file_name, url=url)
    os.system(formatted_command)

    return file_name


def handle_speech(result):
    text = result.lower().strip()
    if text.__contains__("orchid"):
        play_sound_file("hello")
        if not muted_testing:
            handle_speech_input()
    elif text.__contains__("motorhead"):
        url = "https://www.youtube.com/watch?v=hF9Gr5waAJg"
        # play_url = get_youtube_play_url(url)
        # player = create_media_player(play_url)

        create_sound_file("Playing Motorhead", "motorhead")
        play_sound_file("motorhead")
        # player.play()
        file_name = download_mp3_from_youtube(url)
        play_sound_file(file_name)


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
        handle_speech("orchid")
    else:
        handle_speech_input()
