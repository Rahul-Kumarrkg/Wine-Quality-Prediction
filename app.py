import streamlit as st
import pickle 
import  numpy as np

# Load the model
rf = pickle.load(open("wine_predict.pkl", 'rb'))

st.header("Wine Quality Prediction")
st.subheader("Ajdust The Slider And Predict The Wine Quality")

volatile_acidity = st.slider("Volatile Acidity", 0.00, 2.00)
citric_acid= st.slider("Citric Acid", 0.00, 0.2)
sulphates = st.slider("Sulphates", 0.00, 2.0)
alcohol = st.slider("Alcohol", 0.00, 15.0)


input_data = [volatile_acidity,citric_acid,sulphates,alcohol]

if st.button("Predict"):
    result = rf.predict([input_data])
    if result[0] == 1:
        st.success("Wine quality is good")
    else:
        st.error("Wine quality is bad")