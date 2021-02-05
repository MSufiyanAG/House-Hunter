import time
import pandas as pd
from clean_data import CleanData
from encoding import EncodeData
from correlation import Correlation
from sklearn import model_selection
from scipy import stats

class SplitData():
    def __init__(self, data):
        self.__data = data
        self.__X_train = None
        self.__X_test = None
        self.__params = None
    def fit(self):
        self.__split_data()
        self.__boxcox_target()

        return self.__X_train, self.__X_test

    def getParameters(self):
        return self.__params

    def __split_data(self):
        self.__X_train, self.__X_test = model_selection.train_test_split(
            self.__data, test_size=0.2, random_state=100
        )     

    def __boxcox_target(self):
        self.__X_train['rent_amount_boxcox'],self.__params = stats.boxcox(self.__X_train['rent_amount'])
        self.__X_test['rent_amount_boxcox'] = stats.boxcox(self.__X_test['rent_amount'],self.__params)

        self.__X_train.drop('rent_amount',axis=1,inplace=True)
        self.__X_test.drop('rent_amount',axis=1,inplace=True)



""" start = time.time()
clean_data = CleanData("house_price.csv")
data = clean_data.fit()
encode_data = EncodeData(data)  
data = encode_data.fit()
corr = Correlation(data)
data = corr.corr_fit()
split = SplitData(data)
X, x = split.fit()
print(X)


print("Total time taken:", time.time() - start) """