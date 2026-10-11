# ADVI_FIRMBKTS -- DECOMPOSITION (L5) -- ROUND 2, THE ENRICHMENT (PRD v1.3)

```json
{
 "project": "ADVI_FIRMBKTS",
 "directive": "D8",
 "macro": "ADVI",
 "fabric": "dell1",
 "decomp_version": "v2",
 "step": 5,
 "prd_ref": "org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md@30d612d5e5 (v1.3, ADMITTED: ratified-text SIGNED 3.0.0_SA_CVO, brief SIGNED 4.0.0_SA_CRO @2bcb0a340b)",
 "order_ref": "1.0.0_SA_CTO~DELL1 msg 3365: org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round1.md @4c9229fee2 + ROUND_ANALYSIS.round1-addendum.md addenda 1-2 @a7ef4d08ab (823f950ade)",
 "author": "2.0.0_SA_COO~B1",
 "round": 2,
 "rectangle": "the enrichment list (items 1-6): two blind readers on the 209 canonical locations (FB-e-2, FB-e-3); the table repair (FB-e-1); F4's arms exercised (FB-e-4); F7's copy of 49 Financial's served platinum keys (FB-e-5); F6's canonical key path built dormant and proved against the table (FB-e-6); the cot price builder's tolerant load (FB-e-7)",
 "cells": 7,
 "chains": 7,
 "join_cells": 0,
 "ground_truth": "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/L5_FACTS.md (read-only measurement 2026-10-11 ~02:3xZ-03:2xZ)",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~B1` (dell1), seated by `1.0.0_SA_CTO~DELL1` msg 3365. **Inputs:**
- PRD v1.3 (ENDPOINT, CONTRACTS, DEC-1..17, CELL CANDIDATES F1-F13);
- the CTO's round-1 analysis and addenda 1-2 (enrichment items 1-6; the ruling that F7 writes only `address()` paths and
  prints the residue count before and after);
- `deliverables/2.0.0_SA_COO~B1/round2/L5_FACTS.md`.

## Round 2 -- the enrichment

| cell | item | serves (cell_refs) | candidate | owned files | depends on | slot, class | risk |
|---|---|---|---|---|---|---|---|
| `FB-e-1` table repair | 2 | FWD-2 | F2 | `deliverables/mapping_v2.json`, `MAPPING_TABLE_v2.md` | -- | ~4 worker | LOCAL |
| `FB-e-2` blind reader A | 1 | FWD-1 | F3 | `org/tier1_exec/2.0.0_SA_COO~B1/round2/blind/ANSWERS_A.json` | -- | ~5 worker-light | LOCAL |
| `FB-e-3` blind reader B | 1 | FWD-1 | F3 | `org/tier1_exec/2.0.0_SA_COO~B1/round2/blind/ANSWERS_B.json` | -- | ~6 worker-light | LOCAL |
| `FB-e-4` F4's arms | 3 | FWD-4, FWD-6 | F4 | `deliverables/0.9.0_WK_ADVI_FIRMBKTS~7/` | -- | ~7 worker | LOCAL |
| `FB-e-5` F7 copy | 4 | FWD-4 | F7 | `deliverables/0.9.0_WK_ADVI_FIRMBKTS~8/`; the destination keys | -- (pair) | ~8 worker | WORLD |
| `FB-e-6` F6 canonical key path, dormant | 5 | FWD-4, FWD-3 | F6 | `infra/aws/lambda-edge/shared-advisor-router/` | -- | ~9 worker | WORLD (infra floor) |
| `FB-e-7` tolerant load | 6 | FWD-2 (row S11) | F5 (the S11 carrier) | `data/cot/scripts/gold/build_canonical_prices_v2.py`, one new test | -- | ~10 worker-light | LOCAL, direct act |

No two cells write one file. The only shared read is `mapping.json`/`census.json` (round 1, never edited).

**Chains** (maximal paths): seven, one per cell. M = 7.

**Fan-out:** 7 workers for 7 chains, cap 8. FWD-1's clause needs two readers who have never worked together, so the
readers take their own slots. `FB-e-5` is staged until its never-widen pair carries both halves; it is spawned the turn
the CTO's half lands. `FB-e-4`'s negative arm is one SSM command under a bound the face carries.

## Not in round 2 (ruled here, each with its owner and its un-park condition)

| item | ruling | owner, un-park |
|---|---|---|
| F6's DEPLOY (the CTO's "the round's last act") | NOT CUT. The producers rewrite `opal-data-bd` platinum daily; a router flip before they write the new bucket serves a stale copy, and dual write is DEC-17's NEVER. Row `ADVI_FIRMBKTS-D1-S4`. | `1.0.0_SA_CTO~DELL1`: place F10's platinum-producer repoint (or a resync-in-window) before the deploy; a no-behavior-change release of the dormant path may go first. |
| the actual 49 Financial cutover (a map value edit) | NOT this round: it needs the `advTenant` remedy first (`firm-config.mjs` header) and the producers repointed. | CTO, with F10. |
| S_00 SSM step (item 6's optional half) | DROPPED, reason in L5_FACTS section 7 ruling 2. | none; re-openable if a consumer is named. |
| "the literal rename" (item 6's first half) | ALREADY DONE by ADVI_COTBKF (CB-ap-1, CB-at-1, CB-ax-1 @19b3550e8a). | none. |
| F5, F8-F13 | per the PRD's arc | later rounds |

## Battery

| lens | disposition |
|---|---|
| `comp-schedule` | DECLARED-NOT-APPLICABLE for every cell: no cron, rule, schedule or cadence is added or changed (S_00, the one that would, is dropped). |
| `comp-iam` | RUN by the issuer's reading at L5: `FB-e-5` needs `s3:PutObject` on `opal-data-49financial` and `GetObject` on `opal-data-bd`; `simulate-principal-policy` on the caller's own ARN reads `allowed` for both (L5_FACTS section 3). `FB-e-4` needs `ssm:SendCommand`, INFERRED not measured (the simulator is refused for any role); the face makes a refusal a BLOCKING row. Every other cell: no IAM change. |
| `comp-adversary` | RUN by the issuer as the checks' controls (L5_FACTS section 6): each check run at base, on a reference, and against at least one mutant. Blindness: the lens cannot see whether a reader opened a file its face forbids (the sparse worktree withholds the project folder; the report's `OPENED:` line is the only witness), and cannot see the producers' next write window. |

## Rule 24 record

The only new enumerated value is the FAULT row's `fault_owner` (a serial) and the `collisions[].verdict` (`merge` only:
a collision with overlap above 0 is two FAULT rows, never a verdict). (i) MECE: every census class is placed once, or
re-gridded into children that sum to it. (ii) grain: one row per class. (iii) one axis: where the class's bytes end up.
(iv) state coherence: RETIRE moves and deletes nothing; FAULT changes nothing. No new disposition value is added.

## Placement

Every cell executes on dell1 (`fabric: dell1`).
