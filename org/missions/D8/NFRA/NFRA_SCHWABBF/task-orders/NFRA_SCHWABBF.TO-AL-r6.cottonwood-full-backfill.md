# TO NFRA_SCHWABBF.TO-AL-r6 -- Cottonwood: read one day end to end, then backfill every ENTITLED master to Schwab's floor (one at a time, denominator printed)

<to_id>NFRA_SCHWABBF.TO-AL-r6</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>alongside-backfill</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-r-6` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) | **outcome_ref:** FWD-8 |
**depends_on:** `TO-AL-r2` complete (the entitlement read and a one-day pull for at least one master). Start at step 1 only after r2's report names at least one master with `DAILY PULL OK`.

---

## WORKER FACE

### GO

GO -- written by 2.0.0_SA_COO~SA 2026-10-21 ~15:0xZ. Andrew-direct ~14:5xZ, VERBATIM: "Ok great, let's get these backfilled." (record via `1.0.0_SA_CTO` msg 110117). The CTO: "Drive without waiting on further words ... My condition 6 gates only ENABLING the daily rules, not the backfill." So: NO rule is enabled by this order (the four stay DISABLED); the backfill runs under the box's session lock; every enumerated day is accounted as downloaded + skipped + failed.

### THE CELL

`AL-r-6`, PRD C-BACKFILL for the four Cottonwood masters: "History from Schwab's floor (2023-10-17, measured 2026-10-19 21:21Z and again 2026-10-20 08:50Z) ... The puller's own search, download and vendor-master guard are used (`sdd-daily-pull.ps1`) under the box's SDD session lock ... It lands only at the builder's key ... The run record's denominator: enumerated = downloaded + skipped + failed." The box's puller (`C:/schwab-sdd/sdd-daily-pull.ps1`, the exact copy of the 49F puller) is "daily pull + backfill + self-heal" in one mechanism: one wide search, never chunked, resumable (it skips what has landed). A backfill run is the puller with a wide lookback and NO `-OnlyAsOf`: `-Master <m> -Target monolith -LookbackDays 1200` (1200 days reaches before the 2023-10-17 floor from 2026-10). Each landed `.zip` under `schwab/cottonwood/bronze/` fires the converter Lambda `opal-assets-silver-schwab` (S3 event rule `silver-schwab-cottonwood`, live; the converter was redeployed at 13:15Z with the firm-form logic), so a backfill is also thousands of converter invocations; you watch for harm (step 3). Masters are pulled ONE AT A TIME (one Schwab session, one lock).

### DO, IN THIS ORDER

1. **GATE: read the one-day result end to end before any backfill** (from the laptop, your own identity; for each master `TO-AL-r2` pulled, with its day `D`): (a) bronze: the keys under `s3://opal-data-assets/schwab/cottonwood/bronze/` whose names contain `/date=<D>/<master>.` (count, 3 samples); (b) silver: keys under `s3://opal-data-assets/schwab/cottonwood/silver/` whose names end `/date=<D>/<master>.parquet` (count and the table names); (c) the state run record: list `s3://opal-data-cottonwood/schwab/cottonwood/state/pulls/` and `.../state/daily_pull/` for keys beginning `<master>.` under `date=` partitions (the fence admits the box role for these prefixes; it admits your AWS identity too), and READ one run manifest object (it holds counts, not secrets) and print its `downloaded`, `skipped`, `enumerated`, `failed` fields; (d) converter health: `aws logs filter-log-events --log-group-name /aws/lambda/opal-assets-silver-schwab --start-time <10 minutes before the pull> --filter-pattern ERROR` (print the count and the first 3 messages) and the DLQ depth `aws sqs get-queue-attributes --queue-url https://sqs.us-east-1.amazonaws.com/313476888478/opal-assets-silver-dlq --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible` (record it as the BASELINE). Save to `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/r6/gate.txt`. **If bronze, silver or the state record is missing for a pulled master, or the converter logged errors for it, STOP and report; do not start any backfill.** Report the gate result to `2.0.0_SA_COO~SA` before step 2 (do not wait for a reply; this is for the record and the CTO).
2. **BACKFILL, one master at a time** (the masters the entitlement read printed `ENTITLED`, in numeric order; never a master it printed `NOT-ENTITLED`): over SSM (`AWS-RunPowerShellScript`, a `commands` JSON from a NON-SHELL writer, forward slashes in on-box paths) register and START a one-shot task as Administrator, exactly the pattern of `TO-AL-r2` step 4 (`/RU Administrator /IT /RL HIGHEST`, prove it started), running `powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:/schwab-sdd/sdd-daily-pull.ps1 -Master <master> -Target monolith -LookbackDays 1200 -SnsTopicArn arn:aws:sns:us-east-1:313476888478:opal-critical-surface-alerts`. **Do NOT hold the SSM command open for the whole run** (an invocation is capped well below a multi-hour run): start the task, return, and POLL: every 10 minutes read `Get-Content C:/schwab-sdd/daily/<master>/daily-pull.log -Tail 20` and the task state/`LastTaskResult` over short SSM calls. The puller ends `DAILY PULL OK: downloaded=<n> skipped=<n> enumerated=<n> guard=OK` or dies loud. Exit 7 means a sibling holds the session lock: wait 5 minutes and retry once, never delete the lock file. Exit 9, 3 or 8: stop and report (9 = no file for the filter, 3 = token missing, 8 = wrong identity).
3. **Watch for harm while it runs** (every poll): the converter's `Errors` and `Throttles` for the last 10 minutes (`aws cloudwatch get-metric-statistics` on namespace `AWS/Lambda`, function `opal-assets-silver-schwab`, statistics Sum) and the DLQ depth against the step-1 BASELINE. **If the DLQ depth rises by more than 25 above the baseline, or Throttles stay above 0 for two consecutive polls, STOP the task** (`schtasks /End`), report the numbers to `2.0.0_SA_COO~SA`, and do not restart without a reply. A stopped run is safe to resume: the puller skips what has landed.
4. **After each master, account for it** (from the laptop): the final log line (`enumerated`, `downloaded`, `skipped`, and any `failed`; the run must satisfy enumerated = downloaded + skipped + failed with `failed=0`; if `failed` is not 0, run the same command ONCE more, which retries only what is missing, and report both lines); the bronze census: object count under `schwab/cottonwood/bronze/` whose key contains `/<master>.` and the distinct `date=` partitions count, the EARLIEST and LATEST date, and whether the earliest equals Schwab's floor `2023-10-17` (print the comparison; if the earliest is LATER than the floor, name the gap in days and say whether the log shows a search window or a master entitlement start); the silver census for that master (count of `<master>.parquet` keys, tables); the converter Errors sum and DLQ depth now versus the baseline. Save to `.../r6/<master>_accounting.txt`.
5. Send a one-line progress message to `2.0.0_SA_COO~SA` at each master's start and end (master, days, objects, failed, DLQ delta). After the last master, commit all evidence with `safe-commit.sh` paths-only and send the final summary table (per master: enumerated, downloaded, skipped, failed, earliest, latest, silver objects, DLQ delta).

### ACCEPTANCE (read by the issuer from your committed files)

<criterion id="AL2-r6-AC1" cell_refs="AL-r-6"><invocation>python .tools/proof-of-spec-check.py org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-AL-r6.cottonwood-full-backfill.proof_of_spec.json AL2-r6-AC1</invocation><expect>VALID</expect></criterion>
`AL2-r6-AC1` -- the proof instance records the gate reads, and per master the log line, the identity enumerated = downloaded + skipped + failed with failed = 0, the earliest and latest dates against the floor, the silver count and the converter/DLQ deltas as artifact rows.

<expected_criteria>AL2-r6-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. No Terraform, no IAM, no security group, no registry, no code edit.
- **Never:** enabling a rule; running two masters at once; deleting the lock file or any S3 object; pulling a master the read printed `NOT-ENTITLED`; touching the Administrator session, the SI2 app or `UserAuthentication`; `get-secret-value` on any Alongside secret; reading or printing the Schwab token; a backfill window narrower or wider than the command above; continuing past a stop condition of step 3.
- **A surprise row you file is committed AT ONCE** with `bash .tools/safe-commit.sh ... -- <the investigations file and your r6/ files>` (paths only) and its hash sent to `2.0.0_SA_COO~SA`.
- **Refusal clause.** If a step cannot be met as written, stop, write the reason and output in your report and a surprise row, and do not improvise.

<paths>
org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, enrichment), cell `AL-r-6`.
<owned_cells>AL-r-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AL2-r6-AC1. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-AL-r6.cottonwood-full-backfill.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL2-r6-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (your messages to `2.0.0_SA_COO~SA`):** the step-1 gate result; a line at each master's start and end; the final summary table.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the four rules stay DISABLED; the backfill is an ad hoc run under the session lock; no fire slot is used.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the box role's bronze write grant (per master, by file-name prefix) was applied by TO-AL-r1; a PutObject denial is a stop condition.
comp-adversary: DECLARED-NOT-APPLICABLE -- findings: (1) every landed object fires the converter (live event rule), so the DLQ and throttle watch in steps 1 and 3 is the control; (2) one Schwab session means one master at a time; (3) a master the login does not list returns 204, so the entitlement read precedes every pull.
lane: the <paths> block IS the grant; CloudOps seats act on Schwab-touching infrastructure under a task order (rule 34).
</preflight>

Source: PRD v1.0 C-BACKFILL, C-ALONGSIDE; Andrew-direct ~14:5xZ 2026-10-21 via CTO msg 110117; CTO condition 6 (gates enabling, not this); decomposition cell AL-r-6.
