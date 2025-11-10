import streamlit as st
import pandas as pd
import os

st.title("Copilot AI - Prompt Evaluation Dashboard")
st.write("Visualizing experiment metrics from synthetic data.")

file_path = "03_experiments/metrics/prompt_evaluation.csv"

if os.path.exists(file_path):
    data = pd.read_csv(file_path)
    st.dataframe(data)

    st.subheader("Accuracy per Prompt")

    st.subheader("Latency (ms) per Prompt")
    st.line_chart(data.set_index("Prompt")["Latency_ms"])
else:
    st.warning(f"File not found: {file_path}")
    st.info("Please ensure the CSV file exists and rerun the app.")
