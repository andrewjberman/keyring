# TO IRPT_BCKEND.TO-IB-pr-369 -- ReportRepository retains each family under its own policy revision: CUSTODY_REPORT under irpt-custody-x10-v1, PERFORMANCE and ANALYSIS unchanged under irpt-x10-v1

<to_id>IRPT_BCKEND.TO-IB-pr-369</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~177</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>82</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO round analysis ADDENDUM 6 (msg 1415), E9 | **Decomp cell:** `IB-pr-369`
(decomposition section 75) | **outcome_ref:** FWD-8 / CUSTDY hop 5 | **depends_on:** none for the code. Its RELEASE is a later pair, after
IB-pr-368 is live (ADDENDUM 6 order).

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-177` (branch `wk-IRPT_BCKEND-177`). Work and commit only there. `L` =
`infra/aws/lambda/investor-reporting`. Paths below are relative to the worktree.

**Why.**
- A retained row binds the `policy_sha256` of the policy it was written under, and `L/reports/retention.py` (~lines 129-134) refuses
  a row whose sha differs. Editing `irpt-x10-v1` in place would therefore refuse every live retained report.
- So CUSTODY_REPORT gets a NEW policy row, `irpt-custody-x10-v1` (E8, `2.0.0_SA_COO~M2`). It is PENDING_ENFORCEMENT now and ACTIVE
  after install. Its terms mirror PERFORMANCE. The shape is in `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/E8_CUSTODY_REPORT_FAMILY_SHAPE_20261008.md`.
- Today `L/reports/repository.py` (~line 158) reserves every family under ONE default revision.

**Your cell.**
- `ReportRepository` takes a family-to-policy-revision map. `ArtifactRepository` already has one: reuse its shape and do not invent
  a new one.
- CUSTODY_REPORT is reserved, re-checked and read under `irpt-custody-x10-v1`. PERFORMANCE and ANALYSIS stay exactly as today, under
  `irpt-x10-v1`.
- The custody callers pass the custody revision through `build_retained_repositories(..., additional_policy_revisions=...)` in
  `L/reports/composition.py`. In this order's grant those callers are `L/export/submit_installed.py` (the custody read) and
  `L/reports/custody_write.py` (the custody write).
- A family with no registered revision still refuses ("unregistered retention family").
- If another caller outside the grant must change, file a row and do not edit it.
- Your tests build their own policy registry fixture with both rows, shaped like the E8 document. Do not edit
  `infra/logic/registry/` (`~M2`'s lane).

**Tests:** `L/reports/tests/test_repository_family_revisions.py`, with test names containing these substrings:
- `custody_under_custody_policy`: a CUSTODY_REPORT is reserved and read back under `irpt-custody-x10-v1`. In the same test,
  PERFORMANCE and ANALYSIS are reserved under `irpt-x10-v1`.
- `x10_retained_reads_back_unchanged`: a report retained under `irpt-x10-v1` before your change reads back unchanged after it
  (same id, revision and bytes; the regression arm).
- `unregistered_kind_refuses`: a kind with no registered revision is refused.

**AMENDMENT 1 (2026-10-08 ~19:5xZ, issuer `2.0.0_SA_COO~P2`, disarming row D2-W177-S1).**
- **The hazard.** `export/submit_installed.py` now requests `irpt-custody-x10-v1` through `additional_policy_revisions`. Any build of
  this source before E8's registry row (`~M2`) exists would make EVERY submit raise `ValueError`, PERFORMANCE and ANALYSIS included.
- **The fix.** The custody revision is requested ONLY when the reporting-policy registry the function reads actually carries the
  `irpt-custody-x10-v1` row. Read the policy the same way `composition.py` already does; add no new read. Absent the row:
  - PERFORMANCE and ANALYSIS compose and behave exactly as today;
  - a CUSTODY_REPORT still refuses ("unregistered retention family"), which is fail closed.
- **The test.** Add a test whose name contains `x10_composes_without_custody_row`: with a registry fixture that has only `irpt-x10-v1`,
  the submit composition builds and a PERFORMANCE/ANALYSIS reference reads back, while a CUSTODY_REPORT refuses. IB82-1-AC2 now also
  runs `-k x10_composes_without_custody_row` (check amended in the same commit).
- **The row.** When done, append `IRPT_BCKEND-D2-W177-S3`, a DISMISSED_WITH_REASON whose `dismissal_reason` starts
  `Resolves IRPT_BCKEND-D2-W177-S1:` and cites your fix commit.
- Gate limb: none graded this amendment (a modification; GATE viii only).

<criterion id="IB82-1-AC1" cell_refs="IB-pr-369"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r82/p82_cells.py" . IB82-1-AC1</invocation><expect>IB82-1-AC1 PASS</expect></criterion>
`IB82-1-AC1` -- CUSTODY_REPORT is retained and read under its own revision, while PERFORMANCE and ANALYSIS stay under irpt-x10-v1.
Base: FAIL.

<criterion id="IB82-1-AC2" cell_refs="IB-pr-369"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r82/p82_cells.py" . IB82-1-AC2</invocation><expect>IB82-1-AC2 PASS</expect></criterion>
`IB82-1-AC2` -- the regression arm: an irpt-x10-v1 retained report reads back unchanged, and the three existing repository and
retention suites pass, each in its own process. Base: FAIL (no file).

<criterion id="IB82-1-AC3" cell_refs="IB-pr-369"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r82/p82_cells.py" . IB82-1-AC3</invocation><expect>IB82-1-AC3 PASS</expect></criterion>
`IB82-1-AC3` -- an unregistered kind still refuses. Base: FAIL.

<expected_criteria>IB82-1-AC1, IB82-1-AC2, IB82-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block and nothing else. No AWS call, no build, no deploy, and no source-map edit (the release is a later
  pair).
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause.** If a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W177-S<k>`. Re-read the channel right before you append. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~177" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~177@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~177 <0.9.0_WK_IRPT_BCKEND~177@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/lambda/investor-reporting/reports/repository.py
infra/aws/lambda/investor-reporting/reports/composition.py
infra/aws/lambda/investor-reporting/reports/custody_write.py
infra/aws/lambda/investor-reporting/export/submit_installed.py
infra/aws/lambda/investor-reporting/reports/tests/test_repository_family_revisions.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-369.repository-per-family-policy-revision.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~177/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 75 (round 82, workstream ~P), cell `IB-pr-369`.
<owned_cells>IB-pr-369</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB82-1-AC1, IB82-1-AC2, IB82-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~177/IRPT_BCKEND.TO-IB-pr-369.repository-per-family-policy-revision.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the commit hashes, each criterion's last line, which callers changed and why, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- build_retained_repositories callers (5: export/submit_installed.py, performance/retained.py, reports/generate_installed.py, reports/resident_installed.py, reports/status_installed.py); only the custody callers are granted; PERFORMANCE/ANALYSIS keep irpt-x10-v1 (AC2 regression arm). No function is released by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p82_cells.py dry-run at base 038b35d676 on dell2 2026-10-08 ~19:1xZ: AC1, AC2, AC3 FAIL (no test file); existing suites pass at base (24, 9, 21).
lane: the <paths> block IS the grant; infra/logic/registry/ is ~M2's (E8) and NOT granted.
</preflight>
