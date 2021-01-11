def rubahKata(vars):
	splits = vars.split(" ")
	s = ""
	for split in splits:
		s += split[::-1]+" "
	return s[:len(s)-1]

def fizzBuzz():
	for i in range(1,101):
		if i%3!=0 and i%5!=0: 
			print(i)
		elif i%3 == 0 and i%5!=0:
			print('Fizz')
		elif i%5 == 0 and i%3!=0:
			print('Buzz')
		elif i%5 == 0 and i%3==0:
			print('FizzBuzz')

def deretAngka(n):
	if n <= 1:
		return(n)
	else:
		return(deretAngka(n-1) + deretAngka(n-2))

def no3():
	for i in range(0,10):
		print(deretAngka(i))

def convertVideo(vars):
	import ffmpeg_streaming
	from ffmpeg_streaming import Formats, Bitrate, Representation, Size

	video = ffmpeg_streaming.input(vars)
	hls = video.hls(Formats.h264())
	_360p  = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
	hls.representations(_360p)
	hls.output('/home/rendy/Desktop/hls.m3u8')

# input1 = input()
# no1 = rubahKata(input1)
# print(no1)

# no2 = fizzBuzz()

# no3 = no3()

input5 = input()
no5 = convertVideo(input5)