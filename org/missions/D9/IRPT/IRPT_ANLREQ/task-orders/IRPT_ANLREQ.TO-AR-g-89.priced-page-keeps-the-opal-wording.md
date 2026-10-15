# TO-AR-g-89 -- a priced Opal page keeps the Opal wording: the producer builds the page with the Opal form of the layout, so it names no vendor and no time budget

<to_id>IRPT_ANLREQ.TO-AR-g-89</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~189</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-89` (`decompositions/IRPT_ANLREQ_DECOMP_R16_G.md`) |
**outcome_ref:** FWD-7 (the Opal page rule R8) | **depends_on:** `AR-g-86` (merged `1c84d38bf4`; its worker's row `IRPT_ANLREQ-D2-W186-S1` found the defect).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~189`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-189` (branch `wk-IRPT_ANLREQ-189`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/` and `org/missions/D9/IRPT` on disk (it has no portal sub-worktree; your cell does not touch the portal). Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~189 <0.9.0_WK_IRPT_ANLREQ~189@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W189-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`).

### Read first (under `C:/dev/wk-irpt-anlreq-189/infra/aws/lambda/investor-reporting/ycharts/research/`)

- `opal_producer.py`: `produce` and `produce_package`, and the two calls `lo.build(...)` that end with `pricing` (one in each).
- `layout_overview.py`: `build` (line 1104), `_element_html` (1040), `_reason_line` (953), and the constants `SOURCE_CREDIT`, `OPAL_SOURCE_CREDIT` (69) and `OPAL_NOT_IN_VERSION_LINE` (70). In `build`, the `pricing` argument chooses the PAGE WORDING (False is the Opal form: the credit "Data: Opal Capital", no vendor name, "Not available in this version."); the values come from `computed`, which is passed in already worked out. You do not change this file.
- `tests/test_opal_producer.py` (the fakes: `make_stores` and the others) and `tests/test_opal_producer_prices.py` (merged `AR-g-86`: how a priced run is set up).

### THE CELL (`AR-g-89`, inlined)

`AR-g-86` made the producer able to run priced. Its worker found (row `IRPT_ANLREQ-D2-W186-S1`) that a priced page, built with `build(..., pricing=True)`, prints the YCharts wording of the vendor path: the footer "Data: YCharts", "YCharts' data does not give this element ..." lines, and "outside the run's time budget" lines. The Opal page rule R8 says an Opal page names no vendor and no time budget. The figures are already worked out by `compute_all(..., pricing)`; `build` only needs the Opal form of the wording.

**`ycharts/research/opal_producer.py`, exactly this:**
1. In `produce`, the call `lo.build(run_doc, {}, map_doc, brand, computed, None, None, held_sources, classified, None, pricing)` passes `False` as its last argument instead of `pricing`.
2. In `produce_package`, the call `lo.build(run_doc, {}, map_doc, brand, computed, None, None, held_sources, classified, None, pricing, commentary=commentary)` passes `False` there too.
3. A two-line comment at each call: the layout's flag chooses the page wording (Opal form when False); `compute_all` above already took the real `pricing` flag, so priced figures still print.
4. Nothing else changes (`produce_commentary_pdf` already builds the Opal form).

**Tests.** A NEW file `ycharts/research/tests/test_opal_producer_page_wording.py`, offline, self-contained (its own small map, readers and `as_of` `"2026-10-14"`; reuse the fakes of `tests/test_opal_producer.py` by importing it; the map has a BUILDER_ONLY title, a call-sourced element, an `OWN_SERIES` element with statistic `total_return_1y` and one with statistic `sharpe_1y`, on call `portfolio_level_series`; the readers serve made-up monthly levels from 2024-07-14 to 2026-10-14), with these exact test function names (the checker looks for each by name):
`test_priced_page_names_no_vendor_and_no_time_budget` (no "YCharts" and no "time budget", case-insensitive, in the page the render received), `test_priced_package_page_names_no_vendor` (`produce_package`), `test_priced_page_prints_the_figure_and_the_opal_credit` (the number of "Data: Opal Capital" credits equals the number of pages, and a printed value is present), `test_unavailable_lines_use_the_opal_wording` (the Sharpe element reads "Reason: INPUT_MISSING:risk_free" and not "YCharts' data").

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR89-g-AC1" cell_refs="AR-g-89"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g89_checks.py g89</invocation><expect>^AR-G89-OK</expect></criterion>

<criterion id="AR89-g-AC2" cell_refs="AR-g-89"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g86_checks.py regress</invocation><expect>^AR-G86-REGRESS-OK</expect></criterion>

<expected_criteria>AR89-g-AC1,AR89-g-AC2</expected_criteria>

- AC1 runs the producer priced on fakes six ways (the page of `produce`, the credit on every page, the figure printed, the Opal wording of an unavailable line, the page of `produce_package` with its commentary page, and the page with pricing off as it was), then checks the four named tests exist and pass. At base it FAILs.
- AC2 runs eight existing test files one at a time (163 tests, among them the producer's and the price stage's) and needs all of them to pass. At base it PASSes. Run it under `timeout 560`: it takes one to three minutes.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_page_wording.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~189/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-89.priced-page-keeps-the-opal-wording.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R16_G.md</decomp_doc> round 16, workstream ~G, cell `AR-g-89`.
<owned_cells>AR-g-89</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR89-g-AC1, AR89-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~189/IRPT_ANLREQ.TO-AR-g-89.priced-page-keeps-the-opal-wording.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-89`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR89-g-AC1,AR89-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the lines you changed with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `produce` and `produce_package` are the only callers of `lo.build` in this file and run priced only when a caller sets `stores["pricing"]`, which no caller does until the wiring cell; with pricing off the argument was already False, so the change is a no-op there. The layout is not edited, so its YCharts path (`pricing=True` from its command line) is untouched. Nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against the worker row W186-S1 and the layout's R8 comments (lines 69, 1058). Traps: the compute flag changed instead of the page flag (the figures would vanish); only one of the two `build` calls changed (the package page would still name the vendor); the commentary page of the package keeping the vendor credit; the pricing-off page changing. The checker feeds a green arm (a reference build passes all six cases and the four named tests, and the 163 regress tests) and two mutant arms (the priced page flag restored in `produce`: 3 cases fail; restored in `produce_package`: 1 case fails).
</preflight>

- Cut on the AR-g-86 worker's row `IRPT_ANLREQ-D2-W186-S1` and the issuer's reference build. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR89-g-AC1` FAILs and `AR89-g-AC2` PASSes (163), as expected.
- The row proposed either passing `pricing=False` to the build or making the layout's `pricing=True` branch Opal-safe; the first is the smaller change and leaves the YCharts path of the layout alone.
