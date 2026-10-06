# ETFS_RIVALS -- DECOMPOSITION, ROUND 11 (ENRICHMENT): a new code version writes a new G5 revision, then the served code-class replay and the ok-1 deploy; the drift-record cause fix

```json
{
 "project": "ETFS_RIVALS",
 "round": 11,
 "prd_ref": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md (v0.17 @43a5542d11; ADMITTED)",
 "prd_version": "v0.17",
 "analysis_ref": "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round10.md@134485f75b (section 4, ENRICHMENT LIST items 1-5)",
 "author": "2.0.0_SA_COO~RV",
 "cells": 2,
 "chains": 2,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "round10_decomposition": "org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.round10.md"
}
```

## Rectangle (the round-10 analysis section 4, 5 items)

| item | cell | chain | risk |
|---|---|---|---|
| 1 `_g5_target`: a new code version writes a new revision, the same version nothing (FIRST) | RIV-gt-1 (base 0997603f5d, pre-ok-1) | ~1 | SERVED |
| 2 the served replay of the 4 code classes (1,323 rows), pair carrying ruling 1 (per-fund relabels/fills, G5 keys recorded, STOP on drift; W6-S2) | issuer act after gt-1, from gt-1's branch code | - | WORLD |
| 3 the ok-1 deploy AFTER the replay; J1 with the NBIS label | issuer act under a pair | - | SERVED |
| 4 the C-S38 drift-record cause fix | RIV-dr-1 (direct act) | ~6 | LOCAL |
| 5 the six 2026-10-06 first-run reads, graded once at the CVO's 13:30Z read; S31's disarm | issuer read | - | - |

Edges: gt-1 -> item 2 -> item 3 (issuer acts). No edge between the two cells; write sets disjoint.

## Cells

### `RIV-gt-1` -- a same-input G5 pass at a new code version writes a new revision (rows Z-W3-S23 / Z-S42; analysis item 1, FIRST)
- Measured 2026-10-05 by RIV-rp-2's worker: `gold_trade_schedule._g5_target` returns the newest existing object whenever it records
  the same held funds, so a `rebuild_funds` replay at a date whose live G5 already sits at the newest G1 revision reads OK and
  writes nothing (written_new 0, object count unchanged; live 2026-01-02 G5 and G1 both at `20261005T054335Z-8b69497a75c4`).
- Interface: `gold_trade_schedule.GOLD_VERSION` (a module string). Every G5 object the stage writes carries it in its parquet schema
  metadata under `producer_version`; `_g5_target` reuses the newest existing object only when it records the same held funds AND the
  same `producer_version` as the running code (an object without the key reads as a different version); otherwise the next
  `-v<NN>` object, never an overwrite. Both arms are the criterion: new version -> a new revision; same version -> nothing.
- **Organic trigger:** the batch chain's G5 step, and the issuer's served replay of the four code classes (round-10 analysis item 2).

### `RIV-dr-1` -- the G5 drift record names the data-arrival class's cause as data arrival (C-S38; analysis ruling 2)
- Measured: `deliverables/0.9.0_WK_ETFS_RIVALS~6/g5_drift.json` `classes[g3_latest_pull_supersession].cause` reads
  {"commit": "4fa3e25f5e", "cell": "RIV-g-4"}, as do its G5_DRIFT.md row and `tools/g5_drift.py` `CLASSES`; its 9,467 rows moved
  under UNCHANGED code because later G3 pulls landed (round-9 ruling 3 keeps their vintage).
- Interface: that `CLASSES` entry carries `"commit": None` and `"cause": "data arrival (later G3 pulls)"`; its record entry's
  `cause` reads {"commit": null, "cell": "RIV-g-4", "what": "data arrival (later G3 pulls)"}; `markdown()` prints that text in the
  cause-commit column for a null commit. The two record files are corrected IN PLACE (JSON edited, MD re-rendered by `markdown()`);
  no re-run, no S3 read, no data moves.
- **Organic trigger:** none (a record).
