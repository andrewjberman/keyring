# TO-AR-g-101 -- the resident installer supplies the Opal producer's swap store from a pinned pool binding: the dated pool snapshot, the batched Yahoo history port, off unless the binding is present

<to_id>IRPT_ANLREQ.TO-AR-g-101</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~203</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-101` (`decompositions/IRPT_ANLREQ_DECOMP_R25_G.md`) |
**outcome_ref:** FWD-2 (C-SWAP; PRD v0.14, v0.18, v0.19) | **depends_on:** `AR-g-98` (`swap_pass.py`, merged), `AR-g-99` (`yahoo_history_days.py`, merged), `AR-g-90` (the pricing binding this cell mirrors, merged). Order: CTO msgs 8711, 8714 (ADDENDUM 5: the pool is a dated snapshot SHIPPED in the resident package, pinned like the maps; no IAM change).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~203`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-203` (branch `wk-IRPT_ANLREQ-203`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/`, `lib/`, `org/standards`, `org/tier1_exec/2.0.0_SA_COO~G2` and `org/missions/D9/IRPT` on disk. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~203 <0.9.0_WK_IRPT_ANLREQ~203@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either. (A provisioner error about a portal sub-worktree does not concern you.)
- A row id has the form `IRPT_ANLREQ-D2-W203-S<k>` (take the next free `<k>`; check the channel file for `W203` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`). The checker is run WITHOUT `-I`.

### Read first (under `C:/dev/wk-irpt-anlreq-203/infra/aws/lambda/investor-reporting/`)

- `reports/resident_installed.py` (the whole file: `load_bindings`, `_resolve`, `_pricing_extras`, `make_opal_stores`, `_opal_map_loader` and `build_resident_runtime` where `make_opal_stores(...)` is called) and `reports/tests/test_resident_installed.py` and `reports/tests/test_opal_pricing_binding.py` (the `package` fixture, `fake_clients`, `rewrite`, `opal_record`, `sha`; this cell mirrors the pricing binding cell AR-g-90).
- `ycharts/research/swap_pass.py` (`load_pool(path, today)`), `ycharts/research/yahoo_history_days.py` (`make_history_days()`), `ycharts/research/opal_producer.py` (the `swap` store documented in its docstring) and `ycharts/generate/resident_worker.py` `load_opal_producer` (it puts `ycharts/research` on `sys.path`).

### THE CELL (`AR-g-101`, inlined)

`AR-g-100` made the Opal producer accept an optional `swap` store; no caller sets it. This cell makes the resident set it from an OPTIONAL binding, so the capability ships dormant: with no binding the stores carry no `swap` key and an UNRESOLVED holding refuses the run as today.

**`reports/resident_installed.py`, exactly this:**
1. Add `import re` (alphabetical among the existing imports) and, next to `PRICING_TIERS`, a comment and the constant `OPAL_SWAP_POOL_BINDING = "opal_swap_pool"`. The comment says the binding is `{"path", "sha256"}`, that it names the dated pool snapshot the Opal producer replaces UNRESOLVED holdings from, pinned by content like the maps, and that absent, an UNRESOLVED holding refuses the run as before.
2. In `load_bindings`, before the packager check, validate the binding when the key is present, refusing with `ResidentInstallRefused("RESIDENT_SWAP_POOL_BINDINGS")` (that exact text, no suffix) unless ALL hold: it is a `dict` whose keys are exactly `path` and `sha256`; `path` is a `str` that is not blank; `sha256` is a `str` that fully matches `[0-9a-f]{64}` (lower-case hex only). Absent key: nothing changes.
3. New module function `_swap_extras(bindings, base, clock)`: returns `None` unless `bindings.get(OPAL_SWAP_POOL_BINDING)` is a dict; otherwise returns a function `extras()` (called per job by the Opal stores, never at install) that: resolves the path with `_resolve(base, binding["path"])`; raises `ResidentInstallRefused("PINNED_FILE_ABSENT:opal_swap_pool")` when it is not a file and `ResidentInstallRefused("PINNED_FILE_DIFFERS:opal_swap_pool")` when `_sha256(path)` differs from the binding's `sha256` (these exact texts, the pin is read each call); calls `resident_worker.load_opal_producer()` (imported inside) so `ycharts/research` is on `sys.path`; imports `swap_pass` and `yahoo_history_days` inside; takes the run date as the UTC date of `clock()` (`datetime.datetime.fromtimestamp(clock(), datetime.timezone.utc).strftime("%Y-%m-%d")`); and returns `{"swap": {"pool": swap_pass.load_pool(str(path), today), "history_days": yahoo_history_days.make_history_days()}}`. A pool that does not load raises `swap_pass.SwapPoolRefused` out of the job (a stale pool loads: `load_pool` says so). A comment above says the pool is re-read each job so an old pool is stale-flagged by the day, and that the history port imports `yfinance` only when a candidate is asked.
4. `make_opal_stores(...)` gains the keyword `swap_extras=None` (after `pricing_extras=None`). In the returned `opal_stores(principal, record)`, directly after the `pricing_extras` merge and BEFORE `stores.update(extras or {})`: `if swap_extras is not None: stores.update(swap_extras())`. So the offline `extras` still win. Nothing else in the function changes.
5. `build_resident_runtime` passes `swap_extras=_swap_extras(bindings, base, clock)` to `make_opal_stores`, beside `pricing_extras=...`.
6. Nothing else changes: not `build_resident_package.py` (the pool ships through the release tooling, a separate act), not the bindings file in the package, not `opal_producer.py`.

**Tests.** A NEW file `reports/tests/test_opal_swap_pool_binding.py`, offline, importing the fixtures and helpers of `test_resident_installed.py` as `test_opal_pricing_binding.py` does (`from test_resident_installed import fake_clients, opal_record, package, rewrite, ri, sha`, with `# noqa: E402,F401,F811`), with these exact test function names (the checker looks for each by name). Build the runtime with the `package` fixture, an `opal_map` binding to a tiny map file, a pool file `{"schema": "irpt-swap-pool.v1", "pool_as_of": ..., "pool_claim": "held", "rows": [...]}` written beside it and bound by `{"path": "swap_pool.json", "sha256": ...}`, `clock=lambda: 1_800_000_000` (2027-01-15T08:00:00Z), and an Opal record that `producer_for` admits (`opal_record(...)` plus `"ticket_confirmed": True`):
`test_absent_binding_adds_no_swap_store`, `test_binding_supplies_the_pool_and_a_history_port` (the store has exactly `pool` and `history_days`; the history port is callable and has `prefetch`), `test_the_run_date_is_the_clock_date_and_an_old_pool_is_stale` (a pool 45 days before the clock date is stale; one dated the clock date is not), `test_a_changed_or_absent_pool_file_refuses_the_job` (both exact texts), `test_bad_bindings_refuse_the_load` (several bad shapes, including a blank path, an upper-case or short sha, an extra key and a non-dict), `test_offline_extras_win` (`make_opal_stores(..., extras={"swap": "OFFLINE"}, swap_extras=lambda: {"swap": {...}})` returns `"OFFLINE"`).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR101-g-AC1" cell_refs="AR-g-101"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g101_checks.py g101</invocation><expect>^AR-G101-OK</expect></criterion>

<criterion id="AR101-g-AC2" cell_refs="AR-g-101"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g101_checks.py regress</invocation><expect>^AR-G101-REGRESS-OK</expect></criterion>

<expected_criteria>AR101-g-AC1,AR101-g-AC2</expected_criteria>

- AC1 builds the real runtime with the issuer's 29 tests (no store when the binding is absent; the pool and a batched history port when it is present; the run date from the clock so an old pool is stale; a changed or absent pool file refused with the exact texts; a pool that does not load refused with its own code; 15 bad bindings refused with the exact text and 2 good ones loaded; pricing and swap extras together; the offline extras winning; the pin read per job), then checks your six named tests exist and pass. At base it FAILs.
- AC2 runs seven existing test files one at a time (82 tests: the installer, the pricing binding, the packager bindings, the package imports, the r31 and r32 source) and needs all of them to pass, and it needs your branch (against the merge-base with `box/dell2`) to change only your two files, your folder, your order and the channel file. At base it PASSes. Run it under `timeout 590` (the package-imports file alone takes about 40 s).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/reports/tests/test_opal_swap_pool_binding.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~203/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-101.resident-swap-pool-binding.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R25_G.md</decomp_doc> round 25, workstream ~G, cell `AR-g-101`.
<owned_cells>AR-g-101</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR101-g-AC1, AR101-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~203/IRPT_ANLREQ.TO-AR-g-101.resident-swap-pool-binding.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-101`.
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put the `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR101-g-AC1,AR101-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the lines you changed in `resident_installed.py` with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `reports/resident_installed.py` is a member of the resident package (r32 carries the PRE-binding bytes; the next resident release carries this) and is staged into no Lambda (it is not in either source map function's files). With no `opal_swap_pool` binding the module's behaviour is byte for byte today's (the check and the existing 82 tests pin it). A bound pool is read each job, so a bindings edit (or a replaced pool file under a new pin) takes effect on the next job without a restart of the service's process state beyond the bindings load. The pool file is a release artifact (a dated snapshot of the etf-classifications class columns: ticker, asset_class, sub_asset_class, claim held); this cell reads one and writes none.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change; the pool is a shipped file, the history port reads Yahoo (no estate resource), the classifier is the existing GetItem port (CTO ADDENDUM 5: no IAM change).
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against CTO ADDENDUM 5 and the pricing binding cell AR-g-90. Traps: a store supplied with no binding (an unconfigured resident would then try to swap); the pool file not checked against its pin, or checked once at install (a replaced file would be trusted); the run date typed instead of the clock's (a stale pool read as fresh, or a valid one refused as future-dated); a bare function as the history port (no batching, one request per candidate); a binding shape not validated (an upper-case sha, a blank path); the offline extras not winning (a control could not stub the port); the pricing extras lost when the pool is bound; the pool path hard coded. The checker feeds a green arm (a reference build passes the 29 issuer tests, the six named tests and the 82 regress tests) and 13 mutant arms, each of which fails the check.
</preflight>

- Cut on CTO msgs 8711, 8714 and the issuer's reference build in a scratch tree. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR101-g-AC1` FAILs and `AR101-g-AC2` PASSes (82), as expected.
- NOT claimed: that the pool is in any package (the r34 release tooling ships it, with a bindings key this cell reads); that `yfinance` is installed on the host (the history port imports it only when a candidate is asked; its first real read is the r34 apply's one-ticker smoke read and a missing library there reads as `HISTORY_ERROR` candidates, never a wrong replacement); the producer wiring (`AR-g-100`, round 24).
