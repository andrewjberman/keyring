# DATA_ANALYTICS -- the UNIVERSAL SILVER CONTRACT (v1, Andrew-ratified 2026-06-25)

The Schwab-raw-native canonical layer. Bronze = raw Schwab files (untouched). **Silver = the
clean faithful layer.** Gold = joins + analytics + reduction. This doc is the silver invariant
every silver table (fact OR dim) honors, and the fact-vs-dim distinction.

## The universal silver baseline (EVERY silver table, fact or dim)

1. **Type-checked** -- declared dtypes; ids honor their declared dtype (custodian account_id =
   zero-padded STRING, leading zeros significant -- NEVER Int64; `coerce_padded_ids` asserts it).
2. **Consistent** -- canonical naming; UTF-8 / ASCII keys; standardized null representation;
   consistent units/date formats. (Subsumes encoding + null-rep + naming.)
3. **Deduplicated** -- no duplicate rows.
4. **Asserted primary key (the grain contract)** -- the table DECLARES its grain and FAILS LOUD
   if the key is not unique. Dedup is the action; the asserted key is the guarantee that makes
   joins safe. Surrogate key only where no natural key exists (txn_uid, lot_uid, position_seq).
5. **Provenanced (+ source_as_of)** -- every row carries `_source_file` + `_ingested_at`
   (lineage) AND `source_as_of` (the data's effective vintage). This is how downstream labels
   staleness HONESTLY -- the guard against the COTETL "served-stale-as-fresh" class + the surface
   for the custodian-latency we otherwise can't see.
6. **Idempotent + deterministic** -- re-running a partition yields byte-identical output
   (deterministic sort before dedup; stable surrogate keys -- the ADHC_GLDINC lesson). PRECONDITION
   for the 30-day reprocess window to be safe: a re-run inside the hot window must never churn keys.
7. **Non-reductive + judgment-free (PROHIBITION)** -- silver preserves ALL source fields and applies
   NO business logic: no field-dropping, no row-filtering, no fillna/dropna-with-meaning, no
   relevance/derivation judgment. Anything needing judgment is GOLD. (= silver Rule 17. The
   prohibition most easily violated -- the dropped-fees incident is the proof.)
8. **Schema-versioned** -- `schema_version`; schema evolution is ADDITIVE-only (a new field never
   breaks a consumer).

## The two modes on top of the baseline

- **FACT = baseline applied NON-REDUCTIVELY** -- the full typed/keyed/provenanced **1:1 mirror of a
  raw Schwab file**, EVERY column kept. (RPS -> fact_position: all ~60 cols. TRN -> fact_transaction:
  all ~137 cols incl every fee. ULN/RLD/TCF likewise.) Reduction is FORBIDDEN here.
- **DIM = baseline applied as a STRATEGIC JOIN-KEY FUNCTION** -- the SAME clean/typed/keyed/
  provenanced contract, deliberately narrowed to the join key + the slice-by attributes. The
  reduction IS the dim's job. (dim_account, dim_relationship, dim_asset, dim_fee.)
  A dim is not a different kind of clean -- it's the silver baseline purposefully reduced to a join surface.

**Rule of thumb:** if you'd `SUM()` it -> fact; if you'd `GROUP BY` it -> dim. An entity that has
both (account, asset, fee) gets a DIM for its identity + a FACT for its measures over time
(dim_account / fact_position ; dim_asset / fact_asset ; dim_fee / fact_billing).

## Where reduction lives = GOLD
The portal-field-tight column selection, joins, analytics, and DERIVED facts happen at gold
(canonical_holdings, account_gains, fact_asset, the C/D analytics). Silver never reduces; gold does.

## Layer map (current)
- **Silver facts (non-reductive mirrors):** fact_position<-RPS, fact_transaction<-TRN,
  fact_lot_unrealized<-ULN, fact_lot_realized<-RLD, fact_billing<-TCF.
- **Dims (lean join-surfaces):** dim_account, dim_relationship, dim_asset<-SEC, dim_fee(<-firm feed).
- **Gold (reduction + analytics + derived facts):** canonical_holdings, account_gains, fact_asset, C/D.

## Build implication (the rework)
The fact builders read the RAW Schwab file and keep ALL columns (typed + deduped + keyed +
provenanced), NOT the existing reductive `opal-data-bd/schwab/silver/*` (which is a lossy prior
conversion the non-reductive facts supersede). Author: 0.4.0_DS_ClientPlatform, 2026-06-25.
