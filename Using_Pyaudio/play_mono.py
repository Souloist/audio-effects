# play_wav_mono.py

import pyaudio
import wave
import struct
import math

def clip16( x ):    
    # Clipping for 16 bits
    if x > 32767:
        x = 32767
    elif x < -32768:
        x = -32768
    else:
        x = x        
    return int(x)

gain = 0.5

# wavfile = 'author.wav'
wavfile = 'sin01_mono.wav'
# wavfile = 'sin01_stereo.wav'

print("Play the wave file %s." % wavfile)

wf = wave.open( wavfile, 'rb' )

# Read the wave file properties
num_channels = wf.getnchannels()       	# Number of channels
Fs = wf.getframerate()                  # Sampling rate (frames/second)
signal_length  = wf.getnframes()       	# Signal length
width = wf.getsampwidth()       		# Number of bytes per sample

print("The file has %d channel(s)."            % num_channels)
print("The frame rate is %d frames/second."    % Fs)
print("The file has %d frames."                % signal_length)
print("There are %d bytes per sample."         % width)

p = pyaudio.PyAudio()

stream = p.open(format      = pyaudio.paInt16,
                channels    = num_channels,
                rate        = Fs,
                input       = False,
                output      = True )

input_string = wf.readframes(1)          # Get first frame

while input_string != '':

    # Convert string to number
    input_tuple = struct.unpack('h', input_string)  # One-element tuple
    input_value = input_tuple[0]                    # Number

    # Compute output value
    output_value = clip16(gain * input_value)    # Number

    # Convert output value to binary string
    output_string = struct.pack('h', output_value)  

    # Write output value to audio stream
    stream.write(output_string)                     

    # Get next frame
    input_string = wf.readframes(1)                 

print("**** Done ****")

stream.stop_stream()
stream.close()
p.terminate()
