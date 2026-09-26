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

## 5a. AMENDMENT A1, 16:0xZ -- BOTH LEVERS IN SECTION 5 ARE WRONG. SECTIONS 1-2 STAND.

**Andrew is assessing from this record, so this correction leads rather than trails.** Two seats corrected it
within twenty minutes of the commit: `3.0.0_SA_CVO~Z` (msg 26116) and `0.0.0_AB_MSTR~Z` (msg, 15:52Z).

### LEVER 2 IS ALREADY CLOSED, AND WAS CLOSED THREE HOURS BEFORE I WROTE IT

`0.0.0_AB_MSTR~Z`, which owns the hook, ran **the hook itself**: **56 of 56 worktrees return `rc 0` from
`.git/hooks/pre-commit`**, 54 of them still lacking the script locally. The repair landed **12:5xZ, about three
hours before this record**. Installer matched at `df88ff736f`; a SECOND defect -- its exec line silently killing
an appended owned-paths lane check -- fixed at `1e938fb25d`. All on origin.

**So "inert for 98% of the fabric" is FALSE. The gate RUNS in 56 of 56 via the derived `$MAIN` fallback**, and
removing it would drop live protection. The per-commit subprocess cost stands; the "no protection" half does not.

**THE ERROR IS WORSE THAN A STALE NUMBER: I HAD READ THE REPAIRED CODE MYSELF.** I read the resolution block,
quoted its two WARN lines approvingly, and then reported the FAIL-OPEN branch as the operative path -- when the
`$MAIN` candidate two lines above it is what fires. **I fixated on the branch I had asked for and missed the one
that runs.**

> **When a gate's LIVENESS is the question, RUN THE GATE.** File presence is a proxy for a resolution path, and a
> resolution path can have a fallback. MSTR read `rc 0` from the hook; `3.0.0_SA_CVO~Z` and I both counted FILES.
> **Two seats using proxies disagreed with each other AND with the one seat that ran the thing** -- the CVO read
> `MAIN present 56 / NEITHER 0`, I read `MAIN present 48 / NEITHER 16`, and neither figure was the answer.

**My own census was the least trustworthy of the three and I say so with its cause:** I hand-inlined the hook's
resolution and **dropped two `case` arms it has** (the `?:\\*` form and the empty-`CDIR` fallback), so any
worktree where `rev-parse` returned empty resolved `$MAIN` wrongly into my NEITHER bucket. I also read the
denominator as **64** where two seats independently read **56** -- mine is the outlier and I do not defend it.

### LEVER 1 IS NOT A CHEAP WIN EITHER

`0.0.0_AB_MSTR~Z` measured it rather than let anyone prune on my framing: **56 registered, 0 already-dead by
`git worktree prune --dry-run`, and 53 of 56 carrying unmerged commits against `origin/CLOUD` or dirty files.
ONLY 3 LOOK SAFE.**

**So calling this "the single biggest lever and it's cheap" was wrong on the second half.** The serialization
diagnosis is right; the remedy is expensive and destructive, `2.0.0_SA_COO~Y`'s warning holds, and it needs
Andrew's word. **A correct diagnosis does not license a cheap remedy, and I bundled them.**

### WHAT STANDS, CONFIRMED BY MSTR IN TERMS

**Sections 1 and 2 are untouched:** no commit storm, nothing hung, `gc` gains nothing, and the serialization
cost -- 44,589 files, 822 ms `git status`, 56 worktrees on one `index.lock`, ~8 gates plus 3 chained hooks per
commit, my own commits crossing the 120 s timeout. **The analysis survives; both prescriptions did not.**

**Section 4's 23 `node.exe` remains the one open item**, and nothing above touches it.

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
