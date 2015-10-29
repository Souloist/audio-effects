# Make a wave file (.wav) consisting of a sine wave
# Adapted from http://www.swharden.com

from struct import pack
from math import sin, pi
import wave

Fs = 8000 # Frequency 

## CREATE MONO FILE ##

wf = wave.open('sin02_mono.wav', 'w')		# wf : wave file
wf.setnchannels(1)							# one channel (mono)
wf.setsampwidth(4)							# two bytes per sample
wf.setframerate(Fs)							# samples per second
maxAmp = 2**31 - 1.0 						# maximum amplitude
f = 261.625565  							# Hz (middle C)
for n in range(0, 2*Fs):  					# 2 seconds duration
	wvData = pack('i', maxAmp * sin(n*2*pi*f/Fs)) 
    # i indicate 'integer'  ('<i' or '>i' for different Endians)
	wf.writeframesraw(wvData)
wf.close()
