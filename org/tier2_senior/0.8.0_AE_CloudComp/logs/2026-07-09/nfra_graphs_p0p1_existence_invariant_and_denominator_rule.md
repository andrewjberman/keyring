# NFRA_GRAPHS P0/P1 -- the mandated router pointed at a command that never existed

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, VALIDATE

**Agent:** 0.8.0_AE_CloudComp
**Date:** 2026-07-09
**Window:** 2026-07-09T18:40Z -> 19:45Z (fresh session; Andrew-direct NFRA-first drive)
**TO:** none -- Andrew-direct: "NFRA_GRAPHS P0/P1 ... explicitly parallelizable; take them wide."

---

## Summary

Ground-truthed all six NFRA_GRAPHS acceptance criteria by running the thing rather than reading the
project JSON (which is stale: `phase` and `current_phase` are entirely D7/D8 narrative from
2026-06-12; D2 and D3 shipped since and the JSON never learned).

Found that **`comp-which` -- the Rule-21 mandated router -- returned `comp-system` RANK-1 for its own
use_case, while `.tools/comp-system` had never existed in this repo's object graph.** Zero objects
named comp-system across all refs, all branches. An agent following the rail got `command not found`.

Shipped the launcher, then closed the class with a 4th hard-blocking completeness member. CTO
approved with no revert and promoted a self-correction I made mid-build into a fabric-wide standing
rule. 4 commits, all on origin/CLOUD.

**The through-line, again, and now at three new layers:** a gate, a claim, or an oracle that binds a
PROXY instead of the PROPERTY.

---

## Work Completed

### 1. `comp-system`: registered, routable, self-routing -- and nonexistent (`83daa2064`)

Registered in ALL THREE routable-substrate registries (tools_index, comp-coverage-map, capability
provider). Passed member-1 (routable) AND member-3 (self-routes). Absent from disk and from git.

    git ls-files --error-unmatch .tools/comp-system   -> not known to git
    git rev-list --all --objects | grep -c 'comp-system$' -> 0    (all refs, all branches)
    git check-ignore -v .tools/comp-system            -> .gitignore:183  (.tools/ ignored wholesale)

The engine (`org/modules/graph/comp_system.py`, `355b9bf53`) landed tracked and self-tests 7/7; only
its launcher was never force-added. It missed the one-time 42->58 universe-convergence sweep of
2026-07-09. Shipped the shim (`git add -f` via safe-commit; 178 other `.tools/` files are force-added
past the same ignore).

Exercised end-to-end, not read: `--self-test` 7/7; `--check` reports STALE vs live HEAD (oracle
working); `--stdout` non-mutating; `command -v` resolves to the path comp-which prints; and the rail
proof -- ask comp-which, RUN what it prints, 7/7 PASS.

### 2. member-4 EXISTENCE invariant + `comp-stitch-refresh` placement (`96c8edd7f`)

Two AC1 orphans, **opposite directions of one property: the registry and the disk must agree.**

- **registered-but-absent** -- comp-system. Members 1+3 prove the router NAMES the tool. Neither
  proves the named command EXISTS. Routable =/=> runnable.
- **present-but-unregistered** -- `comp-stitch-refresh` (`d31bfb597`, 0.7.0_AE_CloudOps) was on disk
  and tracked but UNPLACED in both coverage-map censuses and absent from tools_index.
  `comp-coverage-check` was RED **estate-wide** on it and comp-which could never route to it. Placed
  as `role: graph-producer` (it WRITES the substrate the query tools read -> no surface home),
  characterized FROM THE SOURCE HEADER, not invented. RED -> GREEN.

member-4 asserts a DETERMINISTIC fact (CTO's hard-block bar): a tools_index tool is on disk AND
git-tracked. Both halves matter -- `.gitignore:183` means **present-but-untracked works for the
author and for nobody else, so it passes every check the author runs.** That is the
16-gitignored-tools class, closed at its root rather than by another decaying sweep.

Universe from files being COMMITTED, never `os.listdir` (shared worktree). Diff-bounded; a `.tools/`
touch is unbounded by construction (a delete orphans any registered tool) at 0.66s over 42 tools.
Ramp-exempt. Fail-closed.

### 3. The denominator standing rule (`308e1a00a`)

CTO ruling, effective fabric-wide, promoted verbatim from my own self-catch (see Corrections #1):

> **A gate that cannot state its denominator cannot be trusted to have a numerator.** Every
> hard-blocking gate MUST print, on its standalone surface, the universe it swept on PASS. Silent
> green is indistinguishable from vacuous green. The commit path may stay quiet; the operator
> surface may not.

`comp-manifest-check` already complied as of `96c8edd7f`. `comp-coverage-check` -- **in safe-commit's
hard-blocking chain** -- was the real violator: its PASS made six universal-quantifier claims
("every tool one home, every overlap declared, no phantom seam, inventory complete, projection
current, grain stable") with no N behind any of them. A green over an empty set reads identically.
Now prints homed-tool count, gate_contract rule count, and the inventory `universe`
(working-vs-commit -- the exact distinction whose invisibility produced the 2026-07-09
unplaced-banner churn).

### 4. `comp-system --check` is unsatisfiable by construction (`735a4d86d` + finding)

CTO called the stale `06_current_state` "a chore, not a finding." I went to do the chore. It is a
finding, and the tool is mine.

`check_stale()` returns 0 IFF `emitted.as_of_head == current HEAD`. Landing the artifact requires a
commit, and that commit ADVANCES HEAD. Exercised in order:

    HEAD before              fe02f71e5
    comp-system              wrote 06 with as_of=fe02f71e5
    comp-system --check      "06 CURRENT"   rc=0     <- uncommitted
    safe-commit              [CLOUD 735a4d86d]
    comp-system --check      "06 STALE: emitted as_of=fe02f71e5 vs current HEAD=735a4d86d"  rc=1

**It reports the freshly-regenerated artifact STALE against the very commit that shipped it.** The
only state where it returns 0 is an uncommitted tree; on a shared branch with ~20 committing agents
that window is seconds. Always-RED carries exactly as much information as never-RED. Same
undiscriminating-check class CVO and DS~B hit today, stuck at the opposite rail.

CTO's "chore" call was correct on the evidence available (the oracle said STALE; the artifact WAS
behind HEAD -- both true). What was invisible from outside is that doing the chore cannot clear the
signal.

---

## Corrections I made against myself (all on the record, one caught by a peer)

1. **I nearly shipped a gate that binds nothing, inside the member built to prevent gates that bind
   nothing.** My first legible PASS printed `0 registered tool(s)` -- exposing that member-4 read
   `tools_index` off `load_manifest()`, which returns the `entries[]` dict keyed by id, NOT the raw
   doc. `manifest.get("tools_index")` was None; the gate swept NOTHING and exited 0. **A mute green
   would have shipped it.** The loud-on-pass line I had framed as cosmetic legibility was the only
   thing that could have caught it. CTO promoted this to the standing rule above.
2. **I suspected `comp-manifest-check completeness` was a no-op** because it printed nothing and
   returned 0. It is not: it does **82 seconds** of real work. Timing settled it; I did not argue it.
3. **I flagged `comp-routable-check` as mute-green. It is not** -- it already prints
   `tools_index routing targets: 42`. My `tail -2` truncated the denominator out of its own output
   and I nearly reported the truncation as the defect. Withdrawn before routing. Third time in two
   sessions my *instrument* was the broken thing (os.path.isfile on 217-char paths; the HUD log's own
   format; now a tail). **Pattern banked: when a tool looks mute, check the pipe before the tool.**
4. **I inferred `comp-platinum`'s warm path was uncached** from "warm 7.9s == force 8.0s". Wrong: the
   cache was legitimately past its 300s TTL and rebuilding. Re-measured with a fresh cache: **warm
   3.0s vs --force 8.0s.** AC3 is MET. I re-measured rather than report the artifact -- exactly the
   error I banked yesterday ("inferred a mechanism from a timing number").
5. **My `--help` probe of the flag surface was weak evidence** (parent parser on subcommand tools). I
   disclosed the caveat and offered to withdraw; 0.7.0_AE_CloudOps closed it by exercising the form I
   could not reach. The finding stood on his evidence, not mine.
6. `python comp_system.py --help` is unhandled -- it RAN the compiler and dirtied
   `infra/system/06_current_state.{md,json}`. Restored to HEAD rather than sneak an unrelated change
   into a commit.

---

## Findings raised (routed, none mine to fix)

| finding | status |
|---|---|
| **AC1 NOT MET.** The manifest asserts its own completeness ("every `.tools/comp-*` is in tools_index, in entries, or excluded with a reason"). FALSE: 60 on disk, 49 accounted, **11 orphans**. The CI guard `comp_coverage_view.py --verify` is GREEN because it checks only `tools_index SUBSET-OF ledger` -- one direction. | routed **1.0.0_SA_CTO** (D1 lane) + **2.0.0_SA_COO~B** (CTO routed the reconciliation there) |
| **`tools_index` conflates two concerns** -- the ROUTER'S CANDIDATE SET and the GRAPH USE-CASE CATALOG. `comp-learns-status` is in BOTH tools_index and `excluded_not_graph_use_cases`; it is routable (must stay: dropping it makes it unreachable) AND genuinely not a graph use-case. A schema bug wearing a data bug's clothes. Do NOT "fix" by deleting a line. | routed **CTO**. Recommendation: close AC1 via the coverage-map's declared `supersedes` PROJECTION, not a hand-sweep -- comp-system became registered-but-absent precisely BY MISSING the last sweep. A sweep closes instances; a projection closes the class. |
| **AC2 NOT MET.** `comp-graph status` prints a "uniform" `--fresh`/`--force` contract; `comp-build --fresh` -> rc=2, `comp-build --force` -> rc=2, `comp-aws derive --fresh` -> rc=2. Only comp-platinum implements it. The tool whose job is to remove per-tool trivia asserts trivia that does not exist. | routed **0.7.0_AE_CloudOps** (D3 lane). CONFIRMED by him; population refined 3->2; **handed back to me to build**. Awaiting CTO GO on a 4-state contract. |
| **`comp-system --check` unsatisfiable by construction** (above). Fix = bind fingerprint-or-TTL (graph_cache's existing contract), not `as_of == HEAD`. Folds into the same 4-state ruling. | routed **CTO**. My tool, my defect. |
| **3 invalid escape sequences**: `bd C_05:91` + `cot C_05:92` (separate firms -- TWO commits, never mirror) + `seeking-alpha/edge_scraper_original.py:138` (likely dead code). commit-gate's ruff misses the class: **W605 is not in ruff's default select.** | routed **0.4.0_DS_ClientPlatform**. Did NOT widen the select -- fabric-wide gate change, CTO call, wants a measured blast radius first. |

---

## AC status (every one ground-truthed by running the thing)

| AC | verdict | evidence |
|---|---|---|
| AC1 manifest complete | **NOT MET** | 11 orphans + 1 schema conflation, quantified |
| AC2 contract operative | **NOT MET** | rc=2 on comp-build --fresh/--force, comp-aws derive --fresh |
| AC3 comp-platinum cached | **MET** | warm 3.0s vs --force 8.0s; `gc.cached()` per-firm keys |
| AC4 mandate enforced | **MET** | gate in pre-commit chain; `selfcheck` PASS 3 findings 0 FP; Rule 20 live |
| AC5 cross-layer | P2 | gated on NFRA_GLOBGRPH P2-STITCH; untouched |
| AC6 substrate | -- | grain sentinel = CVO lane; AC5-dangling = AE~B lane; untouched |

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-which | **FAIL -> PASS** | routed RANK-1 to a command that did not exist. The headline defect. Fixed at the tool, not the router. |
| comp-manifest-check completeness/routable | PASS (silent -> loud) | 82s of real work, printed nothing. Now names its universe. |
| comp-manifest-check existence (NEW, member-4) | 9/9 matrix | regression-proven against the real defect; fail-closed; diff-bounded |
| comp-manifest-check selfcheck | PASS | 3 findings, 0 false-positive -- unregressed |
| comp-coverage-check | **RED -> GREEN** | estate-wide RED on comp-stitch-refresh; also the denominator violator |
| comp-routable-check | PASS 42/42 | NOT a mute-green violator (my tail lied) |
| comp-which-routing-test | PASS 42/42 | unregressed post member-4; 20/20 paraphrases; 3/3 posterior |
| comp-coverage_view --verify | PASS (**undiscriminating**) | one-directional; structurally cannot see the 11 orphans |
| comp-platinum | PASS | AC3 verified: warm 3.0s vs force 8.0s |
| comp-graph status | PASS (**doctrine false**) | reports all 9 caches correctly; its freshness CONTRACT line is not implemented |
| comp-system | PASS / **oracle broken** | self-test 7/7; `--check` unsatisfiable once committed |
| commit-gate / safe-commit | PASS | clean on all 4 commits; W605 gap found |

**What worked:** exercising, never reading. Every defect this session came from running the thing --
and the single highest-value moment was making a gate print its denominator, which immediately
convicted the gate I was writing.

**What failed:** four of my own claims (Corrections 2-5), all withdrawn before they reached anyone
except #5, which a peer closed. And `git checkout` lost a race to a concurrent agent's `index.lock`
-- expected in a shared worktree; waited rather than clearing another agent's lock.

**Gap found:** ruff's default select excludes W605, so `commit-gate.sh` is blind to invalid escape
sequences fabric-wide.

---

## MCP Traffic

~8 messages. Significant: CTO's ARCH CALL (member-4 APPROVED, no revert; **loud-on-pass promoted to a
fabric-wide standing rule**; he verified my launcher BY EXERCISE, not by reading my report, and found
the same defect independently at a different layer -- `command -v` vs my git-object-graph check).
0.7.0_AE_CloudOps CONFIRMED AC2, closed my own evidence caveat, refined the population, and handed me
the fix. Findings routed to CTO x3, COO~B x2, DS x1.

CTO's framing, banked: **redundancy across OBSERVERS does not cure a shared layer assumption;
redundancy across LAYERS does.** (Contrast: the SCTY_PREMCP gate where two agents corroborated at the
same layer and both missed the ALB.)

---

## Blockers

**None.** One CTO GO pending (4-state freshness contract) -- an external gate, stated plainly, and I
kept driving past it rather than idling on it. Not started, deliberately:
`NFRA_GRAPHUNI.SFNBRIDGE.trace-graph-sfn-invoke-edges` -- Andrew says COO is reaping that TO
(pending on an already-complete project). It still surfaces in my broker status; asked COO~B to reap.

---

## Current State (handoff surface)

- **origin/CLOUD:** `83daa2064` (comp-system launcher), `96c8edd7f` (member-4 EXISTENCE + placement),
  `308e1a00a` (denominator rule on comp-coverage-check), `735a4d86d` (06_current_state regen).
- **Completeness family is now FOUR members** (`org/modules/graph/manifest_check_cli.py`):
  routable / placement / self-routes / **existence**. All ramp-exempt, fail-closed, commit-universe
  bounded. Standalone surface is loud-on-pass; commit path stays silent.
- **`comp-manifest-check existence`** is a new standalone subcommand (full 42-tool sweep, 0.66s).
- **Estate green:** comp-coverage-check PASS (61 homed tools, 12 rules), comp-manifest-check
  completeness PASS 42/42, comp-which-routing-test PASS 42/42.
- **CTO is closing** NFRA_SYSTEM P3 + NFRA_TOOLCHECK P3 residuals against `83daa2064` + `96c8edd7f`.
  Neither project reopens.
- **NFRA_GRAPHS project JSON is stale** -- `phase`/`current_phase` are D7/D8 narrative from
  2026-06-12, predating D2/D3 shipping. Registry-drift item; I do not edit project JSON.
- **Watcher:** persistent Monitor `bc0flur89`, armed once at load. Zero crons (LD-0157).

---

## Next Steps

1. **[1.0.0_SA_CTO]** GO/NO-GO on the **4-state freshness contract**
   (`default` / `--check` / `--fresh` / `--force`). On GO I wire THREE tools: `comp-build`,
   `comp-aws derive`, and `comp-system` (repoint `--check`'s predicate from `as_of == HEAD` to
   fingerprint-or-TTL). `comp-platinum` is the reference. 0.7.0 re-verifies AC2 by exercise.
2. **[1.0.0_SA_CTO]** taxonomy ruling on `tools_index`: rename it to the router's candidate catalog
   and give the graph use-case catalog its own key, or add the missing cell. `comp-debt` (a library,
   not a CLI -- no launcher, no entry, by design) is the case proving a merge is wrong and a role
   taxonomy is right.
3. **[2.0.0_SA_COO~B]** the AC1 registry reconciliation (42 tools_index vs 60 coverage-map, one
   declaring `supersedes` over the other). Sequencing ask filed. Also: reap the SFNBRIDGE TO.
4. **[0.4.0_DS_ClientPlatform]** two independent C_05 docstring fixes (bd, cot -- never mirrored) +
   confirm whether `edge_scraper_original.py` is reachable before spending a commit on it.
5. **[0.7.0_AE_CloudOps]** verify/refine `comp-stitch-refresh`'s grain+concern on the entry I placed
   from his source header; carry the `derive_stitch` exit-code semantics into it (the wrapper relies
   on them; a future change silently breaks marker-last atomicity).
6. **[me, on CTO GO]** the wiring in (1). Until then: driving, not idling.
