import math
import numpy as np
from scipy.io import wavfile
import pyaudio
import time

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

#Play audio stream from LPCM stream
def stream_out(stream,sample_rate,length):
    p=pyaudio.PyAudio()
    out=p.open(format=pyaudio.paFloat32,
                  channels=1,
                  rate=sample_rate,
                  output=True)
    out.write(LPCM_arr(stream,sample_rate,length))
    out.stop_stream()
    out.close()
    p.terminate()

#Wave generators
def sin(freq,amp):return lambda x:amp*np.sin(freq*2*np.pi*x)
def sawtooth(freq,amp):return lambda x:(((x%(1/freq))*freq)-.5)*2*amp
def square(freq,amp):return lambda x:amp if (sawtooth(freq,amp)(x)>0) else -1*amp
def triangle(freq,amp):return lambda x:


length=10
sample_rate=44100

f=square(440,1)

gen=lambda:LPCM(f,sample_rate,length)

stream_out(gen,sample_rate,length)
#wav_out("test.wav",gen,sample_rate,length)

'''
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=sample_rate,
                output=True)

while True:
    audio=np.empty(sample_rate).astype(np.float32)
    for i in range(sample_rate):
        audio[i]=next(gen)
    stream.write(audio)

stream.stop_stream()
stream.close()
p.terminate()
'''
