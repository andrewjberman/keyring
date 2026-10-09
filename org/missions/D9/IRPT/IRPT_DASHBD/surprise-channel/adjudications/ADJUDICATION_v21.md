# IRPT_DASHBD -- round 36 L8 adjudication

<sweep_watermark>2026-10-09T05:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~05:1xZ. L8 input: IRPT_DASHBD round 36 drain-end (2.0.0_SA_COO~D2 msg 2443; issuance @01661cf0da; drains c212a8be27, 075d3f3656, 9e6b077faa). 0 judgment criteria, MAY-CLOSE.
10 rows dismissed below; 7 graduate OPEN in `remediations/REMEDIATION_v17.md`. ARMED: 0 (W47-S1 and W47-S5 disarmed by the rollback, measured live).

**For the round-37 analysis:**
1. **The 49F activity-and-lot re-cut** must fix the lots key (D2-W47-S5: a realized-lot key repeats within a day) and package HEAD bytes
   for the four members at older pins (D2-W47-S4), or state each pin.
2. **Cottonwood's tie-out is 0 of 61 by structure** (W48-S1): no Commonwealth window overlaps Black Diamond's value coverage. An
   independent source for the overlap does not exist yet; the first cell's read has now named that gap.
3. **Inflection is 24 of 562 gross vs 421 net** (W49-S2): the reported source is net; the contract is gross with fees as their own
   figures (Andrew @669ab7d677). The tie-out instrument must compare like with like, compounded, as the 49F fee finding taught.
4. **Two flow classes depart from Inflection's ratified cashflow taxonomy by measurement** (W49-S3): that is a ruling, not a worker call.

```json
[
  {
    "id": "IRPT_DASHBD-C-S32",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T05:15:29Z",
    "one_line": "Round 36 rows dismissed: D2-W47-S1 and D2-W47-S5's issuer disarms D2-W47-S6/S7 (the R35 release is rolled back, live code is the anchor -- measured), D2-W47-S1 (its sizing read gates nothing now), D2-W47-S2 and S3 (deploy-record grant and borrowed terraform binary: tooling notes, no served effect), S31-S33 (the withheld-release gating records; the release was applied then rolled back, and their gates carry to the re-cut through D2-W47-S5), W49-S4 (no Eclipse tax lots landed: FWD-11's ACCEPT already makes the page say so in a sentence), W49-S5 (the Orion source's one Rolling-3-Year window: a source description carried by W49-S2's tie-out).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-D2-W47-S1",
      "IRPT_DASHBD-D2-W47-S2",
      "IRPT_DASHBD-D2-W47-S3",
      "IRPT_DASHBD-D2-W47-S6",
      "IRPT_DASHBD-D2-W47-S7",
      "IRPT_DASHBD-S31",
      "IRPT_DASHBD-S32",
      "IRPT_DASHBD-S33",
      "IRPT_DASHBD-W49-S4",
      "IRPT_DASHBD-W49-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "DB-b-70 SUPERSEDED (applied 0/3/0 at 03:59Z, rolled back on CTO msg 2393 / AMENDMENT 2 @f94c5cb919, ledger closed); DB-b-71 and DB-b-72 complete. this seat's live reads ~05:1xZ: irpt-49f-reporting-gold-lambda CodeSha256 Mex71Y5gk9RY... (the pre-apply anchor), LastModified 2026-10-09T04:31:10Z, Successful, 2048 MB; irpt-49f-reporting-gold-policy PutObject only on opal-data-49financial/irpt/49financial/gold/account_return_daily/*; round-close-check --round 36 MAY-CLOSE (3 orders, 0 judgment).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows IRPT_DASHBD-D2-W47-S1, IRPT_DASHBD-D2-W47-S2, IRPT_DASHBD-D2-W47-S3, IRPT_DASHBD-D2-W47-S6, IRPT_DASHBD-D2-W47-S7, IRPT_DASHBD-S31, IRPT_DASHBD-S32, IRPT_DASHBD-S33, IRPT_DASHBD-W49-S4, IRPT_DASHBD-W49-S5",
        "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~47/R35_APPLY_RECORD.json (rollback block)",
        "IRPT_DASHBD round 36 drain-end (2.0.0_SA_COO~D2 msg 2443; issuance @01661cf0da; drains c212a8be27, 075d3f3656, 9e6b077faa)",
        "this seat's live reads ~05:1xZ: irpt-49f-reporting-gold-lambda CodeSha256 Mex71Y5gk9RY... (the pre-apply anchor), LastModified 2026-10-09T04:31:10Z, Successful, 2048 MB; irpt-49f-reporting-gold-policy PutObject only on opal-data-49financial/irpt/49financial/gold/account_return_daily/*; round-close-check --round 36 MAY-CLOSE (3 orders, 0 judgment)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed by a measured rollback, tooling notes, gating records carried by a graduated row, or covered by FWD-11's own clause."
  }
]
```
