from spotdl import Spotdl
from spotdl.utils.config import DOWNLOADER_OPTIONS

download_options = DOWNLOADER_OPTIONS.copy()
download_options["log_level"] = "debug"
download_options['audio_providers'] = ["youtube-music", "soundcloud"]
download_options['format'] = "flac"
download_options['threads'] = 8

spotdl = Spotdl(
        client_id='5f573c9620494bae87890c0f08a60293', 
        client_secret='212476d9b0f3472eaa762d90b19b0ba8', 
        user_auth=False, 
        downloader_settings=download_options
        )
