# TO IRPT_BCKEND.TO-IB-pr-379 -- why the inflection and cottonwood directory builds drop clients the previous build carried: diagnose, fix, and package the release

<to_id>IRPT_BCKEND.TO-IB-pr-379</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~187</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>91</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ruling msg 1949 item (2): this round's FIRST cell, landed before the inflection
and cottonwood directories go OVER_AGE | **Decomp cell:** `IB-pr-379` (decomposition section 84) | **outcome_ref:** FWD-7 (directory
READY at all 3 firms) | **depends_on:** IB-pr-377 (r61 release live, graded PASS at dc3ff4c2c9).

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-187` (branch `wk-IRPT_BCKEND-187`, at `dc3ff4c2c9` on `box/dell2`). Work, build and commit only
there. `L` = `infra/aws/lambda/investor-reporting`. Paths below are relative to the worktree. Keep scratch outside the worktree.

**The fault (row IRPT_BCKEND-D2-S13).** The r61 refresh was driven live on 2026-10-08. 49financial went READY. inflection and cottonwood
returned `REFRESH_FAILED` with action CORRECT and SAFE: clients present in the previous build are absent from the new one, and
`L/directory/refresh.py` (~lines 43 and 966-977) treats a disappearance as a failure, not a delta. The prior directory stays served. It goes
OVER_AGE when its age exceeds `MAX_AGE_TRADING_DAYS = 2` (`L/directory/expiry.py:47`, `age_in_trading_days`). Facts of the run:
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~DELL2/IB89-1_r61_release_after_reads.json`
(`arm_a_driven_refresh.per_firm_branch`).

**Your cell. Nothing is uploaded or applied: AWS READS and BUILD_ONLY only.**
1. **Measure.** Read the REFRESH_FAILED records and the previous and new builds for inflection and cottonwood (refresh manifests under
   `investor-reporting/directory/_refresh/<as_of>/manifest.json`; the short-name buckets opal-data-bd/-inf/-cot are readable from dell2,
   row D2-S12). List the disappeared entries by their opaque directory ids. For each firm, decide the cause from the bytes:
   - `BUILD_BUG`: the client is in the source but our build drops it (filter, join, eligibility, parse);
   - `KEY_CHANGE`: the client is in both builds under a different id (re-keyed), so the comparison is wrong;
   - `SOURCE_REMOVAL`: the client is genuinely gone from the source.
2. **Write the diagnosis** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~187/IB91-1_dropped_entry_diagnosis.json`:
   `{firms: {inflection: {disappeared_count, disappeared_ids, cause, evidence}, cottonwood: {...}}, overage_deadline}`.
   - Opaque ids only: NO client names, emails or account numbers.
   - `overage_deadline` is the first date on which the SERVED directory of either firm is over age, computed with `expiry.age_in_trading_days`
     (lib/trading_calendar), with the served as_of you read.
   - **If either firm is SOURCE_REMOVAL, STOP after the diagnosis:** file a row saying the build is right and the rule needs a ruling,
     and report. Do not change the rule.
3. **Fix** (BUILD_BUG or KEY_CHANGE) in `L/directory/` at its root cause. Do not weaken the disappearance rule: a real disappearance still
   fails.
4. **Test** `L/directory/tests/test_refresh_dropped_entry.py`, test names containing `dropped_entry`, in-memory fakes:
   - a fixture reproducing the measured shape (with synthetic ids) fails before the fix and builds READY after it;
   - a genuine disappearance still returns REFRESH_FAILED.
   - `tests/test_refresh_previous_state.py` and the whole directory suite still pass.
5. **Package.** Commit the fix; that commit is pin P. Run `python infra/aws/lambda/ci/release-census.py irpt-directory-refresh --pin P`
   (and irpt-directory-search if a shared member changed). Every changed member must be owned by your commit.
6. **BUILD_ONLY from a clean tree** (porcelain empty first; `BUILD_ONLY=1` only; clean the residue after).
7. **Census file** `.../0.9.0_WK_IRPT_BCKEND~187/IB91-1_refresh_census.json`: `{pin, changed_members:[{member, owner_commit, why}],
   build_only:{rc, tree_clean, built_sha256}}`.
8. **Packet** `.../0.9.0_WK_IRPT_BCKEND~187/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-379.md`, modelled on
   `deliverables/0.9.0_WK_IRPT_BCKEND~178/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-370.md`. It must contain:
   - P, the built sha256, the cause and the fix;
   - Branch A, and Branch B: rollback to live `RbpsijC23XVUFPE0W34Gr/xqtDil94xYRqDuuZlaYx8=` with its S3 version (read live);
   - the writers of the served directory;
   - an offline replay arm for the applier (the measured inflection and cottonwood inputs through the live and built zips: live gives
     REFRESH_FAILED, built gives READY), plus a negative control;
   - the after-read: a driven refresh READY at all 3 firms, read at each manifest's own as_of.

<criterion id="IB91-1-AC1" cell_refs="IB-pr-379"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r91/p91_cells.py" . IB91-1-AC1</invocation><expect>IB91-1-AC1 PASS</expect></criterion>
`IB91-1-AC1` -- the diagnosis names both firms' dropped entries (opaque ids), the cause and the evidence, plus the over-age date. Base: FAIL.

<criterion id="IB91-1-AC2" cell_refs="IB-pr-379"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r91/p91_cells.py" . IB91-1-AC2</invocation><expect>IB91-1-AC2 PASS</expect></criterion>
`IB91-1-AC2` -- the `dropped_entry` tests pass and the previous-state tests still pass. Base: FAIL.

<criterion id="IB91-1-AC3" cell_refs="IB-pr-379"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r91/p91_cells.py" . IB91-1-AC3</invocation><expect>IB91-1-AC3 PASS</expect></criterion>
`IB91-1-AC3` -- the packet names P, the built sha, the rollback sha and both branches; the census records a clean-tree BUILD_ONLY with rc 0.
Base: FAIL.

<expected_criteria>IB91-1-AC1, IB91-1-AC2, IB91-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block and nothing else. No upload, apply or deploy. AWS reads only.
- **Client data.** Opaque ids only in any committed file; keep raw extracts in scratch outside the worktree and delete them after.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause.** If a criterion cannot be met as written, stop, file a row, and report. Never weaken a check, a test or the rule.
- **Row ids** are `IRPT_BCKEND-D2-W187-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~187" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~187@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~187 <0.9.0_WK_IRPT_BCKEND~187@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/lambda/investor-reporting/directory/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-379.directory-dropped-entry-diagnose-and-fix.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~187/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 84 (round 91, workstream ~P), cell `IB-pr-379`.
<owned_cells>IB-pr-379</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB91-1-AC1, IB91-1-AC2, IB91-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~187/IRPT_BCKEND.TO-IB-pr-379.directory-dropped-entry-diagnose-and-fix.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the cause per firm, the over-age date, P, the built sha256, the commit hashes, each criterion's last
line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- irpt-directory-refresh live RbpsijC2 (IB-pr-377, dc3ff4c2c9); driven refresh 2026-10-08 READY at 49financial, REFRESH_FAILED+SAFE at inflection and cottonwood (after-reads JSON, arm_a); disappearance rule refresh.py ~43, ~966-977; over-age ceiling expiry.py:47 (2 trading days).
comp-iam: DECLARED-NOT-APPLICABLE -- reads under the seat's existing roles; no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the refresh schedule is not touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p91_cells.py dry-run at base dc3ff4c2c9 on dell2 2026-10-08 ~23:5xZ: AC1, AC2, AC3 FAIL (no diagnosis; `-k dropped_entry` selects 0 of 190; no packet or census); 0 control bytes in the check; ruff clean.
lane: the <paths> block IS the grant; directory/ is ~P's.
</preflight>
