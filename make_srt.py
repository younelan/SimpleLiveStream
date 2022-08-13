#!/usr/bin/env python
import sys

SOURCE = "assets/quotes.txt"
OUTPUT = "assets/quotes_topright.srt"
DURATION = 15
STYLE_PRELUDE="""[Script Info]

ScriptType: v4.00+
Collisions: Normal
PlayResX: 1280
PlayResY: 720
Timer: 100.0000

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
;Subtitle Editor
Style: Default,Arial,36,&H00FFFFFF,0,0,0,-1,0,0,0,100,100,0,0,1,1,1,2,30,30,5,0
"""

EVENT_PRELUDE="""

[Events]
Format: Layer, Start, End, Style, Actor, MarginL, MarginR, MarginV, Effect, Text
"""

class SRT(object):
	"""docstring for SRT class, meant to heandle Subtitles"""
	def __init__(self, fname):
		super(SRT, self).__init__()
		self.file = fname
		self.read()

	def read(self):
		with open(self.file) as fp:
			lines=fp.readlines()

			self.lines=lines

	def get_time(self,duration):
		secs=duration
		mins, secs = divmod(secs, 60)
		hrs, mins = divmod(mins,60)
		return "%i:%i:%i" % (hrs, mins, secs)

	def generate_srt(self,outfile,duration=5,style=None):

		with open(outfile,"w") as fp:
			for idx,line in enumerate(self.lines):
				start = self.get_time(idx*duration)
				start = ""
				slide="%s\n" %(idx)
				slide += "%s,100 --> %s,0\n" % (self.get_time(idx*duration),self.get_time(idx*duration+duration) )
				#slide+="<font color=\"#FF0000\" size=12>Fun bit:</font> "
				slide += line
				if style:
					slide += "{\\an9}\n"
				slide+="\n"
				
				print(slide),

				fp.write(slide)
	def generate_ass(self,outfile,duration=5):
		#output=PRELUDE
		styles=[]
		events=[]
		raw_style_str="Style: style_%i,Skia-Regular_Bold,47,&H00FFFFFF,&H3C000000,&H32000000,&H00000000," \
		              "-1,0,0,0,100,100,0,0,1,1,1,1,380,0,616,0"
		raw_event_str="Dialogue: 0,%s.10,%s.0,%s,,0000,0000,0000,,%s" 
		with open(outfile,"w") as fp:

				for idx,line in enumerate(self.lines):
					#slide.append(raw_event_str % (line))
					start = self.get_time(idx*duration)
					stop = self.get_time(idx*duration+duration)

					slide="%s\n" %(idx)
					cur_style="style_%i" %idx

					styles.append(raw_style_str % (idx) )
					events.append(raw_event_str %(start,stop,cur_style,line))
				fp.write(STYLE_PRELUDE)
				fp.write("\n".join(styles))
				fp.write(EVENT_PRELUDE)
				fp.write("".join(events))


def main():
	if len(sys.argv) <> 4:
		print """
Error", need 3 arguments source:
      subtitle_file text (1 slide per line)
      output_file - generated file
      interval - interval between slides in seconds
"""
		sys.exit()

	SCRIPT,SOURCE, OUTPUT, DURATION = sys.argv
	srt = SRT(SOURCE)
	DURATION=int(DURATION)
	srt.generate_srt(OUTPUT,duration=DURATION)



if __name__ == '__main__':
	main()