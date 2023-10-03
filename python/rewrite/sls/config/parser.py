
import argparse
from configparser import ConfigParser

def parse_args():
    parser = argparse.ArgumentParser(description="Simple Live Stream Configuration")

    parser.add_argument("-c", "--config", metavar="CONFIG_FILE", default="config/general.ini",
                        help="Specify an alternate configuration file.")
    parser.add_argument("-p", "--playlist", metavar="PLAYLIST_FILE",
                        help="Provide a file playlist.")
    parser.add_argument("-t", "--target", metavar="TARGET", choices=["youtube", "twitch", "all"],
                        default="all", help="Provide a target platform (youtube, twitch, or all).")
    parser.add_argument("-v", "--video", metavar="VIDEO_FILE",
                        help="Provide a video file for background.")
    parser.add_argument("-i", "--image", metavar="IMG_FILE",
                        help="Provide an image for the background (preferably transparent PNG).")
    parser.add_argument("-o", "--overlay", metavar="OVERLAY_IMAGE",
                        help="Provide an image to overlay on the video.")
    parser.add_argument("-d", "--directory", metavar="AUDIO_DIR",
                        help="Provide a directory to play all audio files in.")
    parser.add_argument("-l", "--loop", action="store_true",
                        help="Enable looping (default: True).")

    return parser.parse_args()

def load_config(args):
    config = ConfigParser()
    config.read(args.config)

    if args.playlist:
        config['General']['audio_input'] = 'PLAYLIST'
        config['General']['audio_files'] = args.playlist
    if args.target:
        config['General']['targets'] = args.target
    if args.video:
        config['General']['video'] = args.video
    if args.image:
        config['General']['image'] = args.image
    if args.overlay:
        config['General']['overlay'] = args.overlay
    if args.directory:
        config['General']['audio_input'] = 'DIR'
        config['General']['audio_directory'] = args.directory
    if not args.loop:
        config['General']['do_loop'] = 'NO'

    return config

if __name__ == "__main__":
    args = parse_args()
    config = load_config(args)


