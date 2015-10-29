# Audio-Effects

Multiple types of audio effects will be described and implemented in python.

===
### GETTING STARTED

All of these implementations will be in python and therefore will utilize the pyaudio module.
I would suggest to use python 2.7 since some of the other modules I will be using will not be compatible with the 3+ version.
By default, ``pip`` and ``setuptools`` will already be installed however they will need to be upgraded: <br>

**For windows:** <br>
```
python -m pip install -U pip setuptools
```

**For Linux or OSX:** <br>
```
pip install -U pip setuptools
```

Now, in order to install the pyaudio module simply type the following into the terminal:
```
pip install pyaudio
```

If you run into an error, you may have to install manually by downloading the corresponding wheel and using pip.
The wheels can be found at http://www.lfd.uci.edu/~gohlke/pythonlibs/ <br>

In order to install, simply download the wheel and move it to your current directory. Then type:
```
pip install (Name of your wheel).whl
```

===
### Playing files

