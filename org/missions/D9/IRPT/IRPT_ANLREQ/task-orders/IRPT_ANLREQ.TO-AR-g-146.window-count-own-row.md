# TO-AR-g-146 -- the lease's window count lives in its OWN store row, so the lease row keeps exactly the eight keys the r34g resident reads (a rollback to r34g must not break the lease): rework of the AR-g-142 mechanism

<to_id>IRPT_ANLREQ.TO-AR-g-146</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~273</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>49</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-146` (`decompositions/IRPT_ANLREQ_DECOMP_R49_G.md`) |
**outcome_ref:** FWD-1 run 3, FWD-7 | **depends_on:** `AR-g-142` (merged `8116e45eb8` on the worker 269 branch, in trunk). Order: CTO msgs 9727, 9757, 9761 (ONE per-window call budget per host) and NEVER-2 (a rollback must leave the host working).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~273`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-273` (branch `wk-IRPT_ANLREQ-273`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~273 <0.9.0_WK_IRPT_ANLREQ~273@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W273-S<k>` (take the next free `<k>`; check the channel file for `W273` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only in the product file. Do not touch anything outside the `<paths>` block.

### THE CELL (`AR-g-146`, inlined)

Why. `AR-g-142` stored the window count INSIDE the provider lease row (two extra keys, `window_start` and `window_count`). The r34g resident that runs on the host checks the lease row's EXACT key set (`OperationLease._read`), so once r34h writes those keys, a rollback to r34g would make every lease read refuse the row (`OPERATION_STORE_INVALID`) while the rollback's own checks still read green. The count must therefore live in its OWN row beside the lease row, and the lease row must stay exactly as r34g reads it. Files: `infra/aws/lambda/investor-reporting/ycharts/session/operation_lease.py` (and its tests). `resident_session.py` already passes `window_budget` and is NOT changed.

Do this in `operation_lease.py`, keeping the public behaviour AR-g-142 gave (`OperationLease(..., window_budget=(calls, window_s))`, `OperationRefused("OPERATION_BUDGET_INVALID")` at construction for an invalid budget, `OperationRefused("OPERATION_WINDOW_BUDGET", retry_after=math.ceil(window_start + window_s - now))` for the (calls+1)th reserve in a window, the window rolling over at exactly `window_s`):

1. REMOVE from the lease row everything AR-g-142 added: `_read` accepts again ONLY the eight base keys (no `window_start`, no `window_count`, no `BASE_KEYS | WINDOW_KEYS` set); `acquire` no longer copies any window keys; `reserve` no longer writes them. The lease row has exactly its eight keys with or without a budget, at every step.
2. The count lives in a second store row. Its key is `self.window_key = "PROVIDER_OPERATION#" + sha256((provider + chr(0) + account_id + chr(0) + "window").encode()).hexdigest()` (the same `PROVIDER_OPERATION#<64 hex>` shape the Dynamo store accepts, computed beside `self.key`). Its value is exactly `{"version": int >= 1, "window_start": finite number >= 0, "window_count": int >= 0 (not a bool)}`; a stored row with any other key set or value is `OperationRefused("OPERATION_STORE_INVALID")`. A missing row means count 0. Reading it goes through `self.store.read(self.window_key)` (a store exception is `OPERATION_STORE_UNAVAILABLE`, as for the lease row).
3. `reserve(token, hard_deadline=...)`: inside the existing `update(row, now)` transform, AFTER the in-flight and spacing refusals (they stay first and unchanged) and only when a budget is configured, DECIDE: read the window row; restart the window when its count is 0 or `now - window_start >= window_s` (start = now, count 0); if `count >= calls` raise `OPERATION_WINDOW_BUDGET` (the transform raises before the lease-row swap, so a refusal writes NOTHING in either row); otherwise remember `(window_start, count + 1)`. After `self._change(token, update)` has swapped the lease row successfully, COMMIT the decision: up to `ATTEMPTS` times read the window row and `self.store.compare_and_swap(self.window_key, <current version or None>, {"version": current + 1 (or 1), "window_start": ..., "window_count": ...})`. A commit that cannot be written (the swap returns False every time, or the store raises) is swallowed: the call already holds its reservation, so it proceeds (the count is then one short; named in the order's report). `reserve` still returns what `_change` returned.
4. The count is shared by every lease object on the same store with no carry-over code, because it is a row of its own; an unbudgeted lease never reads or writes the window row.

Tests: REWRITE the tests AR-g-142 added in `ycharts/session/tests/test_window_budget.py` (and any assertion about the window keys in the lease row in `test_operation_lease.py`) to the new design; keep every behaviour test, change the row-shape tests. Existing tests are not weakened. Read the issuer's check `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g146_checks.py` for the exact fakes and expectations; do not edit it.

1. Run the three criteria. Commit the code and tests, then the proof and the status flip, as separate commits (code first).
2. **Report** the commit hashes and the three criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR146-g-AC1" cell_refs="AR-g-146"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g146_checks.py build</invocation><expect>^AR-G146-OK</expect></criterion>

<criterion id="AR146-g-AC2" cell_refs="AR-g-146"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g146_checks.py guard</invocation><expect>^AR-G146-OK</expect></criterion>

<criterion id="AR146-g-AC3" cell_refs="AR-g-146"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g146_checks.py regress</invocation><expect>^AR-G146-REGRESS-OK</expect></criterion>

<expected_criteria>AR146-g-AC1,AR146-g-AC2,AR146-g-AC3</expected_criteria>

- AC1 runs the real `OperationLease` over a fake store: three calls pass and the fourth is refused with OPERATION_WINDOW_BUDGET and the exact retry_after, writing nothing in either row; the count sits in ONE separate row with keys exactly version, window_start, window_count; the lease row keeps exactly its eight keys with a budget; the window rolls over at exactly window_s; a second lease object shares the count; ten invalid budgets are refused; `resident_session.py` still passes the budget; a budgeted lease over an old store counts from 1; six malformed window rows are OPERATION_STORE_INVALID and leave the lease row alone; a window row that cannot be written (a swap that keeps failing, or a store that raises) does not stop the call. At base (the AR-g-142 in-row design) it FAILs.
- AC2 holds what must not move: with no budget twenty spaced calls pass, the store holds ONE row, the lease row has its eight keys; OPERATION_SPACING comes before the budget and consumes no count. At base it PASSes.
- AC3 runs each existing lease, window-budget, session, capture and runner test file on its own and then that the branch changed only your files, your folder, the order and the channel file (against the merge-base with `box/dell2`). At base it PASSes.
## BOUNDS

- **Grant.** The `<paths>` block only. The checker, the provider port, the cache keys, `KEPT_TTL`, the checker's cap and pacing, and every file not listed are not yours.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/session/operation_lease.py
infra/aws/lambda/investor-reporting/ycharts/session/tests/test_operation_lease.py
infra/aws/lambda/investor-reporting/ycharts/session/tests/test_window_budget.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~273/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-146.window-count-own-row.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R49_G.md</decomp_doc> round 49, workstream ~G, cell `AR-g-146`.
<owned_cells>AR-g-146</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR146-g-AC1, AR146-g-AC2, AR146-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~273/IRPT_ANLREQ.TO-AR-g-146.window-count-own-row.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-146`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR146-g-AC1,AR146-g-AC2,AR146-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 2.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one stdlib module and its tests; no deploy, no AWS call, no network. With no budget configured nothing changes. The new row is written through `DynamoOperationStore`, whose key rule is `PROVIDER_OPERATION#<64 hex>` (the new key has that shape) and which stores any JSON row, so no table change. It reaches production only through the r34h resident release under its own never-widen pair; the rework exists so that pair's rollback leaves the r34g lease readable.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; the lease is called by the resident's jobs.
comp-adversary: RUN -- found by the issuer writing the r34h packet's rollback section: the AR-g-142 design writes two extra keys into the row the r34g lease reads with an exact key-set check, so the install's rollback would leave every lease read refusing. The issuer's check `ar_g146_checks.py` was dry-run against a scratch lease built from the pre-AR-g-142 file plus the reference fix (build OK, guard OK) and four mutants: the count held in memory per lease object, a rollover at `>` instead of `>=`, a fail-closed commit, and a lax window-row read; each fails build. At base (the merged in-row design) build FAILs and guard PASSes. Traps: the count lost between jobs; a refusal that writes a row; the lease row growing a key; a commit failure that stops a call that already holds its reservation. NOT seen (blind): the live DynamoDB rows and any reader of them other than this package; denominator: 9 build arm groups, 2 guard arms.
</preflight>

- Cut on the CTO's rulings (msgs 9727, 9757, 9761) and NEVER-2 by the issuer inside its own decomposition, reworking merged cell AR-g-142. Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: AR146-g-AC1 FAILs, AR146-g-AC2 PASSes, AR146-g-AC3 PASSes (in the worker's worktree).
