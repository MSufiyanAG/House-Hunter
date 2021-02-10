import scipy
import xgboost as xgb
import numpy as np
import pandas as pd
pd.set_option("display.max_columns",None)
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
    #return np.around(int(result1)),df

# print(pd.read_csv("X_test.csv").columns)
# res, df = testing_xgb([2,True,True,22,3,13,4,4,24,4,2,25])
# print(df)

# neworder = ["f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11"]
# df=df.reindex(columns=neworder)
# print(df)

