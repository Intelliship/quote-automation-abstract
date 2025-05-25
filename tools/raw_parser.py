# raw_parser.py
# Converts basic structured RFQ metadata (manual entry or JSON input) into abstract YAML quote cluster

import yaml
import os
from datetime import datetime

OUTPUT_DIR = "rfq_clusters"
TEMPLATE = {
    "origin": "",
    "destination": "",
    "equipment": "flatbed",
    "weight_lbs": 0,
    "journey_legs": 1,
    "accessorials": []
}

def parse_input():
    print("\nEnter RFQ metadata below:")
    data = TEMPLATE.copy()
    data["origin"] = input("Origin: ").strip()
    data["destination"] = input("Destination: ").strip()
    data["equipment"] = input("Equipment Type (e.g., flatbed, stepdeck): ").strip() or "flatbed"
    data["weight_lbs"] = int(input("Total Weight (lbs): ").strip())
    data["journey_legs"] = int(input("# of journey legs (1 if direct): ").strip() or 1)
    accs = input("Accessorials (comma-separated, optional): ").strip()
    data["accessorials"] = [a.strip() for a in accs.split(",") if a]
    return data

def save_yaml(data):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"generated_{timestamp}.yaml"
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        yaml.dump(data, f, sort_keys=False)
    print(f"\n✅ Cluster saved to {path}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    parsed = parse_input()
    save_yaml(parsed)

if __name__ == "__main__":
    main()
