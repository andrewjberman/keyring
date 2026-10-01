# NFRA_MCPMSP task order -- `MS-rx-1` -- ROUND 2, E4: a second seat reconstructs the run from the record alone

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-rx-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~8</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads with existing access.
comp-adversary: DECLARED-NOT-APPLICABLE -- this cell IS the adversary read of MS-rn-1's record.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-rx-1` (decomposition v2, R2.2; PRD FWD-5 -- any conversation can be replayed)

You did not see the run. Its record is three objects under the builder address named by
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~6/r2_e4r_run.json` (`firm`, `run_id`, `date`):
`<address('gateway', firm, 'bronze', 'msp_runs', date)>/<run_id>/{transcript.jsonl, audit.jsonl, manifest.json}`
(`python -c "import lib.opal_naming as n; print(n.address(...))"` from the repo root; read with `aws s3 cp`).

From those three objects ALONE (no other source, no one's account of the run), write
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~8/r2_e4x_replay.md` with exactly these sections:
- `## Asked` -- the operator's question, quoted verbatim from the transcript's first user turn;
- `## Looked up` -- every gateway tool call (from audit.jsonl and the transcript's tool uses): tool, key, time;
- `## Allowed and refused` -- each call's outcome/verdict;
- `## Answered` -- what the session replied (quoted or closely summarised with its figures);
and cite the three object keys. Where the record cannot answer a section, say so in that section -- that is a finding.

## 2. BOUNDS

1. Read-only (S3 reads). No transcript content outside your deliverables. No push, no vendor call. REFUSE a criterion
   you cannot meet.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~8/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~6/r2_e4r_run.json`,
`lib/opal_naming.py`, `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/`. Rows:
`INVESTIGATION_v1.Z.md`, id `NFRA_MCPMSP-Z-W8-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-rx-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e4x.AC1.sh; echo "exit=$?"</invocation><expect>sections_nonempty=4/4 object_cites=3/3 asked_matches_record=True verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~8/NFRA_MCPMSP.TO-MS-rx-1.replay-from-record.proof_of_spec.json`.
Report once, with: the check line; anything the record could not answer; the commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** staged behind MS-rn-1 (chain F). A fresh slot `~8` so the replay is a second seat's, not the
shipper's; spawned at its dependency (cap 8 holds: 8 slots). Checks dry-run at base: AC1 FAIL as expected (no replay,
no run file).

<status>staged</status>
<round>2</round>
<slot>~8</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
