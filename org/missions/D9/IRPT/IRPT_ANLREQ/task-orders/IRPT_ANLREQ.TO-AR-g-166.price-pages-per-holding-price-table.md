# TO-AR-g-166 -- the Opal-built report's price pages, part 4: the per-holding price table (ticker, last price date, source tier as the claim) (row 3c22; CTO msgs 10729, 10734, 10743)

<to_id>IRPT_ANLREQ.TO-AR-g-166</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~303</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>57</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-166` (`decompositions/IRPT_ANLREQ_DECOMP_R57_G.md`) |
**outcome_ref:** FWD-7 (ACCEPT: "the trace shows each price with its source as a claim field") | **depends_on:** none; it gates none of the other cells (CTO msg 10743). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~303`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-303` (branch `wk-IRPT_ANLREQ-303`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~303 <0.9.0_WK_IRPT_ANLREQ~303@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W303-S<k>` (take the next free `<k>`; check the channel file for `W303` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Do not touch anything outside the `<paths>` block. Run Python with plain `python` (the producer's tests need `pypdf`, which `python -I` cannot see).

### THE CELL (`AR-g-166`, inlined)

Files: `infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py` (read it first: `_opal_map` at about line 104 appends the three classified elements after the map's last page through `_classified_elements(page)`; `_price_stage` at about line 261 returns `(kept_by_name, prices, named)`; `prices["symbols"][TICKER]` is `{"symbol", "status", "source", "first_date", "last_date", "attempts"}`; `lo.compute_all(...)` is called at about lines 405 and 491, and `run_doc["prices"] = prices` is set only AFTER the second call, at about line 509) and `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py` (`compute_element` at about line 790 dispatches on `src["computed"]`; the classified methods are the pattern: a computed method that reads the run, a `NAME = "NAME"` constant, and a renderer through `_table_html`, which draws a LIST OF DICTS as a table with a header row).

Add ONE new element, always present in the opal map like the classified three (appended after the last page, including after the classified page): id `opal.prices.holdings`, kind `table`, label `Holdings: last price date and source`, source `{"computed": "PRICE_TABLE", "call": null, "columns": [], "field": null, "sleeve": null, "statistic": null}`. Add the computed method `PRICE_TABLE` to the layout. Its value is a LIST OF DICTS, one per distinct holding ticker in the run's holdings order, each with exactly the keys `Ticker`, `Last price date`, `Source`:
- a holding whose `prices["symbols"][ticker]["status"]` is `PRICED`: `{"Ticker": t, "Last price date": <its last_date>, "Source": <its source, the tier that answered: estate, yfinance or ycharts>}`;
- any other holding: `{"Ticker": t, "Last price date": "not priced", "Source": "none"}`.
It reads ONLY the price stage's own record (`prices`), no new vendor call, no new reader. The layout must be able to see `prices` during the computation: either pass it to `lo.compute_all` as a new optional keyword (default `None`) from BOTH call sites, or set `run_doc["prices"]` before the call; do NOT change any other element's result and do NOT change what `run.json` records. With pricing OFF (`prices` is `None`) the element is present and reads `NOT_AVAILABLE` / `NOT_IN_THIS_VERSION` like every other price element (the layout's `_price_based(src)` must be true for `PRICE_TABLE`; do not add it to `SERIES_METHODS` unless you have read every use of that tuple and none changes behaviour). The trace `inputs` of the element is `["prices"]`; its `coverage` is the weight share of the priced holdings (use the record's own `coverage`).

Then add ONE new test file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_pages_table.py` (pytest): through the shipped producer (harness: `import test_opal_producer as tp`, `import test_opal_producer_prices as tpp`; the sibling `tpp._priced()` helper serves AAA by estate, BBB by yfinance and CCC by ycharts) assert the table is exactly the three dicts with the right dates and tiers; with one holding unpriced (an empty table for its tier, as `tpp._priced` allows) that holding reads `not priced` / `none`; with pricing OFF the element reads NOT_AVAILABLE / NOT_IN_THIS_VERSION; and the rendered report page contains the three tickers and the three tiers (the layout renders HTML before the PDF; assert on the HTML or on the section value, whichever the sibling tests assert on).

1. Edit; write the test; run your test and the three criteria. 2. Commit the code and test (code first), then the proof and the status flip as separate commits. 3. **Report** the commit hashes and the three criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR166-g-AC1" cell_refs="AR-g-166"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 166 build</invocation><expect>^AR-PRICE-166-OK</expect></criterion>

<criterion id="AR166-g-AC2" cell_refs="AR-g-166"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 166 guard</invocation><expect>^AR-PRICE-166-OK</expect></criterion>

<criterion id="AR166-g-AC3" cell_refs="AR-g-166"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 166 regress</invocation><expect>^AR-PRICE-166-REGRESS-OK</expect></criterion>

<expected_criteria>AR166-g-AC1,AR166-g-AC2,AR166-g-AC3</expected_criteria>

- AC1: with pricing on, `opal.prices.holdings` is VALUE with inputs `["prices"]` and equals the three dicts `{"Ticker", "Last price date": "2026-10-14", "Source": estate|yfinance|ycharts}` for AAA, BBB, CCC in that order. At base it FAILs (the element does not exist).
- AC2: with pricing off every base element reads exactly as at the base and the new element reads NOT_AVAILABLE / NOT_IN_THIS_VERSION; with pricing on nothing outside the 17 round-57 elements and the new one moves, and the nine base VALUE elements are byte-equal. At base it PASSes.
- AC3: runs six existing producer and layout test files, then that the branch changed only your files, your folder, the order and the channel file. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. The overview map and every other file are read only (the new element is appended in code, like the classified three; the map is not edited by this cell).
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_pages_table.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~303/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-166.price-pages-per-holding-price-table.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R57_G.md</decomp_doc> round 57, workstream ~G, cell `AR-g-166`.
<owned_cells>AR-g-166</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR166-g-AC1, AR166-g-AC2, AR166-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~303/IRPT_ANLREQ.TO-AR-g-166.price-pages-per-holding-price-table.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-166`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and test first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR166-g-AC1,AR166-g-AC2,AR166-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~282/IRPT_ANLREQ.TO-AR-g-161.pricing-as-of-calendar-frontier.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 3.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `opal_producer.py`, `layout_overview.py` and one new test; no deploy, no AWS call, no network. Both are resident package members: the change reaches the served report only through a later resident release under its own never-widen pair; a new element is appended to every Opal report's element list (present and NOT_IN_THIS_VERSION when pricing is off, a table when it is on), so the report's element count rises by one in both branches and the pair must say so.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change. comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- `ar_price_checks.py` was dry-run at the base (build FAIL because the element does not exist, guard PASS, regress PASS). Traps: `run_doc["prices"]` is set after the second `compute_all` call, so the layout cannot see it unless the cell moves it or passes it; two call sites must change together; `SERIES_METHODS` has other users; the sibling `_priced` fixture serves 27 months (enough for this cell, which reads dates and tiers only). NOT seen (blind): the rendered pixels; no reference fix was dry-run; the table's wording on an unpriced holding (`not priced` / `none`) is the issuer's, open to the CTO.
</preflight>

- Cut on the CTO's rulings (msgs 10729, 10734, 10743) by the issuer inside its own decomposition. Risk WORLD: the floor of an infrastructure path. Base: AR166-g-AC1 FAILs, AR166-g-AC2 PASSes, AR166-g-AC3 PASSes.
