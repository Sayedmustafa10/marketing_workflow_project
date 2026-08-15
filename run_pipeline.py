# Minimal pipeline: generate synthetic data -> load -> transform -> assign open incidents
import os
from subprocess import run
import pandas as pd
from sqlalchemy import create_engine

def run_pipeline():
    # generate synthetic CSVs
    run(['python', 'notebooks/generate_synthetic_data.py'], check=True)
    # load into SQLite
    run(['python', 'src/etl/load_data.py'], check=True)
    # transform
    run(['python', 'src/etl/transform.py'], check=True)

    # assign open incidents
    engine = create_engine("sqlite:///data/marketing_demo.db")
    inc = pd.read_sql("incidents", engine, parse_dates=["reported_at","resolved_at"])
    open_inc = inc[inc['resolved_at'].isna()]
    from src.automation.incident_handler import assign_incident
    for _, row in open_inc.iterrows():
        incident = row.to_dict()
        assign_incident(incident)
    print("Pipeline finished. Check data/incident_assignments.log for assignments.")

if __name__ == '__main__':
    run_pipeline()
