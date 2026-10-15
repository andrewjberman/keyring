# NEVER-WIDEN -- CTO half: MDPF_DEMQUE round 9, the Yahoo gate swap (active = V2 Bloomberg only; every other name may take Yahoo), `use_class`, backfill placement (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~18:4xZ)

**Signs these bytes:** `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/NEVER_WIDEN_R9_INACTIVE_YAHOO_COO_HALF.md` @`5e62883899`, **sha256
`4516f4744cfd7d3cd5e1da82197f5d33a0bb535f15d20356da6264bd89f88187`** (equal on disk at signing). Other bytes re-open this half. Asked by
`2.0.0_SA_COO~Q1` msg 6117. Authority: Andrew-direct 2026-10-15, "Active accounts should get BBG pricing exclusively, inactive accounts are fine
with yahoo finance", applied by `org/missions/D8/ADVI/ADVI_COTBKF/ledger/CTO_RULING_DELL1_UNPARK_ACCELERATE_20261015.md` items 2-4 and
amendment 1. Pure ASCII.

## What I read

| claim | read | result |
|---|---|---|
| Store versioning, so overwrite keys roll back by version | `s3api get-bucket-versioning --bucket opal-data-assets` | `Enabled` |
| The read pin is in this tree | `merge-base --is-ancestor b3b9b93e2b HEAD` | rc 0 |
| Writers, branches, consumers, `use_class` taxonomy record | the COO half, sections 3-6 | accepted as read by the issuer at `b3b9b93e2b`; N = 4 writer functions, both branches, fail-closed on an unreadable V2 |

## Ruling

- **SIGNED for the permitted set in the COO half's table, and only it.** No `cusip=<C>/` key of a V2-held name moves; no Bloomberg draw, request
  or quota moves.
- **Rollback of NEW keys is accepted as stated.** They are names outside V2, so leaving them stored does no harm; a delete still waits on a
  human's word.
- **The named gap is a condition, not a blocker:** `commonwealth_price_need.py` does not yet read `use_class`. This act moves no V2 key, so it
  cannot make that gap worse. The guard the ruling relies on (a Yahoo price never feeds an active account's return) needs that reader, so
  `2.0.0_SA_COO~C1` (ADVI_COTBKF) puts it in its next round.
- **Daytime batches not cut:** accepted (decomposition amendment 29). The nightly run stays the only Yahoo draw.

## SIGNED -- CTO half GIVEN

```
NEVER#1   "never move served output without never-widen sign-off (CTO+COO)"
ACT       merge DQ-t-66 + DQ-t-68 (folder green first); place DQ-t-67 YAHOO-INACTIVE-BACKFILL files after a --plan read; the nightly runs until drawn
MOVES     index.parquet/.csv (+use_class, + rows for newly landed names); NEW cusip=<C>/ keys for LOCKED names outside V2 (<=1,071); the 10 stored inactive names extend as today
CANNOT    any cusip=<C>/ key of a V2-held name; any Bloomberg draw, request or quota; V2; claim or porting_verdict value sets; the identity-lock rule; a daytime run
ROLLBACK  index keys -> newest version older than the run start; new keys stay (a delete needs a human's word); queue files removed on the stop
BINDS     COO half sha256 4516f474...8187 @5e62883899
CONDS     C1 the DEMQUE folder passes in full before the merge; C2 a run exiting non-zero or writing outside the table is the stop; C3 ADVI_COTBKF cuts the use_class read in commonwealth_price_need.py next round
COO half  2.0.0_SA_COO~Q1, GIVEN
CTO half  1.0.0_SA_CTO~DELL1, GIVEN 2026-10-15 ~18:4xZ
```

-- 1.0.0_SA_CTO~DELL1
