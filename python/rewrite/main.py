import argparse
import configparser
from sls.parser.command_line_parser import parse_command_line_args
from sls.config.config_loader import load_configuration
from sls.stream.ffmpeg_streamer import FFmpegStreamer

def main():
    # Parse command-line arguments
    args = parse_command_line_args()

    # Load configuration
    config = load_configuration(args)

    # Create an instance of FFmpegStreamer
    ffmpeg_streamer = FFmpegStreamer(config)

    # Start the stream
    ffmpeg_streamer.start_stream()

if __name__ == "__main__":
    main()

