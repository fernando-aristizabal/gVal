import pandas as pd

class two_class_confusion_matrix(pd.DataFrame):

    def __init__(self, TP, FP, FN, TN=None):

        super().__init__( data={ 'TP' : TP, 'FP' : FP, 'FN' : FN, 'TN' : TN }, dtype=np.int32,
                          name='two-class confusion matrix' )

    def print_table(self):
        print('to do')
