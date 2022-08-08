source config.sh

VIDEO_IMAGE=$DEFAULT_WATERMARK
VIDEO_SOURCE=$DEFAULT_VIDEO
FULLVIDEO_SOURCE=$DEFAULT_VIDEO_SOURCE
SINGLE_AUDIO_FILE=$DEFAULT_SINGLE_AUDIO_SOURCE
START=$(date +"%Y/%M/%D %H:%M")
VIDEO_SOURCE=$DEFAULT_VIDEO
TARGET=$DEFAULT_TARGET
STREAM_URL=$YOUTUBE_URL/$YOUTUBE_KEY

convertsecs() {
 ((h=${1}/3600))
 ((m=(${1}%3600)/60))
 ((s=${1}%60))
 printf "%02d:%02d:%02d\n" $h $m $s
}
log_stream() {
  secs=$SECONDS
  duration=$(( secs/60 ))
  hrs=$(( secs/3600 )); mins=$(( (secs-hrs*3600)/60 )); secs=$(( secs-hrs*3600-mins*60 ))
  END=$(date +"%Y/%M/%D %H:%M")
  echo Start: $START - End: $END Duration: $duration - Playlist: $AUDIO_FILES - VIDEO: $VIDEO_SOURCE - Target: $TARGET >>$LOGFILE

  echo Start: $START - End: $END Duration: $hrs:$mins:$secs - Playlist: $AUDIO_FILES - VIDEO: $VIDEO_SOURCE - Target: $TARGET
}


while getopts ":o:s:l:t:v:p:" opt; do
  case $opt in
    s)
    #static image stream
    VIDEO_INPUT=STATIC
    VIDEO_IMAGE="$OPTARG"
    ;;
    d)
    #directory stream
    AUDIO_INPUT=DIRECTORY
    AUDIO_DIRECTORY="$OPTARG"
    ;;
    l) DO_LOOP="$OPTARG"
    ;;
    o) #add overlay
    VIDEO_INPUT=MOVIE
    VIDEO_OVERLAY="$OPTARG"
    ;;
    t) TARGET="$OPTARG"
    ;;
    p) AUDIO_FILES="$OPTARG"
    ;;
    v) 
    VIDEO_SOURCE="$OPTARG"
    VIDEO_INPUT=MOVIE
    ;;
  esac
  case "$TARGET" in
         ("youtube")
                 STREAM_URL=$YOUTUBE_URL/$YOUTUBE_KEY
                 ;;
         ("twitch")
                 STREAM_URL=$TWITCH_URL/$TWITCH_KEY
                 ;;
  esac
done
manpage() {
           echo "Stream Scripts"
          echo "-l [YES|NO]    optional argument to loop. NO will break on failure, other values will loop"
          echo "-p [playlist]  provide a file playlist"
          echo "-t [target]    provide a target - youtube or twitch"
          echo "-v [video]     provide a video file for background"
}

manpage
