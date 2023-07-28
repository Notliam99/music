from spotdl import Spotdl
from spotdl.utils.config import DOWNLOADER_OPTIONS, get_config

download_options = DOWNLOADER_OPTIONS.copy()
download_options["log_level"] = "debug"
download_options['audio_providers'] = ["youtube-music", "soundcloud"]
download_options['format'] = "flac"
download_options['threads'] = 8

spotdl = Spotdl(
        client_id=get_config()["client_id"], 
        client_secret=get_config()["client_secret"], 
        user_auth=False, 
        downloader_settings=download_options,
        )

songs = spotdl.search(['joji - test drive',
    'https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT'])

results = spotdl.download_songs(songs)
song, path = spotdl.download(songs[0])
