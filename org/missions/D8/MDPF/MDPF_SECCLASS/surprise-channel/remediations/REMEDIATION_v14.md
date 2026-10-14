# MDPF_SECCLASS -- round 24 remediations (dell1)

<sweep_watermark>2026-10-14T12:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T12:20:00Z. Graduated at ADJUDICATION_v23 D1-C-S22: 3 rows.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-S36",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The e97 bars and advisors clauses are graded against Oct-12 baselines that an earlier AUA restatement made stale.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S36",
      "adjudication row MDPF_SECCLASS-D1-C-S22 (ADJUDICATION_v23)"
    ],
    "remedy": "Round 25 re-bases the bars and advisors clauses as a class (CTO call 1108) and grades them on the re-based values.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v24",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v24"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S37",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "C_06 rewrites mix_daily_summary.json with a different advisors key order on identical content, moving its ETag.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S37",
      "adjudication row MDPF_SECCLASS-D1-C-S22 (ADJUDICATION_v23)"
    ],
    "remedy": "C_06 writes JSON with sorted keys, under its own never-widen pair.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v24",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v24"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S39",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "IRPT_DASHBD DB-b-181 (e340e07f4e) changed the shared BD classifier at HEAD; it is not deployed, and the next code/gold/lib/ deploy carries it into served BD classes.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S39",
      "adjudication row MDPF_SECCLASS-D1-C-S22 (ADJUDICATION_v23)"
    ],
    "remedy": "Any pair that ships code/gold/lib/ names DB-b-181's radius (BD holdings whose canonical row is typed Cash) and both branches, or the deploy pins etf_classifier.py at the served bytes.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v24",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v24"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  }
]
```
