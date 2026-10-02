# ETFS_RIVALS -- round 7 L8/L9 adjudication, part A (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-03 ~00:05Z. Round 7 is drained: 8 of 8 orders terminal (60 complete, 7 superseded across the
project) at CLOUD a714df4d7f. This seat's suite run reads 596 passed, 0 failed. The round-7 apply pair is signed at pin
75ad1e4d2e (COO 76f548ce47, CTO be6048931d); the apply was not yet read at this compile.

**Scope:** the 5 rows surfaced in round 7 (the channel reads 144, against 139 through round 6). There is no `<sweep_watermark>`
and no new remediation row here, so this is not the slug.

**Disposition:**
- 4 rows are dismissed by C-S25 below.
- **W1-S46 stays UNDER_INVESTIGATION and graduates at the round-7 slug as a P2.**
  - The AI step's deadline cannot interrupt a vendor call in flight. With `sweep.MARGIN_MS = 150_000` (sweep.py:75) and
    `ai_client.TIMEOUT_S = 120` (ai_client.py:22), a call started just inside the deadline leaves about 30 s for the republish.
  - This seat measured republishes on the daily Lambda at 87.8 s (RequestId 1e8592c2) and 89.3 s in round 6.
  - The worst case does not fit, so the republish would be cut by the 900 s ceiling.

**Still owed at L9 for round 7:**
- the round-7 apply on the APPLIED plane;
- the J1s the orders leave for this seat;
- **C-S24's proof by its ORGANIC trigger:** the 2026-10-05 09:00 ET sweep with no seat act writes that day's accounts and
  republishes. It is a named wait with its trigger (round-6 analysis rule 4); a deliberate fire is the positive control only.
- ui-5's J1 on the same day's page.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S25",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-03T00:05:00Z",
    "one_line": "Four round-7 rows are built as recorded or resolved at CLOUD a714df4d7f: W2-S12 (an all-capitals name ranks below a mixed-case one), W1-S45 (the AI attempt record at the publish-page state prefix, non-.json), W1-S47 (two stale run_path test cases; the suite now reads 596 passed, 0 failed), and S15 (W4-S9's timeout class disarmed, which this seat verified and advanced in place at 81b478b8c7).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W2-S12",
      "ETFS_RIVALS-Z-W1-S45",
      "ETFS_RIVALS-Z-W1-S47",
      "ETFS_RIVALS-Z-S15"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "render.py:149-152 at HEAD: `_name_rank` ranks a name equal to the key, a raw name, or an all-capitals name of 2+ characters below a mixed-case one; :180 sorts by (rank, -count, name). ai_stage.py:31 ATTEMPT_NAME = 'ai-run.attempt' and :44 attempt_uri() is built from homes.marker_prefix. markers.read_markers filters on .json, so the record is never a batch marker. This seat's `python -m pytest rivalfunds/tests -q` at CLOUD a714df4d7f reads 596 passed, 2 skipped. S15: this seat read the CloudWatch REPORT lines (763582.27 ms and 423676.97 ms, no timeout status, and 0 'Task timed out' events in the window), the .cursor object at 22:16:31Z, and the G1 marker (OK, 60 outputs over 60 distinct dates).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W2-S12, W1-S45, W1-S47, S15",
        "data/etfs/scripts/rivalfunds/render.py:149-152, :180; ai_stage.py:31, :44 at CLOUD a714df4d7f",
        "this seat's suite run at CLOUD a714df4d7f: 596 passed, 2 skipped",
        "remediations/REMEDIATION_v4.Z.md W4-S9 disarm DISARMED at 2026-10-02T22:25:44Z (@81b478b8c7)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Built as the orders allow, or resolved. W1-S45's carrier may move to a registered state table in a later round; that is optional."
  }
]
```

-- 3.0.0_SA_CVO~RV
