import numpy as np
import matplotlib.pyplot as plt
import filters
import utils

def dB20(x):
    return 20*np.log(np.abs(x))

fc = 1000
sr = 44100
n_fft = 8192

f = np.fft.rfftfreq(n=n_fft, d=1/sr)

lpf = filters.butterworth.LP2(fc=fc, sr=sr)

plt.plot(f, dB20(lpf.get_rfft(n=n_fft)))
plt.xlim(20, 20000)
plt.ylim(-60, 5)
plt.semilogx()
plt.show()