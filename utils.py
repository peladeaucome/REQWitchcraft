import numpy as np

def dB20(x):
    return 20*np.log10(np.abs(x))

def dB10(x):
    return 20*np.log10(np.abs(x))

def idB20(x):
    return np.power(10, x/20)

def idB10(x):
    return np.power(10, x/20)