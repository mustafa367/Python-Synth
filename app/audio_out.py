import math
import numpy as np
from scipy.io import wavfile

class audio_out:
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
        samples=math.ceil(self.sample_rate*self.length)
        audio=np.empty(samples).astype(np.float32)
        for i,x in enumerate(stream()):audio[i]=x
        return audio

    #Produce wav from LPCM stream
    def wav_out(self,filename):
        audio=self.LPCM_arr(self.LPCM)
        wavfile.write(filename,self.sample_rate,audio)
