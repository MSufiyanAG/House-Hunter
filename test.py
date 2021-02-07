import scipy
import xgboost as xgb
import numpy as np
import pandas as pd
import warnings 
warnings.filterwarnings('ignore')


""" ['furnishingDesc', 'isMaintenance', 'lift', 'maintenanceAmount',
       'parking', 'property_size', 'rent_amount', 'type_bhk', 'waterSupply',
       'Balcony', 'Bathroom', 'floor/totalFloor', 'locality'] """


data_list = list((np.array([1,False,False,17,2,9,3,4,4,2,8,19])).reshape(-1))

# load bst model
bst_model = xgb.Booster({'bthread': 2})
bst_model.load_model('XGB.model')


df = pd.DataFrame()
col_names = ['f%d' % i for i in range(12)]
df = df.append(pd.Series(data=data_list, index=col_names), ignore_index=True)

result1 = bst_model.predict(xgb.DMatrix(df))
print(np.around(result1, decimals=2))