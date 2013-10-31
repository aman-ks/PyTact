import wave
import numpy as np
from scikits.audiolab import Sndfile

a = wave.open('output.wav','r')
total_frames = a.getnframes()
#rate = a.getframerate()
f = Sndfile('output.wav','r')

fs = f.samplerate
nc = f.channels
enc = f.encoding

format_wave = f.format



data_float = f.read_frames(total_frames,dtype=np.float64)

print fs,nc,enc,format_wave
#print data
print "\n \n"
print data_float
