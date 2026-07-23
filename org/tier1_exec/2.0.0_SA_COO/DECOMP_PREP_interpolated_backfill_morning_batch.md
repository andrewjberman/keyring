# DECOMPOSITION PREP — Global interpolated-backfill program (morning batch)

**Status:** CVO CLEARED to decompose @816d48cc9 (2026-07-23 ~02:56Z). COO decomposes in the MORNING batch.
**This note preserves the exact binding items so a fresh-morning decomposition inherits them precisely.**

## The pinned pair (R-5 — bind these EXACT commits in every TO)
- **CTO aggregation spec v0.3 @`be91775dd`** — the aggregation design. ⚠ its §4 schema block is
  **RULING-RECORD-NOT-BUILD-SURFACE**; do NOT copy it into a TO.
- **CRO interpolation delta @`708661904`** — **THE CANONICAL BUILD SCHEMA.** Point every DS/DE TO here as
  the schema source of truth. Delta-wins-on-disagreement; a disagreement is an R-5 review item.
- **R-5 STANDING:** CVO's signature is on the pinned pair ONLY. If either spec changes after
  decomposition, it re-enters review as its own delta BEFORE it binds a TO. The pin does not roll forward
  silently. Cite the exact pins in each TO.

## Contract acceptance (structural checks — NOT nice-to-haves)
- **DE:** ONE FE paired-read accessor returning value+provenance TOGETHER + a test that **FAILS on any
  direct read of a value array** (guard-1 "no unlabeled read" at the served boundary, interim before the
  F1 tuple reshape).
- **DS:** additive `point_class[]` array in the served slice (non-breaking) + the **two-lock absence
  validator**: floor = `max(model_creation, account_first_existence)`, producer AND validator BOTH refuse
  below it, **machine-checked + EXERCISED in acceptance, not prose.**

## Andrew labeling bindings (Directive 2, ride into every TO)
- Interpolation conspicuously marked ("Interpolated" + yellow dashed line over the affected period),
  visually distinct, NEVER overlaid as exact/real.
- NEVER written to bronze/silver as if measured — served-layer overlay only.
- Approximate by design ("doesn't need to be exact") — the reconciliation with the MEASURED fingerprint-ban
  (cosine 0.62-0.98, past strategy not recoverable from holdings alone).
- Mechanism intent: current-day accounts, track inflows, work backwards; overlay via fuzzy match — bounded
  below by the two-lock floor.

## Lanes (draft — finalize at decomposition)
- **DS:** producer emits the interpolated series + `point_class[]` + the two-lock absence validator; the
  aggregation per @be91775dd; schema per @708661904.
- **DE:** the paired-read accessor + the "Interpolated"/yellow-dashed-line render + the failing-on-direct-
  read test.
- **CRO:** advisory (owns the interpolation design); **CVO:** re-review on any spec delta.

**Delete once decomposed into committed TOs.**

-- `2.0.0_SA_COO`, ~02:57Z
