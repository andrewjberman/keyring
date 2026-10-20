# TO-AR-g-173 -- the comparison record (K2): the common window, the rebased paths, the returns, the risk figures and the side-by-side allocation

<to_id>IRPT_ANLREQ.TO-AR-g-173</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~330</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-173` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** AR-g-171 (the earlier order of the same queue; this cell does not call it). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~330`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-330` (branch `wk-IRPT_ANLREQ-330`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~330 <0.9.0_WK_IRPT_ANLREQ~330@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W330-S<k>` (check the channel file for `W330` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **You are the one worker of chain A (queue 171, 173, 174, 175, in that order).** The commits of your earlier orders are on this branch and their files are in this worktree; a later order builds on them. You are handed one order at a time.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py` (read it; you cannot edit it). It builds its own deterministic fixtures and computes every expected number itself, independent of your code: if your number and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both numbers, and stop on that criterion.

### THE CELL (`AR-g-173`, inlined)

Directory `RES` = `infra/aws/lambda/investor-reporting/ycharts/research/`; `TESTS` = its `tests/` folder. Create two files; edit nothing else. Your earlier order (AR-g-171) put `model_source.py` on this branch; this cell does NOT call it (the series arrive as arguments), so it can be tested on fixtures.

**Why.** FWD-10: the report must show how the portfolio did against each comparable it was compared with, over ONE common window, computed by Opal from prices and held data (PRD FWD-10). This module is the pure arithmetic: it takes level series and returns a record. The statistic engine already exists in `RES/layout_overview.py` (`statistic_of`, `_risk_stat`, `_month_returns`, `_sample_var`, `_dt`, `_ms`, `_shift_months`, `_asof`): import it as `layout_overview as lo` and reuse those helpers where they fit; do not copy their code and do not change that file.

**1. `RES/comparables.py`** (no network, no clock, no AWS). Define:

`build_compare(portfolio, comparables, benchmark, risk_free)` -> the record below.
- `portfolio = {"name": str, "series": [[epoch_ms, level], ...]}`; each `comparables` item `{"key": str, "name": str, "kind": "model"|"ticker", "series": [[epoch_ms, level], ...] | None, "reason": str | None}`; `benchmark` and `risk_free` are `[[epoch_ms, level], ...]` or `None`. A series is sorted ascending; levels are positive.
- **Rows.** Row 0 is the portfolio (`"key": "portfolio"`, `"kind": "portfolio"`). Then one row per comparable in the order given. A comparable whose `series` is `None` or has fewer than 2 points is `"status": "NOT_AVAILABLE"` with `"reason"` = its own `reason` (or `"no series was available for it"` when none), `"path": []`, every `returns` value `None`, `"risk"` = `{"years": None, "std_dev": None, "sharpe": None, "sortino": None, "max_drawdown": None, "alpha": None, "beta": None}`. It is left OUT of the window computation. Every other row is `"status": "VALUE"`, `"reason": None`.
- **Window.** `start` = the LATEST first observation among the portfolio and every VALUE comparable; `end` = the EARLIEST last observation among them. `window = {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD", "years": months / 12.0, "rule": <one sentence>}` where `months` = whole calendar months between the two dates (month index difference, minus 1 when the end's day-of-month is earlier than the start's). The `rule` sentence says, in plain words, that the window starts at the latest first observation and ends at the earliest last observation among the portfolio and the comparables that have a price series, and that every line is rebased to 100 at the start.
- **Path.** For each VALUE row: `path` = its points from `start` on, as `[epoch_ms, level / base * 100.0]` where `base` is the row's last level at or before `start`. The first path point is exactly 100.0.
- **Returns.** `returns` = `{"1m","3m","ytd","1y","3y","5y","10y"}` -> percent, from `lo.statistic_of(path_points, "total_return_<p>")` on the row's path (as `(ms, level)` tuples); a period longer than the path (the helper raises `lo._NA`) is `None`.
- **Risk.** `years` = `min(5, floor(window.years))` as an int, or `None` when `floor(window.years) < 1` (then every risk value is `None`). Otherwise, over the last `years` whole years of the row's path (monthly returns from month-end levels, exactly as the layout's `_month_returns` takes them): `std_dev` = sample standard deviation x sqrt(12) x 100 (percent); `sharpe`, `sortino`, `alpha` (percent), `beta` as the layout's `_risk_stat` computes them (it takes `years`, the end timestamp, the end datetime, `benchmark` and `risk_free` as `(ms, level)` tuple lists); `max_drawdown` = the largest peak-to-trough fall of the path over those same `years` years, in percent (negative or 0), starting from the path's value at the start of that span. `benchmark` / `risk_free` is `None` -> `alpha`, `beta` (benchmark) and `sharpe`, `sortino`, `alpha` (risk-free) are `None`; `std_dev` and `max_drawdown` stay. A statistic the helper cannot work out (`lo._NA`) is `None`.
- Record: `{"window": {...}, "rows": [{"name","key","kind","status","reason","path","returns","risk"}, ...]}` exactly those keys; `risk` has the keys `years, std_dev, sharpe, sortino, max_drawdown, alpha, beta`.

`build_allocation(portfolio, comparables)` -> `{"classes": [...], "rows": [...]}`.
- `portfolio = {"name": str, "weights": {class_name: percent}}`; each comparable `{"name", "kind", "weights": {class_name: percent} | None, "asset_class": str | None, "as_of": str | None, "reason": str | None}`.
- Normalise every class name: replace `_` with a space and title-case it (`fixed_income` and `Fixed Income` both -> `Fixed Income`; `equity` -> `Equity`).
- A `model` comparable with `weights` uses them. A `ticker` comparable with an `asset_class` gets `{that class: 100.0}`. Any other comparable (no weights and no asset class) is a gap: its row has `"weights": None`, `"basis": None`, `"reason"` = its `reason` (or `"no allocation was available for it"`).
- `classes` = the classes in which ANY row holds a non-zero weight, in the canonical order Cash, Fixed Income, Equity, Hedge, Structured, Commodities, Alternatives, then any other class name alphabetically. Every row with weights lists a float for EVERY class in `classes` (0.0 when absent).
- Row keys: `name, weights, as_of, basis, reason`. `basis`: the portfolio `"Accepted holdings, by amount"`; a model `"Model positioning as of <as_of>"` (with its `as_of` date); an ETF `"100 percent in its classified asset class"`. The portfolio row is first, then the comparables in order.

**2. `TESTS/test_comparables.py`** (pytest, your own proof; offline): a window from a late-starting model series; the path rebased to exactly 100.0; returns with `None` for periods longer than the window; risk over `floor(years)` years against a hand computation on a small series; a comparable with no series left out of the window and stated; no benchmark and no risk-free; a window under one year; `build_allocation` for a model, an ETF and a gap row, class order and zero-fill.

1. Write the two files. 2. Run your tests and the three criteria. 3. Commit the code and tests (one commit), then the proof and the status flip as separate commits. 4. Report.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR173-g-AC1" cell_refs="AR-g-173"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py 173 build</invocation><expect>^AR-CMP-173-OK</expect></criterion>

<criterion id="AR173-g-AC2" cell_refs="AR-g-173"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py 173 guard</invocation><expect>^AR-CMP-173-OK</expect></criterion>

<criterion id="AR173-g-AC3" cell_refs="AR-g-173"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py 173 regress</invocation><expect>^AR-CMP-173-REGRESS-OK</expect></criterion>

<expected_criteria>AR173-g-AC1,AR173-g-AC2,AR173-g-AC3</expected_criteria>

- AC1: `build_compare` and `build_allocation` return the record the checker computes itself from its own fixtures (window 2024-04-14 to 2026-10-14, 2.5 years, risk over 2 years). At base it FAILs (the module does not exist).
- AC2: no existing element of the Overview, Multi or Comparison report moves. At base it PASSes.
- AC3: the existing test files plus your own pass, and the branch changed only the files of the cells so far. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/comparables.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_comparables.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~330/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-173.compare-record-and-allocation-arithmetic.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-173`.
<owned_cells>AR-g-173</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR173-g-AC1,AR173-g-AC2,AR173-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~330/IRPT_ANLREQ.TO-AR-g-173.compare-record-and-allocation-arithmetic.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-173`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR173-g-AC1,AR173-g-AC2,AR173-g-AC3` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `comparables.py` is a new member of the resident package; nothing calls it until AR-g-175; no deploy or AWS call.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change in this cell (the grant is AR-g-172).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: 173 build FAIL (no module), guard PASS, regress PASS, calibrate OK (the checker's total return, std dev, Sharpe, Sortino, alpha, beta and max drawdown agree with `statistic_of` to 1e-7). Traps: the window is the LATEST start and EARLIEST end; risk years are whole years of the common window, not 3y; a comparable with no series must not move the window. NOT seen (blind): real daily model data (the series here are monthly).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1 FAILs, AC2 PASSes, AC3 PASSes.
