# TO-AR-g-165 -- the Opal-built report's price pages, part 3: the two as-of lines and the two legends (row 3c22; CTO msgs 10729, 10734, 10743)

<to_id>IRPT_ANLREQ.TO-AR-g-165</to_id>
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

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-165` (`decompositions/IRPT_ANLREQ_DECOMP_R57_G.md`) |
**outcome_ref:** FWD-7 | **depends_on:** `AR-g-164` (the same worker, the same chain: your branch already holds its commits; both add statistics to the one statistic engine). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~302`, continuing on `C:/dev/wk-irpt-anlreq-302` (branch `wk-IRPT_ANLREQ-302`) after `AR-g-164`. Your prior commits are inherited state.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~302 <0.9.0_WK_IRPT_ANLREQ~302@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. Never commit ` M portal` or a modified `.parquet` fixture.
- A row id has the form `IRPT_ANLREQ-D2-W302-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Do not touch anything outside the `<paths>` block. Run Python with plain `python`.

### THE CELL (`AR-g-165`, inlined)

**AMENDMENT 1 (issuer, 2026-10-19, on worker ~302's row IRPT_ANLREQ-D2-W302-S1; gate limb: none graded, an in-decomposition amendment of a grant):** `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py` line 754 pins the number of `OWN_SERIES` elements of the real map: `assert len(res) == len(series) == 9`. Your cell adds 4, so it must read `18` on YOUR branch (the three round-57 cells that add `OWN_SERIES` elements each move it by their own delta, 163 by 8, 164 by 5, 165 by 4; the issuer reconciles the line to 26 at the merge). That file is now in your `<paths>`. Change ONLY that number (and, if the line wraps, nothing else); do not weaken the assertion, do not touch any other line of the file. Then re-run AC3.

Files: `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py` (the statistic engine `statistic_of`, which AR-g-164 extended) and `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json`.

Four `text` elements read NOT_IN_THIS_VERSION with pricing on because their `source` names a vendor call (`portfolio_info`, or the last point of `portfolio_level_series`). Re-point each `source` to `OWN_SERIES` (the shape of `p7.e05`: `{"call": "portfolio_level_series", "columns": [], "computed": "OWN_SERIES", "field": "$.chart_data[0][0].raw_data", "sleeve": null, "statistic": "<name>"}`) and add two statistics to the engine. Both read only the last point of the level series `points` ([(ms, level)], ms in UTC milliseconds) and return a string:

| element | statistic | the string it returns |
|---|---|---|
| `p2.e07` Periodic Return - Total as-of date | `as_of_text` (NEW) | `As of YYYY-MM-DD`, the UTC date of the last point |
| `p2.e16` Annual Return - Total as-of date | `as_of_text` | the same |
| `p2.e03` Cumulative Return & Basic Info legend | `legend_text` (NEW) | `Opal portfolio: buy-and-hold from the accepted amounts, priced to YYYY-MM-DD.` (the same date) |
| `p6.e20` Drawdown Info legend | `legend_text` | the same |

Make `_price_based(src)` true for both statistics (the OWN_SERIES method already does that; keep it true) so pricing OFF still reads NOT_IN_THIS_VERSION. A string result must pass through the producer's section writer as it already does for text elements; if it does not, file a row naming the refusal and stop on that criterion.

Then add ONE new test file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_pages_text.py` (pytest): over the REAL map through the shipped producer (harness as in `test_price_pages_series.py`, which you wrote under AR-g-164; reuse its 133-month readers by copying the helper), assert the four elements VALUE with the exact strings above for `as_of="2026-10-14"`; that pricing OFF leaves all four NOT_AVAILABLE / NOT_IN_THIS_VERSION; and unit-test `statistic_of` for both statistics on a made-up series whose last point is a known date.

1. Edit; write the test; run your test and the three criteria. 2. Commit the code, map and test (code first), then the proof and the status flip as separate commits. 3. **Report** the commit hashes and the three criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR165-g-AC1" cell_refs="AR-g-165"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 165 build</invocation><expect>^AR-PRICE-165-OK</expect></criterion>

<criterion id="AR165-g-AC2" cell_refs="AR-g-165"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 165 guard</invocation><expect>^AR-PRICE-165-OK</expect></criterion>

<criterion id="AR165-g-AC3" cell_refs="AR-g-165"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 165 regress</invocation><expect>^AR-PRICE-165-REGRESS-OK</expect></criterion>

<expected_criteria>AR165-g-AC1,AR165-g-AC2,AR165-g-AC3</expected_criteria>

- AC1: the four text elements are VALUE with pricing on and carry exactly `As of 2026-10-14` (two lines) and `Opal portfolio: buy-and-hold from the accepted amounts, priced to 2026-10-14.` (two legends). At base it FAILs.
- AC2: with pricing off every element reads exactly as at the base; with pricing on nothing outside the 17 round-57 elements moves and the nine base VALUE elements are byte-equal. At base it PASSes.
- AC3: runs six existing producer and layout test files, then that the branch changed only your files, your folder, the order and the channel file. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. `opal_producer.py` and every other file are read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_pages_text.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~302/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-165.price-pages-text-elements.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R57_G.md</decomp_doc> round 57, workstream ~G, cell `AR-g-165`.
<owned_cells>AR-g-165</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR165-g-AC1, AR165-g-AC2, AR165-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~302/IRPT_ANLREQ.TO-AR-g-165.price-pages-text-elements.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-165`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code, map and test first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR165-g-AC1,AR165-g-AC2,AR165-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~282/IRPT_ANLREQ.TO-AR-g-161.pricing-as-of-calendar-frontier.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 3.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `layout_overview.py`, the overview map and one new test; no deploy, no AWS call, no network. Both are resident package members: the change reaches the served report only through a later resident release under its own never-widen pair; four text elements move from NOT_IN_THIS_VERSION to VALUE when pricing is on.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change. comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- `ar_price_checks.py` was dry-run at the base (build FAIL, guard PASS, regress PASS). Traps: the legend carries no holding count or source list on purpose (the engine sees only the series; a count of all holdings overstates coverage when one holding is unpriced; the sources are the claim of the price table and of run.json); a text value must survive the producer's section writer. NOT seen (blind): the rendered pixels; no reference fix was dry-run.
</preflight>

- Cut on the CTO's rulings (msgs 10729, 10734, 10743) by the issuer inside its own decomposition. Risk WORLD: the floor of an infrastructure path. Base: AR165-g-AC1 FAILs, AR165-g-AC2 PASSes, AR165-g-AC3 PASSes.
