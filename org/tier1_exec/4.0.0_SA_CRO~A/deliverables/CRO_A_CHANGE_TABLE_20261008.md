# 4.0.0_SA_CRO~A -- changes this seat drives, with write paths and finish times (2026-10-08 ~17:2xZ)

Answers `1.0.0_SA_CTO` msg 107018 (Andrew-direct ~17:1xZ). Scope: GitOps, on Andrew's word ~15:5xZ and the build
order of ~16:5xZ (`org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ANDREW_DIRECT_20261008_165xZ_LEAD_COMMIT_LOCK_SHRINK_BUILD.md`).
**None touches 2.0.0_SA_COO~C's fences:** no `infra/aws/terraform/nfra-ctlpln-identity/`, no `org/devices/`, and no
linked worktree. All work is in the laptop's shared tree, branch `CLOUD`.

| # | Change | Write paths | Writer | Worktree | Expected finish (UTC) | State |
|---|---|---|---|---|---|---|
| 1 | Two-phase safe-commit: candidate, patch and build record | `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/sc2p/` | 4.0.0_SA_CRO~A | shared tree | done 17:2xZ (`bc84cb0d7a`) | DONE |
| 2 | Install the candidate as the live script, default OFF (no seat's behavior changes) | `.tools/safe-commit.sh` | 0.0.0_AB_MSTR (fabric infrastructure) | shared tree | done 17:30Z (`a6096926a5`, LD-0623) | DONE |
| 3 | Remove this seat's untracked dev copy | `.tools/safe-commit-2p-dev.sh` (untracked; no commit) | 4.0.0_SA_CRO~A | shared tree | done 17:3xZ | DONE |
| 4 | Turn two-phase on by default on the laptop | `.tools/safe-commit.sh` (one default value) | 0.0.0_AB_MSTR | shared tree | ~18:1xZ if Andrew says yes | AT ANDREW |
| 5 | Same default on dell1, dell2 and site Z | none by this seat; the trunk carries #4 | each box's MSTR, on its drain | each box's shared tree | after the laptop's first busy hour reads clean | AFTER #4 |
| 6 | GitOps long-term research (per-box "is git the cause" read from the new LANDED-2P and LOCK-WAIT rows; a conflict-free design for shared files; branch-model cost record) | `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/` only | 4.0.0_SA_CRO~A | shared tree | not scheduled; as Andrew asks | OPEN |

**Side effect to know about:** each two-phase commit leaves a small post-commit view dir,
`.git/sc2p-pc-<epoch>-<pid>/` (two files). It is untracked, and a later two-phase run removes any older than an hour.

**Update 17:3xZ:** `1.0.0_SA_CTO` msg 107030 made `4.0.0_SA_CRO~A` the one owner of `.tools/safe-commit.sh` and
`.tools/safe-merge.sh`. Rows 2 and 3 are done. This update was committed through the INSTALLED script with
`SAFE_COMMIT_TWO_PHASE=1`, as the live check of the install.
