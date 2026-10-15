# TO-AR-g-88 -- the layout works out an OWN_SERIES element that names `columns` and no single statistic, so the Periodic Return, Drawdown and Cumulative-bars elements print values instead of STATISTIC_UNKNOWN

<to_id>IRPT_ANLREQ.TO-AR-g-88</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~188</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-88` (`decompositions/IRPT_ANLREQ_DECOMP_R16_G.md`) |
**outcome_ref:** FWD-7 (the report's priced figures) | **depends_on:** `AR-g-86` (merged `1c84d38bf4`, the price stage that supplies the series).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~188`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-188` (branch `wk-IRPT_ANLREQ-188`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/` and `org/missions/D9/IRPT` on disk (it has no portal sub-worktree; your cell does not touch the portal). Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~188 <0.9.0_WK_IRPT_ANLREQ~188@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W188-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`).

### Read first (under `C:/dev/wk-irpt-anlreq-188/infra/aws/lambda/investor-reporting/ycharts/research/`)

- `layout_overview.py`: `compute_element` (line 755), `_compute_own_series` (595), `statistic_of` (477) with `_STATS` (222) and `_NA` (240), `_element_html` (1040), `_table_html` (1013), `_series` (985), `_fmt` (975).
- `tests/test_layout_overview.py` (how it builds a kept answer and an element) and the three real elements in `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json`: ids `p2.e08` (kind chart), `p2.e13` and `p6.e22` (kind table). Each has `computed` `OWN_SERIES`, a list `columns` of statistic ids, and `statistic` null. You do NOT change the map.

### THE CELL (`AR-g-88`, inlined)

Three elements of the Overview map ask for several statistics over the portfolio's own level series (`columns`: `total_return_1m` ... `total_return_15y` for `p2.e08` and `p2.e13`, `max_drawdown_1y` ... `max_drawdown_all` for `p6.e22`), but `_compute_own_series` reads only the single `statistic`, which is null on those elements, so each one prints `STATISTIC_UNKNOWN:None` even when the series is there. This cell makes the layout work out the columns. The renderer already takes a dict for a table (`_table_html`) and a list of numbers for a chart (`_series`).

**`layout_overview.py`, exactly this:**
1. `compute_element` records the element's kind in the accumulator: `acc = {"inputs": set(), "coverage": 0.0, "kind": element.get("kind")}`.
2. In `_compute_own_series`, after `acc["coverage"] = 1.0`: `columns = src.get("columns")`; when `src.get("statistic")` is falsy AND `columns` is a non-empty list, `return _column_statistics(pts, columns, acc.get("kind"), acc)`. Otherwise the function ends as it does today: a named statistic still wins over `columns`, and no columns with no statistic still reads `STATISTIC_UNKNOWN:None`.
3. A module constant `COLUMN_NA = "n/a"` and two new functions placed after `_compute_own_series`:
   - `_column_label(column)`: `stat, _, period = str(column).rpartition("_")`; the label is `stat` with `_` replaced by a space and capitalised, a space, then `period` upper-cased, except that the period `all` stays `all`. Examples: `total_return_1m` -> `Total return 1M`; `total_return_ytd` -> `Total return YTD`; `max_drawdown_all` -> `Max drawdown all`.
   - `_column_statistics(pts, columns, kind, acc)`: for each column in order, `statistic_of(pts, column, acc.get("benchmark"), acc.get("risk_free"))`; an `_NA` raised for one column makes that column `None` and the FIRST such `_NA` is remembered. If no column could be worked out, re-raise the remembered `_NA` (the element is then NOT_AVAILABLE with that first column's own reason). Otherwise set `acc["coverage"]` to the number of columns worked out divided by the number of columns, and: when `kind == "table"`, return a dict `{_column_label(column): value, ...}` in column order with the string `COLUMN_NA` for a column that could not be worked out; for any other kind, return the list of the values that could be worked out, in column order.
4. Nothing else changes: not the map, not `statistic_of`, not the renderer, not `compute_all`, not `build`.

**Tests.** A NEW file `ycharts/research/tests/test_layout_own_series_columns.py`, offline, with these exact test function names (the checker looks for each by name). Use a made-up monthly level series (the 14th of each month from 2024-07-14 to 2026-10-14, level `100 * 1.01 ** k`, as `[epoch_ms, level]` pairs in a kept answer under the call name `portfolio_level_series`), and build the element and call `layout_overview.compute_element(element, kept, run_doc, None, None, {"portfolio_level_series"}, None, None, True)` as `tests/test_layout_overview.py` does:
`test_table_columns_give_labelled_values_and_na_for_a_column_the_series_is_too_short_for` (values hand-computed: the 1M value is 1.0, the 3M value `(1.01 ** 3 - 1) * 100`, the 1Y value `(1.01 ** 12 - 1) * 100`; the 3Y column is `"n/a"` because the series is 27 months long; the coverage is the share worked out), `test_chart_columns_give_the_worked_out_values_in_column_order`, `test_every_column_unworkable_is_the_first_columns_reason` (a two-point series four days long: reason `SERIES_TOO_SHORT`), `test_drawdown_columns_label_the_whole_series_column` (a series with one month of -10 percent: the 1Y and `all` columns are -10.0), `test_a_named_statistic_still_wins_over_columns`, `test_no_columns_and_no_statistic_is_still_statistic_unknown` (`columns` absent and `[]`), `test_pricing_off_is_still_not_in_this_version`, `test_the_page_prints_the_labelled_rows_and_the_na_cells` (`layout_overview._element_html(element, {}, layout_overview._palette({}), computed={id: result}, map_calls={"portfolio_level_series"}, pricing=True)` contains the labels, not the raw ids, and the `n/a` cells).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR88-g-AC1" cell_refs="AR-g-88"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g88_checks.py g88</invocation><expect>^AR-G88-OK</expect></criterion>

<criterion id="AR88-g-AC2" cell_refs="AR-g-88"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g88_checks.py regress</invocation><expect>^AR-G88-REGRESS-OK</expect></criterion>

<expected_criteria>AR88-g-AC1,AR88-g-AC2</expected_criteria>

- AC1 asks the layout ten things with hand-computed values (a table of columns, a chart of columns, the all-unworkable case, the drawdown labels, a named statistic winning, no columns, pricing off, the printed page, and the three real map elements), then checks the eight named tests exist and pass. At base it FAILs.
- AC2 runs six existing test files one at a time (121 tests: the layout, the commentary, the producer, the held data, the map PDF, the series) and needs all of them to pass. At base it PASSes. Run it under `timeout 300`.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_own_series_columns.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~188/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-88.layout-multi-column-series-statistics.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R16_G.md</decomp_doc> round 16, workstream ~G, cell `AR-g-88`.
<owned_cells>AR-g-88</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR88-g-AC1, AR88-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~188/IRPT_ANLREQ.TO-AR-g-88.layout-multi-column-series-statistics.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-88`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR88-g-AC1,AR88-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the functions you changed or added with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `_compute_own_series` is reached through `compute_element` from `compute_all`, `build` and the command line of `layout_overview.py` (YCharts path) and from `opal_producer` (Opal path). Today an `OWN_SERIES` element with `columns` and a null statistic ends in `STATISTIC_UNKNOWN:None` on both paths; after the change it prints values on both, which is the intended repair, and an element with a named statistic or with no columns is untouched. No other element kind reaches the new code. The map is unchanged, so no pin moves. Nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against the compose read (ENGINE_COMPOSE_READ.json, the map statistic defect p2.e08 / p2.e13 / p6.e22). Traps: a column the series is too short for printed as zero or dropped without a mark (a 15-year return shown for a 2-year series); the raw statistic id printed as the row label; a named statistic overridden by `columns`; a wrong coverage; the chart given a dict (the renderer then prints "not a readable series"); the all-unworkable case returning an empty value instead of the element's own reason; the pricing-off element no longer NOT_IN_THIS_VERSION. The checker feeds a green arm (a reference build passes all ten cases, the eight named tests and the 121 regress tests) and seven mutant arms (raw ids as labels: 3 cases fail; unworkable columns dropped: 3; coverage constant 1.0: 2; columns override the statistic: 1; chart given a dict: 2; all-unworkable returns {}: 1; period not upper-cased: 3).
</preflight>

- Cut on the compose read's map statistic finding (`ENGINE_COMPOSE_READ.json`) and the reference build run by the issuer. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR88-g-AC1` FAILs and `AR88-g-AC2` PASSes (121), as expected.
- The read proposed changing the map bytes (one statistic per element, or a split per column), which moves the pinned map; reading `columns` in the engine leaves the map and its pin alone.
