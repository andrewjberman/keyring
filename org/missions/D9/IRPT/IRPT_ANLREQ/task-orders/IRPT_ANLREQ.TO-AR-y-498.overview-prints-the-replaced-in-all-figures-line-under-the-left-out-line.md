# TO IRPT_ANLREQ.TO-AR-y-498.overview-prints-the-replaced-in-all-figures-line-under-the-left-out-line -- BUILD AND PROVE OFFLINE: the Overview prints "Replaced in all figures: X by Y (same asset class and sub asset class)." directly under the left-out line, with the low-confidence suffix

<to_id>IRPT_ANLREQ.TO-AR-y-498.overview-prints-the-replaced-in-all-figures-line-under-the-left-out-line</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~370</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ157</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-498` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-SWAP model leg, graded under FWD-2 (PRD v0.25 and v0.26) | **depends_on:** CTO ruling on run 7N (the PDF never names the BREIT swap); AR-y-461's read `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/SWAP_LEG_READ.md`; CTO ruling v0.26 (kimi-k3, no web search, below 0.80 flagged)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~370`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-370` (branch `wk-IRPT_ANLREQ-370`), provisioned by the issuer from the current branch. FIRST confirm with `git -C C:/dev/wk-irpt-anlreq-370 branch --show-current` that it prints `wk-IRPT_ANLREQ-370` and that this order file exists in it; if not, STOP and report WITHOUT touching any other worktree or branch. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~370 <0.9.0_WK_IRPT_ANLREQ~370@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W370-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII; stdlib only unless the order says otherwise).
- **No AWS call, no network, no model call, no push, no deploy, no release build.** Every model call in a test is a fake `send`. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first; `controls` holds `mutant` and `determinism` only), with `to_id` exactly the order's id; run `python .tools/proof-of-spec-check.py <instance> "AR498-y-AC1,AR498-y-AC2,AR498-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID and only after EVERY other edit you intend is committed (a status of complete removes your path grant). The instance's check-script reference is pinned to a commit that EXISTS (commit the script first, then pin it). A test file that leaks `sys.path` makes other files fail at collection in some orders: keep pytest lines in the order written.
### THE CELL (`AR-y-498`)

*What and why.* CTO ruling (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_IRPT_ANLREQ_RUN_7N_SWAP_NOT_IN_PDF_20261021.md`, @26e0df877f; read it first): on the saved run-7N Overview the line `Left out of all figures: ZQXWVK...` prints, but BREIT (replaced by CTO) appears nowhere: `layout_overview._excluded_line` prints only the NON-replaced swap records. The run document names the swap; the PDF does not: a silent swap. This cell prints the replaced swaps too.

*The change.* In `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py` only (read `_excluded_line` and the place where its line is placed in the page HTML first, and mimic that placement and escaping): add `_replaced_line(run_doc)` and print its result DIRECTLY UNDER the left-out line, in the same element style, on the same page, escaped exactly as the left-out line's text is. For every swap record in `run_doc["swaps"]` (in order) whose `status` is `"REPLACED"`, one item `<proxy_for> by <proxy> (same asset class and sub asset class)`; when that record's `low_confidence` is True the parenthesis reads `(same asset class and sub asset class, a low-confidence match)`. The line is `Replaced in all figures: ` + the items joined by `"; "` + `.` EXACTLY, for example `Replaced in all figures: BREIT by CTO (same asset class and sub asset class).` and with two rows `Replaced in all figures: BREIT by CTO (same asset class and sub asset class); XYZ by DDD (same asset class and sub asset class, a low-confidence match).` The line never carries an amount or a number. When no record is REPLACED there is NO line and the HTML is byte-equal to today's; when records are only left-out ones the HTML is byte-equal to today's too. The two lines may both appear (left-out first, replaced directly under it). The strings are module constants (`REPLACED_PREFIX = "Replaced in all figures: "`, `REPLACED_PARENS = "(same asset class and sub asset class%s)"`, `REPLACED_LOW = ", a low-confidence match"`, `REPLACED_JOIN = "; "`).

*Tests (FAILING-FIRST).* New `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_replaced_line.py` in the style of `tests/test_layout_excluded_line.py` (read it): write it first, run it against the UNCHANGED module and record the failure count, then make the change and see it pass. It PINS the exact strings above (the one-row line; the two-row line with `; ` and the low-confidence parenthesis; the line sits after the left-out line and before the next element when both exist; HTML-escaped symbols such as `<b>X&Y`; no line without a REPLACED record; the HTML of a run with no swaps and of a run with only left-out records is byte-equal to the HTML of the unchanged module, which the test builds from the same fixtures by deleting the new line from the result). Edit `tests/test_layout_excluded_line.py` ONLY if one of its assertions fails because it asserts the ABSENCE of a replaced ticker in the whole page (the docstring sentence that a REPLACED record is "never named" in the LEFT-OUT line stays true; do not reword it beyond adding "in the left-out line"); any other red test elsewhere is reported as a row, not edited.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~370/`: `check_replaced_line.py` (stdlib only, ruff clean, offline). It imports `layout_overview` BY PATH from the worktree and builds the line through the module's own function on six fixture swap lists, printing `REPLACED-LINE-OK cases=6 exact_text=yes join=yes low_conf=yes no_line_when_none=yes escaped=yes` or `REPLACED-LINE-BAD <why>` (rc 1). `--selftest` mutates the module text in memory four ways (the join `"; "` changed to `", "`; the low-confidence suffix removed; the prefix text changed to `Replaced: `; REPLACED records filtered out so no line prints) and prints `CONTROL-FIRES` only when ALL FOUR read BAD. Commit order: the code and test edits as ONE commit first, message citing AR-y-498; then your deliverables and instance.

---

## ACCEPTANCE

<criterion id="AR498-y-AC1" cell_refs="AR-y-498"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~370/check_replaced_line.py</invocation><expect>^REPLACED-LINE-OK cases=6 exact_text=yes join=yes low_conf=yes no_line_when_none=yes escaped=yes$</expect></criterion>
<criterion id="AR498-y-AC2" cell_refs="AR-y-498"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~370/check_replaced_line.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR498-y-AC3" cell_refs="AR-y-498"><invocation>(cd infra/aws/lambda/investor-reporting && python -m pytest ycharts/research/tests/test_layout_replaced_line.py ycharts/research/tests/test_layout_excluded_line.py ycharts/research/tests/test_layout_overview.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)</invocation><expect>^[0-9]+ passed in </expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~370/IRPT_ANLREQ.TO-AR-y-498.overview-prints-the-replaced-in-all-figures-line-under-the-left-out-line.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-498.overview-prints-the-replaced-in-all-figures-line-under-the-left-out-line`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR498-y-AC1,AR498-y-AC2,AR498-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-498</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_replaced_line.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_excluded_line.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~370/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-498.overview-prints-the-replaced-in-all-figures-line-under-the-left-out-line.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test files only; nothing is deployed, built into a release or run against AWS or the model; the resident release that carries the swap leg is built by 2.0.0_SA_COO~G2 and applied by IB2 under its own pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker; no IAM change in the swap leg.
comp-adversary: RUN -- by reading the contract C-SWAP, the swap rule and the interface above against this cell; the lens: a silent swap (a replaced row with no line), a number or amount reaching the line, an unescaped symbol, the join or the suffix off by a character, the line printed above the left-out line or on another page, a changed HTML when no swap is replaced, a left-out test weakened to pass, a control that cannot fire. NOT seen (blind): the live model's answers and the deployed resident bytes; denominator: 3 criteria.
</preflight>
