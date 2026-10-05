# ETFS_RIVALS -- DECOMPOSITION, ROUND 10 (ENRICHMENT): the S25 G4 guard first, one key per security, the G5 code-class replay tool, and the IAM grant for round 9's tables

```json
{
 "project": "ETFS_RIVALS",
 "round": 10,
 "prd_ref": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md (v0.17 @43a5542d11; ADMITTED)",
 "prd_version": "v0.17",
 "analysis_ref": "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round9.md@f68eb77491 (section 4, ENRICHMENT LIST items 1-5)",
 "rulings": [
  "CTO~Z msg 29806: rp-2 option A (the 4 non-G3 classes, 1,323 rows, G3-pinned); the IAM grant as a task order to an AE seat with a simulate arm"
 ],
 "author": "2.0.0_SA_COO~RV",
 "cells": 4,
 "chains": 4,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "round9_decomposition": "org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.round9.md"
}
```

## Rectangle (the round-9 analysis section 4, 5 items)

| item | cell | chain | risk |
|---|---|---|---|
| 1 S25: the all-empty or all-error G4 guard (FIRST) | RIV-eg-1 | ~1 | SERVED |
| 2 the code-defect replay over the 4 non-G3 classes (option A) | RIV-rp-2 (the tool + dry census); the served replay is an issuer act under its pair | ~3 | LOCAL |
| 3 citing rows for the 8 stale remediation rows | issuer act, done: rows Z-S32..Z-S39 @63f9c4d4f6 | - | - |
| 4 one key per security (Broadcom, Intuit, Nebius) | RIV-ok-1 | ~2 | SERVED |
| 5 the four first-run reads of the 2026-10-06 vehicle | issuer act (one read; MSTR~Z's P0 records the names stage and the D12 leg) | - | - |
| Z-S31 remainder: the IAM grant for gold/security_names and gold/security_universe | RIV-iam-1 (issued to 0.7.0_AE_CloudOps~RV) | ~RV | WORLD |

Edges: none between cells. Sequencing (record): the served rp-2 replay runs BEFORE ok-1 deploys (ok-1 re-keys positions). Write sets are disjoint.

## Cells

### `RIV-eg-1` -- the G4 enrichment never lands an all-empty or all-error revision (row Z-S25; round-9 ruling 1, FIRST)
- Measured 2026-10-05: the 08:32 ET vehicle's enrichment ran against a no-data Terminal and landed
  `gold/security_market/date=2026-10-02/market-20261005T123318Z-c86a8d9e27fa.parquet` -- 601 rows, px_close / gics_sector /
  security_name all null -- as the NEWEST revision (status OK), shadowing the good 10-04 revision for every reader until a one-key
  restore at 12:46Z.
- Interface: `enrichment_bloomberg` mode `market` refuses to land a revision in which EVERY security is an error or carries none of
  px_close, gics_sector and security_name: nothing is written, the prior revision stays the newest, the result reads status
  "REFUSED" with `detail.reason` naming the count, and the refusal is recorded in the stage's state (a marker carrying status
  REFUSED). A revision with at least one usable security lands as today.
- **Organic trigger:** the vehicle's 07:00 ET enrichment step.

### `RIV-ok-1` -- one key per security (round-9 ruling 7, COO P3)
- Measured on the served 10-05 page: Nebius Group is two securities -- `N97284108` (GQGU reports it by CUSIP only) and
  `NBIS_US_Equity` (WCMG reports the Bloomberg id, the same CUSIP on the row) -- two dialogs, two ranking rows; Broadcom and Intuit
  carry the same class in the page's name map. `gold_holding_contribution._books` keys a row by `security_id`, else by an alias of
  its `raw_identifier`; the alias never joins on the CUSIP / ISIN columns.
- Interface: a row whose key is a CUSIP or ISIN takes the Bloomberg-id key that another row in the same input window carries for that
  same CUSIP / ISIN (`security_cusip` / `security_isin`); a CUSIP with no Bloomberg counterpart keeps its CUSIP key. The same rule
  keys the trade schedule's positions.
- **Organic trigger:** the 07:00 ET marker publish (A1) and the batch chain (G5).

### `RIV-rp-2` -- the G5 code-class replay tool (round-9 ruling 4, re-ruled option A by CTO~Z msg 29806)
- Measured by RIV-gd-1 (deliverables/0.9.0_WK_ETFS_RIVALS~6/g5_drift.json): key_resolution_out_of_confidence 1,040 rows (RIV-h-6),
  full_exit_priced 266 (RIV-x-1), own_prior_pairing 7 (RIV-t-5), implausible_window_refused 10 (RIV-h-5) -- 1,323 rows; the two
  RIV-e-2 classes (20 rows) and the data-arrival class (9,467 rows) keep their vintage.
- Interface: `data/etfs/scripts/rivalfunds/tools/g5_code_replay.py` with `plan` and `dry` (G3 pinned to the live object's recorded
  revisions; `rebuild_funds` per date), writing `deliverables/0.9.0_WK_ETFS_RIVALS~3/g5_replay_dry.json` (classes, dates, rows_moved,
  rows_moved_by_class, rows_moved_outside_classes, columns_moved_outside_classes, g3_label_columns_moved). No S3 write.
- **Organic trigger:** none; the served replay is the issuer's act under its own pair, with this tool.

### `RIV-iam-1` -- the IAM grant for round 9's two tables (row Z-S31; CTO~Z msg 29806)
- Measured 2026-10-05: the D12 Step B refresh republish failed holding_contribution with "etfs-rivalfunds-daily-role ... not
  authorized to perform: s3:ListBucket on opal-data-etfs" (the gold/security_names read); the sweep's security_universe write has no
  grant either; `gen_policies.py` names neither prefix.
- Interface: `gen_policies.py` grants the publish-page stage (so the daily union role) Get + List on `rivalfunds/etfs/gold/security_names/`
  and Put + Get + List on `rivalfunds/etfs/gold/security_universe/`, regenerated, planned (only the two role policies change) and
  applied under its own never-widen pair; nothing else widens.
- **Organic trigger:** the 07:00 ET marker publish and the 09:00 ET sweep (holding_contribution, build-security-universe).
