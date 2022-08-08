#!/usr/bin/env bash

echo Bafuss Video Overlay
echo --------------------
printf "\nThis script adds an overlay to an existing movie to avoid using resources while streaming"
printf "\nUsage:\n  prep_video.sh input.movie ouput.movie overlay.image\n\n"

if [ $# -ne 3 ]; then
  printf 1>&2 ">>$0 error: this requires exactly 3 parameters, input movie, output movie, image overlay\n\n"
  exit 2
fi

VIDEO_SOURCE=$1 
VIDEO_OVERLAY=$3
VIDEO_OUTPUT=$2


ffmpeg -y -i $VIDEO_SOURCE -i $VIDEO_OVERLAY  -filter_complex [0]overlay=x=0:y=0[out] -map [out] -map 0:a? $VIDEO_OUTPUT

