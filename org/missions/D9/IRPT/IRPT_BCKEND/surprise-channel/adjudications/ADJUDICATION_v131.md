# IRPT_BCKEND: CVO adjudication, round 3 (workstream ~PN, the Scope feed writes complete days only)

<sweep_watermark>2026-10-15T19:51Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T19:51Z, on msg 8586 (shared packet @f7b4555d40). One order, IB-pr-599 (risk LOCAL), complete, merged @0bf8103b1e (the feed script, its test, and a new `test_scope_feed_day_complete.py`). Re-run here at HEAD: IB231-1-AC1..AC3 PASS (exit 0). `round-close-check --round 3 --workstream "~PN"`: MAY-CLOSE. Nothing deployed (v130's live reads).

**The complete-day-only key criterion and its test: present and passing.** The order's criterion 2 is a difference control: it removes every `SCOPE-FEED-C` block in memory and requires the new test file to FAIL on assertions. `test_scope_feed_day_complete.py` was run here: **10 passed**. The tests include `test_day_with_a_failed_household_writes_no_key`, `test_complete_day_writes_both_keys`, `test_failed_households_are_named_in_the_output_and_the_exit_is_nonzero`, `test_a_throttle_stop_writes_no_key_for_the_day` (which also answers v128's held W429-S5, the partial key after a 429 stop), `test_from_date_window_writes_only_complete_days` and `test_rerun_after_a_failed_day_writes_the_day`. The existing feed test file passes 19.

**The dry-run-import STOP is in the feed apply order.** IB-pr-596 step (d), "the dry-run import on the runner (CTO msg 8536 item 3; a STOP)", runs the script on the runner via SSM without `--upload`. It must import, read the roster, print `PLAN ONLY` and exit 0; anything else is a STOP and Branch B. That answers v128's held W429-S4. The same order makes any `SKIPPED:` line in the first run a STOP and a row, and names the operator remedy (a rerun with `--from-date`) for W436-S2, the middle-of-window skip.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S39",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T19:51:00Z",
  "one_line": "~PN r3. The feed writes a day's keys only when every household answered; skipped days and their blockers are named, exit 1. Its criterion 2 is a difference control; test_scope_feed_day_complete.py runs 10 of 10 here (incl. a throttle stop writes no key), the older feed tests 19. The apply order IB-pr-596 carries the dry-run import on the runner as a STOP (step d, CTO msg 8536 item 3) and a SKIPPED line as a STOP. That closes v128's held W429-S4 and W429-S5. IB231-1-AC1..AC3 PASS; repository only. Dismissed (8): D2-W429-S4, -S5 (answered), D2-W436-S1..S5 and D2-S208 (the issuer's dispositions: S2 is handled by the --from-date rerun in the apply order; S5 the B copy shadowed by C, recorded).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W429-S4",
   "IRPT_BCKEND-D2-W429-S5",
   "IRPT_BCKEND-D2-W436-S1",
   "IRPT_BCKEND-D2-W436-S2",
   "IRPT_BCKEND-D2-W436-S3",
   "IRPT_BCKEND-D2-W436-S4",
   "IRPT_BCKEND-D2-W436-S5",
   "IRPT_BCKEND-D2-S208"
  ],
  "spec_asserts": "Signed pair (b) addendum 1 coverage rule (ABSENT, never a zero, never a fill); CTO msg 8536 item 3 (the dry-run import on the runner is a STOP before the apply).",
  "world_is": "The feed is complete in the repository with the day-complete rule tested; its apply order carries the import STOP and the skipped-day STOP. Nothing on the runner yet.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T19:3xZ of the invocations in IB-pr-599: IB231-1-AC1..3 PASS, exit 0; round-close-check ~PN round 3 MAY-CLOSE",
    "pytest data/inf/manual_api/test_scope_feed_day_complete.py: 10 passed; test_pull_inflection_scope_account_returns.py: 19 passed",
    "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-599.scope-feed-day-complete.md line 44 (the difference control)",
    "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-596.apply-scope-account-feed.md lines 29 (dry-run import STOP) and 31 (SKIPPED line STOP, --from-date remedy), amended @123bd21437",
    "investigation rows D2-W429-S4..S5, D2-W436-S1..S5, D2-S208",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PM1_PN2_PN3_PJ4_PJ5_PO8_DRAIN_END_20261015.md @f7b4555d40 (msg 8586)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two v128-held apply risks answered by the apply order and by tests; the worker rows dispositioned by S208 and checked here."
 }
]
```
