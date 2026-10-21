# TO-AR-g-191 -- a kept row left out of the figures is named on the page, ticker and reason only (CTO msg 11980 item 1)

<to_id>IRPT_ANLREQ.TO-AR-g-191</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~382</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL12</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-191` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** Y2's AR-y-492..494 (drained: the swap records exist). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~382`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-382` (branch `wk-IRPT_ANLREQ-382`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~382 <0.9.0_WK_IRPT_ANLREQ~382@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W382-S<k>` (check the channel file for `W382` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` from `infra/aws/lambda/investor-reporting` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`. Your worktree is sparse: a test file that fails only because a file outside the sparse cone is missing (an import of `ycharts_client`, a schema under `org/surprise_channel`) is not yours: run the owned test files and the checker, and name any such failure in your report.
- **You are the one worker of chain A (queue 191, then 192).** Both orders edit `layout_overview.py`; the commits of your earlier order are on this branch and their files are in this worktree. You are handed one order at a time.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_enrich2_checks.py` (read it; you cannot edit it). It builds its own inputs (the repository's own producer test fakes, the real maps) and computes every expected value itself, independent of your code: if your result and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both results, and stop on that criterion.

### THE CELL (`AR-g-191`, inlined)

**What this cell is.** The CTO ruled (msg 11980): a reader must know when the figures exclude a holding the filer kept. Run 7L (an Overview with the unknown ticker ZQXWVK kept as typed) was READY, and ZQXWVK appears nowhere in the 42 pages. The backend swap pass already records the row: `run_doc["swaps"]` is a list of records, one per UNRESOLVED holding, in row order; a record with `status == "REPLACED"` was swapped for a substitute (the substitute is analysed; the existing disclosure names it), any other `status` means the holding was LEFT OUT of every figure. Such a record carries `proxy_for` (the client's ticker), `status`, and `why`: `NO_CLASS` (no asset class is held for it), `NO_CANDIDATE` (no replacement in its class), `NONE_PRICED` (no replacement had a price history). No record carries an amount. The layout (`infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py`, `build(run_doc, ...)`) receives `run_doc` and prints nothing about them.

**Do exactly this.**
1. `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py`: add `_excluded_line(run_doc)` returning None when `run_doc.get("swaps")` holds no record with `status != "REPLACED"`, else the ONE line `Left out of all figures: <ticker>, <reason>.` with the items joined by `; ` when there are several: `<ticker>` is `proxy_for`, `<reason>` maps `NO_CLASS` to `no asset class is held for it`, `NO_CANDIDATE` to `no replacement in its class is available`, `NONE_PRICED` to `no replacement had a price history`, and any other `why` to `it could not be analysed`. Example: `Left out of all figures: ZQXWVK, no asset class is held for it.` Ticker and reason only; never an amount; a REPLACED record is never named.
2. In `build(...)` print that line, when it is not None, as `<p class="na">...</p>` (the text through `_e`) appended after the blocks of the page that holds the FIRST element whose label starts with `Top 10 Holdings` (the Overview's page 9, the Multi-Comp's page 15); when the map has no such element, after the blocks of the first page. Nothing else in `build` changes, and a run with no left-out row produces exactly the HTML it produced before (the fixture-Overview byte-identity tests must still pass unchanged).
3. NEW test file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_excluded_line.py` (at least four tests, which FAIL on the old code; run them first and say so): no `swaps` key, and only REPLACED records, give no line and the same HTML as before; one left-out record gives exactly the line above; two left-out records give the items joined by `; `; the line sits inside the page section that holds the `Top 10 Holdings` element (build a tiny map with two pages through `lo.build`, the way `test_layout_overview.py` does), and with no such element it sits on the first page; an unknown `why` gives `it could not be analysed`; the ticker is HTML-escaped.
4. Run the two acceptance invocations; write the proof instance; commit; flip the order to complete only on both PASS and a VALID proof.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR191-g-AC1" cell_refs="AR-g-191"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_enrich2_checks.py excl</invocation><expect>^AR-ENRICH2-excl-OK$</expect></criterion>

<criterion id="AR191-g-AC2" cell_refs="AR-g-191"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_enrich2_checks.py tests191</invocation><expect>^AR-ENRICH2-tests191-OK passed=[0-9]+$</expect></criterion>

<expected_criteria>AR191-g-AC1,AR191-g-AC2</expected_criteria>

- AC1: the REAL producer, over an Overview and a Multi-Comp with two UNRESOLVED holdings (one left out, one replaced), prints exactly one line `Left out of all figures: ZQXWVK, no asset class is held for it.` on the page that holds the Top 10 Holdings element, naming no replaced row and no amount; a run with no left-out row prints none. At base it FAILs (no line).
- AC2: the new test file passes with at least 4 tests. At base it FAILs (no file).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_excluded_line.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~382/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-191.a-kept-row-left-out-of-the-figures-is-named-on-the-page.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-191`.
<owned_cells>AR-g-191</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR191-g-AC1,AR191-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~382/IRPT_ANLREQ.TO-AR-g-191.a-kept-row-left-out-of-the-figures-is-named-on-the-page.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-191`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR191-g-AC1,AR191-g-AC2` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one lambda-tree source file and one new test file edited in the worker's worktree; nothing is deployed, no AWS call, no network; the change reaches the host only through a later resident release (r34t) under a never-widen pair. The page gains one sentence when a holding was left out; no amount is printed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: both criteria FAIL at base; the checker was calibrated by the issuer against the reference fix in a sparse scratch worktree (excl OK) and mutants: the line on the first page, a generic reason, replaced rows named too, each fails. Traps: printing an amount, naming the replaced row, changing the HTML of a run with no left-out row (the fixture byte-identity tests), editing the checker. NOT seen (blind): the live reasons beyond NO_CLASS (run 7M reads one).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1 and AC2 FAIL.
