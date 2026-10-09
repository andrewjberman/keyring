# NFRA_GATSCP -- round 1 remediations (dell1)

<sweep_watermark>2026-10-09T09:43Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T09:43:00Z. Graduated at ADJUDICATION_v1: 3 rows, all INERT.

```json
[
  {
    "id": "NFRA_GATSCP-D1-S2",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Site Z amended AGENTS.md @a55888e3a2 so a Codex GO admits a mission-tree order with the full suffixed serial; what remains of FWD-7 is the delivery half (C-DELIVER: the issuance opens the crossbox file and the manager's automated path sends it, only once the order is on origin, in UTC) and one exercised Codex receipt.",
    "evidence": [
      "investigation rows NFRA_GATSCP-D1-S1, -D1-S2"
    ],
    "remedy": "Cut the FWD-7 delivery half in round 2. Close when: one crossbox order reaches a Codex seat by the automated path and that seat executes it",
    "owner": "2.0.0_SA_COO~N1",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~N1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~N1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "NFRA_GATSCP-D1-S3",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "box-sync's grade_merge SKIPs a merge whose graded path set is empty, so a CLOUD take usually runs neither the tree check nor the corpus pass, and a standing defect on the box is printed by nobody.",
    "evidence": [
      "investigation row NFRA_GATSCP-D1-S3",
      "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/FWD1_TRACE_round1.md step 4 (graded 0 of 60 -> SKIP, nothing printed)"
    ],
    "remedy": "Rule whether an empty-set sync still prints the box's standing defects (a standing read, not an act grade). Close when: the ruling is recorded and, if yes, a sync with a placed standing error prints it",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "NFRA_GATSCP-D1-S4",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "to-pipeline-gate.py's / surprise-row-gate's L10 limb counts a seat-home POINTER file (the '# pipeline-override: this file is a POINTER' line) as an open task order, so a round close with a live pointer needs an audited override (MDPF_DEMQUE round 4 @0f652707c8).",
    "evidence": [
      "investigation row NFRA_GATSCP-D1-S4",
      "3.0.0_SA_CVO's own hit: MDPF_DEMQUE.R4-ZQ.POINTER.md refused at the round-4 commit"
    ],
    "remedy": "The limb skips files carrying the POINTER line, or pointers become unnecessary (round-2 lane fix). Close when: a round with a live pointer closes with no override",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  }
]
```
