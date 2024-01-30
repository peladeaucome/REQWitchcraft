import numpy as np
import scipy.signal

class Filter():
    def __init__(self, sr=44100):
        self.sr=sr
        self.a=np.array([1])
        self.b=np.array([1])
    
    def process(self, x):
        x = scipy.lfilter(b=self.b, a=self.a, x=x)
        return x
    
    def get_rfft(self, n):
        return np.fft.rfft(self.b, n=n)/np.fft.rfft(self.a, n=n)

    def get_impulseResponse(self, n):
        x = np.zeros(n)
        x[0]=1
        return self.process(x)
    

class Series(Filter):
    def __init__(self, *filters, sr):
        self.filters_list = []
        for filter in filters:
            self.filters_list.append(filter)
    
    def get_rfft(self, n):
        out = np.ones(shape=n//2+1, dtype=np.complex128)
        for filter in self.filters_list:
            out = out*filter.get_rfft(n=n)
        return out
    
    def process(self, x):
        y = x.copy()
        for filter in self.filters_list:
            y = filter.process(y)
        return y

class Parallel(Filter):
    def __init__(self, *filters, sr):
        self.filters_list = []
        for filter in filters:
            self.filters_list.append(filter)
    
    def get_rfft(self, n):
        out = np.zeros(shape=n//2+1, dtype=np.complex128)
        for filter in self.filters_list:
            out = out+filter.get_rfft(n=n)
        return out

    def process(self, x):
        y = np.zeros_like(x)
        for filter in self.filters_list:
            y = filter.process(x)
        return y