# MLOps Project: Fraud Detection with Feast and Kubeflow Pipelines

This project demonstrates an end-to-end MLOps workflow integrating Feast (feature store) with Kubeflow Pipelines for a credit card fraud detection use case.

## Features
- Synthetic data generation
- Feast for feature registration and materialization (offline + online)
- Kubeflow Pipeline orchestrating: data prep → feature engineering → training → serving
- Local setup friendly (uses file-based offline store, SQLite registry)

## Prerequisites
- Python 3.10+
- Docker
- Kubernetes cluster with Kubeflow Pipelines (e.g. local kind cluster + Kubeflow)

## Quick Start (Local Testing)
1. `pip install -r requirements.txt`
2. Generate data: `python data_generation/generate_synthetic_data.py`
3. Apply Feast repo: `cd feature_engineering/feature_repo && feast apply`
4. Materialize: `cd .. && python feast_feature_engineering.py`
5. Compile pipeline: `python pipeline/fraud_detection_pipeline.py`
6. Upload the generated YAML to Kubeflow Pipelines UI and run.

For full production setup on Kubernetes, build the custom images and adjust paths to MinIO.

Inspired by Feast + Kubeflow blueprints: https://feast.dev/blog/kubeflow-fraud-detection-e2e/
