# ADVI_FIRMBKTS -- DECOMPOSITION (L5) -- ROUND 1, THE THREAD (PRD v1.3)

```json
{
 "project": "ADVI_FIRMBKTS",
 "directive": "D8",
 "macro": "ADVI",
 "fabric": "dell1",
 "decomp_version": "v1",
 "step": 5,
 "prd_ref": "org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md@30d612d5e5 (v1.3, ADMITTED: ratified-text SIGNED 3.0.0_SA_CVO, brief SIGNED 4.0.0_SA_CRO @2bcb0a340b; prd-signoff status read 2026-10-09 ~20:0xZ)",
 "order_ref": "1.0.0_SA_CTO~DELL1 msg 3113 (seated @c27536ee0d: FWD-1 is the thread; cut the router repoint early); placement 8afcb0f851",
 "author": "2.0.0_SA_COO~F1",
 "round": 1,
 "rectangle": "THE THREAD (FWD-1): the key census (FB-t-1), the mapping table and its reading list (FB-t-2), two readers who never worked together (FB-t-3, FB-t-4); the comparison of their answers is the issuer's real run at close",
 "cells": 4,
 "chains": 2,
 "join_cells": 0,
 "ground_truth": "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~F1/round1/L5_FACTS.md (read-only measurement 2026-10-09 ~20:0xZ-20:3xZ)",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~F1` (dell1), seated by `1.0.0_SA_CTO~DELL1` msg 3113. **Input:**
- PRD v1.3 (ENDPOINT, CONTRACTS, DEC-1..17, CELL CANDIDATES F1-F13, PATHS, SURFACE MANIFEST);
- the L5 fact sheet;
- the CTO's seating message (msg 3113).

## Round 1 -- THE THREAD (FWD-1)

FWD-1's journey has four hops:
1. Every legacy key is known by class, with a denominator from the live plane.
2. Each class is placed by one table, and its new location is built by `address()`, never typed.
3. A list of locations, new and legacy interleaved, carries nothing but the location strings.
4. Two readers who never worked together say, for every location, which system made it, whose it is, how finished it
   is and what it holds; their answers are compared.

Hop 4's comparison is the issuer's real run at close: per arm (canonical vs legacy), the share of locations where both
readers name the same system, the same firm and the same tier. The legacy arm is FWD-1's "today" clause kept as the
negative arm (Rule 27 L2: the organic case is the negative arm).

| cell | hop | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|---|
| `FB-t-1` the key census (LOCAL) | 1 | FWD-1 (and FWD-2's population) | F1, keys only | `deliverables/census.json`, `deliverables/CENSUS.md` | -- | ~1 (worker) |
| `FB-t-2` the mapping table and the reading list (LOCAL) | 2, 3 | FWD-1 (and FWD-2's first placement) | F2 | `deliverables/mapping.json`, `deliverables/MAPPING_TABLE.md`, `deliverables/reading_list.json` | `FB-t-1` | ~1 (worker) |
| `FB-t-3` reader A (LOCAL) | 4 | FWD-1 | F3 | `deliverables/READING_A.json` | `FB-t-2` | ~2 (worker-light) |
| `FB-t-4` reader B (LOCAL) | 4 | FWD-1 | F3 | `deliverables/READING_B.json` | `FB-t-2` | ~3 (worker-light) |

`deliverables/` is `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/` (PRD PATHS). No two cells write one file.

**Chains** (maximal paths): `FB-t-1 -> FB-t-2 -> FB-t-3` and `FB-t-1 -> FB-t-2 -> FB-t-4`. M = 2.

**Fan-out:** 3 workers for 2 chains, cap 8. FWD-1's ACCEPT needs two readers "who have never worked together", and a
reader who placed the keys would be reading its own table. So the readers take their own slots (~2, ~3) and are
spawned together when `FB-t-2` completes; slot ~1 drains `FB-t-1` then `FB-t-2`. All four orders are cut in one
issuance.

**Close (the one real run):** `checks/r1_agree.py`, written at close, reads `READING_A.json`, `READING_B.json` and the
arm map in `mapping.json`, and prints per-arm agreement on system, firm and tier with denominators. The issuer reads
`contents` pairs by eye and records them. Its artifact goes under `deliverables/2.0.0_SA_COO~F1/round1/`.

## Battery (thread round)

| lens | disposition |
|---|---|
| `comp-schedule` | DECLARED-NOT-APPLICABLE: thread round; no cron, rule, schedule or cadence is added or changed. The lens runs on the enrichment round that touches F10's triggers. |
| `comp-iam` | DECLARED-NOT-APPLICABLE: the thread touches no IAM. Every AWS act is a read (`list_objects_v2`) by the issuing box's existing identity. |
| `comp-adversary` | RUN by the issuer as the checks' controls. `r1_census.py`: 0 of 5 / 0 of 2 at base, 5 of 5 / 2 of 2 on the issuer's reference census. `r1_mapping.py`: 0 of 5 at base, 5 of 5 on a reference table, 3 of 5 with one typed address (negative control). `r1_reading.py`: 0 of 2 at base, 2 of 2 on reference answers. Blindness: the lens sees the checks' own arms and the live listing; it cannot see whether a reader opened a file the face forbids. |

## Rule 24 record for the disposition enum (`MOVE`, `HOME`, `RETIRE`, `DECISION`, `FAULT`)

- **(i) MECE over a declared domain.** Domain: every census class of the three legacy buckets (the live listing, L5_FACTS
  section 1). `MOVE` = to its firm bucket; `HOME` = bronze or silver to `opal-data-assets` (R4); `RETIRE` = no
  destination, removal pending F12's proofs; `DECISION` = the two keys Andrew ruled (FWD-7, FWD-8); `FAULT` = the
  table cannot place it (FWD-2: a fault in the table, never a choice). Subtraction: a class with a destination is
  MOVE or HOME by its bucket; one without is RETIRE, DECISION or FAULT. Nothing is left over.
- **(ii) Same grain:** each value disposes one census class.
- **(iii) Intent coherence:** one axis, where the class's bytes end up.
- **(iv) State coherence:** a `RETIRE` row moves nothing and deletes nothing; deletion stays F12's and Andrew's.
  A `DECISION` row changes neither key.
- Token census (`comp-find '\b(MOVE|HOME|RETIRE|DECISION|FAULT)\b'` over this project's tree and the brief): 20 hits
  in 4 files; the only DEFINITION is the issuer's check. The brief and the PRD use `RETIRE` in the same sense.

## Placement

Every cell executes on dell1 (`fabric: dell1`, placement 8afcb0f851).

## Not in round 1

- **F6, the router repoint (`1.0.0_SA_CTO~DELL1` msg 3113: "cut the router repoint early").** It serves FWD-4, not the
  thread. A rewrite target moved before 49 Financial's served keys exist at their new address would make the page
  404, the same gap LGIC_CANON carded at steps 10 and 16. So F6 is round 2's first cell, cut beside F7's copy of 49
  Financial's served keys, both built on this round's table.
- F4 (adopt and repair, then the grants): its premise has moved. The fence now admits this box's CloudOps user (L5_FACTS
  section 3; row `ADVI_FIRMBKTS-D1-S1`). Its round re-reads whom the fence admits before it cuts.
- F5 (the registry repoint) carries row `ADVI_FIRMBKTS-S11`'s patch for `build_canonical_prices_v2.py`.
- FWD-2's second independent placement (F2's second worker) and F7-F13 follow the PRD's arc.
- The tier-first residue in `opal-data-49financial` (`gold/advi/...`) is outside FWD-2's three-bucket domain; row
  `ADVI_FIRMBKTS-D1-S2`.
