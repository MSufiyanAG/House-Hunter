import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb


""" parking':2,
'balconies':1,
'furnishingDesc':4,
'type_bhk':2,
'bathroom':3,
'swimmingPool':0,
'lift':1,
'gym':0,
'isMaintenance':1,
'totalfloors':5,
'Floor':3,
'maintenanceAmt':2,
'locality' """

stock_column = st.selectbox(label='Select Parking:',options=["BOTH","TWO WHEELER","FOUR WHEELER","NONE"])
stock_column = st.selectbox(label='Select balconies:',options=["0","1","2","3","4","4+"])
stock_column = st.selectbox(label='Select furnishingDesc:',options=["UNFURNISHED","SEMIFURNISHED","FULLFURNISHED"])
stock_column = st.selectbox(label='Select type_bhk:',options=["1RK","1BHK","2BHK","3BHK","4BHK","4+BHK"])
stock_column = st.selectbox(label='Select bathroom:',options=["1","2","3","4","5","5+"])
stock_column = st.selectbox(label='Select swimmingPool:',options=["BOTH","TWO WHEELER","FOUR WHEELER","NONE"])
stock_column = st.selectbox(label='Select lift:',options=["BOTH","TWO WHEELER","FOUR WHEELER","NONE"])
stock_column = st.selectbox(label='Select gym:',options=["BOTH","TWO WHEELER","FOUR WHEELER","NONE"])
stock_column = st.selectbox(label='Select isMaintenance:',options=["BOTH","TWO WHEELER","FOUR WHEELER","NONE"])
stock_column = st.selectbox(label='Select totalfloors:',options=["BOTH","TWO WHEELER","FOUR WHEELER","NONE"])
stock_column = st.selectbox(label='Select Floor:',options=["BOTH","TWO WHEELER","FOUR WHEELER","NONE"])
stock_column = st.selectbox(label='Select maintenanceAmt:',options=["BOTH","TWO WHEELER","FOUR WHEELER","NONE"])
stock_column = st.selectbox(label='Select locality:',options=["BOTH","TWO WHEELER","FOUR WHEELER","NONE"])