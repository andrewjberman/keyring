# NFRA_MCPINDEX task order -- `MX-x-6` -- the round-9 batch repair: the emitter refuses a foreign census dir, and the gateway suite is graded by failing-ID delta

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-x-6</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-x-6</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~32</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- repo code and test records only; no AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- the battery dry-run is the control (x6.AC1 0 of 2 named tests and x6.AC2 tool absent at base).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-x-6` (round 9; `ledger/ROUND_ANALYSIS.round8.md` section 4 item E3; decomposition section ROUND 9)

Two repairs, one cell.

**Repair 1 -- the emitter's census input (row Z-W29-S1).** `workflows/atom_decomposition/emit_catalog_v02.py`
already defaults `--census-dir` to `CENSUS_DIR`, a path inside the checkout it runs from (`:492`). In round 8, an order
told the worker to pass the MAIN tree's census dir from a linked worktree. The emitter accepted it and rewrote every
`census_ref` from a foreign tree. The fix: `main()` REFUSES a `--census-dir` that is not inside `REPO_ROOT` (`:493`,
the checkout the emitter runs from). It prints `EMIT REFUSED (census input): ... outside this checkout ... NOTHING
WRITTEN` and returns 2, before anything is read or written, in the same place and style as the existing refusal at
`:651-653`.
- Compare resolved real paths, so a `..` or a symlink cannot escape.
- The default still works.
- Add two tests to `workflows/atom_decomposition/tests/test_emit_declared_inputs.py`, following that file's existing
  tests and fixtures:
  - `test_census_dir_outside_checkout_refused`: a temp dir outside the checkout gets rc 2, the refusal text, and the
    output catalog's bytes unchanged.
  - `test_census_dir_default_is_this_checkout`: the parsed default resolves inside `REPO_ROOT`.

**Repair 2 -- the gateway suite baseline (rows Z-S88, Z-W28-S8).** The gateway suite under
`infra/aws/ec2/opal-gateway/tests/` is red on the base: 34-38 failures, order-dependent, and a different count on a
sparse tree than on a full one. Drains have graded it by COUNT, which hides a new failure behind a fixed one. Build:
- `infra/aws/ec2/opal-gateway/tests/baseline/failing_ids_full.txt` and `failing_ids_sparse.txt`: one pytest node ID
  per line, sorted, for each tree shape, from a run you make. Your worktree is one shape. Make the other with
  `git worktree add` of the same commit (full checkout, or a sparse cone over `infra/aws/ec2/opal-gateway/` and
  `.tools/`) under your scratch, run there, and remove it. Each file's first line is a `#` header: commit, shape, the
  pytest command, the passed/failed/error counts.
- `infra/aws/ec2/opal-gateway/tests/suite_delta.py` (stdlib only):
  - `--report <pytest -rA output file> --shape full|sparse` prints `NEW <id>` for each failing ID not in that
    shape's baseline, `FIXED <id>` for each baseline ID now passing, and a summary `new N fixed M baseline B`; it
    exits 1 when N > 0.
  - `--self-test` replays each baseline as a report (expect new 0) and a baseline plus one planted ID (expect new 1,
    naming it), prints both baseline sizes, and ends with the line `SELF-TEST PASS`.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT fix any failing gateway test: the baseline records them; their
   owners fix them.
2. No AWS, no deploy, no push. No other emitter behaviour changes.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/tests/test_emit_declared_inputs.py
infra/aws/ec2/opal-gateway/tests/suite_delta.py
infra/aws/ec2/opal-gateway/tests/baseline/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~32/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W32-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` = `date -u +%FT%TZ` at filing, never a placeholder.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-x-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round9/checks/x6.AC1.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 2 of 2; failed/error tests 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-x-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round9/checks/x6.AC2.sh; echo "exit=$?"</invocation><expect>SELF-TEST PASS (replay new 0, planted new 1, both baseline sizes printed) -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~32/NFRA_MCPINDEX.TO-MX-x-6.emitter-census-dir-and-suite-baseline.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`, then flip `<status>` to complete and commit the instance,
deliverables and flip together. Report once: both baseline sizes per shape, and the failing IDs grouped by test file
(the issuer forwards the schwab and grant families to their owner).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 9, chain [MX-x-6 -> MX-c-7]: c-7 runs the emitter this cell fixes. E3 of
`ROUND_ANALYSIS.round8.md` @d2eb6c471b. Battery dry-run at the issuance base, recorded in the issuance commit.

ISSUED 2026-10-10 ~23:4xZ in round 9's ONE issuance, from `ledger/ROUND_ANALYSIS.round8.md` @d2eb6c471b. Battery re-dry-run at issuance base bf8492f48f: every check of this order FAILS there as a build check must.

<status>issued</status>
<round>9</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
