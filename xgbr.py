import time
import pandas as pd
import numpy as np
from clean_data import CleanData
from encoding import EncodeData
from correlation import Correlation
from split import SplitData
from xgboost import XGBRegressor
from sklearn import metrics
import scipy

class XGBReg():
    def __init__(self, X_train, X_test):
        self.__X_train = X_train
        self.__X_test = X_test
        self.__xgbRegression = XGBRegressor(n_jobs=-1)

    def fit_(self):
        X = self.__X_train.drop('rent_amount_boxcox',axis=1)
        y = self.__X_train['rent_amount_boxcox']
        self.__xgbRegression.fit(X, y)

    def predict(self):
        X = self.__X_test.drop('rent_amount_boxcox',axis=1)
        y = self.__X_test['rent_amount_boxcox']
        ypred = self.__xgbRegression.predict(X)
        print('MAE:', metrics.mean_absolute_error(y, ypred))
        print('MSE:', metrics.mean_squared_error(y, ypred))
        print('RMSE:', np.sqrt(metrics.mean_squared_error(y, ypred)))
        print('r2_score:', metrics.r2_score(y, ypred))  

    """ def test(self, lambda_):
        test_data = np.array([2, 1, 4, 2, 3, 0, 1, 0, 1, 5, 3, 2, 10])
        ypred = self.__linearRegression.predict(test_data)
        scipy.special.inv_boxcox(ypred, lambda_) """


start = time.time()
clean_data = CleanData("house_price.csv")
data = clean_data.fit()
encode_data = EncodeData(data)  
data = encode_data.fit()
corr = Correlation(data)
data = corr.corr_fit()
split = SplitData(data)
X, x = split.fit()
para_x = split.getParameters()
print(para_x)
xgb = XGBReg(X, x)
xgb.fit_()
xgb.predict()

print("Total time taken:", time.time() - start)