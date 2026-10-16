# AMGT_RESAPP -- round 104 workstream AIFILL remediations (dell1)

<sweep_watermark>2026-10-14T01:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T01:00:00Z. Graduated at ADJUDICATION_v127: 2 rows, ARMED, owner and disarm owner 2.0.0_SA_COO~R2.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S132",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A filled block states a claim its cited source does not carry. The producer checks that a web block has citations and that its numbers pass the guard, but nothing checks that each claim is located in a cited source: on the graded AMD run, mgmt_bio says Su chairs the SIA board (the cited IR page: vice chair), mgmt_recent names a reporting line its source does not hold, and thesis_pillars prints a non-GAAP gross margin with no qualifier.",
    "evidence": [
      "adjudication row AMGT_RESAPP-D1-C-S132",
      "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104/thread_run_2/AMD_US_Equity.json"
    ],
    "remedy": "Before the 95-name store, each block's claims are located in its cited sources (a support check per sentence, or the block is withheld with a reason), and a non-GAAP figure says so. Close when: this seat's five-name PROD read finds every claim in its cited source.",
    "owner": "2.0.0_SA_COO~R2",
    "round": "v104",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R2",
      "round": "v104"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R2",
      "at": "2026-10-16T14:46:56Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-C-S133",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The model's process narration reaches the stored text: the stored AMD mgmt_team_view opens \"I'll research AMD's management track record from public sources.\" joined to the answer with no space, and the aifill/v1 validator passes it. A block's presence also varies run to run (thesis_pillars filled with 5 citations in the graded run, NONE in the stored one).",
    "evidence": [
      "adjudication row AMGT_RESAPP-D1-C-S133",
      "s3://opal-data-harvest/amgt/harvest/gold/ai_fill/security_key=AMD_US_Equity/ai_fill.json (generated 2026-10-14T00:46:21Z)"
    ],
    "remedy": "The builder keeps only the answer text (no pre-answer narration) and the validator refuses it; the stored AMD document is rebuilt before ar-3 serves it. Close when: a scan of every stored document finds no narration text, and this seat's five-name PROD read finds none.",
    "owner": "2.0.0_SA_COO~R2",
    "round": "v104",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R2",
      "round": "v104"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R2",
      "at": null
    },
    "closed": false
  }
]
```
