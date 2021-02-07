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
        self.__propert_size()
        self.__Floor()
        self.__balconies()
        self.__bathrooms()
        self.__maintenanceAmount()
        self.__ResetAllIndex()
        self.__cleanLocality()
        self.__encode()
        self.__ResetAllIndex()

    def __balconies(self):
        self.__data['Balcony']=np.nan
        self.__data.loc[self.__data['balconies'] == "None", 'Balcony'] = self.__data.loc[self.__data['balconies'] == "None", 'Balcony'].fillna('0')
        self.__data["balconies"].replace({"None": -1}, inplace=True)
        self.__data['balconies']=self.__data['balconies'].astype(int)
        self.__data=self.__data[self.__data['balconies']<10]
        self.__data.loc[self.__data['balconies'] == 0, 'Balcony'] = self.__data.loc[self.__data['balconies'] == 0, 'Balcony'].fillna('0')
        self.__data.loc[self.__data['balconies'] == 5, 'Balcony'] = self.__data.loc[self.__data['balconies'] == 5, 'Balcony'].fillna('4+')
        self.__data.loc[self.__data['balconies'] == 6, 'Balcony'] = self.__data.loc[self.__data['balconies'] == 6, 'Balcony'].fillna('4+')
        self.__data.loc[self.__data['balconies'] == 1, 'Balcony'] = self.__data.loc[self.__data['balconies'] == 1, 'Balcony'].fillna('1')
        self.__data.loc[self.__data['balconies'] == 2, 'Balcony'] = self.__data.loc[self.__data['balconies'] == 2, 'Balcony'].fillna('2')
        self.__data.loc[self.__data['balconies'] == 3, 'Balcony'] = self.__data.loc[self.__data['balconies'] == 3, 'Balcony'].fillna('3')
        self.__data.loc[self.__data['balconies'] == 4, 'Balcony'] = self.__data.loc[self.__data['balconies'] == 4, 'Balcony'].fillna('4')
        self.__data.drop('balconies',axis=1,inplace=True)

    def __propertyCondition(self):
        self.__data.loc[self.__data['property_age'] == 0, 'condition'] = self.__data.loc[self.__data['property_age'] == 0, 'condition'].fillna('0')  
        self.__data.loc[self.__data['property_age'] <= 5, 'condition'] = self.__data.loc[self.__data['property_age'] <= 5, 'condition'].fillna('1-5')  
        self.__data.loc[self.__data['property_age'] > 5, 'condition'] = self.__data.loc[self.__data['property_age'] > 5, 'condition'].fillna('5+')  
        self.__data.drop('property_age',axis=1,inplace=True)
        self.__data.rename(columns={'condition': 'property_age'}, inplace=True)

    def __ResetAllIndex(self):
        self.__data.reset_index(drop=True, inplace=True)    

    def __bathrooms(self):
        self.__data['Bathroom']=np.nan
        self.__data.loc[self.__data['bathroom'] == 1, 'Bathroom'] = self.__data.loc[self.__data['bathroom'] == 1, 'Bathroom'].fillna('1')
        self.__data.loc[self.__data['bathroom'] == 2, 'Bathroom'] = self.__data.loc[self.__data['bathroom'] == 2, 'Bathroom'].fillna('2')
        self.__data.loc[self.__data['bathroom'] == 3, 'Bathroom'] = self.__data.loc[self.__data['bathroom'] == 3, 'Bathroom'].fillna('3')
        self.__data.loc[self.__data['bathroom'] == 4, 'Bathroom'] = self.__data.loc[self.__data['bathroom'] == 4, 'Bathroom'].fillna('4')
        self.__data.loc[self.__data['bathroom'] == 5, 'Bathroom'] = self.__data.loc[self.__data['bathroom'] == 5, 'Bathroom'].fillna('5')
        self.__data.loc[self.__data['bathroom'] > 5, 'Bathroom'] = self.__data.loc[self.__data['bathroom'] > 5, 'Bathroom'].fillna('5+')
        self.__data.drop('bathroom',axis=1,inplace=True)
         

    def __maintenanceAmount(self):
        self.__data["maintenanceAmount"].replace(to_replace = "None", value ='0', inplace=True)
        self.__data['maintenanceAmount'] = self.__data['maintenanceAmount'].astype(int)
        self.__data=self.__data[(self.__data['maintenanceAmount']>=0) & (self.__data['maintenanceAmount']<3000)]
        for i in range(0,3000,100):
            self.__data.loc[(self.__data['maintenanceAmount'] >= i) & (self.__data['maintenanceAmount'] < i+100), 'maintenanceAmount'] = i
        self.__data['maintenanceAmount']=self.__data['maintenanceAmount'].astype(object)

    def __propert_size(self):
        self.__data=self.__data[(self.__data['property_size']>=100) & (self.__data['property_size']<=2000)]
        for i in range(0,2000,100):
            self.__data.loc[(self.__data['property_size'] >= i) & (self.__data['property_size'] < i+100), 'property_size'] = i  

        self.__data['property_size']=self.__data['property_size'].astype(object)    

    def __Floor(self):
        self.__data['totalFloor'] = self.__data['totalFloor'].astype(object)
        self.__data['floor'] = self.__data['floor'].astype(object)
        self.__data['floor/totalFloor']=np.nan
        self.__data['floor/totalFloor'] = self.__data.floor.astype(str).str.cat(self.__data.totalFloor.astype(str),sep="/")
        ll=self.__data['floor/totalFloor'].value_counts()
        self.__data.drop(['floor','totalFloor'],axis=1,inplace=True)

        less=[]
        for key in ll.keys():
            if(ll[key]<=20):
                    less.append(key)

        self.__data = self.__data[~self.__data["floor/totalFloor"].isin(less)]            


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
        for i in range(1,3):
            self.__data[i] = np.where((self.__data[i].notnull()), self.__data[i],  self.__data[0])

        self.__data=self.__data.loc[self.__data[0] != 'TELANGANA']
        self.__data=self.__data.loc[self.__data[0] != 'HYDERABAD']
        self.__data.drop([ 'locality', 1,2,3,4,5,6],axis=1,inplace=True)
        self.__data.rename(columns={0: 'locality'}, inplace=True)
        self.__data.locality = self.__data.locality.str.strip()
        self.__data['locality'] = self.__data['locality'].str.replace(" ","")

        loc=self.__data["locality"].value_counts()
        
        less=[]
        for key in loc.keys():
            if(loc[key]<=100):
                less.append(key)

        self.__data = self.__data[~self.__data.locality.isin(less)]          

        self.__data.replace(to_replace = less,value ="Other",inplace=True)

    def __encode(self):
        list_of_dict = list()
        count_value = ['parking', 'furnishingDesc', 'type_bhk',
                      'facing','waterSupply', 'property_age',
                      'Balcony', 'Bathroom',
                      'floor/totalFloor','locality','maintenanceAmount','property_size']
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


