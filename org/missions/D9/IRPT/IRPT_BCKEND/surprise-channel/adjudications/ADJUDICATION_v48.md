# IRPT_BCKEND -- ~Y rounds 72-75 L8 adjudication (releases 5, 5b and 6b)

<sweep_watermark>2026-10-09T11:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~11:0xZ. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/ledger/IRPT_BCKEND_ROUNDS72_75_Y_L8_COMPILE.md @29fbd15e37 (2.0.0_SA_COO~Y2 msg 3185)`. 0 judgment criteria. 9 rows
dismissed below; D2-S17 closed in place. This closes the rows held since the backlog compile (ADJUDICATION_v42 named D2-S18 and D2-S19
for this compile). ARMED: 0 in this lane.

**For the analysis:** X-1 (the acting principal is the filer, the owner the named advisor) is
proven live. Release 6b's AC1 waits on IRPT_ANLREQ's TO-APPLY-Y1 read 4. One act owes Andrew's word: the S3 deletes of 6b's read 4-5
prospect objects, once keyed by name.

```json
[
  {
    "id": "IRPT_BCKEND-C-S324",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T11:00:27Z",
    "one_line": "~Y rounds 72-75 (and the release-6 rows) dismissed: D2-S18 (release 5's arity regression -- rolled back the same session, the co-change instrument built in round 73, release 5b live at 5FRkux2o under its pair), D2-W190-S1/S2 (custody ports wrap the admitted interpreter; port 1 takes a request-bound scope -- as built), D2-W190-S3 with its disarm D2-S19 (ARMED: pyarrow absent -- release 6b is live with the AWSSDKPandas layer, measured), D2-S21 (the apply cell-id lint, fixed @7d4318cd3e), D2-S42 (the disposition of D2-S17: X-1 proven on keys v3, cleanup done under Andrew's word), D2-W220-S2 and D2-W223-S4 (dispositions under amendments, tests pass). Closed in place, clocks only: D2-S17 (REMEDIATION_v32).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-S18",
      "IRPT_BCKEND-D2-W190-S1",
      "IRPT_BCKEND-D2-W190-S2",
      "IRPT_BCKEND-D2-W190-S3",
      "IRPT_BCKEND-D2-S19",
      "IRPT_BCKEND-D2-S21",
      "IRPT_BCKEND-D2-S42",
      "IRPT_BCKEND-D2-W220-S2",
      "IRPT_BCKEND-D2-W223-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "round-close-check MAY-CLOSE for rounds 72-75 (~Y, per the packet); this seat's live read ~11:0xZ: irpt-ycharts-generate CodeSha256 tdpterTMfJlW... (release 6b), LastModified 2026-10-09T09:32:22Z, Successful, layers irpt-common:5 and AWSSDKPandas-Python312:16. Open item carried: Andrew's word for the S3 deletes of 6b's read 4-5 prospect objects, not yet keyed by name.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S18, D2-W190-S1, D2-W190-S2, D2-W190-S3, D2-S19, D2-S21, D2-S42, D2-W220-S2, D2-W223-S4",
        "org/missions/D9/IRPT/IRPT_BCKEND/ledger/IRPT_BCKEND_ROUNDS72_75_Y_L8_COMPILE.md @29fbd15e37 (2.0.0_SA_COO~Y2 msg 3185)",
        "this seat's live read ~11:0xZ: irpt-ycharts-generate CodeSha256 tdpterTMfJlW... (release 6b), LastModified 2026-10-09T09:32:22Z, Successful, layers irpt-common:5 and AWSSDKPandas-Python312:16"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Rolled back and superseded by a live signed release, disarmed by a measured layer, fixed, or dispositioned under amendment."
  }
]
```
