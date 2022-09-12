import numpy as np
import gval.two_class_confusion_table import two_class_contingency_table  

def two_class_comparison_with_negatives( candidate_map, benchmark_map,
                                         candidate_positive_value, benchmark_positive_value,
                                         candidate_negative_value, benchmark_negative_value,
                                         confusion_matrix_encoding
                                       ):

    # create agreement map
    agreement_map = Agreement_map(candidate_map)

    # determine boolean indexes of two class confusion matrix metrics
    tp = np.logical_and(candidate_map == candidate_positive_value, benchmark_map, benchmark_positive_value)
    fp = np.logical_and(candidate_map == candidate_positive_value, benchmark_map, benchmark_negative_value)
    tn = np.logical_and(candidate_map == candidate_negative_value, benchmark_map, benchmark_negative_value)
    fn = np.logical_and(candidate_map == candidate_negative_value, benchmark_map, benchmark_positive_value)
    
    # create agreement map
    agreement_map[tp] = confusion_matrix_encoding['TP']
    agreement_map[fp] = confusion_matrix_encoding['FP']
    agreement_map[tn] = confusion_matrix_encoding['TN']
    agreement_map[fp] = confusion_matrix_encoding['FP']


    return agreement_map, two_class_contingency_table(tp.sum(),fp.sum(),tn.sum(),fn.sum())

        

