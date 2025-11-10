import pandas as pd
from sqlalchemy import create_engine
import logging, os

CLEANED_DATA = "01_data_generation/sample_datasets/cleaned_data.csv"

os.makedirs("01_etl_pipeline/logs", exist_ok=True)
logging.basicConfig(filename="01_etl_pipeline/logs/etl.log", level=logging.INFO)

engine = create_engine("sqlite:///02_etl_pipeline/etl_practice.db")

def load_data():
    df = pd.read_csv(CLEANED_DATA)
    df.to_sql("customers", engine, if_exists="replace", index=False)
    logging.info(f"Loaded {len(df)} wors into database")

if __name__ == "__main__":
    load_data()
