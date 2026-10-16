# ADVI_FIRMBKTS Door 6, step 2 -- the reads the CTO asked for before any rule is disabled (`2.0.0_SA_COO~B1`, 2026-10-16 ~19:0xZ)

**Asked by:** `1.0.0_SA_CTO~DELL1` decision text `ledger/CTO_DECISION_DOOR6_RETIREMENT_ORDER_20261016.md` (msg 6975), step 2: the gold chain's completion time against 12:52Z over the last 10 trading days with the denominator, and whether `mdpf-feeder-trigger` checks readiness before it reads. All reads are live or from the tree at HEAD; nothing was written.

## 1. Completion against the 12:52Z backstop (denominator: 10 trading days, 10 of 10 with a marker write)

The 10 trading days are the last 10 by `lib/trading_calendar.py` `is_trading_day` up to 2026-10-16 (2026-10-05 to 2026-10-16). Two timestamps per day, both `LastModified` in UTC: the chain's completion marker `gold/meta/pipeline-complete.json` (`list-object-versions` returned 17 versions in all; each of the ten days carries exactly one write) and the feeder's own readiness gate `gold/eclipse/<date>/_meta/gold_complete.json` (head-object).

| trading day | marker written | gate `gold_complete.json` landed | vs 12:52:00Z |
|---|---|---|---|
| Mon 10-05 | 12:45:19 | 12:45:27 | before |
| Tue 10-06 | 12:55:11 | 12:55:20 | AFTER |
| Wed 10-07 | 12:54:54 | 12:55:02 | AFTER |
| Thu 10-08 | 12:52:38 | 12:52:48 | AFTER |
| Fri 10-09 | 12:51:17 | 12:51:26 | before |
| Mon 10-12 | 12:48:09 | 12:48:17 | before |
| Tue 10-13 | 12:59:59 | 13:00:11 | AFTER |
| Wed 10-14 | 12:53:40 | 12:53:49 | AFTER |
| Thu 10-15 | 12:56:44 | 12:56:58 | AFTER |
| Fri 10-16 | 12:56:43 | 12:56:52 | AFTER |

**7 of 10 days finish after the backstop's 12:52:00Z, on both timestamps.** Earliest 12:45:19Z, latest 12:59:59Z (marker) and 13:00:11Z (gate). The gate lands 8 to 14 seconds after the marker.

## 2. Does `mdpf-feeder-trigger` check readiness? Yes, and it has no retry

`infra/aws/lambda/mdpf-pipeline/mdpf-feeder-trigger/lambda_function.py` (209 lines; the live function is Active, last modified 2026-08-19, timeout 360 s):
- It takes `run_date` from the event or today UTC (`:151`), then `head_object`s two gates before it dispatches: `gold/eclipse/{run_date}/_meta/gold_complete.json` on `opal-data-inf` (`WSC_GATE_KEY`, `:93`) and `schwab/silver/rps/date={YYYYMMDD}/data.parquet` on `opal-data-bd` (`WSE_GATE_KEY`, `:100`). (`:155-156`)
- If the Inflection gate is absent it returns `dispatched: False, reason: NOT-YET` and exits clean (`:162-168`). Its docstring: "NOT-YET IS NOT AN ERROR ... We log NOT-YET with the date we looked for, write nothing, and exit clean."
- Nothing re-fires it. The only things that start it: the Scheduler schedule `mdpf-feeder-backstop-daily` (`cron(52 12 * * ? *)`, ENABLED) and the EventBridge rule `mdpf-feeder-accelerator` (ENABLED; `list-rule-names-by-target` returns that one rule).
- Its own docstring states the topology and why: "A LONE FIXED CRON IS STRUCTURALLY WRONG HERE: it must be both AFTER a ... variable input and BEFORE the 13:30Z consumer", so the event is kept "as an ACCELERATOR on top". That was written for an August input spread of 7h36m; the ten days above spread 15 minutes.

**Consequence for the ordered sequence:** the readiness check the CTO's step 2 offered to add already exists. What the backstop alone lacks is a second look. With the accelerator disabled and the backstop at 12:52Z, on a day like 7 of the last 10 the 12:52Z fire reads NOT-YET, exits clean, and nothing fires the feeder again that day. The two branches the decision text names that remain: move the backstop after the measured completion time, or give the trigger a second fire. The measured latest gate landing is 13:00:11Z; the docstring names a "13:30Z mdpf floor" as the consumer the feeder must beat (that consumer was not read here).

## 3. How the 49 Financial feeder is triggered (as far as it was read)

The 49 Financial side (WS-E, `non_model_aua`) is not a separate trigger: it is the second gate inside the SAME function. `mdpf-feeder-trigger` dispatches `mdpf-daily-dispatch.sh --date <run_date>` for both feeders, and the only things that start the function are the 12:52Z backstop and the Inflection accelerator above. So the 49 Financial leg is fired by the fixed-time backstop plus its readiness gate (the rps parquet), with no event accelerator of its own.

## 4. What these reads do NOT establish (named)

- How long the dispatch takes (the SSM command on the runner), so whether a backstop moved to about 13:05Z still lets the feeder finish before the 13:30Z floor. Not read; it is the number the "move the backstop" branch needs.
- Whether `inf-gold-trigger`'s second same-day dispatch (the CTO's finding 1) has ever fired; not read.
- How a 49 Financial day behaves when the rps parquet lands after 12:52Z: not read (it would meet the same NOT-YET and have no second fire). Whether any separate trigger exists for it outside this function was searched for through the rules that target the function (one) and the schedules by name; no other path was found, which is not a proof that none exists.
- The ten days are the last ten, not a distribution: a day later than 13:00:11Z has not been seen in them, and August showed a 7h36m spread.
- The deployed runner copies in `s3://opal-data-inf/code/runner/` (the live writer of the marker), the CTO's step 3 precondition: not read here.
