# NEVER-WIDEN -- COO half: FWD-5's first moved trigger -- Inflection `inf-portal-publisher` from an S3 notification to a Scheduler clock floor (plan moves M01, M03, M04 steps (1) and (2)) (`2.0.0_SA_COO~B1`, 2026-10-14 ~13:3xZ)

Pair: this half and the CTO's half (his file, named at the signing). The ruling that asks for it: `ledger/CTO_RULING_FB_L5_FIRST_MOVED_TRIGGER_AND_Q1_20261014.md` @8d4b58a823 (msg 5530), with its three
conditions C1 to C3, all carried below. The plan rows: `deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json` moves M01, M03, M04, in the order of `ledger/FWD9_MOVE_PLAN.md`. The order it covers:
`task-orders/ADVI_FIRMBKTS.TO-FB-l-5.first-moved-trigger.md`. Executor: `0.7.0_AE_CloudOps~FB1`.

## What moves, and what it may touch (the permitted set, nothing wider)

Three acts in this order; each opens its own ledger entry and reads back before the next.
1. **M01 -- `exec-summary-trigger` under Terraform (state and code only).** In `infra/aws/terraform/exec-summary/` the placeholder resource `exec_summary_trigger_placeholder` is replaced by the rule `exec-summary-trigger`
   (live pattern `chain-complete` from `bd-pipeline.gold-chain`, sole target `exec-summary-generator`) and imported. The plan after the import must show ZERO changes to the rule and target, and
   `describe-rule` reads ENABLED with the same EventPattern before and after. Any change is a STOP. (This moves no trigger; it is the plan's first row and the CTO ruled it in.)
2. **M03 -- the publisher's new trigger, created DISABLED, then exercised once.** New: EventBridge Scheduler schedule `inf-portal-publisher-floor` (default group, target `inf-portal-publisher`, retry 1 and 3600 s
   maximum event age, dead-letter queue, flexible window OFF, state DISABLED), plus only the resources that schedule needs (its dead-letter queue and queue policy, the scheduler's invoke role and policy). The shape
   copies `infra/aws/terraform/opal-assets/advi_49f_publisher.tf:75-110`. **Cron (C2):** set from the gold-completion times of AT LEAST 10 trading days (the marker `gold/meta/pipeline-complete.json`'s
   version history, or the chain completion logs; trading days by `lib/trading_calendar.py`), the series, its latest and the margin printed; the cron time is the latest completion plus a margin of at least 30 minutes.
   No existing resource changes in this act.
3. **M04 steps (1) and (2) -- the switch, in ONE apply (C3).** The floor is set ENABLED and the `gold/meta/` + `pipeline-complete.json` entry is removed from the `opal-data-inf` bucket notification, in the same
   Terraform apply, so the publisher is never triggered twice and never zero times. The bucket notification is a singleton: it is read whole before and after, and the silver entry
   (`silver/_silver_complete/` + `.json` -> `inf-silver-aggregator`) is byte-unchanged. The apply runs between the day's marker-triggered publish and the next day's gold completion.
   **NOT in this pair:** M04 steps (3) to (6): the rule `mdpf-feeder-accelerator`, the marker object and its S3 delete (Andrew's confirmation at the moment it runs, C3), the fence Deny. Each is a later change with its own half.

## What the exercise writes (C1, named)

The one-time `at()` exercise of the floor invokes `inf-portal-publisher`, which writes served output in `opal-data-inf`, and the publisher fans out an asynchronous invoke of `inf-portal-advisor-publisher`
(`lambda_function.py:924-935`), which writes more. The set the exercise may write, and nothing else:
- the three firm snapshots `platinum/firm/snapshots/aua_by_architect.json`, `aua_by_state.json`, `aua_by_region.json`;
- the advisor artifacts `platinum/advisors/<advisor_key>/{book,summary,top_holdings,timeseries}.json` for every Inflection advisor (the count is listed and printed before the exercise; this is the same set every daily publish writes).
The exercise runs ONLY after that day's Inflection gold has been read complete (the marker is newer than the day's gold completion and the gold chain's log reads COMPLETE): an exercise must never publish partial gold.
**Before the exercise, the prior VersionId of every key above is recorded in `deliverables/0.7.0_AE_CloudOps~FB1/rollback_versions_l5.json`** (advisor keys by `<advisor_key>`; no client name or relationship id is printed).

## What the publisher does when it fires early (C2, from the code)

Read at `infra/aws/lambda/inf-portal-publisher/lambda_function.py:915-971` and `load_all` (`:173`): the handler takes NO input from the event. It loads whatever source parquets are in the bucket at that moment
(`_load_parquet_prefix_latest`, `_latest_silver_partition`), builds the three snapshots from them, and writes them; it then invalidates CloudFront. It does not check that gold is complete. **So an early fire PUBLISHES WHAT IS
THERE (the prior complete day's data, or a mix if gold is part-written): the margin in the cron is the only guard**, which is why C2 sets the cron from at least 10 trading days and adds the 30-minute margin.
(Today the S3 notification is the other guard: it fires only after the marker exists. The floor removes that guard by design; that is the defect class the CTO's ruling names, and the margin replaces it.)

## Writers of the property (counted, N printed)

N = 2 for the exercise's writes: `inf-portal-publisher` (the three snapshots) and `inf-portal-advisor-publisher` (the advisor artifacts). The gold chain writes the sources, not these keys. After M04 the trigger count for the
publisher is 1 (the floor); before, 1 (the notification). Nothing else may start `inf-portal-publisher`.

## Both branches

- **Branch A (expected):** M01 reads zero change; the floor exists DISABLED with the stated cron; the exercise produces a publisher invocation (log line) and a LastModified after the exercise time on the three snapshots; all keys
  written are inside the named set; the single apply of act 3 enables the floor, removes only the `gold/meta/` entry, and the plan is exactly those two changes; the next gold completion after the apply is followed by ONE publish at the
  floor, not two.
- **Branch B (STOP, roll back, report):** M01's plan shows any change; fewer than 10 trading days of completion times; the exercise would run before that day's gold is read complete; any key written outside the named set; the publisher
  errors; the act-3 plan shows any change other than the floor's state and the `gold/meta/` entry; the silver entry changes; the publisher fires twice for one gold completion.

## Rollback per object

- M01: `terraform state rm` of the imported rule and target, then revert the commit; the live rule is untouched by the import.
- The floor: set it DISABLED or delete it (Terraform revert, `safe-apply`); until act 3 the S3 notification is the live trigger, so the rollback restores the status quo.
- The exercise: for each key in the named set, restore its prior VersionId from `rollback_versions_l5.json`; CloudFront is invalidated again.
- Act 3: disable the floor and restore the `gold/meta/` entry (Terraform revert of the notification, `safe-apply`), so the S3 notification is the trigger again and the floor is DISABLED.

## What this half does not know (named)

- The gold completion times of the last 10 trading days: C2 makes FB1 read them; this half sets no cron.
- Whether anything else consumes the marker's S3 event beyond `mdpf-feeder-accelerator` and the publisher: the plan and census read none; the marker object itself is NOT touched by this pair.
- Whether the advisor publisher's key count is stable day to day: FB1 lists it before the exercise.

**SIGNED by `2.0.0_SA_COO~B1` for exactly these three acts, the named key set, the single apply of act 3 and this rollback.** Any other resource, `M04` steps (3) to (6), a second exercise on another day, or a change to either
publisher's code or environment needs a new half.
