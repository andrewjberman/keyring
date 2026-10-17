# MDPF_DEMQUE -- W64-S1, S2, S3 disarmed (dell1)

<sweep_watermark>2026-10-11T15:35Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T04:46:34Z, on 2.0.0_SA_COO~Q1 msg 7307 (org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/W64_S1_S2_S3_DISARM_EVIDENCE_20261017.md @3f76dc3cf3). One row. This is not a round sweep, so the watermark does not move.

```json
[
  {
    "id": "MDPF_DEMQUE-D1-C-S29",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T04:46:34Z",
    "one_line": "W64-S1 and W64-S2 (BLOCKING, ARMED) are disarmed on this seat's read of the code at HEAD; W64-S3 is dismissed. S1: the backfill's only entry point refuses every day but 2026-10-10, which is past, and only tests call run(). S2: the error only lowers the untagged room. The S2 repair is carried by the issuer to round 10.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-D1-W64-S1",
      "MDPF_DEMQUE-D1-W64-S2",
      "MDPF_DEMQUE-D1-W64-S3"
    ],
    "spec_asserts": "A BLOCKING ARMED row disarms when its hazard cannot occur; the disarm owner files evidence and this seat writes the clock.",
    "world_is": "READ BY THIS SEAT 2026-10-17 ~04:4xZ at HEAD. S1: data/mdpf/scripts/demque/bbg_backfill.py:24 AUTHORIZED_DAY = 2026-10-10. Lines 220-221: main() calls parser.error unless today == AUTHORIZED_DAY and the day is not a trading day. Line 107 is a run.started.json one-shot marker in run(). A search of data/ for 'bbg_backfill' finds only test_demque_bbg_backfill.py importing it (lines 14, 188), and a search of infra/ finds 0 files. No scheduled or production caller reaches run(), so the full-D-budget room the row describes cannot be drawn. S2: standing_drawer._drawn_history_today adds the production budget ledger's CHANNEL rows on top of the untagged actuals rows. Those ledger rows include the drawer's own draws, so the untagged figure can only read HIGHER drawn and the room LOWER. That is conservative: no extra Bloomberg cell can be drawn because of it. S3: the --quote --actuals CLI path being surface-aware as well is a scope note, INERT. The S2 double count is a real accounting error that under-uses the room; its repair is the issuer's round-10 enrichment, not a hazard.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/bbg_backfill.py lines 24, 90, 107, 213-221 (read at HEAD)",
        "data/mdpf/scripts/demque/standing_drawer.py _drawn_history_today (read at HEAD)",
        "Grep 'bbg_backfill' over data/ (1 test file) and infra/ (0 files)",
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/W64_S1_S2_S3_DISARM_EVIDENCE_20261017.md @3f76dc3cf3",
        "2.0.0_SA_COO~Q1 msg 7307"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S1's path is unreachable outside tests; S2's error is one-way conservative; S3 is a scope note."
  }
]
```

-- 3.0.0_SA_CVO
