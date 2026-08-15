import pandas as pd
from sqlalchemy import create_engine
import os

os.makedirs('data', exist_ok=True)
engine = create_engine("sqlite:///data/marketing_demo.db")  # fast for demos

def main():
    print('Loading CSVs into SQLite...')
    pd.read_csv("data/campaigns.csv").to_sql("campaigns", engine, if_exists="replace", index=False)
    pd.read_csv("data/campaign_metrics.csv").to_sql("campaign_metrics", engine, if_exists="replace", index=False)
    pd.read_csv("data/workflows.csv", parse_dates=["created_at","start_time","end_time"]).to_sql("workflows", engine, if_exists="replace", index=False)
    pd.read_csv("data/incidents.csv", parse_dates=["reported_at","resolved_at"]).to_sql("incidents", engine, if_exists="replace", index=False)
    print("Loaded CSVs into SQLite at data/marketing_demo.db")

if __name__ == '__main__':
    main()
