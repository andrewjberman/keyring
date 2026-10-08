# Two-phase safe-commit -- build record (4.0.0_SA_CRO~A, 2026-10-08 ~17:2xZ)

**Order:** Andrew-direct ~16:5xZ and his ruling ~17:0xZ ("Yes go ahead"), record
`org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ANDREW_DIRECT_20261008_165xZ_LEAD_COMMIT_LOCK_SHRINK_BUILD.md`.
**Why:** `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/CMTQUE_LONG_TERM_ASSESSMENT_20261008.md` (one commit held the
shared commit lock about 11.4 s; option B).
**Files here:** `safe-commit.sh.candidate` (the full script to install as `.tools/safe-commit.sh`), and
`safe-commit.sh.patch` (231 lines added, 2 changed, against `.tools/safe-commit.sh` at `bb1b1e954e`).

## 1. What it does

Opt-in with `SAFE_COMMIT_TWO_PHASE=1`. Off, or not eligible, it is today's path, with one line saying why.

- **Validate, with no lock.** Staging, every safe-commit gate, and the pre-commit, prepare-commit-msg and commit-msg
  hooks run in a private git dir: its HEAD is pinned at the tip read at the start, its index is private, and it reads
  the shared working tree. The private dir's `commondir` file names the real `.git`, so objects, refs, config and hooks
  are the real ones. HEAD cannot move under the checks, and the shared index is not touched.
- **Land, under the existing lock.** Rebuild the tree from the CURRENT tip plus the validated entries
  (`read-tree`, `update-index`, `write-tree`), `commit-tree`, `update-ref` with the expected old value, set the shared
  index's entries for those paths to the commit, release.
- **Post-commit, outside the lock**, in a second private dir whose HEAD is pinned at the new commit, so the five
  post-commit scripts (all of which read HEAD) see this commit and not a later one. Three of them leave background jobs,
  so that dir is kept and removed by a later run once it is an hour old.
- **Race:** a commit that loses only waits for the land lock. It re-validates only if a commit that landed after its
  start changed one of the same files, and it re-runs at most 3 times in total.
- **Eligible only:** main (shared) worktree; not a submodule; a branch checked out; only `--author 'Name <email>'`
  plus `-F` or `-m`; no `GIT_DIR`, `GIT_WORK_TREE` or `GIT_INDEX_FILE` from the caller; `commit.cleanup` unset;
  the queue path not requested. A linked worktree has its own lock, so it has nothing to gain.
- **Logs** one `LANDED-2P` row per commit to the audit log: validate, wait, hold, build, ref and post-commit seconds,
  plus the attempt number. `RETRY-2P` on a same-file race. The existing `LOCK-WAIT` row is unchanged.

## 2. Tests run (laptop, shared tree, real commits, 2026-10-08 17:02Z-17:17Z)

| # | Test | Result |
|---|---|---|
| 1 | Today's path through the candidate (flag off), one commit | landed `ceace9882f`, msg-verify MATCH |
| 2 | Two-phase, one commit | landed `a92d59d74f`; shared index clean; owned-paths PASS row written by the hook |
| 3 | Four two-phase plus one today's-path commit started together; a live `1.0.0_SA_CTO` commit landed in between | all 5 landed, rc 0; two-phase holds 0.99-1.35 s; waits 4.7-25.6 s, all behind today's-path holders |
| 4 | Two two-phase commits of the same file at once | one landed (`3c2e93db02`); the other logged `RETRY-2P`, re-validated, and stopped with "nothing to commit", rc 1 |
| 5 | Pre-commit refusal: an edit to `org/XXX.md` (law-lock hook) | refused in validate, rc 1; nothing landed; shared index clean; the file restored byte for byte |
| 6 | Deletions: 1 path (`dd99f228dd`), then 8 paths (`7e2f61642c`, rebuilt candidate) | landed; paths gone from HEAD; shared index clean |

A probe meant as a lane-refusal test landed instead (`bf5f9303af`, a file in `1.0.0_SA_CTO/deliverables`). The
owned-paths hook ran and wrote PASS: this lane is allowed that path, so it was not a negative test. It was removed in
`dd99f228dd`, and test 5 is the negative. Test files t0-t7 were removed in `7e2f61642c`.

## 3. Measured numbers (from the LANDED-2P rows)

- Lock held per two-phase commit: **0.99-1.91 s** (7 commits), against 11.42 s for today's path (trace, 16:2xZ). Of
  that, rebuilding the tree is 0.60-0.82 s and the commit plus ref plus shared-index update 0.36-0.88 s.
- Wait when nothing else was landing: 0.09-0.28 s.
- Post-commit, now outside the lock: 3.09-6.91 s.
- Validate (the seat's own time, no lock): 11.5-30.1 s. The box was under load during these tests (the today's-path
  commit in test 1 took 35 s against 12 s earlier).

## 4. Not tested, and known limits

- Linked worktrees, submodules, `-C`, `--amend` and the other excluded forms: they take today's path by design.
- Other boxes: not run anywhere but the laptop.
- A post-commit job still running more than an hour after its commit loses its pinned view.
- Checks no longer see changes other commits made to OTHER files during validation. That is the trade Andrew approved
  at ~17:0xZ.
- While some seats still use today's path, a two-phase commit waits behind them for their full run, up to 25.6 s in
  test 3. The gain arrives when the default flips.

## 5. To install

1. `0.0.0_AB_MSTR` replaces `.tools/safe-commit.sh` with `safe-commit.sh.candidate`, checks the diff against
   `safe-commit.sh.patch`, then runs `bash -n` and one flag-off commit. Default stays off, so nothing changes for any
   seat until step 2.
2. Turning it on by default is Andrew's call (open call at `4.0.0_SA_CRO~A`).
3. Remove the dev copy `.tools/safe-commit-2p-dev.sh` (untracked, made by this seat) after step 1.
