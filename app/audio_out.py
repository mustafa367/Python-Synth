import datetime
import math
import numpy as np
from scipy.io import wavfile

class audio_out:
    def __init__(self,f,sample_rate=44100,volume=.1,length=20,
                 filename="../out"+"/test_"+datetime.datetime.now().strftime("%Y:%m:%d:%H:%M:%S")+".wav"):
        self.f=lambda t:f(t/sample_rate)*volume
        self.sample_rate=sample_rate
        self.samples=math.ceil(sample_rate*length)
        self.filename=filename
        self.wav_out()

    #Produce LPCM array
    def LPCM(self):
        audio=np.empty(self.samples).astype(np.float32)
        for i in range(self.samples):audio[i]=self.f(i)
        return audio

    #Produce wav from LPCM stream
    def wav_out(self):
        wavfile.write(self.filename,self.sample_rate,self.LPCM())
