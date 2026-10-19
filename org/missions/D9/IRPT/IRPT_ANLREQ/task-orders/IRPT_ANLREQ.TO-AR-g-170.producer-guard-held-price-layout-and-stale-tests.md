# TO-AR-g-170 -- the producer runs against a layout without the price pages, and the 8 tests the price-page merge left stale are repaired (CTO msg 11012, ~Y2 msg 11010)

<to_id>IRPT_ANLREQ.TO-AR-g-170</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~308</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>59</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-170` (`decompositions/IRPT_ANLREQ_DECOMP_R59_G.md`) |
**outcome_ref:** FWD-7 (the trace shows each price with its source as a claim field; the producer must not break a release that lacks the price pages) | **depends_on:** none. Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~308`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-308` (branch `wk-IRPT_ANLREQ-308`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~308 <0.9.0_WK_IRPT_ANLREQ~308@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W308-S<k>` (check the channel file for `W308` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` from `infra/aws/lambda/investor-reporting` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block.

### THE CELL (`AR-g-170`, inlined)

**AMENDMENT 2 (issuer, 2026-10-19, on worker ~308's BLOCKING row IRPT_ANLREQ-D2-W308-S2; gate limb: none graded, an in-decomposition correction of the issuer's own Part B wording):** Part B arm 1 as first worded deleted `lo.PRICE_TABLE`, which breaks the layout's own `_price_based` (layout_overview.py:764) and `compute_element` (about line 917) and so fails on the layout, not on the producer. The issuer's wording is wrong; the worker's arm was right to stop. Arm 1 now sets the producer flag false and installs the refusing `compute_all` wrapper, and does NOT delattr. The arm still proves what it must: with the flag false the producer lists no `opal.prices.holdings` and passes no `prices` keyword. Inherited state: your commits e65a1596a2, c18cf83cd3, b98b6e0f41, c711b81838, 900cbcdfdd stand; change ONLY the guard test's first test (remove the delattr line and update its docstring), re-run the three criteria, overwrite the proof instance, and flip the order's status to complete only on three PASS.

**AMENDMENT 1 (issuer, 2026-10-19, on worker ~308's BLOCKING row IRPT_ANLREQ-D2-W308-S1; gate limb: none graded, an in-decomposition provisioning fix):** the first seating found the sparse worktree short of directories the tests import, so no code was written and the first proof record reads BLOCKED. The issuer widened the sparse set (`infra/aws/lambda/investor-reporting`, `infra/aws/lambda/v2_portal/_shared`, the YCDGEN maps folder) and re-ran the base from the worktree: AC1 FAIL (no tests ran), AC2 FAIL (8 failed, 24 passed), AC3 PASS (146 passed). Inherited state: commits 44afdd5d89 (the row) and bb0408b656 (the BLOCKED proof record) are on the branch; overwrite the proof instance with the real result and leave the row as it is. Do not run `git sparse-checkout` yourself.

Directory for every file below: `infra/aws/lambda/investor-reporting/ycharts/research/` (`TESTS` = its `tests/` folder).

**Part A: the guard (`opal_producer.py`).** The producer imports the layout as `lo`. Three reads assume the layout carries the AR-g-166 price pages: `lo.PRICE_TABLE` in `_price_table_element` (about line 112) and in `_opal_map` (about line 130), and the keyword `prices=prices` in the two `lo.compute_all(...)` calls (about lines 428 and 513). A layout built before AR-g-163..166 has no `PRICE_TABLE` and its `compute_all` takes no `prices` keyword, so the producer raises at report time. Make the producer work against such a layout WITHOUT changing a byte of behaviour against the current layout:
- Define ONE module-level flag next to the other constants, `_LAYOUT_HAS_PRICE_PAGES = hasattr(lo, "PRICE_TABLE")`.
- `_opal_map`: append the price-table element only when the flag is true. When it is false, the map and every other element are exactly as they are today.
- Both `compute_all` calls: pass `prices=prices` only when the flag is true; otherwise call exactly as before AR-g-166 (no `prices` keyword).
- Do not edit `layout_overview.py` or any map. Do not add a try/except; the flag is the guard.

**Part B: the guard test (NEW file `TESTS/test_producer_held_layout_guard.py`).** Through the shipped producer and the sibling harness (`from test_opal_producer import FIRM, REQ, make_stores, stored`, as `TESTS/test_opal_producer_not_in_this_version.py` does at its top), with `monkeypatch`: (1) set `op._LAYOUT_HAS_PRICE_PAGES` to false (do NOT delete `PRICE_TABLE` from the layout: the layout's own `_price_based` and `compute_element` read that name, so deleting it breaks the layout, which a real held layout does not), and replace `lo.compute_all` by a wrapper that raises `TypeError` if it receives a `prices` keyword and otherwise calls the real one; the producer's run then completes and its element id list does NOT contain `opal.prices.holdings`; (2) the DIFFERENCE CONTROL: with the layout untouched (flag true) the same run lists `opal.prices.holdings` and the wrapper is called with a `prices` keyword. Both arms in this file; the wrapper must be shown to RAISE when given `prices` (assert that directly in a third small test).

**Part C: repair the 8 stale tests. Their intent stays; no assertion is deleted or weakened.** Run these four files first; at the base EIGHT fail: `TESTS/test_opal_producer_not_in_this_version.py` (5: `test_the_fixture_has_the_composition_the_test_claims`, `test_run_json_still_lists_every_entry`, `test_exactly_one_not_shown_disclosure_comes_last_and_counts_the_dropped_entries`, `test_no_not_shown_disclosure_when_nothing_is_dropped`, `test_difference_control_the_unfiltered_list_holds_both_kinds`), `TESTS/test_price_pages_table.py::test_pricing_off_reads_not_available_not_in_this_version_and_prints_no_table`, `TESTS/test_price_pages_series.py::test_pricing_off_reads_not_in_this_version_for_the_five`, `TESTS/test_price_pages_text.py::test_pricing_off_reads_not_in_this_version_for_the_four`. The cause is the AR-y-408 rule, merged after these tests were written: the report DOCUMENT (`run.json` element list) omits every element that resolves NOT_IN_THIS_VERSION or is builder-only and counts them in ONE trailing NOT_SHOWN disclosure; a VALUE element is never dropped. Since AR-g-166 the producer adds one more element, `opal.prices.holdings` (id constant `op.PRICE_TABLE_ID`), to every Opal map; with pricing OFF it resolves NOT_IN_THIS_VERSION, so it is one MORE dropped entry (counts and the disclosure text rise by one, and a map with nothing else dropped now shows "1 report element ... is not listed" unless the run is priced, in which case it is a VALUE element and is listed). Repair each test to say exactly that, keeping what it proves:
- In the 408 file, the fixture's dropped-entry count goes from 5 to 6 and the listed ids gain `op.PRICE_TABLE_ID` only where the test lists VALUE entries of a PRICED run; reference the price table by `op.PRICE_TABLE_ID`, never by a retyped string. `test_no_not_shown_disclosure_when_nothing_is_dropped` must still assert that NO disclosure appears when nothing is dropped: give its run a priced setup (the sibling `test_opal_producer_prices.py` has the priced harness, `tpp._priced()`) so the price table is a VALUE element and nothing is dropped, rather than changing what it asserts.
- In the three round-57 tests, the pricing-off assertions read the report document, where the element is now ABSENT; assert the layout's own computed value (the producer's `seen["computed"]`-style capture in the 408 file, or `lo.compute_all(...)` called directly on the producer's map) reads NOT_AVAILABLE / NOT_IN_THIS_VERSION for each element they name, and additionally that the document omits it. Keep the element lists they name.
If one of the 8 cannot be repaired this way without weakening what it proves, file a row and report which; do not delete or loosen it.

1. Edit Part A, write Part B, repair Part C. 2. Run the three acceptance commands. 3. Commit the code first (`opal_producer.py`), then the tests, then the proof and the status flip as separate commits. 4. **Report** the commit hashes and the three criterion outputs.

### ACCEPTANCE (worktree root `infra/aws/lambda/investor-reporting`, after your last commit)

<criterion id="AR170-g-AC1" cell_refs="AR-g-170"><invocation>cd infra/aws/lambda/investor-reporting && timeout 100 python -m pytest --color=no -q -p no:cacheprovider ycharts/research/tests/test_producer_held_layout_guard.py</invocation><expect>^[0-9]+ passed in</expect></criterion>

<criterion id="AR170-g-AC2" cell_refs="AR-g-170"><invocation>cd infra/aws/lambda/investor-reporting && timeout 100 python -m pytest --color=no -q -p no:cacheprovider ycharts/research/tests/test_opal_producer_not_in_this_version.py ycharts/research/tests/test_price_pages_table.py ycharts/research/tests/test_price_pages_series.py ycharts/research/tests/test_price_pages_text.py</invocation><expect>^[0-9]+ passed in</expect></criterion>

<criterion id="AR170-g-AC3" cell_refs="AR-g-170"><invocation>cd infra/aws/lambda/investor-reporting && timeout 115 python -m pytest --color=no -q -p no:cacheprovider ycharts/research/tests/test_opal_producer.py ycharts/research/tests/test_opal_producer_prices.py ycharts/research/tests/test_opal_producer_page_wording.py ycharts/research/tests/test_price_pages_repoint.py ycharts/research/tests/test_layout_overview.py ycharts/research/tests/test_runner.py</invocation><expect>^[0-9]+ passed in</expect></criterion>

<expected_criteria>AR170-g-AC1,AR170-g-AC2,AR170-g-AC3</expected_criteria>

- AC1: the producer completes against a layout without `PRICE_TABLE` and without the `prices` keyword (no `opal.prices.holdings`), and with the layout untouched it lists the element and passes `prices`. At base it FAILs (the test file does not exist: no tests ran).
- AC2: the 8 stale tests plus the rest of those four files pass (at base: 8 failed, 24 passed).
- AC3: the six existing files that pass at base keep passing (at base: 146 passed). If your change moves the count, say so in the report.

## BOUNDS

- **Grant.** The `<paths>` block only. `layout_overview.py`, every map and every other test file are read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_producer_held_layout_guard.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_not_in_this_version.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_pages_table.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_pages_series.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_pages_text.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R59_G.md</decomp_doc> round 59, workstream ~G, cell `AR-g-170`.
<owned_cells>AR-g-170</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR170-g-AC1, AR170-g-AC2, AR170-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-170`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code first, then the tests, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the pytest summary line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR170-g-AC1,AR170-g-AC2,AR170-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~303/IRPT_ANLREQ.TO-AR-g-166.price-pages-per-holding-price-table.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 4.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one product file (`opal_producer.py`, a resident package member) and five test files; no deploy, no AWS call, no network. The change reaches the served report only through a later resident release under its own never-widen pair; against the current layout the producer's behaviour is unchanged (the flag is true), so the pair need not mention it.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the three criteria were dry-run at the base from the invocations above: AC1 FAIL (no tests ran), AC2 FAIL (8 failed, 24 passed), AC3 PASS (146 passed). Traps: the stale tests read the report DOCUMENT where the element is now absent; `test_no_not_shown_disclosure_when_nothing_is_dropped` needs a priced run, not a changed assertion; `op._LAYOUT_HAS_PRICE_PAGES` is read at call time so a test can flip it. NOT seen (blind): a real resident build against a pre-AR-g-163 layout (the guard test simulates it by deleting the attribute and refusing the keyword).
</preflight>

- Cut on CTO msg 11012 (disarm by guard) and ~Y2 msg 11010 (8 failing tests, both ruled mine) by the issuer inside its own decomposition (declared WORLD: the producer is an infrastructure path, so the order takes the full limbs, not the direct-act path), under Andrew's pause as merge-forward hygiene of already-merged work, not a new cell of the price pair. Gate limb: to be stated in the issuance commit. Base: AC1 FAILs, AC2 FAILs, AC3 PASSes.
