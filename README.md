# CloudKart - Microservice & CI/CD Pipeline

This repository contains a Flask microservice equipped with automated PyTest unit testing, Docker containerization, and a GitHub Actions CI/CD deployment verification pipeline.

## Architecture & Technology
* **Backend API:** Python 3.11 / Flask
* **Testing Framework:** PyTest
* **Containerization:** Docker
* **Automation:** GitHub Actions

## Repository Structure
* `app.py`: Flask API endpoints (`/` and `/health`).
* `test_app.py`: Automated PyTest validation routines.
* `Dockerfile`: Container image build configuration.
* `requirements.txt`: Application dependencies.
* `.github/workflows/devops-pipeline.yml`: CI/CD automated pipeline.

## Local Execution
To run the container locally:
1. Build image: `docker build -t cloudkart-service .`
2. Run container: `docker run -p 5000:5000 cloudkart-service`
