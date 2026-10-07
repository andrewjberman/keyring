# IRPT_DASHBD -- round 21 (workstream B) remediations

<sweep_watermark>2026-10-07T12:0xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~12:0xZ. L8 input: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND21_B_DRAIN_END_20261007.md @727a467b1c` (msg 444). 1 of 1 order (DB-b-33) terminal, merged and VALID
@75717e8580; 0 judgment criteria; SERVED risk with no S3 write (build and local run only). 2 rows surfaced after ADJUDICATION_v7's
watermark, both graduated OPEN here; no row is dismissed, so no ADJUDICATION file is written for this round. ARMED: 0. This seat re-ran
the folder's suite (42 passed). W18-S2 gates the served release of account_class_daily (FWD-3) on a CTO ruling.

```json
[
 {
  "id": "IRPT_DASHBD-W18-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The classification module @63fa1a2e32 names 197 tickers, all ETFs or funds, so single stocks and money-market funds land in 'unclassified': 45 of the sample's 78 holdings, about 16% of position value on 2026-10-01. account_class_daily follows the rule (nothing is guessed), and a served view would show about a sixth of the book as unclassified.",
  "evidence": [
   "investigation row IRPT_DASHBD-W18-S2",
   "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND21_B_DRAIN_END_20261007.md @727a467b1c",
   "pytest -q data/assets/scripts/gold/irpt_reporting/tests: 42 passed (this compile's read, dell2 CLOUD, 2026-10-07 ~12:0xZ)"
  ],
  "remedy": "A ruling before the release: serve as is, with 'unclassified' shown, or first have MDPF_SECCLASS cover single stocks and money-market funds. The served release of account_class_daily waits on it.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v22",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v22"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-W18-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The producer's trade-leg tokens (tr_cd TR, trade_typcd BUY/SELL) sit in one block in account_class_daily.py because sources.json was outside the grant.",
  "evidence": [
   "investigation row IRPT_DASHBD-W18-S1",
   "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND21_B_DRAIN_END_20261007.md @727a467b1c",
   "pytest -q data/assets/scripts/gold/irpt_reporting/tests: 42 passed (this compile's read, dell2 CLOUD, 2026-10-07 ~12:0xZ)"
  ],
  "remedy": "The release cell moves the tokens into sources.json, the declaration they belong in.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v22",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v22"
  },
  "closed": false
 }
]
```
