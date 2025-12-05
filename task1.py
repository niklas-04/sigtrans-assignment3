import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd



sample_start = 0
sample_end = 5
omega = 2000 * np.pi

sampling_frequency_a = 10000
samplingPeriod_a = 1/sampling_frequency_a

sampling_frequency_b = 1100
samplingPeriod_b = 1/sampling_frequency_b


tk_a = np.arange(sample_start, sample_end, samplingPeriod_a)
xk_a = np.array([])


for t in tk_a:
    xk_a = np.append(xk_a, np.cos(omega * t))

tk_b = np.arange(sample_start, sample_end, samplingPeriod_b)
xk_b = np.array([])

for t in tk_b:
    xk_b = np.append(xk_b, np.cos(omega * t))

fig, ax = plt.subplots(2, 1)

ax[0].stem(tk_a, xk_a, label="xk_a")
ax[1].stem(tk_b, xk_b, label="xk_b")

ax[0].set_title("Xk: 10kHz")
ax[0].set_xlabel("time (s)")
ax[0].set_ylabel('Xk(t)')
ax[0].grid(True)

ax[0].set_xlim(0, 10 * 10**-3)
ax[0].set_ylim(-1.1, 1.1)


ax[1].set_title("Xk: 1.1kHz")
ax[1].set_xlabel("time (s)")
ax[1].set_ylabel('Xk(t)')
ax[1].grid(True)

ax[1].set_xlim(0, 10 * 10**-3)
ax[1].set_ylim(-1.1, 1.1)

#plt.show()

#sd.play(xk_a, sampling_frequency_a, blocking=True)