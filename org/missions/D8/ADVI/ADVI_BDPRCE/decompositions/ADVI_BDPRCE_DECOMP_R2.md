# ADVI_BDPRCE -- DECOMPOSITION (L5) -- ROUND 2, BUILD THE RULE WITH NO SERVED WRITE (PRD v1.0)

```json
{
 "project": "ADVI_BDPRCE",
 "directive": "D8",
 "macro": "ADVI",
 "fabric": "dell1",
 "decomp_version": "v2",
 "step": 5,
 "prd_ref": "org/missions/D8/ADVI/ADVI_BDPRCE/prd/ADVI_BDPRCE_PRD.md (v1.0, both halves signed @96028a9e53)",
 "order_ref": "1.0.0_SA_CTO~DELL1 msg 5103: org/missions/D8/ADVI/ADVI_BDPRCE/ledger/ROUND_ANALYSIS.round1.md (section 3, items 1-6) and ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md",
 "author": "2.0.0_SA_COO~K1",
 "round": 2,
 "rectangle": "the round-1 analysis's six enrichment items, one cell per item plus the two joins they imply: item 1 split into the rule (BP-b-1) and its replay into the before/after list (BP-b-2); item 2 the census (BP-b-3); item 3 the thread on a truly unlisted holding (BP-b-8, join); item 4 the trace follows the served row (BP-b-4); item 5 the cause of the missing daily files and the lagging objects (BP-b-5); item 6 the exact-lot export change, as code and fixture proof only (BP-b-6). BP-b-7 is the FWD-7 packet Andrew reads (join). No served write; every order reads AWS and the repo and writes only deliverables and two new, unimported repo files.",
 "cells": 8,
 "chains": 5,
 "join_cells": 2,
 "ground_truth": "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round2/L5_FACTS.md",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~K1` (dell1). **Inputs:** the round-1 analysis (CVO slug msg 5102 behind it), the CTO's R1 ruling, `R1_CLOSE.md`, `round2/L5_FACTS.md`.

## Round 2 -- the cells

| cell | item | serves | owned files | depends on | slot, class | risk | at the cut |
|---|---|---|---|---|---|---|---|
| `BP-b-1` THE rule R1 as ONE module, with its tests and a probe over real partitions (no writer imports it) | 1 | FWD-2, FWD-4, FWD-5, FWD-6 | `data/black_diamond/scripts/silver/bd_price_rule.py`, `data/black_diamond/scripts/silver/tests/test_bd_price_rule.py`, `deliverables/0.9.0_WK_ADVI_BDPRCE~5/` | -- | ~5 worker | LOCAL | pending |
| `BP-b-2` R1 replayed over the 1,657 served rows (and the estimated rows) into the named before/after list | 1 | FWD-7 | `deliverables/0.9.0_WK_ADVI_BDPRCE~6/` | `BP-b-1` | ~6 worker | LOCAL | staged |
| `BP-b-3` the W4-S2 census over every client object, and the listed-but-untickered names | 2 | FWD-3, FWD-8 | `deliverables/0.9.0_WK_ADVI_BDPRCE~7/` (extract outside the checkout) | -- | ~7 worker | LOCAL | pending |
| `BP-b-4` the trace instrument reads what the served lot reads (negative arm) | 4 | FWD-3 | `deliverables/0.9.0_WK_ADVI_BDPRCE~8/` | -- | ~8 worker | LOCAL | pending |
| `BP-b-5` the cause of the six missing daily files and the one-day-behind detail objects (no re-run) | 5 | FWD-5 | `deliverables/0.9.0_WK_ADVI_BDPRCE~9/` | -- | ~9 worker | LOCAL | pending |
| `BP-b-6` the lot-level export change as a patch and a byte-unchanged fixture proof (nothing applied) | 6 | FWD-9 | `deliverables/0.9.0_WK_ADVI_BDPRCE~10/` | -- | ~10 worker | LOCAL | pending |
| `BP-b-7` the FWD-7 packet: before/after list, dollar effect on the latest snapshot, the readers it moves (**JOIN**) | 1 | FWD-7 | `deliverables/0.9.0_WK_ADVI_BDPRCE~11/` | `BP-b-2`, `BP-b-3` | ~11 worker | LOCAL | staged |
| `BP-b-8` FWD-1's thread on a truly unlisted holding, traced to R1 and its distinct trades (**JOIN**) | 3 | FWD-1 | `deliverables/0.9.0_WK_ADVI_BDPRCE~12/` | `BP-b-1`, `BP-b-3`, `BP-b-4` | ~12 worker | LOCAL | staged |

No two cells write one file. `BP-b-1` writes the two repo files (new, imported by no writer, so no behavior changes and nothing deploys); every other cell writes its own deliverables folder.
`BP-b-6` edits no `data/` file: it produces a patch and patched copies under its folder, so the PRD's C1 repo and S3 edits stay one WORLD act under a pair.

**Chains:** `{BP-b-1, BP-b-2}` (one worker's queue: ~5 then ~6 is a new worker slot; the edge is data), `{BP-b-3}`, `{BP-b-4}`, `{BP-b-5}`, `{BP-b-6}`, and the JOINS `{BP-b-7}` (consumes BP-b-2 and BP-b-3) and
`{BP-b-8}` (consumes BP-b-1, BP-b-3, BP-b-4). M = 5 independent chains + 2 joins.

## Staged cells (parked at the cut)

| order | owner | un-park |
|---|---|---|
| `BP-b-2` | `2.0.0_SA_COO~K1` | `BP-b-1` merged and PASS at the merged HEAD (the module is in its worktree) |
| `BP-b-7` | `2.0.0_SA_COO~K1` | `BP-b-2` and `BP-b-3` merged and PASS; the census extract's sha256 read equal |
| `BP-b-8` | `2.0.0_SA_COO~K1` | `BP-b-1`, `BP-b-3` and `BP-b-4` merged and PASS |

## Not cells of this round (each with its owner and its un-park condition)

| item | owner | un-park |
|---|---|---|
| **APPLY the exact-lot export change** (Units and Cost Basis on in the S3 and repo qt4 template; the silver patch; the lot table at the builder address; the first export read against Schwab ULN/RLD on a sample) -- WORLD, reversible | `2.0.0_SA_COO~K1`, executed by a dell1 CloudOps lane the CTO names | `BP-b-6` merged and PASS, then the never-widen pair signed by BOTH halves at the current bytes (CTO + COO; the COO half is authored at the un-park from `BP-b-6`'s proof); the order is cut then by amendment (no CloudOps lane is seated to this project at the cut, and one lane holds one project) |
| every writer imports R1, or is retired; the Lambda's rank copy; the S_00 build and inject stage | `2.0.0_SA_COO~K1` under FWD-7 pairs | Andrew's review of `BP-b-7`'s packet, per fix |
| S32 / S33 / S34 as SERVED moves | same | same |
| unit authority and UNVERIFIED (C4), the C2 measure, the C3 reader census | same | the lot table exists (the apply cell) and Andrew's review |
| the fix of the lots priced off no canonical row (W4-S2) | same | `BP-b-3`'s census names them |
| the fix of the missing daily files and lagging objects | same | `BP-b-5`'s cause |

## ARMED rows (7, owner this seat) -- disarm map

Each disarms only by a served move, so none disarms in round 2; the cells below are what bring each within reach, and the served move is its own act under a pair after Andrew's review of the packet.

| row | brought within reach by | disarmed by (round 3+) |
|---|---|---|
| `W2-S2` repeated ids in the median | `BP-b-1` (R1 counts each id once), `BP-b-2` (the moved prices named) | the writers import R1 |
| `W2-S4` two readers of one rule | `BP-b-1` | the writers import R1 |
| `W1-S3` Lambda rank copy lacks `scoped_override` | `BP-b-1` carries SOURCE_RANK with `scoped_override` | the Lambda imports R1 (or is retired) |
| `W3-S3` which rule is THE rule | answered by R1; built by `BP-b-1` | served match on the census |
| `W3-S4` dividend rows set the median to 1.0 | `BP-b-1` (non-trade rows excluded), `BP-b-2` (the 19 and all others named) | the writers import R1 |
| `W4-S2` lots priced off no canonical row | `BP-b-3` (census) | the fix of their source |
| `W4-S8` market value off quantity x price | `BP-b-3` (the census counts the lots), `BP-b-6` (exact units exist) | per-lot UNVERIFIED under FWD-7 |

## Fan-out

`fanout: 5 of 5 chains, cap 8, reason: BP-b-1, BP-b-3, BP-b-4, BP-b-5 and BP-b-6 are disjoint in write set and data; BP-b-2, BP-b-7 and BP-b-8 are staged and spawn nothing at the cut.`

## Rule 24 record (the typed-result sets this decomposition introduces)

| set | classes | domain and denominator | state coherence |
|---|---|---|---|
| replay result (BP-b-2) | `UNCHANGED`, `CHANGED`, `NOW_CARRY_FORWARD`, `NOT_RECOMPUTABLE` | one served (date, asset) price; denominator `served_rows`, printed | `NOW_CARRY_FORWARD` is not "changed": it names that R1 has no trade that date and shows the last observed price with its date; no remedy of this round moves any of the four |
| census lot class (BP-b-3) | `PRICED_FROM_CANONICAL`, `PRICED_OFF_NO_CANONICAL`, `NOT_UNTICKERED` | one open lot of one client object; denominator `lots_total` | an untickered lot is exactly one of the first two; `NOT_UNTICKERED` lots are counted so the denominator is every lot |
| date cause (BP-b-5) | `NO_RUN`, `RUN_FAILED`, `RUN_SKIPPED_BY_SCHEDULE`, `WROTE_ELSEWHERE`, `NOT_DETERMINED` | one of the six missing daily-file dates; denominator printed | `NOT_DETERMINED` names what could not be read; no class is guessed |

Same grain within each set (one row per element), one intent (how the recomputed or served value relates to its input), and each grader enumerates its closed set and refuses another key (`checks/r2_checks.py`, 33 self-test arms).

## Lenses read at L5 (each order's preflight carries its disposition)

| lens | disposition |
|---|---|
| `comp-schedule` | every cell DECLARED-NOT-APPLICABLE: no rule, schedule or cadence is added or changed; BP-b-5 READS the producers' schedules; the lens runs on the apply cell |
| `comp-iam` | every cell DECLARED-NOT-APPLICABLE: reads only (`s3api get-object`/`list-objects-v2`/`list-object-versions`/`head-object`; `logs`, `events`, `lambda get-*`/`list-*`). No grant is added; a denied read is a finding |
| `comp-adversary` | RUN by the issuer: each grader has a good fixture and mutants (`checks/r2_selftest.py`, 33 arms OK); each criterion fails at the base. Blindness: the graders prove shape and arithmetic, not that a measurement is right; the issuer re-reads cited objects at the drain |
