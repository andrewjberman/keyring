# TO-AR-g-186 -- the report prints no false 'no row has a value' sentence, explains the n/a periods in words, keeps a comparison heading with its table, and prints no raw {portfolio_name} (7J read, Findings 2 and 3; 7f page 3)

<to_id>IRPT_ANLREQ.TO-AR-g-186</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~359</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL8</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-186` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** the 7J read (Findings 2 and 3) and CTO msg 11932. Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~359`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-359` (branch `wk-IRPT_ANLREQ-359`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~359 <0.9.0_WK_IRPT_ANLREQ~359@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W359-S<k>` (check the channel file for `W359` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` from `infra/aws/lambda/investor-reporting` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_gapnote_checks.py` (read it; you cannot edit it, and you cannot edit its fixture). It builds its own inputs and computes every expected value itself, independent of your code: if your result and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both results, and stop on that criterion.

### THE CELL (`AR-g-186`, inlined)

**What this cell is.** The issuer's read of run 7J's served Multi-Comp PDF and of the 7f Overview sample found three presentation defects, all in `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py`:
1. **A false gap sentence.** `_gap_paragraphs` prints `COMPARE_EMPTY_LINE` ("Not available: no row of this section has a value.") when a section has NO gaps, so it appears under the periodic-returns, risk and allocation tables of a report whose rows all carry values. The only real gaps on those pages are the 3Y, 5Y and 10Y cells, which read a bare `n/a` with no words (the common window is 2.4 years).
2. **A stranded heading.** The heading "Comparison: asset allocation" printed at the bottom of one page with its table on the next.
3. **A raw template placeholder.** The Overview's element labels come from the map with the portfolio name replaced by the literal `{portfolio_name}` (for example "Periodic Return - Total: {portfolio_name}"), and the layout prints that literal on the page.

**Do exactly this.**
1. `_gap_paragraphs(gaps)` returns the empty string when there are no gap lines (print nothing; remove `COMPARE_EMPTY_LINE` if nothing else uses it). A section with gap lines prints them as before.
2. For the periodic-returns element only (`COMPARE_RETURNS`): after the table, when one or more period columns read `n/a` in EVERY row, print one paragraph (class `na`) `Not available: <periods> returns, because the common window is shorter than those periods.` where `<periods>` lists those column labels in table order joined with `, ` and the last with ` and ` (three periods: `3Y, 5Y and 10Y`; two: `5Y and 10Y`; one: `10Y`). When no column is empty print nothing.
3. Each of the five comparison elements is rendered as `<div class="el cmp" data-id=...>` (an element whose method is in `COMPARE_METHODS`; every other element keeps `class="el"`), and the page style gains the rule `.cmp { break-inside: avoid; page-break-inside: avoid; }` (put it just before the `.el` rule), so a comparison heading is never left apart from its table or chart.
4. In `_element_html` the label text has the literal `{portfolio_name}` replaced by `Your portfolio` before it is escaped and printed (every element label, not only the periodic-return one).
5. Tests, each of which FAILS before your change (run them first and say so in your report): in `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_compare_elements.py` or `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py` (your choice, at least three tests in all): a section with no gaps prints no gap paragraph; the periodic-returns line for three, two and one empty period columns and none; the `cmp` class and the style rule; a label with `{portfolio_name}` prints `Your portfolio`. Keep every existing test passing.
6. Run the three acceptance invocations; write the proof instance; commit; flip the order to complete only on three PASS and a VALID proof.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR186-g-AC1" cell_refs="AR-g-186"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_gapnote_checks.py gaps</invocation><expect>^AR-GAPNOTE-gaps-OK$</expect></criterion>

<criterion id="AR186-g-AC2" cell_refs="AR-g-186"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_gapnote_checks.py placeholder</invocation><expect>^AR-GAPNOTE-placeholder-OK$</expect></criterion>

<criterion id="AR186-g-AC3" cell_refs="AR-g-186"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_gapnote_checks.py tests</invocation><expect>^AR-GAPNOTE-tests-OK passed=[0-9]+$</expect></criterion>

<expected_criteria>AR186-g-AC1,AR186-g-AC2,AR186-g-AC3</expected_criteria>

- AC1: the REAL producer's served Multi-Comp HTML: the false sentence is nowhere, the line about 3Y, 5Y and 10Y appears once, the five comparison elements are `el cmp`, and the `.cmp` rule holds break-inside and page-break-inside avoid. At base it FAILs.
- AC2: the REAL producer's served Overview HTML has no {portfolio_name} and prints 'Periodic Return - Total: Your portfolio'. At base it FAILs (10 occurrences).
- AC3: the four owned layout test files pass (77 at the base) and at least 80 ran. At base it FAILs (77 ran).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_compare_elements.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~359/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-186.report-presentation-no-false-gap-sentence-heading-kept-with-table-and-no-raw-placeholder.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-186`.
<owned_cells>AR-g-186</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR186-g-AC1,AR186-g-AC2,AR186-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~359/IRPT_ANLREQ.TO-AR-g-186.report-presentation-no-false-gap-sentence-heading-kept-with-table-and-no-raw-placeholder.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-186`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR186-g-AC1,AR186-g-AC2,AR186-g-AC3` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one lambda-tree source file and two test files edited in the worker's worktree; nothing is deployed, no AWS call; the change reaches the host only through a later resident release under a never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: all three criteria FAIL at base; the checker was calibrated by the issuer against a reference fix in a scratch worktree (both arms OK) and five mutants (the empty line kept, wrong period words, the class on one element only, a style rule without page-break-inside, the placeholder replaced with nothing), each of which fails. Traps: dropping the gap sentences of a section that HAS gaps, printing the n/a line on a section that has none, the label replacement only on one element, editing the checker. NOT seen (blind): the real renderer's page breaks (the checker proves the rule and classes in the HTML, not the PDF; the next filing's PDF is the proof).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1, AC2 and AC3 FAIL.
