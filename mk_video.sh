#!/usr/bin/env bash

if [ $# -ne 3 ]  
then
  echo "Error: script needs 2 parameters, background video, audio, output file
  echo "  ./mk_video [input_video] [input_audio] [output_video]
  exit
fi

video=$1
subtitles=$2
outfile=$3

background=assets/video/dancefloor.mp4
audio=assets/FunZone/partypeople.mp3

outfile=assets/FunZone/videos/$(basename "${filepath%.*}")


background=$1
audio=$2
outfile=$3

#caption="@YounElan"
ffmpeg -stream_loop -1 -i $background -i "$audio" \
       -filter_complex "[0:v]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720, \
       setsar=1,fps=25,drawtext=text='$caption'\
       :fontsize=18:fontcolor=white:x=10:y=h-th-10,format=yuv420p[v]" \
       -map "[v]" -map 1:a -c:v libx264 -c:a aac -ac 2 -ar 44100 -g 50 -b:v 2000k -maxrate 2000k -bufsize 6000k -shortest "$outfile"

