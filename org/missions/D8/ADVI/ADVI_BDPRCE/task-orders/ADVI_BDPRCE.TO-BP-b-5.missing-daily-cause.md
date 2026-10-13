# ADVI_BDPRCE task order -- `BP-b-5` -- WHY SIX DAILY PRICE FILES ARE MISSING AND THE SERVED DETAIL OBJECTS RUN A DAY BEHIND (READ-ONLY, NO RE-RUN)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R2.md</decomp_doc>
<owned_cells>BP-b-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~9</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell READS the producers' schedules and logs; it adds and changes none.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api list-objects-v2`/`list-object-versions`/`head-object`; `logs filter-log-events`/`describe-log-streams`; `events list-rules`/`describe-rule`/`list-targets-by-rule`; `lambda get-function`/`list-functions`; `cloudtrail lookup-events`). No grant, no put, no invoke. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects `rerun` true, a date class off the closed set, a date row with no evidence, a missing producer and a write verb in `calls` (33-arm self-test OK). Blindness: the grader proves shape and read-only discipline, not that a cause is right; the issuer re-reads one cited log or version per class.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-b-5` (round 2; read-only; you re-run nothing)

Two lags are open in round 1's record and neither has a named cause:
1. **Six trading days have no `silver/prices/<date>.parquet`** (any version): 2026-09-21, 2026-09-22, 2026-09-28, 2026-09-29, 2026-10-05, 2026-10-06. Every one is a Monday or Tuesday, and each is a trading day by
   `lib/trading_calendar.py` (use that file; do not reason from the weekday). Row `ADVI_BDPRCE-D1-W3-S2`. The daily price Lambda `bd-price-update` writes the daily file (round-1 census:
   `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~1/WRITERS.md` and `WRITERS.json`; read them first).
2. **The served 49F client detail objects carry `data_as_of` 2026-10-09 on a 2026-10-13 read**, one trading day behind T-1 (2026-10-12) (row `D1-W4-S1`), and 9 of 120 sampled objects are older still (row `D1-W4-S10`).
   The key carries no date; the as-of date is in the body (`entities/clients/<key>/detail.json`, field `data_as_of`; the object `generated_at` is also in the body).
The CTO's order: read the cause from the producer's own schedule and logs against the trading calendar; **no re-run**; the fix is a later cell once the cause is named.

### 1a. What to read

1. **The six dates.** For each date: what should have written the daily file (the Lambda's EventBridge rule and its cron, and the S3 or other trigger if any); whether that program RAN that day (its CloudWatch
   log streams and invocations around the expected time, within the log group's retention: state the retention and the oldest event you can read); if it ran, whether it succeeded, wrote another key
   (list `silver/prices/` objects with LastModified on the date and the day after), or wrote nothing; if it did not run, whether the schedule skipped the day (compare the cron's day-of-week and the
   local-time versus UTC offset of the run with the date of the data). Classify each date in the closed set `NO_RUN`, `RUN_FAILED`, `RUN_SKIPPED_BY_SCHEDULE`, `WROTE_ELSEWHERE`, `NOT_DETERMINED`
   (a date you cannot read because the log retention ended is `NOT_DETERMINED`, with that reason; never a guess). Evidence per date: an event id, a log stream name or a listing, with its time.
2. **The lag of the detail objects.** Find the producer of `platinum/entities/clients/*/detail.json` in `opal-data-49financial` (start at `org/missions/D8/ADVI/ADVI_FIRMBKTS/` records, the repo's ADVI
   builders, and the portal's reader; use the repo-search tool or the native Grep tool), its schedule, and how it derives `data_as_of` (from which input's date: max trade date, the silver partition day,
   the gold lots date, or a T-1 rule). State whether the one-trading-day lag is by design (a documented T-1 rule) or a defect, from the code and `lib/trading_calendar.py`, citing file and line.
   For the older objects, state from the object bodies whether they are closed or inactive relationships (a termination date field) without printing any name.

### 1b. The record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~9/CAUSE.json`

```json
{"order": "BP-b-5", "read_at": "<ISO UTC>", "claim": "measured", "calls": ["aws logs filter-log-events ...", "..."],
 "rerun": false, "log_retention_days": 0,
 "dates": [{"date": "2026-09-21", "class": "NO_RUN | RUN_FAILED | RUN_SKIPPED_BY_SCHEDULE | WROTE_ELSEWHERE | NOT_DETERMINED",
            "evidence": "<event id, stream or listing, with its time>", "expected_writer": "<lambda:name>"}],
 "pattern": "<one paragraph: what the six dates have in common, or none>",
 "behind_objects": {"producer": "<script or lambda id>", "schedule": "<cron or trigger>", "derivation": "<how data_as_of is derived, file:line>",
                    "by_design": true, "evidence": "<citation>", "older_objects": "<closed or inactive, from the bodies>"}}
```
Also write `CAUSE.md` (one page in plain words: what ran and what did not on the six dates, why the objects are a day behind, whether either is a defect, and the fix a later cell would make, named and not made).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no invoke, no producer run, no product file edited. Downloaded files go to `C:/dev/wk-bdprce-r2-9-data/` (outside the checkout).
2. No client name, account number or advisor name is printed anywhere. Count objects; do not list keys.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-b-5 cause needs the key listing`. A read that cannot finish reports `claim: absent` for what was not read.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~9/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~9/ADVI_BDPRCE.TO-BP-b-5.missing-daily-cause.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-b-5"><invocation>cd /c/dev/wk-bdprce-r2-9 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round2/checks/r2_checks.py cause --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~9/CAUSE.json</invocation><expect>^CAUSE record ok dates=[0-9]+ determined=[0-9]+ undetermined=[0-9]+ producer=\S+$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-b-5"><invocation>cd /c/dev/wk-bdprce-r2-9 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r2-9 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~9/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape, closed set and read-only discipline; AC2 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged). The cause's truth is read by the issuer from one cited log or version per class.

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit `CAUSE.json` and `CAUSE.md` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W9-S<k>` (D1 coordinate required), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the class of each of the six dates (with the pattern), the producer and derivation of the detail objects and whether the lag is by design,
what stays NOT_DETERMINED and why, AC1, AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 analysis item 5; closes the cause condition of `W3-S2`, `W4-S1`, `W4-S10` (owner CTO). The fix is not this cell's. Read-only; class LOCAL.

<status>pending</status>
<round>2</round>
<workstream>CAUSE</workstream>
<to_id>ADVI_BDPRCE.TO-BP-b-5</to_id>
<slot>~9</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
