# TO-AR-g-87 -- the resident installer registers the commentary policy revision irpt-anlreq-x10-v1, so the packager can read the AI commentary draft back

<to_id>IRPT_ANLREQ.TO-AR-g-87</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~187</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>15</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-87` (`decompositions/IRPT_ANLREQ_DECOMP_R15_G.md`) |
**outcome_ref:** FWD-1 hop 8 (the package attach) | **depends_on:** `AR-g-85` (merged `002a88bdc3`, which edited the same file).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~187`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-187` (branch `wk-IRPT_ANLREQ-187`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/` and `org/missions/D9/IRPT` on disk. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~187 <0.9.0_WK_IRPT_ANLREQ~187@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W187-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`).

### Read first (under `C:/dev/wk-irpt-anlreq-187/infra/aws/lambda/investor-reporting/`)

- `reports/resident_installed.py` (`OPAL_RESEARCH_REVISION` near line 61 and the `build_retained_repositories(...)` call near line 402) and `reports/composition.py` (`build_retained_repositories`, line 31: how `additional_policy_revisions` registers a family under a revision).
- `reports/commentary_draft_store.py` line 65 (`COMMENTARY_POLICY_REVISION = "irpt-anlreq-x10-v1"`: the revision the AI commentary draft is retained under) and `reports/tests/test_resident_installed.py` (`test_installer_wires_ycdgen_research_revision`, near line 289, and the `package` fixture and `fake_clients` it uses).

### THE CELL (`AR-g-87`, inlined)

The packager (the resident's hop 8) reads the AI commentary draft back through the resident's artifact repository. The resident registers only the served revision and `irpt-ycdgen-research-v1`; the draft's family `ANALYSIS_COMMENTARY` lives only in `irpt-anlreq-x10-v1`, so the read refuses "unregistered artifact family" (repository.py, record `0.9.0_WK_IRPT_ANLREQ~155/r41/PACKAGE_REFUSAL_READ.json`). This cell registers that revision in the resident.

**`reports/resident_installed.py`, exactly this:**
1. Add the constant `ANALYSIS_COMMENTARY_REVISION = "irpt-anlreq-x10-v1"` right after `OPAL_RESEARCH_REVISION`, with a two-line comment saying the AI commentary draft is retained as `ANALYSIS_COMMENTARY` under this reporting policy revision (as `commentary_draft_store.COMMENTARY_POLICY_REVISION`), and that the resident reads it back to package it.
2. The `build_retained_repositories(...)` call passes `additional_policy_revisions=(OPAL_RESEARCH_REVISION, ANALYSIS_COMMENTARY_REVISION)` (this order).
3. Nothing else in the file changes.

**`reports/tests/test_resident_installed.py`, exactly this:**
1. In `test_installer_wires_ycdgen_research_revision` the assertion on what the installer asked becomes `asked == [(RESEARCH, "irpt-anlreq-x10-v1")]` (keep the rest of that assertion and the rest of the test).
2. Add the test `test_installer_registers_the_commentary_family_under_its_revision(package)`: it builds the runtime as the neighbouring tests do, and asserts `ri.ANALYSIS_COMMENTARY_REVISION == "irpt-anlreq-x10-v1"`, `artifacts.revisions["ANALYSIS_COMMENTARY"] == "irpt-anlreq-x10-v1"` and `artifacts.revisions["YCHARTS_OPAL_REPORT"] == RESEARCH`, where `artifacts` is `runtime["assembly"].requests.artifacts`.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR87-g-AC1" cell_refs="AR-g-87"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g87_checks.py g87</invocation><expect>^AR-G87-OK</expect></criterion>

<criterion id="AR87-g-AC2" cell_refs="AR-g-87"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g85_checks.py regress</invocation><expect>^AR-G85-REGRESS-OK</expect></criterion>

<expected_criteria>AR87-g-AC1,AR87-g-AC2</expected_criteria>

- AC1 builds the real runtime four ways with the issuer's own tests (what the installer asks for, in order; the constants; where each family is registered; that no other family moves to the new revision), then checks your two named tests exist and pass. At base it FAILs.
- AC2 runs seven existing test files one at a time (65 tests or more; yours adds one) and needs all of them to pass. At base it PASSes. Run it under `timeout 300`.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_installed.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~187/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-87.commentary-revision-in-the-resident-installer.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R15_G.md</decomp_doc> round 15, workstream ~G, cell `AR-g-87`.
<owned_cells>AR-g-87</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR87-g-AC1, AR87-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~187/IRPT_ANLREQ.TO-AR-g-87.commentary-revision-in-the-resident-installer.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-87`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR87-g-AC1,AR87-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the lines you changed with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `additional_policy_revisions` is read by `composition.build_retained_repositories`, which registers each named revision's families in the repository the resident builds; the only caller in this file is the one edited. The packager's read of `ANALYSIS_COMMENTARY` (record ~155/r41 q1 step 13) is the consumer that today refuses. Nothing is deployed, so no edge changes until the release cell ships the file.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change (the service-reader grant for the draft is a separate, existing grant; this registers a family name in a repository object).
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against the package-refusal read (~155/r41). Traps: the revision named but a different spelling (the family stays unregistered); the new revision registered ahead of the research one (the order is part of the contract); the commentary family moved to the wrong revision or another family dragged onto the new revision; the test edited to match a wrong installer instead of the contract. The checker feeds a green arm (a reference build passes the four issuer tests and the two named tests) and three mutant arms (the revision omitted: 3 of 4 issuer tests and both named tests fail; the order swapped: 1 issuer test and 1 named test fail; the revision spelled -v2: all fail).
</preflight>

- Cut on the package-refusal read (`~155/r41`, `PACKAGE_REFUSAL_READ.json`), `~Y2` msg 8566 and CTO msg 8568 (addendum 2 @87fe24c71d). Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR87-g-AC1` FAILs and `AR87-g-AC2` PASSes (65), as expected.
- This is change (1) of the CTO's two additions to the ONE resident release. Change (2), run 3's producer address, is the release cell's.
