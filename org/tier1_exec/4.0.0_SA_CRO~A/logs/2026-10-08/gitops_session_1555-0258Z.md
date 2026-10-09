# 4.0.0_SA_CRO~A -- GitOps session, 2026-10-08 ~15:55Z to 2026-10-09 02:58Z (laptop)
**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Summary

Andrew set this lane's focus at session start: "I need you on the git ops, that will be your focus for this session". In
48 commits the lane:
- moved the monolith from one shared CLOUD branch to per-box branches with one integrator;
- made merges and commits run outside the shared tree and lock;
- taught the merge path to resolve the multi-writer conflict classes itself;
- landed Andrew's per-box law edit.

Process GC moved to 4.0.0_SA_CRO~B.

## Work done (in order; evidence = the commit, and its message carries the measurement)

1. **The GitOps L1 brief and the fast-fix list** (58a71ae779, 5504357066). The F4 union was rolled back by
   0.0.0_AB_MSTR; that was my error and is recorded at a477ba49fb.
2. **CMTQUE assessment** (65a1defac0): shrink the commit lock; do not revive the queue.
3. **Two-phase safe-commit** (bc84cb0d7a, 2d3effcf0f):
   - phase one validates in a private pinned git dir with no lock;
   - phase two lands under the lock with plumbing;
   - default ON; `SAFE_COMMIT_TWO_PHASE=0` opts out;
   - exercised with 9 parallel test commits, then removed (7e2f61642c).
4. **Per-box branches.**
   - Design: 049d81ffa6, 7242a56f84; Andrew answered the four calls ~18:0xZ.
   - B1: box/* is a shared branch (never-rules gate), plus the /integrate BOX and INTEGRATOR passes (7b8188d74a, dfaf3f59b1, dd143e3767).
   - B2: a box deploys on its own push (84bbe98f80); a box push deploys only scripts an OPEN change-management ledger entry names (5dd561c0eb, CTO ruling 107341).
   - B3: root cause of long merges (0db423ed37); path-scoped merge grading (29f80d221a, Andrew ~19:1xZ "Sure, yes").
5. **`.tools/box-sync.sh`** (ae02d7548f): box and integrate passes as a program.
   - It merges with `git merge-tree`, grades on a private index, writes with `commit-tree`, and lands by compare-and-swap.
   - It runs from a scheduled task on each box (8c9e0f9043, Andrew call 1 = B; site Z Git Bash fix bae7abf0d1).
   - All four boxes are switched; integrations run at :00 and :30.
6. **safe-merge**:
   - logs every attempt, and a killed merge no longer blocks its worktree (2ee73e5a64);
   - FAST LANE: a clean merge never opens in the shared tree (2732b61933);
   - safe-commit lock release checks the owner (b02c5becd6).
7. **Deletions on Andrew's word**: the CL-fabric vestiges (12ba84488a); org/tier1_exec/2.1.0_SA_COO (b44b5d76df).
8. **Microproduct policy**: the activity study (0c0fa8fe79); ADOPTED, Andrew ~22:4xZ (f47e363dd3).
9. **merge-resolve-known.py**: merges resolve multi-writer channel files and generated index rows themselves.
   - First cut d79ba738e2; separator fix 3e4b43c0a4.
   - One-list JSON channel files merge by row (324be222dd).
   - One-block-per-row files merge by the id inside each block (9e3e6fa035).
   - Replay of every merge since 2026-10-06 (1,188 merges, 220 conflicted channel files): 217 resolved, every one equal to what landed; 3 left to a person, each a real conflict.
10. **Law edit** (538f0f51a7), Andrew ~23:3xZ "Yes for both", order record ff07fe49e1:
    - CLAUDE.md NEVER-rebase and Git sections, and org/XXX.md SHARED-BRANCH LAW, name box/<box> branches and CLOUD's one writer;
    - broadcast to 9 live seats, 9 DELIVERED;
    - q/* delete: 149 deleted by 0.0.0_AB_MSTR (msg 107499); ls-remote reads 10 left, the KEEP list, owner 2.0.0_SA_COO~M1.
11. **surprise-row-gate patches** (gate owner 1.0.0_SA_CTO; 0.0.0_AB_MSTR applies):
    - DUAL-MINT admit (c8d7080d6b), applied @5ce6b2121c. dell1 then merged into CLOUD 71aac4e90d.
    - A pair already at HEAD freezes nothing on commit or drain, and the remediation wait is scoped to the row's own workstream (1dadca7e01; CTO 107628, 107639; MSTR 107647). Self-test 246/246. Handed to 0.0.0_AB_MSTR as msg 107656; NOT yet applied at log time.
12. **`box-sync.sh status`** (7bfc6ede72): any seat can read each box branch's lag against CLOUD from git.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| native Grep/Glob | locate merge-resolve-known callers | PASS |
| comp-find rail | refused one raw directory grep | WARN: rerouted to native Grep |
| surprise-row-gate --self-test | 235 -> 236 -> 246 arms | PASS |
| .tools/test-merge-resolve-known.py | 10 -> 15 arms | PASS |
| ruff py39 + py_compile | every .py change | PASS |
| commit-gate / safe-commit gates | every commit | PASS; CLAUDE.md byte budget refused 3 times until trimmed |

- **What worked:** grading a merge in a private GIT_DIR with HEAD and MERGE_HEAD pinned. It reproduced dell1's exact refusal hashes off the box.
- **What failed:** two scratchpad folders were deleted under me by another session's startup cleanup. Working files now live under .git/cro-a-replay/.
- **Gap found:** each box's BOX-SYNC audit rows are untracked, so no box can see another box's holds. The status command reads the same fact from git instead.

## MCP traffic (significant only)

- **Received:**
  - 1.0.0_SA_CTO 107530 (DUAL-MINT ruling), 107628 (pair at HEAD), 107639 (workstream scope);
  - 0.0.0_AB_MSTR 107499 (q/* done), 107556 (DUAL-MINT landed), 107647 (drain path);
  - acks from seats on the law edit.
- **Sent:**
  - the law broadcast (107501-107509);
  - the gate hand-offs to 0.0.0_AB_MSTR (107546, 107656);
  - the closure to 1.0.0_SA_CTO (107559).

## Files modified

See commit messages for the 48 commits listed by `git log --author="4.0.0_SA_CRO~A" --since=2026-10-08T00:00Z`.
Tools owned by this lane:
- .tools/safe-commit.sh
- .tools/safe-merge.sh
- .tools/box-sync.sh
- .tools/box-sync-schedule.ps1
- .tools/merge-resolve-known.py
- .tools/test-merge-resolve-known.py
- .tools/deploy-ledger-names.py
- .tools/git-hooks/pre-push-safe-deploy.sh

## Blockers

None at this lane. The pair-at-HEAD and workstream patch waits on 0.0.0_AB_MSTR applying it (msg 107656). That is a
hand-off, not a block; dell1 lands rows meanwhile under the audited override.

## Current State

- **Branches:**
  - each box commits to `box/<box>`; CLOUD has one writer, 0.0.0_AB_MSTR, via `.tools/box-sync.sh integrate` at :00 and :30;
  - box passes run at each box's slot from its scheduled task (`.tools/box-sync-schedule.ps1`);
  - at 02:47Z, `bash .tools/box-sync.sh status` read dell1, laptop and sitez 0 behind CLOUD, and dell2 93 behind (last take 02:18Z, next slot :48).
- **Merge path:**
  - box-sync and the safe-merge fast lane call `.tools/merge-resolve-known.py` on conflicts;
  - three channel shapes are handled: section, one-list and one-block-per-row; generated `org/projects/<CODE>.json` rows are regenerated;
  - the row gate `.tools/surprise-row-gate.py` grades the result.
- **Push state:**
  - origin/box/laptop 24c42f7fc7 at 02:49Z (ls-remote read);
  - 1dadca7e01, 9e3e6fa035 and 7bfc6ede72 are LOCAL and ride the next box pass;
  - 324be222dd is on CLOUD and on all four box branches.
- **Deliverables:** `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/`, including:
  - PER_BOX_BRANCH_DESIGN_20261008.md;
  - MERGE_ROOT_CAUSE_B3_20261008.md;
  - ACTIVITY_STUDY_AND_MICROPRODUCT_POLICY_20261008.md;
  - Q_BRANCH_DELETION_LIST_20261008.md;
  - the two gate patches.

## Next Steps

1. [0.0.0_AB_MSTR] Apply PAIR_AT_HEAD_AND_WORKSTREAM_surprise-row-gate.patch (msg 107656), then tell dell1.
2. [4.0.0_SA_CRO~A] After the next pass, confirm 1dadca7e01, 9e3e6fa035 and 7bfc6ede72 on CLOUD and on every box (`box-sync.sh status --fetch`).
3. [4.0.0_SA_CRO~A] Microproduct policy rule 6: record rejected pushes to the microproduct DEV trunks. Deferred, nothing blocked.
4. [2.0.0_SA_COO~M1] Owns the 10 kept q/* branches (dell1 MDPF_SECCLASS).
