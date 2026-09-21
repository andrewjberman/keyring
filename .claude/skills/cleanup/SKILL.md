---
name: cleanup
description: Identify and remediate this device's recurring disk-space pools -- git worktree sprawl and leftover Terraform provider temp files -- deleting what is safe by construction and flagging, never deleting, the one pool that needs a content-level review first. Use on "cleanup", "clear disk space", "we're running low again", "clean up worktrees".
---

# /cleanup -- recurrent disk-space pools

**Built from a live incident (Andrew-direct 2026-09-17):** this box hit 5.02 GB free / 97.9% used
on a 237 GB volume. Hand cleanup that night reclaimed ~14 GB in three passes -- fully-merged git
worktrees, orphaned worktree-directory husks, and leftover Terraform provider extraction temp
files -- before this skill existed. His words creating it, verbatim: *"We need a skill called
/cleanup that identifies these recurrent storage pools and remediates them, which is usually just
deleting them. The only one that requires more review is the active worktrees, and policy
surrounding their deletion."*

Engine: `.tools/cleanup-disk.ps1`. This skill is the procedure around it, not a replacement for
reading its output.

## The pools, and why each one recurs

| Pool | Policy | Why it keeps coming back |
|---|---|---|
| `terraform-provider-temp` | **AUTO-DELETE** | Every `terraform` invocation (incl. `safe-apply.sh`) that does not exit perfectly clean leaves a `terraform-provider<random>` file in `%LOCALAPPDATA%\Temp` -- ~149 MB each. 53 of them were 5.92 GB on this box alone, all from two days of ordinary apply traffic. |
| `terraform-provider-cache` | **AUTO-DELETE** | `terraform init` writes one full AWS provider (686 MB at v5.100.0) into `.terraform/providers` PER ROOT PER WORKTREE -- 10 roots = 6.71 GB per worktree, no shared plugin cache. Measured 2026-09-20: 28 such dirs in four idle worktrees were 18.78 GB and took the box to 0 bytes free mid-round. Removed only in NON-LIVE linked worktrees, never the shared checkout; `terraform init` restores them from the committed lock file, and no state, planfile or scratch is touched. The prevention is the issuer's: `TF_PLUGIN_CACHE_DIR`, one apply worktree at a time, removed after its drain. |
| `orphaned-worktree-dirs` | **AUTO-DELETE** | A worktree directory removed by hand (`rm -rf` instead of `git worktree remove`) leaves a dangling admin entry git still half-tracks, or the reverse -- a directory with no git claim on it at all. Either way there is nothing left to lose; `git worktree prune` closes the bookkeeping. |
| `merged-worktrees` | **AUTO-DELETE** | A worker's worktree whose branch is fully merged into **both** `origin/CLOUD` and `origin/SITEZ` is a complete duplicate of content already safe on the remote. Nobody drains these once the round closes; they just sit. |
| `unmerged-worktrees` | **REVIEW ONLY -- never auto-deleted** | A worktree carrying a commit that is on **neither** shared branch is the *only copy* of that commit. This is the pool Andrew named explicitly. See below. |

New pools get a new row in `.tools/cleanup-disk.ps1`'s registry as they're found. Do not grow an
existing pool's identify logic to cover a class it wasn't built for -- that is how a false
"merged" verdict happens.

## The worktree policy (the part that needs more than deletion)

**What counts as LIVE, and is therefore untouched by every pool, not just the review one:** a
worktree whose most recent file write is within the last `-LiveWindowHours` (default **6**), or
whose path is passed via `-ExcludePath`. This is a heuristic that can only fail SAFE -- it can
delay cleanup of something actually dead, it can never delete something actually alive faster than
the window. Do not narrow it below a round's real cadence without measuring that cadence first.

**Among worktrees that are not live, the split that matters is per-commit, not per-branch:**

- **Fully merged into both `CLOUD` and `SITEZ`** -- the merge already carries every byte. Removed
  via `git worktree remove` (never a raw `rm`, so git's own worktree-admin bookkeeping stays
  consistent) and the branch is deleted with it. Zero content risk; this is the "usually just
  deleting them" case.
- **Carrying at least one commit absent from both** -- this worktree is the only place that commit's
  content exists. **The engine will not delete it, will not suggest deleting it, and this skill does
  not either.** What happens instead:
  1. `/cleanup` (or `/cleanup unmerged-worktrees`) prints the full list: path, branch, commits
     ahead, size, and which project it belongs to.
  2. Route it for a **content verdict**, per unlanded commit, never per branch as a whole (a branch
     can be part-superseded): is the *substance* of that commit already on the current `CLOUD`/`SITEZ`
     HEAD -- landed by that exact commit, a squash, or someone independently redoing the same fix
     (**SUPERSEDED**, name the superseding commit or the HEAD region that already carries it) -- or
     does no equivalent exist anywhere (**UNIQUE**, never delete without the project's own owner)?
     `3.0.0_SA_CVO` is the standing reviewer for this (event-driven verification is exactly its
     role); route to the project's own COO/owner when CVO is unavailable or the work is squarely
     inside one live project's own round. A worked example of the task message to send is in
     `org/tier1_exec/2.0.0_SA_COO/deliverables/` under the 2026-09-17 disk-hygiene finding, or ask
     the standing MSTR seat for the exact form used that night.
  3. Only **SUPERSEDED** commits authorize deletion, and even then a human or MSTR executes it --
     the verifier marks, it does not remove.

## Invocation forms

| Form | Behavior |
|---|---|
| `/cleanup` | Run every registered pool: auto-remediate the safe four, list (never touch) the unmerged-worktree pool. |
| `/cleanup --dry-run` | Same scan, zero deletions anywhere -- prints exactly what each pool would do. Use this first on an unfamiliar box or after adding a pool. |
| `/cleanup <pool-name>` | Run one pool only, e.g. `/cleanup terraform-provider-temp`. |
| `/cleanup --window <hours>` | Override the live-worktree recency window (default 6). |
| `/cleanup --exclude <path>` | Repeatable. A path never touched by any pool this run, on top of the recency check. |

Mechanically: `.tools/cleanup-disk.ps1 [-DryRun] [-Pool <name>[,<name>...]] [-LiveWindowHours <n>] [-ExcludePath <path> ...]`.

## Procedure

1. **Run `-DryRun` first if it has been a while**, or after adding a pool, or on a box you have not
   run this on before. Read the free-space delta it reports before trusting a live run.
2. **Run it for real.** The three safe pools remediate themselves; watch for `SKIPPED (in use)`
   lines on the Terraform-temp pool -- that means a live process holds the file, which is correct
   behavior, not a bug.
3. **Read the `unmerged-worktrees` block.** If it's empty, done. If not, route it (per the policy
   above) rather than acting on it yourself. Do not re-run `/cleanup` expecting it to resolve that
   list -- it never will, by design.
4. **Report free space before/after** (the engine prints both) so the improvement is measured, not
   asserted.

## Discipline / risk notes

- **The live-worktree check is the single point of failure for the whole skill.** Every pool
  defers to it. If it is ever wrong in the unsafe direction -- touching something actually live --
  that is the bug to fix first, before trusting anything else here. It has not been wrong yet;
  say so precisely if it ever is, and widen the window rather than adding a second heuristic.
- **`orphaned-worktree-dirs` still lists what it is about to delete, size and mtime, before
  deleting it.** Nothing has ever been found there that wasn't genuine litter, but the list is
  kept because a silent bulk-delete of "things git doesn't know about" is exactly the kind of
  action that should stay inspectable.
- **This skill never touches `Downloads`, `AppData\Local\Microsoft` (OneDrive/Outlook/Edge
  caches), or any other personal or app-owned data.** Those were surfaced by hand during the
  2026-09-17 incident and deliberately left out of the pool registry -- they are a different risk
  class (an app's own cache/session state, not a build artifact) and a blanket-delete policy for
  them has not been asked for.
- **COST:** a `-DryRun` pass costs a few seconds of `git fetch` + filesystem scans, no writes. A
  live run's only ongoing cost is the git operations on non-live worktrees, which is exactly the
  same set of commands used by hand the night this was built.
- **NON-APPLICATION:** a box that has never accumulated worktrees or run Terraform locally has
  nothing for this skill to find -- it reports zero and exits, not an error.

## Cross-references

- Engine: `.tools/cleanup-disk.ps1`.
- The incident this was built from, and the exact CVO task-message form for the review pool:
  the 2026-09-17 disk-space conversation, and `org/tier0_exec/0.0.0_AB_MSTR/deliverables/` /
  `org/tier1_exec/2.0.0_SA_COO/` records from that date if a written form is needed later.
- `CLAUDE.md` Rule 14b (worktree isolation while other seats are live) is the reason worktrees
  exist at all; this skill is the maintenance half of that pattern, not a reason to isolate less.
