# ADVI_BILLING -- round 1 remediations

<sweep_watermark>2026-10-09T07:44Z</sweep_watermark>

Graduated at round 1's L9 (ADJUDICATION_v1.md), round label v2: W1-S6, OPEN.

```json
[
  {
    "id": "ADVI_BILLING-W1-S6",
    "project": "ADVI_BILLING",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The order asks that the viewer be scoped to the firm, the advisor's book and pseudonymization as opal-partners-data scopes its relationship routes, but that route's code checks the firm only (is_authorized) and pseudonymize_response returns the body unchanged (needs_pseudonymization is False).",
    "evidence": [
      "investigation row ADVI_BILLING-W1-S6",
      "org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/r1_close/REAL_RUN_FWD1_R1.md @b44766f7ef"
    ],
    "remedy": "Rule the viewer scope: keep firm-level parity with the relationship route (stated on the page), or add a book check from the household's advisor attribution (team_attribution advisor ids) on both routes.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v2"
    },
    "closed": true
  }
]
```
