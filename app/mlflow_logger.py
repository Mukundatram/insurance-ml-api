import mlflow
from datetime import datetime

mlflow.set_experiment("insurance-inference-monitoring")

def log_inference(input_data: dict, prediction: float):
    with mlflow.start_run(run_name="inference"):
        mlflow.log_param("age", input_data["Age"])
        mlflow.log_param("insurance_plan", input_data["Insurance Plan"])
        mlflow.log_metric("predicted_premium", prediction)
        mlflow.log_param("timestamp", datetime.utcnow().isoformat())
