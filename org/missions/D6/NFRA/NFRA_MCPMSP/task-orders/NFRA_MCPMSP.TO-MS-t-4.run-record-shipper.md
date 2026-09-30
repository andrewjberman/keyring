# NFRA_MCPMSP task order -- `MS-t-4` -- ROUND 1, hop 4 record: the operator-side run-record shipper (minimum)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-t-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~4</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- run by the operator per run; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell's criteria run on fixtures; the put runs under the operator's own credentials at the close run.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-t-4` (decomposition section 2)

Every partner run must be replayable from Opal's side, tagged with firm, advisor and run (PRD C9; FWD-5's minimum).
The agent account cannot write the repo or the record, so the record is shipped by the OPERATOR side.

Build `opal_ai/opal/runtime-msp/record/ship-run.py` (new, stdlib + boto3 only), run by the operator for ONE run:
- inputs: `--firm`, `--advisor-oid`, `--run-id`, `--from`/`--to` (ISO-8601 UTC window), `--transcript <path>` (the
  `Opal_MSP` session's JSONL transcript), `--calling-email` (the Opal Analyst user the gateway saw as the caller),
  `--audit-source <local jsonl path or s3 prefix>` (the gateway's audit records; the lake's key shape is
  `audit/dt=<YYYY-MM-DD>/<ts>-<hex>.jsonl`, see `infra/aws/ec2/opal-gateway/app/audit.py` `_emit`);
- it keeps ONLY the audit rows inside the window AND whose `user` is the calling identity;
- it writes, under the builder's address `address('gateway', <firm>, 'bronze', 'msp_runs', <run date>)` -- measured at
  the cut as `s3://opal-data-assets/gateway/<firm>/bronze/msp_runs/<YYYY-MM-DD>` -- the objects
  `<run_id>/transcript.jsonl`, `<run_id>/audit.jsonl` and `<run_id>/manifest.json` (`{firm, advisor_oid, run_id,
  window, calling_email, counts}`). Compute the address by importing `lib/opal_naming.py` from the workspace root
  (path passed as `--workspace`), never a typed bucket;
- DRY RUN by default (prints the planned keys and counts, writes nothing); `--write` performs the puts.
- `record/test_ship_run.py` with at least: `test_dry_run_writes_nothing`, `test_keys_under_builder_address`,
  `test_audit_rows_filtered_to_window_and_identity`, `test_record_tagged_firm_advisor_run` -- all on local fixtures
  with a fake S3 client.

## 2. BOUNDS

1. Write surface: `opal_ai/opal/runtime-msp/record/**` only. No put against AWS in this order.
2. Commit in the nested `opal_ai` repo on your branch; no push. REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
opal_ai/opal/runtime-msp/record/ship-run.py
opal_ai/opal/runtime-msp/record/test_ship_run.py
opal_ai/opal/runtime-msp/record/fixtures/
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~4/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `lib/opal_naming.py`, `infra/aws/ec2/opal-gateway/app/audit.py`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W4-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your parent worktree root after your nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-t-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/t4.AC1.sh; echo "exit=$?"</invocation><expect>pytest: N passed; test_dry_run_writes_nothing=1 test_keys_under_builder_address=1 test_audit_rows_filtered_to_window_and_identity=1 test_record_tagged_firm_advisor_run=1 (each >=1, 0 failed) -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~4/NFRA_MCPMSP.TO-MS-t-4.run-record-shipper.proof_of_spec.json`.
Report once, with: the operator's exact invocation for one run; the check line; the nested and parent commit hashes;
any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 issuance (CTO msg 26985). Check dry-run at base: AC1 FAIL as expected (test file absent).
One criterion: the seam (a real put) is the close run's, under the operator's credentials; a second fixture check
would add nothing the named tests do not.

<status>staged</status>
<round>1</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
