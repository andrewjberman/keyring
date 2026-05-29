# ws Commit-Serialization — Staging-Inside-Lock Design (safe-commit.sh)

**Author:** 1.0.0_SA_CTO
**Date:** 2026-05-29
**Directive:** MSTR ARCH RULING (Andrew-delegated Tier-0, LD-0090) — serialized commit-mutex, integrated into safe-commit.sh, always-on, mkdir-lock, stale-break, per-worktree.
**Status:** DESIGN FOR MSTR REVIEW — do NOT land fabric-wide until reviewed (touches every commit path).

---

## 1. Critical finding — the LD-0138 mutex is ALREADY present and is NOT sufficient

`safe-commit.sh` **already carries a mkdir-mutex** (lines 113-136, shipped LD-0138 `aad93b23b`): `--absolute-git-dir/commit-queue.lock`, kill -0 stale-reclaim, 60s timeout, EXIT-trap release. It serializes `safe-commit ↔ safe-commit` bodies correctly.

**Yet I hit the contamination abort TWICE this session (post-LD-0138)** on a routine cycle-log commit (incident `2fc731ae2`, cleared via `git commit --only` fallback). So "add a mutex" is already done — and demonstrably doesn't close the race. **The design must address WHY.**

## 2. Root cause — the race is in `git add`, which the mutex does not cover

The mutex serializes the *safe-commit body*, but **`git add` is run by callers OUTSIDE safe-commit**, and the ajb_workspace worktree has **ONE shared index** across all co-located agents. Two unguarded sources pollute it:

1. **Caller pre-staging** — agents (including me) run `git add <file>` in a *separate* step before invoking safe-commit (the org/XXX.md "new file needs git add first" pattern). That add is not inside the mutex.
2. **Peer out-of-band adds** — another agent (this session: DE) stages *its* files via its own workflow; they sit in the shared index. When my safe-commit captures `git diff --cached` (line 156, inside my lock), it sees DE's staged files → flagged as contamination → abort.

The mutex can't help: DE was never in a safe-commit when it staged. **Serializing safe-commit↔safe-commit is necessary but not sufficient; the staging step itself must be inside the serialized section, and the guard must stop treating peers' pre-staged files as contamination** (the `--only` commit already excludes them — they are harmless).

## 3. Design — three coordinated changes

### 3a. Move staging INSIDE the lock (safe-commit owns the `git add`)
Callers STOP running `git add` separately. Inside the mutex, after acquiring, safe-commit stages its OWN declared pathspec:
```sh
# inside lock, before the contamination check:
git add -- "${PATHSPEC[@]}" 2>/dev/null || true            # tracked + normal new files
# gitignored-prefix new files (e.g. .tools/) need -f:
git add -f -- "${PATHSPEC[@]}" 2>/dev/null || true         # idempotent; -f is safe for already-tracked
```
This collapses the agent's add→commit window to zero (it's one locked critical section), eliminating source (1) entirely. Backward-compatible: if a caller still pre-`git add`s its own pathspec, re-adding is idempotent.

### 3b. Baseline-diff contamination guard (ignore peers' pre-staged files)
Capture the staged set at lock-entry as a **baseline**, BEFORE 3a's staging. The guard then checks only what THIS invocation added beyond pathspec — which is impossible by construction (we add only pathspec). Peers' pre-staged files are in the baseline → excluded → no false abort. `--only` already guarantees they're never committed.
```sh
BASELINE="$(git diff --cached --name-only)"      # foreign + any pre-staged, captured first
git add -- "${PATHSPEC[@]}" ...                  # 3a
STAGED_NOW="$(git diff --cached --name-only)"
# contamination = files newly staged by THIS run that are outside pathspec:
#   (STAGED_NOW \ BASELINE) \ PATHSPEC   → must be empty
```
Genuine self-scope errors (agent's own stray add inside the run) still caught. Peer files no longer false-positive. **This is the change that actually fixes the incident I hit.** MSTR's "keep the guard" intent is preserved — it just stops policing peers.

### 3c. Mutex — KEEP as-is (LD-0138), with one belt-and-suspenders add
The existing mkdir-lock + kill -0 stale-reclaim + `--absolute-git-dir` per-worktree path + 60s timeout are correct and MSTR-aligned. **Add MSTR-requested mtime stale-break** as a second reclaim path (covers a holder whose PID was *reused* by a different live process — kill -0 would wrongly read it as alive):
```sh
# in the stale-check, after the kill -0 branch:
if [ -d "$LOCK_DIR" ]; then
  lock_age=$(( $(date +%s) - $(stat -c %Y "$LOCK_DIR" 2>/dev/null || echo 0) ))
  if [ "$lock_age" -ge "$LOCK_TIMEOUT_SEC" ]; then rm -rf "$LOCK_DIR"; continue; fi
fi
```
(`date +%s` and `stat -c %Y` are both in Git-Bash 3.6.7 default — Rule 16 OK. `stat` confirmed present; if a target env lacks it, `find "$LOCK_DIR" -maxdepth 0 -mmin +1` is the guarded fallback.)

## 4. Parameters (MSTR sanity-check surface)
- **Stale-lock timeout:** 60s (existing `SAFE_COMMIT_LOCK_TIMEOUT`, unchanged). Dual reclaim: dead-PID (`kill -0`) immediate, OR lock-age ≥60s (mtime). A crashed/PID-reused holder can't deadlock the fabric > 60s.
- **Lock path:** `$(git rev-parse --absolute-git-dir)/commit-queue.lock` — per-worktree by construction (main `.git/`, linked worktree `.git/worktrees/<name>/`, feature_clb its own). CLOUD / DEV / PROD / feature_clb each get a distinct lock = correct per-index serialization. (LD-0138's exact scheme; unchanged.)
- **Always-on:** no toggle (per MSTR — a toggle is a "forgot to flip it" footgun; the mutex is cheap). `SAFE_COMMIT_LOCK_DIR` env override retained for tests only.
- **EC2/SSM exempt:** separate machines, no shared local index — N/A (these run on Amazon Linux, Rule 16 boundary; safe-commit is a local-runtime tool).

## 5. Propagation + rollout (per-branch-copy hazard)
`.tools/safe-commit.sh` is a **separate file per branch worktree** (the LD-0138 / `reference_infra_tooling_fixes_dont_propagate_across_branch_worktree_copies` lesson). This design lands on CLOUD first (review), then ports byte-exact to COMP/feature_clb via `git show <branch>:.tools/safe-commit.sh` under the domain author — NOT assumed to propagate. `record-terraform-deploy.sh` wraps safe-commit → inherits automatically.

## 6. Caller-migration note (the one behavior change)
Agents currently do `git add <newfile> && safe-commit ... -- <newfile>`. Post-change, the `git add` is redundant (safe-commit stages inside the lock) but HARMLESS (idempotent + baseline-diff ignores it). No forced migration; org/XXX.md Step-1b "new file needs git add first" guidance gets a one-line update noting safe-commit now self-stages. Zero breakage for existing call sites.

## 7. Reversibility
Every layer reversible: 3a/3b are a contained diff to one file; revert restores prior behavior. Mutex already present. No data migration, no state. Land on CLOUD, observe one dense multi-agent window, then port.

## 8. Open question for MSTR
3b changes the guard from "whole-index clean" to "this-run-added-nothing-out-of-scope." That is strictly more correct for a `--only` commit (which can't commit unstaged-by-this-run files anyway). Confirm you're comfortable the guard's *scope-error-catching* value is fully preserved by the baseline-diff (I believe it is — a genuine self-scope error = agent adds a file outside its pathspec in the same run, still caught). If you'd rather keep the stricter whole-index check AND just rely on the mutex, I can show why that re-introduces the exact false-positive I hit this session.
