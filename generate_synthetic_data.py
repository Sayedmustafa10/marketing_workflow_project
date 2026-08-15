from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
fake = Faker()
np.random.seed(42)

# campaigns
campaigns = []
for i in range(6):
    start = fake.date_between(start_date='-180d', end_date='-30d')
    end = start + timedelta(days=int(np.random.choice([30,60,90])))
    campaigns.append({
        "campaign_id": f"cmp_{i+1}",
        "channel": np.random.choice(["Email","Paid Social","Search","Affiliate"]),
        "start_date": start,
        "end_date": end,
        "budget": round(np.random.uniform(2000,20000),2)
    })
pd.DataFrame(campaigns).to_csv("data/campaigns.csv", index=False)

# campaign_metrics (daily)
rows=[]
for c in campaigns:
    for d in pd.date_range(c['start_date'], c['end_date']):
        impressions = int(abs(np.random.normal(20000,10000)))
        clicks = max(0, int(impressions * np.random.uniform(0.01,0.08)))
        conversions = int(clicks * np.random.uniform(0.01,0.25))
        spend = round(np.random.uniform(0.2,2.0)*clicks,2)
        revenue = round(conversions * np.random.uniform(20,200),2)
        rows.append({
            "campaign_id": c['campaign_id'],
            "date": d.date(),
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions,
            "spend": spend,
            "revenue": revenue
        })
pd.DataFrame(rows).to_csv("data/campaign_metrics.csv", index=False)

# workflows
wf=[]
teams=["Creative","Analytics","Growth","Ops"]
for i in range(150):
    created = fake.date_time_between(start_date='-90d', end_date='now')
    start = created + timedelta(minutes=int(np.random.exponential(60)))
    duration = int(np.random.exponential(240))  # minutes
    end = start + timedelta(minutes=duration)
    sla = int(np.random.choice([60,120,240,480]))
    wf.append({
        "workflow_id": f"wf_{i+1}",
        "request_type": np.random.choice(["Ad Copy","Landing Page","Report","Tagging"]),
        "created_at": created,
        "assigned_team": np.random.choice(teams),
        "start_time": start,
        "end_time": end,
        "sla_target_minutes": sla,
        "status": np.random.choice(["closed","open"])
    })
pd.DataFrame(wf).to_csv("data/workflows.csv", index=False)

# incidents
inc=[]
cats=["Tracking","CreativeBug","BudgetIssue","ApprovalDelay"]
prio=["LOW","MEDIUM","HIGH"]
for i in range(40):
    r_at = fake.date_time_between(start_date='-90d', end_date='now')
    resolved = r_at + timedelta(minutes=int(np.random.exponential(240)))
    inc.append({
        "incident_id": f"inc_{i+1}",
        "workflow_id": np.random.choice([w['workflow_id'] for w in wf]),
        "reported_at": r_at,
        "category": np.random.choice(cats),
        "priority": np.random.choice(prio, p=[0.5,0.35,0.15]),
        "assigned_to": np.random.choice(["alice","bob","carol","dave"]),
        "resolved_at": resolved if np.random.rand()>0.1 else None,
        "resolution": np.random.choice(["fixed","bounced","escalated","N/A"])
    })
pd.DataFrame(inc).to_csv("data/incidents.csv", index=False)
print("Synthetic CSVs saved under data/")
