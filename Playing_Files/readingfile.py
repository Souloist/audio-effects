import wave

wf = wave.open('cat01.wav') #insert your wav file. Make sure it is in the same directory

#Useful Information 

print 'number of channels: ', wf.getnchannels() # 1 channel for mono. 2 channels for stereo
print 'framerate: ', wf.getframerate()          # Sampling rate (frames/second)
print 'signal length: ', wf.getnframes()        # Signal length
print 'bytes per frame:', wf.getsampwidth()     # Number of bytes per sample

wf.close()
