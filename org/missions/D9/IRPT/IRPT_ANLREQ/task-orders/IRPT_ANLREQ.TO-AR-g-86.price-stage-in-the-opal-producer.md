# TO-AR-g-86 -- the price stage in the Opal producer: prices resolved per symbol through the chain, a buy-and-hold series valued by the layout, each price's source stated, an unpriced security named in the report

<to_id>IRPT_ANLREQ.TO-AR-g-86</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~186</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-86` (`decompositions/IRPT_ANLREQ_DECOMP_R14_G.md`) |
**outcome_ref:** FWD-7 (C-PRICES) | **depends_on:** `AR-g-70` (`price_source.py`), `AR-g-63` (`portfolio_series.py`), `AR-g-80` to `AR-g-84` (the adapters, merged; this cell wires none of them).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~186`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-186` (branch `wk-IRPT_ANLREQ-186`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/` and `org/missions/D9/IRPT` on disk. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~186 <0.9.0_WK_IRPT_ANLREQ~186@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W186-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`).

### Read first (under `C:/dev/wk-irpt-anlreq-186/infra/aws/lambda/investor-reporting/ycharts/research/`)

- `opal_producer.py` (the whole file: `_opal_map`, `_read_stage`, `produce`, `produce_package`, `_entry`, `_section`) and `tests/test_opal_producer.py` (its fakes: `make_stores`, `served_world`, `FakeClassifier`, `Objects`, `Reports`).
- `price_source.py` (`resolve_prices(symbols, start, end, readers, as_of)` and what it returns: `series`, `missing`, `sources_used`, per-symbol `attempts`) and `portfolio_series.py` (`to_pairs`, `buy_and_hold`).
- `layout_overview.py`: `compute_all` (line 803), `compute_element` (755), `_compute_own_series` (595: the kept answer it reads), `_answers` (252), `_kept_key` (264), `element_value` (175), `statistic_of` (477), and `build` (1104). You change none of them.

### THE CELL (`AR-g-86`, inlined)

Today the Opal producer runs with `pricing=False`: every price-based element prints NOT_IN_THIS_VERSION. Andrew's rule (C-PRICES): each security's price comes from the first tier of the chain that holds it (the estate's stores, Yahoo, YCharts per symbol); a security no tier prices is named in the report and the report runs without it; every price carries its source. This cell adds that PRICE STAGE to the producer. It reads prices only through reader functions handed in through `stores`; it builds no client, makes no call and reads no secret. The wiring of the real readers (the four adapters) and of the T-1 date into the resident is a LATER cell; the swap for an unpriced symbol, the benchmark and risk-free series, and the YCharts-snapshot elements are later cells too.

**`ycharts/research/opal_producer.py`, exactly this:**

1. **Imports and constants.** Add the bare imports `import portfolio_series  # noqa: E402` and `import price_source  # noqa: E402` beside the existing sibling imports (alphabetical). Add near the other constants: `PRICE_CALLS = ("portfolio_level_series",)`, `PRICE_HISTORY_YEARS = 10`, `PRICES_INPUT = "prices"`, `UNPRICED_ID = "UNPRICED"`, and `UNPRICED_TEXT = "No price was found for: %s. Return and risk figures cover the other holdings only."` (the `%s` is the missing symbols joined by `", "`).
2. **New `stores` keys (document them in the module docstring):** `pricing` (bool; absent or falsy = today's behaviour, byte for byte), `price_readers` (a dict of tier name -> reader, any subset of `price_source.CHAIN`; a reader is `reader(symbol, start, end)` as `price_source` takes it), `as_of` (the T-1 date, `YYYY-MM-DD`).
3. **`_opal_map(map_doc, pricing=False)`.** `calls` is `[]` when `pricing` is falsy (as today). When `pricing` is true, `calls` holds only the map's own call dicts whose `name` is in `PRICE_CALLS`; every other call stays out of the budget, so the vendor-sourced elements keep reading NOT_IN_THIS_VERSION. `_read_stage` passes `pricing=bool(stores.get("pricing"))`.
4. **`_start_of(as_of)`:** the date `PRICE_HISTORY_YEARS` years before `as_of`, as `YYYY-MM-DD`; 29 February becomes 28 February.
5. **`_price_stage(run_doc, stores)` -> `(kept_by_name, prices)`.**
   - `stores["price_readers"]` not a dict -> `ProducerRefused("store required: price_readers")`; `as_of` missing or not a real `YYYY-MM-DD` date -> `ProducerRefused("store required: as_of")` (check the readers first). Both raise before anything is written.
   - Amounts: for each row of `run_doc["holdings"]["rows"]`, key `str(ticker).strip().upper()`, value the sum of `float(amount)` over repeated tickers.
   - `res = price_source.resolve_prices(list(amounts), _start_of(as_of), as_of, readers, as_of)`. It never raises on a data problem; a failing tier is an attempt with `ERROR:<class name>` and its message is never kept. Do not catch anything around it.
   - `series = {symbol: portfolio_series.to_pairs(entry["rows"])}` for each symbol of `res["series"]` whose `status` is `price_source.PRICED`; `port = portfolio_series.buy_and_hold(series, amounts)`.
   - `kept_by_name` is `{"portfolio_level_series": {"name": PRICES_INPUT, "step": 0, "response": {"status": 200, "body_json": {"chart_data": [[{"raw_data": port["pairs"]}]]}}}}` when `port["status"] == "OK"`, else `{}`.
   - `prices` is the dict `{"as_of": as_of, "window": res["window"], "sources_used": res["sources_used"], "missing": res["missing"], "coverage": port["coverage"], "symbols": {symbol: {"status", "source", "first_date", "last_date", "attempts"} copied from res["series"][symbol]}}`. Every value is a plain str, number, list or dict; no error text.
6. **`produce`.** After `_read_stage`: `pricing = bool(stores.get("pricing"))`; `kept, prices = _price_stage(run_doc, stores) if pricing else ({}, None)`; call `lo.compute_all(run_doc, kept, map_doc, None, None, held_sources, classified, None, pricing)` and `lo.build(run_doc, {}, map_doc, brand, computed, None, None, held_sources, classified, None, pricing)` (the page is built with an EMPTY kept dict: only the computed elements print values). When pricing, rename the trace input the layout derives for the kept answer (`"step=00_prices.json"`, from `_kept_key`) to `PRICES_INPUT` in every element entry's `inputs`. Then, when pricing: `inputs_as_of["prices"]` is `prices["as_of"]` (every other input keeps the run date); `run_doc["prices"] = prices`; the `NO_PRICING` disclosure is NOT emitted; if `prices["missing"]` is non-empty the FIRST disclosure is `{"disclosure_id": UNPRICED_ID, "text": UNPRICED_TEXT % ", ".join(prices["missing"])}`, then `WEIGHTING`. `effective_inputs.settings` gets `"pricing": True`, `"price_as_of": prices["as_of"]` and `"price_sources": {symbol: source}` (the source is `None` for a missing symbol). When pricing is off nothing differs from today: disclosures `NO_PRICING`, `WEIGHTING`; `settings.pricing` False; no `prices` key anywhere.
7. **`produce_package`.** The same price stage and the same `compute_all` / `build` arguments (pricing on only when `stores["pricing"]` is truthy). It writes no new field. `produce_commentary_pdf` is unchanged.
8. **Nothing else changes.** `closed_reason`, `_entry`, `_section` and the validation stay as they are (a price element's `NOT_AVAILABLE` reasons `INPUT_MISSING:...` are already in the closed set). No other file is touched.

**Tests.** A NEW file `ycharts/research/tests/test_opal_producer_prices.py`, offline, with these exact test function names (the checker looks for each by name); reuse the fakes of `tests/test_opal_producer.py` by importing it, and give `make_stores` a small map of your own (a BUILDER_ONLY title, a call-sourced element, and an `OWN_SERIES` element on call `portfolio_level_series` with statistic `total_return_1y`) plus readers that serve made-up monthly levels from 2024-07-14 to 2026-10-14 (the 14th of each month) with `as_of` `"2026-10-14"`:
`test_priced_run_values_a_return_and_a_drawdown_from_the_buy_and_hold_series`, `test_each_price_carries_its_source_as_a_claim`, `test_unpriced_symbol_is_named_in_the_report_and_the_run_still_completes`, `test_nothing_priced_runs_without_prices_and_says_so`, `test_tier_error_text_never_reaches_the_record` (a reader that raises with a marker string: the marker is in neither the written run.json nor the persisted document), `test_rows_after_as_of_are_never_used`, `test_pricing_off_is_unchanged_and_calls_no_reader`, `test_pricing_on_needs_as_of_and_readers` (refused before any write), `test_package_render_uses_the_same_price_stage`, `test_only_the_price_call_is_kept_in_the_map`.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR86-g-AC1" cell_refs="AR-g-86"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g86_checks.py g86</invocation><expect>^AR-G86-OK</expect></criterion>

<criterion id="AR86-g-AC2" cell_refs="AR-g-86"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g86_checks.py regress</invocation><expect>^AR-G86-REGRESS-OK</expect></criterion>

<expected_criteria>AR86-g-AC1,AR86-g-AC2</expected_criteria>

- AC1 runs the producer on fakes nineteen ways with hand-computed values (a fully priced run, a missing symbol, nothing priced, a failing tier, a late row, pricing off, the refusals, the package render), then checks that the ten named tests exist and pass. At base it FAILs.
- AC2 runs eight existing test files one at a time (163 tests: the producer, the packager, the layout, the held data, the chain core, the swap, the series) and needs all of them to pass: the guard that pricing off is unchanged. At base it PASSes. The checker takes 1 to 3 minutes: run it under `timeout 500`.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_prices.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~186/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-86.price-stage-in-the-opal-producer.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R14_G.md</decomp_doc> round 14, workstream ~G, cell `AR-g-86`.
<owned_cells>AR-g-86</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR86-g-AC1, AR86-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~186/IRPT_ANLREQ.TO-AR-g-86.price-stage-in-the-opal-producer.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-86`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR86-g-AC1,AR86-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the functions you changed or added with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `opal_producer.produce`, `produce_package` and `_read_stage` are called by `resident_worker.run_opal` through the injected `opal_stores` and by the packager; none of them passes `pricing`, `price_readers` or `as_of` today, so every caller keeps today's behaviour until the wiring cell sets them. The new `prices` key of run.json and the new `settings` members of the AnalysisReport document are read by nobody (`settings` is a free object in `AnalysisReport.v2.schema.json`; `disclosure_id` is a free string). Nothing is deployed, so no edge changes until the release cell ships the file.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change in this cell (the grants the real readers need are recorded in the R11 and R12 decompositions).
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against the compose read (ENGINE_COMPOSE_READ.json q4, the price seam). Traps: a symbol priced by a tier that was not the first to hold it; a row dated after T-1 reaching the series; a failing reader's message (it may hold a credential) reaching run.json or the document; an unpriced symbol dropped without a word; the series built over all amounts when one symbol has no price (the weights then no longer sum to the priced share); every vendor-sourced element turning into INPUT_MISSING because every call was kept in the map; the page printing a kept series for elements the trace calls NOT_AVAILABLE (so the page is built with an empty kept dict); pricing off changing a byte of today's output; a Feb-29 as_of crashing the window; `as_of` missing and the run writing anyway. The checker feeds a green arm (a reference build passes all nineteen cases, the ten named tests and the 163 regress tests) and eight mutant arms (pricing not passed to the compute: fails; the unpriced disclosure last: 2 cases; the source claim constant: 4; amounts ignored: 3; a five-year window: 1; NO_PRICING kept when priced: 3; the prices input dated the run date: 1; every call kept in the map: 1).
</preflight>

- Cut on the compose read (`q4`), the C-PRICES contract in PRD v0.15 and CTO msg 8377. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR86-g-AC1` FAILs and `AR86-g-AC2` PASSes (163), as expected.
- The chain core, the series builder and the four adapters are merged and untouched. The readers' production wiring, the swap for an unpriced symbol, the benchmark and risk-free series, the YCharts-snapshot elements and the map's statistic defects are later cells.
