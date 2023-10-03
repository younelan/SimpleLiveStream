import subprocess
import os
import re

class FFmpegStreamer:
    def __init__(self, config):
        self.config = config

    def construct_ffmpeg_command(self):
        # Get the target platforms from the configuration
        targets = self.config['General']['targets'].split(',')

        # Construct the FFmpeg command based on your configuration
        command = [
            'ffmpeg',
            '-stream_loop', '-1',  # Loop indefinitely
            '-re',  # Read input at native frame rate
        ]

        # Add input options
        command.extend(['-i', self.config['General']['video']])
        command.extend(['-thread_queue_size', '512'])
        command.extend(['-stream_loop', '-1'])  # Loop indefinitely
        command.extend(['-re'])  # Read input at native frame rate

        # Add audio input options
        if self.config['General']['audio_input'] == 'FILE':
            command.extend(['-i', self.config['General']['single_audio_file']])
        elif self.config['General']['audio_input'] == 'PLAYLIST':
            command.extend(['-f', 'concat', '-i', self.config['General']['audio_files']])

        # Add video and audio encoding options
        command.extend(['-c:v', 'libx264'])
        command.extend(['-preset', self.config['General']['quality']])
        command.extend(['-r', self.config['General']['fps']])
        command.extend(['-g', str(int(float(self.config['General']['fps']) * 2))])
        command.extend(['-b:v', self.config['General']['vbr']])
        command.extend(['-bufsize', '3000k'])
        command.extend(['-maxrate', self.config['General']['vbr']])
        command.extend(['-c:a', self.config['General']['audio_encoder']])
        command.extend(['-ar', '44100'])
        command.extend(['-b:a', '128k'])
        command.extend(['-pix_fmt', 'yuv420p'])

        # Add output format and targets using tee
        command.extend(['-f', 'tee'])
        for target in targets:
            # Specify [f=flv:onfail=ignore] followed by the target
            command.extend(['[f=flv:onfail=ignore]' + target])

        return command

    def start_streaming(self):
        # Construct the FFmpeg command
        ffmpeg_command = self.construct_ffmpeg_command()

        # Start the FFmpeg process
        try:
            subprocess.run(ffmpeg_command, check=True)
        except subprocess.CalledProcessError as e:
            print("Error starting FFmpeg:", e)

if __name__ == "__main__":
    # Example usage:
    from configparser import ConfigParser

    # Load your configuration from a file
    config = ConfigParser()
    config.read('your_config_file.ini')

    # Create an instance of FFmpegStreamer
    streamer = FFmpegStreamer(config)

    # Start streaming
    streamer.start_streaming()

