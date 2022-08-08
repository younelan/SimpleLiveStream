#!/usr/bin/env bash
source common.sh

ACTION=$(echo "$ACTION" | tr a-z A-Z)
DO_LOOP=$(echo "$DO_LOOP" | tr a-z A-Z)

case $VIDEO_INPUT in
    ("STATIC") 
    #static image stream 
    SOURCE_STR="-loop 1 -framerate 10 -re -i $VIDEO_IMAGE"
    ;;
    *)
    SOURCE_STR="-i $VIDEO_SOURCE"
    ;;
esac
case $AUDIO_INPUT in
    ("DIR")
    echo "Error, Not Supported yet, use PLAYLIST"
    exit 2
    ;;
    ("FILE")
    AUDIO_STR=" -i $SINGLE_AUDIO_FILE" ;;
    ;;
    #("PLAYLIST")
    *)
    AUDIO_STR="-f concat -i $AUDIO_FILES" ;;
esac

OVERLAY_STR=""
if [[ ! -z "$VIDEO_OVERLAY" ]];then
OVERLAY_STR=" \
    -i $VIDEO_OVERLAY \
    -filter_complex overlay=0:0:format=yuv444 \
"
fi

while :
do

ffmpeg \
	-stream_loop -1 \
	-re \
	$SOURCE_STR \
	-thread_queue_size 512 \
	-stream_loop -1 \
	-re \
	$AUDIO_STR \
	-map 0:v:0 -map 1:a:0 \
	-map_metadata:g 1:g \
	-c:v libx264 -preset $QUAL -r $FPS -g $(($FPS *2)) -b:v $VBR -bufsize 3000k -maxrate $VBR \
	-c:a $AUDIO_ENCODER -ar 44100 -b:a 128k -pix_fmt yuv420p \
	-f flv $STREAM_URL \
  $OVERLAY_STR

  END=$(date +"%Y/%M/%D %H:%M")
  secs=$SECONDS

  log_stream

  if [ "$DO_LOOP" == "NO" ]; then
          break;
  fi
done
