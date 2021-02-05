import time
import pandas as pd
import numpy as np
from clean_data import CleanData
from encoding import EncodeData
from correlation import Correlation
from split import SplitData
from sklearn import ensemble
from sklearn import metrics
from sklearn import model_selection
import scipy

class RandomReg():
    def __init__(self, X_train, X_test):
        self.__X_train = X_train
        self.__X_test = X_test
        self.__randomRegression = ensemble.RandomForestRegressor()
        self.__param_grid = {
            'max_depth': [10, 30, 50],
            'min_samples_leaf': [2, 3, 4],
            'min_samples_split': [5, 10, 15],
            'n_estimators': [100, 300, 500, 1000],
            'max_samples':[0.1, 0.2]
        }
    

    def fit_(self):
        X = self.__X_train.drop('rent_amount_boxcox',axis=1)
        y = self.__X_train['rent_amount_boxcox']
        grid_search = model_selection.GridSearchCV(estimator = self.__randomRegression, param_grid = self.__param_grid,cv = 5, n_jobs = -1, verbose = 10)
        grid_search.fit(X, y)
        best_param = grid_search.best_params_
        best_grid = grid_search.best_estimator_
        self.__predict(best_grid)

    def __predict(self, model):
        X = self.__X_test.drop('rent_amount_boxcox',axis=1)
        y = self.__X_test['rent_amount_boxcox']
        ypred = model.predict(X)
        print('MAE:', metrics.mean_absolute_error(y, ypred))
        print('MSE:', metrics.mean_squared_error(y, ypred))
        print('RMSE:', np.sqrt(metrics.mean_squared_error(y, ypred)))
        print('r2_score:', metrics.r2_score(y, ypred))  

    def test(self, lambda_):
        test_data = [[2, 3, 2, 2, 0, 0, 0, 2, 2, 91]]
        ypred = self.__randomRegression.predict(test_data)
        res = scipy.special.inv_boxcox(ypred, lambda_)
        res_predict = scipy.special.inv_boxcox(self.__X_test['rent_amount_boxcox'].head(1).values,lambda_)
        return res, self.__X_test.drop('rent_amount_boxcox',axis=1).head(1), res_predict


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
rf = RandomReg(X, x)
rf.fit_()
#rf.predict()
#print(rf.test(para_x))

print("Total time taken:", time.time() - start)