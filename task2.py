import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

sample_start = 0
sample_end = 5
omega = 2000 * np.pi


def task2a():
    minimum_sampling_frequency = 2000
    samplingPeriod_a = 1/minimum_sampling_frequency

    tk_a = np.arange(sample_start, sample_end, samplingPeriod_a)
    xk_a = np.array([])

    for t in tk_a:
        xk_a = np.append(xk_a, np.cos(omega * t))

    
    fig, ax = plt.subplots()

    ax.stem(tk_a, xk_a, label="xk_a")

    ax.set_title("Xk: 2kHz")
    ax.set_xlabel("time (s)")
    ax.set_ylabel('Xk(t)')
    ax.grid(True)

    ax.set_xlim(0, 10 * 10**-3)
    ax.set_ylim(-1.1, 1.1)

    plt.show()



def task2b():
    sampling_frequency_b = 10000
    samplingPeriod_b = 1/sampling_frequency_b

    tk_b = np.arange(sample_start, sample_end, samplingPeriod_b)
    xk_b = np.array([])

    for t in tk_b:
        xk_b = np.append(xk_b, np.sin(omega * t))

    fig, ax = plt.subplots()

    ax.stem(tk_b, xk_b, label="xk_a")

    ax.set_title("Xk: 10kHz")
    ax.set_xlabel("time (s)")
    ax.set_ylabel('Xk(t)')
    ax.grid(True)

    ax.set_xlim(0, 10 * 10**-3)
    ax.set_ylim(-1.1, 1.1)

    plt.show()
    #sd.play(xk_b, sampling_frequency_b, blocking=True)

task2b()