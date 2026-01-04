This repository contains a deployed machine learning application for detecting fraudulent credit card transactions using a trained Random Forest classifier.
The project demonstrates a complete ML workflow: model training → evaluation → deployment → real-time & batch inference.

🔗 **Live Demo:** https://credit-card-fraud-detection-app-8uwp4pgd2gz559coaqugdz.streamlit.app/

---
### Sample CSV for Testing
A small sample CSV is provided within the 'app' folder (**sample_test.csv**) so users and recruiters can test the application immediately without needing to clean their own data.

* The sample follows the required column structure.

* It is intended for **demonstration purposes only.**

---

## 🔍 How It Works

### 1️⃣ Prediction Logic
The model evaluates each transaction and outputs a specific **fraud probability** between `0` and `1`. A decision threshold is then applied to classify the transaction:

* **Probability $\ge$ Threshold** $\rightarrow$ **Fraud** 🔴
* **Probability < Threshold** $\rightarrow$ **Legit** 🟢

### 2️⃣ Predicted vs. Actual Fraud Counts
You may observe that the model flags more transactions as fraud than the number of confirmed frauds in the original dataset.

* **Original Dataset:** 492 confirmed fraud transactions.
* **Model Prediction:** ~721 transactions flagged as fraud (at threshold `0.5`).

#### 💡 Why is this expected?
This is a deliberate design choice to prioritize **Safety**.
* The model allows for **False Positives** (flagging a legit transaction as suspicious) to minimize **False Negatives** (missing an actual fraud).
* In banking systems, it is operationally safer to flag a suspicious transaction for manual review than to let a fraudulent transaction pass unnoticed.

### 3️⃣ Threshold Selection (Important)
The system allows you to adjust the decision threshold based on your risk tolerance:

| Threshold | Effect | Use Case |
| :--- | :--- | :--- |
| **0.3** | **High Sensitivity** | Higher recall (catches more fraud) but triggers more alerts. |
| **0.5** | **Balanced Approach** | Default setting. Balances precision and recall. |
| **> 0.5** | **High Precision** | Fewer alerts, but higher risk of missing actual fraud. |

> **Note:** In real-world production systems, thresholds are tuned based on operational costs and specific risk policies.

---

## 📂 Data & Input Format

### 4️⃣ Batch CSV Upload Format
To perform batch fraud detection, upload a `.csv` file with the following column structure:

```csv
time, v1, v2, ..., v28, amount
```

#### 📋 Guidelines
* ❌ Do not include the class (label) column.

* ✅ Each row is treated as a new, unseen transaction.

#### 📤 Output
The application will process the file and append the following columns to your data:

* fraud_probability

* prediction (Fraud / Legit)

### ✅ Summary
* **Safety First:** A higher predicted fraud count is normal; the system prioritizes safety over silence.

* **Flexible Control:** Threshold adjustments allow for realistic, business-driven decision-making.

* **Dual Modes:** The app supports both real-time and batch fraud detection.

