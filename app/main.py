import datetime
import numpy as np
from audio_out import audio_out

#Wave generators
def sin(freq,amp):return lambda x:amp*np.sin(freq*2*np.pi*x)
def sawtooth(freq,amp):return lambda x:(((x%(1/freq))*freq)-.5)*2*amp
def square(freq,amp):return lambda x:amp if (sawtooth(freq,amp)(x)>0) else -1*amp
def triangle(freq,amp):return lambda x:2*(sawtooth(freq,amp)(x)*square(freq,amp)(x)-amp/2)

def shepard_tone_a(freq,amp,x):
    f=lambda z,i:(0 if z+i==0 else amp/(z+i)*np.sin(freq*2*np.pi*((z+i)**2)))
    return sum([f(x,i) for i in range(64)])

def shepard_tone_b(freq,amp,x):
    f=lambda z:amp/(z**2+1)*np.sin(freq*2*np.pi*(2**z))
    g=lambda z,i:f(z-i)
    return sum([g(x,i) for i in range(64)])

if __name__ == "__main__":
    out_dir='../out'
    now=datetime.datetime.now()
    now_str=now.strftime("%Y:%m:%d:%H:%M:%S")
    out_name=out_dir+"/test_"+now_str+".wav"

    f=lambda x:shepard_tone_b(440,1,x)

    audio_out(f).wav_out(out_name)
