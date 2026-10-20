# TO IRPT_ANLREQ.TO-AR-y-473.audit-test-file-leaves-no-module-or-path-state-behind -- FIX AND PROVE OFFLINE: the audit test file (AR-y-467) binds `entry` and edits `sys.path` at collection, so collecting it before `test_generate_installed.py` breaks that file; make the audit test file leave no module or path state behind

<to_id>IRPT_ANLREQ.TO-AR-y-473.audit-test-file-leaves-no-module-or-path-state-behind</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~347</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ132</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor (a path under infra/) | **Decomp cell:** `AR-y-473` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-AUDIT-RECORD hygiene (row IRPT_ANLREQ-D2-S216A, filed by 2.0.0_SA_COO~G2, measured on trunk 09dd4ea9951) | **depends_on:** AR-y-467 and AR-y-469 drained (the file's final form)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~347`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-347` (branch `wk-IRPT_ANLREQ-347`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~347 <0.9.0_WK_IRPT_ANLREQ~347@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W347-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (the combined run on today's trunk file reads an error: record it as the mutant) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "AR473-y-AC1,AR473-y-AC2,AR473-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID.

### THE CELL (`AR-y-473`, inlined)

*The measured defect (row IRPT_ANLREQ-D2-S216A).* From `infra/aws/lambda/investor-reporting`, `python -m pytest reports/tests/test_analysis_audit.py reports/tests/test_generate_installed.py` gives 1 error in collection: collecting the audit test file first binds the module name `entry` (or edits `sys.path` at import) to `ops/entry.py`, and `test_generate_installed.py` (its assertion near line 32) then fails because it expects `entry` to be the generate entry. `test_generate_installed.py` alone passes (14). The whole `reports/tests` directory errors at collection for `test_generate_installed.py` and `test_generate_installed_custody.py` until the audit file is ignored.

*The change.* In `infra/aws/lambda/investor-reporting/reports/tests/test_analysis_audit.py` ONLY (and its helper imports): make the file leave no module or path state behind. Find, by reading the top of the file and the fixtures, what it adds to `sys.path` or `sys.modules` at import (the `entry` binding and any path inserts) and move that into a pytest fixture or context manager that saves and restores `sys.path` and removes the modules it imported, so that importing/collecting the file changes neither. Do not change `reports/analysis_audit.py`, the packager, or any other test file. Every test of the file stays and passes (25 after AR-y-469).

*Prove.* Run the three orderings in the acceptance block. Record in `MUTANT_REPORT.txt` the combined run on the trunk file BEFORE your change (it must read the collection error) and AFTER.

---

## ACCEPTANCE

<criterion id="AR473-y-AC1" cell_refs="AR-y-473"><invocation>(cd infra/aws/lambda/investor-reporting && python -m pytest reports/tests/test_analysis_audit.py reports/tests/test_generate_installed.py reports/tests/test_generate_installed_custody.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)</invocation><expect>^[0-9]+ passed in </expect></criterion>
<criterion id="AR473-y-AC2" cell_refs="AR-y-473"><invocation>(cd infra/aws/lambda/investor-reporting && python -m pytest reports/tests/test_generate_installed.py reports/tests/test_generate_installed_custody.py reports/tests/test_analysis_audit.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)</invocation><expect>^[0-9]+ passed in </expect></criterion>
<criterion id="AR473-y-AC3" cell_refs="AR-y-473"><invocation>(cd infra/aws/lambda/investor-reporting && python -m pytest reports/tests/test_analysis_audit.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)</invocation><expect>^[0-9]+ passed in </expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~347/IRPT_ANLREQ.TO-AR-y-473.audit-test-file-leaves-no-module-or-path-state-behind.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-473.audit-test-file-leaves-no-module-or-path-state-behind`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR473-y-AC1,AR473-y-AC2,AR473-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-473</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/reports/tests/test_analysis_audit.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~347/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-473.audit-test-file-leaves-no-module-or-path-state-behind.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one test file changed so that it leaves no import-time state behind; no source, no AWS, no deploy.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading row S216A (measured by G2 on trunk 09dd4ea9951) against this cell; the lens: tests deleted or skipped to make the combined run pass (all 25 stay), the module under test changed instead of the test, a fixture that restores sys.path but leaves `entry` in sys.modules (or the reverse), an ordering that passes only in the listed order (all three orderings are run). NOT seen (blind): the whole reports/tests directory run (the S216B failure in another directory is G2's and is out of scope); denominator: three criteria.
</preflight>
