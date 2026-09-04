# NFRA_OUTSET — DECOMPOSITION (L5)

**v0.1** (2026-09-04 ~15:5xZ, `2.0.0_SA_COO`) — the L5 act on PRD v0.1 @`7fb59f239b` (RATIFIED; Andrew's
"all approved" on FWD-1..FWD-8 @`26da5ec0fa` and the L4 notifier frame id 94205). **Input:** the PRD's
17-row surface manifest (s.7), its two ordering rulings (s.8) and its one architectural choice (s.3).
**This document adds the ORDER, the SEATING and the ROUND FENCE. It re-litigates no row and invents no
surface** — the manifest's MECE check was run at L4 and is not re-derived here.

**Home:** `org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md` (lane TREE_COO;
versioned in place). **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.1 @`7fb59f239b`. **Fabric:** laptop.

---

## 0. The cell set — 1:1 with the manifest, no cell invented

**`OS-n` IS manifest row `OS-n`.** 17 rows in, 17 cells out. The `claim`, `evidence`, `lane`, `verb`,
`depends_on` and `accept` columns are the PRD's and are authoritative; this document does not restate
them, so there is ONE carrier and it cannot drift. What follows is what L5 owns: the chain read, the
round fence, and the seating.

**Cell vocabulary (Rule 24, a NOT-EVALUATED value present so non-evaluation is never a verdict):**
`status` = **DONE** (graded) · **IN-FLIGHT** (landed, grade pending) · **OPEN** (not started) ·
**HELD** (blocked on a named decision, owner stated) · **NOT-EVALUATED** (this decomp did not measure it
and says so). **State coherence:** a CVO grade moves `status`; a ruling moves the PRD's `claim`, never
this file. At v0.1 **every cell reads OPEN** — an honest starting state, not a measurement.

⛔ **The `status` column of a decomposition DRIFTS AGAINST ITS ORDERS and nothing links them
mechanically** — measured twice on 2026-09-04, on NFRA_COMPEFFICACY (ten cells reading OPEN against
COMPLETE orders) and on NFRA_CLDGRPH (the same defect, found by the check-out). **The order is the
truth; this column is bumped at a round close and is one round behind between them.**

## 1. THE CHAIN READ — computed from the manifest's `depends_on` edges, not chosen

```
  M (dependency-independent chains) = 3
    chain A  15 cells  OS-1 -> {OS-2, OS-4, OS-5, OS-8, OS-15} -> {OS-3, OS-10, OS-12, OS-16}
                       -> {OS-9, OS-11} -> {OS-13, OS-17} -> OS-14
    chain B   1 cell   OS-6   (CloudOps, audit, no edges)
    chain C   1 cell   OS-7   (CloudOps, audit, no edges)

  longest dependency depth in chain A = 6
```

⛔ **THE BINDING FACT, AND IT IS A CEILING NO WORKER COUNT BEATS: 15 of 17 cells hang off ONE chain
rooted at `OS-1`, six levels deep.** `OS-1` is the Rule T budget fix, and the PRD's own ruling puts it
before everything that prints a denominator. So the project is *structurally* serial for its first
step, and wide only afterwards. **A fan-out chosen against the cell COUNT (17) rather than the chain
COUNT (3) would spawn workers that immediately block**, and each blocked worker is a live worktree, an
open branch and a drain the COO owes.

**M = 3 is therefore the cap on useful workers for round 1, and the real width is 1 until `OS-1` lands.**

## 2. THE ROUND FENCE — where L5 cuts the rounds, and why here

| round | cells | the fence's reason |
|---|---|---|
| **1** | `OS-1` · `OS-6` · `OS-7` | The only three cells with NO unmet dependency. `OS-1` is the PRD's own first ruling; `OS-6`/`OS-7` are the two `unmeasured` audits, and the PRD says plainly they "release `OS-4` and `OS-10`". Round 1 is the whole releasable frontier and nothing is held back. |
| **2** | `OS-2` `OS-4` `OS-5` `OS-8` `OS-15` | Everything that `OS-1` alone releases — the width the project actually has, five parallel cells at depth 2. |
| **3** | `OS-3` `OS-10` `OS-12` `OS-16` | Depth 3. `OS-16` sits here **only if `OS-15` decided BUILD**; if `OS-15` decides RETIRE, `OS-16` is struck by that ruling and the round is three cells. |
| **4** | `OS-9` `OS-11` | Depth 4, both on the seam `OS-10` builds. |
| **5** | `OS-13` `OS-17` | Depth 5. |
| **6** | `OS-14` | Depth 6, the last. |

⛔ **THE FENCE IS A PLAN, NOT A COMMITMENT.** Spine v3 L6 requires ONE issuance covering EVERY cell of
the decomposition; a *round* here is the dependency wave inside that issuance, and a worker holds a
QUEUE it drains in order. **No cell is deferred to "a later round" in the spine's sense** — a later
round exists only when the CTO's round-N analysis sends work back.

## 3. SEATING — and the two cells that are NOT a worker's

**Chain A (15 cells) → worker slots.** The verbs are `fix`, `build`, `wire`, `record` and one `decide`
against a repo surface; the lane is `0.8.0_AE_CloudComp`'s code, which a worker holds under the task
order's `<paths>` grant (RULING 1, Andrew 2026-09-04 ~04:58Z).

⛔ **`OS-6` AND `OS-7` ARE NOT WORKER CELLS, AND THE REASON IS THE LANE, NOT THE TOOL.** A worker has
`Bash`, so it *could* run an AWS read. But the PRD re-homes both to `0.7.0_AE_CloudOps` because each
reads a LIVE CLOUD PLANE — who holds `ecs:RunTask` on the trino task definition and `logs:GetLogEvents`
(`OS-6`), and a glue-bound parquet's refresh cadence and owner (`OS-7`). **A worker subagent is
registered nowhere, holds no cloud identity of its own, and its answer would carry the launching seat's
credentials while reading as the worker's** — an attribution the estate cannot check. These two go to a
`0.7.0_AE_CloudOps` SEAT as ordinary task orders.

⛔ **`OS-17` IS THE CVO's.** Its lane in the manifest is `CVO` and its acceptance is that a day's
proposals each cite the tool row behind them — a certification act. **The spine reserves that to
`3.0.0_SA_CVO`; a worker of the issuing COO inside it is the shape this estate has refused twice
(NFRA_COMPEFFICACY's `CE-pass-1`, and the 2026-09-04 ~07:0xZ fork Andrew ruled "a").**

**So the seating is: 15 → 13 worker cells (chain A minus `OS-17`, which is chain A by dependency but not
by lane) + `OS-17` to `3.0.0_SA_CVO` + `OS-6`/`OS-7` to `0.7.0_AE_CloudOps`.**

## 4. THE FAN-OUT L6 WILL CARRY

```
fanout: 3 of 3 chains, cap 8, reason: 15 of 17 cells hang off ONE chain rooted at OS-1 at depth 6, so
        the useful width is the CHAIN count (3) and not the cell count (17); a fourth worker would
        block on OS-1 immediately and cost a live worktree, an open branch and a drain for nothing.
```

**One slot per chain**: `~1` drains chain A's 13 worker cells in dependency order; `~2` and `~3` take
`OS-6` and `OS-7`. ⚠ **`OS-6`/`OS-7` are SEAT orders, not worker orders** — the fan-out line counts
chains for the record, and the issuance addresses those two to `0.7.0_AE_CloudOps`, not to a
`0.9.0_WK_*` slot.

## 5. THE BATTERY — run at L5, with each instrument's blindness stated

| instrument | result | what it does NOT cover |
|---|---|---|
| the chain read | M=3, depth 6, computed from the manifest's own `depends_on` | it trusts the PRD's edges; a MISSING edge would show as false width, and L5 did not re-derive the dependencies from the surfaces |
| lane read | `OS-6`/`OS-7` CloudOps, `OS-17` CVO, 14 CloudComp — from the manifest's `lane` column | it reads the DECLARED lane, not `.owned-paths.yaml`; the `<paths>` grant is settled per order at L6, not here |
| worker-executability | 13 of 17 cells are a worker's | judged from verb + lane + surface; **not exercised** — the first spawn is the test |
| `comp-schedule` | NOT RUN at L5 | the gate ledger is an L6 preflight per order; running it here would date-stamp a reading L6 must take fresh |

## 6. What this decomposition does NOT decide

- **The `<paths>` block of any order.** That is L6's, per order, and under RULING 1 it IS the worker's
  grant — a surface omitted there is a wall, not an oversight.
- **`OS-15`'s answer.** It is a `decide` cell. L5 fences `OS-16` behind it and takes no position on
  whether the O2–O4 legs are reachable or retired.
- **§3's falsifier.** If a decomposed cell finds the artifact seam cannot be produced on a cadence the
  09:00 window relies on, **that is a SCOPE CHANGE to L2 and not a cell** — the PRD says so and L5
  agrees rather than absorbing it.

— `2.0.0_SA_COO`, L5
