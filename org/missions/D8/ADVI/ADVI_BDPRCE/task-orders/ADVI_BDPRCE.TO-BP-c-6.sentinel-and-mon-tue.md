# ADVI_BDPRCE task order -- `BP-c-6` -- IS THE HONEST SENTINEL LINE DEPLOYED AND EXERCISED, AND WHY DOES THE MONDAY/TUESDAY FIRST EXPORT COME BACK HEADER-ONLY? (READ-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R3.md</decomp_doc>
<owned_cells>BP-c-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~18</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell READS the producers' schedules and logs; it adds and changes none.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api list-objects-v2`/`list-object-versions`/`head-object`/`get-object`; `logs filter-log-events`/`describe-log-streams`; `lambda get-function-configuration`/`get-function`; `events describe-rule`/`list-targets-by-rule`; `cloudtrail lookup-events`). No grant, no put, no invoke. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects `rerun` true, fewer than 14 runs checked, a cause off the closed set, a Monday/Tuesday row without evidence, a missing deployed-fix block and a write verb in `calls` (35-arm self-test OK). Blindness: the grader proves shape and read-only discipline, not that the cause is right; the issuer re-reads one cited log or version.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-c-6` (round 3; read-only; you re-run nothing)

Two linked questions from round 2's cause record (`org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~9/CAUSE.json`, `CAUSE.md`; read them first) and the CTO's round-2 analysis:

**(a) The honest sentinel line (row `ADVI_BDPRCE-D1-W9-S2`).** On 2026-10-05 and 2026-10-06 the bronze runner printed `OK: bronze sentinel emitted` while S3 held no sentinel. The repo's runner `infra/aws/lambda/bd-pipeline/bd-49f-runner/lambda_function.py` now prints `OK: bronze sentinel emitted` only after a `head_object` read-back (lines 156-198) and `WARN: bronze sentinel NOT emitted` otherwise (:168);
it was committed as `3709ae40d6` (2026-10-02) and the deployed function's `LastModified` reads 2026-10-07T00:50:44Z. The commit message says the runner role then lacked `s3:GetObject` on `bronze/*`, so the read-back could be refused. You establish: is the honest line deployed, and does it hold on the runs since the deploy?
**(b) The Monday/Tuesday header-only export.** On every Monday and Tuesday run date from 2026-09-14 to 2026-10-13 the first `forwardfill_v2/transactions/TRANSACTIONS_DAILY_<date>.xlsx` is header-only (about 4,356 bytes, zero rows). Why? Is it the export's date window (a rule in the runner or the template), the vendor returning no rows, or a runner defect?

### 1a. What to read

1. **Deployed fix.** `lambda get-function-configuration --function-name bd-49f-runner` (LastModified, CodeSha256, the role ARN) and `get-function` for the code location if readable. Compare the deployed code to the repo file at `3709ae40d6` as far as you can read it (download the deployment package the function reports if it is readable and compare the lines 156-198 text; if it is not readable, say so).
   Read the runner role's S3 policy for `s3:GetObject` on `bronze/*` (a named read of the role's attached and inline policies; `iam get-role-policy` / `list-attached-role-policies` on that ONE role).
2. **Every run since the deploy, and the 14 days before.** For each run date from 2026-09-29 to the newest (at least 14 dates, more if the logs reach), read the runner's log lines containing `bronze sentinel` and whether `bronze/<date>/_BRONZE_COMPLETE.json` exists (`head-object`). Count `honest_lines` (an OK line with the sentinel present, or a WARN line with it absent) and `dishonest_lines` (an OK line with the sentinel absent).
   The log group retention is 14 days: state the oldest event you can read. `runs_checked` is the number of run dates read.
3. **The Monday/Tuesday rows.** For each Monday and Tuesday run date in the window (09-14 .. the newest): `weekday`, `first_export_bytes` (the first version of the transactions workbook), `sentinel_exists`, and one line of evidence (a version time and size, a log event id). Include 2026-10-12 (Mon) and 2026-10-13 (Tue), the first two since the deployed fix.
4. **The window rule.** Find where the runner or the template sets the transactions export's date window (look for `asOfDate`, `startDate`, `endDate`, `today`, `utcnow`, a business-day offset; the P1 history in `git log -S asOfDate -- infra/aws/lambda/bd-pipeline/bd-49f-runner/lambda_function.py` is a hint) and quote file and line. Work out what window the export covers on a Monday and a Tuesday run, against the trade dates in the data:
   does a Monday run ask for Sunday's trades (none) and a Tuesday run for Monday's? Compare with the trade dates inside a normal day's export (a Wednesday file) and with the following day's file (does Tuesday's data arrive in Wednesday's workbook?).
5. **The cause**, in the closed set: `EXPORT_WINDOW_RULE` (the window rule asks for a day with no trades), `VENDOR_EMPTY` (the window is right and the vendor returned nothing), `RUNNER_DEFECT` (the runner builds the request wrongly), `NOT_DETERMINED` (name what could not be read). State what a later cell would change (named, not made).

### 1b. The record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~18/SENTINEL.json`

```json
{"order": "BP-c-6", "read_at": "<ISO UTC>", "claim": "measured", "calls": ["aws lambda get-function-configuration ...", "..."], "rerun": false,
 "deployed_fix": {"deployed": true, "last_modified": "<ISO>", "code_sha256": "<b64>", "evidence": "<how the deployed code was compared; the role's GetObject on bronze>"},
 "log_retention_days": 0, "runs_checked": 0, "honest_lines": 0, "dishonest_lines": 0,
 "monday_tuesday": [{"date": "YYYY-MM-DD", "weekday": "Mon", "first_export_bytes": 0, "sentinel_exists": false, "evidence": "<version time and size, log event id>"}],
 "window_rule": "<file:line, and what window a Monday and a Tuesday run ask for>",
 "cause": "EXPORT_WINDOW_RULE | VENDOR_EMPTY | RUNNER_DEFECT | NOT_DETERMINED", "cause_evidence": "<three sentences>", "later_cell_would": "<named, not made>"}
```
`runs_checked` is at least 14. Also write `SENTINEL.md` (one page in plain words: whether the honest line is live and held, the Monday/Tuesday pattern and its cause, the fix a later cell would make, what stays unknown).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no invoke, no export run, no producer run, no product file edited. Downloaded files go to `C:/dev/wk-bdprce-r3-18-data/` (outside the checkout).
2. No client name, account number or advisor name is printed. Do not print a secret value from a Lambda environment.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-c-6 needs the key listing`. A read that cannot finish reports `claim: absent` for what was not read.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~18/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~18/ADVI_BDPRCE.TO-BP-c-6.sentinel-and-mon-tue.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-c-6"><invocation>cd /c/dev/wk-bdprce-r3-18 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round3/checks/r3_checks.py sentinel --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~18/SENTINEL.json</invocation><expect>^SENTINEL record ok runs=[0-9]+ honest=[0-9]+ dishonest=[0-9]+ cause=(EXPORT_WINDOW_RULE|VENDOR_EMPTY|RUNNER_DEFECT|NOT_DETERMINED) deployed=(true|false)$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-c-6"><invocation>cd /c/dev/wk-bdprce-r3-18 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r3-18 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~18/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape, closed set and read-only discipline; AC2 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged). The cause's truth is read by the issuer from one cited log or version.

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit `SENTINEL.json` and `SENTINEL.md` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W18-S<k>` (D1 coordinate required), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: whether the honest line is deployed and whether it held (honest and dishonest counts over the runs checked), the role's `GetObject` on bronze, the Monday/Tuesday pattern with 2026-10-12 and 2026-10-13, the window rule with file and line, the cause, AC1, AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 analysis items 4 and 5 (first half). The analysis ordered an honest sentinel LINE under a pair; the issuer's measurement at the cut found the line already in the repo (committed 2026-10-02) and deployed (2026-10-07), so this order verifies instead of building (the decomposition says so). If the line is NOT deployed or does not hold, the record says so and the CTO's ruling stands as a later cell.
Closes the cause condition of `W9-S2` and of the Monday/Tuesday header-only export. Read-only; class LOCAL.

<status>pending</status>
<round>3</round>
<workstream>SENTINEL</workstream>
<to_id>ADVI_BDPRCE.TO-BP-c-6</to_id>
<slot>~18</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
