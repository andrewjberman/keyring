# TO-AR-g-174 -- the layout computes and draws the five comparison elements (K3)

<to_id>IRPT_ANLREQ.TO-AR-g-174</to_id>
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

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-174` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** AR-g-173 (the K2 module this cell's test builds records with, earlier in the same queue). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~330`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-330` (branch `wk-IRPT_ANLREQ-330`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~330 <0.9.0_WK_IRPT_ANLREQ~330@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W330-S<k>` (check the channel file for `W330` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **You are the one worker of chain A (queue 171, 173, 174, 175, in that order).** The commits of your earlier orders are on this branch and their files are in this worktree; a later order builds on them. You are handed one order at a time.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py` (read it; you cannot edit it). It builds its own deterministic fixtures and computes every expected number itself, independent of your code: if your number and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both numbers, and stop on that criterion.

### THE CELL (`AR-g-174`, inlined)

Directory `RES` = `infra/aws/lambda/investor-reporting/ycharts/research/`; `TESTS` = its `tests/` folder. Edit `RES/layout_overview.py` and create `TESTS/test_compare_elements.py`; nothing else. Your earlier orders put `model_source.py` and `comparables.py` on this branch; build to the record shape `comparables.build_compare` and the table shape `comparables.build_allocation` return (you may call them in tests).

**Why.** FWD-10's comparison section must be drawn by the layout. The producer appends five computed elements (cell AR-g-175); this cell makes the layout compute and draw them, the way it already computes and draws the price table (`PRICE_TABLE`, `_compute_price_table`, `compute_element`, `compute_all`, `_price_based`, `_element_html`, `_chart_svg`, `_table_html`). Read those first and follow their pattern.

**The change in `RES/layout_overview.py`.**
- Five constants, each equal to its own name: `COMPARE_WINDOW`, `COMPARE_CHART`, `COMPARE_RETURNS`, `COMPARE_RISK`, `COMPARE_ALLOCATION` (computed method names).
- `compute_element(..., compare=None)` and `compute_all(..., compare=None)` take a new optional keyword `compare = {"record": <build_compare record>, "allocation": <build_allocation table>}` (passed through exactly as `prices` is). Absent when needed -> NOT_AVAILABLE with reason `INPUT_MISSING:compare`. `_price_based(src)` is true for the five methods, so with `pricing=False` each reads NOT_AVAILABLE / NOT_IN_THIS_VERSION. The trace `inputs` of each is `["compare"]`; `coverage` = the share of rows that are VALUE.
- Values (the producer stores them as the element's value):
  - `COMPARE_WINDOW` -> a string: `"Common window: <start> to <end> (<years> years, to one decimal). <rule>"` (`<years>` printed with `%.1f`).
  - `COMPARE_CHART` -> a list, one item per VALUE row in record order (the portfolio first): `{"name": row name, "points": row path}`.
  - `COMPARE_RETURNS` -> `{"rows": [...], "gaps": [...]}`. One row per VALUE row: `{"Name": name, "1M": v, "3M": v, "YTD": v, "1Y": v, "3Y": v, "5Y": v, "10Y": v}` where `v` is the percent as a float, or the string `"n/a"` when it is `None`. `gaps` = one string per NOT_AVAILABLE row: `"not available for <name>: <reason>"`.
  - `COMPARE_RISK` -> `{"rows": [...], "gaps": [...], "note": str}`. Rows: `{"Name", "Std dev (%)", "Sharpe", "Sortino", "Max drawdown (%)", "Alpha (%)", "Beta"}` with floats or `"n/a"`. `note` states the period and the references in words: when `years` is an int N: `"Risk figures cover the last N years of the common window. Alpha and beta are measured against SPY, a proxy for the S&P 500 Total Return index. Sharpe, Sortino and alpha use BIL, the 1-3 Month T-Bill ETF, as the risk-free rate."` (write `1 year` for N = 1); when `years` is `None`: `"Not available: the common window is shorter than 1 year."`. `gaps` as above.
  - `COMPARE_ALLOCATION` -> `{"rows": [...], "gaps": [...]}`. One row per allocation row with weights: `{"Name": name, "<class>": percent for each class in classes, "Basis": basis}`; each row whose `weights` is `None` is NOT a row but a gap string `"not available for <name>: <reason>"`.
- HTML: `_element_html` draws the window as a paragraph; the chart as ONE SVG with one line per item (the portfolio line and each comparable in distinct palette colours) and a legend of the names beneath it (extend `_chart_svg` or add a sibling; the existing single-line charts must draw exactly as before); the three tables with `_table_html` over `rows`; and every `gaps` string and the risk `note` as paragraphs under their table. A reader must never meet a blank: a section with no VALUE rows prints its gap lines.
- No vendor name anywhere on the page (R8).

**`TESTS/test_compare_elements.py`** (pytest, your own proof; offline): each method's value shape and columns on a record with a NOT_AVAILABLE row; `INPUT_MISSING:compare` when absent; pricing off -> NOT_IN_THIS_VERSION; the HTML of a built page names every row and prints each gap line; an existing single-line chart draws byte-identically to before (compare with `git stash`-free means: build the same single-line chart from the base's expected string, or assert the SVG path data is unchanged).

1. Edit, write the test. 2. Run your test and the three criteria. 3. Commit the code and test (one commit), then the proof and the status flip as separate commits. 4. Report.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR174-g-AC1" cell_refs="AR-g-174"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py 174 build</invocation><expect>^AR-CMP-174-OK</expect></criterion>

<criterion id="AR174-g-AC2" cell_refs="AR-g-174"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py 174 guard</invocation><expect>^AR-CMP-174-OK</expect></criterion>

<criterion id="AR174-g-AC3" cell_refs="AR-g-174"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py 174 regress</invocation><expect>^AR-CMP-174-REGRESS-OK</expect></criterion>

<expected_criteria>AR174-g-AC1,AR174-g-AC2,AR174-g-AC3</expected_criteria>

- AC1: `compute_all(..., compare=...)` returns VALUE for the five elements with the shapes and numbers the checker computes itself, the gap lines in words, and pricing off reads NOT_IN_THIS_VERSION. At base it FAILs (no COMPARE methods).
- AC2: no existing element of the Overview, Multi or Comparison report moves. At base it PASSes.
- AC3: the existing test files plus your own pass, and the branch changed only the files of the cells so far. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_compare_elements.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~330/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-174.layout-comparison-section-elements.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-174`.
<owned_cells>AR-g-174</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR174-g-AC1,AR174-g-AC2,AR174-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~330/IRPT_ANLREQ.TO-AR-g-174.layout-comparison-section-elements.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-174`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR174-g-AC1,AR174-g-AC2,AR174-g-AC3` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `layout_overview.py` is a resident package member; the new methods are reachable only through `compare=`, which no caller passes until AR-g-175; the Overview and every existing element read as before (the guard arm compares every element's status).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change in this cell (the grant is AR-g-172).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: 174 build FAIL (no COMPARE_* names), guard PASS, regress PASS. Traps: `_chart_svg` is single-line today and must still draw the existing charts identically; a section with no VALUE rows must print its gaps, never a blank; `_price_based` must include the five methods or pricing off will not read NOT_IN_THIS_VERSION. NOT seen (blind): the rendered pixels (the end-to-end arm checks the HTML text only).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1 FAILs, AC2 PASSes, AC3 PASSes.
