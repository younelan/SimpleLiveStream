#!/usr/bin/env python

SOURCE = "assets/quotes.txt"
OUTPUT = "assets/quotes.srt"
duration = 15

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

	def generate(self,outfile):
		with open(outfile,"w") as fp:
			for idx,line in enumerate(self.lines):
				start = self.get_time(idx*duration)
				start = ""
				slide="%s\n" %(idx)
				slide += "%s,100 --> %s,0\n" % (self.get_time(idx*duration),self.get_time(idx*duration+duration) )
				slide += line + "\n"
				print(slide),

				fp.write(slide)


def main():
	srt = SRT(SOURCE)
	srt.generate(OUTPUT)



if __name__ == '__main__':
	main()