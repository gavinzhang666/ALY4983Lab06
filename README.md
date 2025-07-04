# ALY4983 Lab 06 – CI/CD Pipeline for a Simple ML Project

This project demonstrates a basic CI/CD pipeline for a machine learning workflow using GitHub Actions and Docker. It includes training, evaluation, unit testing, performance threshold checks, and a Docker-based deployment step.

## Project Overview

The project includes:

- `train.py`: Trains a logistic regression model on the Iris dataset and saves it to `artifacts/model.pkl`.
- `evaluate.py`: Evaluates the model and writes accuracy to `artifacts/accuracy.txt`.
- `check_performance.py`: Checks if model accuracy meets a defined threshold (default: 0.80); exits with error if not.
- `test_data.py`: Unit tests to verify that training scripts run without error and produce expected output.

## Directory Structure

```
.
├── artifacts/                  # Stores model and accuracy output  
├── src/  
│   ├── train.py  
│   ├── evaluate.py  
│   └── check_performance.py  
├── tests/  
│   └── test_data.py  
├── .github/workflows/  
│   └── ci.yml                  # GitHub Actions workflow  
├── requirements.txt  
├── Dockerfile                  # Docker image for model deployment  
└── README.md
```

## How to Run Locally

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate      # On Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Train and evaluate the model:

   ```bash
   python src/train.py
   python src/evaluate.py
   python src/check_performance.py
   ```

4. Run unit tests:

   ```bash
   pytest tests/
   ```

## CI/CD Workflow

A GitHub Actions workflow (`ci.yml`) is triggered on every push or pull request to the `main` branch. It executes the following stages:

- **Lint**: Run flake8 on `src/` and `tests/` directories.
- **Unit Test**: Validate that scripts run without errors.
- **Model Training**: Train the model and generate `model.pkl`.
- **Model Evaluation**: Write accuracy score to `accuracy.txt`.
- **Threshold Check**: Fail the pipeline if accuracy is below 0.80.
- **Deployment**: If the threshold passes, build a Docker image and push to Docker Hub.

### Docker Deployment (CD)

If the pipeline passes all checks, a Docker image containing the trained model is built and pushed to:

**Docker Hub**:  
https://hub.docker.com/repository/docker/gavinzhang29/aly4983lab06/general

Image is tagged using the commit SHA:  
`gavinzhang29/aly4983lab06:<commit-sha>`

This step ensures the model is ready for staging or production deployment using Docker.

## How I Tested the Pipeline

- I triggered a failure by editing `train.py` to break a function. The pipeline failed as expected.
- I fixed the bug and pushed again. The pipeline passed.
- I raised the threshold in `check_performance.py` to 0.999, forcing a failure when accuracy was below that value.
- I restored the threshold to 0.80, and the pipeline passed.
- The final Docker deployment step successfully built and pushed the image to Docker Hub.

## Author

Yuhui Zhang  
