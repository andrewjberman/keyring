# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-05 05Z-08Z (ETFS_RIVALS, FULL)

Row: project | limb | round | TOs | cells | thread | act.

## 05Z
| ETFS_RIVALS | issuer act D12 Step A | 8 | 11/11 built | 11/11 | y | DRIVE FORWARD: backfill trace -- the S3 event rule consumes ANY fetch-bloomberg marker within seconds, so a bare CLI backfill widens served output (plan @59ce8c3bc0); Step A local pull IDVZ/PFOE 01-02..10-02: 189/189 OK, 12,820 rows, nothing on S3 (b2a21b3411) |
## 06Z
| ETFS_RIVALS | issuer act D13 Step A -> lg-1 re-opened | 8 | lg-1 amend 2 | 11/11 | y | RULE: real-Terminal defects in lg-1 found by the D13 local pull: Range.Value com_error escaping as a traceback (rows Z-S21 476b309960, Z-S22 3d876c5c05) -> amendment 2 (Value2 + serial-date conversion + per-unit partial) bb1f305983, built 5bb37fb4e0 |
## 07Z
| ETFS_RIVALS | lg-1 amend 3 + BQL capacity | 8 | lg-1 built c239ad01bb | 11/11 | y | RULE + ESCALATE: per-query column order (row Z-S23) -> amendment 3 (merge by column name) 3dd14c9feb, built; the D13 re-run hit "Daily Capacity, request is blocked" -- the overnight pulls (~170k rows) exhausted the Terminal BQL capacity; row Z-S24 (070d0bae23); CTO~Z ruled @b5167de528 (exposure: rivalfunds leg + constituents A4; 07:00 ET runs; hourly one-query probe; no backfill until production reads OK); MSTR~Z re-runs A4 on the probe's first OK |

## Compiler Tools
- bloomberg_health: ok throughout -- it does not see BQL capacity (the block arrived with health ok).
- lib.opal_naming address(): accepted security_universe.
