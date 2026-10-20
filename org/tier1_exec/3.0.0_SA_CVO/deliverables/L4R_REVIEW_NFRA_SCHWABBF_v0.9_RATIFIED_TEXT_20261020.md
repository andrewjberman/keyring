# L4-R review -- NFRA_SCHWABBF PRD v0.9 @3941c46886, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (laptop), 2026-10-20 ~17:0xZ. Delivered by 1.0.0_SA_CTO msgs 109938 and 109939 (both acked). Half hash
`e30544382080`. **Graded:** the diff 998fe82631 -> 3941c46886: one addition to C-TIERS (the master in the silver file name) and the change
log. ENDPOINT unchanged.

## Verdict: SIGN

## The v0.8 ground, read against the code and the bucket

| claim in v0.9 | read by this seat | result |
|---|---|---|
| the silver key is `address('schwab', <firm>, 'silver', <table>, 'date=D')` + `/<master>.parquet`, replacing `data.parquet` | the rule text | four Cottonwood masters write four distinct keys per table and date; the overwrite is gone |
| the builder refuses a two-segment partition | `address('schwab','cottonwood','silver','dim_balance','master=08719286/date=2026-10-16')` | `ValueError: partition must be ... no '/'`; `date=2026-10-16` alone resolves. Matches |
| rows can still be told apart by master inside a firm partition | parquet schema of `schwab/08403355/silver/{dim_balance,dim_position,fact_rps}/date=2024-09-30/data.parquet` | every table carries `_master_observed`; `dim_balance` and `fact_rps` also carry `mstracct_number` |
| (b) and (c) refused | C-TIERS' stated reasons | (b) changes the converters, against "the same full bronze/silver process"; (c) narrows Andrew's "a, yes". Both reasons hold |

## Carried, not grounds (they bind the key-form and cutover cells)

1. **Every silver writer and reader of a firm-form master changes its file name in the same release.** Today the converters write
   `date=D/data.parquet` (`convert_schwab_rps_to_silver.py:185`, `convert_schwab_trn_to_nna_silver.py:207`), and gold readers read that
   name. C-READERS' census should grep `data.parquet` as well as the old bronze grammar, or a missed reader finds no file and reports
   "nothing to do".
2. **A reader that lists a whole firm partition must filter rows on `_master_observed`.** Bronze readers filter on the file-name prefix;
   a silver reader that unions `schwab/cottonwood/silver/<table>/date=D/*.parquet` gets four masters' rows. This is the purpose law in
   `_monolith_bronze.py` carried into silver.
3. **C-EQUAL's before-and-after read** compares 0840 silver at `schwab/08403355/silver/.../data.parquet` (before) with
   `schwab/49financial/silver/.../08403355.parquet` (after); the rebuild must read the new name.

-- 3.0.0_SA_CVO
