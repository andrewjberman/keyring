# TO IRPT_ANLREQ.TO-AR-y-293.kept-state-freeze-branch-and-page-words -- C-SWAP: a holding the checker KEEPS passes the freeze, and the upload page says so in words

<to_id>IRPT_ANLREQ.TO-AR-y-293</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~110</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-293` (`decompositions/IRPT_ANLREQ_DECOMP_R23C_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~107`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-107` (branch `wk-IRPT_ANLREQ-107`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~107 <0.9.0_WK_IRPT_ANLREQ~107@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W107-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-293`, inlined) -- THE KEPT STATE. Code and tests only; every test on fakes; nothing is released.

**C-SWAP (PRD `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` :104), steps (1) KNOWN and (2) the YFINANCE CHECKER, and the CTO's rulings (msg 7210) on the read `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~99/r23/C_SWAP_STEPS_1_2_READ.json` (cell `AR-y-278`, drained @de81ce19c1):** one pass per unknown holding; a holding the provider (YCharts `securities_info`) answers NOT_FOUND is checked against the registry (step 1) and then with ONE yfinance `history(period='1mo')` call (step 2); rows greater than 0 with a finite positive last close means KEPT (KEEP still requires history). Rulings: **K = 10 unknown symbols checked per upload, one call each, paced at 1 s**; unknowns beyond 10 get the EXISTING proxy prompt, worded 'not checked'; **a yfinance exception, a timeout, or an error-shaped empty frame reads CHECK_FAILED, shown in words and never treated as absent: make the client raise** (yfinance hides exceptions by default and returns an empty frame: MEASURED, ALPPL, BREIT and CCCQ returned 0 rows with no exception, ALPPL printed an HTTP 404 'Quote not found'); a 401, 403 or 429 stops the step for the rest of the upload. No Andrew word is needed for the Yahoo egress: standing law, CLAUDE.md Agent Autonomy ('Egress is open on every channel, except Bloomberg'; 'other vendor APIs need no per-use word'; Andrew-direct 2026-10-09, `ANDREW_DIRECT_20261009_024xZ_LAW_EDIT_*`), which postdates the MDPF_SECHIST addendum's limit: cite it in the record. MEASURED: `TIMXX` returns 20 daily rows, last close 1.0 (a money-market fund): KEPT, no proxy. The registry row and the price landing for a KEPT symbol are MDPF_SECCLASS's and MDPF_SECHIST's (dell1) and are NOT this cell's (the CTO routes them). The withdrawn Kimi model-proposed swap is retired and reverted (@c822052bc4): do not touch `resolution_kimi.py` or `upload_suggestions.py`.
**THE INTERFACE (fixed here so the three cells build in parallel):** a new module `infra/aws/lambda/investor-reporting/intake/yfinance_check.py` (cell B) exposes `class YfinanceChecker(*, history=None, sleep=time.sleep, clock=time.monotonic, cap=10, pace_seconds=1.0)` with `check(symbols) -> dict` mapping each UPPER-CASE symbol to `{'state': 'KEPT' | 'NOT_KEPT' | 'CHECK_FAILED' | 'NOT_CHECKED', 'rows': int, 'last_close': float | None, 'reason': str}`; `history(symbol)` is an injected port returning a list of `(date_iso, close)` pairs and RAISING on any error (the default builds the real yfinance call with exceptions made to raise); `NOT_CHECKED` is a symbol beyond the cap; `CHECK_FAILED` carries a reason word (`EXCEPTION`, `TIMEOUT`, `PUSHBACK`, `ERROR_FRAME`); `NOT_KEPT` is a clean empty answer. The resolver (cell C) consumes it: the resolution result for a symbol the provider answered NOT_FOUND gets a new state `KEPT` (reason `YFINANCE_HISTORY`, `price_source 'yfinance'`, the checker's rows and last close, NO provider receipt) when the checker says KEPT; `CHECK_FAILED` and `NOT_CHECKED` keep the symbol unknown and carry their reason words to the finding.

1. **Read first:** the read record above (`design.kept_holding_to_the_rest_of_the_upload`, `page_words_for_a_kept_holding`, `failure_behaviour`), `infra/aws/lambda/investor-reporting/intake/security_resolution.py` (the resolver, `STATES`, `check`, how a result reaches `portfolio.py`), `intake/portfolio.py` :440-500 (the FOUND gate at :464-471 and TICKER_NOT_FOUND at :477-478), `intake/uploads.py` (`CORRECTION_WORDS`, the notice findings such as SHEETS_NOT_READ, how a finding's `description` and `actions` are made and what the portal shows: the portal shows the server's NOTICE words as they are), `intake/tests/test_correction_words.py` (the words-table lock), and how prices reach a holding (`resolve_prices`, `price_source`). Record `read` {`states_today`, `found_gate` (file:line), `how_notices_reach_the_page` (file:line), `words_lock` (what the lock test pins), `price_for_a_kept_holding` (what a SHARES holding needs and where it would come from: **if the freeze needs a price that only MDPF_SECHIST can supply for the request, STOP at step 3 for SHARES only, file a BLOCKING row naming the file and what is needed, and build KEPT for dollar and weight bases; say so in the record**)}.
2. **The state.** Add the resolution state `KEPT` (reason `YFINANCE_HISTORY`, `price_source 'yfinance'`, rows, last close; NO provider receipt) to the resolver: for a symbol the provider answered NOT_FOUND, ask the checker (THE INTERFACE; inject it as a port the resolver is given, default absent = today's behaviour exactly, so nothing changes until the resident wires it) with the upload's distinct unknown symbols in one batch (so the cap of 10 applies per upload); `KEPT` -> the KEPT result; `NOT_KEPT` -> the NOT_FOUND result unchanged; `CHECK_FAILED` -> the symbol stays unknown and the result carries `check_failed` with the reason word; `NOT_CHECKED` -> unknown, carries `not_checked`. A cached NOT_FOUND must not hide a later KEPT, and a KEPT must not be cached longer than the existing NOT_FOUND TTL (900 s): read the cache code and say what you did.
3. **The freeze branch.** In `portfolio.py` beside the FOUND gate: a KEPT holding passes the gate (it is not TICKER_NOT_FOUND) and is recorded with its identity as given by the client (the holding KEEPS the client's own ticker and name), `price_source 'yfinance'`, `method 'KEPT_BY_HISTORY'`. Everything else about FOUND holdings is byte-identical (the existing portfolio tests all pass unedited).
4. **The page words (server side; the portal already shows NOTICE words as written).** For each KEPT holding, one NOTICE finding with a `description` in plain words, in the style of the existing correction words, for example: `<TICKER> is not in our data provider but has price history, so it is used as it is.`; for a `check_failed` symbol: `<TICKER> could not be checked just now (<reason in words>); name a proxy, or upload again in a few minutes.` and keep the existing proxy actions; for `not_checked` (beyond the cap of 10): `<TICKER> was not checked in this upload (the limit is 10 unknown tickers per upload); name a proxy.` Add the codes to the words table and keep the words-table lock test green by editing it ONLY to include the new codes (list the edit).
5. **Tests, offline, on fakes (at least 14), new file `intake/tests/test_kept_holding.py` plus the lock test edit:** a TIMXX-like symbol with a fake checker KEPT passes the freeze for dollars, shares (if not stopped) and weights; the finding NOTICE words; no TICKER_NOT_FOUND for it; NOT_KEPT stays TICKER_NOT_FOUND exactly as today; CHECK_FAILED stays unknown with its words and NEVER reads as not-found-because-absent; 12 unknown symbols: ten go to the checker, two read 'not checked' (a spy on the checker proves it); no checker injected: byte-identical to today; the cache cases; the client's ticker and name are kept; the FOUND path unchanged. `before_arm`: the KEPT test FAILS at HEAD. Then `intake/tests` (370 floor) with the existing correction-words tests unedited except the one lock edit.
6. **Write `r23/KEPT_STATE.json`:** `read`, `state`, `freeze_branch`, `words` (the three descriptions as written), `tests`, `before_arm`, `shares_status`, `claim`, `not_read`.
7. **In your report:** the three sentences a person sees, the share-pricing status, the counts.

### ACCEPTANCE

<criterion id="AR293-y-AC1" cell_refs="AR-y-293"><invocation>python C:/dev/wk-irpt-anlreq-107/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y293-kept --root C:/dev/wk-irpt-anlreq-107</invocation><expect>Y293-KEPT-OK</expect></criterion>
`AR293-y-AC1`: the record shows the KEPT state, the freeze branch, the three descriptions as written, and whether SHARES holdings are covered; the new test file passes with at least 14 tests whose KEPT case fails at HEAD; the intake folder passes at 370 or more; with no checker injected behaviour is byte-identical.

<criterion id="AR293-y-AC2J" cell_refs="AR-y-293" judgment="true"/>
`AR293-y-AC2J` (judgment, graded at L9, never by you): a KEPT holding keeps the client's own ticker and name, CHECK_FAILED is shown in words and never read as absent, the cap of 10 and the 'not checked' words are pinned, NOT_KEPT is unchanged, no checker means today's behaviour, and nothing was released.

<expected_criteria>AR293-y-AC1 AR293-y-AC2J</expected_criteria>

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-13 ~21:3xZ, after the first worker's stop, rows `IRPT_ANLREQ-D2-W107-S1` and `-S3`; the stop was right).** (S1, the grant) `<paths>` now also names `infra/aws/lambda/investor-reporting/ops/status.py`: the words-table lock (`intake/tests/test_correction_words.py` :44 `uploads.CORRECTION_WORDS == status.CORRECTION_WORDS`) compares the upload door's table with the status envelope's literal copy (`ops/status.py` :86), and `SHEETS_NOT_READ` set the precedent (a new finding code goes in BOTH tables; release 20's `irpt-status` carried its words, words-only by AST). Add EXACTLY the three new entries, copied byte for byte from `uploads.CORRECTION_WORDS`, to the `ops/status.py` literal and change nothing else in that file; prove it: an AST comparison of `ops/status.py` before and after shows only the `CORRECTION_WORDS` dict literal changed, and only by three added keys (print it). The release therefore gains an `irpt-status` leg (record it in `release_needs`). The first worker's source edits are held in its worktree as `r23/KEPT_STATE_SOURCE.patch` (record folder `0.9.0_WK_IRPT_ANLREQ~107/r23/`): apply it (`git apply --check` first), then continue; do not redo the design. (S3, shares) CONFIRMED as scoped by the first worker: a KEPT SHARES holding is NOT covered by this cell; it refuses as the existing `SHARES_PRICE_UNAVAILABLE`, which is the honest answer; say so in `shares_status`; the pricing of a KEPT shares holding from the checker's dated closes is a later cell and a CTO question (issuer). Dollar and weight bases are covered. Build `intake/tests/test_kept_holding.py` (at least 14 tests as the face lists) and keep the intake suite at its floor; the test's count of finding codes (`len(codes) == 30`) becomes 33 by the three new codes: edit it ONLY for that. Your record goes in YOUR folder `deliverables/0.9.0_WK_IRPT_ANLREQ~110/r23/KEPT_STATE.json` (the lane gate refuses a continuation serial under the first worker's folder); the check reads it first. Gate limb that graded this amendment: none stated (the issuer amends its own pending order's grant and text).

**AMENDMENT 2 (issuer `2.0.0_SA_COO~Y2`, 2026-10-13 ~22:0xZ; the same defect as `AR-y-281`'s `W108-S3`, closed before the continuation worker hits it).** `<issued_to>` is now `0.9.0_WK_IRPT_ANLREQ~110`, the continuation worker, who works in the first worker's worktree `C:/dev/wk-irpt-anlreq-107` and commits the code and test paths as `~110`; its record folder is `deliverables/0.9.0_WK_IRPT_ANLREQ~110/`. Nothing else changes. Gate limb that graded this amendment: none stated (the issuer amends its own pending order's assignee).

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~107/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/intake/security_resolution.py
infra/aws/lambda/investor-reporting/intake/portfolio.py
infra/aws/lambda/investor-reporting/intake/uploads.py
infra/aws/lambda/investor-reporting/intake/tests/test_correction_words.py
infra/aws/lambda/investor-reporting/intake/tests/test_kept_holding.py
infra/aws/lambda/investor-reporting/ops/status.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23C_Y.md</decomp_doc>
<owned_cells>AR-y-293</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~107/IRPT_ANLREQ.TO-AR-y-293.kept-state-freeze-branch-and-page-words.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-293`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR293-y-AC1,AR293-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test edits in a worktree; every test on fakes; nothing is released, deployed or called; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the PRD's C-SWAP and the CTO's rulings (msg 7210) against the cell; the lens: an outage read as absence, a KEPT holding without history, a symbol beyond the cap silently dropped or silently checked, a model in the loop, a live call from a test. The order requires the client to raise, CHECK_FAILED in words, the cap and the 1 s pace pinned, and every test on fakes. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's rulings on the C-SWAP read (msg 7210: 'Cut A to C'; K = 10, 1 s pace, CHECK_FAILED never absent) as workstream `Y` round 25. The grant names every file the cell writes. Base: `AR293-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
