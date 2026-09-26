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

## 5b. AMENDMENT A2, 16:2xZ -- MY DISCREPANT CENSUS IS FULLY EXPLAINED, AND 56 IS CONFIRMED BY THREE INSTRUMENTS

A1 said my census was the outlier and did not defend it. **That was honest but incomplete: an unexplained
discrepancy left `0.0.0_AB_MSTR~Z`'s lever-1 denominator in doubt, and Andrew is deciding a restart on it.** It
is now closed.

### THE CAUSE WAS ONE BUG, AND IT IS THE TRAP THIS DEVICE HAS A BANKED LESSON FOR

I iterated worktrees with an **unquoted** `for wt in $(git worktree list ... )`. The tell, printed:

```
[1] 'C:/Users/Opal'
[2] 'Bloomberg/Desktop/ajb_workspace'
```

**Word-splitting cut every path containing a space in two.** Site Z's workspace root is
`C:/Users/Opal Bloomberg/...`, and this device's own banked lesson is *"path has a space -- 4 faces, all report
SUCCESS SHAPE."* **I walked into the exact trap I have written down for this box.**

### THE ARITHMETIC CLOSES EXACTLY, WHICH IS WHY THIS IS AN EXPLANATION AND NOT A STORY

**Predicted BEFORE measuring:** 64 iterations - 56 real worktrees = 8 extra, so **8 paths must contain a
space**, each splitting into 2 fragments = **16 non-existent paths**, which would be counted NEITHER because
neither candidate resolves under a fragment.

**Measured after:** `paths with a space: 8`. And my bogus NEITHER count was **16**. **8 x 2 = 16, exact.**

### THE LINE-SAFE CENSUS, WHICH IS WHAT SHOULD HAVE RUN

```
worktrees 56 | ROOT present 2 | MAIN present 56 | NEITHER (gate inert) 0
```

**That reproduces `3.0.0_SA_CVO~Z`'s census digit for digit** (56 / 2 / 56 / 0). So the state is confirmed by
THREE independent instruments now: MSTR ran the hook and read `rc 0` from 56 of 56; the CVO counted files with a
correct loop; and this seat, having fixed its loop, agrees with both.

### WHAT THIS SETTLES

1. **`NEITHER = 0`. The gate is inert in ZERO worktrees.** A1's withdrawal of lever 2 stands and is now
   over-determined rather than taken on another seat's word.
2. **`0.0.0_AB_MSTR~Z`'s 56-worktree denominator is SOUND**, so its lever-1 census -- 53 of 56 carrying unmerged
   commits or dirty files, only 3 safe -- is measured over the right population. **Nothing about the restart
   decision rests on my 64.**
3. **My `ROOT present` figure also corrects**, 1 -> 2, matching the CVO exactly.

> **A discrepancy is not closed by conceding it.** Saying "mine is the outlier" removed my wrong number from the
> argument and left the *disagreement* standing, which is what actually threatened the denominator a restart
> would be planned on. **Finding the bug is what closed it** -- and it cost one printed iteration list.

---

## 5c. AMENDMENT A3, 16:2xZ -- A CROSS-DEVICE CONTROL SEPARATES TWO AXES THIS RECORD CONFLATED

`0.0.0_AB_MSTR` ran the control neither device could run alone. **It is the strongest evidence in this record and
it is not mine.**

| device | worktrees | tracked files | bare `git status` |
|---|---|---|---|
| laptop, after its cleanup | **12** | 44,574 | **1335 / 910 / 865 ms** (three runs) |
| site Z | **56** | 44,589 | **822 ms** (one run) |

**Nearly identical file counts, a 4.7x difference in worktree count, and THE FEWER-WORKTREE DEVICE IS NOT
FASTER.**

### THE TWO AXES, WHICH SECTION 2 RAN TOGETHER

Section 2 listed `56 worktrees on one index.lock` beside `822 ms git status` as if they were one cost. **They are
two, and the control separates them:**

| axis | driven by | evidence |
|---|---|---|
| **PER-COMMAND LATENCY** -- why one `git status` costs ~1 s | **FILE COUNT** (44.5k), not worktree count | the control: 12 trees is not faster than 56 at the same file count |
| **CONTENTION** -- why live seats serialize and a commit needs 2-3 retries | **CONCURRENT SEATS on one shared lock** | the lock measured ABSENT between my failed attempts while peer git processes ran |

**Neither axis is "worktree count."** A tree that nobody is committing from contributes to neither.

### SO LEVER 1 FAILS ON A THIRD GROUND

1. A1: not cheap -- 53 of 56 carry unmerged commits or dirty files, only 3 safe.
2. A1: destructive, and needs Andrew's word.
3. **A3: it would not help even if it were FREE.** Pruning to 12 is exactly the laptop's state, and the laptop is
   not faster. **The remedy was aimed at a term that is not the dominant one.**

### AND MY OWN 822 ms IS A WEAKER NUMBER THAN IT LOOKED

The laptop ran **three** samples and they spread **1335 -> 910 -> 865 ms** -- a 1.5x warm-up effect. **My 822 ms
was ONE run, with no repeat and no stated cache state.** It is probably a warm figure, and I reported it as
though it were the device's characteristic latency. **The contrast in method is what exposed that; the number
itself looked fine.**

### THE LIMITS, WHICH MSTR STATED FIRST AND I ADOPT RATHER THAN SOFTEN

*"That is a natural experiment, not a designed one ... different hardware, three runs against one, and no attempt
to hold anything else constant. It cannot put a number on either term."* **So this settles DIRECTION only.** It
does not tell us how much of the wall clock is file-count latency versus contention, and nothing here should be
quoted as a magnitude.

> **A diagnosis that names two causes in one breath invites a remedy aimed at whichever is easier to change.** I
> named worktrees and file count together, then recommended pruning worktrees -- the one of the two that was
> visible, destructive and irrelevant.

---

## 5d. AMENDMENT A4, 16:3xZ -- SITE Z READS 385 ms UNDER THE PAUSE. A4 PARTLY REVERSES A3, AND FIXES AN ATTRIBUTION I GOT WRONG

### CORRECTION 1: THE THREE LAPTOP SAMPLES ARE NOT `0.0.0_AB_MSTR~Z`'s

A3 credits `0.0.0_AB_MSTR~Z` with running 1335 / 910 / 865 ms. **It did not.** The LAPTOP seat
`0.0.0_AB_MSTR` ran them; `~Z` relayed them and put them beside mine. Its own objection is the right one and
worth keeping as a rule:

> *"an instrument credited to the wrong seat cannot be asked for its method."*

**Mis-attributing a measurement does not just misplace credit -- it breaks the only route back to how the number
was produced.**

### CORRECTION 2: THE SAME DEVICE NOW READS HALF WHAT I REPORTED

`0.0.0_AB_MSTR~Z`, site Z, three runs, bare `git status`: **393 / 385 / 379 ms.** Tracked files **44,595**,
worktrees **56** -- both unchanged from my reading.

| site Z reading | value | fabric state when taken |
|---|---|---|
| mine, section 2 | **822 ms**, ONE run | ~10 seats LIVE |
| MSTR~Z's, now | **393 / 385 / 379 ms**, three runs | Andrew's Tier-1 PAUSE, fabric QUIET |

**Same device, same file count, same worktree count, roughly HALF the latency.**

### SO A3'S ATTRIBUTION WAS OVER-READ, AND THIS IS THE ANSWER TO ANDREW'S QUESTION

A3 concluded that per-command latency *tracks FILE COUNT*. **That over-read the evidence, because my 822 ms was
itself inflated by concurrency.** Under quiet, site Z does 385 ms at the same 44.5k files.

> **A LARGE SHARE OF THE LATENCY ANDREW MEASURED IS CONTENTION, NOT PER-COMMAND COST -- AND THE PAUSE IS ITSELF
> RELIEVING IT.**

That is the most decision-relevant sentence in this record, and it took four amendments and three seats to reach.
**It also means A3's cross-device comparison is confounded on BOTH arms:** the laptop's 865-1335 ms was taken at
an unstated concurrency too, so "12 trees is not faster than 56" may be comparing two different load states
rather than two tree counts. **The direction A3 claimed survives only as a weaker statement: worktree count is
not established as the dominant term.**

### LEVER 1 FAILS A FOURTH TIME

Site Z with **56** worktrees at 385 ms is **two to three times FASTER** than the laptop with **12** at
865-1335 ms. Whatever the confounds, nothing in any reading makes 56 trees the problem.

### WHAT NOBODY HAS HELD CONSTANT, STATED AS MSTR~Z STATED IT

Cache warmth and time of day also differ between these readings and **neither was held.** So the contention
reading is the honest interpretation, not a proven one.

**THE CLEAN TEST, and it needs Andrew:** three runs under load and three under pause, **back to back on one
device**, holding file count and tree count fixed. **The loaded arm cannot be run while the pause holds** -- so
this is a proposal for his resume, not something to assume past. `0.0.0_AB_MSTR~Z` named it first and I am
carrying it to him rather than claiming the result in advance.

> **My 822 ms was a single sample taken under a condition I never recorded.** A timing number without its
> concurrency state is not a device measurement; it is one moment wearing a device's name.

---

## 5e. AMENDMENT A5, 16:4xZ -- THE LOADED ARM RAN. CONTENTION IS THE DOMINANT TERM, AND THE VARIANCE PROVES IT

**Andrew resumed Tier 1 at ~16:18Z** (*"resume tier 1"*, relayed by `0.0.0_AB_MSTR~Z`), which made the loaded arm
runnable. `0.0.0_AB_MSTR~Z` named this test; this is its other half.

### THE THREE ARMS, ONE DEVICE, FILE COUNT AND TREE COUNT HELD

| arm | timings (ms) | spread | concurrency | files | worktrees |
|---|---|---|---|---|---|
| PAUSE (`0.0.0_AB_MSTR~Z`) | **393 / 385 / 379** | **14** | quiet | 44,595 | 56 |
| POST-RESUME (this seat) | **774 / 1119 / 1004** | **345** | 10 `claude.exe` | 44,597 | 56 |
| my original, section 2 | 822, ONE run | -- | ~10 seats | 44,589 | 56 |

**File count moved by 8 files across all three. Worktrees did not move at all. Only CONCURRENCY changed.**

### THE RESULT

**Latency 2 to 3x higher under load -- and the SPREAD widened from 14 ms to 345 ms, about 25x.**

> **The variance is the proof, not the mean.** A file-count-bound operation is SLOW BUT STABLE: the same walk
> costs the same every time. A LOCK-CONTENDED operation is ERRATIC, because what it waits for depends on who else
> is holding the lock at that instant. **385/385/379 is a device doing work. 774/1119/1004 is a device waiting.**

**So CONTENTION BETWEEN CONCURRENT SEATS IS THE DOMINANT TERM in the latency Andrew measured.** That answers the
question he actually asked -- why tokens-per-runtime collapsed with an idle CPU -- and it took five amendments
and three seats.

**And it vindicates my 822 ms while condemning how I reported it:** 822 sits inside the post-resume band
(774-1119). The number was real. **What was missing was its condition, and without that it was one moment wearing
a device's name.**

### WHAT THIS RETIRES

- **A3's "per-command latency tracks FILE COUNT" is now wrong as stated.** File count sets a FLOOR (~385 ms);
  concurrency is what moved the number Andrew saw. A4 already softened it; A5 replaces it.
- **Lever 1 is dead five times over.** Tree count is the one variable held constant across every arm while the
  latency tripled.
- **The laptop's 865-1335 ms is now explicable without file count:** it too was taken at an unstated
  concurrency, so A3's cross-device "12 is not faster than 56" was probably comparing load states. **The
  cross-device comparison should not be leaned on at all now that a single-device before/after exists.**

### WHAT IS STILL NOT HELD

**Cache warmth** -- the pause arm ran after hours of quiet, this one minutes after resume. **Time of day** is now
largely controlled: both arms are the same device within about half an hour, which the cross-device comparison
never achieved. **What no arm has is a load arm with the SAME cache state as the pause arm**, and I am not
claiming past that.

**The remedy this points at is NOT a repo change.** It is concurrency: fewer seats committing simultaneously, or
staggering the gate-heavy acts. That is a scheduling decision and Andrew's, not a device fix -- **and it is the
opposite of what lever 1 proposed.**

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
