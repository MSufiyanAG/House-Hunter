import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import scipy


parking_col = st.selectbox(label='Select PARKING:',options=["BOTH","TWO_WHEELER","FOUR_WHEELER","NONE"])

balconies_col = st.selectbox(label='Select balconies:',options=["0","1","2","3","4","4+"])

furnsihing_col = st.selectbox(label='Select furnishingDesc:',options=["UN FURNISHED","SEMI FURNISHED","FULL FURNISHED"])

bhk_col = st.selectbox(label='Select type_bhk:',options=["1RK","1BHK","2BHK","3BHK","4BHK","4+BHK"])

bath_col = st.selectbox(label='Select bathroom:',options=["1","2","3","4","5","5+"])

swimming_col = st.selectbox(label='Select swimmingPool:',options=["NO","YES"])

lift_col = st.selectbox(label='Select lift:',options=["YES","NO"])

gym_col = st.selectbox(label='Select gym:',options=["YES","NO"])

isMaintenance_col = st.selectbox(label='Select isMaintenance:',options=["YES","NO"])

totalFloor_col = st.selectbox(label='Select totalfloors:',options=["0","1-5","6-14","14+"])

floor_col = st.selectbox(label='Select Floor:',options=["0","1-7","8-19","19+"])

maintenance_col = st.selectbox(label='Select maintenanceAmt:',options=["0","0-500","500-1000","1000-1500","1500-2000","2000-3000","3000+"])

locality_col = st.selectbox(label='Select locality:',options=['KOMPALLY', 'UPPARPALLY', 'WEST MARREDPALLY', 'KOTI', 'NANAKRAM GUDA', 'GACHIBOWLI', 
                                                              'BANDLAGUDA JAGIR', 'JILLALGUDA', 'KOKAPET', 'AMEERPET', 'SHIVAJI NAGAR', 'SAINIKPURI', 
                                                              'JUBILEE HILLS', 'A. S. RAO NAGAR', 'MOULA ALI', 'HAYATHNAGAR', 'AMEENPUR', 'MASAB TANK',
                                                              'RAMPALLY', 'HI-TECH CITY', 'BASHEER BAGH', 'TARNAKA', 'HAFEEZPET', 'KHAIRTABAD', 'NAGARAM', 
                                                              'RAMACHANDRAPURAM,', 'ANNOJIGUDA', 'SERLINGAMPALLI', 'KAVADIGUDA', 'OLD ALWAL', 'DILSUKHNAGAR',
                                                              'HITEC CITY', 'NALAGANDLA', 'LINGAMPALLY', 'BOWENPALLY', 'QUTUB SHAHI TOMBS', 'RAMANTHAPUR', 
                                                              'MALAKPET', 'MEERPET', 'VANASTHALIPURAM', 'HITECH CITY', 'RAJENDRANAGAR MANDAL', 'KISTAREDDYPET',
                                                              'PRAGATI NAGAR', 'PRAGATHI NAGAR', 'TELLAPUR', 'KUKATPALLY,', 'MANIKONDA', 'NANAKRAMGUDA', 
                                                              'KACHIGUDA', 'NARSINGI', 'BOLLARAM', 'NANAKARAMGUDA', 'TRIMULGHERRY', 'BADANGPET', 'BAHADURGUDA',
                                                              'METTUGUDA', 'MADHURA NAGAR', 'SERILINGAMPALLY', 'CHIKKADPALLY', 'FILM NAGAR', 'SERILINGAMPALLE', 
                                                              'BALAJI NAGAR', 'HYDERSHAKOTE', 'MALLAMPET', 'GUDIMALKAPUR', 'PADMARAO NAGAR', 'MALKAJGIRI', 'MADHAPUR',
                                                              'JAWAHAR NAGAR', 'BACHUPALLY', 'KISMATPUR', 'ALWAL', 'BHARAT HEAVY ELECTRICALS LIMITED', 'NEREDMET', 
                                                              'KHARMANGHAT', 'YAPRAL', 'AMBERPET', 'SURARAM', 'MADINAGUDA', 'MUSHEERABAD', 'BORABANDA', 'KONDAPUR,', 'KAPRA', 
                                                              'POCHARAM', 'OSMAN NAGAR', 'BANDLAGUDA', 'B N REDDY NAGAR', 'ERRAGADDA', 'KRISHNA REDDY PET', 'LANGAR HOUZ', 
                                                              'HASTINAPURAM', 'SOMAJIGUDA', 'RAM NAGAR', 'GAJULARAMARAM', 'NACHARAM', 'GOPANPALLY', 'MEHDIPATNAM', 'CHANDA NAGAR',
                                                              'MANIKONDA JAGIR', 'KARKHANA', 'GURRAM GUDA', 'SANJEEVA REDDY NAGAR', 'UPPAL', 'MOOSAPET', 'HYDERABAD', 'GOPANAPALLI',
                                                              'SHAMSHABAD', 'MADEENAGUDA', 'RAMACHANDRA PURAM', 'TOLI CHOWKI', 'JAGATHGIRI GUTTA', 'PATANCHERU', 'ADIKMET', 'NEKNAMPUR',
                                                              'OLD MALAKPET', 'YOUSUFGUDA', 'YELLA REDDY GUDA', 'RAMACHANDRAPURAM', 'SAFILGUDA', 'BEERAMGUDA', 'NALLAGANDLA', 'CHAMPAPET',
                                                              'GANDAMGUDA', 'NIZAMPET', 'HABSIGUDA', 'NEW NALLAKUNTA', 'SAIDABAD', 'MIYAPUR', 'KARMANGHAT', 'NARAYANGUDA', 'JEEDIMETLA',
                                                              'LB NAGAR', 'KUKATPALLY', 'OLD BOWENPALLY', 'NAGOLE', 'BODUPPAL', 'BAGH AMBERPET', 'CHANDANAGAR', 'MOTI NAGAR', 'IBRAHIM BAGH',
                                                              'KHAIRATABAD', 'A S RAO NAGAR', 'SUN CITY', 'PUPPALAGUDA', 'BOWRAMPET', 'ALMASGUDA', 'MANSOORABAD', 'LAKDIKAPUL', 'HI TECH CITY', 
                                                              'ZAMISTANPUR', 'KOTHAGUDA', 'KHAJAGUDA', 'PUPPALGUDA', 'SANATH NAGAR', 'BEGUMPET', 'KONDAPUR', 'WHITEFIELDS', 'ADIBATLA',
                                                              'BANDAM KOMMU', 'KOHTAGUDA', 'KUSHAIGUDA', 'PUNJAGUTTA', 'MEDIPALLY', 'L. B. NAGAR', 'PEERANCHURUVU', 'PEDDA AMBERPET',
                                                              'ATTAPUR', 'QUTHBULLAPUR', 'MAHADEVPUR COLONY', 'UPPERPALLY', 'Other', 'KAMALAPRASAD NAGAR', 'HIMAYATNAGAR', 
                                                              'BANJARA HILLS', 'SHAIKPET', 'DAMMAIGUDA', 'BOLARUM', 'BALKAMPET', 'BALANAGAR', 'EAST MARREDPALLY',
                                                              'SECUNDERABAD', 'JILLELAGUDA', 'HAKIMPET', 'BHOIGUDA', 'KOTHAPET', 'MALLAPUR', 'HYDER NAGAR', 
                                                              'PEERZADIGUDA', 'BALAPUR', 'RAMGOPALPET', 'NALLAKUNTA', 'RAIDURG KHALSA', 'SAROORNAGAR', 'RODAMESTRI NAGAR'
                                                              ])


##################33

yes_no_dict={'YES':1,'NO':0}
balconies_dict={'4+': 6, '4': 5, '3': 4, '2': 3, '1': 2, '0': 1}
bath_dict={'5+': 6, 5: 5, 4: 4, 3: 3, 2: 2, 1: 1}
furnsihing_dict= {"FULL FURNISHED": 3, 'SEMI FURNISHED': 2, 'UN FURNISHED': 1}
parking_dict= {'FOUR_WHEELER': 4, 'BOTH': 3, 'TWO_WHEELER': 2, 'NONE': 1}
bhk_dict={'4+BHK': 6, '4BHK': 5, '3BHK': 4, '2BHK': 3, '1BHK': 2, '1RK': 1}
maintenance_dict= {'3000+': 7, '2000-3000': 6, '1500-2000': 5, '1000-1500': 4, '500-1000': 3, '0': 2, '0-500': 1}
totalfloors_dict = {'14+': 4, '6-14': 3, '1-5': 2, '0': 1}
floor_dict ={'19+': 4, '8-19': 3, '1-7': 2, '0': 1}
locality_dict={'HI TECH CITY': 195, 'WHITEFIELDS': 194, 'NANAKRAMGUDA': 193, 'KOKAPET': 192, 'RAJENDRANAGAR MANDAL': 191, 'NANAKARAMGUDA': 190, 'GOPANAPALLI': 189, 'PUPPALGUDA': 188, 'BANJARA HILLS': 187, 'KHAJAGUDA': 186, 'NANAKRAM GUDA': 185, 'PEERANCHURUVU': 184, 'FILM NAGAR': 183, 'NEKNAMPUR': 182, 'KOTHAGUDA': 181, 'NARSINGI': 180, 'GACHIBOWLI': 179, 'JUBILEE HILLS': 178, 'BASHEER BAGH': 177, 'NALLAGANDLA': 176, 'KOHTAGUDA': 175, 'GOPANPALLY': 174, 'KONDAPUR': 173, 'HITEC CITY': 172, 'NALAGANDLA': 171, 'MANIKONDA': 170, 'SOMAJIGUDA': 169, 'TELLAPUR': 168, 'MADHAPUR': 167, 'HITECH CITY': 166, 'LAKDIKAPUL': 165, 'RAMGOPALPET': 164, 'PUNJAGUTTA': 163, 'MADINAGUDA': 162, 'EAST MARREDPALLY': 161, 'MADHURA NAGAR': 160, 'HYDERABAD': 159, 'HABSIGUDA': 158, 'PUPPALAGUDA': 157, 'AMEERPET': 156, 'WEST MARREDPALLY': 155, 'HAKIMPET': 154, 'MASAB TANK': 153, 'KOTI': 152, 'UPPARPALLY': 151, 'ADIBATLA': 150, 'YAPRAL': 149, 'UPPERPALLY': 148, 'SERILINGAMPALLY': 147, 'NARAYANGUDA': 146, 'HYDER NAGAR': 145, 'HIMAYATNAGAR': 144, 'BAGH AMBERPET': 143, 'KAVADIGUDA': 142, 'SHAIKPET': 141, 'KONDAPUR,': 140, 'KARKHANA': 139, 'TOLI CHOWKI': 138, 'MADEENAGUDA': 137, 'SAINIKPURI': 136, 'BANDLAGUDA': 135, 'HAFEEZPET': 134, 'KHAIRTABAD': 133, 'MANIKONDA JAGIR': 132, 'CHIKKADPALLY': 131, 'KOMPALLY': 130, 'BEGUMPET': 129, 'HI-TECH CITY': 128, 'SANJEEVA REDDY NAGAR': 127, 'MEHDIPATNAM': 126, 'MIYAPUR': 125, 'BOWENPALLY': 124, 'PRAGATI NAGAR': 123, 'BOWRAMPET': 122, 'POCHARAM': 121, 'NALLAKUNTA': 120, 'KUKATPALLY': 119, 'Other': 118, 'SERILINGAMPALLE': 117, 'QUTUB SHAHI TOMBS': 116, 'SERLINGAMPALLI': 115, 'MALAKPET': 114, 'TARNAKA': 113, 'NIZAMPET': 112, 'CHANDA NAGAR': 111, 'HYDERSHAKOTE': 110, 'NEW NALLAKUNTA': 109, 'SECUNDERABAD': 108, 'YELLA REDDY GUDA': 107, 'ATTAPUR': 106, 'BALKAMPET': 105, 'LINGAMPALLY': 104, 'KUKATPALLY,': 103, 'PRAGATHI NAGAR': 102, 'SHAMSHABAD': 101, 'SUN CITY': 100, 'ANNOJIGUDA': 99, 'MOOSAPET': 98, 'ZAMISTANPUR': 97, 'OLD MALAKPET': 96, 'BANDLAGUDA JAGIR': 95, 'KACHIGUDA': 94, 'NACHARAM': 93, 'PADMARAO NAGAR': 92, 'BACHUPALLY': 91, 'BHOIGUDA': 90, 'AMBERPET': 89, 'METTUGUDA': 88, 'OSMAN NAGAR': 87, 'MANSOORABAD': 86, 'MALLAPUR': 85, 'BORABANDA': 84, 'RAIDURG KHALSA': 83, 'ADIKMET': 82, 'KARMANGHAT': 81, 'BANDAM KOMMU': 80, 'BOLARUM': 79, 'SHIVAJI NAGAR': 78, 'SAIDABAD': 77, 'CHANDANAGAR': 76, 'JEEDIMETLA': 75, 'IBRAHIM BAGH': 74, 'MUSHEERABAD': 73, 'TRIMULGHERRY': 72, 'DILSUKHNAGAR': 71, 'A. S. RAO NAGAR': 70, 'OLD BOWENPALLY': 69, 'NAGOLE': 68, 'A S RAO NAGAR': 67, 'GUDIMALKAPUR': 66, 'SANATH NAGAR': 65, 'GAJULARAMARAM': 64, 'KHAIRATABAD': 63, 'MALLAMPET': 62, 'BHARAT HEAVY ELECTRICALS LIMITED': 61, 'YOUSUFGUDA': 60, 'KOTHAPET': 59, 'ERRAGADDA': 58, 'JILLELAGUDA': 57, 'MOTI NAGAR': 56, 'KAPRA': 55, 'SAROORNAGAR': 54, 'UPPAL': 53, 'AMEENPUR': 52, 'MAHADEVPUR COLONY': 51, 'LB NAGAR': 50, 'ALWAL': 49, 'KRISHNA REDDY PET': 48, 'MALKAJGIRI': 47, 'MEDIPALLY': 46, 'BAHADURGUDA': 45, 'BALANAGAR': 44, 'VANASTHALIPURAM': 43, 'BEERAMGUDA': 42, 'PATANCHERU': 41, 'HASTINAPURAM': 40, 'KISMATPUR': 39, 'BALAJI NAGAR': 38, 'OLD ALWAL': 37, 'JAWAHAR NAGAR': 36, 'GANDAMGUDA': 35, 'LANGAR HOUZ': 34, 'RAMACHANDRA PURAM': 33, 'RAMACHANDRAPURAM': 32, 'RAMANTHAPUR': 31, 'CHAMPAPET': 30, 'RAM NAGAR': 29, 'SAFILGUDA': 28, 'PEERZADIGUDA': 27, 'MOULA ALI': 26, 'KAMALAPRASAD NAGAR': 25, 'KHARMANGHAT': 24, 'HAYATHNAGAR': 23, 'QUTHBULLAPUR': 22, 'DAMMAIGUDA': 21, 'L. B. NAGAR': 20, 'KISTAREDDYPET': 19, 'BODUPPAL': 18, 'RAMPALLY': 17, 'BALAPUR': 16, 'KUSHAIGUDA': 15, 'RODAMESTRI NAGAR': 14, 'B N REDDY NAGAR': 13, 'JAGATHGIRI GUTTA': 12, 'GURRAM GUDA': 11, 'RAMACHANDRAPURAM,': 10, 'NEREDMET': 9, 'MEERPET': 8, 'BADANGPET': 7, 'JILLALGUDA': 6, 'SURARAM': 5, 'ALMASGUDA': 4, 'PEDDA AMBERPET': 3, 'NAGARAM': 2, 'BOLLARAM': 1}


###########################

parking=parking_dict.get(parking_col)
balcony=balconies_dict.get(balconies_col)
furnishing=furnsihing_dict.get(furnsihing_col)
bhk=bhk_dict.get(bhk_col)
bathroom=bath_dict.get(bath_col)
swimming=yes_no_dict.get(swimming_col)
lift=yes_no_dict.get(lift_col)
gym=yes_no_dict.get(gym_col)
maintanance=yes_no_dict.get(isMaintenance_col)
totalfloors=totalfloors_dict.get(totalFloor_col)
floor=floor_dict.get(floor_col)
maintananceAmt=maintenance_dict.get(maintenance_col)
locality=locality_dict.get(locality_col)


#############################

def testing_xgb(data):
    data_list = list((np.array(data)).reshape(-1))

    # load bst model
    bst_model = xgb.Booster({'bthread': 2})
    bst_model.load_model('XGB.model')


    df = pd.DataFrame()
    col_names = ['f%d' % i for i in range(13)]
    df = df.append(pd.Series(data=data_list, index=col_names), ignore_index=True)

    result1 = bst_model.predict(xgb.DMatrix(df))
    lambda_ = 0.02336110709655923
    res = scipy.special.inv_boxcox(result1[0], lambda_)
    return np.around(res, decimals=2)

#################################
    
acc = testing_xgb([parking, balcony, furnishing, bhk, bathroom, swimming, lift, gym, maintanance, totalfloors, floor, maintananceAmt, locality]) 
print(acc)
if st.button('predict'):
        st.success("The output is {}".format(acc))