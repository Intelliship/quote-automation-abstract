# Quote Automation System – Abstract Logic Repository

This repository contains abstracted logic and modular components that power the quote automation system at scale.

## Objective

Reduce quote turnaround time from 2+ hours to under 30 minutes by using structured logic objects, reusable templates, and smart risk scoring.

## Structure

- `rfq_clusters/` – YAML objects per project (e.g., Vestas, Tera9, Siemens)
- `quote_templates/` – Prewritten customer responses based on scenario
- `logic_modules/` – Risk scoring, decision rules, SLA triggers
- `accessorials/` – Master accessorial cost tables (detention, FSC, permits)

## Usage

This repo consumes raw files from `quote-automation-raw` and transforms them into structured, automated logic for internal execution and customer response.
