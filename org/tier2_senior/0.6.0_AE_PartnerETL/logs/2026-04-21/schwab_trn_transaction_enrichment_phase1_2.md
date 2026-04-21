# Session Log — Schwab TRN Transaction Enrichment Phase 1 + Phase 2

**Agent:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-21
**Continues from:** `schwab_trn_nna_coverage_diagnosis.md` (methodology clarification)
**Brief:** `docs/briefs/ae-schwab-trn-transaction-enrichment-feasibility.md`
**Authorization:** Andrew 2026-04-21 — "priority is the most complete transactions history as possible, so if we can enrich 1st and 2nd order transactions tables, thereby enriching gold, that is what we want to assess feasibility and implementation"

---

## Phase completion

| Phase | Deliverable | Status |
|-------|-------------|--------|
| 1 | `build_schwab_bd_account_xref.py` + daily xref partition | complete |
| 2 | `enrich_transactions_with_schwab.py` + 494 backfilled partitions | complete |
| 2b | `validate_transactions_enriched.py` + validation report CSV | complete |

## Artifacts produced

### Code

| Path | Purpose |
|------|---------|
| `data/black_diamond/scripts/bronze/build_schwab_bd_account_xref.py` | Joins Schwab ACC (latest) + BD silver (90-day lookback) → one-row-per-account xref with architect/relationship attribution + fuzzy last-name fallback for Schwab-only accounts |
| `data/black_diamond/scripts/silver/enrich_transactions_with_schwab.py` | Per-date: reads BD silver/transactions + Schwab TRN_NNA + xref. Dedup: ±2% gross_amount + same-direction + ±180d window. Synthesizes BD-schema-compatible rows for unmatched Schwab events, tags `source_system='schwab_imputed'`. Preserves BD rows byte-intact tagged `source_system='bd'`. |
| `data/schwab/analysis/validate_transactions_enriched.py` | Per-partition invariant check + per-month imputation share + top-5 events audit. Emits `data/schwab/analysis/enriched_validation_report.csv`. |

### S3 artifacts

| Path | Count |
|------|-------|
| `s3://opal-data-schwab/03_silver/account_xref/date=20260421/data.parquet` | 7,114 rows (5,786 bd+schwab + 656 fuzzy + 361 bd_only + 311 schwab_only) |
| `s3://opal-data-bd/silver/transactions_enriched/date={YYYY-MM-DD}/data.parquet` | 494 partitions, 2024-04-12 → 2026-04-20 |

### Results (full backfill)

- BD rows preserved: 1,569,376
- Schwab-imputed rows added: 28,415
- Invariant failures (bd + imputed < plain silver): 0
- Dec 2024 worked example: Jessica Lindsey SHORT TRUST (acct 79128541) $20.1M wire attributed to Travis Penfield via direct acct10 match
- Oct 2025: William Chan (acct 26881039) $41M + $7.4M (charitable trust) — correctly attributed

### Monthly imputation share (% of total inflow)

| Month | Share | Flag |
|-------|------:|------|
| 2024-04 | 5.3% | |
| 2024-05 | 18.4% | |
| 2024-06 | 12.0% | |
| 2024-07 | 12.4% | |
| 2024-08 | 4.1% | |
| 2024-09 | 6.0% | |
| 2024-10 | 14.1% | |
| 2024-11 | 23.9% | |
| **2024-12** | **66.3%** | HIGH — confirmed onboarding batch (Jessica Lindsey, Stoneridge, Petty) |
| 2025-01 | 10.8% | |
| 2025-02 | 6.3% | |
| 2025-03 | 13.2% | |
| 2025-04 | 26.8% | |
| 2025-05 | 5.6% | |
| 2025-06 | 7.0% | |
| 2025-07 | 9.3% | |
| 2025-08 | 6.4% | |
| 2025-09 | 17.1% | |
| **2025-10** | **50.3%** | HIGH — William Chan + charitable trust onboarding |
| 2025-11 | 10.9% | |
| 2025-12 | 31.4% | watch |
| 2026-01 | 9.9% | |
| 2026-02 | 3.9% | |
| 2026-03 | 5.3% | |
| 2026-04 | 8.1% | |

## Findings relayed to CTO

**BD silver schema drift (flagged via MCP):** The `is_nna` / `is_nna_inflow` / `is_nna_outflow` columns were dropped from BD silver/transactions starting 2026-01-27. NNA signal moved to `external_flow` column (values `'Contribution'` | `'Withdrawal'` | NaN). Without the fallback to read `external_flow`, my NNA index only captured 232,678 rows; after the fix it captured 344,011 rows — **111,333 rows** would have been missed and the dedup logic would have emitted ~12-17K false `schwab_imputed` rows for events BD already had, inflating firm NNA.

My enricher and validator now read both signals; but any other consumer of BD silver that reads only `is_nna_*` is silently undercounting NNA on every run touching 2026 data. CTO asked to awareness-flag and investigate upstream ownership.

## Compiler Tools

| Phase | Tool | Applicability |
|-------|------|---------------|
| 1, 2 | N/A | This workstream writes new bronze/silver producers (not Lambda code, not Terraform, not gold scripts, not IAM, not CloudFront). comp-pipescript, comp-iam, comp-routes do not apply to new bronze/silver-layer producers. comp-blast on the new producers would be uninformative (no upstream dependencies in repo). Honest scope call, per role-minimum mandate policy. |

## Current State + Next Steps

**Current state:**
- Phase 1 xref partition live at `03_silver/account_xref/date=20260421/`
- Phase 2 enriched partitions live at `silver/transactions_enriched/` (494 dates)
- Validator output clean: 0 invariant failures; imputation shares line up with our investigation hypotheses (Dec 2024 and Oct 2025 dominated by onboarding-batch imputation)
- CTO notified of BD silver schema drift (MCP 17:03Z)
- DS still standing by for COO-issued TO on canonical_nna merge (as of 15:09Z ACK)

**Next steps:**
1. **[0.6.0_AE_PartnerETL]** Commit xref + enricher + validator + report CSV + this log. Push CLOUD. (this step)
2. **[0.6.0_AE_PartnerETL]** MCP DS: pivot handoff — the brief's Phase 6 (gold canonical_nna merge) is superseded by this silver-layer enrichment. `silver/transactions_enriched/` is ready; C_01 consumer cutover is just a read-path swap. Share schema contract (`source_system` column added, otherwise identical).
3. **[0.6.0_AE_PartnerETL]** MCP CTO: completion report + confirmation that the schema-drift mitigation is in place; decision to proceed on Phase 3 (gold consumer cutover) pending his response on the flag I sent.
4. **[1.0.0_SA_CTO]** Decision on schema-drift investigation ownership: direct someone to audit `data/black_diamond/scripts/gold/**` for readers of `is_nna_*` columns (likely silent undercounting on 2026 data).
5. **[0.4.0_DS_ClientPlatform]** Phase 3 after CTO approval: flip `C_01.canonical_nna.py` read path from `silver/transactions/` to `silver/transactions_enriched/`. Simpler than original brief's Phase 6 gold-merge because the union already happened in silver.
6. **[0.7.0_AE_CloudOps]** Future follow-on TO: daily schedule for xref + enricher (EventBridge trigger after BD silver refresh). Out of scope for this session.

## Incidents / Lessons

1. **Schema drift is a silent consumer killer.** BD allocation processor dropped NNA flag columns mid-pipeline without downstream notification. My enricher caught it only because pytest-style unit verification of the Dec 2024 Jessica Lindsey case forced me to actually look at what "NNA row" meant across the full history. Generalizable lesson: new consumers of legacy silver should sample at least 3 date-spaced partitions during schema discovery.

2. **Mixed-type parquet union pitfall.** BD silver `transaction_id` flipped object→int64 at 2026-01-27. Same for other id-like cols. `pd.concat` of int64-dtype + synthetic string IDs fails at parquet write. Per-partition dtype alignment (ints→strings for the union) is the correct fix; the alternative of writing synthetic IDs as ints would collide with real BD IDs.

3. **pyarrow.read_parquet(columns=...)** is the right first move but breaks when columns are missing. Pattern: `ParquetFile(body).schema_arrow.names` → project to intersection → fill missing with None in pandas. Much faster than reading full parquet and slicing.

4. **Fuzzy fallback rate was lower than expected.** Only 656 Schwab-only accounts fuzzy-resolved out of 967 unmatched. The remaining 311 `schwab_only_unassigned` accounts are likely the never-onboarded edge — Schwab has them, BD never will. For now these imputed rows carry `architect='Unassigned'`; CTO should decide whether to keep them or drop.
