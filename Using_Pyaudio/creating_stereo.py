# Make a wave file (.wav) consisting of a sine wave
# Adapted from http://www.swharden.com

from struct import pack
from math import sin, pi
import wave

Fs = 8000 # Frequency 

## GENERATE STERIO FILE ##

wf = wave.open('sin02_stereo.wav', 'w')
wf.setnchannels(2)		# one channel (stereo)
wf.setsampwidth(4)		# two bytes per sample
wf.setframerate(Fs)		# samples per second
maxAmp = 2**31-1.0 		# maximum amplitude
f1 = 261.625565  		# 261.625565 Hz (middle C)
f2 = 440.0  			# note A4
for n in range(0, 2*Fs):	# 2 seconds duration
	wvData = pack('i', maxAmp * sin(n*2*pi*f1/Fs)) # left
	wvData += pack('i', maxAmp * sin(n*2*pi*f2/Fs)) # right
	wf.writeframesraw(wvData)
wf.close()
