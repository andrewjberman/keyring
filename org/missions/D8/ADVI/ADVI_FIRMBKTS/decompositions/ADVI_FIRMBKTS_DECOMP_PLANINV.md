# ADVI_FIRMBKTS -- DECOMPOSITION (L5) -- WORKSTREAM PLANINV, ROUND 7: THE READ-ONLY INVENTORIES FOR THE FWD-9 MOVE PLAN (PRD v1.5)

```json
{
 "project": "ADVI_FIRMBKTS",
 "directive": "D8",
 "macro": "ADVI",
 "fabric": "dell1",
 "decomp_version": "v7-planinv",
 "step": 5,
 "prd_ref": "org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md (v1.5 @c7a122d445)",
 "order_ref": "1.0.0_SA_CTO~DELL1 msg 5215: cut the FWD-9 read-only inventories now as a separate workstream PLANINV, not as cells added to round 7",
 "author": "2.0.0_SA_COO~B1",
 "round": 7,
 "workstream": "PLANINV",
 "rectangle": "FWD-9(a): per firm (Inflection, Cottonwood), every Advisor Intelligence operating function with its legacy-bucket reads and writes (what runs; what serves and notifies), the Cottonwood crosswalk input with its consumers, and the candidate legacy operations to retire. READ-ONLY; the plan document itself is round 8's.",
 "cells": 5,
 "chains": 5,
 "join_cells": 0,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~B1` (dell1). A workstream is a SCOPE, not a round (CLAUDE.md rule 27): round 7's decomposition (`ADVI_FIRMBKTS_DECOMP_R7.md`) stays frozen; this workstream has a disjoint write
surface (each worker's own deliverables folder), no AWS write and no move.

## Workstream PLANINV -- the cells

| cell | item | serves | owned files | depends on | slot, class | risk | at the cut |
|---|---|---|---|---|---|---|---|
| `FB-k-1` Inflection: what runs (rules, schedules, tasks, S3 events, pipeline scripts) | 1 | FWD-9 | its deliverables folder | -- | ~76 worker | LOCAL | pending |
| `FB-k-2` Inflection: what serves and notifies (Lambdas, edge, IAM grants, SNS/SES, portal readers) | 1 | FWD-9 | its deliverables folder | -- | ~77 worker | LOCAL | pending |
| `FB-k-3` Cottonwood: what runs | 1 | FWD-9 | its deliverables folder | -- | ~78 worker | LOCAL | pending |
| `FB-k-4` Cottonwood: what serves and notifies, and every consumer of the crosswalk | 1 | FWD-9 | its deliverables folder | -- | ~79 worker | LOCAL | pending |
| `FB-k-5` the legacy operations the move makes unnecessary (candidates with evidence and decision owner) | 1 | FWD-9 | its deliverables folder | -- | ~80 worker | LOCAL | pending |
