#!/usr/bin/env python3

import os
import subprocess
import sys
from sls.stream.ffmpeg import FFmpegStreamer
from sls.config.parser import parse_args, load_config

def main():
    # Parse command-line arguments
    args = parse_args()
    print (args)
    sys.exit()
    # Load and merge configuration
    config = load_config(args)

    # Create an instance of the FFmpegStreamer
    streamer = FFmpegStreamer(config)

    try:
        # Start the stream
        streamer.start_stream()
    except KeyboardInterrupt:
        print("Streaming stopped by user.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Cleanup and stop the streamer
        streamer.stop_stream()

if __name__ == "__main__":
    main()

