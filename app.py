import streamlit as st
import pickle
import pandas as pd

model=pickle.load(open('tips_model.pkl','rb'))

st.title("TIP PREDICTION APP")

total_bill=st.number_input("size")
size=st.number_input("size")
sex=st.selectbox("sex",['Male','Female'])
smoker=st.selector("smoker",['yes','no'])
day=st.selectbox("day",['thur','fri','sat','sun'])
time=st.selectbox("time",['lunch','dinner'])
input_data=pd.DataFrame({
    'total_bill': [total_bill],
    'size':[size],
    'smoker':[smoker],
    'day':[day],
    'time':[time]
})


if st.button("predict tip"):
    prediction=model.predict(input_data)
    st.success(f"predicted_tip:{prediction[0]:.2f}")


                        