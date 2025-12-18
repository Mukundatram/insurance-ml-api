from prediction_helper import predict
from app.mlflow_logger import log_inference

def run_prediction(request_data: dict) -> int:
    prediction = predict(request_data)
    log_inference(request_data, prediction)
    return prediction
