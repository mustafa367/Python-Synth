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
    mod_amp=lambda z:1/(z**2+1)
    mod_freq=lambda z:2**z
    f=lambda z:amp*mod_amp(z)*np.sin(freq*2*np.pi*mod_freq(z))
    g=lambda z,i:f(z-i)
    return sum([g(x,i) for i in range(64)])

def shepard_tone_c(x,freq_start=220,freq_end=880,amp=1,duration=20):
    mod_amp=lambda z:(-abs(z*amp*2/duration)+amp if abs(z)<duration else 0)
    mod_freq=lambda z:(z*(freq_end-freq_start)/duration+(freq_end-freq_start)/2 if abs(z)<duration else 0)
    f=lambda z:amp*mod_amp(z)*np.sin(2*np.pi*z*mod_freq(z))
    g=lambda z,i:f(z-i)
    return sum([g(x,i) for i in range(20)])

def shepard_tone_d(freq,amp,x):
    mod_amp=lambda z:1/((z/2)**2+1)
    mod_freq=lambda z:2**z
    f=lambda z:amp*mod_amp(z)*np.sin(freq*2*np.pi*mod_freq(z))
    g=lambda z,i:f(z-i)
    return sum([g(x,i) for i in range(64)])


if __name__ == "__main__":
    out_dir='../out'
    now=datetime.datetime.now()
    now_str=now.strftime("%Y:%m:%d:%H:%M:%S")
    out_name=out_dir+"/test_"+now_str+".wav"

    f=lambda x:shepard_tone_d(440,1,x)

    audio_out(f).wav_out(out_name)
