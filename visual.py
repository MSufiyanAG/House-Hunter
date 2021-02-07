import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm,skew


class Visual():
    
    def __init__(self, data):
        self.data = data
        self.columns = self.data.columns
        
    def countplot(self,column):
        plt.figure(figsize=(15,8))
        return sns.countplot(data=self.data,x=column)
        
    def heatmap(self,annot=None,cmap="YlGnBu"):
        plt.figure(figsize=(15,8))
        matrix_corr = self.data.corr()
        mask = np.zeros_like(matrix_corr)
        mask[np.triu_indices_from(mask)] = True
        return sns.heatmap(matrix_corr, linewidths=.4,annot=annot,cmap=cmap,mask=mask)
    
    def distplot(self,column):
        plt.figure(figsize=(15,8))
        return sns.distplot(self.data[column],fit=norm)
        
    def boxplot(self,column_1):
        plt.figure(figsize=(15,8))
        return sns.boxplot(x=column_1,data=self.data,palette="Set3")
    
