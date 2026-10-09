# TO-IB-yr-691 -- Performance client statement submissions compose with the custody revision (E11)

<to_id>IRPT_BCKEND.TO-IB-yr-691</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~220</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>69</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~Y | **Decomp cell:** `IB-yr-691` (`decompositions/IRPT_BCKEND_DECOMP_R69_Y.md`)
| **Ordered by:** `1.0.0_SA_CTO~DELL2` ADDENDUM 10, item E11.

---

## WORKER FACE

### THE CELL

The "Performance client statement" is the quarterly client export of Performance. Its code id is the custody report:
`CUSTODY_REPORT`, retention family revision `irpt-custody-x10-v1`. Keep the code ids exactly as they are.

`infra/aws/lambda/investor-reporting/ycharts/generate/custody_submission.py`, around line 77, builds its retained repositories with
`build_retained_repositories(self.table, self.s3, access.authorize_current, lambda _: None, reporting_policy=self.reporting_policy,
reporting_destination=self.reporting_destination, clock=self.clock)`. That call requests no custody revision, so a statement
submission's repositories cannot retain a `CUSTODY_REPORT` under `irpt-custody-x10-v1`.

The export side already does this right (E9, commit 97e679c64f): see `infra/aws/lambda/investor-reporting/export/submit_installed.py`,
function `retained_reports`. It probes the registry with `reporting_policy(CUSTODY_POLICY_REVISION)`. On success it passes
`additional_policy_revisions=(CUSTODY_POLICY_REVISION,)`; on `ValueError` it passes `()`. `CUSTODY_POLICY_REVISION` is imported from
`composition` (`infra/aws/lambda/investor-reporting/reports/composition.py`).

**Your cell:**
1. **The edit.** Make `custody_submission.py`'s call use the SAME probe and pass `additional_policy_revisions` the same way.
   - Keep every other argument identical, and change no other line's behaviour.
   - Reuse rather than copy if a shared helper is importable from `custody_submission.py`'s package without new staging. Otherwise
     write the five-line probe inline, matching `retained_reports`.
   - Keep the module's import-time rule: no SDK clients and no cloud effects at import.
2. **The test.** Add `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_custody_submission_revision.py`, offline, with
   no AWS and no network. Use fakes or monkeypatching in the style of the neighbouring custody tests. Prove three things:
   - (a) with a reporting policy whose registry resolves `irpt-custody-x10-v1`, the repositories `custody_submission` builds request
     that revision, so a `CUSTODY_REPORT` family resolves under `irpt-custody-x10-v1`;
   - (b) PERFORMANCE and ANALYSIS still resolve under `irpt-x10-v1`;
   - (c) with a reporting policy that raises `ValueError` for the custody revision, the build passes no additional revision, and
     composes exactly as before.

### ACCEPTANCE (run from your worktree root)

<criterion id="Y69-1-AC1" cell_refs="IB-yr-691"><invocation>python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_custody_submission_revision.py</invocation><expect>passed</expect></criterion>

<criterion id="Y69-1-AC2" cell_refs="IB-yr-691"><invocation>python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_custody_composition.py infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_custody_entry.py infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_custody_retained.py</invocation><expect>passed</expect></criterion>

<expected_criteria>Y69-1-AC1,Y69-1-AC2</expected_criteria>

**Issuer's base run at dell2 box/dell2 (~22:3xZ):** AC1 `no tests ran` (the file does not exist); AC2 `66 passed, 2 skipped`.

- AC1 must report at least 3 passed and 0 failed.
- AC2: run it at base BEFORE your edit, record the counts, and after the edit it must show the same passed count and 0 failed.
- If base AC2 already fails, record that as a ROW. Do not fix unrelated tests.

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-08 ~22:5xZ, on row IRPT_BCKEND-D2-W220-S1).** AC2's two failures come from the
fixture in `test_custody_retained.py`, not from the edit. Its `w.policy.reporting_policy` answers EVERY revision with the default
document and never raises `ValueError`, which the real registry does for an unknown revision. So the probe correctly adds
`irpt-custody-x10-v1`, and `composition.py` correctly refuses the overlap. Ruling:
- Fix the FIXTURE, not the probe. Make that test's `reporting_policy` raise `ValueError` for any revision it does not register, as
  `export/tests/test_custody_writer_composed.py` does. Do NOT catch `ReportRefused` in `custody_submission.py`.
- `<paths>` now admits `ycharts/generate/tests/test_custody_retained.py`. Change only that fixture's revision lookup.
- AC2's bar is unchanged: 66 passed, 2 skipped, 0 failed.
- Gate limb that graded this amendment: `to-pipeline-gate.py` GATE (viii) on a modify (the order declares `<placeholders>`).

## BOUNDS

- **Grant.** The `<paths>` block and this order's file. No deploy, no upload, no AWS writes, no downloads or installs, no `bun`.
- Every `.py` edit passes `.tools/commit-gate.sh` (py_compile + ds-precommit + ruff py39).
- **Refusal clause.** If a criterion cannot be met as written: stop, write the reason in your report and a surprise row, and do not
  weaken the check.
- **Row ids** are `IRPT_BCKEND-D2-W220-S<k>`. Re-read the channel before appending your own block. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~220" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~220@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~220 <0.9.0_WK_IRPT_BCKEND~220@opal.agent>" -F <msgfile> -- <paths>`.
  Write the message file with the Write tool; no pre-`git add`; edit byte-preserving; ASCII only; use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/custody_submission.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_custody_submission_revision.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_custody_retained.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~220/IRPT_BCKEND.TO-IB-yr-691.statement-submission-custody-revision.proof_of_spec.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-yr-691.statement-submission-custody-revision.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R69_Y.md</decomp_doc> round 69, workstream ~Y, cell `IB-yr-691`.
<owned_cells>IB-yr-691</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y69-1-AC1, Y69-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~220/IRPT_BCKEND.TO-IB-yr-691.statement-submission-custody-revision.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> Y69-1-AC1,Y69-1-AC2` BEFORE you flip the order to complete. Copy the
shape from `deliverables/0.9.0_WK_IRPT_BCKEND~155/IRPT_BCKEND.TO-IB-yr-641.repin-x1-staged-rows.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):**
- each criterion's output lines, including AC2's base and after counts;
- the diff summary;
- the commit hashes;
- any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one composition call in custody_submission.py (line ~77) plus one new offline test; no deployed byte moves; the change rides ~Y2's next release pair (ADDENDUM 10).
comp-iam: DECLARED-NOT-APPLICABLE -- no boto3 call, role or grant changes; the test is offline.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched.
comp-adversary: RUN -- AC1 at base FAILs (the test file does not exist); its arm (c) is the negative control, an unregistered revision composes as before; AC2 is the regression control with a base count recorded first.
lane: the <paths> block IS the grant (worker_grant).
</preflight>
