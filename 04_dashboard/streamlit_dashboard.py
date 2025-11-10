import streamlit as st
import pandas as pd

st.title("Copilot AI - Prompt Evaluation Dashboard")
st.write("Visualizing experiment metrics from synthetic data.")

data = pd.read_csv("03_experiments/metrics/prompt_evaluation.csv")
st.dataframe(data)

st.subheader("Accuracy per Prompt")

st.subheader("Latency (ms) per Prompt")
st.line_chart(data.set_index("Prompt")["Latency_ms"])
