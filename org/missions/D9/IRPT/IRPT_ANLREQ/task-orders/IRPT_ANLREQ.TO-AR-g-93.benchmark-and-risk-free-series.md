# TO-AR-g-93 -- the Opal producer prices a benchmark (SPY) and a risk-free rate (BIL) through the same chain, so beta, alpha, Sharpe and Sortino print, and the report names both in words

<to_id>IRPT_ANLREQ.TO-AR-g-93</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~195</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-93` (`decompositions/IRPT_ANLREQ_DECOMP_R19_G.md`) |
**outcome_ref:** FWD-7 (C-PRICES) | **depends_on:** `AR-g-86` (merged `1c84d38bf4`, the price stage) and `AR-g-89` (merged `8762c03234`, the Opal wording). Ruling: CTO msg 8630 (`CTO_RULING_DELL2_IRPT_ANLREQ_FOUR_LANES_END_TO_END_20261015.md` ADDENDUM 2 @77c0e9fde2): option A, SPY and BIL, adjusted close, through the C-PRICES chain, each with a source claim, named in words as proxies; an unpriced one leaves its statistics INPUT_MISSING, never a silent substitute.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~195`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-195` (branch `wk-IRPT_ANLREQ-195`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/` and `org/missions/D9/IRPT` on disk (it has no portal sub-worktree; your cell does not touch the portal). Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~195 <0.9.0_WK_IRPT_ANLREQ~195@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W195-S<k>` (take the next free `<k>`; check the channel file for `W195` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`).

### Read first (under `C:/dev/wk-irpt-anlreq-195/infra/aws/lambda/investor-reporting/ycharts/research/`)

- `opal_producer.py`: `_price_stage` (line 247), `produce` and `produce_package` (their price-stage calls and the `lo.compute_all` calls), and the disclosure and `settings` block of `produce`.
- `layout_overview.py`: `compute_all` (803) and `compute_element` (801): the `benchmark` and `risk_free` arguments; `_named_series` (644: a plain list of `[ms, level]` pairs is accepted, a given `key` would be added to EVERY element's trace inputs); `_risk_stat` (439: what beta, alpha, Sharpe and Sortino read, and the reasons `INPUT_MISSING:benchmark` and `INPUT_MISSING:risk_free`). You do not change this file.
- `portfolio_series.py` (`to_pairs`), `price_source.py` (`resolve_prices`), `tests/test_opal_producer_prices.py` (merged: how a priced run is set up and what it asserts) and `tests/test_opal_producer.py` (the fakes).

### THE CELL (`AR-g-93`, inlined)

The Overview's beta, alpha, Sharpe and Sortino read a benchmark level series and a risk-free level series that nothing supplies, so they read `INPUT_MISSING`. The CTO ruled: the benchmark is SPY and the risk-free rate is BIL, each priced through the C-PRICES chain (the same readers, the same T-1 cut, a source claim on each), named in the report in words as proxies. This cell adds that to the price stage.

**`ycharts/research/opal_producer.py`, exactly this:**
1. Constants beside `UNPRICED_ID`: `BENCHMARK_SYMBOL, RISK_FREE_SYMBOL = "SPY", "BIL"`; `BENCHMARK_ID, RISK_FREE_ID = "BENCHMARK", "RISK_FREE"`; and four texts, character for character:
   `BENCHMARK_TEXT = "Benchmark: SPY, a proxy for the S&P 500 Total Return index."`
   `RISK_FREE_TEXT = "Risk-free rate: BIL, 1-3 Month T-Bill ETF."`
   `BENCHMARK_MISSING_TEXT = "Benchmark: SPY, a proxy for the S&P 500 Total Return index, could not be priced; beta and alpha are not available."`
   `RISK_FREE_MISSING_TEXT = "Risk-free rate: BIL, 1-3 Month T-Bill ETF, could not be priced; alpha, Sharpe and Sortino are not available."`
2. `_price_stage(run_doc, stores)` now returns `(kept_by_name, prices, named)`. After the holdings are resolved and `prices` is built as today, resolve the two reference symbols in a SEPARATE call: `ref = price_source.resolve_prices([BENCHMARK_SYMBOL, RISK_FREE_SYMBOL], _start_of(as_of), as_of, readers, as_of)`, so a missing one never touches the holdings' `missing` list or `coverage`, and a client holding named SPY or BIL is still priced as a holding. For each slot (`"benchmark"` with SPY, `"risk_free"` with BIL): `prices[slot] = {"symbol": <symbol>, "status", "source", "first_date", "last_date", "attempts"}` copied from `ref["series"][symbol]`; and `named[slot]` is `portfolio_series.to_pairs(rows)` when the status is `price_source.PRICED` and that list has at least two points, else `None`. Update the function's docstring. The series are passed to the layout as PLAIN LISTS (no key), so no element's trace `inputs` gains a name it did not use.
3. `produce` and `produce_package` unpack the triple (`({}, None, {})` when pricing is off) and pass `named.get("benchmark")` and `named.get("risk_free")` as the `benchmark` and `risk_free` arguments of `lo.compute_all` (they are `None, None` there today).
4. In `produce`, when pricing: the disclosures are, in this order: `UNPRICED` (only when a holding is missing, as today), then `{"disclosure_id": BENCHMARK_ID, "text": BENCHMARK_TEXT}` (or `BENCHMARK_MISSING_TEXT` when `named["benchmark"]` is `None`), then `{"disclosure_id": RISK_FREE_ID, "text": RISK_FREE_TEXT}` (or `RISK_FREE_MISSING_TEXT`), then `WEIGHTING`. `effective_inputs.settings` also gets `"price_benchmark": {"symbol": ..., "source": ...}` and `"price_risk_free": {"symbol": ..., "source": ...}` (`source` is `None` when unpriced), beside `price_sources` (which still lists the holdings only).
5. With pricing off nothing differs from today: the two reference symbols are not read, the disclosures are `NO_PRICING`, `WEIGHTING`, and the settings carry neither new key.

**`ycharts/research/tests/test_opal_producer_prices.py`, one assertion:** the line that asserts the disclosure ids of the run with one unpriced holding, `== ["UNPRICED", "WEIGHTING"]`, becomes `== ["UNPRICED", "BENCHMARK", "RISK_FREE", "WEIGHTING"]` (that run's readers serve neither SPY nor BIL, so both new disclosures are the missing form). Change nothing else in that file.

**Tests.** A NEW file `ycharts/research/tests/test_opal_producer_benchmark.py`, offline, self-contained (its own small map with a BUILDER_ONLY title and `OWN_SERIES` elements on call `portfolio_level_series` with statistics `total_return_1y`, `beta_1y`, `alpha_1y`, `sharpe_1y` and `sortino_1y`; readers serving made-up monthly levels from 2024-07-14 to 2026-10-14 for AAA, BBB, CCC, SPY and BIL, SPY varying month to month so its variance is not zero; `as_of` `"2026-10-14"`; reuse the fakes of `tests/test_opal_producer.py` by importing it), with these exact test function names (the checker looks for each by name):
`test_beta_alpha_sharpe_and_sortino_are_valued_from_spy_and_bil`, `test_the_report_names_the_benchmark_and_the_risk_free_rate_in_words` (the two texts and the id order `BENCHMARK`, `RISK_FREE`, `WEIGHTING`), `test_an_unpriced_benchmark_leaves_beta_and_alpha_input_missing_and_says_so`, `test_an_unpriced_risk_free_rate_leaves_alpha_sharpe_and_sortino_input_missing_and_says_so`, `test_each_benchmark_price_carries_its_source_and_the_trace_inputs_stay_clean` (every element's `inputs` is exactly `["prices"]`), `test_pricing_off_reads_neither_the_benchmark_nor_the_risk_free_rate` (a recording reader is never called).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR93-g-AC1" cell_refs="AR-g-93"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g93_checks.py g93</invocation><expect>^AR-G93-OK</expect></criterion>

<criterion id="AR93-g-AC2" cell_refs="AR-g-93"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g93_checks.py regress</invocation><expect>^AR-G93-REGRESS-OK</expect></criterion>

<expected_criteria>AR93-g-AC1,AR93-g-AC2</expected_criteria>

- AC1 runs the producer on fakes thirteen ways with a hand-computed beta, alpha, Sharpe and Sortino (the checker recomputes the four from the monthly returns with its own formulas), the sources, the two statements in words and their order, an unpriced benchmark, an unpriced risk-free rate, both with a holding unpriced as well, a late row, a failing reader, pricing off, and the package render, then checks the six named tests exist and pass. At base it FAILs.
- AC2 runs ten existing test files one at a time (177 tests, among them the producer's, the price stage's and the page wording's) and needs all of them to pass: the guard that your one assertion edit is exactly that. At base it PASSes. Run it under `timeout 590` (one to three minutes).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_benchmark.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_prices.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~195/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-93.benchmark-and-risk-free-series.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R19_G.md</decomp_doc> round 19, workstream ~G, cell `AR-g-93`.
<owned_cells>AR-g-93</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR93-g-AC1, AR93-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~195/IRPT_ANLREQ.TO-AR-g-93.benchmark-and-risk-free-series.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-93`.
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put the `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR93-g-AC1,AR93-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the functions you changed or added with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `_price_stage` is called by `produce` and `produce_package` only, both edited here; nothing outside `opal_producer.py` and its tests reads the new `prices.benchmark` / `prices.risk_free` blocks, the two new disclosure ids (a free string in `AnalysisReport.v2.schema.json`) or the new `settings` members (a free object). With pricing off, or with a caller that supplies no `pricing`, nothing changes; and no caller supplies it until the release switches the resident's `opal_pricing` binding on. Nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change; SPY and BIL are read through the same readers (and so the same grants) as any holding.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against the CTO's ruling (msg 8630) and the layout's `_risk_stat`. Traps: the series handed to the layout with a key, so every element (even a plain total return) lists the benchmark as an input it did not use; the reference symbols resolved in the holdings' call, so an unpriced SPY lowers the portfolio's coverage or lands in `missing`; a silent substitute for an unpriced SPY or BIL (the CTO forbids it); the two statements out of order or in the wrong form; the T-1 cut skipped for the reference series; the benchmark and risk-free slots swapped; the pricing-off run reading SPY and BIL; the edited assertion of the prices test widened beyond the one line. The checker feeds a green arm (a reference build passes all thirteen cases, the six named tests and the 177 regress tests) and six mutant arms (the series not passed to the layout: the four statistics read INPUT_MISSING; BIL replaced by SHV: the sources and statistics differ; the two statements swapped: 3 cases fail; the missing form never used: 1; the T-1 cut skipped for the reference series: 1; the slots swapped: the statistics differ).
</preflight>

- Cut on CTO msg 8630 and the issuer's reference build on the merged tree. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR93-g-AC1` FAILs and `AR93-g-AC2` PASSes (177), as expected.
- The benchmark chart `p7.e15` (a call-sourced element, always NOT_AVAILABLE in the producer's trace) is not changed by this cell. The cell is in the ENGINE lane's resident release r32 only if it merges before the release pin.
