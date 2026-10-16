# IRPT_DASHBD: CVO adjudication, round 130 (workstream B-IN, ~I2): the wrapper's partition key is the day

<sweep_watermark>2026-10-16T00:46Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T00:46Z, on msg 8810 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND130_BIN_DRAIN_END_20261016.md` @ed9233af0a, blob 3ab43b984a). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One task order, TO-DB-i-17 (LOCAL, <direct_act>true, worker ~317, merged @cfa6dcab48). No judgment criterion. Re-run on the landed tree (HEAD 8e55b664bb): DBI130-1-AC1..AC3, 3 of 3 PASS (rc 0); adapter and wrapper tests 64 passed; proof VALID. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S54",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T00:46:00Z",
  "one_line": "Round 130 B-IN (~I2): the wrapper refuses a row whose day is not its partition's date, and accepts a pull_date later than the partition. THE v115 CASE NOW PASSES: DBI130-1-AC1, the backfill-shaped feed that refused 48 rows at HEAD feb0a37a46 in v115, PASSES at HEAD with nothing refused. THE FEED'S OWN WRITER, generated here: this seat ran the feed's own run() (data/inf/manual_api/pull_inflection_scope_account_returns.py) over its own offline harness (test_scope_feed_day_complete.py: fake S3, fake transport, standard replies) with from_date 2026-10-12. That gave exit 0, 2 households called, and 3 silver partitions of 5 rows each (date=2026-10-12, -13, -14), every row stamped pull_date 2026-10-14 with its own day. The wrapper at HEAD accepted them: trading_days_unaccounted 0, 15 rows written. WHAT THE 15 ROWS COVER: 3 trading days (2026-10-12, 10-13, 10-14) x 5 synthetic accounts (7001-7005, households 5001 and 5002). Only 2026-10-14 carries series points in the harness, so 13 rows are ABSENT and only 10-14 has PRESENT rows. This seat reads 2 PRESENT (7001, 7004), with all five accounts in the dimension; the packet reads 1 PRESENT and 14 ABSENT, a difference in the dimension input, not in the rule. The fixture proves the partition shape and that no day is lost. It exercises no multi-day chain and no real account, and it is small by design; round 131 (TO-DB-i-18) makes the feed-writer fixture a criterion, per the CTO's rule. TESTS 90 -> 64: nothing removed. Round 127's 90 included test_account_return_contract_042.py (27), which still passes (27). The module's own tests went 63 -> 64: one renamed to the new rule (test_partition_whose_rows_name_another_pull_date_is_refused... becomes ..._another_day_is_refused...) and one added (test_a_backfill_shaped_feed_whose_pull_date_is_later_than_its_partition_is_accepted). No criterion's coverage was lost. ROUND 128: its packet now exists (IRPT_DASHBD_ROUND128_BIN_DRAIN_END_20261016.md, committed @4d303631ad). The owed packet is written; it has not reached this seat as a message or been graded. Rows: D2-W317-S1 (a stale docstring) and D2-W317-S2 (a partition's rows may carry differing or null pull_date, untested) are inert, accepted. S2 is the one gap left in the partition rule.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W317-S1",
   "IRPT_DASHBD-D2-W317-S2"
  ],
  "spec_asserts": "Spine L9: grade against the shape the real writer produces (the CTO's msg 8779: fixtures come from the feed's own writer); a test-count change is explained by name.",
  "world_is": "The wrapper accepts the real feed's backfill shape and loses no trading day on the feed-writer fixture. The first real run still waits on ~P2's feed apply (IB-pr-596) and the backfill. FWD-2 for Inflection is not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T00:4xZ (HEAD 8e55b664bb): DBI130-1-AC1..AC3 PASS rc 0; pytest adapter + wrapper 64 passed; contract-042 27 passed; proof-of-spec-check VALID rc 0 on ~317",
    "scratchpad feedwriter_check.py: the feed's run() over its own harness (from_date 2026-10-12): 3 partitions x 5 rows, pull_date 2026-10-14; wrapper: trading_days_unaccounted 0, rows_present 2, rows_absent 13, 15 rows",
    "def-name diff of test_inflection_scope_feed_run.py 0350741d4c..HEAD: 1 renamed, 1 added; adapter test file unchanged in count",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND128_BIN_DRAIN_END_20261016.md @4d303631ad",
    "ADJUDICATION_v115 (the 48-row reproduction)",
    "investigation rows D2-W317-S1, D2-W317-S2",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND130_BIN_DRAIN_END_20261016.md blob 3ab43b984a (msg 8810)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two inert worker rows. The repair is verified on the v115 case and on the feed's own writer output."
 }
]
```
