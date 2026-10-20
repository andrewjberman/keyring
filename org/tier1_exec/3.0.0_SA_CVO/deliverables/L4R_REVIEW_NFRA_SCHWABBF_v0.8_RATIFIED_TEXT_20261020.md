# L4-R review -- NFRA_SCHWABBF PRD v0.8 @998fe82631, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (laptop), 2026-10-20 ~16:5xZ. Asked by 1.0.0_SA_CTO msg 109935 (acked). **Graded:** the diff e8d796975f ->
998fe82631: one CONTRACTS row added, C-TIERS, plus the record line, the closed OPEN AT ANDREW item and the change log. ENDPOINT unchanged.

## Verdict: REFUSE

**Reason (one line):** C-TIERS puts four Cottonwood masters' silver in one `schwab/cottonwood/silver/<table>/date=D/` through "the same
converters", which write one fixed `data.parquet` per date partition, so the masters overwrite one another silently.

## The evidence

- **Silver keys are one object per table per date.** Listed by this seat: `schwab/08403355/silver/dim_balance/date=2024-09-27/data.parquet`,
  `.../date=2024-09-30/data.parquet`, and so on.
- **The writers make that key.** `data/black_diamond/scripts/bronze/convert_schwab_rps_to_silver.py:185`:
  `Key=f'{DST_PREFIX}date={date}/data.parquet'`, and `convert_schwab_trn_to_nna_silver.py:207` is the same. **The readers read that one
  file:** `data/black_diamond/scripts/gold/B_00.canonical_holdings.py:20` reads `schwab/08335338/silver/fact_rps/date={YYYY-MM-DD}/data.parquet`.
- **C-TIERS says:** "Each Cottonwood master writes every tier under `schwab/cottonwood/` from its first day", through "the same converters,
  the same silver tables ... Nothing is converted by a one-off path", "with rows told apart by master as in bronze".
- **Bronze is told apart by the vendor file name's master prefix. Silver has no such name:** its file is always `data.parquet`. Four masters
  converting the same table and date write the same key, and the last writer wins. Nothing errors, and FWD-8's trace for one master would
  still pass.
- **49financial is safe today only by accident:** 0840 is its only firm-form master since v0.7. The first second master there hits the
  same collision.

## What makes it signable (the CTO's choice; one row either way)

- **(a)** The silver key carries the master below the table, for example `.../silver/<table>/date=D/master=<m>/data.parquet` or
  `.../date=D/<m>.parquet`. C-TIERS then names the converter and reader change, and C-READERS' census covers every reader of
  `data.parquet` under a firm-form master.
- **(b)** A firm-level silver write that merges all masters of the firm into the one `data.parquet` per partition, with a master column.
  That is a new write path, so C-TIERS' "the same converters ... nothing converted by a one-off path" would change.
- **(c)** Silver stays per master (`schwab/<master>/silver/`) and only bronze, meta and `_ops` move to firm scope. That narrows Andrew's
  "a, yes", so it would need his word.

## Cleared or confirmed in v0.8

- The 0840 tier counts, listed by this seat (~16:5xZ), total 20,585 objects under `schwab/08403355/`: bronze 6,074, silver 7,581, meta
  6,898 and `_ops` 32. C-MOVE's re-measure at the cut should print about this denominator, not bronze's alone.
- The opal-gateway's 08403355 prefixes in C-READERS' census, coordinated MSTR to MSTR, are right: the gateway is another fabric's reader.

-- 3.0.0_SA_CVO
