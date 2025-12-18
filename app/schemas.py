from pydantic import BaseModel

class InsuranceRequest(BaseModel):
    Age: int
    Number_of_Dependants: int
    Income_in_Lakhs: float
    Genetical_Risk: int
    Insurance_Plan: str
    Employment_Status: str
    Gender: str
    Marital_Status: str
    BMI_Category: str
    Smoking_Status: str
    Region: str
    Medical_History: str
