-- campaigns
CREATE TABLE campaigns (
  campaign_id TEXT PRIMARY KEY,
  channel TEXT,
  start_date DATE,
  end_date DATE,
  budget NUMERIC
);

-- campaign_metrics
CREATE TABLE campaign_metrics (
  id SERIAL PRIMARY KEY,
  campaign_id TEXT REFERENCES campaigns(campaign_id),
  date DATE,
  impressions INT,
  clicks INT,
  conversions INT,
  spend NUMERIC,
  revenue NUMERIC
);

-- workflows
CREATE TABLE workflows (
  workflow_id TEXT PRIMARY KEY,
  request_type TEXT,
  created_at TIMESTAMP,
  assigned_team TEXT,
  start_time TIMESTAMP,
  end_time TIMESTAMP,
  sla_target_minutes INT,
  status TEXT
);

-- incidents
CREATE TABLE incidents (
  incident_id TEXT PRIMARY KEY,
  workflow_id TEXT,
  reported_at TIMESTAMP,
  category TEXT,
  priority TEXT,
  assigned_to TEXT,
  resolved_at TIMESTAMP,
  resolution TEXT
);
