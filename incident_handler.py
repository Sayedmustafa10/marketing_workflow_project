import json
from datetime import datetime
import os

os.makedirs('data', exist_ok=True)
TEAM_MAP = {
    "Tracking": "Analytics",
    "CreativeBug": "Creative",
    "BudgetIssue": "Growth",
    "ApprovalDelay": "Ops"
}

def assign_incident(incident):
    assigned_team = TEAM_MAP.get(incident.get("category"), "Ops")
    if assigned_team == "Analytics":
        assigned_to = "alice"
    elif assigned_team == "Creative":
        assigned_to = "bob"
    elif assigned_team == "Growth":
        assigned_to = "carol"
    else:
        assigned_to = "dave"
    incident['assigned_to'] = assigned_to
    incident['assigned_team'] = assigned_team
    incident['assigned_at'] = datetime.utcnow().isoformat()
    with open("data/incident_assignments.log","a") as f:
        f.write(json.dumps(incident) + "\n")
    return incident

if __name__ == "__main__":
    sample = {"incident_id":"inc_demo", "category":"Tracking", "priority":"HIGH", "reported_at": datetime.utcnow().isoformat()}
    print(assign_incident(sample))
