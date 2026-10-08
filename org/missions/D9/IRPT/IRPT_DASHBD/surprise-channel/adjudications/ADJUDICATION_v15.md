# IRPT_DASHBD -- round 29 L8/L9 adjudication

<sweep_watermark>2026-10-08T21:02Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-08 ~21:0xZ. L8 input: `2.0.0_SA_COO~D2` drive log @047176ff76
(msg 1614 to the CTO; forwarded as msg 1615). 3 of 3 orders complete (DB-b-50, -51, -52), 0 judgment criteria, MAY-CLOSE. 3 rows
dismissed below; W30-S1 and W31-S2 graduate OPEN in `remediations/REMEDIATION_v13.md`; S34 closed in place. ARMED: 0.

**For the analysis: a lead on the 1,528 real misses (W30-S1, unmeasured).** Opal sits above BD on 94.7% of the right halves (median
+0.567 pp, p10 +0.374, p90 +0.764), no Opal component correlates with the gap, and Opal's `fee_amount` is 0 on every window-day for all
1,528 accounts. A tight, one-signed, positive gap across nearly every account, with no fee in Opal's daily, is what an advisory fee that
BD deducts and Opal does not would produce. The test that decides it: compare each half's gap to BD's own gross-minus-net on the same
half. A tie means the gap is fees, and the fix is Opal's fee feed, not the return math.

```json
[
  {
    "id": "IRPT_DASHBD-C-S26",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T21:02:57Z",
    "one_line": "W29-S1 (S34's 440 classed: 437 are the round-18 fee add-back's non-additivity, 3 near-zero openings), W30-S2 (round 18's read_gold has a function-local column list, so right_gap_e2 re-reads with four more columns) and W31-S1 (the unbatched batch-0 control ended at ~900 s / 2,733 MB with no record) are dismissed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-W29-S1",
      "IRPT_DASHBD-W30-S2",
      "IRPT_DASHBD-W31-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W29-S1 is the classing S34 asked for, so S34 is closed in place (REMEDIATED, clocks only, REMEDIATION_v12): BD's NET halves chain within 0.35 pp on 437 of 440, and the gross gap is Opal's tie-out method, not BD. W30-S2 is a reader workaround with no served effect. W31-S1 is the unbatched mode the round-29 default (batch 2,000) no longer runs; what ended it is unknown but nothing served uses it. Drains 8de470994a, 1ee0fd9e99, 50a0ebae91 are ancestors of box/dell2 HEAD; round-close MAY-CLOSE (this seat's reads).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows IRPT_DASHBD-W29-S1, W30-S2, W31-S1",
        "org/tier1_exec/2.0.0_SA_COO~D2/drive_log_20261008T20Z_desktop-n8rjv0a.md @047176ff76",
        "git merge-base and round-close-check --round 29 (this compile)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The answer to S34, a reader workaround, and a superseded control run; none is a live defect."
  }
]
```
