# TO IRPT_ANLREQ.TO-AR-y-36 -- the ycharts/generate test suite stops depending on test order

<to_id>IRPT_ANLREQ.TO-AR-y-36</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~54</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (test files only) The class is WORLD because the L6 gate's floor for an `infra/` path is WORLD; the cell itself builds, uploads and applies nothing. | **Decomp cell:** `AR-y-36`
(`decompositions/IRPT_ANLREQ_DECOMP_R3_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~54`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-54` (branch `wk-IRPT_ANLREQ-54`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~54 <0.9.0_WK_IRPT_ANLREQ~54@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. Run tests with invalid AWS keys (`AWS_ACCESS_KEY_ID=x AWS_SECRET_ACCESS_KEY=y`).
- `GT` below is `infra/aws/lambda/investor-reporting/ycharts/generate/tests`. `surfaced_at` of any row = `date -u +%FT%TZ` at filing.

### THE CELL (`AR-y-36`, inlined)

*The `ycharts/generate` test suite stops depending on test order: the 34 custody tests pass inside the full run.*

**What is measured** (row `IRPT_ANLREQ-D2-S31`, on this box, Python 3.14.7): `python -m pytest GT -q` ends 2 failed, 32 errors, 461 passed.
All 34 are in `GT/test_custody_entry.py` (2 failed) and `GT/test_custody_retained.py` (32 errors, `KeyError: 'data'`). The same two files
run ALONE pass 42 of 42 (2 skipped). The base fails the same 34 with or without any release's change. Which earlier test leaves the state
is NOT established; finding it is the first half of this cell.

**THE FULL SUITE TAKES MINUTES. Every command you run is bounded at 120 seconds, so never run the whole folder in one command.** Work by
bisection over FILES: run `python -m pytest -q -p no:cacheprovider <some files> GT/test_custody_retained.py` with fewer and fewer files
ahead of the custody file until the smallest sequence that still fails is left.

**Build:**
1. **Find the polluter.** The minimal ordered list of test files, ending with the custody file(s), that reproduces the failure. Name what
   state leaks (a module left in `sys.modules`, a patched attribute not restored, an environment variable, a `sys.path` entry, a
   module-level cache) with file and line.
2. **Record it** in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/S31_REPRODUCER.json`:
   `{"files": ["<polluter file name>", ..., "test_custody_retained.py"], "fails_at_base": true, "base_commit": "<the commit you ran it
   at>", "base_tail": "<the last line pytest printed at the base>", "leak": "<what leaks, file:line>"}`. `files` are names inside `GT`,
   in run order. `fails_at_base` is true only if you ran that exact sequence at the base and it failed.
3. **Fix it in the TESTS.** The leak is closed where it is made (the polluting test restores what it changed: a fixture with teardown, a
   `monkeypatch`, a context manager) or, if the polluter is a legitimate module-level import, the custody tests stop assuming a clean
   interpreter. Do not weaken, skip, reorder or mark any test, and do not add `pytest-randomly`, `xdist` or a `conftest.py` hook that
   resets the interpreter between files.
4. **If the leak is in PRODUCT code** (a module under `ycharts/generate/` that is not a test keeps state between calls in a way a real
   Lambda invocation could also hit), STOP after step 2: file ONE BLOCKING row with the file and line and what a second invocation in a
   warm container would see. Product files are not in your grant.

### ACCEPTANCE

<criterion id="AR36-y-AC1" cell_refs="AR-y-36"><invocation>python C:/dev/wk-irpt-anlreq-54/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y36-order --root C:/dev/wk-irpt-anlreq-54</invocation><expect>Y36-ORDER-OK</expect></criterion>
`AR36-y-AC1`: the reproducer you recorded (the polluter, then the custody file) exists, records that it failed at the base, and now runs
green. The control is inside the criterion: the same sequence, at the base commit, failed.

<expected_criteria>AR36-y-AC1</expected_criteria>

The issuer runs the WHOLE folder, unbounded, twice at the drain and compares the failing SET of the two runs with each other and with the
base's 34. A suite that is green in your reproducer and still fails in the full run comes back to you.

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/` and this order's
  file (status flip only).
- READ only: everything else under `infra/aws/lambda/investor-reporting/`.
- No live act: never push, never deploy, never call a live API. No non-ASCII. Synthetic test data only.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/tests/
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R3_Y.md</decomp_doc> (round 3, workstream Y), cell `AR-y-36`.
<owned_cells>AR-y-36</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR36-y-AC1. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/IRPT_ANLREQ.TO-AR-y-36.generate-suite-order-independence.proof_of_spec.json`.
Validate it AFTER its commit with `python .tools/proof-of-spec-check.py <instance> AR36-y-AC1`.
</proof_of_spec>

**REPORT (once):** the check line verbatim; the commit; the polluter, what leaks and where; every test file you changed and what the
change restores; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- test files only; no product member, no zip. comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE. comp-adversary: RUN -- AR36-y-AC1 base FAIL as expected (no reproducer file); BLIND: the full-suite numbers on the face are 2.0.0_SA_COO~G2's measurement in row IRPT_ANLREQ-D2-S31, not re-run by the issuer, and the full run is the issuer's drain check because it does not fit a worker's 120 s bound.
lane: the generate suite's files are workstream Y's (CTO round-3 analysis section 4; row D2-S31 notes).
</preflight>

Source: CTO round-3 analysis @430d79e86d section 4, the D2-S31 line ("fixed in this workstream when a slot is free; it gates no release,
since releases are graded by failing SET"); row IRPT_ANLREQ-D2-S31 (2.0.0_SA_COO~G2). A slot is free: the round has four worker chains
under a cap of eight.
