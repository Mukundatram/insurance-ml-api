# Insurance Premium Prediction – ML Inference API

## Overview
This project is a **production-ready machine learning inference service** that predicts health insurance premiums based on user demographics, lifestyle, and medical history.  
The system is deployed as a REST API using **FastAPI**, containerized with **Docker**, and hosted on **Railway**.

---

## Architecture

**Workflow:**
- Client sends input data as JSON
- FastAPI handles request validation and routing
- Preprocessing ensures training–inference consistency
- Trained ML model generates the premium prediction
- Response is returned in real time

---

## Tech Stack
- **Backend:** FastAPI  
- **ML Model:** XGBoost  
- **ML Libraries:** Scikit-learn  
- **Containerization:** Docker  
- **Deployment:** Railway  
- **Monitoring & Tracking:** MLflow  

Client → FastAPI → Preprocessing → ML Model → Prediction

## API Endpoints

### Health Check
GET /health
### Prediction

# POST /predict

---

## Live Demo
Swagger UI (Public API Documentation):  
🔗 https://insurance-ml-api-production.up.railway.app/docs

---

## Run Locally

```bash
docker build -t insurance-ml-api .
docker run -p 8000:8000 insurance-ml-api
# Then open:
http://localhost:8000/docs

---

Monitoring & Experiment Tracking (MLflow)
What is implemented?

MLflow is used for experiment tracking during model training

Model parameters, evaluation metrics, and artifacts are logged

Inference-time predictions are logged for monitoring

Enables model version traceability and observability

📊 MLflow Inference Monitoring – Explanation

The graphs shown below are generated using MLflow and represent inference-time monitoring of the deployed model.

What is being tracked?

predicted_premium
The insurance premium predicted by the model for each API request.

How is this data generated?

Every time the /predict endpoint is called:

The model generates a prediction

The predicted value is logged to MLflow as a metric

MLflow automatically visualizes these logged values

What does the graph represent?

The Y-axis shows the predicted insurance premium

Each bar/run corresponds to a single inference

Helps observe:

Prediction range

Output consistency

Sudden abnormal predictions (early warning signals)

Why is this important?

Simulates real-world production monitoring

Helps in:

Detecting model drift

Validating model behavior over time

Debugging unexpected predictions

Key Takeaway

MLflow is used for internal monitoring and observability, not as a public dashboard.
This mirrors real production systems where monitoring tools are kept internal.

MLflow Screenshots

![alt text](<Screenshot (221).png>) 
![alt text](<Screenshot (222).png>)