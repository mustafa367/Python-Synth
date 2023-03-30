import datetime
import numpy as np
from audio_out import audio_out

#Wave generators
def sin(freq,amp):return lambda x:amp*np.sin(freq*2*np.pi*x)
def sawtooth(freq,amp):return lambda x:(((x%(1/freq))*freq)-.5)*2*amp
def square(freq,amp):return lambda x:amp if (sawtooth(freq,amp)(x)>0) else -1*amp
def triangle(freq,amp):return lambda x:2*(sawtooth(freq,amp)(x)*square(freq,amp)(x)-amp/2)

if __name__ == "__main__":
    out_dir='./out'
    now=datetime.datetime.now()
    now_str=now.strftime("%Y:%m:%d:%H:%M:%S")
    out_name=out_dir+"/test_"+now_str+".wav"

    f=triangle(440,1)
    sq=audio_out(f)
    sq.wav_out(out_name)
