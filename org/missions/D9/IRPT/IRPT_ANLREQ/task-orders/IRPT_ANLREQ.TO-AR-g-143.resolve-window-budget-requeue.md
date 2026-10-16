# TO-AR-g-143 -- the resolve hop treats a lease WINDOW-BUDGET refusal like a busy provider: it re-sends the upload for the refusal's retry_after instead of burning its receives

<to_id>IRPT_ANLREQ.TO-AR-g-143</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~270</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>47</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-143` (`decompositions/IRPT_ANLREQ_DECOMP_R47_G.md`) |
**outcome_ref:** FWD-1 run 3 | **depends_on:** none (it only reads a code the lease cell AR-g-142 will raise; the code string is fixed here). Order: CTO msg 9727 condition 1.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~270`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-270` (branch `wk-IRPT_ANLREQ-270`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~270 <0.9.0_WK_IRPT_ANLREQ~270@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W270-S<k>` (take the next free `<k>`; check the channel file for `W270` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only in the product file. Do not touch anything outside the `<paths>` block.

### THE CELL (`AR-g-143`, inlined)

File: `infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`. The cell AR-g-142 makes the provider lease refuse a call over its window budget with `OperationRefused("OPERATION_WINDOW_BUDGET", retry_after=<seconds>)`. The upload door's lookup port already turns a lease refusal into the resolve hop's RETRY code `PROVIDER_READ_UNAVAILABLE:<closed code>` and carries the refusal's `retry_after` (`intake/resolution_broker.py`, `last_refusal`, `last_retry_after`). Today `poll_once` treats ONLY a code ending `RESOLVE_BUSY_CLASS = ":OPERATION_BUSY"` as a busy provider: it re-sends the message for the lease's `retry_after` (clamped to 1..900 s, the flat 60 s when none) BEFORE deleting the received one, so SQS's receive count restarts, and past `RESOLVE_BUSY_DEADLINE_S` (3600 s) from `requested_at` it ends the upload through `_end_busy_resolve` with the journal line `RESOLVE_PROVIDER_BUSY`. Make a code ending `:OPERATION_WINDOW_BUDGET` take exactly the same path.

1. Add a constant `RESOLVE_WINDOW_CLASS = ":OPERATION_WINDOW_BUDGET"` beside `RESOLVE_BUSY_CLASS` and widen the `busy` test in `poll_once` to a code ending with either class (an `endswith`, never a substring: a code that only CONTAINS `OPERATION_WINDOW_BUDGET`, or ends `_EXTRA`, is not it). Everything after the test (the clamp, the send-before-delete, the deadline, the journal) is shared and unchanged; the journal line already prints the code, so the class is named.
2. Nothing else changes: the OPERATION_BUSY class, the WAF back-off (150, 300, 450 s), every other RETRY code (flat 60 s) and the rows with no `requested_at` behave as today.

Tests: append tests to `ycharts/generate/tests/test_resolve_upload.py` (do not weaken existing ones): a budget code with retry_after 120 re-sends with DelaySeconds 120 and deletes the original, none names 60, 5000 clamps to 900; past the deadline the upload ends busy; a code that merely contains the class keeps the flat 60 s visibility. Read the issuer's check `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g143_checks.py` for the exact fakes; do not edit it.

1. Run the three criteria. Commit the code and tests, then the proof and the status flip, as separate commits (code first).
2. **Report** the commit hashes and the three criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR143-g-AC1" cell_refs="AR-g-143"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g143_checks.py build</invocation><expect>^AR-G143-OK</expect></criterion>

<criterion id="AR143-g-AC2" cell_refs="AR-g-143"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g143_checks.py guard</invocation><expect>^AR-G143-OK</expect></criterion>

<criterion id="AR143-g-AC3" cell_refs="AR-g-143"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g143_checks.py regress</invocation><expect>^AR-G143-REGRESS-OK</expect></criterion>

<expected_criteria>AR143-g-AC1,AR143-g-AC2,AR143-g-AC3</expected_criteria>

- AC1 runs the REAL `poll_once` with a queue double: a budget code re-sends for retry_after 120, the flat 60 s when none, 900 at most, 1 at least, deletes the original, makes no visibility call; past the busy deadline the upload ends through `_end_busy_resolve` with `RESOLVE_PROVIDER_BUSY`; the journal names the class. At base it FAILs.
- AC2 holds what must not move: the BUSY class keeps its re-send; the WAF class keeps 150, 300, 450 s; every other code, a code that only contains the class, and a budget code with no requested_at take the flat 60 s visibility path. At base it PASSes.
- AC3 runs the two existing resident-worker test files on their own (`test_resolve_upload.py`, `test_frozen_worker.py`) and then that the branch changed only your files, your folder, the order and the channel file (against the merge-base with `box/dell2`). At base it PASSes.
## BOUNDS

- **Grant.** The `<paths>` block only. The checker, the provider port, the cache keys, `KEPT_TTL`, the checker's cap and pacing, and every file not listed are not yours.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resolve_upload.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~270/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-143.resolve-window-budget-requeue.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R47_G.md</decomp_doc> round 47, workstream ~G, cell `AR-g-143`.
<owned_cells>AR-g-143</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR143-g-AC1, AR143-g-AC2, AR143-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~270/IRPT_ANLREQ.TO-AR-g-143.resolve-window-budget-requeue.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-143`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR143-g-AC1,AR143-g-AC2,AR143-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 2.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one module and its tests; no deploy, no AWS call, no network. The change is one extra class in the resolve hop's busy test; every other path is unchanged. It reaches production only through a later resident release under its own never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; poll_once runs inside the existing resident.
comp-adversary: RUN -- the issuer's check `ar_g143_checks.py` was dry-run against a scratch copy of the whole package with the reference fix (build OK, guard OK) and a mutant that matches the class as a SUBSTRING (build OK, guard FAILS on the `_EXTRA` code and the mid-string code). Traps: a substring match; a budget code taking the 60 s visibility path (burning the receive count that the busy path restarts); a retry_after not clamped; the deadline not applied. NOT seen (blind): the live queue's redelivery and the lease raising the code in the resident (cell AR-g-142 and the release); denominator: 3 build arms, 4 guard arms.
</preflight>

- Cut on the CTO's ruling (msg 9727) by the issuer inside its own decomposition. Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: AR143-g-AC1 FAILs, AR143-g-AC2 PASSes, AR143-g-AC3 PASSes (in the worker's worktree).
