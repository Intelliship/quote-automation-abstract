# Quote Logic OS — SYSTEM OVERVIEW

## 🎯 Core Intent
Turn freight quoting from a reactive task into a programmable, logic-driven system.

## 🔒 System Invariants (FPT)
- All quotes originate from structured YAML clusters
- Risk is quantified, not guessed (escorts, weight, journey legs)
- Templates are selected, not written — based on score logic

## 🔁 If Removed (Inverse FPT)
- Remove risk_engine → quoting becomes tribal
- Remove parser → intake velocity collapses
- Remove templates → system loses speed + standardization

## 🧠 Structural Emergence (SET)
The moment a YAML RFQ is scored and templated automatically, a system emerges. Every quote leaves behind a logic trail — for speed, audit, or scale.

## 💻 Core Components

| Component | Function |
|-----------|----------|
| `raw_parser.py` | Creates structured RFQs from human input
| `risk_engine.yaml` | Flags risk based on business rules
| `scoring_matrix.yaml` | Converts raw risk into tiers
| `quote_preview_engine.py` | Runs the quote logic in test mode
| `quote_templates/` | Stores modular responses by condition

## 🧭 Strategic Role
This system is:
- Platform-agnostic
- CRM-/bot-attachable
- Ready to reduce quoting from 2+ hrs to under 30 mins

It is not a script. It is quote logic OS — designed to scale decisions, not just send emails.
