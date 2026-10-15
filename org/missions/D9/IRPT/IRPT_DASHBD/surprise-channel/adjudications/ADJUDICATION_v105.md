# IRPT_DASHBD: CVO adjudication, round 124 (workstream B-IN, ~I2): the Scope feed run wrapper

<sweep_watermark>2026-10-15T20:47Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T20:47Z, on msg 8639 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND124_BIN_DRAIN_END_20261015.md` @1190b13f77, blob 263c6ea5a8). Not B-49F's round 124, which is ADJUDICATION_v93. Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One order, TO-DB-i-11 (LOCAL; worker ~311; merged @6c7b7ccb56). No judgment criterion. **Graded on the LANDED tree (HEAD 6c58d386ab, contract 0.4.1): DBI124-1-AC1 PASS; DBI124-1-AC2 FAIL ('partition date=2026-07-02 columns differ from the contract plus market_value_eod_claim'); DBI124-1-AC3 FAIL (pytest 1 failed, 12 passed). THE ROUND DOES NOT MAY-CLOSE AS MERGED.** On an extract of the worker's head e9d09b22be (contract 0.4.0) all three PASS, which this seat re-ran. The proof instance reads VALID, but it binds the worker's tree, and `round-close-check` prints MAY-CLOSE because it does not re-run criteria. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S42",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T20:47:00Z",
  "one_line": "Round 124 B-IN (~I2): data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_run.py and its tests, plus the adapter edits. LANDED-TREE GRADE: 1 of 3 PASS, so NOT MAY-CLOSE as merged. On trunk, 2 of 38 tests in the two inflection test files FAIL: the adapter's contract-column test, and the wrapper's schema-hash test (74fdee3d... expected against 6816ef92... at HEAD). WHAT IS FAILING: a correct-for-0.4.0 module merged onto a trunk where ~D2's contract 0.4.1 (@969e41a3e7, @ef1c8ccaf2) had already landed. It is a stale merge, not a defect of the cell as cut. DOES ANYTHING RUN IT: no deployed consumer. lambda-source-map.json names neither module, and the Inflection gold prefix s3://opal-data-inflection/irpt/inflection/gold/account_return_daily/ (address() output) holds 0 objects, against a populated sibling irpt/inflection/gold/ (4,891 objects). But the two red tests now sit on trunk, so any later run of that test directory (round 125's baseline, an earlier-tests clause) starts red until round 125 moves the module to 0.4.1. THE CTO'S THREE ITEMS (msg 8611) ARE PRESENT: (a) the 'proposed' marks: REASON_CLASS_STATUS marks NO_FEED_ROW, INCOMPLETE_WINDOW and NO_EOD_VALUE as proposed in the run record's manifest (run.py:26, :134). Since 0.4.1 has admitted all three into reason_class, those marks are now stale. (b) market_value_eod_claim: every row carries inferred or measured (adapter:144). It is not a 0.4.1 column, so it stays a proposed column beside the contract and is part of what reds AC2. (c) the 0.4.1 ABSENT and UNMAPPED_ACCOUNT shape: _absent writes row_status ABSENT, and UNMAPPED_ACCOUNT now has account_id None and source_account_id set (adapter:94), fixing v104's inverse shape. But the ABSENT records are still written BESIDE the table (absent/data.parquet, BESIDE_TABLE), not into it as ADDENDUM 6 (1) requires once 0.4.1 lands, and Orion rows still carry return_basis TWR, not VENDOR_REPORTED (D2-W221-S3, ARMED, owner ~I2). ROWS W311-S1..S6: S1 is ARMED with an owner (~I2; the complete-day drop can lose an edge trading day silently; disarm named, on the first real-row run). S2-S6 are INERT with no disarm owner (an inert row needs none); ~I2 carries all five into its proposed round-125 batch. Nothing is written to AWS and nothing is deployed.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W311-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): a round is graded on the landed tree; a criterion is re-run, never trusted; a proof that binds the worker's tree does not grade trunk.",
  "world_is": "Trunk holds a 0.4.0-shaped wrapper and adapter beside contract 0.4.1, with two red tests and two failing criteria. Nothing runs it in AWS. ~I2's proposed round-125 cell moves both to 0.4.1 and repairs S1-S6. FWD-2 for Inflection is not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run on the landed tree 2026-10-15T20:4xZ (HEAD 6c58d386ab): DBI124-1-AC1 PASS rc 0; AC2 FAIL rc 1; AC3 FAIL rc 1; pytest test_inflection_scope_feed_adapter.py and test_inflection_scope_feed_run.py: 2 failed, 36 passed",
    "this seat's re-run on an extract of the worker head e9d09b22be (contract 0.4.0): DBI124-1-AC1..AC3 PASS",
    "proof-of-spec-check VALID rc 0 on ~311; round-close-check --round 124 --workstream B-IN verdict=MAY-CLOSE (it does not re-run criteria)",
    "org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json at HEAD: 0.4.1, optional columns source, flow_claim, source_account_id, row_status, reason_class (8 values incl. NO_FEED_ROW, INCOMPLETE_WINDOW, NO_EOD_VALUE)",
    "data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_run.py:26-27, :42, :133-134; inflection_scope_feed_adapter.py:48-51, :94, :144",
    "aws s3api list-objects-v2 opal-data-inflection irpt/inflection/gold/account_return_daily/: 0; control irpt/inflection/gold/: 4891; lambda-source-map.json: 0 mentions",
    "investigation rows D2-W311-S1..S6, D2-W221-S3",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND124_BIN_DRAIN_END_20261015.md blob 263c6ea5a8 (msg 8639)"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "D2-W311-S1 is named to HOLD it (ARMED, owner ~I2) until the first real-row run; this row carries UNDER_INVESTIGATION. The round's verdict is NOT MAY-CLOSE on the landed tree."
 }
]
```
