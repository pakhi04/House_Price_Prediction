import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle

with open("C:\\Users\\lenovo\\Code\\model\\house_price_predict.pkl", "rb") as f:
    lr_clf=pickle.load(f)

def main():
    st.title("Real Estate Price Prediction ")
    total_sqft=st.text_input('total_sqft')

    numbers=[str(i) for i in range (0,10,1)]
    bath=st.selectbox('bath',numbers)
    bal=[str(i) for i in range(0,6,1)]
    balcony=st.selectbox('Balcony',bal)
    bhks = [str(i) for i in range(0, 11, 1)]
    BHK = st.selectbox('BHK', bhks)

    location = st.text_input("Location")

    if st.button('Predict'):
        input_data=pd.DataFrame({
                  'total_sqft': [total_sqft],'bath': [bath],
                  'balcony': [balcony],'BHK':[BHK],'Location': [location]})

        p= lr_clf.predict(input_data)
        st.write(f'Predicted house price: {p}')

if __name__ == '__main__':
    main()