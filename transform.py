import pandas as pd
from sqlalchemy import create_engine
import os

os.makedirs('data/processed', exist_ok=True)
engine = create_engine("sqlite:///data/marketing_demo.db")

def main():
    print('Transforming data...')
    wf = pd.read_sql("SELECT * FROM workflows", engine, parse_dates=["created_at","start_time","end_time"])
    wf['fulfillment_duration_min'] = (wf['end_time'] - wf['start_time']).dt.total_seconds()/60
    wf['sla_met'] = wf['fulfillment_duration_min'] <= wf['sla_target_minutes']

    cm = pd.read_sql("SELECT * FROM campaign_metrics", engine, parse_dates=["date"])
    cm['ctr'] = cm['clicks'] / cm['impressions'].replace(0, pd.NA)
    cm['cpa'] = cm.apply(lambda r: (r['spend']/r['conversions']) if r['conversions']>0 else pd.NA, axis=1)
    cm['roi'] = (cm['revenue'] - cm['spend']) / cm['spend'].replace(0, pd.NA)

    wf.to_parquet("data/processed/workflows.parquet", index=False)
    cm.to_parquet("data/processed/campaign_metrics.parquet", index=False)
    print("Transformed and saved processed datasets at data/processed/")

if __name__ == '__main__':
    main()
