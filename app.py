# app.py
import streamlit as st
import pandas as pd
import pickle

# Load the model from the pickle file
with open('loan_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create a Streamlit app
st.title("Loan Prediction App")

# Create a form to input customer data
st.header("Enter Customer Data:")
form = st.form("loan_form")
Gender = form.selectbox("Gender", ["Male", "Female"])
Married = form.selectbox("Married", ["Yes", "No"])
Dependents = form.selectbox("Dependents", ["0", "1", "2", "3+"])
Education = form.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = form.selectbox("Self Employed", ["Yes", "No"])
ApplicantIncome = form.number_input("Applicant Income")
CoapplicantIncome = form.number_input("Coapplicant Income")
LoanAmount = form.number_input("Loan Amount")
Loan_Amount_Term = form.number_input("Loan Amount Term")
Credit_History = form.selectbox("Credit History", ["0", "1"])
Property_Area = form.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

# Create a button to submit the form
submit_button = form.form_submit_button("Predict Loan Eligibility")

# Process the form data and make a prediction
if submit_button:
    data = {
        "Gender": [Gender],
        "Married": [Married],
        "Dependents": [Dependents],
        "Education": [Education],
        "Self_Employed": [Self_Employed],
        "ApplicantIncome": [ApplicantIncome],
        "CoapplicantIncome": [CoapplicantIncome],
        "LoanAmount": [LoanAmount],
        "Loan_Amount_Term": [Loan_Amount_Term],
        "Credit_History": [Credit_History],
        "Property_Area": [Property_Area]
    }
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    st.write("Loan Eligibility:", "Yes" if prediction[0] == "Y" else "No")