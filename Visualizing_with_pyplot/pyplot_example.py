# plot_micinput.py
"""
Using Pyaudio, record sound from the audio device and plot,
for 8 seconds, and display it live in a Window.
Usage example: python pyrecplotanimation.py
Gerald Schuller, October 2014 
Modified: Ivan Selesnick, September 2015
"""

import pyaudio
import struct
from matplotlib import pyplot as plt

plt.ion()           # Turn on interactive mode so plot gets updated

WIDTH = 2           # bytes per sample
CHANNELS = 1        # mono
# RATE = 16000
RATE = 8000
BLOCKSIZE = 1024
DURATION = 10        # Duration in seconds

NumBlocks = int( DURATION * RATE / BLOCKSIZE )

print 'BLOCKSIZE =', BLOCKSIZE
print 'NumBlocks =', NumBlocks

# Initialize plot window:
plt.figure(1)
plt.ylim(-10000, 10000)        # set y-axis limits

plt.xlim(0, BLOCKSIZE)         # set x-axis limits
plt.xlabel('Time (n)')
t = range(0, BLOCKSIZE)

# # Time axis in units of milliseconds:
# plt.xlim(0, 1000.0*BLOCKSIZE/RATE)         # set x-axis limits
# plt.xlabel('Time (msec)')
# t = [n*1000/float(RATE) for n in range(BLOCKSIZE)]

line, = plt.plot([], [], color = 'blue')  # Create empty line
line.set_xdata(t)                         # x-data of plot (time)

# Open audio device:
p = pyaudio.PyAudio()
stream = p.open(format = p.get_format_from_width(WIDTH),
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = False)

for i in range(1, NumBlocks):
    input_string = stream.read(BLOCKSIZE)                     # Read audio input stream
    input_tuple = struct.unpack('h'*BLOCKSIZE, input_string)  # Convert
    line.set_ydata(input_tuple)                               # Update y-data of plot
    # # Print block number:
    # if i % 20 == 0:
    #     print i,
    plt.draw()
plt.close()

stream.stop_stream()
stream.close()
p.terminate()

print '* Done'
