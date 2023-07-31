import os
import re
import json
from rich.console import Console
from spotdl import Spotdl
from spotdl.utils.config import DOWNLOADER_OPTIONS, get_config
from spotdl.utils.formatter import create_file_name
from spotdl.utils.m3u import create_m3u_file
from spotdl.types.playlist import Playlist

console = Console()

def get_music(json_file_name="music.json"):
    with open(json_file_name) as file:
        file_data = json.load(file)
        return file_data

user_music = dict(get_music())
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

total_songs = list()

for songs in user_music.values():
    total_songs += songs

song_info = spotdl.search(total_songs)

spotdl.download_songs(song_info)

verifyed_files = list()

for playlist_url in user_music["playlists"]:
    playlist = Playlist.from_url(playlist_url)
    verifyed_files.append(f"{playlist.name}.m3u")
    create_m3u_file(
        file_name=f"{playlist.name}.m3u",
        song_list=playlist.songs,
        template=f"A:\\{download_options['output']}",
        file_extension=download_options['format'],
    )

for song in song_info:
    verifyed_files.append(str(
        create_file_name(
            song=song,
            template=download_options['output'],
            file_extension=download_options['format'],
            short=False
        )
    ))

file_in_dir = os.listdir()

music_file_re = re.compile('^.*\.(mp3|flac|ogg|opus|m4a|wav|m3u)$')

file_in_dir = [
        i for i in file_in_dir 
        if bool(music_file_re.search(i)) == True and i not in verifyed_files
    ]

console.clear()

if file_in_dir != []:
    console.print(f"[bold red]DELETING:[/bold red] [i yellow]{file_in_dir}[/i yellow]\n")

for i in file_in_dir:
    os.remove(i)

console.print("[bold green]FINISHED :thumbs_up:[/bold green]")
