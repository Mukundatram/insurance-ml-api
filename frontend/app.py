import streamlit as st
import requests

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
API_URL = "https://insurance-ml-api-production.up.railway.app/predict"

st.set_page_config(
    page_title="Insurance Premium Predictor",
    layout="centered"
)

st.title("🏥 Insurance Premium Predictor")
st.write(
    "This application consumes a **production ML inference API** "
    "to predict health insurance premiums in real time."
)

st.divider()

# --------------------------------------------------
# INPUT FORM
# --------------------------------------------------
with st.form("prediction_form"):
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    dependants = st.number_input("Number of Dependants", min_value=0, max_value=10, value=0)
    income = st.number_input("Income (in Lakhs)", min_value=0.0, max_value=200.0, value=10.0)

    genetical_risk = st.slider("Genetical Risk", min_value=0, max_value=5, value=1)

    insurance_plan = st.selectbox(
        "Insurance Plan",
        ["Bronze", "Silver", "Gold"]
    )

    employment_status = st.selectbox(
        "Employment Status",
        ["Salaried", "Self-Employed", "Freelancer"]
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    marital_status = st.selectbox(
        "Marital Status",
        ["Married", "Unmarried"]
    )

    bmi_category = st.selectbox(
        "BMI Category",
        ["Normal", "Overweight", "Obesity", "Underweight"]
    )

    smoking_status = st.selectbox(
        "Smoking Status",
        ["No Smoking", "Occasional", "Regular"]
    )

    region = st.selectbox(
        "Region",
        ["Northwest", "Northeast", "Southeast", "Southwest"]
    )

    medical_history = st.selectbox(
        "Medical History",
        [
            "No Disease",
            "Diabetes",
            "High blood pressure",
            "Heart disease",
            "Diabetes & High blood pressure",
            "Diabetes & Heart disease",
            "High blood pressure & Heart disease",
            "Thyroid"
        ]
    )

    submitted = st.form_submit_button("Predict Premium")

# --------------------------------------------------
# API CALL
# --------------------------------------------------
if submitted:
    payload = {
        "Age": age,
        "Number_of_Dependants": dependants,
        "Income_in_Lakhs": income,
        "Genetical_Risk": genetical_risk,
        "Insurance_Plan": insurance_plan,
        "Employment_Status": employment_status,
        "Gender": gender,
        "Marital_Status": marital_status,
        "BMI_Category": bmi_category,
        "Smoking_Status": smoking_status,
        "Region": region,
        "Medical_History": medical_history
    }

    with st.spinner("Calling ML inference API..."):
        try:
            response = requests.post(API_URL, json=payload, timeout=10)

            if response.status_code == 200:
                prediction = response.json()["predicted_insurance_cost"]
                st.success(f"💰 Predicted Insurance Premium: ₹ {prediction}")
            else:
                st.error("API returned an error. Please try again.")

        except requests.exceptions.RequestException as e:
            st.error("Unable to connect to the inference API.")
            st.caption(str(e))

st.divider()

st.caption(
    "🔗 Backend: FastAPI + Docker + Railway | "
    "📊 Monitoring: MLflow | "
    "🧠 Model: XGBoost"
)
