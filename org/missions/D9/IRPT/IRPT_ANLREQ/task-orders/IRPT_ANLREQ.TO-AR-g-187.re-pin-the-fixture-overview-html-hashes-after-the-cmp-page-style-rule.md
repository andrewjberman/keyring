# TO-AR-g-187 -- the three pinned HTML hashes of two layout tests move with the one CSS rule AR-g-186 added (measured: removing the rule restores the old hashes)

<to_id>IRPT_ANLREQ.TO-AR-g-187</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~363</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL9</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-187` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** AR-g-186 (merged) and the issuer's full-directory drain run. Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~363`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-363` (branch `wk-IRPT_ANLREQ-363`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~363 <0.9.0_WK_IRPT_ANLREQ~363@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W363-S<k>` (check the channel file for `W363` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **The checks** are the acceptance invocations below (plain `python`, from the worktree root); they print closed lines only.

### THE CELL (`AR-g-187`, inlined)

**What this cell is.** AR-g-186 added one CSS rule to the layout's page style (`.cmp { break-inside: avoid; page-break-inside: avoid; }`, `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py`). Two older tests pin the sha256 of the fixture Overview's HTML (the logo payload normalised) and now fail on it: `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_commentary.py::test_a_no_commentary_is_byte_identical_to_today` and `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_commentary_standalone_pdf.py::test_b_build_is_byte_identical_to_base_with_and_without_the_commentary_keyword`. The issuer MEASURED that the rule is the ONLY difference: removing that one line from the new HTML restores both old pinned hashes exactly (no commentary `475b060b6e2b...`, with commentary `790d953d59fb...`). So the pins move; nothing else about the HTML changed.

**Do exactly this (three constants and their comments; no code, no other test).**
1. `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_commentary.py`: set `BASE_HTML_SHA256` to `3d6dfd48d3a47d59e2e77dbc6cf00c1f59d97aed757dc323f13ab34f75705f71` and extend the comment above it by one sentence: `AR-g-187: re-pinned after AR-g-186 added the .cmp page-style rule, the only difference (removing that rule's line restores the earlier value 475b060b6e2b).`
2. `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_commentary_standalone_pdf.py`: set `BASE_BUILD_SHA256` to the same `3d6dfd48d3a47d59e2e77dbc6cf00c1f59d97aed757dc323f13ab34f75705f71` and `BASE_BUILD_WITH_COMMENTARY_SHA256` to `a9d38267d2857b8bac88da552da14e48fa2e2582e7d42491fb05b5b48841c087`, each comment extended by the same kind of sentence naming the earlier value (`475b060b6e2b` and `790d953d59fb`).
3. Run the acceptance invocation, write the proof instance, commit, flip the order to complete only on PASS and a VALID proof.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR187-g-AC1" cell_refs="AR-g-187"><invocation>python -m pytest -q -p no:cacheprovider --color=no infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_commentary.py infra/aws/lambda/investor-reporting/ycharts/research/tests/test_commentary_standalone_pdf.py</invocation><expect>^[0-9]+ passed in</expect></criterion>

<expected_criteria>AR187-g-AC1</expected_criteria>

- AC1: the two owned test files pass (at base two tests fail on the old pins). At base it FAILs (2 failed).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_commentary.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_commentary_standalone_pdf.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~363/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-187.re-pin-the-fixture-overview-html-hashes-after-the-cmp-page-style-rule.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-187`.
<owned_cells>AR-g-187</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR187-g-AC1. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~363/IRPT_ANLREQ.TO-AR-g-187.re-pin-the-fixture-overview-html-hashes-after-the-cmp-page-style-rule.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-187`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR187-g-AC1` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- two test files edited (three constants and comments) in the worker's worktree; nothing is deployed, no AWS call; the change reaches no host.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: the criterion FAILs at base; the new values were measured by the issuer by building the fixture HTML with the merged layout, and the single added CSS line was shown to be the only difference (removing it restores both old hashes). Traps: re-pinning to a value that hides another change (the issuer's measurement rules that out for this base), editing any test or code other than the three constants and comments. NOT seen (blind): tests that read the layout through other fixtures (the issuer ran the whole research test directory: only these two failed).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1 FAILs (2 failed).
