import os
import subprocess
import argparse
from common import config

# Define FFmpeg source and audio input options based on your cases
def get_source_options():
    if config['VIDEO_INPUT'] == "STATIC":
        return ["-loop", "1", "-framerate", "10", "-re", "-i", config['VIDEO_IMAGE']]
    else:
        return ["-i", config['VIDEO_SOURCE']]

def get_audio_options():
    if config['AUDIO_INPUT'] == "DIR":
        print("Error, Not Supported yet, use PLAYLIST")
        exit(2)
    elif config['AUDIO_INPUT'] == "FILE":
        return ["-i", config['SINGLE_AUDIO_FILE']]
    else:
        return ["-f", "concat", "-i", config['AUDIO_FILES']]

def get_overlay_options():
    if config['VIDEO_OVERLAY']:
        return ["-i", config['VIDEO_OVERLAY'], "-filter_complex", "overlay=0:0:format=yuv444"]
    else:
        return []

def main(args):
    # Define the streaming URL if needed
    # stream_url = ["-tee", f"{config['YOUTUBE_URL']}/{config['YOUTUBE_KEY']}|{config['TWITCH_URL']}/{config['TWITCH_KEY']}"]
    stream_url = []

    # Loop indefinitely (or break based on your DO_LOOP variable)
    while True:
        source_str = get_source_options()
        audio_str = get_audio_options()
        overlay_str = get_overlay_options()

        ffmpeg_command = [
            "ffmpeg",
            "-stream_loop", "-1",
            "-re",
            *source_str,
            "-thread_queue_size", "512",
            "-stream_loop", "-1",
            "-re",
            *audio_str,
            "-map", "0:v:0", "-map", "1:a:0",
            "-map_metadata:g", "1:g",
            "-attempt_recovery", "1", "-max_recovery_attempts", "5", "-drop_pkts_on_overflow", "1",
            "-c:v", "libx264", "-preset", config['QUAL'], "-r", str(config['FPS']), "-g", str(config['FPS'] * 2), "-b:v", config['VBR'],
            "-bufsize", "3000k", "-maxrate", config['VBR'],
            "-c:a", config['AUDIO_ENCODER'], "-ar", "44100", "-b:a", "128k", "-pix_fmt", "yuv420p",
            "-f", "flv",
            *stream_url,
            *overlay_str,
        ]

        # Run the FFmpeg command
        subprocess.run(ffmpeg_command)

        END = subprocess.check_output("date +'%Y/%M/%D %H:%M'", shell=True).decode().strip()
        secs = 0  # Calculate SECONDS as needed

        # Log stream information

        if config['DO_LOOP'] != "YES":
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stream video using FFmpeg.")
    # Add any additional subparser arguments here if needed

    args = parser.parse_args()
    main(args)

