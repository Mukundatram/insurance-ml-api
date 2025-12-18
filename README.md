# insurance-ml-api
# Insurance Premium Prediction – ML Inference API

## Overview
Production-ready ML inference service for predicting health insurance premiums.

## Architecture
Client → FastAPI → Preprocessing → ML Model → Prediction

## Tech Stack
FastAPI, XGBoost, Scikit-learn, Docker, Railway

## API Endpoints
GET /health
POST /predict

## Live Demo
https://insurance-ml-api-production.up.railway.app/docs

## Run Locally
docker build -t insurance-ml-api .
docker run -p 8000:8000 insurance-ml-api

## Monitoring & Experiment Tracking
- Implemented MLflow for experiment tracking during model training
- Logged model parameters, evaluation metrics, and artifacts
- Added inference-time logging to track prediction metadata
- Enabled model version traceability for production monitoring

