import streamlit as st
import pickle

# Load the model
with open(r"https://drive.google.com/file/d/1UXOsdGuqmr2SsnmZFWN0gmjOYPxPimtK/view?usp=sharing", "rb") as f:

    model = pickle.load(f)


st.title("Salary Prediction App")

years_experience = st.number_input("Enter years of experience:", step=0.1)
if st.button("Predict"):
    salary = model.predict([[years_experience]])[0]
    st.write(f"Predicted Salary: ₹{salary:.2f}")
