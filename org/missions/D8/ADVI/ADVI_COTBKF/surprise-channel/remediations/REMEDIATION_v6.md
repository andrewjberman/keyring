# ADVI_COTBKF -- round 10 remediations

<sweep_watermark>2026-10-07T12:3xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~12:3xZ. Graduated at this compile (ADJUDICATION_v8.md): 1 row, OPEN, round label v11.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W26-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "infra/logic/registry/resources.json carries a marketdata Lambda historical-prices-yfinance whose only evidence is a log-group name; the function does not exist live (ResourceNotFound in four regions). The real writer is historical-prices-scheduler, which launches an EC2 running fetch_historical_prices_yfinance.py; the EC2's own environment could override the target bucket, which was not read.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W26-S1",
   "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_10_DRAIN_END_20261007.md @9e7ba4c0fb"
  ],
  "remedy": "The registry row names the scheduler and its EC2 script as the writer (or the dead row is struck); a registry edit is the laptop's under NFRA_CTLPLN v0.12 C-ROLES.",
  "owner": "1.0.0_SA_CTO",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v11"
  },
  "closed": false
 }
]
```
