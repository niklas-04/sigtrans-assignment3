import matplotlib.pyplot as plt
import sounddevice as sd
import numpy as np

def task3a():
    T = 10
    fs = 40000
    K = T*fs
    x = sd.rec(int(K), fs, channels=1, blocking=True)


    xk = x[::5]

    if x.shape() == 80000:
        print("it fucking worked")

    sd.play(xk, fs, blocking=True)

task3a()