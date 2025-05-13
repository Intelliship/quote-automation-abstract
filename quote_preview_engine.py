# quote_preview_engine.py
# MVP quote preview system — built for clarity, reuse, and raw speed.

import yaml
from pathlib import Path

# --- Configuration
TEMPLATE_MAP_PATH = Path("template_map.yaml")
TEMPLATE_DIR = Path("quote_templates")

# --- Simulated incoming RFQ cluster and data
rfq_cluster = "bess_cluster"
variables = {
    "customer_name": "Marcus",
    "order_number": "191835",
    "rate": "5140.80",
    "cargo_description": "BESS container - 20ft",
    "transit_time": "2 days",
    "insurance_clause": "Standard coverage up to $100,000",
    "accessorials": "escort, permits"
}

# --- Step 1: Load RFQ Cluster-to-Template Mapping
with open(TEMPLATE_MAP_PATH, 'r') as f:
    template_mapping = yaml.safe_load(f)

# --- Step 2: Resolve Template Path
template_file = template_mapping[rfq_cluster]['template']
template_path = TEMPLATE_DIR / template_file

# --- Step 3: Extract response_body block from YAML
with open(template_path, 'r') as f:
    lines = f.readlines()

body_lines = []
in_body = False

for line in lines:
    if line.strip() == "response_body: |":
        in_body = True
        continue
    if in_body:
        body_lines.append(line[2:] if line.startswith("  ") else line)

body = "".join(body_lines)

# --- Step 4: Interpolate Variables
for key, val in variables.items():
    body = body.replace(f"{{{{ {key} }}}}", val)

# --- Output
print("\n--- Quote Preview ---\n")
print(body)
