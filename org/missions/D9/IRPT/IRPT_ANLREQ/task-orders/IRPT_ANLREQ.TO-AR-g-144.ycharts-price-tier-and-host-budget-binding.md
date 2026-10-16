# TO-AR-g-144 -- the resident's YCharts price tier and the host's call-budget binding (FWD-7 C-PRICES; PRD v0.22 item 4; CTO msgs 9727, 9757, 9761): bindings accept the tier and ycharts_window_budget, a transport over the stored session feeds the existing price reader, the runtime hands the budget to the session

<to_id>IRPT_ANLREQ.TO-AR-g-144</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~271</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>48</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-144` (`decompositions/IRPT_ANLREQ_DECOMP_R48_G.md`) |
**outcome_ref:** FWD-7 | **depends_on:** `AR-g-142` (`ResidentSession(window_budget=)`, merged before this order's branch was cut); the scope record `YCHARTS_PRICE_TIER_SCOPE.json` (AR-g-141). Order: CTO msgs 9727 (build the four code gaps, offline-tested; ONE budget per host), 9757 and 9761 (the budget is (6 calls, 390 s), counts every securities_info call, and is a floor set in the bindings, not in code).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~271`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-271` (branch `wk-IRPT_ANLREQ-271`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~271 <0.9.0_WK_IRPT_ANLREQ~271@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W271-S<k>` (take the next free `<k>`; check the channel file for `W271` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only in the product file. Do not touch anything outside the `<paths>` block.

### THE CELL (`AR-g-144`, inlined)

Read the scope record first: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~268/YCHARTS_PRICE_TIER_SCOPE.json` (51 cited rows; the `rows` with role TIER_LIST, WIRING, READER_TEMPLATE and SESSION_OR_LEASE name every line this cell touches). Files: `infra/aws/lambda/investor-reporting/reports/resident_installed.py` and ONE new module `infra/aws/lambda/investor-reporting/ycharts/research/price_transport_ycharts.py`.

1. Tier list and budget binding in `resident_installed.py`. `PRICING_TIERS` gains `"ycharts"` (the validator in `load_bindings` already reads it). A new optional binding `ycharts_window_budget` (a constant `YCHARTS_WINDOW_BUDGET_BINDING = "ycharts_window_budget"`) is exactly `{"calls": <int>, "window_s": <number>}`: `calls` an int of at least 1 (a bool is not an int here), `window_s` a finite int or float above 0, no other key; anything else raises `ResidentInstallRefused("RESIDENT_WINDOW_BUDGET_BINDING")` in `load_bindings`. Absent is fine (no budget). `import math` if the module lacks it.
2. The transport. `ycharts/research/price_transport_ycharts.py`: `class PriceTransportRefused(RuntimeError)` and `make_transport(session, *, request_budget=60, ttl=120)` returning `transport(path, params)`, the callable `price_adapter_ycharts.make_reader` expects. Per call it builds the request path `path + "?" + urllib.parse.urlencode(params, safe=":,")` (the research runner encodes exactly so: `ycharts/research/runner.py` line 121; no `?` when params is empty), calls `session.acquire(request_budget=request_budget, ttl=ttl)` ONCE, then `info, body = facade.request(request_path)`, and ALWAYS closes the facade in a `finally`. If `info.get("status") != 200` raise `PriceTransportRefused("PRICE_HTTP_<status>")`; if the body is not JSON raise `PriceTransportRefused("PRICE_BODY_NOT_JSON")`; otherwise return `json.loads(body)`. Nothing is caught or invented: an `OperationRefused` from the lease (including the window budget cell AR-g-142's `OPERATION_WINDOW_BUDGET`) propagates, and `price_source._ask_tier` records it as that tier's ERROR so the symbol falls to the next step or is reported unpriced.
3. The reader. `_pricing_extras(bindings, clients, clock, session=None)`: when the enabled binding lists `"ycharts"` and `session is None`, raise `ResidentInstallRefused("PRICING_YCHARTS_SESSION_REQUIRED")` right away (before `extras` is returned); in `extras()` a tier `"ycharts"` builds `readers["ycharts"] = price_adapter_ycharts.make_reader(price_transport_ycharts.make_transport(session))` (imports inside the branch, as the estate and yfinance branches do). Estate and yfinance branches and the return are unchanged.
4. The runtime. In `build_resident_runtime`: pass `window_budget=_window_budget(bindings)` to the `ResidentSession(...)` it builds (add the small helper `_window_budget(bindings)` returning `None` when the binding is absent and `(calls, window_s)` as a tuple otherwise) and pass `session=session` to `_pricing_extras(...)`.

Tests: add `reports/tests/test_ycharts_price_tier.py` and `ycharts/research/tests/test_price_transport_ycharts.py` with one test per numbered item (a passing and a refusing arm each), offline: fake session objects, no network. In `reports/tests/test_opal_pricing_binding.py` the refused-tiers list includes `"ycharts"` today (the scope record row names its line): remove it from that list in the same change. Existing tests are not weakened. Read the issuer's check `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g144_checks.py` for the exact fakes and expectations; do not edit it.

1. Run the three criteria. Commit the code and tests, then the proof and the status flip, as separate commits (code first).
2. **Report** the commit hashes and the three criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR144-g-AC1" cell_refs="AR-g-144"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g144_checks.py build</invocation><expect>^AR-G144-OK</expect></criterion>

<criterion id="AR144-g-AC2" cell_refs="AR-g-144"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g144_checks.py guard</invocation><expect>^AR-G144-OK</expect></criterion>

<criterion id="AR144-g-AC3" cell_refs="AR-g-144"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g144_checks.py regress</invocation><expect>^AR-G144-REGRESS-OK</expect></criterion>

<expected_criteria>AR144-g-AC1,AR144-g-AC2,AR144-g-AC3</expected_criteria>

- AC1 runs the real `load_bindings`, the new transport and `_pricing_extras` over fake sessions: a valid tier and budget load; twelve malformed budgets are refused with RESIDENT_WINDOW_BUDGET_BINDING; the transport returns the parsed answer, encodes the request path as the research runner does, acquires once per call and closes the facade even when the call raises, and raises on an exception, a non-200 reply and a body that is not JSON; the ycharts reader is built from a session and returns rows; a ycharts tier with no session is refused; `build_resident_runtime` passes `window_budget` to its `ResidentSession` and `session=` to `_pricing_extras` (read from the source). The fixture is the r34g package's own bindings file at `C:/dev/irpt-release-r34m/x34/reports/resident_bindings.json`. At base it FAILs.
- AC2 holds what must not move: the shipped bindings still load, an unknown tier is still refused, a disabled pricing binding gives no extras, a two-tier binding works with no session. At base it PASSes.
- AC3 runs each existing pricing, price-source, adapter and session test file on its own (`test_opal_pricing_binding.py`, `test_resident_r32_source.py`, `test_price_source.py`, `test_price_adapter_ycharts.py`, `ycharts/session/tests/test_resident_session.py`) and then that the branch changed only your files, your folder, the order and the channel file (against the merge-base with `box/dell2`). At base it PASSes (after the AR-g-142 merge).
## BOUNDS

- **Grant.** The `<paths>` block only. The checker, the provider port, the cache keys, `KEPT_TTL`, the checker's cap and pacing, and every file not listed are not yours.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/ycharts/research/price_transport_ycharts.py
infra/aws/lambda/investor-reporting/reports/tests/test_opal_pricing_binding.py
infra/aws/lambda/investor-reporting/reports/tests/test_ycharts_price_tier.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_transport_ycharts.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~271/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-144.ycharts-price-tier-and-host-budget-binding.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R48_G.md</decomp_doc> round 48, workstream ~G, cell `AR-g-144`.
<owned_cells>AR-g-144</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR144-g-AC1, AR144-g-AC2, AR144-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~271/IRPT_ANLREQ.TO-AR-g-144.ycharts-price-tier-and-host-budget-binding.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-144`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR144-g-AC1,AR144-g-AC2,AR144-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 2.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one existing module, one new module and their tests; no deploy, no AWS call, no network. With no `ycharts` tier and no budget binding nothing changes (the shipped r34g bindings have neither). It reaches production only through the r34h resident release under its own never-widen pair, where the bindings carry the tier and the budget (6 calls, 390 s, a FLOOR set by the paced read, CTO msgs 9757 and 9761).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; the price stage runs inside the existing resident's job.
comp-adversary: RUN -- the issuer's check `ar_g144_checks.py` was dry-run against a scratch copy of the whole package with the reference fix (build OK, guard OK) and five mutants: the facade not closed on a failed call, no status or JSON check, a query encoded without safe=':,', a bool accepted as calls, and no refusal of a ycharts tier with no session; each fails build. Traps: a lease leaked by a failed call (the facade stays acquired until its ttl and blocks every later YCharts caller); a query encoded differently from the runner (the id: token changes on the wire); a ycharts tier silently absent; the budget read from code instead of the bindings. NOT seen (blind): the live YCharts answer to `id:<TICKER>` (one of the three unmeasured items, measured after window 4), the served single-ticker shape (the adapter's fixtures only) and whether the price route needs the signed-in session (this cell uses the session-bearing acquire); denominator: 4 build groups, 4 guard arms.
</preflight>

- Cut on the CTO's rulings (msgs 9727, 9757 and 9761) from the scope record AR-g-141 by the issuer inside its own decomposition. Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: AR144-g-AC1 FAILs, AR144-g-AC2 PASSes, AR144-g-AC3 PASSes (in the worker's worktree).
