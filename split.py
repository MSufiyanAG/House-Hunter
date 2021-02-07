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
    def fit(self):
        self.__split_data()

        return self.__X_train, self.__X_test

    def __split_data(self):
        self.__X_train, self.__X_test = model_selection.train_test_split(
            self.__data, test_size=0.2, random_state=100
        )     



""" start = time.time()
clean_data = CleanData("house_price.csv")
data = clean_data.fit()
encode_data = EncodeData(data)  
data = encode_data.fit()
corr = Correlation(data)
data = corr.corr_fit()
split = SplitData(data)
X, x = split.fit()
print(split.getParameters())


print("Total time taken:", time.time() - start) """