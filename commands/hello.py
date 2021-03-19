from utils import sound_helpers


def say_hello():
    hello = sound_helpers.create_sound_file("Hello", "hello")
    sound_helpers.play_sound_file(hello)
