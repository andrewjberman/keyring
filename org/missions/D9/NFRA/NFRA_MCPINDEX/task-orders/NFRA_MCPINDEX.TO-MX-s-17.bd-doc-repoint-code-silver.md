# NFRA_MCPINDEX task order -- `MX-s-17` -- disarm first: point the two HELD Black Diamond documents' merge step at `code/silver/`, the script bd-silver-merge runs

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-17</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~24</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at PHASE A by the worker -- bd-realized-pipeline-trigger 21:45Z and bd-transaction-pipeline-trigger 21:53Z (weekdays) dispatch the two documents; no publish inside 21:30-22:15Z.
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy change; two SSM document versions only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a code-path repoint under never-widen halves (CTO + COO); served DELTA stated in the ANNOUNCE.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `MX-s-17` (round 7; `ROUND_ANALYSIS.round6.md` @361b186c92 section 3b row Z-W24-S3, section 5 item 1(a))

**The CTO's ruling (Z-W24-S3):** the realized and transactions documents still run `scripts/merge-daily-incremental.py`,
so two code versions write each of those tables. Disarm FIRST, before the sentinel fix: point both documents' merge
step at `code/silver/`, the script `bd-silver-merge` runs. Disarm read: both documents' Default content names no
`scripts/` path.

**Where the stale paths are, measured at the round-7 base:**
- `infra/aws/ssm/opal-bd-transaction-download.json:27` -- `aws s3 cp s3://opal-data-bd/scripts/merge-daily-incremental.py`
  (and the run line near :29).
- `infra/aws/ssm/opal-bd-realized-download.json:30` (the same cp), `:31`
  (`aws s3 sync s3://opal-data-bd/scripts/lib/ lib/` -- repoint to `code/silver/lib/`) and `:33`.
- `bd-silver-merge` (`infra/aws/lambda/bd-pipeline/bd-silver-merge/lambda_function.py`) runs
  `s3://opal-data-bd/code/silver/merge-daily-incremental.py`.
- The two documents are published with `aws ssm update-document` (they are not Terraform-managed); the new version is
  set DEFAULT and Default == Latest is read back.
- `force-alloc-download.json:17` and `force-txn-download.json:17` also name `scripts/`. They are NOT in this cell: list
  them in the ANNOUNCE as a census line only.

### PHASE A -- no publish
1. Diff the served `scripts/merge-daily-incremental.py` (and `scripts/lib/`) against `code/silver/merge-daily-incremental.py`
   (and `code/silver/lib/`): `aws s3 cp` both to a scratch dir, `diff`. Confirm `code/silver/lib/` exists with every
   module the script imports.
2. State the expected served DELTA on `silver/transactions/` and `silver/realized/` when the documents run the
   `code/silver` script (0 if the scripts are equivalent on these tables; otherwise the difference, named per table).
3. Write `ANNOUNCE_MX-s-17.md` in your deliverables: the diff, the edited document JSON for both, the DELTA, and the
   rollback per document (re-set the prior version DEFAULT, with its version number read). Report and STOP. The
   issuer takes it to the never-widen halves.

### PHASE B -- only on the issuer's GO
4. Open the NEVER-2 ledger `nfra-mcpindex-r7-bd-doc-repoint`, naming BOTH paths when committing: the entry under
   `org/critical_paths/change_management/` AND the sentinel
   `org/critical_paths/.open_deploys/nfra-mcpindex-r7-bd-doc-repoint.json`.
5. Publish both documents, set DEFAULT, read Default == Latest back, run s17.AC1, close the ledger. Roll back on any
   failed leg; never half-landed.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-06 ~18:3xZ) -- disarm row Z-W24-S9 before the publish.**
- Between steps 4 and 5: on the instance the documents target, run ONE read-only SSM command,
  `python3 -c "import boto3, pandas; print('OK:', boto3.__version__, pandas.__version__)"`, from the documents' working
  directory, and quote its output. `OK:` disarms Z-W24-S9 (cite this amendment). An ImportError is a BLOCKING row:
  publish nothing, close the ledger as not-applied, report.
- Publish window: outside 21:30-22:15Z (the two document crons, 21:45Z and 21:53Z).
- Base pins re-read by the issuer at 2026-10-06T18:29Z: both documents Default 3 = Latest 3, Active, which equals the
  ANNOUNCE's rollback version. `code/silver/merge-daily-incremental.py` ETag `91eaf248...`, 59,820 B. If either differs
  at your first act, stop and report.
- Graded by: no gate limb graded this modification.

## 2. BOUNDS

1. One producer per table after the round: no second schedule, no parallel path, no comparator.
2. Nothing under `data/cot/`. No push. Never `aws lambda update-function-code`; never bare `terraform apply`.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ssm/opal-bd-transaction-download.json
infra/aws/ssm/opal-bd-realized-download.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r7-bd-doc-repoint.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~24/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W24-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-s-17" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/s17.AC1.sh; echo "exit=$?"</invocation><expect>documents repointed 4 of 4 (2 documents x DEFAULT,LATEST; code/silver refs>=1, scripts/ refs=0 each) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-17" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/s17.AC2.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~24/NFRA_MCPINDEX.TO-MX-s-17.bd-doc-repoint-code-silver.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

PHASE A ends at the ANNOUNCE: report and stop. After PHASE B, write the proof instance at the `<instance_path>` and
report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-7 item 1(a). AC2 is the NEVER-2 ledger criterion of a WORLD act. Battery
dry-run at base: s17.AC1 FAIL as expected (0 of 4; transaction scripts/ refs=1, realized scripts/ refs=2); s17.AC2
FAIL as expected (no entry).

<status>issued</status>
<round>7</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
