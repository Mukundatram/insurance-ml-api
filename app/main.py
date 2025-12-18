from fastapi import FastAPI
from app.schemas import InsuranceRequest
from app.inference import run_prediction

app = FastAPI(
    title="Insurance Premium Prediction API",
    version="1.0"
)
@app.get("/")
def root():
    return {
        "message": "Insurance Premium Prediction API is running"
    }
@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict_premium(request: InsuranceRequest):
    input_dict = {
        "Age": request.Age,
        "Number of Dependants": request.Number_of_Dependants,
        "Income in Lakhs": request.Income_in_Lakhs,
        "Genetical Risk": request.Genetical_Risk,
        "Insurance Plan": request.Insurance_Plan,
        "Employment Status": request.Employment_Status,
        "Gender": request.Gender,
        "Marital Status": request.Marital_Status,
        "BMI Category": request.BMI_Category,
        "Smoking Status": request.Smoking_Status,
        "Region": request.Region,
        "Medical History": request.Medical_History
    }

    prediction = run_prediction(input_dict)

    return {
        "predicted_insurance_cost": prediction
    }
