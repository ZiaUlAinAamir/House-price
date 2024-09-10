import streamlit as st
import pickle

# Load the "model" (a very basic example)
# Function to load the model from the pickle file

with open('rg.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit App
st.title("House Price Prediction")

# User input
input_value = st.number_input("Enter number of rooms:", value=0)



# Make prediction
if st.button("Predict"):
    prediction = model.predict([[input_value]])
    st.write(f"Predicted Price of house value is:{prediction}")