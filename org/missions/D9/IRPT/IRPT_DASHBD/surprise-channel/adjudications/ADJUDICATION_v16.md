# IRPT_DASHBD -- rounds 30-31 L8/L9 adjudication

<sweep_watermark>2026-10-09T00:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~00:4xZ. L8 inputs: `org/tier1_exec/2.0.0_SA_COO~D2/drive_log_20261009T00Z_desktop-n8rjv0a.md @37a1f0d629` and `org/tier1_exec/2.0.0_SA_COO~D2/drive_log_20261009T00Z_round31_desktop-n8rjv0a.md @4aaa1f8383` (msg 2005;
the CTO routed drain-ends to this seat from round 31, msg 1980). Round 30: DB-b-53 (compounded re-grade), DB-b-55 (batch p95), DB-b-54
superseded; round 31: DB-b-57, -58, -59. All complete, 0 judgment criteria, both rounds MAY-CLOSE. 6 rows dismissed below; W35-S1 and
this seat's correction S35 graduate in `remediations/REMEDIATION_v14.md` (S35 as REMEDIATED). ARMED: 0.

**For the analysis.**

1. **The fee add-back is now right twice over.**
   - It is compounded, which settles S35.
   - Its balance base is the daily mean, which settles W35-S1.
   - Within tolerance: 5,416 -> 8,088 of 9,078.
   - The fix exists in two modules that agree, and one should become the reader of record.
2. **What remains of the 990 outside is named, with nothing left unexplained by class:**
   - LARGE_FLOW_DAY 170;
   - NEAR_ZERO_BALANCE 153;
   - FLOW_TIMING_AFTER_FEE_BASE 116;
   - smaller classes.
3. **FLOW_TIMING is a convention question, not a defect.** Flow-start ties 337 of 370. Adopting it is a ruling, not a fix.

```json
[
  {
    "id": "IRPT_DASHBD-C-S27",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T00:45:56Z",
    "one_line": "Rounds 30-31 rows dismissed: W33-S1 (the dell2 reaper killed two timing runs; killed runs are not timings, and MSTR's GC fix 3be885041e declares long jobs), W33-S2 (batch 1,500 failed p95 on spread; the default is 1,000, p95 652.38 s), W34-S1 (the chain test needed the compounded daily drag, superseded by the daily-mean base), W34-S2 (the 181 crossovers, classed by DB-b-57), W36-S1 (the same daily-mean fix as W35-S1, found independently), W37-S1 (two near-zero-divisor segments, a named class).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-W33-S1",
      "IRPT_DASHBD-W33-S2",
      "IRPT_DASHBD-W34-S1",
      "IRPT_DASHBD-W34-S2",
      "IRPT_DASHBD-W36-S1",
      "IRPT_DASHBD-W37-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The tie-out after rounds 30-31: within 0.35 pp 5,416 (round 18, additive add-back) -> 7,459 (DB-b-53, compounded) -> 8,088 of 9,078 (DB-b-57 and DB-b-58 independently, daily-mean fee base; 762 OUT->IN, 133 IN->OUT). FLOW_TIMING (370) ties on 337 at flow-start against 0 at the served end-of-day convention, with nothing adopted. this seat's reads ~00:4xZ: drains 495789d6ec, d6ddc0e2a7, 605c4cd4ac, cc72b3f60d, 51b6e3736d are ancestors of box/dell2 HEAD; round-close-check --round 30 and --round 31 both MAY-CLOSE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows IRPT_DASHBD-W33-S1, W33-S2, W34-S1, W34-S2, W36-S1, W37-S1",
        "org/tier1_exec/2.0.0_SA_COO~D2/drive_log_20261009T00Z_desktop-n8rjv0a.md @37a1f0d629",
        "org/tier1_exec/2.0.0_SA_COO~D2/drive_log_20261009T00Z_round31_desktop-n8rjv0a.md @4aaa1f8383",
        "this seat's reads ~00:4xZ: drains 495789d6ec, d6ddc0e2a7, 605c4cd4ac, cc72b3f60d, 51b6e3736d are ancestors of box/dell2 HEAD; round-close-check --round 30 and --round 31 both MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Named causes, superseded checks or a duplicate finding; none is a live defect."
  }
]
```
