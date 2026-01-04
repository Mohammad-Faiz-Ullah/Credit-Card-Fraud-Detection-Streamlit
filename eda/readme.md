## 📌 Project Overview
This project focuses on building and optimizing machine learning models to detect fraudulent credit card transactions.  
Fraud detection is a critical problem in the financial sector — detecting fraudulent transactions early helps prevent financial losses for customers and institutions.

## 🎯 Goal
To accurately classify transactions as **fraudulent** or **legitimate** using historical transaction data, while handling the **severe class imbalance** in fraud datasets.

## 🛠 Problem Statement
Fraudulent transactions are rare compared to normal ones, making it challenging for standard machine learning algorithms to detect them effectively.  
We address this by:
- Handling **class imbalance** using **SMOTE**
- Training multiple models
- Hyperparameter tuning for better performance
- Comparing results with visual metrics

## Dataset
The dataset used in this project is the **Credit Card Fraud Detection** dataset from [Kaggle](https://www.kaggle.com/datasets/mexwell/credit-card-fraud).  

⚠ **Note:** The file `creditcard_sample.csv` included in this repository is **only a small random sample** of the full dataset.  
It is provided for demonstration purposes so that the notebook can be executed quickly.  
For full-scale training and evaluation, please download the complete dataset from the Kaggle link above.

## 📂 Project Steps
1. **Data Preprocessing**
   - Checked for missing values & data types
   - Scaled numerical features
   - Handled **class imbalance** using **SMOTE**
   
2. **Model Training**
   - Random Forest (Baseline)
   - Random Forest (Tuned)
   - XGBoost (Optimized for speed and accuracy)

3. **Model Evaluation**
   - Metrics: **Precision, Recall, F1-Score, Accuracy, ROC-AUC**
   - Plotted **ROC Curve** and **Precision-Recall Curve**
   - Compared models visually and numerically

4. **Key Insights**
   - Tuning Random Forest improved **recall** (fewer missed frauds) but slightly reduced precision.
   - XGBoost trained significantly faster than RF while maintaining competitive performance.
   - ROC-AUC > 0.98 for tuned RF and XGBoost indicates strong discrimination ability.

## 📊 Results Summary
| Model                | Precision | Recall | F1-Score | ROC-AUC |
|----------------------|-----------|--------|----------|---------|
| RF (Before Tuning)   | 0.84      | 0.83   | 0.83     | 0.913   |
| RF (After Tuning)    | 0.54      | 0.89   | 0.67     | 0.943   |
| XGBoost              | 0.48      | 0.88   | 0.62     | 0.981   |

## 📌 Why This Project Matters
- Addresses **real-world fraud detection** challenges in finance.
- Demonstrates **handling of imbalanced datasets**, a common ML challenge.
- Shows **model comparison, tuning, and evaluation skills**.
- Relevant for **Data Science, Machine Learning, and AI roles**.

## 🖥 Technologies Used
- **Python**
- **Pandas**
- **Scikit-learn**
- **XGBoost**
- **Matplotlib**

## 🚀 Future Improvements
- Try **deep learning models** (LSTMs) for sequential transaction analysis.
- Deploy model as an **API** for real-time fraud detection.
- Add **cost-sensitive learning** to further optimize for fraud costs.

---

