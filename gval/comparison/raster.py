
import xarray
import numpy as np
from tqdm.dask import TqdmCallback
import dask

import gval.two_class_confusion_table import two_class_contingency_table  

@dask.delayed()
def contigency_table(candidate_map, benchmark_map):
    
    # use dask
    comparison_dd = dask.dataframe.concat( candidate_map.to_dask_dataframe(),
                                           benchmark_map.to_dask_dataframe() )

    # create categorical datatypes
    comparison_dd.categorize()

    # create pivot table
    ct = comparison_dd.pivot_table()

    return(ct)


def two_class_comparison( candidate_map, benchmark_map,
                          candidate_positive_value, benchmark_positive_value,
                          candidate_negative_value, benchmark_negative_value,
                          confusion_matrix_encoding
                        ):

    # create agreement map
    agreement_map = candidate_map.copy()

    # how to handle NDVs

    # determine boolean indexes of two class confusion matrix metrics
    candidate_is_positive = candidate_map == candidate_positive_value
    benchmark_is_positive = benchmark_map == benchmark_positive_value

    # computes negatives otherwise just flips positives
    if with_negatives:
        candidate_is_negative = candidate_map == candidate_negative_value
        benchmark_is_negative = benchmark_map == benchmark_negative_value
    else:
        candidate_is_negative = ~candidate_is_positive
        benchmark_is_negative = ~benchmark_is_positive

    tp = np.logical_and(candidate_is_positive, benchmark_is_positive)
    fp = np.logical_and(candidate_is_positive, benchmark_is_negative)
    tn = np.logical_and(candidate_map == candidate_negative_value, benchmark_map == benchmark_negative_value)
    fn = np.logical_and(candidate_map == candidate_negative_value, benchmark_map == benchmark_positive_value)
    
    # create agreement map
    agreement_map[tp] = confusion_matrix_encoding['TP']
    agreement_map[fp] = confusion_matrix_encoding['FP']
    agreement_map[tn] = confusion_matrix_encoding['TN']
    agreement_map[fp] = confusion_matrix_encoding['FP']


    return Agreement_map(agreement_map), two_class_contingency_table(tp.sum(),fp.sum(),tn.sum(),fn.sum())



def multi_class_comparison():
    pass

def continuous_comparison():
    pass
