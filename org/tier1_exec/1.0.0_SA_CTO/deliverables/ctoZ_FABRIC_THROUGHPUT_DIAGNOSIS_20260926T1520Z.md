# WHY TOKENS-PER-RUNTIME COLLAPSED: it is LOCK-WAIT AND SUBPROCESS WALL TIME, not the device
`1.0.0_SA_CTO~Z`, 2026-09-26 ~15:2xZ

**Asked by Andrew, verbatim:** *"CPU/Memory activity is not strained, antivirus is not acting up, seemingly
everything is running fine on this device, but when I look at the token count in a given session on a
long-running job, they are lower than ive ever seen, with regard to tokens/runtime. Usually this is indicative of
some kind of halting somewhere. I want to restart the fabric but before doing so need to clarify if there is
anything going on here, device-side, that would be causing a slowdown. This is why I thought perhaps it is a
commit storm, but index lock is also same problem."*

**Committed as a RECORD rather than left in a terminal because a restart is imminent and this analysis would not
survive one.**

---

## 1. THE ANSWER

**It is not a commit storm, nothing is hung, and `git gc` will not help.** His instinct that low
tokens-per-runtime means halting is correct -- but the halt is **lock-wait and subprocess wall time**, which is
exactly why CPU reads idle. A seat blocked on a gate stack burns minutes and emits almost no tokens.

### What this RULES OUT, measured

| measure | value | reading |
|---|---|---|
| commits per UTC hour, 6h | **9, 11, 10, 9, 12, 10** | FLAT -- no storm |
| git processes | 2 MSYS, **0** Windows-visible | nothing stuck holding the index |
| loose objects / garbage | 119 / **0 bytes** | already packed |
| packs / in-pack | 4 / 1.17 GiB | healthy |
| `prune-packable` | 0 | nothing to reclaim |

**So the 1.6 GB `.git` is not bloat -- it is a large, well-packed repo, and repacking is not the lever.** That
matters because `gc` is the obvious remedy and it would have cost hours for nothing.

---

## 2. WHAT IS ACTUALLY COSTING THE WALL CLOCK

| cause | measured |
|---|---|
| tracked files | **44,589** |
| a bare `git status --porcelain` | **822 ms** (healthy is 50-100 ms) |
| `git ls-files` | **865 ms** |
| `git worktree list --porcelain` | 601 ms |
| **worktrees sharing ONE `.git/index.lock`** | **56** |
| live `claude.exe` | 10 |
| gates per `safe-commit` | ~8 (comp-pulse, commit-gate, ds-precommit, ruff, to-pipeline-gate, surprise-row-gate, prd-manifest, missions-tree-check) |
| git hooks chained per commit | `pre-commit` -> `pre-commit.chained-gitlinkpub`, `commit-msg` -> `commit-msg.chained-ascii`, `post-commit` |

**The composition is the cost.** Every commit from any of 56 worktrees takes the same lock; ~10 live seats
therefore serialize. On top of that each commit runs ~8 gates, several of which walk all 44,589 files, plus 3
chained git hooks -- **in a repo where a single `git status` already costs 822 ms, so every gate that shells to
git pays about a second, repeatedly.**

**DIRECT EVIDENCE FROM THIS SEAT, which is the clearest instance of his symptom:** several of my own commits
**exceeded the 120-second harness timeout and were moved to the background.** That is minutes of runtime, and
near-zero tokens, for ONE commit. Others needed 2-3 retries against `index.lock: File exists`. The lock was
measured ABSENT between attempts while MSYS showed live git processes -- so it is **millisecond churn from live
peers, not a stale lock**, and nothing should be deleted.

---

## 3. THE GITLINK HOOK MADE IT WORSE, AND THAT ONE IS MINE

I carried the ADOPT on the gitlink publication check. It was installed into the **shared** `.git/hooks` while its
script lives in the tree, so it added a process spawn to EVERY commit in EVERY worktree.

**Measured now: `worktrees 56 | carry the script 1 | MISSING 55`.**

- **Before the 12:5xZ repair** it hard-failed `No such file or directory` and **refused every commit in 55 of 56
  worktrees** -- silently, until a worker's first commit after its work was already done.
- **After the repair** it fails open with a printed WARN, so commits flow -- but the gate is **installed and
  inert for 98% of the fabric**, and still pays a doomed subprocess spawn per commit.

**So it is currently the worst of both: no protection, full cost.** By NEVER-2's own definition that is a
half-landed deploy.

---

## 4. THE ONE NUMBER I CANNOT EXPLAIN

**23 `node.exe` processes**, against 10 `claude.exe` and 1 `bun.exe`.

I will not guess at these. They could be MCP servers, Playwright, Vite workers, or orphans from earlier sessions.
**If any are orphaned, every MCP tool call may be paying for them, and that would be a per-call tax invisible to
CPU averages.** This is the single item in this record I could not close, and it is where I would look first
device-side. Naming it as UNRESOLVED rather than folding it into the explanation above, because an unmeasured
cause sitting beside measured ones borrows their credibility.

---

## 5. THE TWO LEVERS, NEITHER OF WHICH THIS SEAT PULLED

1. **Prune worktrees.** 56 sharing one index is the root of the serialization. **NOT blindly** --
   `2.0.0_SA_COO~Y` warned that several carry in-flight worker state, so each tree needs its own check first.
   This is a destructive act and it is not mine.
2. **Fix or remove the gitlink hook.** Either install the script where all 56 trees can resolve it, or take the
   hook out until it can be. Leaving it inert-but-spawning is strictly worse than either.

**Not recommended:** `git gc` / repack. Section 1 measured why -- 119 loose objects and zero garbage.

---

## 6. WHAT THIS RECORD DOES NOT CLAIM

It does not claim the fabric is stalled -- **12 commits across 9 authors in 90 minutes**, and round-6 cells
draining, say otherwise. It does not measure the laptop fabric. It does not measure inference latency, only the
wall time around it. **And it corrects one of my own numbers:** I earlier reported the `~O` fabric at "0 commits
in 3h" from a window starting 15 minutes in the FUTURE; measured properly, `1.0.0_SA_CTO~O` committed at 10:33
local. That zero was my arithmetic, not that fabric's state.

## Compiler Tools

`git count-objects -vH` for the gc question, which answered it in one call and in the negative -- explicit
`date -u` windows after a `--since` with a local offset produced a FUTURE window and two vacuous zeros --
per-op wall timing with `date +%s%N` around read-only git calls, so the 822 ms is measured rather than felt --
`tasklist` AND MSYS `ps` read together because the two namespaces are disjoint on this device -- a per-worktree
`[ -f ]` loop for the 1-of-56 script coverage, printed with its denominator.
