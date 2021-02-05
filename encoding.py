import warnings
warnings.filterwarnings("ignore")
import pandas as pd
pd.set_option("display.max_columns",None)
import numpy as np
import time
from clean_data import CleanData

class EncodeData():
    def __init__(self,data):
        self.__data = data
        self.__list_dict = list()

    def fit(self):
        self.__binning()

        return self.__data    

    def head(self):
        return self.__data

    def showListDict(self):
        return self.__list_dict    

    def __binning(self):
        self.__propertyCondition()
        self.__totalFloors()
        self.__Floors()
        self.__bathrooms()
        self.__maintenanceAmount()
        self.__ResetAllIndex()
        self.__cleanLocality()
        self.__encode()
        self.__ResetAllIndex()

    def __propertyCondition(self):
        self.__data.loc[self.__data['property_age'] == 0, 'condition'] = self.__data.loc[self.__data['property_age'] == 0, 'condition'].fillna('0')  
        self.__data.loc[self.__data['property_age'] <= 5, 'condition'] = self.__data.loc[self.__data['property_age'] <= 5, 'condition'].fillna('1-5')  
        self.__data.loc[self.__data['property_age'] > 5, 'condition'] = self.__data.loc[self.__data['property_age'] > 5, 'condition'].fillna('5+')  
        self.__data.drop('property_age',axis=1,inplace=True)

    def __ResetAllIndex(self):
        self.__data.reset_index(drop=True, inplace=True)    

    def __bathrooms(self):
        self.__data["bathroom"].replace({6: "5+",7: "5+",8: "5+",10: "5+",12: "5+",14: "5+"}, inplace=True)
        self.__data['bathroom'] = self.__data['bathroom'].astype(object)
         
    def __totalFloors(self):
        self.__data.loc[self.__data['totalFloor'] == 0, 'totalfloors'] = self.__data.loc[self.__data['totalFloor'] == 0, 'totalfloors'].fillna('0')
        self.__data.loc[self.__data['totalFloor'] <6, 'totalfloors'] = self.__data.loc[self.__data['totalFloor'] <6, 'totalfloors'].fillna('1-5')
        self.__data.loc[self.__data['totalFloor'] <=14, 'totalfloors'] = self.__data.loc[self.__data['totalFloor'] <=14, 'totalfloors'].fillna('6-14') 
        self.__data.loc[self.__data['totalFloor'] >14, 'totalfloors'] = self.__data.loc[self.__data['totalFloor'] >14, 'totalfloors'].fillna('14+')
        self.__data.drop('totalFloor',axis=1,inplace=True)

    def __Floors(self):
        self.__data.loc[self.__data['floor'] == 0, 'Floor'] = self.__data.loc[self.__data['floor'] == 0, 'Floor'].fillna('0')
        self.__data.loc[self.__data['floor'] <=7, 'Floor'] = self.__data.loc[self.__data['floor'] <=7, 'Floor'].fillna('1-7')
        self.__data.loc[self.__data['floor'] <=19, 'Floor'] = self.__data.loc[self.__data['floor'] <=19, 'Floor'].fillna('8-19')
        self.__data.loc[self.__data['floor'] >19, 'Floor'] = self.__data.loc[self.__data['floor'] >19, 'Floor'].fillna('19+')
        self.__data.drop('floor',axis=1,inplace=True)

    def __maintenanceAmount(self):
        self.__data["maintenanceAmount"].replace(to_replace = "None", value ='0', inplace=True)
        self.__data["maintenanceAmount"] = pd.to_numeric(self.__data["maintenanceAmount"])
        self.__data.loc[self.__data['maintenanceAmount'] == 0, 'maintenanceAmt'] = self.__data.loc[self.__data['maintenanceAmount'] == 0, 'maintenanceAmt'].fillna('0')    
        self.__data.loc[self.__data['maintenanceAmount'] <= 500, 'maintenanceAmt'] = self.__data.loc[self.__data['maintenanceAmount'] <= 500, 'maintenanceAmt'].fillna('0-500')
        self.__data.loc[self.__data['maintenanceAmount'] <= 1000, 'maintenanceAmt'] = self.__data.loc[self.__data['maintenanceAmount'] <= 1000, 'maintenanceAmt'].fillna('500-1000')
        self.__data.loc[self.__data['maintenanceAmount'] <= 1500, 'maintenanceAmt'] = self.__data.loc[self.__data['maintenanceAmount'] <= 1500, 'maintenanceAmt'].fillna('1000-1500')
        self.__data.loc[self.__data['maintenanceAmount'] <= 2000, 'maintenanceAmt'] = self.__data.loc[self.__data['maintenanceAmount'] <= 2000, 'maintenanceAmt'].fillna('1500-2000')
        self.__data.loc[self.__data['maintenanceAmount'] <= 3000, 'maintenanceAmt'] = self.__data.loc[self.__data['maintenanceAmount'] <= 3000, 'maintenanceAmt'].fillna('2000-3000')
        self.__data.loc[self.__data['maintenanceAmount'] > 3000, 'maintenanceAmt'] = self.__data.loc[self.__data['maintenanceAmount'] > 3000, 'maintenanceAmt'].fillna('3000+')
        self.__data.drop('maintenanceAmount',axis=1, inplace=True)

    def __cleanLocality(self):
        loc=self.__data["locality"].value_counts()
        
        less=[]
        for key in loc.keys():
            if(loc[key]<=1):
                less.append(key)

        self.__data = self.__data[~self.__data.locality.isin(less)]  
        self.__data['locality']=self.__data['locality'].str.upper()
        self.__data.locality = self.__data.locality.str.strip()
        self.__data=pd.concat([self.__data, self.__data['locality'].str.split(', ', expand=True)], axis=1)
        for i in range(1,6):
            self.__data[i] = np.where((self.__data[i].notnull()), self.__data[i],  self.__data[0])

        self.__data=self.__data.loc[self.__data[0] != 'TELANGANA']
        self.__data.drop([ 'locality', 1,2,3,4,5,6,7,8],axis=1,inplace=True)
        self.__data.rename(columns={0: 'locality'}, inplace=True)
        self.__data.locality = self.__data.locality.str.strip()
        features=self.__data.columns
        for feature in features:
            if self.__data[feature].dtypes == bool:
                self.__data[feature] = self.__data[feature].map({True: 1, False: 0})

        less=[]
        for key in self.__data["locality"].value_counts().keys():
            if(self.__data["locality"].value_counts()[key]<10):
                less.append(key)        

        self.__data.replace(to_replace = less,value ="Other",inplace=True)

    def __encode(self):
        list_of_dict = list()
        count_value = ['bathroom','facing', 'furnishingDesc',
            'parking', 'type_bhk', 'waterSupply', 'condition',
            'maintenanceAmt', 'totalfloors', 'Floor','locality']
        for value in count_value:
            temp = self.__data.groupby(value)['rent_amount'].mean()
            temp = temp.to_frame()
            temp = temp.sort_values(by='rent_amount',ascending=False)
            temp_dict = dict()
            j = temp.shape[0]
            for i in range(temp.shape[0]):
                temp_dict[temp.index[i]] = j
                j = j - 1        

            list_of_dict.append(temp_dict)

        for i in range(0, len(count_value)):
            self.__data[count_value[i]] = self.__data[count_value[i]].map(list_of_dict[i])

            