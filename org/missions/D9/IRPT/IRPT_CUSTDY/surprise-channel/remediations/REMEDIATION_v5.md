# IRPT_CUSTDY -- round 5 remediations

<sweep_watermark>2026-10-07T13:1xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~13:2xZ. Graduated at this compile (ADJUDICATION_v5.md): 3 rows, all OPEN, round label v6.

```json
[
 {
  "id": "IRPT_CUSTDY-S10",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The CLOUD irpt_custody suite is red again on test_none_source_names_the_seam_line: IRPT_BCKEND IB-pr-348 (11ba48fdc7) made the seam guard case-insensitive, so no refusing spelling remains for the tracer to fabricate. This is the second time the same tracer has gone red on an upstream fix (S7).",
  "evidence": [
   "investigation row IRPT_CUSTDY-S10",
   "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_5_DRAIN_END_20261007.md @2e68ccd2d2",
   "pytest -q data/assets/scripts/gold/irpt_custody/tests: 125 passed, 1 failed (test_none_source_names_the_seam_line), 1 xfailed (this compile's read, dell2 CLOUD, 2026-10-07 ~13:1xZ)"
  ],
  "remedy": "Retire the tracer test; its purpose (naming the seam line that refused) ended when the seam stopped refusing.",
  "owner": "2.0.0_SA_COO~K2",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~K2",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "IRPT_CUSTDY-W13-S2",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A NOT_HELD account sits in its own household document without household_returns or lineage; validate_document and si_anchor_probe.py would reject such a document if they read it.",
  "evidence": [
   "investigation row IRPT_CUSTDY-W13-S2",
   "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_5_DRAIN_END_20261007.md @2e68ccd2d2"
  ],
  "remedy": "validate_document admits a not_covered account (with its reason) without the per-household blocks, or the producer folds not-held accounts into a household that carries them; the template renders the not_covered account (the CTO's review note on 99addd80).",
  "owner": "2.0.0_SA_COO~K2",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~K2",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "IRPT_CUSTDY-W12-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "hop3_real_run.py exceeds its 120 s bound because the SI anchor probe lists S3; it completes under 1,500 s.",
  "evidence": [
   "investigation row IRPT_CUSTDY-W12-S1",
   "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_5_DRAIN_END_20261007.md @2e68ccd2d2"
  ],
  "remedy": "Bound the anchor probe's listing (a manifest read, or a narrower prefix) before the hop runs on a schedule.",
  "owner": "2.0.0_SA_COO~K2",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~K2",
   "round": "v6"
  },
  "closed": false
 }
]
```
