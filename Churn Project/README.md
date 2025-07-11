# 📊 Customer Churn Prediction App

This Streamlit web application predicts whether a customer is likely to churn based on various input features. It uses a pre-trained machine learning model and is designed to help businesses proactively retain customers.

---

## 📄 Features

* User-friendly interface built with **Streamlit**
* Predict customer churn using a trained **machine learning model**
* Input form includes all relevant customer and account details
* Displays prediction result: **"Churn Likely"** or **"Customer Retained"**
* Shows a preview of the input data used for prediction

---

## 📁 Files and Structure

```bash
churn-app-project/
├── app.py                   # Main Streamlit app
├── churn_model.pkl          # Trained ML model
├── feature_columns.pkl      # List of feature columns
├── requirements.txt         # Required Python packages
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/churn-app-project.git
cd churn-app-project
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit pandas scikit-learn joblib
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 🔍 Example Inputs for Testing

Try different combinations of values to test the prediction. Example:

* **Tenure:** 60
* **Monthly Charges:** 55
* **Contract:** Two year
* **Payment Method:** Bank transfer (automatic)
* **InternetService:** DSL

---

## 📊 Model Details

The model used (`churn_model.pkl`) was trained using the [Telco Customer Churn dataset](https://www.kaggle.com/blastchar/telco-customer-churn).
It expects the features listed in `feature_columns.pkl`.

---

## 💼 License

This project is licensed under the MIT License.

---

## 🙋️ Acknowledgements

* Dataset: Kaggle - Telco Customer Churn
* Streamlit library
* scikit-learn for modeling

---

## 🚀 Demo (Optional)

You can deploy this app on [Streamlit Cloud](https://streamlit.io/cloud) or any cloud platform that supports Python.
