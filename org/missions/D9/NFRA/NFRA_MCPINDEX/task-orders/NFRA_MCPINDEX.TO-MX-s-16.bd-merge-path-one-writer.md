# NFRA_MCPINDEX task order -- `MX-s-16` -- one writer per Black Diamond silver table: retire the Playwright documents' merge step (and the allocation processor) behind bd-silver-merge

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-16</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-s-16</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~24</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at PHASE A by the worker -- the four BD trigger rules (bd-{unrealized,realized,transaction}-pipeline-trigger 21:38/21:45/21:53Z, bd-allocation-pipeline-trigger 22:00Z MON-FRI) and bd-silver-merge's S3 trigger; no act inside 21:30-22:15Z or 00:00-00:30Z.
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy change; a notification and SSM document/rule change only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a writer retirement under never-widen halves (CTO + COO), DELTA=0 on served silver expected.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `MX-s-16` (round 6; `ROUND_ANALYSIS.round5.md` @1edec80f63 section 3 (Z-S69 ruling) and section 5 item 7; rows Z-S69, Z-S72)

**The CTO's ruling:** `bd-silver-merge` stays the writer of record, and the documents' merge step is retired, so each
BD silver table has ONE writer.

**Today, measured at the round-6 base (s16.AC1):**

| table | writers |
|---|---|
| transactions | the `opal-bd-transaction-download` document, and `bd-silver-merge` |
| realized | the `opal-bd-realized-download` document, and `bd-silver-merge` |
| unrealized | the `opal-bd-unrealized-download` document, and `bd-silver-merge` |
| allocations | the `opal-bd-allocation-download` document, `bd-silver-merge`, and `bd-allocation-processor` |

How each writer is wired:
- Each document (`infra/aws/ssm/opal-bd-*-download.json`, the download already stripped by MX-s-14) downloads
  `s3://opal-data-bd/scripts/merge-daily-incremental.py` and runs it per table.
- `bd-silver-merge` (`infra/aws/lambda/bd-pipeline/bd-silver-merge/lambda_function.py`) runs
  `code/silver/merge-daily-incremental.py` `run(["all"])`. It is triggered by `BronzeCompleteSilverMerge`
  (`infra/aws/terraform/bd-pipeline/s3-notifications.tf:71-77`, `bronze/` + `_BRONZE_COMPLETE.json`).
- `bd-allocation-processor` is triggered by `ProcessAllocationFiles` (`s3-notifications.tf:49-55`,
  `forwardfill_v2/allocations/*.xlsx`) and writes `silver/allocations/{date}.parquet`.

**⛔ ROW Z-S72 FIRST.** `bd-silver-merge`'s unrealized merge read `failures=6, rows_added=0` on 6 new files on BOTH
2026-09-30 00:15Z and 2026-10-01 00:14Z. The unrealized document wrote those 6 dates (2026-07-03..07-09) as 0-row
partitions at 2026-09-30 21:39Z. Retiring the unrealized document's merge without fixing this leaves a failing sole
writer.

### PHASE A -- no publish, no apply
1. **Census per table on the applied plane:**
   - which inputs each writer processed over the last 10 runs: the Lambda logs, and the documents' merge logs at
     `s3://opal-data-bd/logs/<leg>-download-<date>.log`;
   - for each document-merged input, whether `bd-silver-merge` also processed it, and when.
2. **Diagnose Z-S72:**
   - read `bd-silver-merge`'s per-file error lines for the 6 unrealized files, and the files themselves (bronze or
     forwardfill);
   - state why they fail, and whether the 0-row partitions the document wrote are correct (empty source files) or a
     defect.
   - A source-code fix to `data/black_diamond/scripts/silver/merge-daily-incremental.py` is in your `<paths>`. Deploying
     that script to its served key is a DS act under `.tools/safe-deploy.sh` and goes in the ANNOUNCE as a separate
     leg.
3. **Plan the retirement per table:**
   - for each document: remove its merge step, or disable its trigger rule through Terraform, whichever leaves no
     dead-but-scheduled run. The download is already gone (MX-s-14), so a document with no merge step does nothing;
   - for `bd-allocation-processor`: remove its S3 notification through Terraform ONLY IF the census proves
     `bd-silver-merge` processes every allocation input it does. Otherwise file a BLOCKING row and leave it;
   - nothing is deleted. Documents and functions stay, disabled or unreferenced, for rollback.
4. **Write `ANNOUNCE_MX-s-16.md`** in your deliverables:
   - the census and the Z-S72 diagnosis;
   - the per-table plan with its rollback per key;
   - the saved Terraform plan (targeted; any destroy of a non-notification resource is a BLOCKING row);
   - the expected served DELTA (0 on transactions, realized and allocations; unrealized per the diagnosis).
   Report and STOP. The issuer takes it to the never-widen halves.

### PHASE B -- only on the issuer's GO
5. Open the NEVER-2 ledger `nfra-mcpindex-r6-bd-merge-retire`, naming BOTH paths when committing: the entry under
   `org/critical_paths/change_management/` AND the sentinel
   `org/critical_paths/.open_deploys/nfra-mcpindex-r6-bd-merge-retire.json`.
6. Publish or apply per the signed plan: `safe-apply` only, never bare `terraform apply`. For an SSM document, the new
   version is set DEFAULT and Default == Latest is read back.
7. Read back s16.AC1 and s16.AC2. The acceptance is the next scheduled `bd-silver-merge` run and the next weekday
   trigger slot, read as Success on the retired path's absence. Close the ledger.
   - Roll back on any failed leg. Never half-landed.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-01 ~10:0xZ) -- rules PHASE A row Z-W24-S2 (BLOCKING, ARMED): diagnose before
the halves.**
- PHASE A (worker ~24 @a8db7f31bf) found that on days with no `bronze/.../_BRONZE_COMPLETE.json` sentinel, the
  documents are the ONLY same-day silver writer for transactions and realized. `bd-silver-merge` writes them about 26h
  later (e.g. REALIZED_DAILY_2026-09-21: document 21:46Z on 09-21, merge 09-23 00:07Z, same 9,330 rows). Retiring them
  as planned would move served silver freshness on those days.
- **Ruling:** no halves are asked until the sentinel gap has a cause. **PHASE A continuation, read-only:**
  1. For every date in the census window, list whether the sentinel exists, which producer writes it (read the
     producer's code and its logs: the bd-49f runner chain, `bd-49f-session-daily` 00:00Z ->
     `bd-49f-session-trigger` -> `bd-49f-runner`), and why it is absent on the gap dates. Name the cause from the
     producer's own logs or code, never from the date pattern alone.
  2. Re-plan per key. Unrealized (after the DS deploy leg) and allocations do not depend on the sentinel, and their
     plan stands. For transactions and realized, the plan is one of:
     - (a) retire with the producer fix named, as its own leg or carried;
     - (b) HOLD those two keys this round, with the cause carried to L10;
     - (c) retire, accepting the lag, with the measured lag distribution printed.
     Recommend one, with its served-freshness consequence stated.
  3. Re-issue `ANNOUNCE_MX-s-16.md` with the diagnosis, and report.
- **Grading:** s16.AC1 stays as written (4 of 4). If the ruled plan holds transactions and realized, AC1 is REFUSED as
  written for those two tables with its measurement, and they are carried to the round-6 slug; the order closes on its
  other keys only by an issuer ruling recorded here.
- Graded by: no gate limb graded this modification (LIMB 6 grades only a newly-added order; GATE (viii) finds
  `<placeholders>NONE</placeholders>`).

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-10-01 ~10:2xZ) -- the per-key ruling on PHASE A-A1 (worker ~24 @b9d1a9577c; rows
Z-W24-S2, S4, S5).**
- **Cause, as measured:**
  - On 9 of 9 sentinel-less dates in 09-03..10-01, the first transactions pull's sidecar reads `has_data_rows=0`.
    Black Diamond posts transactions about 2 days late, so Monday and Tuesday runs return an empty window.
  - The sentinel writer (`emit_bronze_sentinel`, called by `bd-49f-runner`) correctly withholds the sentinel, so
    `bd-silver-merge` never fires that day.
- **Per key:**
  - **unrealized -- GO (after the DS deploy leg).** The empty-stub fix to
    `data/black_diamond/scripts/silver/merge-daily-incremental.py` is deployed to its served key FIRST, through
    `.tools/safe-deploy.sh` (rule 13). If safe-deploy refuses the worker serial (the DS lane), file a BLOCKING row
    naming the refusal and STOP that key. The issuer routes the leg to a DS seat.
  - **allocations -- GO.** No-op document version, trigger rule disabled, and the `ProcessAllocationFiles` notification
    removed. Coverage is proven 131/131.
  - **transactions -- GO, option (c), on one precondition.** PHASE B's first leg is a read-only consumer trace of
    `s3://opal-data-bd/silver/transactions/<date>.parquet` same-day existence: the gold/served readers and any freshness
    check (`comp-freshness`, the bd gold chain). If any consumer keys on a same-day partition existing, file a BLOCKING
    row and HOLD transactions. Otherwise retire. Served content is unchanged: on gap days the document writes only an
    empty 34,882 B placeholder.
  - **realized -- HOLD this round.** The document is the only same-day real-rows writer on 9 of 9 gap dates. Retiring
    it adds +26.5h every Monday and +2.5h every Tuesday (n=9, median 48.1h vs 3.3 min). The sentinel fix (option (a):
    accept a measured `has_data_rows=0` for the transactions table only) lives in the shared `data/cot` ingest script,
    outside this order and across a firm line, and is carried to the round-6 slug.
- **Grading:** s16.AC1 is REFUSED as written for realized (2 writers by design this round); the other 3 tables must read
  1. The order closes on unrealized, allocations and transactions by this ruling. s16.AC2 and AC3 as written.
- **Before the halves:** re-cut the saved targeted plan WITHOUT `bd-realized-pipeline-trigger` (expect
  0 to add / 4 to change / 0 to destroy: 3 rules + the notification), re-issue the ANNOUNCE with the per-key plan,
  rollback per key, and the consumer-trace leg, then report. PHASE B runs only on the issuer's GO after both halves.
- Rows Z-W24-S4 and S5 (the runner prints "OK: bronze sentinel emitted" after the module said "NOT emitted") are carried
  to the slug with the realized hold.
- Graded by: no gate limb graded this modification.

**AMENDED A3 (2.0.0_SA_COO~MI, 2026-10-02 ~00:3xZ) -- AC1 graded on the keys A2 retired; the acceptance is met.**
- A2 ruled transactions and realized HELD, and the PHASE B consumer trace held transactions (Z-W24-S8). So the original
  4-of-4 AC1 cannot pass BY DESIGN.
- AC1's invocation now names the graded tables (`s16.AC1.sh unrealized allocations`). The script still prints all 4
  (the denominator), and the unscoped call still FAILs 2 of 4 as the control.
- **Acceptance:** the SCHEDULED `bd-silver-merge` run, invoked 2026-10-02T00:11:36Z, read unrealized
  `failures=0 empty_stub=6`. Z-S72 is disarmed by the deployed fix. Transactions, realized and allocations were clean.
- Ledger `nfra-mcpindex-r6-bd-merge-retire` CLOSED 8/8 at the issuer's read.
- The order completes on unrealized and allocations. Transactions and realized are carried to the round-6 slug
  (REMEDIATION_v5; the cot sentinel fix).
- Graded by: no gate limb graded this modification (LIMB 6 grades only a newly-added order; GATE (viii) finds
  `<placeholders>NONE</placeholders>`).

## 2. BOUNDS

1. One producer per table after the change: no second schedule, no parallel path, no comparator (the NEVER shadow
   rule).
2. Served silver must not lose a partition or a row it has today. A non-zero DELTA beyond the unrealized diagnosis is a
   BLOCKING row.
3. Nothing under `data/cot/`. 49F only. No push. REFUSE a criterion you cannot meet as written, and report it with its
   measurement.

## 3. SURFACES

<paths>
infra/aws/ssm/opal-bd-transaction-download.json
infra/aws/ssm/opal-bd-realized-download.json
infra/aws/ssm/opal-bd-unrealized-download.json
infra/aws/ssm/opal-bd-allocation-download.json
infra/aws/terraform/bd-pipeline/
data/black_diamond/scripts/silver/merge-daily-incremental.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r6-bd-merge-retire.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~24/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W24-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-s-16" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/checks/s16.AC1.sh unrealized allocations; echo "exit=$?"</invocation><expect>OK: unrealized 1 writer; OK: allocations 1 writer; transactions and realized printed NOT GRADED (A2 HOLD); graded 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-16" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/checks/s16.AC2.sh; echo "exit=$?"</invocation><expect>graded tables with a clean newest run: 3 of 3 (control; unrealized printed, graded by the Z-S72 diagnosis) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-s-16" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/checks/s16.AC3.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~24/NFRA_MCPINDEX.TO-MX-s-16.bd-merge-path-one-writer.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

PHASE A ends at the ANNOUNCE: report and stop. After PHASE B, write the proof instance at the `<instance_path>` and
report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-6 item 7. Battery dry-run at base:
- s16.AC1 FAIL as expected (0 of 4 tables with 1 writer; allocations 3);
- s16.AC2 PASS as expected (control: transactions, realized and allocations clean; unrealized failures=6 printed,
  row Z-S72);
- s16.AC3 FAIL as expected (no entry).

<status>complete</status> <!-- A3: AC1 graded on unrealized+allocations; acceptance run bd-silver-merge 2026-10-02T00:11:36Z unrealized failures=0 empty_stub=6; ledger CLOSED 8/8 -->
<round>6</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
