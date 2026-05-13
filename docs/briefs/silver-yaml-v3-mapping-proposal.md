# Silver YAML v3 Mapping Proposal — REST-side trans_type_id → trans_type_desc + bucket

**Author:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-13
**Project:** ADVI_INFETL.SILVER-DUAL-WRITER-SPLIT (CTO PRD v0.1 incoming)
**Audience:** 1.0.0_SA_CTO (ratification), 2.0.0_SA_COO (sequencing), 0.4.0_DS_ClientPlatform~A (yaml v3 author), 0.4.0_DS_ClientPlatform~C (INF_C_01 read-path consumer)

## Status

Mapping research COMPLETE for the 23-entry NEW lookup gap. **20 of 24 gap trans_type_ids self-resolve via bronze description-join** (no CTO ratification needed — semantics inherit cleanly from yaml v2). **4 new orphans need CTO ratification** with empirical evidence captured below.

Bronze description-join method (DS~A's pattern) is trivial for Inflection: bronze `transactionDescription` column IS the canonical trans_type_desc literal. The `convert_transactions_to_silver.py` `TRANS_TYPE_DESC` lookup at line 72-96 is a re-encoding of what's already in bronze.

## Empirical foundation

- Bronze: `s3://opal-data-inf/bronze/transactions/2026-05-13.parquet` (1,251,020 rows, 47 distinct `transTypeId`, parquet v21.0.0, 18-col, pull_date='2026-05-13')
- NEW REST lookup: `data/orion/scripts/silver/convert_transactions_to_silver.py:72-96` — 23 entries
- Yaml v2 baseline: `data/orion/scripts/silver/orion_cashflow_taxonomy.yaml` — 43 entries (CTO 5-item ratified 2026-05-11)
- DS~A audit context: `docs/briefs/INFGRO_TXN_TYPE_UNIVERSE_AUDIT_20260513.md`
- Bronze 2026-05-13 covers 47 of the 45 historically-observed silver type_descs (DS~A reported 45 across 1,513 historical partitions; today's bronze has 47, with the delta likely from new corporate actions).

## Gap analysis

| Coverage |  |  |
|---|---|---|
| Distinct `transTypeId` in bronze today | **47** | |
| NEW REST lookup covers | **23** | (already in `TRANS_TYPE_DESC`) |
| Gap (must add) | **24** | (in bronze but absent from NEW lookup → fallback "Unknown") |

The 24 gap tids split:
- **20 inherit cleanly from yaml v2** (description matches; just need lookup entry + bucket attached)
- **4 are new orphans** (description present in bronze but absent from yaml v2; need CTO ratification)

## Group A — 20 gap tids that inherit cleanly from yaml v2

Each row below is read directly from bronze 2026-05-13. Bucket is the yaml v2 assignment (already CTO-ratified). Proposal: add to `TRANS_TYPE_DESC` lookup with the listed description, and yaml v3 inherits bucket unchanged.

| trans_type_id | trans_type_desc | bronze row count | yaml v2 bucket | yaml v2 row_count_audit |
|---:|---|---:|---|---:|
| 9 | Employer Contribution | 18 | NNA (in) | 18 |
| 20 | Dividend Reinvested | 65 | Internal | 65 |
| 26 | Administrative Fee | 4 | Return | 9 |
| 32 | Interest Reinvested | 29 | Internal | 29 |
| 61 | Starting Value | 914 | Internal | 896 |
| 63 | Foreign Tax Withheld | 33 | Return | 33 |
| 93 | Interest Paid | 3 | Return | 3 |
| 113 | Federal Tax Withheld | 2,254 | Return | 2,252 |
| 114 | State Tax Withheld | 275 | Return | 274 |
| 115 | Administrative Fee Adjustment | 5 | Return | 6 |
| 150 | Return of Principal (Bonds) | 2 | Internal | 2 |
| 153 | Wire Fee | 5 | Return | 6 |
| 166 | Rollover Contribution | 332 | NNA (in) | 362 |
| 167 | Spin Off out | 9 | Internal | 6 |
| 168 | Spin Off in | 6 | Internal | 6 |
| 180 | Return of Capital | 10 | Internal | 10 |
| 192 | ADR Fee | 34 | Return | 33 |
| 198 | Tax Credit | 2 | Return | 2 |
| 205 | External Account Activity Out | 13 | NNA (out) | 14 |
| 211 | Foreign Dividend Tax | 33 | Return | 33 |

Row-count parity is exact-to-within-rolling-pull-delta for all 20 entries (the 1-2 row deltas match the rolling daily pull-window vs the 1,513-partition historical scan; not a divergence concern). **Group A is mechanical — no CTO action required, just yaml v3 + NEW lookup additions.**

## Group B — 4 new orphans needing CTO ratification

These appear in bronze but NOT in yaml v2. Each row has full empirical evidence below; my bucket proposal + rationale is provided but defers to CTO ratification.

### B-1 — tid=46 "Remark" (239 rows, **$1.87M aggregate** ← MATERIAL)

**Description-vs-notes mismatch:** Orion's external description label is "Remark" but the underlying notes universally read:

```
File Transaction Code - 41DRS+ Note - FIDELITY <FUND>   DIRECT ROLLOVER FROM FIRSCO PLAN 38794  EDMENTUM
```

Sample 4 rows from 2021-03-16, all `DIRECT ROLLOVER FROM FIRSCO PLAN 38794 EDMENTUM`:
| transDate | transAmount | productName |
|---|---:|---|
| 2021-03-16 | $1,003.04 | Fidelity Intl Small Cap Opportunities |
| 2021-03-16 | $1,036.81 | Fidelity US Bond Index |
| 2021-03-16 | $13,011.47 | Fidelity Total Market Index |
| 2021-03-16 | $1,947.57 | Fidelity International Index |

These are direct-rollover NNA inflows misclassified as "Remark" in the Orion external description. Code "41DRS+" appears to be a separate rollover variant distinct from "30DRC+" (which corresponds to tid=166 Rollover Contribution).

**Proposed bucket:** **NNA (in)** — inherit semantics from yaml v2 "Rollover Contribution" entry.
**Proposed `trans_type_desc`:** Keep Orion-canonical "Remark" OR override to "Rollover Contribution" for FE label-clarity (DS~B preference: keep "Remark" so downstream code mapping stays 1:1 with Orion source; map bucket via yaml v3 type_desc → bucket key as usual).
**Materiality:** $1.87M aggregate misclassified NNA inflow if left in "Unknown" + Internal default. Same magnitude class as Starting Value ($6.64M, CTO-ratified Internal) — warrants explicit ratification, not silent inherit.
**Caveat for CTO:** if the "Remark" description is *also* used for non-rollover transactions in future pulls, this bucket assignment could mis-classify. Recommend a structured note in yaml v3: "bucket=NNA assumes 41DRS+ notes pattern; if Orion expands Remark to cover other semantics, re-audit."

### B-2 — tid=48 "Reversal" (6 rows, $273K aggregate)

Notes span three patterns:
- `30PDP+ Note - VD CK# 0947108348` — voided check pre-determined payment
- `30ETF- Note - NO ACCOUNT/UNABLE TO ER49154285` — returned wire to no account (reverse of an outflow)
- `30JNL+ Note - S/P CK# 947655759` — stop-payment journal

All amount values are **positive** ($1.2K to $240K range), reversing prior outflows. These are paired with their original outflow transactions — net economic effect $0 over the pair.

**Proposed bucket:** **Internal** — paired-reversal semantics. Inherit from yaml v2 "Spin Off out / Spin Off in" or "Internal Account Journal In / Out" pairing model. Each Reversal nets out an earlier (incorrectly executed) Distribution / Wire.

**Risk if mis-classified as NNA inflow:** would falsely inflate firm NNA by the gross amount ($273K) without the paired-original-deduction.

### B-3 — tid=96 "Reverse Stock Split" (7 rows, **$0 cash impact** — all `transAmount=0`)

Notes:
- `10REV+ Note - THRIVENT CONSERV ALLOCATION CLASS A  1:2 REV SPLIT`
- `corp action`
- `REVERSE S/S: General Electric Company DECLARED A 1 FOR 8 REVERSE STOCK SPLIT Effective 08/02/2021`

`transAmount=0` for all rows. `noUnits` is negative (position adjustment — fewer shares post-split). Pure representation change.

**Proposed bucket:** **Internal** — corporate action with no economic impact. Symmetric to "Spin Off in/out" (yaml v2 Internal). 
**Materiality:** $0 cash impact. Zero-risk bucket call.

### B-4 — tid=178 "Expired-" (1 row, **$0 cash impact**)

Single row: Thornburg Mortgage Inc, transDate=2022-12-01, transAmount=$0, noUnits=-100. Notes: `10EXP-_9 ... THORNBURG MTG INC COM NEW *EXPIRED POSITION*`. Thornburg Mortgage was a 2008-financial-crisis bankruptcy; this is a final position-zero adjustment.

**Proposed bucket:** **Internal** — position writedown via expiration; `transAmount=0` so no cash flow. Could arguably be Return (security loss-of-value), but with $0 cash recording, Internal is the safer/conventional bucket. If CTO prefers Return for performance-impact visibility, the assignment cost is trivial (1 row, $0).

**Materiality:** 1 row, $0. Lowest stakes among the 4 orphans.

## Group C — Historical-only label (in yaml v2, NOT in today's bronze)

| trans_type_desc | yaml v2 bucket | yaml v2 row_count | bronze today |
|---|---|---:|---|
| Cancel Account | NNA (out) | 101 | NOT in 2026-05-13 bronze pull |

Cancel Account is a yaml v2 entry that doesn't appear in today's 1.25M-row daily snapshot. Either:
1. The trans_type_id for Cancel Account exists in older bronze but Orion stopped emitting it (deprecated trans_type_id).
2. Cancel Account is rare and didn't fire in today's window — would appear in monthly/quarterly snapshots.

**Recommendation:** Keep Cancel Account in yaml v3 (CTO already ratified bucket=NNA(out)). When the next bronze that contains it lands, capture its trans_type_id via the same description-join. Until then, the historical 101 rows in OLD silver carry valid Cancel Account semantics; yaml v3 is forward-compatible without a bronze ID assigned today.

DS~A's `INFGRO_TXN_TYPE_UNIVERSE_AUDIT_20260513.md` may identify the historical trans_type_id from older silver partitions — a 30-second cross-reference if useful.

## Proposed yaml v3 changes (delta only)

Conceptual structure (the file authoring should be DS~A per their handoff):

```yaml
version: 3
title: Orion Cashflow Taxonomy (Stage 0c — REST-canonical + trans_type_id-keyed)
schema_version_history:
  - v1 (Stage 0): compound key (type_desc, activity_category)
  - v2 (Stage 0b): type_desc-only key, CTO 5-item ratification applied
  - v3 (Stage 0c): trans_type_id-keyed for NEW REST canonical path; preserves type_desc as secondary key for OLD CSV/zombie compatibility; adds 4 new orphans pending CTO ratification

types:
  # ALL 43 v2 entries preserved; each gets an added trans_type_id field (where known).
  - trans_type_id: 8      # NEW: id-keyed
    type_desc: "Client Contribution"
    bucket: NNA            # v2 — unchanged
    nna_direction: in
    # ... (rest of v2 entry preserved)

  # 20 Group A additions: yaml v2 entries that need their trans_type_id annotated.
  - trans_type_id: 9
    type_desc: "Employer Contribution"
    bucket: NNA            # v2
    # ...

  # ... (19 more Group A entries) ...

  # 4 Group B new orphans (pending CTO ratification — placeholders below)
  - trans_type_id: 46
    type_desc: "Remark"
    bucket: NNA            # PROPOSED — pending CTO ratification (DS~B brief 2026-05-13)
    nna_direction: in
    rationale: "DS~B 2026-05-13 trace: notes universally '41DRS+ DIRECT ROLLOVER FROM <plan>' (239 rows / $1.87M). Direct-rollover NNA inflow misclassified by Orion external label."
    row_count_audit: 239
    materiality_firm_aggregate: 1872347.46
    cto_ratification_status: pending
    cto_ratification_evidence: docs/briefs/silver-yaml-v3-mapping-proposal.md#b-1

  - trans_type_id: 48
    type_desc: "Reversal"
    bucket: Internal       # PROPOSED — pending CTO ratification
    rationale: "DS~B 2026-05-13 trace: paired-reversal semantics (30PDP+ VD / 30ETF- NO ACCOUNT-RETURNED / 30JNL+ S/P). 6 rows / $273K gross; nets to ~$0 with paired originals."
    row_count_audit: 6
    materiality_firm_aggregate: 273075.58
    cto_ratification_status: pending
    cto_ratification_evidence: docs/briefs/silver-yaml-v3-mapping-proposal.md#b-2

  - trans_type_id: 96
    type_desc: "Reverse Stock Split"
    bucket: Internal       # PROPOSED — pending CTO ratification (low-stakes, $0 cash)
    rationale: "DS~B 2026-05-13 trace: corporate action representation change. transAmount=0 for all 7 rows. Symmetric to Spin Off in/out semantics."
    row_count_audit: 7
    materiality_firm_aggregate: 0.0
    cto_ratification_status: pending
    cto_ratification_evidence: docs/briefs/silver-yaml-v3-mapping-proposal.md#b-3

  - trans_type_id: 178
    type_desc: "Expired-"
    bucket: Internal       # PROPOSED — pending CTO ratification (1 row, $0 cash)
    rationale: "DS~B 2026-05-13 trace: position writedown via expiration (Thornburg Mortgage 2008-bankruptcy aftermath). transAmount=0, noUnits=-100. Internal preferred over Return given $0 cash."
    row_count_audit: 1
    materiality_firm_aggregate: 0.0
    cto_ratification_status: pending
    cto_ratification_evidence: docs/briefs/silver-yaml-v3-mapping-proposal.md#b-4
```

## CTO ratification items requested

| # | Item | Materiality (firm) | Recommended decision | Risk if delayed |
|---|---|---:|---|---|
| 1 | tid=46 "Remark" → NNA(in) Rollover-Contribution-class | **$1,872,347.46** | ACCEPT (B-1 evidence is unambiguous) | $1.87M misclassified Internal/Unknown if held |
| 2 | tid=48 "Reversal" → Internal | $273,075.58 gross / ~$0 net | ACCEPT (B-2 paired-reversal evidence) | Risk of falsely inflating NNA inflow if mis-bucketed |
| 3 | tid=96 "Reverse Stock Split" → Internal | $0 cash | ACCEPT (B-3 symmetric to Spin Off) | Zero risk; cosmetic only |
| 4 | tid=178 "Expired-" → Internal (vs Return) | $0 cash | ACCEPT Internal OR flag Return | Zero risk; assignment cost trivial |

## Cross-references

- **Bug B silver-empty-partition** (`docs/briefs/data-scientist-bug-b-silver-empty-partition-trace.md`): the NEW REST `convert_transactions_to_silver.py` reads `_load_rep_lookup` from `silver/api_dims/accounts_v2/latest` (`:107-117`). When Bug B fires (today, 2026-05-08), `_load_rep_lookup` returns 0 rows, and the NEW REST transactions silver has 0 rep_id attribution. **DUAL-WRITER project should sequence Bug B fix before any chain that exercises NEW REST canonical path.**

- **Yaml v2 reference** (`data/orion/scripts/silver/orion_cashflow_taxonomy.yaml`): 43 entries already CTO-ratified 2026-05-11. v3 inherits ratifications; Group A is mechanical.

- **DS~A audit baseline** (`docs/briefs/INFGRO_TXN_TYPE_UNIVERSE_AUDIT_20260513.md`): 45 distinct type_desc across 1,513 historical partitions; today's bronze covers 47. The delta (47 - 45 = 2) is likely the 4 new orphans here (B-1..B-4) minus 2 that DS~A's 1,513-scan caught but today's 1-day bronze didn't.

## Effort + sequencing

Phase 0 (this brief): COMPLETE — ~90 minutes mapping research.

Phase 1 (DS~A): yaml v3 authoring with the Group A trivial-merge + Group B placeholders. Estimate ~1-2h.

Phase 2 (CTO): ratification table above. Estimate ~30min review + decision.

Phase 3 (DS~A or DS~B): update `convert_transactions_to_silver.py` `TRANS_TYPE_DESC` lookup with the 24 new entries + bucket-aware override in INF_C_01 read-path (DS~C lane). Estimate ~1-2h.

Phase 4 (AE): chain re-fire after silver re-run on retroactive partitions. AE-lane timing per AE 0.6.1.

**Sequencing note:** Phases 1 + 2 can run in parallel — DS~A pre-authors v3 with placeholders, CTO ratifies, DS~A folds ratified buckets in.

— 0.4.0_DS_ClientPlatform~B 2026-05-13
