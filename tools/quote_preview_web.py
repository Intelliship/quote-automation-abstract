# quote_preview_web.py
# Secure internal-use-only demo of the quote preview engine using Streamlit

import streamlit as st
import yaml
from pathlib import Path

RISK_ENGINE_PATH = Path("logic_modules/quote-risk-engine.yaml")
SCORING_MATRIX_PATH = Path("logic_modules/scoring_matrix.yaml")
TEMPLATE_PATH = Path("quote_templates/flatbed_response.md")


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

def main():
    st.set_page_config(page_title="Quote Preview (Demo Mode)", layout="centered")
    st.title("🚚 Quote Preview Engine — Demo")
    st.caption("This is a local-use, internal demo of the abstract quote logic system. Do not deploy externally.")

    uploaded_file = st.file_uploader("Upload RFQ Cluster YAML", type=["yaml", "yml"])
    if uploaded_file:
        cluster_data = yaml.safe_load(uploaded_file)
        risk_engine = load_yaml(RISK_ENGINE_PATH)
        scoring_matrix = load_yaml(SCORING_MATRIX_PATH)

        score, tier = evaluate_risk(cluster_data, risk_engine, scoring_matrix)
        st.markdown(f"### Risk Score: `{score}` — Tier: `{tier}`")

        with open(TEMPLATE_PATH, "r") as file:
            template = file.read()

        st.markdown("### Recommended Template Response")
        st.code(template, language="markdown")

if __name__ == "__main__":
    main()
