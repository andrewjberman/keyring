# ETFS_RIVALS -- round 9 remediations (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-05 ~20:40Z. Graduated at round 9's L9 (`adjudications/ADJUDICATION_v9.Z.md`).

Round 9 is drained and applied:
- 7 of 7 orders are complete;
- the ledger is CLOSED 6/6 at 8ba7b13b90;
- D12 Step B is executing under its own ledger.

This slug covers the whole project and carries no sweep watermark. Three items graduate: C-S38, W6-S2 and C-S41. Named first:
**S25 (REMEDIATION_v8) is still unplaced after two analyses** (C-S39). Still OPEN with their proof owed:
- S24: the next production pull after a budgeted day;
- S29: Step B's K1 census;
- C-S36: nm-3 J1 after the first vehicle run with capacity.

Review: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R9_REVIEW_20261005.md`.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S38",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "g5_drift.json attributes its largest class (g3_latest_pull_supersession, 9,467 of 9,477 differing rows) to commit 4fa3e25f5e. Those columns moved because later G3 pulls landed under unchanged code. Under ruling 5, that class reads as old values that were right for the G3 they were built from, not as a code defect.",
    "evidence": [
      "adjudications/ADJUDICATION_v9.Z.md ETFS_RIVALS-Z-C-S38",
      "deliverables/0.9.0_WK_ETFS_RIVALS~6/g5_drift.json"
    ],
    "remedy": "Correct the class: cause {data: 'G3 revisions landed after the live build', commit: null}, and give g3_minor_unit_dividend_currency its own confirmed_by. A per-column reader_visible map would make the flag exact. The history ruling for this class is then a choice of data vintage, not a defect fix.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-W6-S2",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A G5 replay started inside its scope loses each fund's first window, because the pairing needs the prior report date and the replay has not built it (CGIC 2026-01-02).",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W6-S2"
    ],
    "remedy": "Any future G5 replay starts one report date before its scope, or reads the prior date's live G5 for pairing. Proof: a planted mid-scope replay keeps the first window.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-C-S41",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Ruling 6 required each of the 8 stale rows to be cut, closed with a citing row, or to name its blocker. The triage f70677780a changed none of their states: S13 is 'proposed' with no cell, and 4 are re-homed with no citing row.",
    "evidence": [
      "adjudications/ADJUDICATION_v9.Z.md ETFS_RIVALS-Z-C-S41",
      "commit f70677780a"
    ],
    "remedy": "One citing row per stale remediation row: REMEDIATED with evidence, re-homed with the receiving project's row id, or parked with its blocker and un-park condition. S13 gets a cell or a row naming why not.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v9"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~RV
