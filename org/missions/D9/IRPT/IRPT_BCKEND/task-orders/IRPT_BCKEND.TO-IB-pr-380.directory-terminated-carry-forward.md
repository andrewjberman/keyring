# TO IRPT_BCKEND.TO-IB-pr-380 -- directory refresh carries a source-removed entry forward as TERMINATED; package the refresh release

<to_id>IRPT_BCKEND.TO-IB-pr-380</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~188</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>92</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ruling msg 1959 on row D2-W187-S1 (an ENDPOINT change, ruled by the CTO) |
**Decomp cell:** `IB-pr-380` (decomposition section 85) | **outcome_ref:** FWD-7 (directory READY at all 3 firms) | **depends_on:** IB-pr-379
(diagnosis, drained @5e504225d9). **Deadline:** live before cottonwood goes OVER_AGE on 2026-10-12, so in practice by the close on Friday
2026-10-09.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-188` (branch `wk-IRPT_BCKEND-188`, cut from `box/dell2`). Work, build and commit only there.
`L` = `infra/aws/lambda/investor-reporting`. Paths below are relative to the worktree. Keep scratch outside the worktree.

**The fault (row IRPT_BCKEND-D2-W187-S1).** The diagnosis is
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~187/IB91-1_dropped_entry_diagnosis.json`:
- inflection: household `cli_eee3d5ecc6dda8132ba25158` was merged away by the vendor;
- cottonwood: account-only entry `cli_6be3d8625139a8d2613ab8af` (market value 0) is no longer emitted.
- Both have been absent from the source since 2026-10-06.

In `L/directory/refresh.py`, `refresh_firm` (~line 966) turns any non-empty disappeared set from `compute_delta` (line 387) into
REFRESH_FAILED, so every inflection and cottonwood refresh fails on these entries indefinitely.

**The rule, as ruled by the CTO (msg 1959). Build exactly this:**
- An entry absent from BOTH the new build and the source snapshot is carried forward into the new build, marked `TERMINATED` with
  `source_removed_on` (the first source snapshot that lacks it), and the build goes READY.
- An entry still IN the source but missing from the build stays REFRESH_FAILED, unchanged.
- Each refresh prints and records its TERMINATED count (`terminated_count`) in its result and manifest.
- Termination is a change of marking, never a deletion (refresh.py docstring). Readers must still be able to see the entry, marked.

**Your cell. Nothing is uploaded or applied: AWS READS and BUILD_ONLY only.**
1. **Implement** the rule in `L/directory/`. Decide "absent from the source" from the source snapshot the build read, not from the build
   output. Keep the existing reason codes. A READY build with terminations carries `terminated_count >= 1`.
2. **Test** in `L/directory/tests/test_refresh_terminated.py`, with test names containing `terminated_carry_forward`, using in-memory
   fakes. Write at least 3 tests:
   - an entry absent from both the build and the source gives READY, with the entry carried and marked TERMINATED, and
     `terminated_count` 1;
   - an entry present in the source but missing from the build gives REFRESH_FAILED (the negative arm);
   - an already-TERMINATED entry on the next refresh is carried again, keeps its `source_removed_on`, and is not counted as a new
     disappearance.
   The whole directory suite must still pass.
3. **Real-case replay** (offline, no invoke), written to `.../0.9.0_WK_IRPT_BCKEND~188/IB92-1_terminated_replay.json` as
   `{firms: {inflection: {built: {reason_code, terminated_count}, live: {reason_code}, negative: {reason_code}}, cottonwood: {...}}}`:
   - Drive the real inflection and cottonwood inputs (the previous READY build plus the latest source snapshot, read from AWS) through
     the LIVE zip and the BUILT zip.
   - The negative arm is the same input with the dropped id put back into the source only, through the built zip.
   - Opaque ids only. Raw extracts stay in scratch outside the worktree and are deleted after.
4. **Package.** Commit the fix; that commit is pin P. Run `python infra/aws/lambda/ci/release-census.py irpt-directory-refresh --pin P`
   (and `irpt-directory-search` if a shared member changed). Every changed member must be owned by your commit.
5. **BUILD_ONLY from a clean tree.** Check that porcelain is empty first, set `BUILD_ONLY=1` only, and clean the residue after.
6. **Census file** `.../0.9.0_WK_IRPT_BCKEND~188/IB92-1_refresh_census.json`:
   `{pin, changed_members:[{member, owner_commit, why}], build_only:{rc, tree_clean, built_sha256}}`.
7. **Packet** `.../0.9.0_WK_IRPT_BCKEND~188/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-380.md`, modelled on
   `deliverables/0.9.0_WK_IRPT_BCKEND~178/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-370.md`. It must contain:
   - P, the built sha256 and the rule;
   - the writers of the served directory;
   - Branch A, and Branch B: rollback to live `RbpsijC23XVUFPE0W34Gr/xqtDil94xYRqDuuZlaYx8=` with its S3 version (read live);
   - the replay arm for the applier: rerun step 3 against the live and built zips before the ledger;
   - the after-read: a driven refresh READY at all 3 firms, read at each manifest's own as_of, with `terminated_count` 1 at inflection
     and cottonwood and 0 at 49financial.

<criterion id="IB92-1-AC1" cell_refs="IB-pr-380"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r92/p92_cells.py" . IB92-1-AC1</invocation><expect>IB92-1-AC1 PASS</expect></criterion>
`IB92-1-AC1` -- at least 3 `terminated_carry_forward` tests pass, and the whole directory suite passes. Base: FAIL.

<criterion id="IB92-1-AC2" cell_refs="IB-pr-380"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r92/p92_cells.py" . IB92-1-AC2</invocation><expect>IB92-1-AC2 PASS</expect></criterion>
`IB92-1-AC2` -- on both firms' real inputs: built READY with `terminated_count` 1; live REFRESH_FAILED; negative arm REFRESH_FAILED.
Base: FAIL.

<criterion id="IB92-1-AC3" cell_refs="IB-pr-380"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r92/p92_cells.py" . IB92-1-AC3</invocation><expect>IB92-1-AC3 PASS</expect></criterion>
`IB92-1-AC3` -- the packet names P, the built sha, the rollback sha and both branches; the census records a clean-tree BUILD_ONLY with rc 0.
Base: FAIL.

<expected_criteria>IB92-1-AC1, IB92-1-AC2, IB92-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No upload, apply or deploy. AWS reads only.
- **Client data:** opaque ids only in any committed file.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test, and never
  widen the rule beyond the ruling.
- **Row ids** are `IRPT_BCKEND-D2-W188-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~188" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~188@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~188 <0.9.0_WK_IRPT_BCKEND~188@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/lambda/investor-reporting/directory/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-380.directory-terminated-carry-forward.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~188/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 85 (round 92, workstream ~P), cell `IB-pr-380`.
<owned_cells>IB-pr-380</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB92-1-AC1, IB92-1-AC2, IB92-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~188/IRPT_BCKEND.TO-IB-pr-380.directory-terminated-carry-forward.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give P, the built sha256, the commit hashes, each criterion's last line, the replay outcomes per firm,
and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- irpt-directory-refresh live RbpsijC2 (IB-pr-377); refresh_firm ~966 fails any disappeared set; diagnosis IB91-1 (both SOURCE_REMOVAL, 1 entry each); readers of the served directory: irpt-directory-search (IV7P2AL4) reads entries by status, so a TERMINATED marking must stay readable.
comp-iam: DECLARED-NOT-APPLICABLE -- reads under the seat's existing roles; no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the refresh schedule is not touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p92_cells.py dry-run at base 0eb7a4abbe on dell2 2026-10-09 ~00:1xZ: AC1, AC2, AC3 FAIL (`-k terminated_carry_forward` selects 0 of 190; no replay; no packet or census); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; directory/ is ~P's.
</preflight>
