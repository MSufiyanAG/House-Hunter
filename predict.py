import scipy
import xgboost as xgb
import numpy as np
import pandas as pd
import warnings 
warnings.filterwarnings('ignore')

def testing_xgb(data):
    data_list = list((np.array(data)).reshape(-1))

    # load bst model
    bst_model = xgb.Booster({'bthread': 2})
    bst_model.load_model('XGB.model')


    df = pd.DataFrame()
    col_names = ['f%d' % i for i in range(12)]
    df = df.append(pd.Series(data=data_list, index=col_names), ignore_index=True)

    result1 = bst_model.predict(xgb.DMatrix(df))
    
    return np.around(int(result1)), df, bst_model
