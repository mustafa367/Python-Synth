import math
import numpy as np
from scipy.io import wavfile
import time

out_dir='./out'

#LPCM stream generator
def LPCM(f,sample_rate,length):
    samples=math.ceil(sample_rate*length)
    for i in range(samples):
        yield f(i/sample_rate)

#Turn LPCM generator into array
def LPCM_arr(stream,sample_rate,length):
    samples=math.ceil(sample_rate*length)
    audio=np.empty(samples).astype(np.float32)
    for i,x in enumerate(stream()):audio[i]=x
    return audio

#Produce wav from LPCM stream
def wav_out(filename,stream,sample_rate,length):
    audio=LPCM_arr(stream,sample_rate,length)
    wavfile.write(filename,sample_rate,audio)

#Wave generators
def sin(freq,amp):return lambda x:amp*np.sin(freq*2*np.pi*x)
def sawtooth(freq,amp):return lambda x:(((x%(1/freq))*freq)-.5)*2*amp
def square(freq,amp):return lambda x:amp if (sawtooth(freq,amp)(x)>0) else -1*amp
#def triangle(freq,amp):return lambda x:

length=10
sample_rate=44100

f=square(440,1)

gen=lambda:LPCM(f,sample_rate,length)

wav_out(out_dir+"/test.wav",gen,sample_rate,length)
