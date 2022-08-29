import numpy as np

def CSI(TP, FP, FN, TN=None):
    """
    Computes Critical Success Index (CSI)
    """

    metric_value = TP / (TP + FP + FN)

    return(metric_value)

