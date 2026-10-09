# IRPT_BCKEND -- rounds 94, 107 and 109-113 remediations (~P)

<sweep_watermark>2026-10-09T14:31Z</sweep_watermark>

Graduated at the L8 in ADJUDICATION_v51.md, round label v114: 3 rows, OPEN.

```json
[
  {
    "id": "IRPT_BCKEND-D2-S24",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "On a BUNDLE-ROUTED path, safe-deploy.sh mints and uploads the bundle and then prints its summary as 'OK: safe-deploy gate PASS -- 0 file(s) deployed. NOTHING WAS DEPLOYED.' -- the count covers only the LOOSE script leg, so the one sentence a reader is most likely to quote asserts the opposite of what the run did to S3.",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-S24",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_109_113_P_DRAIN_END_20261009.md @32526fbde0 (msg 3453)"
    ],
    "remedy": "On a bundle-routed path, safe-deploy.sh's summary counts the bundle it minted and uploaded, instead of printing '0 file(s) deployed. NOTHING WAS DEPLOYED' after an upload.",
    "owner": "0.0.0_AB_MSTR~DELL2 (safe-deploy.sh owner)",
    "round": "v114",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "0.0.0_AB_MSTR~DELL2 (safe-deploy.sh owner)",
      "round": "v114"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-D2-W269-S2",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "e56's CUSIP-key fallback adds one UNCACHED DynamoDB GetItem per symbol miss: 3,907 s vs 443 s on the same real 49F run.",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-W269-S2",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_109_113_P_DRAIN_END_20261009.md @32526fbde0 (msg 3453)"
    ],
    "remedy": "Cache the e56 CUSIP-key fallback's DynamoDB GetItem per symbol (or batch it): the same real 49F run took 3,907 s against 443 s; measure the cached run against the runner's window before the 49F release.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v114",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v114"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-D2-W272-S2",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "IB-pr-399's replay driver derived its pre-binding negative control from `pin^`; at the IB-pr-409 pin that parent is IB-pr-399's own NarrativeEntry, so the control would have measured nothing. The driver is re-pinned to cabad9008c^.",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-W272-S2",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_109_113_P_DRAIN_END_20261009.md @32526fbde0 (msg 3453)"
    ],
    "remedy": "Derive the replay driver's pre-binding negative control from the commit before the binding change, not from pin^ (at IB-pr-409's pin, pin^ is IB-pr-399's own NarrativeEntry), so the control can fail.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v114",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v114"
    },
    "closed": true
  }
]
```
