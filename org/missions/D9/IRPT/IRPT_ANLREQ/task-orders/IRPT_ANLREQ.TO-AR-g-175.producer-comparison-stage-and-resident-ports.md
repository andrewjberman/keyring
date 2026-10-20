# TO-AR-g-175 -- the producer runs the comparison stage and the resident hands it the request's comparables and the two model objects (K4)

<to_id>IRPT_ANLREQ.TO-AR-g-175</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~330</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-175` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** AR-g-171, AR-g-173 and AR-g-174 (earlier orders of the same queue: this cell calls all three). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~330`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-330` (branch `wk-IRPT_ANLREQ-330`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~330 <0.9.0_WK_IRPT_ANLREQ~330@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W330-S<k>` (check the channel file for `W330` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **You are the one worker of chain A (queue 171, 173, 174, 175, in that order).** The commits of your earlier orders are on this branch and their files are in this worktree; a later order builds on them. You are handed one order at a time.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py` (read it; you cannot edit it). It builds its own deterministic fixtures and computes every expected number itself, independent of your code: if your number and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both numbers, and stop on that criterion.

### THE CELL (`AR-g-175`, inlined)

Directory `RES` = `infra/aws/lambda/investor-reporting/ycharts/research/`; `TESTS` = its `tests/` folder; `GEN` = `infra/aws/lambda/investor-reporting/ycharts/generate/`; `REP` = `infra/aws/lambda/investor-reporting/reports/`. Edit `RES/opal_producer.py`, `GEN/resident_worker.py` and `REP/resident_installed.py`; create `TESTS/test_compare_producer.py` and `REP/tests/test_compare_ports.py`; nothing else. Your earlier orders put `model_source.py`, `comparables.py` and the layout's COMPARE methods on this branch.

**Why.** This cell connects the pieces so a real Comparison or Multi-Comp request produces the comparison section (PRD FWD-10, C-MODEL-SOURCE). The decomposition's K4 contract: `stores["comparables"]` = the ordered list of catalogue entries (`{"key", "label", "ticker"}`; a model entry has `"ticker": None`, an ETF entry has its ticker); `stores["model_bytes"]` = `callable(key) -> bytes` for the two model objects.

**A. The producer (`RES/opal_producer.py`).** Follow how `_price_stage`, `_price_table_element`, `_opal_map` and `_price_kwargs` work (AR-g-166, AR-g-170).
- A module flag `_LAYOUT_HAS_COMPARE = hasattr(lo, "COMPARE_CHART")`, used exactly like `_LAYOUT_HAS_PRICE_PAGES`: when false the producer neither appends the elements nor passes `compare=`. Import `comparables` and `model_source` INSIDE the stage function (lazily), so a package that lacks them still runs an Overview.
- The stage runs only when `stores.get("comparables")` is a non-empty list AND pricing is on AND the flag is true. It builds the `portfolio` argument from the price stage's buy-and-hold path (the kept `portfolio_level_series` pairs; the name is the string `Your portfolio`), and one `comparables` item per entry, in order, named by the entry's `label`:
  - a model entry (`model_source.code_for_key(entry["key"])` is a code): its series = `model_source.read_series(stores["model_bytes"])["series"][code]`; a `ModelSourceRefused`, or a code with no series, makes this comparable a gap with the reason `"the Opal model series could not be read"` (the run NEVER fails for it);
  - an ETF entry (`ticker` set): priced with ONE extra `price_source.resolve_prices(...)` call for all ETF comparables over the same window and readers as the holdings (`_start_of(as_of)` to `as_of`); a symbol not PRICED is a gap with the reason `"no price was found for it"`; a priced one's series = `portfolio_series.to_pairs(rows)`.
- Allocation inputs: the portfolio's by-amount weights grouped by the classifier's asset class (the same classified rows the existing ALLOCATION_ASSET_CLASS element uses; class names normalised by `build_allocation`); a model's weights and `as_of` from `model_source.read_allocation(...)`; an ETF's `asset_class` from `stores["classifier"].get_classification(ticker)` (none -> a gap with the reason `"no classification is held for it"`).
- Then `comparables.build_compare(...)` (benchmark and risk-free are the price stage's `named` series), `comparables.build_allocation(...)`, pass `compare={"record": ..., "allocation": ...}` to `lo.compute_all` at BOTH call sites, and append the five elements after the last page (after the classified elements and the price table), ids `opal.compare.window`, `opal.compare.chart`, `opal.compare.returns`, `opal.compare.risk`, `opal.compare.allocation`, kinds `text`, `chart`, `table`, `table`, `table`, labels `Comparison: common window`, `Comparison: cumulative return`, `Comparison: periodic total returns`, `Comparison: risk`, `Comparison: asset allocation`, source `{"computed": <method>, "call": null, "columns": [], "field": null, "sleeve": null, "statistic": null}`.
- The values must reach `run.json` and the report sections the way the price table's and the classified tables' do (read `_check_values`, `_section`, `_entry`): the window as a string, the chart as a list, the three tables as the `{"rows", "gaps"}` dicts. If the existing value checks reject a dict value, extend them for these five ids only.
- With no `comparables` (an Overview), with pricing off, or with the flag false, NOTHING changes: no compare element, no extra read, the same element list as before.

**B. The resident ports.**
- `GEN/resident_worker.py` `run_opal`: when the accepted record's `report_variant` is `comparison` or `multicomp`, add `comparables` to the stores handed to the producer, read through the SAME guarded path the vendor job uses for its comparisons (`self.frozen.recipe_inputs(...)` / `prepare(...)` and its `["comparisons"]`, the resolved `comparison_catalog` entries of the request's own `comparison_keys`; see `frozen_worker.py` around line 95): never from the browser. Keep each entry's `key`, `label` and `ticker` only. An Overview adds nothing.
- `REP/resident_installed.py`: the resident's Opal stores gain `model_bytes`: `lambda key: s3.get_object(Bucket=model_source.BUCKET, Key=key)["Body"].read()` over the host role's own S3 client, and it refuses (raises) for any key other than `model_source.SERIES_KEY` and `model_source.POSITIONING_KEY`. Wire it the way `pricing_extras` / `swap_extras` are wired (a per-job extras function, built only for an Opal principal; import `model_source` lazily).

**C. Tests (your own proof; offline).** `TESTS/test_compare_producer.py`: a Multi-Comp run on fixtures end to end through `produce` (two models and one ETF), the gaps stated, an Overview unchanged, pricing off unchanged, the flag false unchanged. `REP/tests/test_compare_ports.py`: `run_opal` hands the producer the comparables for a multicomp record and nothing for an overview (fake frozen reader); `model_bytes` asks the bucket for the two keys only and refuses any other.

1. Edit, write the tests. 2. Run your tests and the three criteria. 3. Commit the producer first, then the ports, then the tests (separate commits are fine), then the proof and the status flip as separate commits. 4. Report.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR175-g-AC1" cell_refs="AR-g-175"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py 175 build</invocation><expect>^AR-CMP-175-OK</expect></criterion>

<criterion id="AR175-g-AC2" cell_refs="AR-g-175"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py 175 guard</invocation><expect>^AR-CMP-175-OK</expect></criterion>

<criterion id="AR175-g-AC3" cell_refs="AR-g-175"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py 175 regress</invocation><expect>^AR-CMP-175-REGRESS-OK</expect></criterion>

<expected_criteria>AR175-g-AC1,AR175-g-AC2,AR175-g-AC3</expected_criteria>

- AC1: a Multi-Comp run through the SHIPPED producer on the REAL multi map (two models and one ETF) lists the five compare elements as VALUE with the numbers the checker computes itself, the page prints every name and the window, an unpriced comparable is stated in words, the Comparison map works with one comparable, and an Overview or a pricing-off run lists none. At base it FAILs.
- AC2: no existing element of the Overview, Multi or Comparison report moves when no comparable is given. At base it PASSes.
- AC3: the existing test files plus your own pass, and the branch changed only the files of the cells so far. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_compare_producer.py
infra/aws/lambda/investor-reporting/reports/tests/test_compare_ports.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~330/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-175.producer-comparison-stage-and-resident-ports.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-175`.
<owned_cells>AR-g-175</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR175-g-AC1,AR175-g-AC2,AR175-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~330/IRPT_ANLREQ.TO-AR-g-175.producer-comparison-stage-and-resident-ports.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-175`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR175-g-AC1,AR175-g-AC2,AR175-g-AC3` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `opal_producer.py`, `resident_worker.py` and `resident_installed.py` are resident package members: the change reaches the served report only through a later resident release (the issuer builds it under its own COO+CTO never-widen pair, after the grant AR-g-172 is applied); with no comparables the producer behaves as before, and the model reader refuses any key but the two named.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change in this cell (the grant is AR-g-172).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: 175 build FAIL (no compare elements), guard PASS, regress PASS. Traps: the stores are injected, so the checker passes `comparables` and `model_bytes` as fakes (a gzip positioning object, a plain series object); an ETF comparable shares the holdings' price window and readers; a comparable that cannot be read or priced must never fail the run (R8 and FWD-12); the layout flag must keep a held layout working (see AR-g-170). NOT seen (blind): the real `frozen.prepare` call with live data and the real S3 get (the issuer runs the one real run after the release).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1 FAILs, AC2 PASSes, AC3 PASSes.
