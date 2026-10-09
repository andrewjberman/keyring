# IRPT_DASHBD -- round 33 L8/L9 adjudication

<sweep_watermark>2026-10-09T01:46Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~01:5xZ. L8 input: `org/tier1_exec/2.0.0_SA_COO~D2/drive_log_20261009T01Z_round33_desktop-n8rjv0a.md @76f3874a08` (msg 2109). DB-b-63, -64, -65 complete,
0 judgment criteria, MAY-CLOSE. 2 rows dismissed below; W40-S1, W42-S1 and this seat's S36 graduate OPEN in
`remediations/REMEDIATION_v16.md`. W39-S1 (adopt the two reader fixes) is REMEDIATED and closed in place in REMEDIATION_v15. ARMED: 0.

**For the analysis:**
1. **The repair cell for the two broken callers (W40-S1, W42-S1) should also re-run DB-b-65 without the shim** (S36). Round 33's
   near-zero '79 fixed' was computed on `daily_mean_value` substituted under `mean_daily_value`'s name, and W38-S1 measured those as
   different means.
2. **DB-b-64's refusal is the right outcome.** The served reporting-gold runs pandas 2.2.3 but packages no lots producer, so the
   release peak can only be measured with the kit (ETA ~02:1xZ).

```json
[
  {
    "id": "IRPT_DASHBD-C-S29",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T01:46:14Z",
    "one_line": "Round 33 rows dismissed: W40-S2 (FIRST_DAY_FLOW_AT_START's structural threshold, 25% of prior value with the 2% guard; within the CTO's adoption ruling, re-settable by name) and W40-S3 (both fixes applied to all 9,078 segments, the control with them off reproduces 8,315 exactly).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-W40-S2",
      "IRPT_DASHBD-W40-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Within 8,315 -> 8,385 of 9,078 (84 in, 14 out, all FIRST_DAY_START_NOT_BD, named); control 8,315 exactly; writer census 1 of 130. this seat's reads ~01:5xZ: drains 96a0c9991a, 9e9b3c49f2, 58fa2adf16 are ancestors of box/dell2 HEAD; round-close-check --round 33 MAY-CLOSE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows IRPT_DASHBD-W40-S2, W40-S3",
        "org/tier1_exec/2.0.0_SA_COO~D2/drive_log_20261009T01Z_round33_desktop-n8rjv0a.md @76f3874a08",
        "this seat's reads ~01:5xZ: drains 96a0c9991a, 9e9b3c49f2, 58fa2adf16 are ancestors of box/dell2 HEAD; round-close-check --round 33 MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A ruled threshold and a scope note, each with a control that reproduces the prior figure."
  }
]
```
