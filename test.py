import scipy
import xgboost as xgb
import numpy as np
import pandas as pd
import warnings 
warnings.filterwarnings('ignore')

data_list = list((np.array([3, 1, 3, 3, 2, 0, 1, 0, 0, 2, 2, 2, 125])).reshape(-1))

# load bst model
bst_model = xgb.Booster({'bthread': 2})
bst_model.load_model('XGB.model')


df = pd.DataFrame()
col_names = ['f%d' % i for i in range(13)]
df = df.append(pd.Series(data=data_list, index=col_names), ignore_index=True)

result1 = bst_model.predict(xgb.DMatrix(df))
lambda_ = 0.02336110709655923
res = scipy.special.inv_boxcox(result1[0], lambda_)
print(np.around(res, decimals=2))