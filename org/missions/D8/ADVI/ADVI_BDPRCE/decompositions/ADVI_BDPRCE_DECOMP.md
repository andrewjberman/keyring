# ADVI_BDPRCE -- DECOMPOSITION (L5) -- ROUND 1, THE THREAD: ONE UNTICKERED 49F HOLDING TRACED FROM ITS SERVED PRICE TO ITS RULE AND TRADES (PRD v1.0)

```json
{
 "project": "ADVI_BDPRCE",
 "directive": "D8",
 "macro": "ADVI",
 "fabric": "dell1",
 "decomp_version": "v1",
 "step": 5,
 "prd_ref": "org/missions/D8/ADVI/ADVI_BDPRCE/prd/ADVI_BDPRCE_PRD.md (v1.0, both halves signed at @96028a9e53)",
 "order_ref": "1.0.0_SA_CTO~DELL1 msg 4814 and msg 4819 (PRD LANDED)",
 "author": "2.0.0_SA_COO~K1",
 "round": 1,
 "rectangle": "FWD-1 over its hops: the writers of the served price (BP-a-1), the trace instrument (BP-a-2), the served-versus-recomputed gap bounded (BP-a-3), and the thread join (BP-a-4). Read-only against AWS; nothing served moves.",
 "cells": 4,
 "chains": 3,
 "join_cells": 1,
 "ground_truth": "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round1/L5_FACTS.md",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~K1` (dell1). **Inputs:** the PRD's ENDPOINT, CONTRACTS, DECs and cell candidates; the brief PARTS IV and VI; `L5_FACTS.md`.

## Why round 1 holds four cells and not ten

Rule 27 and the spine's L5: round 1 is over the thread's hops, and "only FWD-1 is in scope". The PRD's cell candidates C1, C2, C3, C4, C6, C7, C8 serve FWD-4 to FWD-9; they are
the ENRICHMENT LIST the round-1 analysis cuts, and each is named below with its un-park condition. The three FWD-1 preconditions the PRD names (DEC-8) are the cells here:
the writers of the served price (C5's census half, V.3), the trace instrument (C9), and the 603-of-1,610 gap (V.7). C10 is the thread itself, as the join.

## Round 1 -- the cells

| cell | PRD cell | serves | owned files | depends on | slot, class | risk | at the cut |
|---|---|---|---|---|---|---|---|
| `BP-a-1` the writers of the served T-1 price, named, with the rule copy each applies (read-only) | C5 (census half) | FWD-1, FWD-2 | `deliverables/0.9.0_WK_ADVI_BDPRCE~1/` | -- | ~1 worker | LOCAL | pending |
| `BP-a-2` the trace instrument: any (asset, date) of the served T-1 price to its rule, trade ids and recompute | C9 (instrument half) | FWD-1, FWD-3 | `deliverables/0.9.0_WK_ADVI_BDPRCE~2/` | -- | ~2 worker | LOCAL | pending |
| `BP-a-3` the 603-of-1,610 gap classified and bounded, denominator printed (read-only) | C9 (gap half) | FWD-1, FWD-3 | `deliverables/0.9.0_WK_ADVI_BDPRCE~3/` | -- | ~3 worker | LOCAL | pending |
| `BP-a-4` the thread: ONE 49F account, ONE untickered holding, served price, rule, trade ids, recompute equal (**JOIN**) | C10 | FWD-1 | `deliverables/0.9.0_WK_ADVI_BDPRCE~4/` | `BP-a-1`, `BP-a-2`, `BP-a-3` | ~4 worker | LOCAL | staged |

No two cells write one file: each owns its own worker deliverables directory. The instrument is born under `deliverables/` (the PRD's PATHS row "new ... deliverables, C2, C3, C5, C9, C10"),
not in `data/black_diamond/scripts/`: that keeps the cell LOCAL and moves no deployed path; promoting it to a tools home is an enrichment item.

**Chains** (cells joined by a real data dependency are one chain): `{BP-a-1}`, `{BP-a-2}`, `{BP-a-3}`, and the JOIN `{BP-a-4}`, which consumes the last cell of each.
M = 3 independent chains + 1 join. The edges are data edges: BP-a-4 reads BP-a-1's writer record (to name the writer of the served row), BP-a-2's instrument (to produce
its trace) and BP-a-3's classification (to state the thread row's class).

## Staged cell (parked at the cut)

| order | owner | un-park |
|---|---|---|
| `BP-a-4` | `2.0.0_SA_COO~K1` | `BP-a-1`, `BP-a-2`, `BP-a-3` each merged and PASS at the merged HEAD; the join worker's worktree is cut from that HEAD |

## Not cells of this round (each with its owner and its un-park condition)

| item | PRD cell | owner | un-park |
|---|---|---|---|
| the exact-data switch: Units and Cost Basis on in the qt4 template, the lot table (WORLD, reversible) | C1 | `2.0.0_SA_COO~K1` | the round-1 analysis's enrichment list; it is the longest-latency item (it waits on one scheduled export), so the COO recommends it first |
| the measure: BD units and Schwab ULN against FIFO per capped lot | C2 | `2.0.0_SA_COO~K1` | C1's first export read |
| the reader census of lot `market_value` and `accrued_gain` | C3 | `2.0.0_SA_COO~K1` | the enrichment list |
| unit authority and UNVERIFIED (a served move) | C4 | `2.0.0_SA_COO~K1` under a FWD-7 pair | C2, C3 and Andrew's review of the named diff |
| the one rule's home and every writer importing it | C5 (build half) | `2.0.0_SA_COO~K1` | `BP-a-1`'s writer list |
| S32 distinct median, S33 ties, S34 trade-date keying (served moves) | C6, C7, C8 | `2.0.0_SA_COO~K1` under FWD-7 pairs | the one rule's home exists (C5 build half) and Andrew's review per fix |
| the 603-of-1,610 gap, if BP-a-3 leaves a residue UNEXPLAINED | C9 | `2.0.0_SA_COO~K1` | read at the round-1 drain; the residue is bounded and named, FWD-1 does not wait on it past the thread's own row |

## Fan-out

`fanout: 3 of 3 chains, cap 8, reason: BP-a-1, BP-a-2 and BP-a-3 are disjoint in write set and in data (each reads AWS and the repo, writes only its own deliverables folder); BP-a-4 is the join and is staged, spawning nothing at the cut.`

## Rule 24 record (the one schema this decomposition introduces: the gap classification)

The classes of BP-a-3 are a typed-result set, so the four postulates are stated.
- **MECE over a declared domain.** Domain: the served `transaction_observed` rows over the window (denominator printed). Classes: `EQUAL`, `EXPLAINED_BY_VERSION_AT_WRITE`,
  `EXPLAINED_BY_MULTIDAY_WINDOW`, `EXPLAINED_OTHER` (with a named cause), `UNEXPLAINED`, `NOT_RECOMPUTABLE` (no transaction partition or no valid rows). Every row lands in one class
  (the grader's check is the sum equals the denominator). A row that satisfies two explanations takes the first in the listed order, and the second is a note.
- **Same grain.** One row = one (date, asset_name) served price.
- **Intent coherence.** One axis: how the recompute relates to the served value.
- **State coherence.** `UNEXPLAINED` is not moved by any remedy of this project; it is a bound, stated, and it does not claim a cause.
- **Token census:** the six class tokens are new to this project; the grader enumerates the closed set (`GAP_CLASSES` in `checks/r1_checks.py`) and refuses any other key.

## Lenses read at L5 (each order's preflight carries its disposition)

| lens | disposition |
|---|---|
| `comp-schedule` | every cell DECLARED-NOT-APPLICABLE: thread round; no rule, schedule or cadence is added or changed; the lens runs on the enrichment round that touches a schedule (C1's export, C5's writers) |
| `comp-iam` | every cell DECLARED-NOT-APPLICABLE: reads only (`s3api get-object`, `list-objects-v2`, `list-object-versions`, `head-object`; CloudTrail or CloudWatch reads where the census needs them). No grant is added; a denied read is a finding |
| `comp-adversary` | RUN by the issuer: each grader has a good fixture and ten mutants (`checks/r1_selftest.py`, 14 arms OK); each criterion fails at the base (the record is absent). Blindness: the graders prove shape, read-only discipline and arithmetic, not that a measurement is right; the issuer re-reads the cited objects at the drain |
