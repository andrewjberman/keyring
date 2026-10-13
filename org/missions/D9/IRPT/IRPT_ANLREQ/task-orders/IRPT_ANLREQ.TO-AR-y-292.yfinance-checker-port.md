# TO IRPT_ANLREQ.TO-AR-y-292.yfinance-checker-port -- C-SWAP step 2: the yfinance history checker -- one paced read per unknown symbol, errors raise, a cap of 10

<to_id>IRPT_ANLREQ.TO-AR-y-292</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~106</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-292` (`decompositions/IRPT_ANLREQ_DECOMP_R23C_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~106`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-106` (branch `wk-IRPT_ANLREQ-106`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~106 <0.9.0_WK_IRPT_ANLREQ~106@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W106-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-292`, inlined) -- THE CHECKER. Code and tests only; every test on fakes; NO LIVE CALL except the one read-only history call named in step 4; nothing is released.

**C-SWAP (PRD `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` :104), steps (1) KNOWN and (2) the YFINANCE CHECKER, and the CTO's rulings (msg 7210) on the read `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~99/r23/C_SWAP_STEPS_1_2_READ.json` (cell `AR-y-278`, drained @de81ce19c1):** one pass per unknown holding; a holding the provider (YCharts `securities_info`) answers NOT_FOUND is checked against the registry (step 1) and then with ONE yfinance `history(period='1mo')` call (step 2); rows greater than 0 with a finite positive last close means KEPT (KEEP still requires history). Rulings: **K = 10 unknown symbols checked per upload, one call each, paced at 1 s**; unknowns beyond 10 get the EXISTING proxy prompt, worded 'not checked'; **a yfinance exception, a timeout, or an error-shaped empty frame reads CHECK_FAILED, shown in words and never treated as absent: make the client raise** (yfinance hides exceptions by default and returns an empty frame: MEASURED, ALPPL, BREIT and CCCQ returned 0 rows with no exception, ALPPL printed an HTTP 404 'Quote not found'); a 401, 403 or 429 stops the step for the rest of the upload. No Andrew word is needed for the Yahoo egress: standing law, CLAUDE.md Agent Autonomy ('Egress is open on every channel, except Bloomberg'; 'other vendor APIs need no per-use word'; Andrew-direct 2026-10-09, `ANDREW_DIRECT_20261009_024xZ_LAW_EDIT_*`), which postdates the MDPF_SECHIST addendum's limit: cite it in the record. MEASURED: `TIMXX` returns 20 daily rows, last close 1.0 (a money-market fund): KEPT, no proxy. The registry row and the price landing for a KEPT symbol are MDPF_SECCLASS's and MDPF_SECHIST's (dell1) and are NOT this cell's (the CTO routes them). The withdrawn Kimi model-proposed swap is retired and reverted (@c822052bc4): do not touch `resolution_kimi.py` or `upload_suggestions.py`.
**THE INTERFACE (fixed here so the three cells build in parallel):** a new module `infra/aws/lambda/investor-reporting/intake/yfinance_check.py` (cell B) exposes `class YfinanceChecker(*, history=None, sleep=time.sleep, clock=time.monotonic, cap=10, pace_seconds=1.0)` with `check(symbols) -> dict` mapping each UPPER-CASE symbol to `{'state': 'KEPT' | 'NOT_KEPT' | 'CHECK_FAILED' | 'NOT_CHECKED', 'rows': int, 'last_close': float | None, 'reason': str}`; `history(symbol)` is an injected port returning a list of `(date_iso, close)` pairs and RAISING on any error (the default builds the real yfinance call with exceptions made to raise); `NOT_CHECKED` is a symbol beyond the cap; `CHECK_FAILED` carries a reason word (`EXCEPTION`, `TIMEOUT`, `PUSHBACK`, `ERROR_FRAME`); `NOT_KEPT` is a clean empty answer. The resolver (cell C) consumes it: the resolution result for a symbol the provider answered NOT_FOUND gets a new state `KEPT` (reason `YFINANCE_HISTORY`, `price_source 'yfinance'`, the checker's rows and last close, NO provider receipt) when the checker says KEPT; `CHECK_FAILED` and `NOT_CHECKED` keep the symbol unknown and carry their reason words to the finding.

1. **Read first:** the read record above (`design.step_2_yfinance_check`, `measurement`), `data/mdpf/scripts/demque/yahoo_pull.py` (the estate's existing paced yfinance caller: its `Pacer`, its pushback codes `_PUSHBACK_CODES`, how it builds the call; REUSE its conventions, do not import across the data/lambda boundary), `infra/aws/lambda/investor-reporting/intake/security_resolution.py` (the resolver the checker will feed), and the resident's runtime: **is `yfinance` importable in the resident host's Python, and in the `irpt-ycharts-generate` Lambda package?** Read the resident package recipe and requirements (`infra/aws/lambda/investor-reporting/ycharts/generate/` requirements files, `reports/build_resident_package.py`, the release-19 recipe record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/RESIDENT_RECIPE_AND_DELTA.json`, `infra/aws/lambda/ci/lambda-source-map.json` for the Lambda). Record `read` {`pacer_conventions` (file:line), `yfinance_in_resident` (yes, no or NOT READ, with the file:line that decides), `yfinance_in_lambda`, `pandas_needed`}. **If yfinance is NOT a member or dependency of the resident or Lambda package, do not add a dependency: build the module with the history port INJECTED (the default raises `CHECKER_UNAVAILABLE`), state the missing dependency in `release_needs`, and continue.**
2. **The module.** ONE new file `infra/aws/lambda/investor-reporting/intake/yfinance_check.py` (ASCII) implementing THE INTERFACE: symbols upper-cased and de-duplicated; the first `cap` (10) distinct symbols are checked in order, one `history` call each, `sleep(pace_seconds)` between calls (none before the first); the rest are `NOT_CHECKED`; `KEPT` needs rows greater than 0 AND a finite positive last close; a clean empty list is `NOT_KEPT`; any exception from the port is `CHECK_FAILED` with a reason word (`EXCEPTION`, `TIMEOUT` for timeout-shaped errors, `PUSHBACK` for 401/403/429-shaped errors which also stop the step: every later symbol is `NOT_CHECKED`, `ERROR_FRAME` when the port reports an error-shaped empty frame); a symbol that does not match the symbol pattern the estate uses (`security_resolution.py` SYMBOL pattern) is refused before any call. The DEFAULT history port builds the real yfinance call WITH EXCEPTIONS RAISED (set `yf.config.debug.hide_exceptions = False` or the argument the installed version supports; read the installed version's behaviour: the measurement says the default hides them) and returns `(date, close)` pairs for `period='1mo'`, `auto_adjust=False`; the module imports yfinance lazily so the module imports without it.
3. **Tests, offline, on fakes (at least 12):** KEPT with rows; a clean empty is NOT_KEPT; an exception is CHECK_FAILED/EXCEPTION and NEVER NOT_KEPT; a timeout-shaped error; a 429-shaped error stops the step and the rest are NOT_CHECKED; the 11th distinct symbol is NOT_CHECKED and its history port is never called (a spy); duplicates call once; the pace (a fake `sleep` records 9 sleeps of 1.0 for 10 symbols, none before the first); non-positive or NaN last close is NOT_KEPT; a bad symbol is refused before any call; the default port without yfinance raises `CHECKER_UNAVAILABLE`; the default port with a fake yfinance module whose `history` hides the error (returns an empty frame) is classified from the error-shaped signal, not as absent (build the fake from what the measurement showed for ALPPL). `before_arm`: the file does not exist at HEAD (record). Then `intake/tests` (370 floor).
4. **One measurement, read-only:** with the REAL default port (if yfinance imports on this box), run the checker once for `TIMXX`, `ALPPL` and `ZZQXJVK` (a nonsense symbol) and record each state, rows, last close, elapsed seconds, and for the two that return no rows whether the client RAISED (now) or returned empty; if yfinance is not importable here, record that and run nothing. No other live call.
5. **Write `r23/YFINANCE_CHECKER.json`:** `read`, `module` {`path`, `sha256`}, `tests` {`added`, `passed`, `failed`, `folders`}, `measurement`, `release_needs`, `claim`, `not_read`.
6. **In your report:** whether yfinance is in the resident and the Lambda, the states for the three symbols, the counts, `release_needs`.

### ACCEPTANCE

<criterion id="AR292-y-AC1" cell_refs="AR-y-292"><invocation>python C:/dev/wk-irpt-anlreq-106/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y292-checker --root C:/dev/wk-irpt-anlreq-106</invocation><expect>Y292-CHECKER-OK</expect></criterion>
`AR292-y-AC1`: the record states whether yfinance is a member of the resident and the Lambda package (file:line), the module with its sha256, at least 12 passing offline tests including the cap, the pace, the raise-as-CHECK_FAILED and the hidden-error frame, and a measurement or the reason none was made.

<criterion id="AR292-y-AC2J" cell_refs="AR-y-292" judgment="true"/>
`AR292-y-AC2J` (judgment, graded at L9, never by you): an exception or error-shaped frame is never read as absent, the 11th symbol is never called, the pace and cap are pinned, KEPT needs history, no dependency was added, every test ran on fakes, and nothing was released.

<expected_criteria>AR292-y-AC1 AR292-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~106/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/intake/yfinance_check.py
infra/aws/lambda/investor-reporting/intake/tests/test_yfinance_check.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23C_Y.md</decomp_doc>
<owned_cells>AR-y-292</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~106/IRPT_ANLREQ.TO-AR-y-292.yfinance-checker-port.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-292`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR292-y-AC1,AR292-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a new source file and test file in a worktree; one read-only yfinance history measurement; nothing is released or applied; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the PRD's C-SWAP and the CTO's rulings (msg 7210) against the cell; the lens: an outage read as absence, a KEPT holding without history, a symbol beyond the cap silently dropped or silently checked, a model in the loop, a live call from a test. The order requires the client to raise, CHECK_FAILED in words, the cap and the 1 s pace pinned, and every test on fakes. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's rulings on the C-SWAP read (msg 7210: 'Cut A to C'; K = 10, 1 s pace, CHECK_FAILED never absent) as workstream `Y` round 25. The grant names every file the cell writes. Base: `AR292-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
