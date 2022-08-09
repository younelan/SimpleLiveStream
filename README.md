# *BaFuss* - Bash FFmpeg Uncomplicated Stream Script

This is a simple script to simplify streaming platforms like YouTUBE or Twitch through ffmpeg

##Steps to make it work:
- install ffmpeg (apt-get install ffmpeg on ubuntu or brew install ffmpeg on a mac)
- Get a Youtube Stream Key and/or Twitch Stream Key and add them there
- edit DEFAULT_VIDEO_SOURCE to reflect the video background file
- edit your playlist, default music.txt playlist with One music file per line 
  in the following format: 'file filename.mp3' . Note the word file is required
- optionally run the screen command if you want to run it remotely
- optionally add an overlay to your video with add_image.sh
- run stream.sh with optional parameters below

## Syntax examples:
- **stream using defaults in config.sh**
    > ./stream.sh 
- **stream to twitch restarting on a loop if streaming fails**
    > ./stream.sh -t twitch -l YES
- **stream playlist "music.txt" with background "title.png"**
    > ./stream.sh -p music.txt -t title.png
- **stream playlist dance.txt with video video.mp4 as a background**
    > ./stream.sh -p dance.txt -v video.mp4
- **stream playlist play.txt with overlay overlay title.png and video video.mov in the background**
    > ./stream.sh -p play.txt -o title.png -v video.mov >log.txt @&1 -l YES &&
- **pre-create a video with your overlay to use less resources while streaming**
    > ./add_image.sh {input.video} {output.video} {overlay.image}

## optional parameters
- -p [playlist]  provide a file playlist
- -t [target]    provide a target - youtube or twitch
- -v [video]     provide a video file for background
- -i [img.file]  provide a image for the background, preferably transparent png
- -o [image]     provide an image to overlay on video
- -d [dir]       provide a dir to play all audio files in a directory

## main files:
- *config.sh* - variables to customize the script
- *common.sh* - common functions
- *stream.sh* - main stream script
- *overlay_text.sh* - overlay an image on an existing video

