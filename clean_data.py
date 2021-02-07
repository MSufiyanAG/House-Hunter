import pandas as pd
import numpy as np

class CleanData():
    def __init__(self, PATH: str):
        self.__data = pd.read_csv(PATH)

    def fit(self):    
        self.__asint()
        self.__dropColumns()
        self.__removeOutliers()

        return self.__data
    
    def head(self):
        return self.__data.head()

    def shape(self):
        return self.__data.shape

    def dtypes(self):
        return self.__data.dtypes    

    def __asint(self):
        self.__data.loc[self.__data['maintenanceAmount'] == "None", 'maintenanceAmount'] = 0
        self.__data.loc[self.__data['balconies'] == "None", 'balconies'] = 0
        self.__data['balconies'] = self.__data['balconies'].astype('int64')
        self.__data['maintenanceAmount'] = self.__data['maintenanceAmount'].astype('int64')

    def __dropColumns(self):
        columns_drop = [
            'combineDescription','weight','id','localityId','shortUrl','propertyTitle','amenities',
            'location','propertyType','reactivationSource','facingDesc','ownerName','completeStreetName',
            'parkingDesc','loanAvailable','active','sharedAccomodation','deposit'
        ]
        self.__data.drop(columns_drop, axis=1, inplace=True)
        self.__data.drop(self.__data[self.__data['rent_amount'] <= 0].index ,inplace=True)
        self.__data.dropna(inplace=True)

    def __removeOutliers(self):    
        self.__data = self.__data[(self.__data['property_age']>-1) & (self.__data['property_age']<15)]
        self.__data['condition'] = np.nan
        self.__data['totalfloors'] = np.nan
        self.__data['Floor'] = np.nan
        self.__data['maintenanceAmt']=np.nan
        
    def save(self):
        self.__data.to_csv("cleaned_data.csv",index=False) 
        