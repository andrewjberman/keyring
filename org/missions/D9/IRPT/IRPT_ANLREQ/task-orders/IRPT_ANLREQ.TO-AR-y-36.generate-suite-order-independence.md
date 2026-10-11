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

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (test files for `AR-y-36`; two product files and a test file for `AR-y-37`; nothing built, uploaded or applied) The class is WORLD because the L6 gate's floor for an `infra/` path is WORLD; the cell itself builds, uploads and applies nothing. | **Decomp cell:** `AR-y-36`
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

<expected_criteria>AR36-y-AC1 AR37-y-AC1 AR37-y-AC2</expected_criteria>

The issuer runs the WHOLE folder, unbounded, twice at the drain and compares the failing SET of the two runs with each other and with the
base's 34. A suite that is green in your reproducer and still fails in the full run comes back to you.

---

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-11 ~07:2xZ; decomposition R3_Y AMENDMENT 1): this order also owns cell `AR-y-37`.**
The cell arrived on a CTO ruling in another project's analysis (CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_8_20261011.md @fe73849335 section 2,
row IRPT_YCDGEN-D2-W8-S1; `2.0.0_SA_COO~G2` msg 4331) while the round's issuance was being cut. A separate order for it was REFUSED by
`to-pipeline-gate.py` (one issuance per round per workstream), whose stated remedy is a re-cut into the first issuance; this is that re-cut.
Gate limb that graded this amendment: read from this commit's own output.

**Do `AR-y-36` FIRST and commit it. Then `AR-y-37`, in the same worktree.** They are two separate pieces of work: the first changes
tests only; the second changes two product files and adds one test file. Report both.

`G` below is `infra/aws/lambda/investor-reporting/ycharts/generate`.

### THE CELL (`AR-y-37`, inlined)

*A NEW accepted ANALYSIS request records `acting_principal_id`, the verified submitter, passed by the submission service and never read
from the body. A request accepted before stays as it is (no rewrite); a reader that finds no actor reads ABSENT.*

**What is there today:**
- `G/acceptance.py`, `DynamoAcceptance.accept(owner, browser, composition_ref, *, ingestion_revision, destination_revision)` (:90-118)
  builds `record` with five top-level members -- `identity`, `owner`, `browser_sha256`, `composition_ref`, `accepted_at` -- plus `ticket_id`
  when the browser request carries one. None is an actor.
- `G/submission_service.py`, `SubmissionService.submit` (:103 on) holds `principal`, the VERIFIED submitter (`resolve_owner`, :109), and
  calls `self.acceptance.accept(owner, browser, ref, ...)` (:143-145) without passing it.
- The only server-recorded acting principal in the estate is on the on-behalf UPLOAD row:
  `infra/aws/lambda/investor-reporting/intake/uploads.py:267`, `original["acting_principal_id"] = principal["principal_id"]`.
- `accept` returns a PRIOR record unchanged when one exists (`prior = self.lookup(owner, browser)`, :102-104).

**Build:**
1. `accept` takes a new REQUIRED keyword argument `acting_principal_id`. It must be a non-empty string; anything else raises
   `AcceptanceRefused("ACTING_PRINCIPAL_REQUIRED")`. It is written as the top-level member `record["acting_principal_id"]` of a NEW record.
2. `submit` passes `acting_principal_id=principal["principal_id"]`: the verified principal it already holds. NOTHING in `browser` or in
   `payload` is ever read for the actor; if the browser request carries a member of that name, it is not used (and `validate_public_request`
   already decides whether such a member is admitted at all -- do not loosen it).
3. A prior record is returned exactly as stored: no actor is added to it, nothing is rewritten.
4. **Census the readers before you finish.** List every non-test reader of the accepted record under
   `infra/aws/lambda/investor-reporting/` (start from `ops/owned_requests.py` `_validate`, `ops/owned_status.py`,
   `reports/commentary_composition.py` `read_composition`, `ycharts/generate/resident_worker.py`, the packager) and, for each, whether it
   would REFUSE a record carrying one more top-level member (an exact-key-set check on the record, not on `identity`). `ticket_id` is the
   precedent: it is optional and tolerated. Write the census to your deliverables folder as `ACTOR_READER_CENSUS.json`
   (`[{"file", "line", "reads", "closed_key_set": true|false}]`). **A reader with a closed key set is a BLOCKING row** naming it: the
   release that ships this writer must ship that reader in the same act. Do not edit a reader: none is in your grant.
5. Do NOT make any reader USE the actor (`resident_worker.producer_for` reading it is another project's cell).
6. New test file `G/tests/test_acceptance_actor.py` with EXACTLY these names:
   - `test_new_accepted_request_records_the_verified_actor`
   - `test_actor_in_the_request_body_is_never_used`
   - `test_a_prior_accepted_record_is_returned_unchanged_and_not_rewritten`
   - `test_submit_passes_the_verified_principal_to_accept`
   Build its world the way `G/tests/test_submission.py` does.
7. Existing tests that call `accept(...)` directly need the new argument: pass a synthetic principal id, change nothing else in them, and
   name each file you touched.

### ACCEPTANCE (AR-y-37)

<criterion id="AR37-y-AC1" cell_refs="AR-y-37"><invocation>python C:/dev/wk-irpt-anlreq-54/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y37-actor --root C:/dev/wk-irpt-anlreq-54</invocation><expect>Y37-ACTOR-OK</expect></criterion>
`AR37-y-AC1`: the four named tests exist and pass.

<criterion id="AR37-y-AC2" cell_refs="AR-y-37"><invocation>python C:/dev/wk-irpt-anlreq-54/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y37-keep --root C:/dev/wk-irpt-anlreq-54</invocation><expect>Y37-KEEP-OK</expect></criterion>
`AR37-y-AC2`: `test_submission.py` and `test_prospect_submission.py` still pass (they pass at the base).

**The grant gains two product files for `AR-y-37` only:** `infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py` and
`infra/aws/lambda/investor-reporting/ycharts/generate/submission_service.py`. `AR-y-36` still may not touch a product file.
The issuer reads your reader census (step 4) before any release is cut.

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/` and this order's
  file (status flip only).
- READ only: everything else under `infra/aws/lambda/investor-reporting/`.
- No live act: never push, never deploy, never call a live API. No non-ASCII. Synthetic test data only.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/tests/
infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py
infra/aws/lambda/investor-reporting/ycharts/generate/submission_service.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R3_Y.md</decomp_doc> (round 3, workstream Y), cells `AR-y-36` and `AR-y-37` (AMENDMENT 1).
<owned_cells>AR-y-36 AR-y-37</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR36-y-AC1 AR37-y-AC1 AR37-y-AC2. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/IRPT_ANLREQ.TO-AR-y-36.generate-suite-order-independence.proof_of_spec.json`.
Validate it AFTER its commit with `python .tools/proof-of-spec-check.py <instance> AR36-y-AC1,AR37-y-AC1,AR37-y-AC2`.
</proof_of_spec>

**REPORT (once), for BOTH cells:** each check line verbatim; for `AR-y-37` also the reader census (count of readers, count with a closed key set, each named) and every existing test file you touched; the commit; the polluter, what leaks and where; every test file you changed and what the
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
