import time
import pandas as pd
import numpy as np
from clean_data import CleanData
from encoding import EncodeData
from correlation import Correlation
from split import SplitData
from xgboost import XGBRegressor
from sklearn import model_selection
import xgboost as xgb
from sklearn import metrics
import scipy

class XGBReg():
    def __init__(self, X_train, X_test):
        self.__X_train = X_train
        self.__X_test = X_test
        self.__xgbRegression = XGBRegressor(n_jobs=-1)
        self.__params = {
            'max_depth':6,
            'min_child_weight': 1,
            'eta':.3,
            'subsample': 1,
            'colsample_bytree': 1,
            'objective':'reg:squarederror',
            'eval_metric':'mae'
        }
        self.__params_dict = dict()
        self.__dtrain = None
        self.__dtest = None
        self.__model = None

    def fit_(self):
        X = self.__X_train.drop('rent_amount_boxcox',axis=1)
        y = self.__X_train['rent_amount_boxcox']
        self.__dtrain = xgb.DMatrix(X, label=y)
        X_ = self.__X_test.drop('rent_amount_boxcox',axis=1)
        y_ = self.__X_test['rent_amount_boxcox']
        self.__dtest = xgb.DMatrix(X_, label=y_)
        self.__model = xgb.train(
            self.__params,
            self.__dtrain,
            num_boost_round=999,
            evals=[(self.__dtest, "Test")],
            early_stopping_rounds=10
        )

        return metrics.mean_absolute_error(self.__model.predict(self.__dtest), y_)

    def save_XGBmodel(self):
        self.__model.save_model("XGB.model")



    """ def decide_params(self):
        X = self.__X_train.drop('rent_amount_boxcox',axis=1)
        y = self.__X_train['rent_amount_boxcox']
        self.__dtrain = xgb.DMatrix(X, label=y)
        X_ = self.__X_test.drop('rent_amount_boxcox',axis=1)
        y_ = self.__X_test['rent_amount_boxcox']
        self.__dtest = xgb.DMatrix(X_, label=y_)

        gridsearch_params = [
            (max_depth, min_child_weight, subsample, colsample, eta)
            for max_depth in range(9,12)
            for min_child_weight in range(5,8)
            for subsample in [i/10. for i in range(7,11)]
            for colsample in [i/10. for i in range(7,11)]
            for eta in [.3, .2, .1, .05, .01, .005, .001]
        ]

        min_mae = float("Inf")
        best_params = None
        for max_depth, min_child_weight, subsample, colsample, eta in gridsearch_params:
            print("CV with max_depth={}, min_child_weight={}, subsample={}, colsample={}".format(
                                    max_depth,
                                    min_child_weight,
                                    subsample,
                                    colsample))
            # Update our parameters
            self.__params_dict['max_depth'] = max_depth
            self.__params_dict['min_child_weight'] = min_child_weight
            self.__params_dict['subsample'] = subsample
            self.__params_dict['colsample_bytree'] = colsample
            self.__params_dict['eta'] = eta
            # Run CV
            cv_results = xgb.cv(
                self.__params_dict,
                self.__dtrain,
                num_boost_round=99,
                seed=42,
                nfold=5,
                metrics={'mae'},
                early_stopping_rounds=10
            )
            # Update best MAE
            mean_mae = cv_results['test-mae-mean'].min()
            boost_rounds = cv_results['test-mae-mean'].argmin()
            print("\tMAE {} for {} rounds".format(mean_mae, boost_rounds))
            if mean_mae < min_mae:
                min_mae = mean_mae
                best_params = (max_depth,min_child_weight, subsample, colsample, eta)

        self.__params_dict['max_depth'] = best_params[0]        
        self.__params_dict['min_child_weight'] = best_params[1]
        self.__params_dict['subsample'] = best_params[2]
        self.__params_dict['colsample_bytree'] = best_params[3]
        self.__params_dict['eta'] = best_params[4]
    

    def fit_best(self):
        X = self.__X_train.drop('rent_amount_boxcox',axis=1)
        y = self.__X_train['rent_amount_boxcox']
        self.__dtrain = xgb.DMatrix(X, label=y)

        X_ = self.__X_test.drop('rent_amount_boxcox',axis=1)
        y_ = self.__X_test['rent_amount_boxcox']
        self.__dtest = xgb.DMatrix(X_, label=y_)

        tunedModel=xgb.train(
        self.__params_dict,
        self.__dtrain,
        num_boost_round=999,
        evals=[(self.__dtest,"Test")],
        early_stopping_rounds=10)

        num_boost_round = tunedModel.best_iteration + 1

        best_model = xgb.train(
            self.__params,
            self.__dtrain,
            num_boost_round=num_boost_round,
            evals=[(self.__dtest, "Test")]
        )

        best_model.save_model("XGB.model")

        return metrics.mean_absolute_error(best_model.predict(self.__dtest), y_) """


    """ def predict(self):
        ypred = self.__xgbRegression.predict(X)
        print('MAE:', metrics.mean_absolute_error(y, ypred))
        print('MSE:', metrics.mean_squared_error(y, ypred))
        print('RMSE:', np.sqrt(metrics.mean_squared_error(y, ypred)))
        print('r2_score:', metrics.r2_score(y, ypred)) """  

    """ def test(self, lambda_):
        test_data = [[2, 1, 4, 2, 3, 0, 1, 0, 1, 5, 3, 2, 91]]
        ypred = self.__model.predict(test_data)
        return scipy.special.inv_boxcox(ypred, lambda_) """


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
xgb_ = XGBReg(X, x)
print(xgb_.fit_())
choice = input("Enter do you want to save this model.....type 'yes' to save or 'no' to ignore: ")
choice = choice.lower()

if choice == 'yes':
    xgb_.save_XGBmodel()
else:
    print("Model not saved")    



#xgb_.decide_params()
#mae = xgb_.fit_best()
#print(mae)
#print(xgb_.test(para_x))

print("Total time taken:", time.time() - start)