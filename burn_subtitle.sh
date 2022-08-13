#!/usr/bin/env bash

video=assets/FunZone/partypeople.mp4
subtitles=assets/quotes_topright.srt
output=output.mp4

#./burn_subtitle.sh assets/FunZone/partypeople.mp4 assets/FunZone/partypeople.srt assets/FunZone/videos/partypeople.mp4

if [ $# -ne 3 ]  
then
  echo "Error: script needs 2 parameters, video, subtitles, output file
  echo "  ./mk_video [input_video] [subtitles] [output_video]
  exit
fi

video=$1
subtitles=$2
outfile=$3
style=" \
:force_style=Alignment=0,OutlineColour=&H100000000,BorderStyle=3,Outline=1,Shadow=0,Fontsize=12,MarginL=305,MarginV=25 \
"
# style=""
# ffmpeg -i $video -lavfi "subtitles=$subtitles:force_style=Alignment=0,\OutlineColour=&H100000000,BorderStyle=3,Outline=1,Shadow=0,Fontsize=12,MarginL=305,MarginV=25" \
#         -crf 1 -c:a copy $outfile

#ffmpeg -i $video -lavfi "subtitles=$subtitles:force_style='Alignment=0,OutlineColour=&H100000000, \
#                         BorderStyle=3,Outline=1,Shadow=0,Fontsize=18,MarginL=70,MarginV=5'"

#ffmpeg -i "$video" -lavfi "subtitles=$subtitles:force_style='Alignment=0,OutlineColour=&H100000000,BorderStyle=3,Outline=1,Shadow=0,Fontsize=12,MarginL=100,MarginV=5'" -crf 1 -c:a copy "$outfile"
ffmpeg -i "$video" -lavfi "subtitles=$subtitles:force_style='Alignment=0,OutlineColour=&H100000000,Outline=1,Shadow=0,Fontsize=14,MarginL=100,MarginV=5'" -crf 1 -c:a copy "$outfile"
