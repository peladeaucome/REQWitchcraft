import numpy as np

from .base import Filter, Series
import filters.equalizer.RBJ as RBJ


class LP2(Filter):
    """2nd order lowpass butterworth filter"""
    def __init__(self, f0, sr=44100):
        super(LP2, self).__init__(sr=sr)

        self.b, self.a = self.compute_coeffs(f0=f0)

    def compute_coeffs(self, f0):
        om0 = 2*np.pi*f0/self.sr
        om02 = np.square(om0)
        b = np.array([1, 2, 1])
        a = np.array([
            (4+2*np.sqrt(2)*om0+om02)/om02,
            (2*om02-8)/om02,
            (4-2*np.sqrt(2)*om0+om02)/om02
        ])
        return b, a


class HP2(Filter):
    """2nd order highpass butterworth filter"""
    def __init__(self, f0, sr=44100):
        super(HP2, self).__init__(sr=sr)

        self.b, self.a = self.compute_coeffs(f0=f0)

    def compute_coeffs(self, f0):
        om0 = 2*np.pi*f0/self.sr
        om02 = np.square(om0)
        b = np.array([1, -2, 1])*4
        a = np.array([
            (4+2*np.sqrt(2)*om0+om02),
            (2*om02-8),
            (4-2*np.sqrt(2)*om0+om02)
        ])
        return b, a

class LP4(Series):
    """4th order lowpass butterworth filter"""
    def __init__(self, f0, sr=44100):
        super(LP4, self).__init__(
            RBJ.LowPass(f0=f0, Q=0.54, sr=sr),
            RBJ.LowPass(f0=f0, Q=1.31, sr=sr),
            sr=sr
        )

class HP4(Series):
    """4th order lowpass butterworth filter"""
    def __init__(self, f0, sr=44100):
        super(HP4, self).__init__(
            RBJ.HighPass(f0=f0, Q=0.54, sr=sr),
            RBJ.HighPass(f0=f0, Q=1.31, sr=sr),
            sr=sr
        )