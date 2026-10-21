# TO-AR-g-192 -- the Overview's six Risk Info tables print as tables, not 'The kept answer is not a readable table' (CTO msg 11980 item 2)

<to_id>IRPT_ANLREQ.TO-AR-g-192</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~382</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL12</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-192` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** AR-g-191 (same file, one worker, in order). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~382`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-382` (branch `wk-IRPT_ANLREQ-382`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~382 <0.9.0_WK_IRPT_ANLREQ~382@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W382-S<k>` (check the channel file for `W382` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` from `infra/aws/lambda/investor-reporting` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`. Your worktree is sparse: a test file that fails only because a file outside the sparse cone is missing (an import of `ycharts_client`, a schema under `org/surprise_channel`) is not yours: run the owned test files and the checker, and name any such failure in your report.
- **You are the one worker of chain A (queue 191, then 192).** Both orders edit `layout_overview.py`; the commits of your earlier order are on this branch and their files are in this worktree. You are handed one order at a time.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_enrich2_checks.py` (read it; you cannot edit it). It builds its own inputs (the repository's own producer test fakes, the real maps) and computes every expected value itself, independent of your code: if your result and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both results, and stop on that criterion.

### THE CELL (`AR-g-192`, inlined)

**What this cell is.** The CTO ruled (msg 11980): the six lines "The kept answer is not a readable table." on the Overview's page 21 (report page 7, Risk Info) are a FWD-9 defect. Found and reproduced offline by the issuer: the Overview map (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json`) elements p7.e02 Alpha, p7.e03 Beta, p7.e05 Sharpe, p7.e06 Sortino, p7.e07 Max Drawdown and p7.e08 Monthly VaR are `kind` "table" and name BOTH `columns` (five periods, for example `alpha_1y` .. `alpha_15y`) AND a `statistic` (`alpha_1y`). In `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py`, `_compute_own_series` takes the column-by-column path (`_column_statistics`, which returns a dict `{label: value}` the table prints) only when the element has NO `statistic`; with a statistic it returns the first column's scalar, and a scalar is not a table, so `_element_html` prints the fallback sentence. Std dev and the returns table name no statistic and print correctly.

**Do exactly this.**
1. `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py`, `_compute_own_series`: take the column path when `columns` is a non-empty list and (the element has no `statistic` OR the element's kind is "table" (`acc.get("kind") == "table"`)). A non-table element with a `statistic` keeps its scalar. Nothing else changes in the file.
2. `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py`: its helper `_wired_docs()` builds table elements with `columns: [stat]` and `statistic: stat`; the test `test_wired_statistics_compute_from_the_kept_benchmark_and_the_held_yield` reads their `value` as a scalar. They are table elements, so after your change their value is the dict `{"Beta 1Y": v}` (the label is `_column_label`'s: the statistic words with the period upper-cased). Update that test's expectations to read the number from the dict; do not weaken any assertion otherwise. If another test in this file or in `test_layout_own_series_columns.py` fails for the same reason, update it the same way and say which.
3. Add at least two tests, which FAIL on the old code (run them first and say so), to `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_own_series_columns.py`: a table element with five `columns` and a `statistic` yields a dict with one labelled entry per column (an `n/a` cell for a column the series cannot work out) and `_element_html` prints a `<table>`, never the fallback sentence; a `kind` "number" element with a `statistic` and `columns` still yields the scalar.
4. Run the two acceptance invocations; write the proof instance; commit; flip the order to complete only on both PASS and a VALID proof. Also run the fixture-Overview byte-identity tests `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_commentary.py` and `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_commentary_standalone_pdf.py`: they must still pass unchanged (they do not use these elements); if one fails, report it and do not re-pin.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR192-g-AC1" cell_refs="AR-g-192"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_enrich2_checks.py p21</invocation><expect>^AR-ENRICH2-p21-OK$</expect></criterion>

<criterion id="AR192-g-AC2" cell_refs="AR-g-192"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_enrich2_checks.py tests192</invocation><expect>^AR-ENRICH2-tests192-OK passed=[0-9]+$</expect></criterion>

<expected_criteria>AR192-g-AC1,AR192-g-AC2</expected_criteria>

- AC1: the REAL producer's Overview over a ten-year synthetic history prints the six Risk Info elements as tables with one row per column (Alpha 1Y .. 15Y and the rest), cells a number or n/a, and the phrase 'not a readable table' occurs 0 times. At base it FAILs (5 times).
- AC2: the two owned test files pass (58 at the base) and at least 60 ran. At base it FAILs (58 ran).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_own_series_columns.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~382/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-192.risk-info-tables-with-columns-and-a-statistic-print-as-tables.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-192`.
<owned_cells>AR-g-192</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR192-g-AC1,AR192-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~382/IRPT_ANLREQ.TO-AR-g-192.risk-info-tables-with-columns-and-a-statistic-print-as-tables.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-192`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR192-g-AC1,AR192-g-AC2` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one lambda-tree source file and two test files edited in the worker's worktree; nothing is deployed, no AWS call, no network; the change reaches the host only through a later resident release (r34t) under a never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: both criteria FAIL at base; the checker was calibrated by the issuer against the reference fix in a sparse scratch worktree (p21 OK) and mutants: the fix reverted, the column path for one-column elements only, each fails. Traps: weakening the one existing test instead of updating its expectation, changing the scalar of a non-table element, re-pinning a fixture hash (none should move), editing the checker. NOT seen (blind): the live series (run 7M reads the page).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1 and AC2 FAIL.
