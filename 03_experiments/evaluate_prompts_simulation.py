import pandas as pd, numpy as np

prompts = ["Summarize feedback", "Extract entities", "Detect sentiment"]

metrics = pd.DataFrame({
    "Prompt": prompts,
    "Accuracy": np.random.uniform(0.7, 0.95, len(prompts)),
    "Latency_ms": np.random.uniform(200, 600, len(prompts))
})

metrics.to_csv("03_experiments/metrics/prompt_evaluation.csv", index=False)
print("Simulated prompt evalutation metrics saved.")
