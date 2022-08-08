source common.sh
echo "Dummy script to test parameters without running ffmpeg"
DO_LOOP=NOT
while :
do
  sleep  3
  echo hello
  if [ "$DO_LOOP" == "NO" ]; then
	  break;
  fi
done
log_stream
