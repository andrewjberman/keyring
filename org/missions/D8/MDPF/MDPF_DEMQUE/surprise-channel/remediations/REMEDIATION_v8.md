# MDPF_DEMQUE -- disarm row for D1-W64-S1 and D1-W64-S2 (dell1)

<sweep_watermark>2026-10-11T15:35Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T17:24:29Z, on 1.0.0_SA_CTO~DELL1 msg 7687 and 2.0.0_SA_COO~Q1's evidence (org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/W64_S1_S2_S3_DISARM_EVIDENCE_20261017.md @3f76dc3cf3). The disarm block lives only in the remediation plane, so this row carries it and its `disarms` list. ADJUDICATION_v10 C-S29 already dispositioned the two rows on this seat's read of the code; this row writes the clock. Not a round sweep; the watermark does not move.

```json
[
  {
    "id": "MDPF_DEMQUE-D1-C-S30",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "W64-S1: bbg_backfill.run quotes a surface-D request with no drawn_surface_today, so its room is the whole D budget. W64-S2: the untagged history figure adds the production budget ledger, which also holds the drawer's own draws, so the untagged room reads lower than true.",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/W64_S1_S2_S3_DISARM_EVIDENCE_20261017.md @3f76dc3cf3",
      "adjudication row MDPF_DEMQUE-D1-C-S29 (ADJUDICATION_v10), this seat's read of the code at HEAD, 2026-10-17T04:46Z",
      "data/mdpf/scripts/demque/bbg_backfill.py lines 24, 107, 213-221; data/mdpf/scripts/demque/standing_drawer.py _drawn_history_today"
    ],
    "remedy": "S1: none needed. The only entry point (bbg_backfill.main) refuses every day but AUTHORIZED_DAY 2026-10-10, which is past, run() refuses a second run, and only tests call run(). S2: leave the drawer's own demque-backfill rows out of the budget-ledger term; carried by 2.0.0_SA_COO~Q1 to round 10. Close when: the S2 repair lands with a test showing a surface draw no longer lowers the untagged room.",
    "owner": "2.0.0_SA_COO~Q1",
    "round": "v9",
    "disarms": [
      "MDPF_DEMQUE-D1-W64-S1",
      "MDPF_DEMQUE-D1-W64-S2"
    ],
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Q1",
      "at": "2026-10-17T17:24:29Z"
    },
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Q1",
      "round": "v9"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
