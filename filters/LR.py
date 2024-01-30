### Linkwitz-Riley Filters
from .base import Filter, Series
from . import butterworth


class LP4(Series):
    def __init__(self, f0, sr=44100):
        super(LP4, self).__init__(
            butterworth.LP2(f0=f0, sr=sr),
            butterworth.LP2(f0=f0, sr=sr),
            sr=sr
        )

class HP4(Series):
    def __init__(self, f0, sr=44100):
        super(HP4, self).__init__(
            butterworth.HP2(f0=f0, sr=sr),
            butterworth.HP2(f0=f0, sr=sr),
            sr=sr
        )