import pandas as pd
from sqlalchemy import create_engine

def test_database_load():
    engine = create_engine("sqlite:///02_etl_pipeline/etl_practice.db")
    df = pd.read_sql("SELECT COUNT(*) AS total FROM customers", engine)
    assert df["total"][0] > 0
