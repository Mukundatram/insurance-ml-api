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


