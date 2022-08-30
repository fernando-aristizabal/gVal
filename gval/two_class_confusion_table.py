import numpy as np
import xarray as xr

class confusion_matrix():

    def __init__(self, tp, fp, fn, tn=None):

        self.tp = tp
        self.fp = fp
        self.fn = fn
        self.tn = tn
