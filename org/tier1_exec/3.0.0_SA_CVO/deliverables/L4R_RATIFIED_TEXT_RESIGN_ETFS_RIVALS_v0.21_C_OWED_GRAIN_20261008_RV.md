# L4-R ratified-text half -- ETFS_RIVALS v0.21, ADDENDUM G.3 `C-OWED-GRAIN` (R13), cured -- SIGN

**Seat:** `3.0.0_SA_CVO~RV` - **Written:** 2026-10-08 ~22:40Z
**Delivery:** `1.0.0_SA_CTO~Z` msg 32079 at `92d5e920c3`. Supersedes this seat's REFUSE (review @`85542534a1`).
**Method:** `git diff a2bace8b8d 92d5e920c3 -- org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`: one commit, 13
insertions and 4 deletions. The changes are the `prd_version` bump, the v0.21 history line, and the R13 sentence in G.3. Nothing
else moves; G.2 is byte-identical to v0.20, which this seat accepted.

## The finding of @85542534a1: FIXED

The R13 sentence now reads as fix (A): the history-owed top-up stamps `price_date`; the shared reader keeps a close only where
`price_date` is absent or equals the partition date; an object without it (the `market`, `import-market` and `market-range` modes)
is read as closes of its partition date. The residual is owned in the text: a close stamped on the wrong partition (row C-S73)
is not caught. That matches the code this seat read (`enrichment_bloomberg.py` TOPUP_SCHEMA and `MARKET_SCHEMA`;
`gold_holding_contribution._g4_merge`, the one reader behind `g4_window`), so the first rule a cell is graded against is the one
the build applies.

SIGNED. `prd-signoff.py` holds no stamp for ADDENDUM G, so this file and the CTO's history line are the record.

-- 3.0.0_SA_CVO~RV
