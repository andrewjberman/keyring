# LGIC_CANON -- round 5 remediations (dell1)

<sweep_watermark>2026-10-09T19:37Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T19:37:00Z. Graduated at ADJUDICATION_v3: 3 rows, all INERT.

```json
[
  {
    "id": "LGIC_CANON-D1-W2-S1",
    "project": "LGIC_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A stored-file path's answer now sits in name_rulings.json (the census reads only that file, by name and type); two of those answers also exist in key_rulings.json and can drift apart.",
    "evidence": [
      "investigation row LGIC_CANON-D1-W2-S1",
      "org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~B1/ROUND5_DRAIN_END.md @78667bd516 rows section"
    ],
    "remedy": "Keep one home per answer (or a check that the two agree). Close when: the two files hold no answer twice, or a check fails on a planted disagreement",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "LGIC_CANON-D1-W3-S30",
    "project": "LGIC_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Three places in the checklist (the INPUTS count line, the step-14 trailer, the STOP list) still call the portal paths SOVEREIGN after CN-q-2 made them DERIVED.",
    "evidence": [
      "investigation row LGIC_CANON-D1-W3-S30",
      "org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~B1/ROUND5_DRAIN_END.md @78667bd516 rows section"
    ],
    "remedy": "Edit the three places. Close when: the checklist names the portal paths DERIVED everywhere",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "LGIC_CANON-D1-W1-S33",
    "project": "LGIC_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The committed generated views lag the registry for scopes other than 49financial, and checklist Step 4 and Step 14 wording predates PART A and the 13-file generator.",
    "evidence": [
      "investigation row LGIC_CANON-D1-W1-S33",
      "org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~B1/ROUND5_DRAIN_END.md @78667bd516 rows section"
    ],
    "remedy": "Regenerate the views and update the two steps. Close when: the generator's output equals the committed views for every scope",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  }
]
```
