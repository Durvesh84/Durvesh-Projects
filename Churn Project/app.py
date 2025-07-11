import streamlit as st
import pandas as pd
import joblib

# Load model and features
model = joblib.load('churn_model.pkl')
feature_columns = joblib.load('feature_columns.pkl')

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")
st.title("\U0001F4C9 Customer Churn Prediction App")
st.markdown("Fill out the customer details and click Predict to see if the customer is likely to churn.")

# Form block to retain input state
with st.form("churn_form"):
    # Binary fields
    gender = st.selectbox('Gender', ['Male', 'Female'])
    senior = st.selectbox('Senior Citizen', [0,1])
    partner = st.selectbox('Has Partner?', ['Yes', 'No'])
    dependents = st.selectbox('Has Dependents?', ['Yes', 'No'])
    tenure = st.slider('Tenure (months)', 0, 72, 12)
    phone_service = st.selectbox('Phone Service', ['Yes', 'No'])
    paperless_billing = st.selectbox('Paperless Billing?', ['Yes', 'No'])
    monthly = st.number_input('Monthly Charges', min_value=0.0)
    total = st.number_input('Total Charges', min_value=0.0)

    # One-hot encoded categorical fields
    selections = {}
    categories = {
        'MultipleLines': ['No', 'Yes', 'No phone service'],
        'InternetService': ['DSL', 'Fiber optic', 'No'],
        'OnlineSecurity': ['No', 'Yes', 'No internet service'],
        'OnlineBackup': ['No', 'Yes', 'No internet service'],
        'DeviceProtection': ['No', 'Yes', 'No internet service'],
        'TechSupport': ['No', 'Yes', 'No internet service'],
        'StreamingTV': ['No', 'Yes', 'No internet service'],
        'StreamingMovies': ['No', 'Yes', 'No internet service'],
        'Contract': ['Month-to-month', 'One year', 'Two year'],
        'PaymentMethod': ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']
    }

    for field, options in categories.items():
        selections[field] = st.selectbox(field, options)

    # Submit button
    submitted = st.form_submit_button("\U0001F50D Predict Churn")

if submitted:
    # Initialize input data
    user_data = {
        'gender': 1 if gender == 'Male' else 0,
        'SeniorCitizen': senior,
        'Partner': 1 if partner == 'Yes' else 0,
        'Dependents': 1 if dependents == 'Yes' else 0,
        'tenure': tenure,
        'PhoneService': 1 if phone_service == 'Yes' else 0,
        'PaperlessBilling': 1 if paperless_billing == 'Yes' else 0,
        'MonthlyCharges': monthly,
        'TotalCharges': total
    }

    # Add one-hot encoded fields
    for col in feature_columns:
        if col not in user_data:
            user_data[col] = 0  # Initialize all to 0

    for field, val in selections.items():
        colname = f"{field}_{val}"
        if colname in user_data:
            user_data[colname] = 1

    # Create DataFrame and reorder columns
    input_df = pd.DataFrame([user_data])[feature_columns]

    # Debug display
    st.subheader("\U0001F9FE Input Preview:")
    st.dataframe(input_df)

    # Prediction
    prediction = model.predict(input_df)[0]
    result = "\u26A0\uFE0F Churn Likely" if prediction == 1 else "\u2705 Customer Retained"
    st.subheader("\U0001F4CA Prediction Result:")
    st.success(result)
