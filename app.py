import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import xgboost as xgb
import scipy
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import time
import base64
from pathlib import Path
import shap
from predict import testing_xgb
from visualize import ExploratoryAnalysis
import plotly.express as px
import webbrowser
from bokeh.models.widgets import Div

st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

EA = ExploratoryAnalysis()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")


def main():


    def img_to_bytes(img_path):
        img_bytes = Path(img_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return encoded

    st.sidebar.title('**MENU**')

    sidebar=("https://media.giphy.com/media/l0IylQoMkcbZUbtKw/giphy.gif")
    sidebar_html = "<img  style= 'vertical-align: bottom' src='data:image/gif;base64,{}' class='img-fluid'>".format(
    img_to_bytes("hh.gif")
        )
    st.sidebar.markdown(
    sidebar_html, unsafe_allow_html=True,
    )

    
    activities=["[$$-PREDICTION-$$]","[-ABOUT-]","[-VISUALISATION-]","[-HYDERABAD-]"]
    graphs=["HEAT-MAP","COUNT-PLOT","DISTRIBUTION-PLOT","SCATTER-PLOT","BOX-PLOT"]
    choice = st.sidebar.selectbox("Select",activities)



    st.sidebar.write("----------------------------")

    st.sidebar.title('**CONTRIBUTORS**')
    st.sidebar.write('''
                    -------------------------------

                    **Syed Mahboob Abrar Ali**                    
                    1604-18-733-088

                    **Mohd Abdul Azeem**                         
                    1604-18-733-089
                    
                    **Mohammed Sufiyan Abdullah Ghori**          
                    1604-18-733-094

                    -------------------------------

                ''')

        
    #gitHub = 'https://github.com/MSufiyanAG/House-Hunter'
    #if st.sidebar.butotn('GITHUB Link'):
        #webbrowser.open_new_tab(gitHub)

    if st.sidebar.button('GITHUB Link'):
        js="window.open('https://github.com/MSufiyanAG/House-Hunter')"
        html='<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)


        
    



    if choice=="[$$-PREDICTION-$$]" :

        image = Image.open('HH.png')
        st.image(image, use_column_width=True)
        html_temp = """
        <div style="background-color:SeaGreen;padding:10px">
        <h2 style="color:white;text-align:center;">Streamlit Price Prediction ML App </h2>
        </div>
        """


        st.header("**PARKING**")
        parking_col = st.selectbox(label='',options=["BOTH","TWO_WHEELER","FOUR_WHEELER","NONE"])
        st.write("--------------------------------")

        st.header("**BALCONIES**")
        #balconies_col = st.selectbox(label='',options=["0","1","2","3","4","4+"])
        balconies_col=st.selectbox('',options=['0', '1', '2', '3', '4', '4+'])
        st.write("--------------------------------")

        st.header("**FURNISHING**")
        furnsihing_col = st.selectbox(label='',options=["UN FURNISHED","SEMI FURNISHED","FULLY FURNISHED"])
        st.write("--------------------------------")

        st.header("**BHK:**")
        #bhk_col = st.selectbox(label='',options=["1RK","1BHK","2BHK","3BHK","4BHK","4+BHK"])
        bhk_col=st.selectbox('',options=["1RK","1BHK","2BHK","3BHK","4BHK","4+BHK"])
        st.write("--------------------------------")

        st.header("**PROPERTY SIZE  in sq_ft**")
        propertySize_col = st.selectbox(label='',options=['100', '200', '300', '400', '500',
                                                        '600', '700', '800', '900', '1000', 
                                                        '1100', '1200', '1300', '1400', '1500',
                                                        '1600', '1700', '1800', '1900'])
        st.write("--------------------------------")

        st.header("**BATHROOMS**")
        bath_col = st.selectbox(label='',options=["1","2","3","4","5","5+"])
        st.write("--------------------------------")

        st.header("**WATER FACILITY**")
        water_col = st.selectbox(label='',options=['CORPORATION & BORE', 'BOREWELL', 'CORPORATION', 'None'])
        st.write("--------------------------------")


        st.header("**LIFT**")
        #lift_col = st.selectbox(label='',options=["YES !","NO!"])
        lift_col=st.radio('Select',["YES","NO"])
        st.write("--------------------------------")



        st.header("** FLOOR **")
        f_tf_col = st.selectbox(label='',options=['0/0', '0/1', '0/2', '0/3', '0/4',
                                                '0/5','1/1','1/2','1/3','1/4','1/5',
                                                '1/6','2/2', '2/3', '2/4', '2/5', '2/6',
                                                '3/3', '3/4', '3/5','3/6','4/4', '4/5',
                                                '4/6','5/5', '5/6', '6/6'])
        st.write("--------------------------------")


        st.header("**MAINTENANCE**")
        #isMaintenance_col = st.selectbox(label='',options=["NO!","YES!"])
        isMaintenance_col=st.radio('Necessary ?',["YES","NO"])
        st.write("--------------------------------")

        if isMaintenance_col=="YES":
            st.header("**MAINTENANCE AMOUNT**")
            maintenance_col = st.selectbox(label='',options=['0', '100', '200', '300', '400',
                                                            '500', '600', '700', '800', '900',
                                                            '1000', '1100', '1200', '1300', 
                                                            '1400', '1500', '1600', '1700', 
                                                            '1800', '1900', '2000', '2100',
                                                            '2200', '2300', '2400', '2500',
                                                            '2600', '2700', '2800', '2900'])

        else :
            st.header("**MAINTENANCE AMOUNT**")
            maintenance_col = st.selectbox(label='',options=['0'])

        st.write("--------------------------------")
        

        st.header("**LOCALITY**")
        locality_col = st.selectbox(label='',options=['BANJARAHILLS', 'MADHAPUR', 'KONDAPUR', 'GACHIBOWLI', 
                                                        'MANIKONDA', 'TOLICHOWKI', 'MEHDIPATNAM',
                                                        'SHAIKPET', 'SERILINGAMPALLY', 'BEGUMPET',
                                                        'MIYAPUR', 'PRAGATHINAGAR', 'KUKATPALLY', 'NIZAMPET', 
                                                        'CHANDANAGAR', 'HAFEEZPET', 'ATTAPUR', 'SERILINGAMPALLE',
                                                        'other', 'YOUSUFGUDA', 'NAGOLE', 'AMBERPET', 'BORABANDA',
                                                        'UPPAL', 'VANASTHALIPURAM', 'RAMACHANDRAPURAM',
                                                        'MALKAJGIRI', 'BODUPPAL'])



        
        st.write('\n\n')
        st.write('\n\n')
        st.write('\n\n')
        st.write('\n\n')


        yes_no_dict={'YES':True,'NO':False}
        balconies_dict={'4': 6, '3': 5, '2': 4, '4+': 3, '1': 2, '0': 1}
        bath_dict={'5+': 5, '4': 4, '3': 3, '2': 2, '1': 1}
        furnsihing_dict= {"FULLY FURNISHED": 3, 'SEMI FURNISHED': 2, 'UN FURNISHED': 1}
        parking_dict= {'FOUR_WHEELER': 4, 'BOTH': 3, 'TWO_WHEELER': 2, 'NONE': 1}
        bhk_dict={'4+BHK': 6, '4BHK': 5, '3BHK': 4, '2BHK': 3, '1BHK': 2, '1RK': 1}
        water_dict={'CORPORATION & BORE': 4, 'BOREWELL': 3, 'CORPORATION': 2, 'None': 1}
        f_tf_dict={'4/6': 27, '5/6': 26, '2/6': 25, '4/5': 24, '1/6': 23, '1/5': 22, '2/5': 21, '3/5': 20, '5/5': 19, '3/6': 18, '6/6': 17, '1/4': 16, '2/4': 15, '0/5': 14, '3/4': 13, '4/4': 12, '0/4': 11, '1/3': 10, '0/3': 9, '2/3': 8, '1/2': 7, '3/3': 6, '1/1': 5, '2/2': 4, '0/1': 3, '0/2': 2, '0/0': 1}
        maintenance_dict= {'2700': 30, '2800': 29, '2600': 28, '2500': 27, '2300': 26, '2200': 25, '2900': 24, '2100': 23, '2400': 22, '2000': 21, '1900': 20, '1600': 19, '1800': 18, '1700': 17, '1500': 16, '1200': 15, '1300': 14, '1400': 13, '1000': 12, '1100': 11, '900': 10, '800': 9, '0': 8, '700': 7, '600': 6, '500': 5, '300': 4, '400': 3, '100': 2, '200': 1}
        propertySize_dict={'1900': 19, '1700': 18, '1800': 17, '1600': 16, '1500': 15, '1400': 14, '1300': 13, '1200': 12, '1100': 11, '1000': 10, '900': 9, '800': 8, '700': 7, '600': 6, '500': 5, '400': 4, '300': 3, '200': 2, '100': 1}
        locality_dict={'BANJARAHILLS': 28, 'MADHAPUR': 27, 'KONDAPUR': 26, 'GACHIBOWLI': 25, 'MANIKONDA': 24, 'TOLICHOWKI': 23, 'MEHDIPATNAM': 22, 'SHAIKPET': 21, 'SERILINGAMPALLY': 20, 'BEGUMPET': 19, 'MIYAPUR': 18, 'PRAGATHINAGAR': 17, 'KUKATPALLY': 16, 'NIZAMPET': 15, 'CHANDANAGAR': 14, 'HAFEEZPET': 13, 'ATTAPUR': 12, 'SERILINGAMPALLE': 11, 'other': 10, 'YOUSUFGUDA': 9, 'NAGOLE': 8, 'AMBERPET': 7, 'BORABANDA': 6, 'UPPAL': 5, 'VANASTHALIPURAM': 4, 'RAMACHANDRAPURAM': 3, 'MALKAJGIRI': 2, 'BODUPPAL': 1}


################################
        parking=parking_dict.get(parking_col)
        balcony=balconies_dict.get(balconies_col)
        furnishing=furnsihing_dict.get(furnsihing_col)
        bhk=bhk_dict.get(bhk_col)
        bathroom=bath_dict.get(bath_col)
        lift=yes_no_dict.get(lift_col)
        maintanance=yes_no_dict.get(isMaintenance_col)
        f_tf=f_tf_dict.get(f_tf_col)
        maintananceAmt=maintenance_dict.get(maintenance_col)
        locality=locality_dict.get(locality_col)
        propertySize=propertySize_dict.get(propertySize_col)
        water=water_dict.get(water_col)

        acc, df, bst_model = testing_xgb([furnishing,maintanance,lift,maintananceAmt,parking,propertySize,bhk,water,balcony,bathroom,f_tf,locality]) 
        if st.button(' HUNT FOR HOUSES '):
            with st.spinner(text=":tophat: Our HOUSE HUNTERS are at work :tophat:"):
                time.sleep(1)
                st.warning(':space_invader:   :house:   :space_invader: ')
                st.balloons()
                st.success("Predicted Rent Price : ₹ {}".format(acc))
                st.success("Rent can vary between ₹ {} -- ₹ {} ".format(acc-2000,acc+2000))
                
 
                


    elif choice == "[-ABOUT-]":

        st.title("\n ** :tophat: HouseHunter :tophat: ** \n")
        st.write("-----------")
        st.header("PROBLEM")
        st.write('''

                :o: When people migrate to new cities in search of jobs , 
                        they tend to look for Rental Houses rather than purchasing 
                        the property right away.

                :o: Finding an appropriate Rental House can be a 
                        very tedious task especially in a new city.

                :o: It’s almost impossible to predict and find a
                        suitable house for rent within our Budget and needs.

                ''')


        st.write("-----------")
        st.header("SOLUTION")
        st.write('''
                :ballot_box_with_check: We propose to Digitize this process 

                :ballot_box_with_check: A Web Application that can predict House Rental Prices in Hyderabad City

                :ballot_box_with_check: This Web App will predict the House Rental Price based on customers preferences and needs

                ''')


        st.write("-----------")
        st.header("DATA can be found here : ")
        
        url = 'https://www.nobroker.in/property/sale/hyderabad/Hyderabad?searchParam=W3sibGF0IjoxNy4zODUwNDQsImxvbiI6NzguNDg2NjcxLCJwbGFjZUlkIjoiQ2hJSng5THI2dHFaeXpzUnd2dTZrb08zazY0IiwicGxhY2VOYW1lIjoiSHlkZXJhYmFkIn1d&radius=2.0'
        if st.button('NO BROKER'):
            js="window.open('https://www.nobroker.in/property/sale/hyderabad/Hyderabad?searchParam=W3sibGF0IjoxNy4zODUwNDQsImxvbiI6NzguNDg2NjcxLCJwbGFjZUlkIjoiQ2hJSng5THI2dHFaeXpzUnd2dTZrb08zazY0IiwicGxhY2VOYW1lIjoiSHlkZXJhYmFkIn1d&radius=2.0')"
            html='<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)


        st.write("-----------")
        st.header("LIFE CYCLE")
        image1 = Image.open('life.png')
        st.image(image1, use_column_width=True)
        html_temp = """
        <div style="background-color:SeaGreen;padding:10px">
        <h2 style="color:white;text-align:center;">Streamlit Price Prediction ML App </h2>
        </div>
        """
        st.write("-----------")






    elif choice == "[-VISUALISATION-]" :

        st.title("** VISUALISATION **")
        graphChoice = st.selectbox("Select",graphs)
        

        if graphChoice == 'HEAT-MAP':
            st.write("-----------")
            st.header("CORRELATION HEAT MAP")
            st.write('''
            Checking correlations is an important part of the exploratory data analysis process. 

            This analysis is one of the methods used to decide which features affect the target variable the most, 
            and in turn, get used in predicting this target variable. 

            In other words, it’s a commonly-used method for feature selection in machine learning.
            ''')
            fig=EA.heatmap()
            st.pyplot()
            st.write("-----------")


        elif graphChoice == 'COUNT-PLOT':

            st.write("---------------")
            st.header(" COUNT PLOT ")
            st.write('''
            A countplot is kind of like a histogram or a bar graph for some categorical area. 
            
            It simply shows the number of occurrences of an item based on a certain type of category.
            ''')
            choice = st.selectbox(label='',options=['balconies','bathroom','facing','floor','furnishingDesc','gym','isMaintenance','lift','parking','property_age','totalFloor','type_bhk','waterSupply'])
            fig = EA.countplot(choice)
            st.pyplot()
            st.write("---------------")

        elif graphChoice == 'DISTRIBUTION-PLOT':

            st.write("---------------")
            st.header(" DISTRIBUTION PLOT ")
            st.write('''
            A distribution plot, as the name suggests is used for one purpose .

            i.e. displaying the distribution and range of data values over a scale.
            ''')
            choice = st.selectbox(label='',options=['maintenanceAmount','property_size','rent_amount'])
            fig = EA.distplot(choice)
            st.pyplot()
            st.write("---------------")

        elif graphChoice == 'SCATTER-PLOT':
    
            st.write("---------------")
            st.header(" SCATTER PLOT ")
            st.write('''
            Scatter Plot represents the relationship between two continuous values, respectively. 
            
            It depicts how one data variable gets affected by the other data variable in every fraction of the value of the data set.

            ''')
            choice_1 = st.selectbox(label='First column ',options=['maintenanceAmount','property_size','rent_amount'])
            choice_2 = st.selectbox(label='Second column ',options=['maintenanceAmount','property_size','rent_amount'])        
            fig = EA.scatterplot(choice_1, choice_2)
            st.pyplot()
            st.write("---------------")


        elif graphChoice == 'BOX-PLOT':

            st.write("---------------")
            st.header(" BOX PLOT ")
            st.write('''
            A boxplot is a standardized way of displaying the distribution of data based on a five number summary
            
             (“minimum”, first quartile (Q1), median, third quartile (Q3), and “maximum”). 
             
             It can tell you about your outliers and what their values are.
            ''')
            image = Image.open('box.jpeg')
            st.image(image, use_column_width=True)
            html_temp = """
            <div style="background-color:SeaGreen;padding:10px;">
            <h2 style="color:white;text-align:center;">Streamlit Price Prediction ML App </h2>
            </div>
            """

            st.write("---------------")
            choice_1 = st.selectbox(label='Column VS RENT_AMOUNT',options=['balconies','bathroom','facing','floor','furnishingDesc','gym','isMaintenance','lift','parking','property_age','totalFloor','type_bhk','waterSupply'])
            #choice_2 = st.selectbox(label='Select the second column for Box plot:',options=['balconies','bathroom','facing','floor','furnishingDesc','gym','isMaintenance','lift','parking','property_age','totalFloor','type_bhk','waterSupply'])        
            fig = EA.boxplot(choice_1, 'rent_amount')
            st.pyplot()
            st.write("---------------")




    elif choice=='[-HYDERABAD-]':
        st.title("** HYDERABAD MAP **")
        st.write("-------------------")
        fig = EA.plotMap()
        st.plotly_chart(fig)



# ["COUNT-PLOT","DISTRIBUTION-PLOT","LINE-PLOT","BOX-PLOT"]





    



##################33

if __name__ == '__main__':
    main()
