
# MLOps Kubeflow Assignment

This project implements an end-to-end MLOps pipeline for a simple machine learning task using DVC for data versioning, Kubeflow Pipelines for orchestration, and Jenkins/GitHub Workflows for CI. [file:1][web:27][web:30]

## Project Overview

- Data versioning with DVC for the Boston Housing dataset. [file:1][web:28]
- ML pipeline components built as Kubeflow components (data extraction, preprocessing, training, evaluation). [file:1][web:27]
- Pipeline orchestration and execution on Kubeflow Pipelines running on Minikube. [file:1][web:25]
- Continuous integration using Jenkins or GitHub Actions to compile and validate the pipeline. [file:1][web:23]

## Repository Structure

- `data/` – Raw and processed datasets tracked with DVC. [file:1][web:21]
- `src/` – Python source files (`pipelinecomponents.py`, `modeltraining.py`). [file:1]
- `components/` – Compiled Kubeflow component YAML files. [file:1][web:27]
- `pipeline.py` – Main Kubeflow pipeline definition. [file:1]
- `requirements.txt` – Python dependencies for the project. [file:1]
- `Dockerfile` – Optional Docker image definition for custom components. [file:1]
- `Jenkinsfile` – CI pipeline configuration for Jenkins. [file:1]

## Setup Instructions

1. Create and activate a Python virtual environment, then install dependencies: [file:1][web:30]  


2. Initialize DVC and configure remote storage, then pull the dataset: [file:1][web:21]  
3. Start Minikube and ensure the Kubernetes cluster is running: [file:1][web:2]  
2. Access the Kubeflow Pipelines UI (via port-forwarding or ingress), upload `pipeline.yaml`, create an experiment, and run the pipeline. [file:1][web:20][web:25]
3. Inspect each step (data extraction, preprocessing, training, evaluation) and review the logged metrics (e.g., MSE, R²) in the run details. [file:1][web:27]

## Continuous Integration

- The `Jenkinsfile` defines stages for environment setup, pipeline compilation, and component validation. Configure a Jenkins Pipeline job that pulls from this repository and runs on each commit or pull request. [file:1][web:18][web:26]
- Alternatively, a GitHub Actions workflow can be added to run the same checks using a YAML workflow file in `.github/workflows/`. [file:1][web:24]

## Reproducibility

- All code, configuration, and data pointers are stored in Git, while large data files are tracked with DVC remotes. [file:1][web:30]
- Cloning the repository, creating the environment, running `dvc pull`, and recompiling the pipeline should reproduce the full ML workflow. [file:1][web:21]

EOF
