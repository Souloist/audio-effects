# simple_wire.py
# Play microphone input to speaker using callback function
#
# Adapted from Wire(Callback) example
# https://people.csail.mit.edu/hubert/pyaudio/

import pyaudio
import time

CHANNELS = 1
RATE = 16000

# Define callback function
def my_callback_fun(input_string, block_size, time_info, status):
    return (input_string, pyaudio.paContinue)    # Return data and status

# Create audio object
p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(format = pyaudio.paInt16,   	# 16 bits/sample
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
                stream_callback = my_callback_fun)

stream.start_stream()

print 'Audio stream is on?', stream.is_active()

print 'The wire will be on for 6 seconds'
time.sleep(6)

# Close audio stream
stream.stop_stream()

print 'Audio stream is on?', stream.is_active()

stream.close()
p.terminate()
