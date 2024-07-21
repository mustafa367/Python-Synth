import numpy as np
import datetime
from matplotlib import pyplot
from scipy.io import wavfile

from tone import tone
from audio_out import audio_out

def main():
    f0 = .5
    f1 = 2
    duration = 5

    bound = lambda x: min(max(x, 0), duration)
    f = lambda x: f0 * 2 ** (np.log2(f1 / f0) * (bound(x) / duration))
    A = lambda x: -1 * np.abs(2 * (bound(x) - duration / 2) / duration) + 1
    X = np.arange(0, 5 , 1/44100)

    ## Plots to verify shape of freq and amp
    # pyplot.plot(X, [f(x) for x in X])
    # pyplot.savefig("./out/shepard_test_f.png")
    # pyplot.close()
    # pyplot.plot(X, [A(x) for x in X])
    # pyplot.savefig("./out/shepard_test_A.png")

    base_form = lambda x: A(x)*np.sin(f(x)*x*2*np.pi)
    Y = np.array([base_form(x) for x in X])
    pyplot.plot(X, Y)
    pyplot.savefig("./out/shepard_test_base_form.png")
    wav_write(Y)

    return

def wav_write(LPCM ,sample_rate=44100,
                 filename="./out"+"/test_"+datetime.datetime.now().strftime("%Y:%m:%d:%H:%M:%S")+".wav"):
    wavfile.write(filename,sample_rate, LPCM)
    return

#Wave generators
def sin(freq,amp):return lambda x:amp*np.sin(freq*2*np.pi*x)
def sawtooth(freq,amp):return lambda x:(((x%(1/freq))*freq)-.5)*2*amp
def square(freq,amp):return lambda x:amp if (sawtooth(freq,amp)(x)>0) else -1*amp
def triangle(freq,amp):return lambda x:2*(sawtooth(freq,amp)(x)*square(freq,amp)(x)-amp/2)

if __name__ == "__main__":
    main()
