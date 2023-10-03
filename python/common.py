import argparse
import subprocess
import os
import time

# Define a dictionary for configuration variables
config = {
    "CONF_FILE": "config.sh",
    "VIDEO_INPUT": "DEFAULT_VIDEO_INPUT",
    "VIDEO_IMAGE": "DEFAULT_WATERMARK",
    "AUDIO_INPUT": "DEFAULT_AUDIO_INPUT",
    "AUDIO_DIRECTORY": "DEFAULT_AUDIO_DIRECTORY",
    "DO_LOOP": "NO",
    "VIDEO_OVERLAY": "DEFAULT_VIDEO_OVERLAY",
    "TARGET": "youtube",
    "AUDIO_FILES": "DEFAULT_AUDIO_FILES",
    "VIDEO_SOURCE": "DEFAULT_VIDEO_SOURCE",
    "FULLVIDEO_SOURCE": "DEFAULT_FULLVIDEO_SOURCE",
    "SINGLE_AUDIO_FILE": "DEFAULT_SINGLE_AUDIO_FILE",
    "LOGFILE": "logfile.txt",
    "SECONDS": 0,
}

# Function to load alternate config
def load_alternate_config(conf_file):
    global config
    with open(conf_file, "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            config[key] = value

# Function to convert seconds to HH:MM:SS format
def convertsecs(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# Function to log stream information
def log_stream():
    global config
    seconds = config["SECONDS"]
    duration = seconds // 60
    hrs = seconds // 3600
    mins = (seconds - hrs * 3600) // 60
    seconds = seconds - hrs * 3600 - mins * 60
    end_time = time.strftime("%Y/%m/%d %H:%M")
    log_entry = (
        f"Start: {config['START']} - End: {end_time} Duration: {duration} - Playlist: {config['AUDIO_FILES']} - "
        f"VIDEO: {config['VIDEO_SOURCE']} - Target: {config['TARGET']}\n"
    )
    with open(config["LOGFILE"], "a") as log_file:
        log_file.write(log_entry)
    print(
        f"Start: {config['START']} - End: {end_time} Duration: {hrs:02}:{mins:02}:{seconds:02} - "
        f"Playlist: {config['AUDIO_FILES']} - VIDEO: {config['VIDEO_SOURCE']} - Target: {config['TARGET']}"
    )

# Function to display manpage
def manpage():
    print("Stream Scripts")
    print("-l [YES|NO]    optional argument to loop. NO will break on failure, other values will loop")
    print("-p [playlist]  provide a file playlist")
    print("-t [target]    provide a target - youtube or twitch")
    print("-v [video]     provide a video file for background")

# Create the main parser
parser = argparse.ArgumentParser(description="Stream Scripts")

# Create subparsers for main commands
subparsers = parser.add_subparsers(title="Available Commands", dest="command")

# Create subparser for "config" command
config_parser = subparsers.add_parser("config", help="Load alternate config")
config_parser.add_argument("-c", metavar="CONF_FILE", type=str, default="config.sh", help="Load alternate config file")

# Create subparser for "set" command
set_parser = subparsers.add_parser("set", help="Set configuration options")

# Create sub-subparsers for "set" subcommand
set_subparsers = set_parser.add_subparsers(title="Available Options", dest="option")

# Subparser for "static" option
static_parser = set_subparsers.add_parser("static", help="Set static image stream")
static_parser.add_argument("-s", metavar="VIDEO_IMAGE", type=str, required=True, help="Static image file")

# Subparser for "directory" option
directory_parser = set_subparsers.add_parser("directory", help="Set directory stream")
directory_parser.add_argument("-d", metavar="AUDIO_DIRECTORY", type=str, required=True, help="Audio directory")

# Subparser for "overlay" option
overlay_parser = set_subparsers.add_parser("overlay", help="Add overlay")
overlay_parser.add_argument("-o", metavar="VIDEO_OVERLAY", type=str, required=True, help="Overlay file")

# Subparser for "target" option
target_parser = set_subparsers.add_parser("target", help="Set target")
target_parser.add_argument("-t", metavar="TARGET", type=str, required=True, help="Streaming target")

# Subparser for "playlist" option
playlist_parser = set_subparsers.add_parser("playlist", help="Set playlist")
playlist_parser.add_argument("-p", metavar="AUDIO_FILES", type=str, required=True, help="Audio files playlist")

# Subparser for "video" option
video_parser = set_subparsers.add_parser("video", help="Set video source")
video_parser.add_argument("-v", metavar="VIDEO_SOURCE", type=str, required=True, help="Video source file")

# Parse the command-line arguments
args = parser.parse_args()

# Update configuration variables based on command-line arguments
if args.command == "config":
    config["CONF_FILE"] = args.c
    load_alternate_config(config["CONF_FILE"])
elif args.command == "set":
    if args.option == "static":
        config["VIDEO_INPUT"] = "STATIC"
        config["VIDEO_IMAGE"] = args.s
    elif args.option == "directory":
        config["AUDIO_INPUT"] = "DIRECTORY"
        config["AUDIO_DIRECTORY"] = args.d
    elif args.option == "overlay":
        config["VIDEO_INPUT"] = "MOVIE"
        config["VIDEO_OVERLAY"] = args.o
    elif args.option == "target":
        config["TARGET"] = args.t
    elif args.option == "playlist":
        config["AUDIO_FILES"] = args.p
    elif args.option == "video":
        config["VIDEO_SOURCE"] = args.v

# Access configuration variables using the config dictionary
print(f"VIDEO_INPUT: {config['VIDEO_INPUT']}")
print(f"VIDEO_IMAGE: {config['VIDEO_IMAGE']}")
# ... (access other configuration variables as needed)

