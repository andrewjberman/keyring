# ADVI_BDPRCE task order -- `BP-c-4` -- IS 500,000 AN EXPORT CAP? (READ-ONLY, BEFORE ANY APPLY OF THE UNITS AND COST BASIS SWITCH)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R3.md</decomp_doc>
<owned_cells>BP-c-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~16</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only measurement; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api get-object`/`list-objects-v2`/`list-object-versions`/`head-object`; `lambda get-function-configuration`; `logs filter-log-events`). No grant, no put, no invoke. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a verdict off the closed set, a days-at-500000 count that differs from the per-day rows, fewer than ten days, an empty evidence or paging field and a write verb in `calls` (35-arm self-test OK). Blindness: the grader proves shape and arithmetic, not that the verdict is right; the issuer re-reads one cited export.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-c-4` (round 3; read-only)

Black Diamond's unrealized-gains export (query type 4, the 49 Financial template `data/black_diamond/scripts/bronze/templates/unrealized.json`) is pulled daily by the bronze runner `infra/aws/lambda/bd-pipeline/bd-49f-runner/lambda_function.py` into `opal-data-bd` bronze as `UNREALIZED_DAILY_<date>.xlsx`.
Round 2's fixture used the export of 2026-10-09 and it held EXACTLY 500,000 rows (row `ADVI_BDPRCE-D1-W10-S3`; `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~10/LOT_PROOF.md`). A round-number count is the signature of a vendor cap, and a capped export silently drops lots, the opposite of the project's exact-lot outcome.
The CTO's order: before ANY apply of the Units and Cost Basis switch, a read-only cell proves whether 500,000 is a cap, from the export's own paging and limit settings and from a second export window. You do that. You change nothing and run nothing.

### 1a. What to read

1. **The row count of each day's export.** For at least the last 14 run dates (more if available), find the bronze unrealized export key for each date (find the key pattern from the runner and the silver step `data/black_diamond/scripts/silver/merge-daily-incremental.py` `process_unrealized_xlsx_to_parquet`; list the bronze prefix with `list-objects-v2`) and read its data-row count
   (stream the file's row count from the xlsx sheet dimension or read it with openpyxl in read-only mode; download to `C:/dev/wk-bdprce-r3-16-data/`; do not load a whole file into memory if it is large). Record `rows_per_day` (date -> rows) and the count of days at exactly 500,000.
2. **The paging and limit settings.** Read the runner code and the qt4 template/query body for any limit, page size, `top`, `maxRows`, `pageSize`, row cap, or xlsx-limit knowledge (an Excel sheet holds at most 1,048,576 rows; 500,000 is below that, so say whether the xlsx format can be the limit). Quote file and line. Read the Lambda's configuration (`get-function-configuration`: environment variables, timeout, memory) for a limit knob, without printing a secret value.
3. **A second export window.** Compare days: if the export were a cap, every day with more positions than the cap reads exactly 500,000; if it is complete, the count varies day to day with the book. Read at least 10 further days (or the history of the bronze prefix, whichever is longer) and state the distribution: how many days are exactly 500,000, the smallest and the largest.
   `second_window` = `{"dates": [...], "rows": [...]}` for a window that does NOT include 2026-10-09's neighbours, e.g. a week from September.
4. **The verdict**, in the closed set: `CAP` (exactly 500,000 on more than one day, or a limit setting that yields it), `NOT_A_CAP` (the count varies and no limit setting yields 500,000), or `NOT_DETERMINED` (name what could not be read). One round number on one day is not a verdict.
5. **If CAP:** state from the evidence how the export would be paged until complete (the query's paging or date-slicing parameters), without running it.

### 1b. The record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~16/CAP.json`

```json
{"order": "BP-c-4", "read_at": "<ISO UTC>", "claim": "measured", "calls": ["aws s3api list-objects-v2 ...", "..."],
 "days_checked": 0, "rows_per_day": {"YYYY-MM-DD": 0}, "days_at_500000": 0,
 "paging_config": "<file:line quotes of any limit or paging setting, or 'none found' with what was searched>",
 "second_window": {"dates": ["YYYY-MM-DD"], "rows": [0]},
 "verdict": "CAP | NOT_A_CAP | NOT_DETERMINED", "evidence": "<three sentences>", "paging_plan": "<if CAP, else n/a>"}
```
`rows_per_day` holds exactly `days_checked` entries (at least 10) and `days_at_500000` must equal the number of entries equal to 500000. Also write `CAP.md` (one page in plain words: the distribution, the settings found, the verdict and what it means for the apply).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no invoke, no export run, no producer run, no product file edited. Downloaded files go to `C:/dev/wk-bdprce-r3-16-data/` (outside the checkout).
2. No client name, account number or advisor name is printed or committed.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-c-4 cap check needs the bronze prefix listing`. A read that cannot finish reports `claim: absent` for what was not read.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~16/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~16/ADVI_BDPRCE.TO-BP-c-4.export-cap-check.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-c-4"><invocation>cd /c/dev/wk-bdprce-r3-16 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round3/checks/r3_checks.py cap --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~16/CAP.json</invocation><expect>^CAP record ok days=[0-9]+ at_500000=[0-9]+ verdict=(CAP|NOT_A_CAP|NOT_DETERMINED)$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-c-4"><invocation>cd /c/dev/wk-bdprce-r3-16 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r3-16 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~16/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape, arithmetic, closed set and read-only discipline; AC2 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged). The verdict's truth is read by the issuer from one cited export.

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit your scripts, `CAP.json` and `CAP.md` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W16-S<k>` (D1 coordinate required), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the days checked, the distribution (days at 500,000, smallest, largest), the settings found with file and line, the verdict, AC1, AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 analysis item 3 (first read); row `W10-S3`. `BP-c-5` (the lot-key fixture proof) is staged on this cell's verdict, the CTO's order being check, then proof, then apply. Read-only; class LOCAL.

<status>complete</status>
<round>3</round>
<workstream>CAPCHECK</workstream>
<to_id>ADVI_BDPRCE.TO-BP-c-4</to_id>
<slot>~16</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
