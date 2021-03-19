from main import spotify, device_id


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


def play_track(uri):
    spotify.start_playback(device_id=device_id, uris=[uri])