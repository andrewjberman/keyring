# NFRA_MCPMSP task order -- `MS-rn-1` -- ROUND 2, E4: one supervised Opal_MSP run, shipped to the lake

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-rn-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~6</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- puts under the builder address with the operator's existing credentials.
comp-adversary: DECLARED-NOT-APPLICABLE -- MS-rx-1 (a second seat) is the adversary read of this record.
EGRESS CLASS, declared: none (Opal's own S3).
</preflight>

## 1. THE CELL -- `MS-rn-1` (decomposition v2, R2.2; PRD C9, FWD-5)

An Opal operator (Andrew) has put ONE question to the supervised `Opal_MSP` session (opal_ai DEV checkout at
`C:\opal_runtime_msp\opal_ai`, launched with the operator recipe) and exported its transcript. This order's AMENDMENT
(issuer) names: the transcript path, the run window (`--from`/`--to`, ISO UTC), the calling email (the MSP calling
identity), the operator's oid, and the run id. Firm for an operator rehearsal is `global` (address
`s3://opal-data-assets/gateway/global/bronze/msp_runs/<date>`, builder output).

1. Dry run first: `python opal_ai/opal/runtime-msp/record/ship-run.py --firm global --advisor-oid <oid> --run-id <id>
   --from <t0> --to <t1> --transcript <path> --calling-email <email> --audit-source s3://opal-mcp-audit/<prefix>
   --workspace <your worktree root>` -- read what it would write (three objects).
2. Then the same with `--write`.
3. Write `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~6/r2_e4r_run.json` = `{"firm": "global",
   "run_id": "<id>", "date": "<YYYY-MM-DD of the address>"}`.
If the amendment is absent, the transcript path does not exist, or the dry run fails, STOP with a BLOCKING row.

## 2. BOUNDS

1. S3 writes ONLY under the builder address for this run id. No transcript content in the repo (the record lives in
   the lake). No push, no vendor call. REFUSE a criterion you cannot meet.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~6/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `opal_ai/opal/runtime-msp/record/ship-run.py`, `lib/opal_naming.py`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W6-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-rn-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e4r.AC1.sh; echo "exit=$?"</invocation><expect>record base=s3://opal-data-assets/gateway/global/bronze/msp_runs/DATE/RUN_ID; objects=3/3 manifest_firm=global run_id_match=True user_turns>=1 verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~6/NFRA_MCPMSP.TO-MS-rn-1.one-replayable-run.proof_of_spec.json`.
Report once, with: the dry-run and write lines; the three object keys; the check line; the commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** HELD on G-MSPID (the MSP calling identity; CTO 27416 asks Andrew) and G-MSPCL (Claude installed and
signed in under `Opal_MSP` as that identity; Andrew's MFA act), then Andrew's one question. The issuer amends this order
with the run's facts before handing it to slot `~6`. Checks dry-run at base: AC1 FAIL as expected (no run file).

<status>staged</status>
<round>2</round>
<slot>~6</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
