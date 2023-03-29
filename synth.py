import math
import numpy as np
from scipy.io import wavfile
import datetime

out_dir='./out'
now=datetime.datetime.now()
now_str=now.strftime("%Y:%m:%d:%H:%M:%S")
out_name=out_dir+"/test_"+now_str+".wav"

class synth:
    def __init__(self,f,sample_rate=44100,volume=.1,length=20):
        self.f=lambda x:f(x)*volume
        self.sample_rate=sample_rate
        self.length=length

    #LPCM stream generator
    def LPCM(self):
        samples=math.ceil(self.sample_rate*self.length)
        for i in range(samples):
            yield self.f(i/self.sample_rate)

    #Turn LPCM generator into array
    def LPCM_arr(self,stream):
        samples=math.ceil(sample_rate*length)
        audio=np.empty(samples).astype(np.float32)
        for i,x in enumerate(stream()):audio[i]=x
        return audio

    #Produce wav from LPCM stream
    def wav_out(self,filename):
        audio=self.LPCM_arr(self.LPCM)
        wavfile.write(filename,self.sample_rate,audio)

#Wave generators
def sin(freq,amp):return lambda x:amp*np.sin(freq*2*np.pi*x)
def sawtooth(freq,amp):return lambda x:(((x%(1/freq))*freq)-.5)*2*amp
def square(freq,amp):return lambda x:amp if (sawtooth(freq,amp)(x)>0) else -1*amp
#def triangle(freq,amp):return lambda x:

f=sin(440,1)
sq=synth(f)
sq.wav_out(out_name)
