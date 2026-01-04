import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("fraud_model.pkl")

st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")

st.title("💳 Credit Card Fraud Detection System")

# Decision making criteria
with st.expander("ℹ️ How decisions are made"):
    st.write("""
    This system predicts the probability of a transaction being fraudulent.

    - Lower thresholds increase fraud detection (recall)
    - Higher thresholds reduce false alarms (precision)

    In real financial systems, thresholds are adjusted based on risk tolerance.
    """)

st.write("Enter  transaction  details  to  check  if  it  is  fraudulent.".upper())

# Inputs
time = st.number_input("Time", value=0.0)
amount = st.number_input("Amount", value=0.0)

v_features = []
for i in range(1, 29):
    v = st.number_input(f"V{i}", value=0.0)
    v_features.append(v)

# Prepare input
input_data = [time] + v_features + [amount]
columns = ["time"] + [f"v{i}" for i in range(1, 29)] + ["amount"]
input_df = pd.DataFrame([input_data], columns=columns)

# Threshold slider
st.subheader("⚙️ Decision Threshold")

threshold = st.slider(
    "Fraud Probability Threshold",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.01
)

st.caption(
    "Lower threshold → catches more frauds (higher recall) | "
    "Higher threshold → fewer false positives (higher precision)"
)


# Prediction
if st.button("Check Transaction"):
    probability = model.predict_proba(input_df)[0][1]

    if probability >= threshold:
        st.error("🚨 Fraud Detected")
    else:
        st.success("✅ Legit Transaction")

    st.metric("Fraud Probability", f"{probability:.4f}")
    st.metric("Threshold Used", f"{threshold:.2f}")

# ===============================
# Batch CSV Prediction
# ===============================
st.divider()
st.subheader("📂 Batch Fraud Detection (CSV Upload)")

uploaded_file = st.file_uploader(
    "Upload CSV file with columns: time, amount, v1…v28",
    type=["csv"]
)

if uploaded_file is not None:
    batch_df = pd.read_csv(uploaded_file)

    st.write("📄 Preview of uploaded data")
    st.dataframe(batch_df.head())

    expected_cols = ["time"] + [f"v{i}" for i in range(1, 29)] + ["amount"]


    if not all(col in batch_df.columns for col in expected_cols):
        st.error("❌ CSV does not contain required columns.")
    else:
        batch_df = batch_df[expected_cols]

        batch_probs = model.predict_proba(batch_df)[:, 1]
        batch_preds = (batch_probs >= threshold).astype(int)

        batch_df["fraud_probability"] = batch_probs
        batch_df["prediction"] = batch_df["fraud_probability"].apply(
            lambda x: "Fraud" if x >= threshold else "Legit"
        )

        st.subheader("📊 Batch Prediction Summary")
        st.metric("🚨 Fraud Transactions", (batch_df["prediction"] == "Fraud").sum())
        st.metric("✅ Legit Transactions", (batch_df["prediction"] == "Legit").sum())

        st.dataframe(batch_df)

        # Download results
        csv_out = batch_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download Results as CSV",
            csv_out,
            "fraud_detection_results.csv",
            "text/csv"
        )

        #Threshold Impact
        st.subheader("🎯 Threshold Impact")

        fraud_above_threshold = (batch_df["fraud_probability"] >= threshold).sum()
        st.write(
            f"At threshold **{threshold:.2f}**, "
            f"**{fraud_above_threshold}** transactions are flagged as fraud."
        )
