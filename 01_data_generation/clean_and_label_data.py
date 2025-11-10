import pandas as pd

SYNTHETIC_CUSTOMERS = "01_data_generation/sample_datasets/synthetic_customers.csv"
CLEANED_DATA = "01_data_generation/sample_datasets/cleaned_data.csv"

df = pd.read_csv(SYNTHETIC_CUSTOMERS)

df["Category"] = pd.cut(df["Spend"],
    bins=[0,300,700,1000],
    labels=["Low", "Medium", "High"])

df.to_csv(CLEANED_DATA, index=False)
print("Cleaned and Labeled dataset saved.")
