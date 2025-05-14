# quote_preview_engine.py
# MVP quote preview system — built for clarity, reuse, and raw speed.

import yaml
from pathlib import Path

# --- Configuration
TEMPLATE_MAP_PATH = Path("template_map.yaml")
TEMPLATE_DIR = Path("quote_templates")

# --- Simulated incoming RFQ cluster and data
rfq_cluster = "high_value_cluster"

# --- Simulated variable values
variables = {
    "customer_name": "Leslie",
    "order_number": "875420",
    "rate": "11,200.00",
    "cargo_description": "Siemens turbine housing",
    "insurance_clause": "Expanded coverage to $6M",
    "handling_instructions": "Climate-controlled warehouse, 24/7 guard",
}

# --- Payload override for demos, previews, or high-stakes customer sessions
override = {
    "customer_name": "Michael",
    "rate": "9,870.00",
    "order_number": "198422",
    "cargo_description": "Battery Packs // Class 9 Hazmat",
    "insurance_clause": "Up to $250K value with on-site inspection",
    "handling_instructions": "Secure pallet wrap and escort",
}

# --- Apply override on top of base variables
variables.update(override)

# --- Step 1: Load RFQ Cluster-to-Template Mapping
with open(TEMPLATE_MAP_PATH, 'r') as f:
    template_mapping = yaml.safe_load(f)

# --- Step 2: Resolve Template Path
template_file = template_mapping[rfq_cluster]["template"]
template_path = TEMPLATE_DIR / template_file

# --- Step 3: Extract response body block from YAML
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

# --- Step 4: Render template with variables
for key, val in variables.items():
    body = body.replace(f"{{{{ {key} }}}}", val)

# --- Step 5: Output result
print("\n--- Quote Preview ---\n")
print(body)
