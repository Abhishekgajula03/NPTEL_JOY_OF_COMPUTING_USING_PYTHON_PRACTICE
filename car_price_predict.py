import streamlit as st
import numpy as np
import pandas as pd
import datetime
import xgboost as xgb

def main():
    html_temp="""
     <div style = "background-color:lightblue;padding:16px">
     <h2 style="color:yellow;text-align:center">Car Price Prediction
     </div>
    """
    model=xgb.XGBRegressor()
    model.load_model('xgb_model.json')
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.markdown("#### Are you planning to selling your car !?\n #### so lets try  evaluating the price ")
    p1=st.number_input("what is the current ex-showroom price of  car in (lakhs)",2.5,25.0,step=1.0)
    p2=st.number_input("What is the distance by the car in km?",100,5000000,step=100)
    s1=st.selectbox("what fuel type of car?",('petrol','diesel','cng'))
    if s1=="petrol":
        p3=0
    elif s1=="diesel":
        p3=1
    elif s1=="cng":
        p3=2
    s2=st.selectbox("are you a dealer of individual?",('dealer','individual'))
    if s2=="dealer":
        p4=0
    elif s2=="individual":
        p4=1
    s3=st.selectbox("Transmission manual or automatic?",('manual','auto'))
    if s3=="manual":
        p5=0
    elif s3=="auto":
        p5=1
    p6=st.slider("no of owner the car previously had?",0,3)
    date_time=datetime.datetime.now()
    years=st.number_input("in which year car was purchased?",1990,date_time.year)
    p7=date_time.year - years
    
    data_new = pd.DataFrame({
    'Present_Price':p1,
    'Kms_Driven':p2,
    'Fuel_Type':p3,
    'Seller_Type':p4,
    'Transmission':p5,
    'Owner':p6,
    'Age':p7
},index=[0])
    try:
        if st.button('Predict'):
            pred=model.predict(data_new)
            if pred>0:
                
                st.success("you can sell your car for {:.2f} lakhs".format(pred[0]))
            else:
                st.Warning("you can't sell")
    except:
        st.warning("something went wrong")

if __name__=='__main__':
    main()
