# TO-AR-g-83 -- the Yahoo price adapter: the daily total return from the as-traded Close, the ex-date dividends and the splits, chained to a base-100 level series

<to_id>IRPT_ANLREQ.TO-AR-g-83</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~183</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-83` (`decompositions/IRPT_ANLREQ_DECOMP_R12_G.md`) |
**outcome_ref:** FWD-7 (C-PRICES) | **depends_on:** `AR-g-80` (merged `f089142e91`, `tr_level.py`) and `AR-g-69` (merged `d1de2f0cd6`, the read that fixed the one formula).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~183`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-183` (branch `wk-IRPT_ANLREQ-183`), provisioned by the issuer with the whole of `infra/`, `docs/` and `data/` on disk. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~183 <0.9.0_WK_IRPT_ANLREQ~183@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W183-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree. `pandas`, `pyarrow` and `yfinance` may be absent from this box: a test that needs one skips with `pytest.importorskip`, never fails.

### Read first (under `C:/dev/wk-irpt-anlreq-183/`)

- `infra/aws/lambda/investor-reporting/ycharts/research/tr_level.py` (merged; the ONE formula: `chain_levels(daily_returns, base=100.0)` and `returns_from_levels(pairs)`) and `infra/aws/lambda/investor-reporting/ycharts/research/price_source.py` (the chain core that will call your reader as `reader(symbol, start, end)`), with their tests under `infra/aws/lambda/investor-reporting/ycharts/research/tests/`.
- The facts record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~176/r9/PRICE_ADAPTER_FACTS.json`: `q2` (the formula for each source) and `q4` (the four adapter shapes).
- `data/mdpf/scripts/demque/yahoo_pull.py` (`_default_fetch` lines 72-74: `history(..., auto_adjust=False, actions=True)`; `pull()` line 107 and lines 141-147: `as_traded_close` undoes every split dated STRICTLY AFTER the row) and `data/mdpf/scripts/demque/tr_compare.py` (`daily_tr` line 36 and `as_traded_dividends` line 60: Yahoo serves dividends split-adjusted; undo every split dated strictly after the ex-date). NOT importable on the host; re-write the logic.

### THE CELL (`AR-g-83`, inlined)

Andrew's rule: prices are TOTAL RETURN. The price chain (`price_source.resolve_prices`) asks each source for a level series through `reader(symbol, start, end)`; every reader hands back `(date_str, level)` on the same footing: `level = 100` at the first retained date and `level_t = level_(t-1) * (1 + r_t)` with `r_t` that source's DAILY total-return fraction, built by `tr_level`. This cell builds yfinance adapter. It takes its client as an argument and makes no call at import.

**Build a NEW file `infra/aws/lambda/investor-reporting/ycharts/research/price_adapter_yfinance.py`** with exactly this contract.

1. The module exposes `make_reader(*, fetch=None, yf=None)` and NO other public name. It returns `reader(symbol, start, end)`: `symbol` is any str (strip blanks, upper-case it, and pass that to the fetch); `start` and `end` are inclusive `YYYY-MM-DD` strings. The reader returns a list of `(date_str, level)` tuples, ascending by date, `level` a `float`, `[]` when no row is usable in the window.
2. `fetch(symbol)` returns the SERVED rows, a list of dicts with `date` (a `YYYY-MM-DD` str), `Close`, `Dividends`, `Stock Splits`. Yahoo SERVES `Close` and `Dividends` split-adjusted, so before the formula the reader makes them as-traded: for a row dated `d`, `factor(d)` is the product of every split ratio dated STRICTLY AFTER `d` (a ratio counts only if it is a finite number above zero; the splits come from ALL fetched rows, including a row whose Close is unusable and including rows after `end`); `P(d) = Close * factor(d)` and `D(d) = Dividends * factor(d)`. A `Dividends` value that is `None`, NaN or not a number counts as `0.0`; a `Stock Splits` value that is `None`, NaN, `0` or not a finite number above zero counts as ratio `1.0`.
3. Rows are sorted ascending by `date`. A row is usable only if `Close` is a finite number above zero (not a `bool`). Cut the usable rows to `start <= date <= end`, then compute the daily return of each usable row after the first as `r_t = (P_t + D_t) / (P_prev / s_t) - 1` where `P_prev` is the previous USABLE row's as-traded close in the window and `s_t` is the split ratio on `t` (1.0 when none). A bad row between two good rows is dropped and the next return spans the gap. The FIRST usable row gets `r = 0.0` (its own move is not applied). Chain with `tr_level.chain_levels` (`import tr_level`, a bare import) and return the pairs as tuples. `Adj Close` is never used.
4. When `fetch` is `None` the default fetch is used: `yfinance` is imported INSIDE the default-fetch function only (or the `yf` argument is used when given, as `yf.Ticker(symbol)`), then `.history(period="max", auto_adjust=False, actions=True)`; the frame goes through `.reset_index().to_dict("records")`; each record's `Date` becomes `date` with `.strftime("%Y-%m-%d")` when it has `strftime`, else `str(value)[:10]`; the other three columns pass through under the names above. No other keyword is passed to `history`.
5. A fetch error propagates unchanged (the chain types it); nothing is caught or invented, and no error text is stored or logged.
6. The module is stdlib-only at the top level (`__future__`, `math`, `re`, `datetime`, `collections`, `typing` and `tr_level`); it opens no file, prints nothing, reads no environment variable.

**Tests.** A NEW file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_adapter_yfinance.py` with at least 6 tests, offline, with hand-computed values (made-up dates and numbers): the first row seeding the base and later rows chaining the daily return; a dividend adding to the day's return; a served split-adjusted Close with a 2-for-1 split (D1 served 50 is 100 as traded, the D2 return is +2 percent); a served dividend dated before a later split undone to as-traded; a zero, NaN or missing split ratio counting as 1; a bad Close row dropped with the next return spanning the gap; the window cut before chaining; the symbol stripped and upper-cased before the fetch; a fetch error propagating; and the `yf` seam with a fake `Ticker` whose `history` asserts `auto_adjust` is `False` and `actions` is `True`.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR83-g-AC1" cell_refs="AR-g-83"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g8x_checks.py g83</invocation><expect>^AR-G83-OK</expect></criterion>

<criterion id="AR83-g-AC2" cell_refs="AR-g-83"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g8x_checks.py hygiene83</invocation><expect>^AR-G83-HYGIENE-OK</expect></criterion>

<expected_criteria>AR83-g-AC1,AR83-g-AC2</expected_criteria>

- AC1 imports `price_adapter_yfinance`, asks it 10 direct cases with hand-computed values (the contract above, item by item), then runs your test file (0 failed, at least 6 passed). At base it FAILs (no module).
- AC2 reads the module's bytes: ASCII only, top-level imports only the allowed standard library names and `tr_level`, nested imports only `pandas`, `pyarrow`, `yfinance`, `io`, `json`, `time`, no `open`, `print`, `exec`, `eval`. At base it FAILs (no module).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs. The module is NEW and imported by nothing yet; do not import it from any other file.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/price_adapter_yfinance.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_adapter_yfinance.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~183/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-83.yfinance-price-adapter.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R12_G.md</decomp_doc> round 12, workstream ~G, cell `AR-g-83`.
<owned_cells>AR-g-83</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR83-g-AC1, AR83-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~183/IRPT_ANLREQ.TO-AR-g-83.yfinance-price-adapter.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-83`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR83-g-AC1,AR83-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the module's function names with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the module is NEW and imported by nothing; the price chain's wiring cell (a later cut) is its first importer. Nothing deployed, so no edge is changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change in this cell (the grant questions for the host are recorded in the decomposition and stay with the CTO and CloudOps).
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against the price-adapter facts record (q2, q4). Traps: Adj Close used (a dividend counted twice); a split-adjusted Close treated as as-traded (a phantom 50 percent loss on a split day); the dividend not undone for a later split; a NaN split read as a real ratio; the window applied before the factors (a split after the window ignored); the first row's own return applied. The reference build passes all cases; a mutant that drops the dividend fails two.
</preflight>

- Cut on the AR-g-69 record (`q2`, `q4`) and CTO msg 8377. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR83-g-AC1` and `AC2` FAIL as expected (no module).
- One of four independent adapter cells (`AR-g-81` to `AR-g-84`), each its own file pair; they share only `tr_level`.
