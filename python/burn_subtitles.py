import subprocess
import sys

def burn_subtitles(input_video, subtitles, output_video):
    style = (
        ":force_style=Alignment=0,OutlineColour=&H100000000,BorderStyle=3,Outline=1,Shadow=0,Fontsize=12,MarginL=305,MarginV=25"
    )
    # FFmpeg command to burn subtitles
    cmd = [
        "ffmpeg",
        "-i",
        input_video,
        "-lavfi",
        f"subtitles={subtitles}{style}",
        "-crf",
        "1",
        "-c:a",
        "copy",
        output_video,
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"Subtitles burned successfully to {output_video}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error: script needs 3 parameters: input_video, subtitles, output_video")
        print("Usage: python mk_video.py [input_video] [subtitles] [output_video]")
        sys.exit(1)

    input_video = sys.argv[1]
    subtitles = sys.argv[2]
    output_video = sys.argv[3]

    burn_subtitles(input_video, subtitles, output_video)

