# IRPT_BCKEND -- round 96 remediations (~P)

<sweep_watermark>2026-10-09T05:18Z</sweep_watermark>

Graduated at round 96's L8 (ADJUDICATION_v45.md), round label v97: D2-W198-S2, OPEN.

```json
[
  {
    "id": "IRPT_BCKEND-D2-W198-S2",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Ruling item 3 says test_served_refuses_all asserts FIRM_BINDING, but the string 'ALL' alone is unrestricted in served.py so the refusal is uploads.py INVALID_INPUT.",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-W198-S2",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_96_P_DRAIN_END_20261009.md @6dea768ce8"
    ],
    "remedy": "Either make a lone 'ALL' string fail closed at served.py (one rule: ALL never admits), or show by test on every route behind served.py that a lone 'ALL' profile row is refused downstream; correct ruling item 3's stated refusal code either way.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v97",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v97"
    },
    "closed": false
  }
]
```
