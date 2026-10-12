# TO IRPT_BCKEND.TO-IB-pr-474 -- BUILD ONLY: build-and-upload.sh exits non-zero, and names the files, when a restore from HEAD fails

<to_id>IRPT_BCKEND.TO-IB-pr-474</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~329</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>165</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6476 (PRD ADDENDUM v0.49 @6bed773b76, section 2 row D2-S72, section 3 item 6) | **Decomp cell:** `IB-pr-474` (decomposition section 157) | **outcome_ref:** FWD-14

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-329/` (bash `/c/dev/wk-irpt-bckend-329`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it).

**HARD BOUNDS.** BUILD ONLY. No AWS call (every test stubs `aws` as `tests/test_build_only.sh` does), nothing is uploaded, no source map is written, no Lambda is touched. Run no build against the real
`lambda-source-map.json`.

**Why (row IRPT_BCKEND-D2-S72, search it by id in `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`).**
`infra/aws/lambda/ci/build-and-upload.sh` stages pinned members into the working tree: a staged member whose repo path is a TRACKED file overwrites the working copy with the pinned
blob, and `cleanup_staged` (about lines 326-340, called at the top of each iteration and from the EXIT trap at line 343) restores it with
`git -C "$WORKSPACE_ROOT" checkout HEAD -- "$rel" || echo "  WARN: could not restore tracked $rel from HEAD"` (about line 332). Twice, that restore failed with
`Unable to create .git/index.lock: File exists` (another seat was committing), printed only the WARN, and the script exited 0. The members happened to equal HEAD both times;
for a member whose PIN differs from HEAD, a failed restore leaves the pinned content in a tracked file of the SHARED tree with rc 0 and only a WARN in a long log, and the next
`safe-commit` over that path would land it.

**Build (one rule).** A failed restore from HEAD fails the script loudly:
- the script exits NON-ZERO on every path after a failed restore (including when everything else succeeded, and when the failure happens in the EXIT trap), and prints one
  `ERROR:` line that NAMES every tracked file left carrying staged content (its repo-relative path);
- after a failed restore NO further member is staged (do not build on a polluted tree); an unrelated exit code that a path already returns for its own reason is unchanged;
- a restore that succeeds, and every path that stages nothing tracked, behave exactly as today (same exit codes, same output lines);
- the retry of the restore (if you add one, at most 3 tries with a short wait) is allowed only if a failed final try still ends as above. State your choice.
Keep the change small. Read the script's `trap`, `set -e` and `exit` structure first (lines 36-50, 297-343, 640-735) before editing; an `exit` inside an EXIT trap overrides the script's status in bash.

**Tests (the build's own):** `infra/aws/lambda/ci/tests/test_build_restore_fails_loud.sh`, run as `bash infra/aws/lambda/ci/tests/test_build_restore_fails_loud.sh` from the repo root. It prints ONE line per arm in the
exact form `ARM <name> PASS` (or `ARM <name> FAIL`) and exits 0 only if all hold. At least three arms, each in a THROWAWAY git repository it builds in a temp directory (the script derives
`WORKSPACE_ROOT` from its own location, so copy the script into the temp repo's `infra/aws/lambda/ci/`; see `infra/aws/lambda/ci/test_build_staging_keeps_tracked.py` and `tests/test_build_only.sh` for the working technique): (a) a tracked staged
member whose pin differs from HEAD, with the restore forced to fail (hold `.git/index.lock`): the script exits non-zero and prints an `ERROR:` line naming that file; (b) the same member with the restore NOT blocked:
exit 0 and the tracked file equals HEAD afterwards; (c) a build that stages nothing tracked: exit 0, unchanged. The existing `test_build_staging_keeps_tracked.py` (5 passed at base) and `tests/test_build_only.sh` (rc 0 at base)
must still pass, and you do not edit them.

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~329/IB165-4_restore_fails_loud_record.json`: `{base_commit, files_changed, exit_code_rule (in words, at least a sentence),
failure_message_sample (the exact ERROR line your test (a) produced), retry_choice, hash_pins: [every place in the repo that pins a hash of a file you changed, with what you did about it], deployed: false,
aws_calls_made: 0, suites: {staging_before, staging_after, build_only_before, build_only_after}}`.

<criterion id="IB165-4-AC1" cell_refs="IB-pr-474"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-4-AC1</invocation><expect>IB165-4-AC1 PASS</expect></criterion>
<criterion id="IB165-4-AC2" cell_refs="IB-pr-474"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-4-AC2</invocation><expect>IB165-4-AC2 PASS</expect></criterion>
<criterion id="IB165-4-AC3" cell_refs="IB-pr-474"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-4-AC3</invocation><expect>IB165-4-AC3 PASS</expect></criterion>

<expected_criteria>IB165-4-AC1, IB165-4-AC2, IB165-4-AC3</expected_criteria>

What the checks grade: AC1 your shell test exits 0 with at least three `ARM ... PASS` lines and none failing; AC2 the regression guard (it PASSes at base by design): `test_build_staging_keeps_tracked.py` reads at least 5 passed
and `tests/test_build_only.sh` exits 0; AC3 the record's form, `deployed` false, `aws_calls_made` 0, and that nothing outside `infra/aws/lambda/ci/` and your deliverables changed.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. `lambda-source-map.json` and every other file under `infra/aws/lambda/ci/` not named here are NOT yours.
- **Refusal clause:** if a failed restore cannot be made to exit non-zero from the EXIT trap without changing another path's exit code, STOP, file a row and report; do not weaken a test. Never weaken a check; do not edit `p165_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W329-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~329" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~329@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~329 <0.9.0_WK_IRPT_BCKEND~329@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
infra/aws/lambda/ci/build-and-upload.sh
infra/aws/lambda/ci/tests/test_build_restore_fails_loud.sh
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~329/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-474.build-and-upload-restore-failure-exits-nonzero.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 157 (round 165, workstream ~P), cell `IB-pr-474`.
<owned_cells>IB-pr-474</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB165-4-AC1, IB165-4-AC2, IB165-4-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~329/IRPT_BCKEND.TO-IB-pr-474.build-and-upload-restore-failure-exits-nonzero.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the exit-code rule in a sentence; the exact ERROR line from arm (a); the three arms; the retry choice; both existing suites' last lines before and after; the hash pins found and what you did;
each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell changes the release build script and adds one offline test; nothing is built against the real source map, uploaded or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p165_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~18:0xZ: IB165-4 AC1 FAIL (the new test is absent), AC2 PASS (the regression guard: test_build_staging_keeps_tracked.py 5 passed, tests/test_build_only.sh rc 0), AC3 FAIL (no record); commit-gate clean. AC2 passes at base by design and is not a difference control; the difference is AC1 arm (a).
lane: the <paths> block IS the grant. Class WORLD by the L6 floor (an infra path); nothing is deployed. The script is the release instrument for every Lambda pipeline: the change is small and its blast radius is any seat that runs it; the offline test and the two existing suites are the guard.
</preflight>
