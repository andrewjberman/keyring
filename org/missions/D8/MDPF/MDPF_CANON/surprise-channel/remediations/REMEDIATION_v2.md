# MDPF_CANON -- round 2 remediations (dell1)

<sweep_watermark>2026-10-11T02:30Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T02:25:00Z. Graduated at ADJUDICATION_v2: 3 rows (1 BLOCKING, 2 INERT observations). The round-1 rows in REMEDIATION_v1 stay open with their owners.

```json
[
  {
    "id": "MDPF_CANON-D1-S9",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The first scheduled daily write (2026-10-10 13:30Z) built 12 of 16. Global was refused by the cross-axis coherence gate: 5 models carry model_value None on 2026-10-09 against a count, with the value feed one trading day behind. The 49financial A7 reconciliation ERROR skipped its partition write, and inflection holds two types on CONFLICT lines. Platinum for global and for 49financial's aggregate, aum and category leaves served as of 2026-10-08.",
    "evidence": [
      "investigation row MDPF_CANON-D1-S9",
      "adjudication row MDPF_CANON-D1-C-S19",
      "deliverables/2.0.0_SA_COO~D1/round2/DAILY_READ_20261010T1330Z.md"
    ],
    "remedy": "Rule whether the value-feed lag and the reconciliation/CONFLICT guard are a round-3 cell, then re-read a scheduled fire. Close when: one scheduled fire writes 16 of 16 at address(), r2_daily.py read passes 4 of 4, and CN-a-2 AC3 grades",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-C-S12",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "X2_GLOBAL_BASIS.md asserts a minimum firm count of 2 and no per-account value. The producer's global output carries single-firm by_model entries (12 on 2026-10-08, 6 at 3 or fewer accounts, values equal to the firm's) and two single-firm series (non_model_aua, inflection_non_model_aua).",
    "evidence": [
      "adjudication row MDPF_CANON-D1-C-S12"
    ],
    "remedy": "Rewrite the basis per field family from the producer's output (headline sums 2-3 firms; by_model 1-3 firms; two single-firm series) and say what a small-count single-firm entry reveals, or rule a suppression or threshold in the fold. Close when: the basis's minimum firm count matches the output, read by a seat that did not write it",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-S8",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The stale served key json/portfolios/aum-timeseries.json has dead readers in portal/src/api (portal-proxy.ts:338-345, endpoints/aum.ts:322-328, :447-449) and no live page caller at portal c96efe17.",
    "evidence": [
      "investigation row MDPF_CANON-D1-S8",
      "adjudication row MDPF_CANON-D1-C-S18"
    ],
    "remedy": "Remove the dead readers as a portal-repo act when the served key retires. Close when: portal/src names no reader of the key, at the retirement step",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  }
]
```
