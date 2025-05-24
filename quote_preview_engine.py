# quote_preview_engine.py

import yaml
import os

RISK_ENGINE_PATH = "logic_modules/quote-risk-engine.yaml"
SCORING_MATRIX_PATH = "logic_modules/scoring_matrix.yaml"
TEMPLATE_PATH = "quote_templates/flatbed_response.md"

def load_yaml(path):
    with open(path, "r") as file:
        return yaml.safe_load(file)

def evaluate_risk(cluster_data, risk_engine, scoring_matrix):
    score = 0
    weight = cluster_data.get("weight_lbs", 0)
    legs = cluster_data.get("journey_legs", 1)
    destination = cluster_data.get("destination", "")

    for rule in risk_engine.get("risk_factors", []):
        if rule["name"] == "overweight" and weight > scoring_matrix["permit_threshold_lbs"]:
            score += rule["score"]
        elif rule["name"] == "escort_required" and weight > scoring_matrix["escort_threshold_lbs"]:
            score += rule["score"]
        elif rule["name"] == "remote_destination" and destination in rule.get("condition", ""):
            score += rule["score"]
        elif rule["name"] == "multi-leg" and legs > 1:
            score += rule["score"]

    for key, value in scoring_matrix["scoring_weights"].items():
        lower, _, upper = key.partition("-")
        if int(lower) <= score <= int(upper):
            return score, value

    return score, "Unknown"

def suggest_template():
    with open(TEMPLATE_PATH, "r") as file:
        return file.read()

def main():
    cluster_file = input("Enter path to RFQ cluster file (e.g., rfq_clusters/project_heavyhaul.yaml): ")
    if not os.path.exists(cluster_file):
        print("File not found.")
        return

    cluster_data = load_yaml(cluster_file)
    risk_engine = load_yaml(RISK_ENGINE_PATH)
    scoring_matrix = load_yaml(SCORING_MATRIX_PATH)

    score, level = evaluate_risk(cluster_data, risk_engine, scoring_matrix)

    print(f"\n--- RISK EVALUATION ---\nScore: {score} | Level: {level}")
    print("\n--- RECOMMENDED TEMPLATE ---")
    print(suggest_template())

if __name__ == "__main__":
    main()
