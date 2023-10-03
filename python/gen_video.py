import subprocess
import shlex

# Paths to input files
VIDEO_FILE = "assets/video/stardust.mp4"
AUDIO_FILE = "assets/audio/livestream.mp3"
VIDEO_IMAGE = "assets/title.png"
OUTFILE = "test.mp4"
TMPFILE = "tmp.jpg"
FONT = "assets/DancingScript-Regular.ttf"

def run_ffmpeg_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def execute_ffprobe(command):
    process = subprocess.Popen(
        shlex.split(command),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error: {stderr}")
        return None
    return stdout.strip()

def get_tag(tag, fname):
    command = [
        'ffprobe',
        '-loglevel', 'quiet',
        '-show_entries', f'format_tags={tag}',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        fname
    ]
    return execute_ffprobe(' '.join(command))

def get_attr(tag, fname):
    command = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', f'format={tag}',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        fname
    ]
    return execute_ffprobe(' '.join(command))

def get_stream_tag(tag, fname):
    command = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', f'stream={tag}',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        fname
    ]
    return execute_ffprobe(' '.join(command))

def save_cover_image(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-an', '-vcodec', 'copy',
        output_file
    ]
    run_ffmpeg_command(' '.join(command))

artist = get_tag("artist", AUDIO_FILE)
album = get_tag("album", AUDIO_FILE)
title = get_tag("title", AUDIO_FILE)
audio_duration = get_attr("duration", AUDIO_FILE)
video_duration = get_stream_tag("duration", VIDEO_FILE)

print(f"Artist: {artist} TITLE: {title} Album: {album} Duration: {audio_duration}")
print(f"Video Duration: {video_duration}")

# Save the cover image (not included in your original script)
# save_cover_image(AUDIO_FILE, TMPFILE)

ffmpeg_command = [
    'ffmpeg',
    '-i', VIDEO_FILE,
    '-i', AUDIO_FILE,
    '-c:v', 'libx264',
    '-tune', 'stillimage',
    '-c:a', 'aac',
    '-b:a', '192k',
    '-pix_fmt', 'yuv420p',
    '-shortest',
    OUTFILE,
    '-i', TMPFILE,
    '-filter_complex',
    f'[1:v]scale=-1:200 [ovrl], '
    f'[0:v][ovrl]overlay=(main_w-overlay_w)-5:(main_h-overlay_h)-100, '
    f'drawtext=fontfile={FONT}:text=\'{artist}\':x=(w-text_w)-220:y=(h-text_h)-200:fontsize=50:fontcolor=white, '
    f'drawtext=fontfile={FONT}:text=\'{title}\':x=(w-text_w)-220:y=(h-text_h)-150:fontsize=50:fontcolor=white'
]

run_ffmpeg_command(' '.join(ffmpeg_command))

