# Credit Card Fraud Detection (Research + Deployment)

This repository contains a full credit card fraud detection project:
1. **Exploratory Data Analysis & Model Benchmarking**
2. **Deployed Streamlit Application for Real-Time and Batch Inference**

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


## 📌 Live Demo
*https://credit-card-fraud-detection-app-8uwp4pgd2gz559coaqugdz.streamlit.app/*

---

## 🧠 How It Works
The model outputs a probability score and uses a threshold slider to classify fraud/legit. Lower thresholds increase recall (more frauds caught), higher thresholds increase precision (fewer false alarms).

## 📜 Resume Summary
Deployed an ML application integrating model evaluation and real-world inference with interactive visualization.
