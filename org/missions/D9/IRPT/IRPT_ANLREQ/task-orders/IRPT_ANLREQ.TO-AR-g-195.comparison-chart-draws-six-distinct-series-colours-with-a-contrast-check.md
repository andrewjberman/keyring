# TO-AR-g-195 -- the comparison chart draws six distinct series colours, each readable on white (CTO ADJ v31 note on run 7M)

<to_id>IRPT_ANLREQ.TO-AR-g-195</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~385</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL16</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-195` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** none. Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~385`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-385` (branch `wk-IRPT_ANLREQ-385`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~385 <0.9.0_WK_IRPT_ANLREQ~385@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W385-S<k>` (check the channel file for `W385` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` from `infra/aws/lambda/investor-reporting` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`. Your worktree is sparse: a test file that fails only because a file outside the sparse cone is missing (an import of `ycharts_client`, a schema under `org/surprise_channel`) is not yours: run the owned test files and the checker, and name any such failure in your report.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_palette_checks.py` (read it; you cannot edit it). It builds its own inputs (the repository's own producer test fakes, the real maps) and computes every expected value itself, independent of your code: if your result and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both results, and stop on that criterion.

### THE CELL (`AR-g-195`, inlined)

**What this cell is.** The CTO (ADJ v31 note on run 7M) found that on the served Multi-Comp chart Opal Long-Term (#0A1733) and the typed ETF (#000000) are indistinguishable (contrast 1.18:1). The cause is in `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py`, `_palette`: `colors["lines"]` holds four colours (`electric_purple`, `opal_navy`, `midnight_blue`, `black` from the brand spec), three of them near-black navy or black, and `_lines_svg` and `_legend_html` cycle it (`palette[i % len(palette)]`), so a fifth line repeats the first colour and a Multi-Comp can carry six lines (the portfolio and up to five comparables).

**Do exactly this.**
1. `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py`, `_palette`: replace the value of `"lines"` with SIX colours, in this order: `pick("electric_purple", "#5F3BE3")`, `pick("opal_navy", "#163372")`, then four chart-only supplementary colours written as literals with a one-line comment saying they are chart-only (the brand spec has no further accent): `"#D95F02"`, `"#00897B"`, `"#C2185B"`, `"#8A6D00"`. Nothing else in the file changes: `_lines_svg` and `_legend_html` keep their code (the modulo stays; six colours cover six lines). The issuer measured this palette: every colour is at least 3.8:1 against white and every pair is at least 43 apart in CIE76 Delta E.
2. NEW test file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_chart_palette.py` (at least three tests, which FAIL on the old code; run them first and say so): the six `colors["lines"]` are distinct and each at least 3.0:1 against white by WCAG relative luminance; every pair is at least 30 apart in CIE76 Delta E (write the colour arithmetic in the test file; do not import it from the checker); `_lines_svg` on six lines draws six distinct stroke colours and `_legend_html` swatch i equals stroke i; the single-line `_chart_svg` is unchanged.
3. Run the two acceptance invocations; also run `ycharts/research/tests/test_compare_elements.py`, `test_layout_overview.py`, `test_layout_commentary.py` and `test_commentary_standalone_pdf.py` (they must still pass; if one fails because it pins a colour or an HTML hash, report it with the measured difference and re-pin only the pinned value, and say which); write the proof instance; commit; flip the order to complete only on both PASS and a VALID proof.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR195-g-AC1" cell_refs="AR-g-195"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_palette_checks.py palette</invocation><expect>^AR-PALETTE-palette-OK$</expect></criterion>

<criterion id="AR195-g-AC2" cell_refs="AR-g-195"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_palette_checks.py tests</invocation><expect>^AR-PALETTE-tests-OK passed=[0-9]+$</expect></criterion>

<expected_criteria>AR195-g-AC1,AR195-g-AC2</expected_criteria>

- AC1: the layout's own line chart and legend, and the REAL producer's Multi-Comp, draw distinct colours, each at least 3.0:1 against white and every pair at least 30 apart in Delta E, with the legend swatches equal to the strokes. At base it FAILs (a fifth line repeats the first colour; Long-Term and the ETF are 22.6 apart).
- AC2: the new test file passes with at least 3 tests. At base it FAILs (no file).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_chart_palette.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_compare_elements.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~385/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-195.comparison-chart-draws-six-distinct-series-colours-with-a-contrast-check.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-195`.
<owned_cells>AR-g-195</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR195-g-AC1,AR195-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~385/IRPT_ANLREQ.TO-AR-g-195.comparison-chart-draws-six-distinct-series-colours-with-a-contrast-check.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-195`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR195-g-AC1,AR195-g-AC2` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one lambda-tree source file, one new test file and (only if a pinned colour needs it) one existing test file edited in the worker's worktree; nothing is deployed, no AWS call, no network; the change reaches the host only through a later resident release (r34u) under a never-widen pair. The chart's line colours change on Multi-Comp and Comparison reports; the Overview has no multi-line chart.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: both criteria FAIL at base; the checker was calibrated in-process against the reference palette (OK) and four mutants (duplicate colours, a too-light colour, a near-identical pair, the old four colours), each of which fails. Traps: a palette that passes Delta E but not contrast on white, repeating a colour for the fifth and sixth lines, changing the single-line chart, re-pinning a hash without measuring. NOT seen (blind): colour-vision deficiency and greyscale printing (Delta E does not guarantee them).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1 and AC2 FAIL.
