# IRPT_DASHBD -- round 48 L8 adjudication, with the three judgment points

<sweep_watermark>2026-10-09T14:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~14:4xZ. L8 input: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND48_B_DRAIN_END_20261009.md @63b594d8d0 (msg 3482)`. DB-b-98 complete, MAY-CLOSE.
1 row dismissed below; W73-S1 and W73-S2 graduate OPEN in `remediations/REMEDIATION_v23.md`. ARMED: 0.

**The packet's judgment points:**
1. **The thresholds** (NEAR_ZERO_BASE at 1%% of peak; a dollar tie at max($1, 0.1%%)) are plausible -- a ratio on a vanishing base, and
   the usual rounding tie -- but NOT shown pre-registered: the rule and the results landed in one commit (145eb673c6), and there is no
   sensitivity table. 156 segments rest on the 1%% cut. Owed: the count at 0.5%% and 2%% of peak, so the class is shown not to be the
   threshold's artifact. The reasons are INFERRED from inputs, not confirmed by Black Diamond, and should be shown as inferred (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~73/REASON_SET_RULE24.md`:55
   says so).
2. **197 DEFECT segments** (W73-S1 74, W73-S2 123): FWD-8's ACCEPT ('every day they disagree carries a stated reason') is NOT met while
   they stand. The CTO's next enrichment.
3. **The issuer's face error** (W73-S3): dismissed; the verdict re-derives from the rows.

```json
[
  {
    "id": "IRPT_DASHBD-C-S40",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:40:07Z",
    "one_line": "Round 48 row dismissed: D2-W73-S3 (the issuer's face said V2's segment rows carry no reason; every OUTSIDE row does -- the issuer sampled a WITHIN row; the 510 were re-derived from the rows, verdict unaffected). D2-W73-S1 (74 DEFECT) and D2-W73-S2 (123 DEFECT) graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-D2-W73-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "DB-b-98 (LOCAL) complete; round-close-check --round 48 MAY-CLOSE (this seat's read); 990 OUTSIDE segments: 793 reasoned, 197 DEFECT.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row IRPT_DASHBD-D2-W73-S3",
        "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND48_B_DRAIN_END_20261009.md @63b594d8d0 (msg 3482)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An issuer face error with no effect on the verdict."
  }
]
```
