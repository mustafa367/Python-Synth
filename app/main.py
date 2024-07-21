import numpy as np
import datetime
from matplotlib import pyplot
from scipy.io import wavfile

from tone import tone
from audio_out import audio_out

def main():
    f0 = 220
    f1 = 880
    duration = 12

    bound = lambda x: min(max(x, 0), duration)
    f = lambda x: f0 * 2 ** (np.log2(f1 / f0) * (bound(x) / duration))
    # A = lambda x: -1 * np.abs(2 * (bound(x) - duration / 2) / duration) + 1
    A = lambda x: -1 * np.abs(2 * (bound(x) - duration / 2) / duration) + 1
    
    base_form = lambda x: A(x)*np.sin(f(x)*x*2*np.pi)

    X = np.arange(0, 12 , 1/44100)
    Y = np.array([base_form(x) for x in X]).astype(np.float32)

    ## Plots to verify shape of freq and amp
    # pyplot.plot(X, [f(x) for x in X])
    # pyplot.savefig("./out/shepard_test_f.png")
    # pyplot.close()
    # pyplot.plot(X, [A(x) for x in X])
    # pyplot.savefig("./out/shepard_test_A.png")
    # pyplot.plot(X, Y)
    # pyplot.savefig("./out/shepard_test_base_form.png")

    n = 5
    m = 24

    # offset = int(len(Y) / 2)
    # Z = Y + np.concat([Y[offset:],Y[:offset]])
    # out = np.concat([Y[:offset]] + [Z] * 10  + [Y[offset:]])

    offset = int(len(Y) / n)
    out = np.empty(Y.size * m).astype(np.float32)
    before = 0
    after = out.size - Y.size
    for i in range(m):
        Y_padded = np.pad(Y, (before, after), 'constant', constant_values=(0, 0))
        out = out + Y_padded
        before += offset
        after -= offset

    wav_write(out)

    return

def wav_write(LPCM ,sample_rate=44100, volume = .05,
                 filename="./out"+"/test_"+datetime.datetime.now().strftime("%Y:%m:%d:%H:%M:%S")+".wav"):
    wavfile.write(filename,sample_rate, volume * LPCM)
    return

#Wave generators
def sin(freq,amp):return lambda x:amp*np.sin(freq*2*np.pi*x)
def sawtooth(freq,amp):return lambda x:(((x%(1/freq))*freq)-.5)*2*amp
def square(freq,amp):return lambda x:amp if (sawtooth(freq,amp)(x)>0) else -1*amp
def triangle(freq,amp):return lambda x:2*(sawtooth(freq,amp)(x)*square(freq,amp)(x)-amp/2)

if __name__ == "__main__":
    main()
