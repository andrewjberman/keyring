# TO-AR-g-164 -- the Opal-built report's price pages, part 2: the series forms (cumulative return, drawdown path, calendar-year returns, benchmark chart) (row 3c22; CTO msgs 10729, 10734, 10743)

<to_id>IRPT_ANLREQ.TO-AR-g-164</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~302</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>57</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-164` (`decompositions/IRPT_ANLREQ_DECOMP_R57_G.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none. A second order for the same worker (`AR-g-165`, text elements) follows on the same chain after this one. Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~302`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-302` (branch `wk-IRPT_ANLREQ-302`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~302 <0.9.0_WK_IRPT_ANLREQ~302@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W302-S<k>` (take the next free `<k>`; check the channel file for `W302` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Do not touch anything outside the `<paths>` block. Run Python with plain `python` (the producer's tests need `pypdf`, which `python -I` cannot see).

### THE CELL (`AR-g-164`, inlined)

**AMENDMENT 1 (issuer, 2026-10-19, on worker ~302's row IRPT_ANLREQ-D2-W302-S1; gate limb: none graded, an in-decomposition amendment of a grant):** `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py` line 754 pins the number of `OWN_SERIES` elements of the real map: `assert len(res) == len(series) == 9`. Your cell adds 5, so it must read `14` on YOUR branch (the three round-57 cells that add `OWN_SERIES` elements each move it by their own delta, 163 by 8, 164 by 5, 165 by 4; the issuer reconciles the line to 26 at the merge). That file is now in your `<paths>`. Change ONLY that number (and, if the line wraps, nothing else); do not weaken the assertion, do not touch any other line of the file. Then re-run AC3.

Files: `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py` (read it first: `statistic_of` at about line 477 is the statistic engine; `_compute_own_series` at about line 595 feeds it the buy-and-hold level series `points` [(ms, level)] plus `acc["benchmark"]` and `acc["risk_free"]` named series, and `acc["kind"]` the element kind; `_column_statistics` shows how a table gets `{label: value}` and a chart gets a list; `_chart_svg` renders a list of numbers or of `[x, y]` pairs; `_table_html` renders a dict) and `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json`.

Five map elements read NOT_IN_THIS_VERSION with pricing on. Re-point each `source` to `OWN_SERIES` (copy the shape of the existing `p7.e05`: `{"call": "portfolio_level_series", "columns": [], "computed": "OWN_SERIES", "field": "$.chart_data[0][0].raw_data", "sleeve": null, "statistic": "<name>"}`) and give the engine the three statistics it lacks. The statistic name goes in `source.statistic`:

| element | kind | statistic | the value it must return |
|---|---|---|---|
| `p2.e04` Cumulative Return chart | chart | `cumulative_series` (EXISTS: `statistic_of` already returns `[[ms, level], ...]`) | map re-point only |
| `p6.e21` Drawdown Info chart | chart | `drawdown_series` (NEW) | `[[ms, pct], ...]`, one pair per input point, `pct = (level / running_peak_so_far - 1) * 100` (so 0 at a new high, negative below it) |
| `p2.e18` Annual Return table | table | `annual_returns` (NEW) | a dict `{"2017": pct, "2018": pct, ..., "YTD": pct}` (below) |
| `p2.e17` Annual Return chart | chart | `annual_returns` (the same) | the SAME numbers as a list, the calendar years in ascending order then YTD (below) |
| `p7.e15` Benchmark level series chart | chart | `benchmark_series` (NEW) | `[[ms, level], ...]` of the benchmark named series `acc["benchmark"]` (the proxy SPY); `_NA("INPUT_MISSING:benchmark")` when absent |

`annual_returns` (use the layout's own convention for YTD, `_window_start(points, end_dt, "ytd")`, the last level at or before 31 December of the prior year): for each calendar year Y from the first year of the series up to but not including the year of the last point, include `str(Y)` when a level exists at or before 31 December of Y-1 AND at or before 31 December of Y; its value is `(level_at_or_before_31Dec_Y / level_at_or_before_31Dec_Y-1 - 1) * 100`. Then `"YTD"`: the last level over the level at or before 31 December of the last point's year minus 1, minus 1, times 100 (this equals the `Total return YTD` cell of `p2.e13`). If neither a year nor YTD can be worked out, `_NA("SERIES_TOO_SHORT")`. The dict is the value when `acc["kind"] == "table"`; when the kind is `chart` the value is `list(dict.values())` in that same order. Make `_price_based(src)` true for all three new statistics so pricing OFF still reads NOT_IN_THIS_VERSION (the OWN_SERIES method already does that; keep it true).

Then add ONE new test file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_pages_series.py` (pytest): over the REAL map through the shipped producer (harness: `import test_opal_producer as tp`, `import test_opal_producer_prices as tpp`, `tp.make_stores(map=<the real map>, pricing=True, as_of="2026-10-14", price_readers=<readers>)`, `tpp.op.produce(tp.REQ, tp.FIRM, stores)`), assert the five elements VALUE and that each value is what the table above says, computed in the test by plain arithmetic that does not call the code under test; assert pricing OFF leaves all five NOT_AVAILABLE / NOT_IN_THIS_VERSION; and unit-test `statistic_of` for the three new statistics on a small made-up series (including a series too short for any year). The sibling fixture serves 27 months, too short for the annual table; serve your OWN deterministic 133 monthly points per ticker (2015-10-14 to 2026-10-14, one level per month on the 14th) for AAA, BBB, CCC and the benchmark proxy `SPY` and the risk-free proxy `BIL`, each reader returning only rows with `start <= date <= end` (the price window is as_of less 10 years), AAA/SPY/BIL on tier `estate`, BBB on `yfinance`, CCC on `ycharts`.

1. Edit; write the test; run your test and the three criteria. 2. Commit the code, map and test (code first), then the proof and the status flip as separate commits. 3. **Report** the commit hashes and the three criterion outputs. The issuer then continues you with the next order on this chain (`AR-g-165`).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR164-g-AC1" cell_refs="AR-g-164"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 164 build</invocation><expect>^AR-PRICE-164-OK</expect></criterion>

<criterion id="AR164-g-AC2" cell_refs="AR-g-164"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 164 guard</invocation><expect>^AR-PRICE-164-OK</expect></criterion>

<criterion id="AR164-g-AC3" cell_refs="AR-g-164"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 164 regress</invocation><expect>^AR-PRICE-164-REGRESS-OK</expect></criterion>

<expected_criteria>AR164-g-AC1,AR164-g-AC2,AR164-g-AC3</expected_criteria>

- AC1: the five elements are VALUE with pricing on and carry the values above, checked by the checker's own arithmetic (the level path; the percent-off-the-peak path whose minimum equals the Drawdown table's `Max drawdown all`; the calendar-year table and its bars; `YTD` equal to `p2.e13`'s; the SPY path). At base it FAILs.
- AC2: with pricing off every element reads exactly as at the base; with pricing on nothing outside the 17 round-57 elements moves and the nine base VALUE elements are byte-equal. At base it PASSes.
- AC3: runs six existing producer and layout test files, then that the branch changed only your files, your folder, the order and the channel file. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. `opal_producer.py` and every other file are read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_pages_series.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~302/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-164.price-pages-series-forms.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R57_G.md</decomp_doc> round 57, workstream ~G, cell `AR-g-164`.
<owned_cells>AR-g-164</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR164-g-AC1, AR164-g-AC2, AR164-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~302/IRPT_ANLREQ.TO-AR-g-164.price-pages-series-forms.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-164`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code, map and test first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR164-g-AC1,AR164-g-AC2,AR164-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~282/IRPT_ANLREQ.TO-AR-g-161.pricing-as-of-calendar-frontier.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 3.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `layout_overview.py`, the overview map and one new test; no deploy, no AWS call, no network. Both files are members of the resident package, so the change reaches the served report only through a later resident release under its own never-widen pair: five elements move from NOT_IN_THIS_VERSION to VALUE when pricing is on, and the layout file's statistic engine is shared by every OWN_SERIES element (the nine base VALUE elements are guarded byte-equal).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change. comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- `ar_price_checks.py` was dry-run at the base (build FAIL, guard PASS, regress PASS; `calibrate` OK). Traps: the sibling fixture serves 27 months (the annual table needs 10 years, so the checker serves its own 133); `python -I` cannot import `pypdf`; a chart gets a LIST while a table gets a dict, and the element kind lives in `acc["kind"]`, not in `statistic_of`; YTD must use `_window_start`'s convention so it equals the `p2.e13` cell. NOT seen (blind): the rendered pixels of the chart pages; no reference fix was dry-run (the base arms bound the cell).
</preflight>

- Cut on the CTO's rulings (msgs 10729, 10734, 10743) by the issuer inside its own decomposition. Risk WORLD: the floor of an infrastructure path. Base: AR164-g-AC1 FAILs, AR164-g-AC2 PASSes, AR164-g-AC3 PASSes.
