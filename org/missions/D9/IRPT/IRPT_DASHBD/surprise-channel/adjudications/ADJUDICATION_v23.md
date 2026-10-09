# IRPT_DASHBD -- round 38 L8 adjudication

<sweep_watermark>2026-10-09T08:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~08:4xZ. L8 input: IRPT_DASHBD round 38 drain-end (2.0.0_SA_COO~D2 msg 2917; issuance @3c01cf1110; drains 8b8b91e20b, 3b94ec13b4, 5759f1fd77, 37d098b5ed). 0 judgment criteria, MAY-CLOSE.
5 rows dismissed below; 5 remediation rows closed in place (v17: D2-W47-S4, D2-W47-S5; v18: D2-W51-S1, D2-W53-S1, D2-W53-S2). No new row
graduates. ARMED: 0.

**For the analysis:** the 49 Financial activity-and-lot release is live, measured; the 11:41Z fire is its organic
acceptance. Inflection ties 418 of 562 gross and 421 net on the taxonomy keys; W49-S3 (the taxonomy ruling) and W54-S1 stay open.

```json
[
  {
    "id": "IRPT_DASHBD-C-S34",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T08:40:43Z",
    "one_line": "Round 38 rows dismissed: D2-W55-S1 (the 07:50Z ad-hoc fire wrote nothing because 10-08 is SOURCE_LAG; the 11:41Z scheduled fire is the organic acceptance), D2-W55-S2 (the rewritten 10-07 manifest differs only in its calendar_source label; returns data byte-equal), W57-S1 (a token-floor lowered for one read-only pull), W57-S2 (Orion gross silver resolves by address() to opal-data-assets by prefix; readers must take the builder's address), W56-S1 (the fee-slice and miss-class code stays in ~53's copy). Closed in place, clocks only: D2-W47-S4 and D2-W47-S5 (the lots key and the HEAD pins, shipped in R37: A1-A7 pass), D2-W51-S1 (the root restore, in R37's apply), D2-W53-S1 (Orion gross landed), D2-W53-S2 (the fee slices stated PARTIAL).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-D2-W55-S1",
      "IRPT_DASHBD-D2-W55-S2",
      "IRPT_DASHBD-W57-S1",
      "IRPT_DASHBD-W57-S2",
      "IRPT_DASHBD-W56-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "R37 (activity and lots for 49 Financial) is LIVE: 0/3/0, dry_run 1,632 MB / 335 s (80% of 2,048 MB), returns byte-equal, ledger closed. this seat's live reads ~08:4xZ: irpt-49f-reporting-gold-lambda CodeSha256 ciTGx5UVE3BJ..., LastModified 2026-10-09T07:03:12Z, Successful, 2048 MB / 900 s; irpt-49f-reporting-gold-policy PutObject on exactly the five 49financial gold prefixes (account_return_daily, account_lot_unrealized_daily, account_lot_realized, account_class_daily, account_activity_daily); round-close-check --round 38 MAY-CLOSE (4 orders, 0 judgment); the four drains are ancestors of box/dell2 HEAD.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W55-S1, D2-W55-S2, W57-S1, W57-S2, W56-S1",
        "IRPT_DASHBD round 38 drain-end (2.0.0_SA_COO~D2 msg 2917; issuance @3c01cf1110; drains 8b8b91e20b, 3b94ec13b4, 5759f1fd77, 37d098b5ed)",
        "this seat's live reads ~08:4xZ: irpt-49f-reporting-gold-lambda CodeSha256 ciTGx5UVE3BJ..., LastModified 2026-10-09T07:03:12Z, Successful, 2048 MB / 900 s; irpt-49f-reporting-gold-policy PutObject on exactly the five 49financial gold prefixes (account_return_daily, account_lot_unrealized_daily, account_lot_realized, account_class_daily, account_activity_daily); round-close-check --round 38 MAY-CLOSE (4 orders, 0 judgment); the four drains are ancestors of box/dell2 HEAD"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Notes on a measured, live release; nothing changes a served value."
  }
]
```
