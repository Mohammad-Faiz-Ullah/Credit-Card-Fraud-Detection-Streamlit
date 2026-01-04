# 💳 Credit Card Fraud Detection (Research + Deployment)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

This repository contains a full credit card fraud detection project:
1. **Exploratory Data Analysis & Model Benchmarking**
2. **Deployed Streamlit Application for Real-Time and Batch Inference**

## 📌 Live Demo
*https://credit-card-fraud-detection-app-8uwp4pgd2gz559coaqugdz.streamlit.app/*

## 📁 Repository Structure
├── eda/  
│   └── main.ipynb                  # EDA + model comparison  
│   └── creditcard_sample.csv       # sample dataset  
├── app/  
│   ├── app.py                     # Streamlit app  
│   ├── fraud_model.pkl            # saved model  
 |   ├── sample_test.csv            # Structure_of_csv_that_app_accepts(**DOWNLOAD IT & TEST IN APP !!**) 

│   └── requirements.txt  
└── README.md

## 🔍 EDA & Model Comparison
The `eda/` notebook explores the dataset, compares Random Forest and XGBoost models, and evaluates them using ROC-AUC, precision, recall, and F1-score.

## 🚀 Deployed App
The `app/` folder contains a Streamlit app that:
- Accepts transaction input
- Performs fraud prediction
- Supports batch CSV upload
- Offers a threshold slider for probability-based decisions

## 🛠 Dataset & Feature Description

The dataset used in this project is a credit card transaction dataset where sensitive customer information has been anonymized.

- Features **V1–V28** are **PCA-transformed components** derived from the original transaction features.
- **Time** represents the seconds elapsed between each transaction and the first transaction in the dataset.
- **Amount** represents the transaction amount.
- The target variable (`class`) indicates whether a transaction is fraudulent (1) or legitimate (0).

Because the PCA transformation was already applied to the dataset, the deployed model operates directly on these transformed features rather than raw transaction attributes.

---

## 🧠 How It Works
The model outputs a probability score and uses a threshold slider to classify fraud/legit. Lower thresholds increase recall (more frauds caught), higher thresholds increase precision (fewer false alarms).

