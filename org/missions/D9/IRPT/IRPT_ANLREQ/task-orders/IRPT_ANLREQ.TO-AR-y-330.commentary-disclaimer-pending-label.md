# TO IRPT_ANLREQ.TO-AR-y-330.commentary-disclaimer-pending-label -- the standalone commentary PDF shows a visible "[Opal disclaimer pending approval]" line in place of the placeholder disclaimer prose (CTO msg 7768, call 095e held for Andrew); one constant and its tests; nothing deployed

<to_id>IRPT_ANLREQ.TO-AR-y-330</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~138</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZP</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the infrastructure `<paths>` imply; source and tests only, the worker deploys NOTHING)
**Decomp cell:** `AR-y-330` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the fourth attachment) | **depends_on:** `AR-y-327` (merged `6240c0530d`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~138`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-138` (branch `wk-IRPT_ANLREQ-138`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~138 <0.9.0_WK_IRPT_ANLREQ~138@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W138-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH, no deploy, no upload, no apply, no invoke. Scratch outside the product tree.

### THE CELL (`AR-y-330`, inlined)

*The CTO, msg 7768 (call 095e: the Opal disclaimer for the commentary PDF is HELD for Andrew): "`layout_overview.DISCLAIMER_TEXT` renders as a visible '[Opal disclaimer pending approval]' line, not plausible-looking legal text, while the Ticket Center is internal-only and the PDF says DRAFT. The approved wording is a release gate for any client delivery."*

`AR-y-327` (merged) put placeholder PROSE in the constant `COMMENTARY_DISCLAIMER` in `C:/dev/wk-irpt-anlreq-138/infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py` (about lines 71-73), which reads like real disclaimer text. This cell replaces it with a visible pending label.

1. **Read first:** `layout_overview.py` lines about 65-80 (the two constants) and about 1080-1100 (`_commentary_section`, where `COMMENTARY_DISCLAIMER` is rendered inside `<p class="disclaimer">`), and `ycharts/research/tests/test_commentary_standalone_pdf.py` (lines about 62 and 157 assert `lo.COMMENTARY_DISCLAIMER` is in the HTML). Record what the constant says today.
2. **The change (`layout_overview.py` only):** set `COMMENTARY_DISCLAIMER` to EXACTLY the string `[Opal disclaimer pending approval]` (ASCII, square brackets, no period). Replace the comment above it so it says: the approved wording is held for Andrew (call 095e), this label stands in for it, and the approved wording is a release gate for any client delivery. Change nothing else in the file: the DRAFT mark, the `<p class="disclaimer">` element and its CSS stay as they are.
3. **The tests (NEW file `ycharts/research/tests/test_commentary_disclaimer_pending.py`; copy the style of `test_commentary_standalone_pdf.py`; run with `python -m pytest <file>` from the folder those tests run in):** (a) `COMMENTARY_DISCLAIMER == "[Opal disclaimer pending approval]"`; (b) `build_commentary_only` HTML contains that exact label inside an element of class `disclaimer`, the DRAFT mark, and NO sentence of the old placeholder prose (assert the first six words of the old constant, read from `git show HEAD:<file>` at authoring time and written into the test as a literal, are absent); (c) `build(...)` with `commentary=` and `draft=False` still carries NO disclaimer element (the combined layout is unchanged); (d) a test whose NAME states the scope: `the commentary PDF shows a visible pending label, not plausible legal text`. The two existing assertions in `test_commentary_standalone_pdf.py` read the constant by name and keep passing; change that file only if a case fails, and say so. `before_arm`: run the new tests on the base so (a), (b), (d) FAIL.
4. **Commit** the source and the new test; record the full sha and `git diff --stat <base> <commit>` printing exactly the paths you touched.
5. **Write `r41/DISCLAIMER_PENDING_LABEL_RECORD.json`** in your deliverable folder: `base`, `commit`, `files_changed`, `old_constant` (the old text, read at the base), `new_constant`, `tests` {`added`, `passed`, `failed`}, `before_arm`, `claim`, `not_read` (the rendered PDF bytes).
6. **Write the three checker scripts** named in ACCEPTANCE into your deliverable folder. In your report: the commit, the counts, the before-arm failures.

### ACCEPTANCE

<criterion id="AR330-y-AC1" cell_refs="AR-y-330"><invocation>python C:/dev/wk-irpt-anlreq-138/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~138/tests_check.py</invocation><expect>^TESTS-OK </expect></criterion>
`AR330-y-AC1`: you write `deliverables/0.9.0_WK_IRPT_ANLREQ~138/tests_check.py`: it runs the new test file AND every test file in `ycharts/research/tests/` whose name contains `commentary`, `packager`, `producer` or `layout` (print the file list), parses the counts, and prints `TESTS-OK <new passed> new, <others passed> others, 0 failed` only when the new file has every case (a) to (d) passing and the others have 0 failed; otherwise `TESTS-BAD <why>` and exit 1.

<criterion id="AR330-y-AC2" cell_refs="AR-y-330"><invocation>python C:/dev/wk-irpt-anlreq-138/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~138/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR330-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `layout_overview.py` to a scratch folder OUTSIDE the product tree with `COMMENTARY_DISCLAIMER` set back to the old text, runs the new test file against the copy (with the copy first on the import path), and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR330-y-AC3" cell_refs="AR-y-330"><invocation>python C:/dev/wk-irpt-anlreq-138/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~138/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR330-y-AC3` (a third check, with a reason: the cell edits shared layout code that a later resident release carries): you write `scope_check.py`: it prints `SCOPE-OK` only when `git diff --name-only <base> HEAD` lists only `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py`, the new test file, and paths under `org/missions/D9/IRPT/IRPT_ANLREQ/` (`<base>` = the `base` field of your record JSON, the parent of your first commit of this order, printed); and `git diff <base> HEAD -- infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py` changes exactly the constant and its comment (no other hunk); otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR330-y-AC4J" cell_refs="AR-y-330" judgment="true"/>
`AR330-y-AC4J` (judgment, graded at L9, never by you): the commentary PDF's disclaimer line is a visible pending label that cannot be mistaken for approved legal text, and nothing else in the layout moved.

<expected_criteria>AR330-y-AC1 AR330-y-AC2 AR330-y-AC3 AR330-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~138/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_commentary_disclaimer_pending.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-330</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~138/IRPT_ANLREQ.TO-AR-y-330.commentary-disclaimer-pending-label.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-330`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR330-y-AC1,AR330-y-AC2,AR330-y-AC3,AR330-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one constant and a test in a worktree; nothing is landed, pushed, deployed or called. A later resident release carries the file; this cell widens nothing.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO ruling (msg 7768) against the cell; the lens: placeholder prose that still reads as real legal text, a change that also moves the DRAFT mark or the layout, a combined-layout page that gains a disclaimer it did not have. The cell requires an exact label, a one-hunk diff, and a before-arm that fails. NOT seen (blind): the rendered PDF bytes; denominator: 4 test cases (a) to (d) and 1 constant.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling msg 7768 (call 095e held for Andrew; the release is not gated). Workstream `ZP` of round 40. Base: `AR330-y-AC1`, `AC2` and `AC3` FAIL as expected (no checker files).
- The approved wording replaces the label in a later release, as a release gate for any client delivery.
