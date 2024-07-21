import numpy as np
from scipy.io import wavfile
import datetime
from tone import tone

def main():
    f=sin(330,1)
    tone1=tone(f)
    g=sin(220,1)
    tone2=tone(g)
    tone3=tone1+tone2

    wav_write(tone3.get)
    return

def wav_write(LPCM ,sample_rate=44100,volume=.1,
                 filename="../out"+"/test_"+datetime.datetime.now().strftime("%Y:%m:%d:%H:%M:%S")+".wav"):
    wavfile.write(filename,sample_rate, volume * LPCM)
    return

#Wave generators
def sin(freq,amp):return lambda x:amp*np.sin(freq*2*np.pi*x)
def sawtooth(freq,amp):return lambda x:(((x%(1/freq))*freq)-.5)*2*amp
def square(freq,amp):return lambda x:amp if (sawtooth(freq,amp)(x)>0) else -1*amp
def triangle(freq,amp):return lambda x:2*(sawtooth(freq,amp)(x)*square(freq,amp)(x)-amp/2)

if __name__ == "__main__":
    main()
