# TO-AR-g-63 -- the portfolio level series: one pure module that turns per-security price rows into the [epoch_ms, level] pairs the priced layout reads, by the layout's own buy-and-hold arithmetic

<to_id>IRPT_ANLREQ.TO-AR-g-63</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~175</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-63` (`decompositions/IRPT_ANLREQ_DECOMP_R9_G.md`) |
**outcome_ref:** FWD-7 (C-PRICES) | **depends_on:** none (it consumes the SHAPE of `price_source.py`'s rows, merged).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~175`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-175` (branch `wk-IRPT_ANLREQ-175`), provisioned by the issuer. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~175 <0.9.0_WK_IRPT_ANLREQ~175@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W175-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.

### Read first (under `C:/dev/wk-irpt-anlreq-175/infra/aws/lambda/investor-reporting/ycharts/research/`)

- `layout_overview.py` lines 386-410 (`_series_points`, `_asof`), 517-527 (`_buy_and_hold_path`: V(t) = sum of amount_i * series_i(t) / series_i(t0) on the union of observation times from the common start t0) and 595-606 (`_compute_own_series`). Your module must follow that arithmetic, in the shape below, and must not import `layout_overview`.
- `price_source.py` (merged): `resolve_prices(...)["series"][SYMBOL]["rows"]` is `[[date_str, price], ...]` ascending. Your module's input is those rows.
- `tests/test_price_source.py` for the test style.

### THE CELL (`AR-g-63`, inlined)

The priced Overview reads each portfolio-level figure (returns, risk) from ONE series, a list of `[epoch_ms, level]` pairs, ascending, at least two. No
estate store holds a portfolio series; it must be BUILT from the holdings' own price rows by buy-and-hold. This cell builds that step as one pure module.
It reads no store and calls no vendor. The compose cell of a later round wires it between `price_source` and the layout.

**Build a NEW file `infra/aws/lambda/investor-reporting/ycharts/research/portfolio_series.py`** with exactly this contract.

1. `to_epoch_ms(day)`: `day` a `str` `YYYY-MM-DD` that is a real calendar date -> the integer milliseconds since 1970-01-01 of that date at 00:00 UTC
   (`1970-01-01` -> 0). Anything else (not a `str`, wrong shape, `2026-13-45`, blank) raises `ValueError("SERIES_DATE")`.
2. `to_pairs(rows)`: `rows` an iterable of `(date_str, price)` (or two-item lists). Returns `[[epoch_ms, float(price)], ...]` ascending by `epoch_ms`. A row is dropped if
   the date is not a real date string, or the price is not an `int`/`float` (not a `bool`), not finite, or `<= 0`. If a date repeats, the LATER value given wins.
3. `buy_and_hold(series_by_ticker, amounts)`: `series_by_ticker` maps ticker -> pairs as `to_pairs` returns (ascending); `amounts` maps ticker -> number.
   - An amount that is not a finite `int`/`float` (not a `bool`) `> 0` is ignored and named: excluded with reason `"BAD_AMOUNT"`.
   - A ticker with a positive amount and no series (absent or empty) is excluded with reason `"NO_SERIES"`.
   - Over the tickers left, `t0` is the LATEST first timestamp. Each ticker's base is its value as of `t0` (the last observation at or before `t0`); a base `<= 0` excludes
     the ticker with reason `"BAD_BASE"` and `t0` is recomputed over the tickers still in.
   - The observation times are the sorted union of the used tickers' timestamps that are `>= t0`. At each time `t`, `V(t) = sum over used tickers of amount * asof(t) / base`,
     where `asof(t)` is the ticker's last observation at or before `t`. The level is `100 * V(t) / V(t0)`, so the first pair is exactly `100.0`.
   - Returns a `dict`: `{"status": "OK"|"TOO_SHORT"|"NO_SERIES", "pairs": [[ms, level], ...], "used": [sorted tickers], "excluded": [{"ticker", "reason"}, ...] sorted
     by ticker then reason, "coverage": float, "t0": ms or None}`. `coverage` is the sum of the used tickers' amounts over the sum of ALL positive amounts (0.0 when none used).
     `NO_SERIES`: no ticker used (pairs `[]`, `t0` None). `TOO_SHORT`: fewer than two pairs (pairs `[]`, `used` and `t0` still given). Otherwise `OK`.
   - The inputs are not changed.
4. `named_series(pairs, key)`: returns `{"series": pairs, "key": key}` when `pairs` is a list of at least two pairs and `key` is a non-blank `str`; else `None`. (The layout's
   benchmark and risk-free inputs take this shape.)
5. **The module is pure and stdlib-only:** it imports nothing but `math`, `datetime`, `re`, `bisect`, `collections`, `typing`, `calendar` (and `__future__`); it opens no file,
   makes no connection, reads no environment variable, and has no `print`.

**Tests.** A NEW file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_portfolio_series.py` with at least 8 tests, offline, with hand-computed expected values: the epoch
conversion and its refusals; `to_pairs` dropping bad rows and keeping the later repeated value; two tickers with a common start (level 100, 105, 115 for amounts 100/100, prices
A 10/11/12 and B 20/20/22); a later start moving `t0`; the union of times with as-of carry; amount weighting; the typed exclusions and `coverage`; `NO_SERIES` and `TOO_SHORT`;
inputs unchanged; `named_series`.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR63-g-AC1" cell_refs="AR-g-63"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g63_checks.py g63</invocation><expect>^AR-G63-OK</expect></criterion>

<criterion id="AR63-g-AC2" cell_refs="AR-g-63"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g63_checks.py hygiene</invocation><expect>^AR-G63-HYGIENE-OK</expect></criterion>

<expected_criteria>AR63-g-AC1,AR63-g-AC2</expected_criteria>

- AC1 imports `portfolio_series`, asks it twelve cases with hand-computed values (the contract above, item by item), then runs your test file (0 failed, at least 8 passed). At base it FAILs (no module).
- AC2 reads the module's bytes: ASCII only, only the allowed imports, no `open`, `print`, `exec`, `eval`. At base it FAILs (no module).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs. Nothing outside the two new files, your deliverable folder, this order's status flip and the channel file is edited.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/portfolio_series.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_portfolio_series.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~175/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-63.portfolio-series-buy-and-hold-core.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R9_G.md</decomp_doc> round 9, workstream ~G, cell `AR-g-63`.
<owned_cells>AR-g-63</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR63-g-AC1, AR63-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~175/IRPT_ANLREQ.TO-AR-g-63.portfolio-series-buy-and-hold-core.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-63`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR63-g-AC1,AR63-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the module's function names with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the module is NEW and imported by nothing; the compose cell of a later round is its first importer. Nothing deployed, so no edge is changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read the cell against `_buy_and_hold_path` (layout_overview.py 517-527) and the engine compose read (AR-g-54 record, q1: no estate store holds a portfolio series). Traps: a level not normalised to 100 at t0; t0 taken as the earliest start (a ticker not yet trading enters at its own first price and distorts the path); a ticker carried forward from before t0 instead of as-of t0; a zero base dividing; amounts treated as shares; a bool taken as a number. The checker feeds a green arm (a reference build passes all twelve cases) and a mutant arm (level left un-normalised fails four cases). NOT seen (blind): the layout's statistics over real series.
</preflight>

- Cut on AR-g-54's record (`deliverables/0.9.0_WK_IRPT_ANLREQ~173/r7/ENGINE_COMPOSE_READ.json`, q1) and CTO msg 8377. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed.
- Base: `AR63-g-AC1` and `AC2` FAIL as expected (no module).
