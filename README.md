 End-to-End Machine Learning Pipeline with Deployment on AWS



Check out the live application here ->   
http://end-to-endproject-env.eba-mpiwrvch.us-east-1.elasticbeanstalk.com/predict_datapoint



This project demonstrates a full machine learning workflow — from data ingestion and preprocessing to model training and deployment. The final model is deployed using **AWS EC2 with Elastic Beanstalk**, and the deployment pipeline is automated via **CI/CD** tools for seamless updates.

Developed a regression model to predict a student’s Mathematics score based on various socio-educational factors including gender, ethnicity, parental education level, lunch type, test preparation status, and their scores in Reading and Writing. The pipeline includes data preprocessing, feature engineering, model training, evaluation, and deployment.

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Deployment](#deployment)
- [Directory Structure](#directory-structure)
- [Setup Instructions](#setup-instructions)
- [How to Run Locally](#how-to-run-locally)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## 🚀 Project Overview

The goal of this project is to simulate a production-grade machine learning system capable of end-to-end automation. It involves:

- Data ingestion
- Data preprocessing
- Model training & evaluation
- Model serialization
- REST API for inference
- CI/CD-based deployment on AWS using Elastic Beanstalk

The architecture is modular, production-ready, and easy to scale.

---

## ✨ Features

- Clean and modular codebase with OOP principles
- Real-world data ingestion and transformation pipeline
- Model training and serialization using `pickle`
- REST API using Flask to serve predictions
- **CI/CD Pipeline for automated deployment**
- **Hosted on AWS EC2 via Elastic Beanstalk**
- Logging and error handling throughout the pipeline

---

## 🛠️ Tech Stack

**Languages & Libraries:**

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- flask
- Catboost
- XGBoost
- dill

**Frameworks & Tools:**

- Flask (API)
- Pickle (model serialization)
- Git & GitHub (Version Control)
- AWS EC2 + Elastic Beanstalk (Hosting)
- GitHub Actions / CI/CD Tools (Deployment automation)
- Docker (optional)

---

## ☁️ Deployment
**Live Deployment:**

The trained model is deployed using:

- **AWS EC2 instance** with Elastic Beanstalk
- **CI/CD pipeline** (GitHub Actions) for continuous integration and deployment

Every push to the `main` branch triggers a build and deploys the latest version to AWS automatically.

---

## 🗂️ Directory Structure

```bash
mlproject/
│
├── data/                   # Input dataset and processed files
├── artifacts/              # Trained model and preprocessor
├── src/                    # Source code
│   ├── components/         # Core modules (ingestion, transformation, training)
│   ├── pipeline/           # Wrapper pipeline
│   ├── utils/              # Helper functions
│   └── logger.py           # Custom logger
│
├── app.py                  # Flask app for model API
├── application.py          # WSGI entry point for AWS
├── requirements.txt        # Python dependencies
├── .elasticbeanstalk/      # AWS EB config
├── .github/workflows/      # CI/CD GitHub Actions workflows
├── README.md               # Project documentation
└── setup.py                # Local package setup
