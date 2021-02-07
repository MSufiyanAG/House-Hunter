import time
import pandas as pd
from clean_data import CleanData
from encoding import EncodeData

class Correlation():
    def __init__(self, data):
        self.__data = data
        self.__features = list()

    def corr_fit(self):
        self.__data.drop(['facing','gym','swimmingPool'],axis=1,inplace=True)
        self.__calculateCorrelation()   
        return self.__data

    def __calculateCorrelation(self):
        data_corr = self.__data.corr()
        data_corr = data_corr['rent_amount']

        for i in range(data_corr.shape[0]):
            if data_corr[i] >= 0.1:
                self.__features.append(data_corr.index[i])

        self.__data = self.__data[self.__features]        


""" start = time.time()
clean_data = CleanData("NO-CHANGES\hyd_v2.csv")
data = clean_data.fit()
encode_data = EncodeData(data)  
data = encode_data.fit()
corr = Correlation(data)
data = corr.corr_fit()
print(data.columns)



print("Total time taken:", time.time() - start) """