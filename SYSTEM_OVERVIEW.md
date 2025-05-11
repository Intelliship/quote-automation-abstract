# Intelliship Quote Automation System (Repo Index)

Welcome to the full-stack quoting automation ecosystem designed by Intelliship.
This modular, CLI-driven system simulates how a freight organization can reduce
quote turnaround time from **2+ hours** to **under 10 minutes** for live RFQs,
and under 30 minutes for raw intake-to-decision scenarios.

Each repo is composable, documented, and versioned for enterprise evolution.

---

## 🧱 Repo Index and Descriptions

| Repo Name | Description |
|-----------|-------------|
| [`quote-automation-abstract`](https://github.com/Intelliship/quote-automation-abstract) | High-level orchestration of the quoting system using YAML and scripts |
| [`bash-batch-intake`](https://github.com/Intelliship/bash-batch-intake) | Automates batch intake of files and generates structured intake logs |
| [`rfq-normalizer`](https://github.com/Intelliship/rfq-normalizer) | Converts raw customer files (.msg, .pdf, .xlsx) into clean YAML RFQs |
| [`quote-risk-engine`](https://github.com/Intelliship/quote-risk-engine) | Applies scoring rules to determine quote risk based on urgency, value, flags |
| [`quote-decision-logic`](https://github.com/Intelliship/quote-decision-logic) | Decides to quote or not based on rules; assigns response templates |
| [`rfq-template-library`](https://github.com/Intelliship/rfq-template-library) | Houses Markdown templates with dynamic placeholders for quote replies |
| [`quote-preview-engine`](https://github.com/Intelliship/quote-preview-engine) | One-command quote preview engine that simulates entire quote generation |
| [`quote-feedback-loop`](https://github.com/Intelliship/quote-feedback-loop) | Tracks quote outcomes, captures feedback, and classifies RFQ intent |

---

## 📊 Architecture Highlights

- **Input Sources**: Email RFQs, file drops, SharePoint batch folders
- **Processing Stack**: YAML + Bash + Python (fully modular CLI)
- **Output Formats**: Human-readable Markdown, YAML logs, preview-ready quotes
- **System Intelligence**:
  - Risk scoring based on declared value, urgency, flags
  - Quote decision logic (quote / no-quote + template selection)
  - Intent classification (live vs. budgetary)
  - Feedback logging for win/loss/ghosted

---

## 🔄 Evolution Plan

This system supports:
- AI-driven classification (future LLM plug-in layer)
- Integration with Salesforce or TMS
- JSON or API translation layer for containerized scaling
- KPI dashboards powered by `quote-feedback-loop`

---

## 📦 Usage

Each repo can be cloned and executed independently, or integrated via the `quote-preview-engine` CLI for full-stack simulation.

---

Built by **Intelliship LLC**  
Designed for modern freight quoting at enterprise scale.
