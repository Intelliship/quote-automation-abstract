# Quote Risk Scoring Logic

This document defines how quotes are scored for risk and priority.

## Scoring Criteria

- Urgency: +5 if pickup is same-day
- Missing data: -10 if dimensions or value not provided
- High value: +10 if declared value > $100,000
- Incomplete files: -15 if attachment is corrupt or unreadable

Max Score: 100  
