# ADVI_FIRMBKTS -- DECOMPOSITION (L5) -- ROUND 8, THE FWD-9 MOVE PLAN, ONE REAL RETIREMENT AND THE FIRST MOVED TRIGGER (PRD v1.5)

```json
{
 "project": "ADVI_FIRMBKTS",
 "directive": "D8",
 "macro": "ADVI",
 "fabric": "dell1",
 "decomp_version": "v8",
 "step": 5,
 "prd_ref": "org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md (v1.5 @c7a122d445)",
 "order_ref": "1.0.0_SA_CTO~DELL1 msg 5482: org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round7.md (section 3) @8d8c1ec7c8",
 "author": "2.0.0_SA_COO~B1",
 "round": 8,
 "rectangle": "the round-7 analysis's enrichment list: item 1, the FWD-9(a) move plan per firm (Inflection, Cottonwood) from the round-7 inventories and live reads, carrying inf-portal-publisher, inf-silver-aggregator, exec-summary-trigger and the Cottonwood forks; item 2, FWD-9(b) one real retirement by recorded decision, the first legacy operation with no live consumer, never the Door 6 marker before the publisher moves; item 3, FWD-5 the first trigger moved in the plan's order, exercised and read. Item 4 is conditions carried (D1-W75-S2, D1-S50/D1-S53, D1-W70-S1: all six slots stay OFF), not cells.",
 "cells": 5,
 "chains": 3,
 "join_cells": 0,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~B1` (dell1). **Inputs:** `ledger/ROUND_ANALYSIS.round7.md` section 3, `ledger/ROUND8_PLAN_INPUTS_20261013.md`, the PLANINV records (`deliverables/0.9.0_WK_ADVI_FIRMBKTS~76` to `~80`).

## Round 8 -- the cells

| cell | item | serves | owned files | depends on | slot, class | risk | at the cut |
|---|---|---|---|---|---|---|---|
| `FB-l-1` the move plan, Inflection (publisher, silver aggregator, exec-summary-trigger under Terraform, Door 6 after the publisher, grants and environment read live) | 1 | FWD-9 | its deliverables folder | -- | ~81 worker | LOCAL | pending |
| `FB-l-2` the move plan, Cottonwood (the two homes, the crosswalk consumers, SRC_BUCKET, the router_iam comment) | 1 | FWD-9 | its deliverables folder | -- | ~82 worker | LOCAL | pending |
| `FB-l-3` the consumer census of every retirement candidate; the first with no live consumer | 2 | FWD-9 | its deliverables folder | -- | ~83 worker | LOCAL | pending |
| `FB-l-4` the one real retirement, by recorded decision, under a pair | 2 | FWD-9 | `deliverables/0.7.0_AE_CloudOps~FB1/RETIRE_RECORD.json` | `FB-l-3`, the CTO's decision record, the pair | `0.7.0_AE_CloudOps~FB1` seat order | WORLD | staged |
| `FB-l-5` the first moved trigger, exercised and read | 3 | FWD-5 | `deliverables/0.7.0_AE_CloudOps~FB1/MOVE_RECORD.json` | `FB-l-1` or `FB-l-2` (the plan's first move), the CTO's read of the plan, the pair | `0.7.0_AE_CloudOps~FB1` seat order | WORLD | staged |

Chains: {`FB-l-1`, `FB-l-5`}, {`FB-l-2`}, {`FB-l-3`, `FB-l-4`}. The three read-only cells have disjoint write surfaces (each worker's own deliverables folder). The ONE plan document the PRD
names is the index `ledger/FWD9_MOVE_PLAN.md`, written by the issuer at the merge from the two per-firm plans (a hookup that belongs to no cell). Conditions carried, not cells (all `2.0.0_SA_COO~B1`,
all before any position slot is switched on): D1-W75-S2, D1-S50/D1-S53, D1-W70-S1.
