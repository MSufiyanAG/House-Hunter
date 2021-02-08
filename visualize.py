import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm,skew
import plotly.express as px
px.set_mapbox_access_token("pk.eyJ1Ijoiam9obmNlbmExMTgiLCJhIjoiY2trd25wbXRiMWYzaTJxbXMzNWRkM2FudyJ9.FHvM5KBpGwOORijMbA8p2Q")

class ExploratoryAnalysis():
    def __init__(self):
        self.data = pd.read_csv("visualize_.csv")

    def getData(self):
        return self.data    
        
    def countplot(self,column):
        plt.figure(figsize=(15,8))
        return sns.countplot(data=self.data,x=column)
        
    def heatmap(self,annot=None):
        plt.figure(figsize=(15,8))
        matrix_corr = self.data.corr()
        mask = np.zeros_like(matrix_corr)
        mask[np.triu_indices_from(mask)] = True
        return sns.heatmap(matrix_corr, linewidths=.4,annot=annot,mask=mask) 
    
    def distplot(self,column):
        plt.figure(figsize=(15,8))
        #plt.xticks(rotation = 90)
        return sns.distplot(self.data[column],fit=norm)
    
    '''
    def joint_plot(self,column_1,column_2,kind='reg'):
        plt.figure(figsize=(15,8))
        return sns.jointplot(x=column_1,y=column_2,data=self.data,kind=kind)
    '''

    def boxplot(self,column_1,column_2=None):
        plt.figure(figsize=(15,8))
        return sns.boxplot(x=column_1,y=column_2,data=self.data)
    
    '''
    def pointplot(self,column_1,column_2):
        plt.figure(figsize=(15,8))
        return sns.pointplot(x=column_1,y=column_2,data=self.data)
    '''

    '''
    def lineplot(self,column_1,column_2):
        plt.figure(figsize=(15,8))
        return sns.lineplot(x=column_1,y=column_2,data=self.data)
    '''

    def scatterplot(self,column_1,column_2):
        plt.figure(figsize=(15,8))
        return sns.scatterplot(x=column_1,y=column_2,data=self.data)


    def plotMap(self):
        return px.scatter_mapbox(self.data, lat="lat", lon="long",size="rent_amount",color='rent_amount',hover_name="locality",
            color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)   
