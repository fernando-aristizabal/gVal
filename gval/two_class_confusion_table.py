import numpy as np
import xarray as xr

class confusion_matrix():

    def __init__(self, TP, FP, FN, TN=None, legend=None):

        self.values = { 'TP' : TP, 'FP' : FP, 'FN' : FN, 'TN' : TN }
        self.legend = legend

    def print_table(self):
        

