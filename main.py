from spotdl import Spotdl
from spotdl.utils.config import DOWNLOADER_OPTIONS, get_config
from spotdl.utils.formatter import create_file_name

user_config = get_config()

download_options = DOWNLOADER_OPTIONS.copy()
download_options["log_level"] = "debug"
download_options['audio_providers'] = ["youtube-music", "soundcloud"]
download_options['lyrics_providers'] = user_config['lyrics_providers']
download_options['format'] = "flac"
download_options['threads'] = 8

spotdl = Spotdl(
        client_id=user_config["client_id"], 
        client_secret=user_config["client_secret"], 
        user_auth=False, 
        downloader_settings=download_options,
        )

songs = spotdl.search(['joji - test drive',
    'https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT'])

results = spotdl.download_songs(songs)

song_file_names = list()
for song in songs:
    song_file_names.append(
        str(create_file_name(
            song=song,
            template=download_options['output'],
            file_extension=download_options['format'],
            short=False
        ))
    )

print(song_file_names)
