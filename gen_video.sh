#!/usr/bin/env bash
#source common.sh
source config.sh
VIDEO_FILE=assets/video/stardust.mp4
AUDIO_FILE=assets/audio/livestream.mp3
VIDEO_IMAGE=assets/title.png
OUTFILE="test.mp4"
TMPFILE="tmp.jpg"
FONT="assets/DancingScript-Regular.ttf"

getTag()   { 
	TAG=$1
	FNAME=$2
	ffprobe -loglevel quiet -show_entries format_tags=$TAG -of default=noprint_wrappers=1:nokey=1 $AUDIO_FILE
}
getAttr() {
	TAG=$1
	FNAME=$2
    ffprobe -v error -show_entries format=$TAG -of default=noprint_wrappers=1:nokey=1 $FNAME
}
getStreamTag() {
	TAG=$1
	FNAME=$2
	ffprobe -v error -select_streams v:0 -show_entries stream=$TAG -of default=noprint_wrappers=1:nokey=1 $FNAME
}
saveCoverImage() {
	INPUT=$1
	OUTPUT=$2
	ffmpeg -i $INPUT -an -vcodec copy $OUTPUT
}


ARTIST=$(getTag artist $AUDIO_FILE)
ALBUM=$(getTag album $AUDIO_FILE)
TITLE=$(getTag title $AUDIO_FILE)
AUDIO_DURATION=$(getAttr duration $AUDIO_FILE)
VIDEO_DURATION=$(getStreamTag duration $VIDEO_FILE)
echo Artist: $ARTIST TITLE: $TITLE Album: $ALBUM Duration: $AUDIO_DURATION
echo Video Duration: $VIDEO_DURATION
#saveCoverImage $AUDIO_FILE $TMPFILE


ffmpeg \
	   -i $VIDEO_FILE \
	   -i $AUDIO_FILE \
       -c:v libx264 -tune stillimage -c:a aac -b:a 192k \
       -pix_fmt yuv420p -shortest \
       $OUTFILE \
       -i $TMPFILE \
-filter_complex "[1:v]scale=-1:200 [ovrl], \
[0:v][ovrl]overlay=(main_w-overlay_w)-5:(main_h-overlay_h)-100, \
drawtext=fontfile=$FONT: \
text='$ARTIST': x=(w-text_w)-220:y=(h-text_h)-200: fontsize=50: fontcolor=white,
drawtext=fontfile=$FONT: \
text='$TITLE': x=(w-text_w)-220:y=(h-text_h)-150: fontsize=50: fontcolor=white"

exit
echo ffmpeg -loop 1 -i $VIDEO_IMAGE -i $AUDIO_FILE \
       -c:v libx264 -tune stillimage -c:a aac -b:a 192k \
       -pix_fmt yuv420p -shortest \
       $OUTFILE \
       -i $TMPFILE \
       -filter_complex "[0:v][1:v] scale=320:-1;overlay=0:0;" 
       echo \
   		-vf 'color=c=white:s=1280x30[L0]; \
       color=c=red:s=1280x30[L1]; \
       [L0][L1]overlay=(t/6.072733-1)*w:0:eval=frame[L2]; \
       [in][L2]overlay=0:690:shortest=1[out]' \

#echo $video_duration
#echo $video_width
#echo $video_height
#echo $five_percent

#ffmpeg -i "$1"  "$2" -map [bar] -f xv display


##IMAGE
#ffmpeg -ss 125 -i wrong-way-fixed.mp3 -t 1 \ -s 480x300 -f image2 /dev/null
#or use this
#ffmpeg -i input.mp3 -an -vcodec copy cover.jpg