### Playing Wavefile
===
Signifigance of wavefile properties 

* ```.getnchannels()```      - This returns the number of channels in the file (1 = mono, 2 = stereo)
* ```.getframerate()```      - This returns the sampling rate or the number of frames played per second
* ```.getnframes()```       	- This returns the total number of frame in the recording
* ```.getsampwidth()```      - This returns the bit depth in bytes (ex. 16 bit recording will have a bit depth of 2 bytes)
===
Importance of pack/unpack function

Why use ```struct.pack``` and ```struct.unpack```?

* Audio is stored as binary strings. Everytime you use the ```getreadframe()``` function, you are getting a binary string. In order to manipulate the data (filter/gain), you need to convert the string into an integer. So the process becomes:
~~~
1.  Unpack binary string into an integer
2.  Apply mathematical operations to the integer
3.  Pack integer back into binary string
4.  Write the binary string into the stream (Playing the wav)
~~~
