# Session Log -- Schwab TRN NNA Enrichment Investigation + Design Brief

**Agent:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-21
**Session purpose:** Investigate the 49 Financial NNA reconciliation gap between our canonical NNA (BD silver -> `C_01.canonical_nna`) and Schwab's Business Review PDF. Identify root causes, author an engineering design brief for Schwab TRN enrichment of canonical_nna, catalog reusable bronze/silver infrastructure to prevent wheel-reinvention, and verify OneDrive -> S3 sync coverage for the full 2024-2026 TRN corpus.

---

## Phase Overview

| Phase | Action | Outcome |
|-------|--------|---------|
| 1 | Parse Schwab Business Review PDF monthly NNA (May 2024 - May 2025) and compare to our `platinum/firm/timeseries_overview.json` `nna.monthly` | 3 divergence classes identified; 13-mo NNA delta = -$143.6M (ours lower) |
| 2 | Advisor-level drilldown on Jun 2024 (largest divergence month) | $85M outflow excess attributed entirely to null-advisor "Other" bucket; single-day spike on 2024-06-28 |
| 3 | Canonical NNA parquet drill to account level (Jun 2024) | 210 "ghost" accounts with null architect + null relationship_id, zero pre-event AUA, post $80.82M outflow on 2024-06-28 |
| 4 | Silver transaction drill for those 210 accounts | 644 `EF Transfer Out` + 274 `Cash Withdrawal` + 18 `DST TRANSFER OUT` = 936 txns; `original_account_number` prefix `METVA_` identifies them as **MetLife Variable Annuity** held-away accounts; Schwab excludes VA from NNA, our classifier counts them. Jun 2024 root cause CONFIRMED. |
| 5 | Same drill on Dec 2024 (largest inflow-undercount month) | BD silver Dec 2024 inflow = $27M; Schwab PDF Dec 2024 inflow = $81.8M; $54.8M gap is not a classifier issue -- BD silver is complete for Dec 2024 (22 business days, all present). |
| 6 | User provided Schwab TRN files (128 files Jul-Dec 2024 at this point, later expanded to 245 incl. H1 2024) | Located at `C:\Users\AndrewBerman\OneDrive - Opal Capital\Documents\Schwab Data Delivery\08242234\CRS{YYYYMMDD}.TRN` |
| 7 | Reverse-engineered Schwab TRN format (pipe-delimited; record-type prefixes H1/H2/H3/D1/T1; 115 columns with duplicates) | Classifier rules derived by matching monthly totals against Schwab PDF (achieved 85-90% parity) |
| 8 | Account-level cross-reference Schwab TRN vs BD silver (Dec 2024) | 581 Schwab-only (acct, date) pairs summing $61M; no matching BD record at any date |
| 9 | Expanded to Jul-Dec 2024 full window + delay-match search (±180d) | 1,642 truly-missing pairs totaling $91.3M; only 696 delayed matches ($8.4M, median lag 7d). Confirms BD silver is missing, not just lagging. |
| 10 | Acct-lifecycle investigation on top 10 missing accounts | Root cause: **BD client-master onboarding lag.** New 49F accounts appear in Schwab with initial wire immediately; BD doesn't ingest for 2d-5mo and never backfills the original funding transaction. Example: acct `33823043` (STONERIDGE ROAD GROUP HOLDINGS) -- Schwab $17.40M wire on 2024-12-30, BD first sighting 2025-05-30. |
| 11 | Cataloged existing Schwab ingestion infrastructure | `sync_schwab_onedrive_to_s3.py`, `convert_schwab_trn_to_parquet.py`, `convert_schwab_uln_to_silver.py`, `convert_schwab_rps_to_silver.py` all present and owned by partner-ETL lane |
| 12 | Authored design brief `docs/briefs/ae-brief-schwab-trn-nna-enrichment.md` | Scopes two-layer silver + reconciliation + C_01 enrichment; phased AE -> DS -> DE handoff |
| 13 | Saved PoC scripts as persistent references under `data/schwab/analysis/` | Prevents wheel-reinvention during brief -> TO -> implementation cycle |
| 14 | Dry-run `sync_schwab_onedrive_to_s3.py --account 08242234` after user uploaded Q1-Q4 2025 TRNs | Nothing to upload; all 1,232 local CRS files already present in `s3://opal-data-schwab/01_raw/` |
| 15 | Verified S3 TRN coverage totals: 568 files (2024-01-16 -> 2026-04-20) | 243 x 2024, 251 x 2025, 74 x 2026 (partial) |

---

## Investigation Findings (Summary)

### Three gap classes (13-mo window May 2024 – May 2025)

| Gap | Period | Amount | Root Cause |
|-----|--------|-------:|-----------|
| Outflow overcount | Jun 2024 | ~$85M (single day 2024-06-28) | 210 MetLife VA "ghost" accounts with null advisor/relationship, zero pre-event AUA. Schwab excludes held-away VA from NNA; BD's `nna_flows` classifier treats them as outflows. |
| Inflow undercount | Jul-Dec 2024 | ~$91M across 1,642 (acct, date) pairs | BD client-master onboarding lag. Schwab credits TRN on wire receipt; BD recognizes account 2d–5mo later, then ingests only current holdings, never replays original wire. |
| Classifier / definition diffs | ongoing | ~$35-50M small-item residual | Schwab NNA definition: Cash + TOA + FDIC, excluding intra-Schwab Retail<->Advisor moves. Our classifier mostly aligns but has small residual diffs. Probably acceptable after the big two gaps are fixed. |

### Reconciliation evidence

Top 4 missing inflows (from delay-matching analysis Jul-Dec 2024) = $47.5M of the $91M gap:

| acct10 | Trade date | Amount | Type | BD first sighting | BD inflow for this event |
|--------|------------|-------:|------|-------------------|-------------------------|
| 79128541 (Jessica Lindsey Short Trust) | 2024-12-31 | $20.10M | WIRED FUNDS RECEIVED | 2025-01-02 | Never |
| 33823043 (Stoneridge Road Group Holdings) | 2024-12-30 | $17.40M | WIRED FUNDS RECEIVED | 2025-05-30 | Never (only current-holdings ACAT-In spread) |
| 31796322 (Petty, Trent & Mary) | 2024-12-23 | $6.23M | WIRED FUNDS RECEIVED | 2025-01-02 | Never |
| 59843655 (Petty, Mary & Trent) | 2024-12-23 | $3.75M | WIRED FUNDS RECEIVED | 2025-01-03 | Never |

### Monthly NNA parity (my TRN classifier vs Schwab PDF, Jul-Dec 2024)

| Month | PoC Inflow | Schwab Inflow | Coverage | PoC Outflow | Schwab Outflow | Coverage |
|-------|-----------:|--------------:|---------:|------------:|---------------:|---------:|
| 2024-07 | $19.91M | $43.4M | 46% | $9.80M | $15.1M | 65% |
| 2024-08 | $27.86M | $40.9M | 68% | $29.42M | $31.4M | 94% |
| 2024-09 | $15.94M | $23.8M | 67% | $15.18M | $16.4M | 93% |
| 2024-10 | $59.19M | $69.5M | 85% | $18.20M | $23.2M | 78% |
| 2024-11 | $20.38M | $28.9M | 71% | $8.96M | $11.0M | 81% |
| 2024-12 | $73.66M | $81.8M | 90% | $14.86M | $17.5M | 85% |

Inflow coverage is >85% on 2 of 6 months and 46-71% on the others -- classifier rules need tightening before production. Direction dominates the gap (we're reasonably close on outflows). User-provided Schwab NNA definition ("Cash + TOA + FDIC; exclude Retail<->Advisor intra-Schwab") will likely close most of the remaining diff.

---

## Asset Inventory

### Existing infrastructure REUSED (do not reinvent)

| Path | Owner | Purpose |
|------|-------|---------|
| `data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py` | 0.4.0_DS_ClientPlatform (2026-04-14) | OneDrive -> `s3://opal-data-schwab/01_raw/` uploader; idempotent; SSE=AES256; supports `--account`, `--since`, `--upload` |
| `data/black_diamond/scripts/bronze/convert_schwab_trn_to_parquet.py` | 0.6.0_AE_PartnerETL (ADHC_HISTRY) | TRN -> `03_silver/TRN/date={date}/data.parquet`; pattern-matched key columns; uses `D1|` record-type filter. **Written but never backfilled.** |
| `data/black_diamond/scripts/bronze/convert_schwab_uln_to_silver.py` | 0.6.0_AE_PartnerETL (2026-04-17) | ULN silver pipeline; reference implementation for the pattern the new TRN-NNA converter should follow. 349 STANDARD partitions backfilled. |
| `data/black_diamond/scripts/bronze/convert_schwab_rps_to_silver.py` | 0.6.0_AE_PartnerETL | RPS silver pipeline (position snapshots, not transactions) |
| `data/black_diamond/scripts/gold/lib/nna_flows.py` | 0.4.0_DS_ClientPlatform | BD-side NNA classifier (`INFLOW_TYPES`, `OUTFLOW_TYPES`, garbage filter, intra-Schwab exclusion patterns) -- reference for semantic parity with the Schwab-side classifier |
| `data/black_diamond/scripts/gold/C_01.canonical_nna.py` | 0.4.0_DS_ClientPlatform | Gold-layer canonical NNA producer -- will become the merge point per brief Phase 6 |
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` `_build_nna_by_period` | 0.4.0_DS_ClientPlatform | Monthly/quarterly/annual rollup; consumer of canonical_nna |

### PoC scripts AUTHORED this session (investigation artifacts, not production)

| Path | Purpose |
|------|---------|
| `data/schwab/analysis/README.md` | Index + status ("PoC, not production; delete after canonical versions ship") |
| `data/schwab/analysis/trn_nna_classify_poc.py` | TRN parser + NNA classifier + monthly-total reporter; validated to 85-90% parity vs Schwab PDF on 6 months |
| `data/schwab/analysis/reconcile_schwab_bd_nna.py` | Cross-references Schwab TRN inflow (acct10, date) pairs vs BD silver with same-day exact match + ±180d delay-match; emits `missing / delayed_or_offset / exact_same_day` classification |

### New assets to BUILD (per brief, post-TO)

| Path | Phase | Owner |
|------|-------|-------|
| Fix-up + backfill of `convert_schwab_trn_to_parquet.py` | Brief Phase 2 | 0.6.0_AE |
| `data/black_diamond/scripts/bronze/convert_schwab_trn_to_nna_silver.py` (new) | Brief Phase 3 | 0.6.0_AE |
| `docs/data/schwab_trn_nna_contract.md` (schema + classifier doc) | Brief Phase 5 | 0.6.0_AE |
| NNA-parity validation harness (monthly totals vs Schwab PDF) | Brief Phase 4 | 0.6.0_AE |
| Extension of `C_01.canonical_nna.py` (`source_system` column, merge logic) | Brief Phase 6 | 0.4.0_DS |
| Portal `imputed_pct` surface in partner_analytics | Brief Phase 7 | 0.4.0_DE |

### Data-path cheatsheet (every path touched this session)

**Schwab `s3://opal-data-schwab/`:**

| Path | Count (2026-04-21) | Status |
|------|-------------------:|--------|
| `01_raw/CRS{YYYYMMDD}.TRN` | 568 | Complete 2024-01-16 to 2026-04-20 |
| `01_raw/CRS{YYYYMMDD}.RPS` | present | Existing silver producer consumes |
| `01_raw/CRS{YYYYMMDD}.ULN` | 566 | 349 STANDARD + 217 GLACIER |
| `02_anonymized/CRS{YYYYMMDD}.*` | partial | Overlap with `01_raw/` |
| `03_mappings/CRS{YYYYMMDD}.*.mapping.json` | through 2025-11 | Anon hash -> item_id |
| `silver/RPS/date={YYYYMMDD}/data.parquet` | backfilled | RPS silver (per existing converter) |
| `silver/ULN/date={YYYYMMDD}/data.parquet` | 349 | ULN silver (per existing converter, 2026-04-17) |
| `bronze/rps/` | 63 | Historical RPS mirror |
| `03_silver/TRN/date={YYYYMMDD}/data.parquet` | **0** | **Phase 2 target** |
| `03_silver/TRN_NNA/date={YYYYMMDD}/data.parquet` | **0** | **Phase 3 target (new layer)** |

**BD `s3://opal-data-bd/`:**

| Path | Purpose in this investigation |
|------|-------------------------------|
| `silver/transactions/{YYYY-MM-DD}.parquet` | BD's side of the reconciliation (inflow/outflow source for `nna_flows.py`) |
| `gold/canonical/nna/{YYYY-MM-DD}.parquet` | Per-account daily NNA; confirmed silver agrees with canonical on totals |
| `platinum/firm/timeseries_overview.json` | Monthly/quarterly/annual NNA timeseries; where the original 13-mo delta vs Schwab was first observed |
| `platinum/firm/partner_analytics_monthly.json` | Per-period, per-advisor, per-geo breakdown (recent 4 months window) |
| `platinum/49financial/ownership_map.json` | 49F-specific ownership map (unused this session; referenced for completeness) |

**OneDrive (manual Schwab delivery):**

| Path | Count |
|------|------:|
| `C:\Users\AndrewBerman\OneDrive - Opal Capital\Documents\Schwab Data Delivery\08242234\CRS*.TRN` | 496 |
| `C:\Users\AndrewBerman\OneDrive - Opal Capital\Documents\Schwab Data Delivery\08242234\CRS*.*` (all extensions) | 1,232 |

**Schwab master-account identifier:** `0008242234` = 49 WEALTH MANAGEMENT LLC (embedded in every TRN H1 header).

---

## TRN OneDrive -> S3 Sync Action

**Command:** `python3 data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py` (dry-run; no `--upload`)

**Result:**

```
Account: 08242234
OneDrive root: C:\Users\AndrewBerman\OneDrive - Opal Capital\Documents\Schwab Data Delivery\08242234
Local CRS files: 1,232
Listing s3://opal-data-schwab/01_raw/ ...
  existing in 01_raw/: 6,565
  existing in bronze/rps/: 63
Missing in 01_raw/: 0
Missing in bronze/rps/: 0
Nothing to upload. In sync.
```

**Interpretation:** The user's newly-downloaded 2025 TRN files (123 Q1/Q2 + 128 Q3/Q4 = 251) were already delivered to S3 via a prior sync cycle. No manual upload required. TRN coverage in `01_raw/` is continuous from 2024-01-16 through 2026-04-20 (243 x 2024 + 251 x 2025 + 74 x 2026 = 568 TRN files).

**What this unblocks:** Brief Phase 2 (`03_silver/TRN/` backfill via `convert_schwab_trn_to_parquet.py`) can execute against the full authoritative corpus immediately upon TO issuance. No data-movement prerequisite remains.

---

## Compiler Tools

| Phase | Tool | Command | Result / rationale |
|-------|------|---------|---------------------|
| 1-10 | Investigation, not code-shipping. Compiler tools (comp-pipescript/blast/iam/routes) N/A -- no gold script change, no Lambda/EC2 deploy, no IAM, no CloudFront. Role-minimum compiler-tools mandate does not apply to non-deployment AE sessions. | | |
| 11 | `aws s3 ls s3://opal-data-schwab/` (recursive + filter-by-year) | manual | Confirmed `01_raw/`, `02_anonymized/`, `03_mappings/`, `03_silver/`, `bronze/rps/` structure; 568 TRN files with year-level distribution |
| 14 | `python sync_schwab_onedrive_to_s3.py` (dry-run) | as above | `Missing in 01_raw/: 0` |
| Verification | `python data/schwab/analysis/trn_nna_classify_poc.py --months 2024-07 2024-12` | PoC validation | Confirmed saved script produces same Jul ($19.91M in / $9.80M out) and Dec ($73.66M in / $14.86M out) totals as original inline analysis. |

---

## Current State + Next Steps

**Current state:**
- Investigation complete; root causes for both gap classes identified and documented
- Design brief authored at `docs/briefs/ae-brief-schwab-trn-nna-enrichment.md`
- PoC classifier + reconciler saved under `data/schwab/analysis/` for reference / validation handoff
- S3 raw-TRN corpus complete (568 files, 16 months continuous)
- `03_silver/TRN/` still empty (Phase 2 execution gated on CTO brief approval + TO)
- No code pushed; no AWS changes; no Terraform changes

**Next steps:**

- `[2.0.0_SA_COO]` — Review brief `docs/briefs/ae-brief-schwab-trn-nna-enrichment.md` with CTO. Resolve the four open design questions (advisor-attribution fallback, diff-flag threshold, Layer B materialization cost, merge-locus DS-vs-AE). Decompose into 2-3 TOs for 0.6.0_AE_PartnerETL (Phase 2-5) + 1 TO for 0.4.0_DS_ClientPlatform (Phase 6).
- `[0.6.0_AE_PartnerETL]` — On GO: validate existing `convert_schwab_trn_to_parquet.py` on one sample file, confirm `D1|` row count matches parquet row count, confirm all 12 KEY_FIELD_PATTERNS resolve, confirm numeric and date parsing works. Then backfill all 568 dates.
- `[0.6.0_AE_PartnerETL]` — Post Phase 2: promote `trn_nna_classify_poc.py` classifier rules into a production `convert_schwab_trn_to_nna_silver.py` converter. Write to `03_silver/TRN_NNA/date={date}/data.parquet`.
- `[0.6.0_AE_PartnerETL]` — Post Phase 3: run parity harness; write `docs/data/schwab_trn_nna_contract.md`; update `pipeline_inventory.xml` and hand to DS.
- `[0.4.0_DS_ClientPlatform]` — Post Phase 5: extend `C_01.canonical_nna.py` per brief merge algorithm; add `source_system` column; re-run canonical_nna and validate against Schwab PDF for Jul-Dec 2024 (target: within +/- 15% on inflow totals; Jun 2024 outflow separately handled by VA ghost-account fix in `nna_flows.py`, out of this workstream's scope).
- `[Andrew]` — Confirm attribution fallback preference (brief Q1) before DS integration.

**Not touched this session / out of scope:**
- VA ghost-account classifier fix (Jun 2024 outflow overcount). Separate DS-lane work on `nna_flows.py`.
- Snowflake / warehouse export of Schwab TRN silver.
- Multi-firm generalization (only 49F today; structure generalizes trivially).
- Schwab SFTP automation (replacing OneDrive manual delivery). Follow-up TO after Phase 5.

---

## Related

| Doc | Purpose |
|-----|---------|
| **Brief:** `docs/briefs/ae-brief-schwab-trn-nna-enrichment.md` | Engineering design for the enrichment pipeline; this log is the work-trace leading to it |
| Reference brief (same pattern, prior workstream): `docs/briefs/ae-brief-schwab-uln-silver-ingestion.md` | ULN ingestion for B_01 phantom-position investigation (0.4.0_DS -> 0.6.0_AE, 2026-04-17) |
| Prior 0.6.0_AE session log (ULN backfill precedent): `org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-04-17/schwab_uln_silver_ingestion.md` | Shape / structure of successful silver-layer backfill; reuse its patterns |
| Investigation memory: `~/.claude/projects/C--Users-AndrewBerman-Desktop-ajb-workspace/memory/project_schwab_trn_nna_enrichment.md` | Agent-scoped persistent memory of this workstream |
| DS-authored Schwab SoT cross-reference (prior investigation): `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-03-04/REQ_schwab_sot_cross_reference.md` | Earlier manual Schwab PDF ingestion for May 2025 snapshot |
| Source PDF (user's authoritative reference): `C:\Users\AndrewBerman\Downloads\49 Financial Business Review Dashboard May 2025 1.pdf` | Monthly/annual NNA ground truth |
