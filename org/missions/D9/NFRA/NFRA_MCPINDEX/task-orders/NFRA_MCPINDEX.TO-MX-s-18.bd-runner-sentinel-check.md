# NFRA_MCPINDEX task order -- `MX-s-18` -- the BD runner's own sentinel check: a measured empty transactions window completes the day, and "OK" follows a read-back

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-18</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~24</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at PHASE A by the worker -- bd-49f-session-daily 00:00Z -> bd-49f-session-trigger -> bd-49f-runner; no apply inside 23:45-00:45Z.
comp-iam: DECLARED-NOT-APPLICABLE -- the runner's role already reads and writes s3://opal-data-bd/bronze/ (it writes the sentinel today); a head_object on a key it writes needs no new grant. A refusal at the read-back is a BLOCKING row, never a policy edit.
comp-adversary: DECLARED-NOT-APPLICABLE -- a sentinel-predicate change under never-widen halves (CTO + COO); its served effect (bd-silver-merge fires on Mon/Tue) is stated in the ANNOUNCE.
EGRESS CLASS, declared: NONE beyond Opal's own AWS. The runner's Black Diamond pull is NOT invoked by you: no ad-hoc runner invocation.
</preflight>

## 1. THE CELL -- `MX-s-18` (round 7; `ROUND_ANALYSIS.round6.md` @361b186c92 section 3a row Z-W24-S4, section 5 item 1(b); rows Z-W24-S4, Z-W24-S5)

**The CTO's ruling (Z-W24-S4):** fix it in the BD runner's OWN sentinel check, never in the shared script under
`data/cot/`. For the transactions PERIOD table only, the check accepts a MEASURED `has_data_rows=0` sidecar. The runner
prints `OK: bronze sentinel emitted` only after a `head_object` on the sentinel key reads it back. Negative controls:
(i) a snapshot table with 0 rows still withholds the sentinel; (ii) `data/cot/` is byte-unchanged.

**What is measured today:**
- Black Diamond posts transactions about 2 days late, so the Monday and Tuesday runs' transactions pull reads
  `has_data_rows=0`. On 9 of 9 sentinel-less dates in 09-03..10-01 that was the cause. The sentinel is withheld, so
  `bd-silver-merge` (S3-triggered on `bronze/<date>/_BRONZE_COMPLETE.json`) never fires that day.
- The runner, `infra/aws/lambda/bd-pipeline/bd-49f-runner/lambda_function.py`:
  - `:59-60`, `:71-78` download `s3://opal-data-bd/code/bronze/cot_bronze_ingest.py` at runtime and import it;
  - `:204` `if not failed and landed:`, `:206` `mod.emit_bronze_sentinel(run_date, landed)`, `:207` prints
    `OK: bronze sentinel emitted` whenever no exception was raised -- even when the module printed
    `WARN: bronze sentinel NOT emitted` (Z-W24-S5);
  - `_already_landed` at `:87-102`.
- The shared module `data/cot/scripts/bronze/cot_bronze_ingest.py` (READ-ONLY to you): `emit_bronze_sentinel` at
  `:1328`; `_table_complete` at `:632-670` ends `return int(meta.get("has_data_rows",0))==1`; the sidecar is
  `forwardfill_v2/{table}/_complete/{date}.json` with `has_data_rows` 1 / 0 / -1; `SNAPSHOT_TABLES` at `:147`; the
  PERIOD tables are transactions and realized.
- The runner is deployed as a zip through Terraform: `infra/aws/terraform/bd-pipeline/bd-49f-interim.tf:276-332`
  (module `bd_49f_runner`, artifact `bd-pipeline/bd-49f-runner.zip`). A runner change is a zip build + `safe-apply`.
  Never `aws lambda update-function-code`.

**The fix, in the runner only:**
- The runner decides completeness itself: every table in `landed` complete, where complete means sidecar
  `has_data_rows==1`, OR (table == transactions AND the sidecar exists AND reads a measured `has_data_rows==0`). A
  missing sidecar or `-1` is never complete. Any snapshot table at 0 rows withholds.
- When complete, the runner writes the sentinel (the same key and body shape `emit_bronze_sentinel` writes -- read it
  from the module's code and reproduce it; a body field that differs is a BLOCKING row), then `head_object`s the key,
  and prints `OK: bronze sentinel emitted` only on that read. A failed read prints `ERROR:` and fails the invocation.
- When not complete, it prints `WARN:` naming the incomplete tables, and never `OK`.
- Tests: new `infra/aws/lambda/bd-pipeline/bd-49f-runner/tests/test_runner_sentinel.py`, offline (stub S3), with these
  exact test names: `test_period_empty_window_emits_sentinel`, `test_snapshot_zero_rows_withholds`,
  `test_ok_line_only_after_head_object_readback`.

**The hazard you also disarm (issuer-found, this cell):** `infra/aws/ec2/bd-gold-layer-runner/deploy-to-ec2.sh:43,75-85`
runs `aws s3 sync --delete data/black_diamond/scripts/bronze/ s3://opal-data-bd/code/bronze/`. The runner's engine
`code/bronze/cot_bronze_ingest.py` is not in that source dir, so the next gold-runner deploy deletes it. Add an
`--exclude 'cot_bronze_ingest.py'` to the bronze sync (an excluded key is never deleted at the destination). Do not
run the deploy script.

### PHASE A -- no apply
1. Build the zip, run the tests, and cut a saved targeted plan for the runner module only.
2. Write `ANNOUNCE_MX-s-18.md`: the diff, the test output, the saved plan (any destroy is a BLOCKING row), the served
   effect (bd-silver-merge fires on empty-transactions days; name what it writes on such a day, read from its code),
   and the rollback (the prior zip's S3 version id, read). Report and STOP.

### PHASE B -- only on the issuer's GO
3. Open the NEVER-2 ledger `nfra-mcpindex-r7-bd-runner-sentinel`, naming BOTH the entry under
   `org/critical_paths/change_management/` AND `org/critical_paths/.open_deploys/nfra-mcpindex-r7-bd-runner-sentinel.json`.
4. Upload the artifact, `safe-apply` the saved plan, read the deployed `CodeSha256` against your built zip, close the
   ledger. The first live exercise is the scheduled 00:00Z run; report its log line (OK after read-back, or WARN
   naming tables).

## 2. BOUNDS

1. Nothing under `data/cot/` changes (AC2 is that control). No ad-hoc runner invocation (it pulls from Black Diamond).
2. No push. Never bare `terraform apply`; never `update-function-code`.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/lambda/bd-pipeline/bd-49f-runner/
infra/aws/terraform/bd-pipeline/bd-49f-interim.tf
infra/aws/ec2/bd-gold-layer-runner/deploy-to-ec2.sh
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r7-bd-runner-sentinel.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~24/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W24-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3,AC4</expected_criteria>
  <criterion id="AC1" cell_refs="MX-s-18" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/s18.AC1.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 3 of 3 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-18" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/s18.AC2.sh; echo "exit=$?"</invocation><expect>data/cot/ files changed since the issuance base: 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-s-18" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/s18.AC3.sh; echo "exit=$?"</invocation><expect>to code/bronze=1; deleting without excluding cot_bronze_ingest.py=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="MX-s-18" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/s18.AC4.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/NFRA_MCPINDEX.TO-MX-s-18.bd-runner-sentinel-check.proof_of_spec.json</instance_path>
</proof_of_spec>

Fourth criterion, reason: AC4 is the NEVER-2 ledger of the runner deploy; AC2 is the CTO's named negative control and
AC3 disarms a hazard that would delete this cell's engine.

## 5. WHEN YOU ARE DONE

PHASE A ends at the ANNOUNCE: report and stop. After PHASE B, write the proof instance at the `<instance_path>` and
report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-7 item 1(b) with criteria (i)-(iii). The `--delete` hazard was found in the
round-7 fact read and folded here because it deletes this cell's engine. Battery dry-run at base: s18.AC1 FAIL as
expected (test file absent); s18.AC2 PASS as expected (control, 0 files); s18.AC3 FAIL as expected (1 code/bronze
sync deleting unprotected; a fixed-copy control reads 0 and rc=0); s18.AC4 FAIL as expected (no entry).

- **ISSUER GRADE (2.0.0_SA_COO~MI, 2026-10-08 ~22:4xZ):** the assignee seat is dark after the site Z reboot, so the
  issuer closed ledger leg V1 and graded. V1: the 2026-10-08 00:00Z scheduled run printed `OK: bronze sentinel emitted
  for 2026-10-08` after the read-back; head-object reads the key at 00:11:37Z, 277 B. Ledger CLOSED @f2422adb7f, 6 of 6
  legs. s18.AC1-AC4 re-run in `wk-nfra_mcpindex-r7-24`: 4 of 4 PASS. Mutant (OK printed before head_object): AC1 reads
  2 of 3, FAIL; restored, PASS. Proof instance VALID (rc=0). All four criteria are mechanical; none waits on L9.
  The instance sits at `deliverables/2.0.0_SA_COO~MI/NFRA_MCPINDEX.TO-MX-s-18.bd-runner-sentinel-check.proof_of_spec.json`,
  not at `<instance_path>`: owned-paths refuses the issuer a write under the worker's serial folder.

<status>complete</status>
<round>7</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
