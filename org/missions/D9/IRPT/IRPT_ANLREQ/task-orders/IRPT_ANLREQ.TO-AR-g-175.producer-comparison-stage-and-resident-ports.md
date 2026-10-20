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

**AMENDMENT 2 (issuer, 2026-10-20, after the issuer's broader-suite run on trunk; gate limb: none graded, an in-decomposition grant and one added part):** Part D. `infra/aws/lambda/investor-reporting/reports/tests/test_resident_r31_source.py` is now in your `<paths>`. Its test `test_the_bindings_carry_the_opal_map_member_pinned_by_content` pins the packaged Overview map's sha256 as the literal `21a8f6d690bbd28cf7eedfc979c3edcfa8d8a156336d9de779e8438c4913310f`; the round-57 price pages re-pointed that map, so the pin is stale and the test FAILS on trunk (its second assertion, against `_sha(MAP_SOURCE)`, is the live check and stays). Change that ONE literal to the map's current sha256, `661adac1efa8ee72cd95952f72815dfea90bfe83c4af162ee74daf3d4542143b` (compute it yourself from `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json` and confirm), and change nothing else in the file. The checker's `175 build` arm now runs that test. Inherited state: your commits 1c700aee586, 1b00c8dafbd, 05f9a402c68, 538f1492298 and ed599b9bfd1 stand; re-run the three criteria, write a new proof instance, flip `<status>` to complete again on three PASS. Also: do not fix anything else you see failing in the reports or generate suites; the issuer has the baseline and the other failures are not this cell's.

**AMENDMENT 3 (issuer, 2026-10-20, after the issuer's post-merge suite run on trunk; gate limb: GATE (viii) graded the modify and passed; an in-decomposition grant):** Part E, two defects of your own tests' reach, both found by running `reports/tests` whole. `infra/aws/lambda/investor-reporting/reports/tests/test_resident_installed.py` is now in your `<paths>`. (1) In `reports/tests/test_resident_installed.py::test_installer_supplies_opal_stores` the asserted key set of the Opal stores (line ~244) now also holds `\"model_bytes\"`: add that one name to the expected set and change nothing else in the file. (2) `reports/tests/test_compare_ports.py` edits `sys.path` at module level (your copy of its sibling's list, `ops/` and `intake/` ahead of `ycharts/generate/`), which makes pytest bind `entry` to the wrong file when `test_generate_installed.py` is collected after it (`AssertionError ... ops/entry.py` or `export/entry.py` at its line 32; reproduce with `python -m pytest reports/tests/test_compare_ports.py reports/tests/test_generate_installed.py` from `infra/aws/lambda/investor-reporting`). Fix: take `_PATH_BEFORE = list(sys.path)` just before the `HERE = ...` line, and put `sys.path[:] = _PATH_BEFORE` on the line right after `from test_resident_installed import opal_record`, with a two-line comment saying why. The checker's `175 build` arm runs both. Inherited state: your commits through 62b33c5588 are MERGED on trunk (09dd4ea9951); this is one more small commit; re-run the three criteria, write a new proof instance, status complete on three PASS. Do not touch `test_analysis_audit.py` or any other failing test.

**AMENDMENT 4 (issuer, 2026-10-20, replaces Part E item (2) only; item (1), the `model_bytes` name in the stores key set, stands and is done; gate limb: GATE (viii) graded the modify, as for AMENDMENT 3):** your `sys.path[:] = _PATH_BEFORE` restore fixed the collection but removed `reports/` and `_scope/` from the path after `test_resident_installed` had run its own header at your import, so 7 of its tests fail later in the regress list (`ModuleNotFoundError: canonical_profile_reads`, `composition`; your row W330-S11, correct). The issuer proved a different fix on the trunk tree: no path edit and no import at module level at all; the edits and the imports move into a module-scoped autouse fixture, so they run when this file's tests run and never at collection. In `infra/aws/lambda/investor-reporting/reports/tests/test_compare_ports.py`: remove the `_PATH_BEFORE` line, the three-line comment and the `sys.path[:] = _PATH_BEFORE` line you added, remove the original module-level path loops and the four module-level imports (`import resident_installed as ri`, `import resident_worker as rw`, `import model_source as msrc`, `from test_resident_installed import opal_record`) with their `# noqa: E402`, and put EXACTLY this block in their place, from the line `HERE = Path(__file__).resolve().parent` up to (not including) the line that defines `PRINCIPAL`. Keep every test function, helper and constant below it unchanged (they already use `ri`, `rw`, `msrc` and `opal_record` only inside functions):

```python
HERE = Path(__file__).resolve().parent
PKG = HERE.parents[1]  # infra/aws/lambda/investor-reporting
ROOT = PKG.parents[3]  # the workspace / worktree root
ri = rw = msrc = opal_record = None  # bound by _bind below, at run time


@pytest.fixture(autouse=True, scope="module")
def _bind():
    """The path edits and imports run when this module's tests run, never at collection: at module level they reorder the
    lookup of `entry` for the sibling test files pytest collects after this one (test_generate_installed.py pins ycharts/generate)."""
    for rel in ("reports", "ycharts/generate", "ycharts/research", "ycharts/session", "ycharts/extract", "_scope", "_ids", "_keys",
                "_authz", "intake", "ops"):
        p = PKG / rel
        if str(p) not in sys.path:
            sys.path.insert(0, str(p))
    for p in (HERE, ROOT / "lib"):
        if str(p) not in sys.path:
            sys.path.insert(0, str(p))
    import resident_installed
    import resident_worker
    import model_source
    from test_resident_installed import opal_record as opal_record_fn
    globals().update(ri=resident_installed, rw=resident_worker, msrc=model_source, opal_record=opal_record_fn)
```

Then run `reports/tests/test_compare_ports.py` alone (4 passed), the order's three criteria, and `python -m pytest --color=no -q -p no:cacheprovider reports/tests/test_compare_ports.py reports/tests/test_generate_installed.py reports/tests/test_resident_installed.py` (all pass). Inherited state: your commits through 77e329a4069 stand; the proof instance is rewritten again at the end; flip `<status>` to complete on three PASS. Do not edit the checker.

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
infra/aws/lambda/investor-reporting/reports/tests/test_resident_r31_source.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_installed.py
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
