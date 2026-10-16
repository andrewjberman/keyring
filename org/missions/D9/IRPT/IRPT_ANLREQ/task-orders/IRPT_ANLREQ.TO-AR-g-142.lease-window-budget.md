# TO-AR-g-142 -- the provider lease counts reserved calls per window, ONE count per host account (PRD v0.22 item 4; CTO msg 9727 condition 1): OperationLease(window_budget=(calls, window_s)) and ResidentSession(window_budget=...)

<to_id>IRPT_ANLREQ.TO-AR-g-142</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~269</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>47</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-142` (`decompositions/IRPT_ANLREQ_DECOMP_R47_G.md`) |
**outcome_ref:** FWD-1 run 3, FWD-7 | **depends_on:** none (the paced read sets the NUMBER later, in the bindings). Order: CTO msgs 9522, 9727 (ONE per-window count budget per host, shared by the door's lookups, the price tier and the SPY/BIL calls; never one per caller).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~269`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-269` (branch `wk-IRPT_ANLREQ-269`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~269 <0.9.0_WK_IRPT_ANLREQ~269@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W269-S<k>` (take the next free `<k>`; check the channel file for `W269` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only in the product file. Do not touch anything outside the `<paths>` block.

### THE CELL (`AR-g-142`, inlined)

Files: `infra/aws/lambda/investor-reporting/ycharts/session/operation_lease.py` and `.../ycharts/session/resident_session.py`. The YCharts firewall counts calls per window from this host, not per caller. Every YCharts caller already shares ONE lease row per provider account (`OperationLease.key`, stored through `DynamoOperationStore` as the JSON of the whole row). Add a per-window call count to that row, so the count is shared by every process and every caller, and the next release can set its number from a measurement.

1. `OperationLease.__init__(self, store, *, provider, account_id, clock, window_budget=None)`. `window_budget` is None (no budget: the lease of today, exactly) or a tuple `(calls, window_s)` with `calls` an int of at least 1 (not a bool) and `window_s` a finite int or float above 0. Anything else raises `OperationRefused("OPERATION_BUDGET_INVALID")` at construction.
2. The stored row keeps its eight keys. When (and only when) a budget is configured, the row also carries `window_start` (a finite number of at least 0) and `window_count` (an int of at least 0, not a bool). `_read` accepts a row with the eight keys, or with the eight plus BOTH window keys; a row with an unknown extra key, only one of the two window keys, or a malformed window value is still `OperationRefused("OPERATION_STORE_INVALID")`. A row with no window keys read by a budgeted lease means count 0.
3. `reserve(token, hard_deadline=...)`: after the existing in-flight and spacing refusals (they stay first and unchanged), with a budget: if `window_count` is 0 or `now - window_start >= window_s` the window restarts (`window_start = now`, count 0); then if `window_count >= calls` raise `OperationRefused("OPERATION_WINDOW_BUDGET", retry_after=math.ceil(window_start + window_s - now))`; else store `window_count + 1` and `window_start` in the same compare-and-swap as the spacing and in-flight updates. A refused reserve writes nothing (the transform raises before the swap, as the existing refusals do).
4. `acquire(...)` builds a new row from scratch today: when the old row carries the window keys, the new row carries them over unchanged (like `next_allowed_at`), so a new lease object (a new job) shares the count. `renew`, `complete` and `release` change nothing about the window keys (they copy the row).
5. `ResidentSession.__init__` gains `window_budget=None` and passes it as `window_budget=window_budget` to the `OperationLease` it builds.

6. REPAIR one existing test (a test defect that the merged AR-g-133 door change exposed, not a product defect): `ycharts/session/tests/test_resident_session.py::test_resident_factory_uses_canonical_secret_and_durable_lookup_boundary` calls `runtime.template_resolver(identity=..., source_revision='fixture')` with no `checker`, which builds the REAL `YfinanceChecker()`. Since the door now asks the checker FIRST for every uncached symbol, that offline test makes a live Yahoo call for AAPL and reads KEPT instead of the provider's FOUND. Pass an offline checker (an object with `check(symbols)` returning `{symbol: {"state": "NOT_KEPT"}}` for each symbol; `template_resolver` documents `checker` as the offline control) so the test again proves the provider boundary it is named for (FOUND, no stored-session read, the lease row after the lookup). Do not weaken any assertion. Nothing else in that file changes. AC3 FAILs at base on exactly this test; your change makes it pass.

Tests: add `ycharts/session/tests/test_window_budget.py` with one test per numbered behaviour (a passing and a refusing arm for 3, the carry-over for 4, the invalid budgets for 1, the row-shape arms for 2); existing tests are not weakened. Read the issuer's check `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g142_checks.py` for the exact fake store and expectations; do not edit it.

1. Run the three criteria. Commit the code and tests, then the proof and the status flip, as separate commits (code first).
2. **Report** the commit hashes and the three criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR142-g-AC1" cell_refs="AR-g-142"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g142_checks.py build</invocation><expect>^AR-G142-OK</expect></criterion>

<criterion id="AR142-g-AC2" cell_refs="AR-g-142"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g142_checks.py guard</invocation><expect>^AR-G142-OK</expect></criterion>

<criterion id="AR142-g-AC3" cell_refs="AR-g-142"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g142_checks.py regress</invocation><expect>^AR-G142-REGRESS-OK</expect></criterion>

<expected_criteria>AR142-g-AC1,AR142-g-AC2,AR142-g-AC3</expected_criteria>

- AC1 runs the real `OperationLease` over a fake linearizable store: three calls pass and the fourth is refused with OPERATION_WINDOW_BUDGET and the exact retry_after; a refused reserve consumes nothing; the window rolls over at exactly window_s; the count is shared by a second lease object on the same store (the carry-over in `acquire`); ten invalid budgets are refused; the stored row carries exactly the eight keys plus the two window keys; `resident_session.py` passes the budget on. At base it FAILs.
- AC2 holds what must not move: with no budget twenty spaced calls pass and the row keeps exactly its eight keys; an old-schema row reads under a budget; an unknown key and malformed window fields are still OPERATION_STORE_INVALID; OPERATION_SPACING still comes before the budget and consumes no count. At base it PASSes.
- AC3 runs each existing lease, session, capture and runner test file on its own (`test_operation_lease.py`, `test_resident_session.py`, `test_host_capture.py`, `ycharts/research/tests/test_runner.py`) and then that the branch changed only your files, your folder, the order and the channel file (against the merge-base with `box/dell2`). At base it FAILs on the one test named in item 6 (a live Yahoo call in an offline test); after your change it passes.
## BOUNDS

- **Grant.** The `<paths>` block only. The checker, the provider port, the cache keys, `KEPT_TTL`, the checker's cap and pacing, and every file not listed are not yours.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/session/operation_lease.py
infra/aws/lambda/investor-reporting/ycharts/session/resident_session.py
infra/aws/lambda/investor-reporting/ycharts/session/tests/test_operation_lease.py
infra/aws/lambda/investor-reporting/ycharts/session/tests/test_resident_session.py
infra/aws/lambda/investor-reporting/ycharts/session/tests/test_window_budget.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~269/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-142.lease-window-budget.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R47_G.md</decomp_doc> round 47, workstream ~G, cell `AR-g-142`.
<owned_cells>AR-g-142</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR142-g-AC1, AR142-g-AC2, AR142-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~269/IRPT_ANLREQ.TO-AR-g-142.lease-window-budget.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-142`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR142-g-AC1,AR142-g-AC2,AR142-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 2.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- two stdlib modules and their tests; no deploy, no AWS call, no network. The lease row is shared by every YCharts caller of the account through `DynamoOperationStore` (the whole row is stored as JSON, so the two new keys need no table change). With no budget configured nothing changes. It reaches production only through a later resident release under its own never-widen pair, and the budget NUMBER only through the bindings (cell AR-g-144).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; the lease is called by the resident's jobs.
comp-adversary: RUN -- the issuer's check `ar_g142_checks.py` was dry-run against a scratch copy with the reference fix (build OK, guard OK) and five mutants: acquire drops the count (the count dies at each job), the count kept in memory per lease object, the window rolling over at `>` instead of `>=`, a relaxed `_read` that accepts unknown keys and malformed window values, and a lease that writes the window keys with no budget; each fails build or guard. One more mutant (the refusal consuming the spacing before it raises) is equivalent, because a raising transform writes nothing. Traps: the count lost at `acquire`; one count per lease object instead of per account; the schema loosened for everyone; the window keys written when no budget is set (an older reader of the same row would refuse it). NOT seen (blind): the live DynamoDB row and any older process still reading it, the budget's number (set later from the paced read), and the real WAF behaviour; denominator: 5 build arms, 4 guard arms.
</preflight>

- Cut on the CTO's rulings (msgs 9522 and 9727) by the issuer inside its own decomposition. Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: AR142-g-AC1 FAILs, AR142-g-AC2 PASSes, AR142-g-AC3 PASSes (in the worker's worktree).
