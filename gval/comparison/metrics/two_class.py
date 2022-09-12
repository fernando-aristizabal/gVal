"""
Secondary metrics for two-class (binary) agreement evaluation. Uses the binary, primary metrics as input, true positive (TP), false positive (FP), false negative (FN), true negative (TN).
"""

import numpy as np

def CSI(TP, FP, FN, TN=None):
    """
    Computes Critical Success Index (CSI)

    Parameters
    ----------

    Returns
    -------

    Raises
    ------

    Notes
    -----
    
    References
    ----------

    Examples
    --------
    """

    metric_value = TP / (TP + FP + FN)

    return(metric_value)


def POD(TP, FP, FN, TN=None):
    """
    Computes Probability of Detection (POD)
    """

    metric_value = TP / (TP + FP)

    return(metric_value)


def FAR(TP, FP, FN, TN=None):
    """
    Computes False Alarm Rate (FAR)
    """

    metric_value = FN / (TP + FP)

    return(metric_value)
