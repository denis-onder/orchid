from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

from utils import env

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

selected_track = None


class InvalidSearchError(Exception):
    pass


def get_track_uri(name):
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='track')
    if not results['tracks']['items']:
        raise InvalidSearchError(f'No track named "{original}"')

    track_uri = results['tracks']['items'][0]['uri']
    return track_uri


def play_track(song_name):
    uri = get_track_uri(song_name)
    spotify.start_playback(device_id=device_id, uris=[uri])


def pause_playback():
    spotify.pause_playback(device_id)


def resume_playback():
    spotify.start_playback(device_id=device_id, uris=[selected_track])