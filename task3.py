import matplotlib.pyplot as plt
import sounddevice as sd
import numpy as np
import scipy as sp

def task3a():
    T = 10
    fs = 40000
    K = T*fs
    x = sd.rec(int(K), fs, channels=1, blocking=True)


    xk = x[::5]

    print(x.shape)

    sd.play(xk, fs / 5, blocking=True)
    
def task3b():

    N = 4
    wn = 3400
    z, p, k = sp.signal.butter(N, wn, analog=True, output='zpk')

    H = sp.signal.ZerosPolesGain(z, p, k)
    w, magnitudedB, phaseDeg = sp.signal.bode(H, n=1000)
    
    f = w / (np.pi * 2)
    magnitude = 10**(magnitudedB/20)
    phaseRad = phaseDeg * np.pi / 180

    
    fig , ax = plt.subplots(2 ,1)
    ax[0].stem(f, magnitude)
    ax[1].stem(f, phaseRad)

    ax[0].set_title("Magnitude spectrum |X(ω)|")
    ax[0].set_xlabel('freq Hz')
    ax[0].set_ylabel('|X(ω)|')
    ax[0].grid(True)

    ax[1].set_title("Phase spectrum ∠X(ω)")
    ax[1].set_xlabel('freq Hz')
    ax[1].set_ylabel('Phase [rad]')
    ax[1].grid(True)


    plt.tight_layout()
    # plt.show()
    
    T = 10
    fs = 40000
    K = T*fs
    x = sd.rec(int(K), fs, channels=1, blocking=True)
    t = np.arange(0, T, 1/(fs/5))

    xk = x[::5]

    print(xk.shape)
    print(t.shape)
    

    tf, xt, __ = sp.signal.lsim(H, xk, t)
    sd.play(xk, fs / 5, blocking=True)

task3b()