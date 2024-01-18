from ..base import Filter
import numpy as np

### This follows the Audio EQ Cookbook by Robert Bristow-Johnson

def computeGain(gain_dB):
    A=np.power(10, gain_dB/40)
    return A

def compute_intermediateValues(f0, Q, sr):
    w0 = f0*2*np.pi/sr
    alpha = np.sin(w0)/(2*Q)
    return w0, alpha


class EQBand(Filter):
    def __init__(self, f0, g, Q, sr):
        super(EQBand, self).__init__(sr=sr)
        self.f0=f0
        self.g=g
        self.Q=Q
    
    def compute_intermediateValues(self, f0, g, Q, sr):
        A=computeGain(g)
        w0 = f0*2*np.pi/sr
        alpha = np.sin(w0)/(2*Q)
        return A, w0, alpha

class EQFilter(Filter):
    def __init__(self, f0, Q, sr):
        super(EQFilter, self).__init__(sr=sr)
        self.f0=f0
        self.Q=Q

        self.alpha, self.w0 = self.get_intermediateValues()
        self.b, self.a = self.get_coeffs()
    
    def get_intermediateValues(self):
        w0, alpha = compute_intermediateValues(self.f0, self.Q, self.sr)
        return w0, alpha
    
    def get_coeffs(self):
        return np.array([1]), np.array([1])
    

class AllPass(EQFilter):
    def __init__(self, f0, Q, sr):
        super(AllPass, self).__init__(f0, Q, sr)
    

    def get_coeffs(self):
        b = np.array([
             1 - self.alpha,
            -2*np.cos(self.w0),
             1 + self.alpha,
        ])
        a = np.array([
             1 + self.alpha,
            -2*np.cos(self.w0),
             1 - self.alpha,
        ])
        return b, a
