import math
import numpy as np
from scipy.io import wavfile

class audio_out:
    def __init__(self,f,sample_rate=44100,volume=.1,length=20):
        self.f=lambda x:f(x/sample_rate)*volume
        self.sample_rate=sample_rate
        self.samples=math.ceil(sample_rate*length)

    def LPCM_arr(self):
        audio=np.empty(self.samples).astype(np.float32)
        for i in range(self.samples):audio[i]=self.f(i)
        return audio

    #Produce wav from LPCM stream
    def wav_out(self,filename):
        audio=self.LPCM_arr()
        wavfile.write(filename,self.sample_rate,audio)
