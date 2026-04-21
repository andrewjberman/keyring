# Session Log — Schwab TRN NNA Enrichment: Layer A + Layer B Ingestion

**Agent:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-21
**Continues from:** `org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-04-21/schwab_trn_nna_enrichment_investigation.md`
**Brief:** `docs/briefs/ae-brief-schwab-trn-nna-enrichment.md`
**Authorization:** Andrew direct GO (in-session 2026-04-21) — "enhancing our data with Schwab TRNs and working these definitively into early stage pipeline via the imputation method as described. BD files take precedence, as they are multi-platform, but Schwab files come in when they are novel."

---

## Andrew's precedence directive (recorded verbatim)

> "BD files take precedence, as they are multi-platform, but Schwab files come in when they are novel, i.e. BD doesn't have them."

This is the merge-table default in `ae-brief-schwab-trn-nna-enrichment.md` (lines 212-220): `bd` / `bd_lagged` / `bd_delayed` always win on matches; `schwab_imputed` activates only where no BD record exists in ±180d. No brief changes required — directive confirms the existing design.

---

## Phase Overview (AE scope)

| Phase | Deliverable | Status |
|-------|-------------|--------|
| 2a | Validate converter positional schema on sample TRN files | complete |
| 2b | Rewrite `convert_schwab_trn_to_parquet.py` (positional, full Layer A schema, OneDrive source) | complete |
| 2c | Backfill `03_silver/TRN/` (496 partitions) | complete |
| 3 | New `convert_schwab_trn_to_nna_silver.py` + backfill `03_silver/TRN_NNA/` | *in progress / complete — update at end* |
| 4 | NNA parity harness Jul-Dec 2024 vs Schwab PDF | *pending* |
| 5 | Schema contract doc + pipeline_inventory.xml + commit/push | *pending* |

---

## Decisions

### Source selection: local OneDrive, not S3 01_raw
- OneDrive has 496 TRN files (2024-04-12 → 2026-04-20); fully covers the reconciliation window.
- S3 `01_raw/` has 568 TRN files but 390 are GLACIER (all 2024 H2 + all 2025 H1); only 178 STANDARD.
- Triggering Glacier restore would take 5-12h with no added coverage — Andrew confirmed "we have it all locally ready to go".
- `02_anonymized/` route (345 STANDARD, 2024-07 → 2025-11) was an option but requires de-anon via `03_mappings/` JSONs — strictly worse than reading the original un-anonymized files from OneDrive.
- Decision: **OneDrive is authoritative for Layer A backfill. S3 01_raw becomes archive-only.**

### Positional parsing over regex pattern match
- Existing converter used regex against H2 column names. Verified broken: pattern `Trade.*Date` never matches the bare `Trade` column label (the date-ness comes from the H3 extension row — `h3='Date'`). Prior script had never been backfilled in production; all schema gaps discovered by this session.
- Positions 0..50 are stable across format versions 01.04 (2024, 116 cols) and 01.06 (2026, 137 cols) — verified on CRS20240412 / CRS20241231 / CRS20260402.
- Positional scheme follows ULN converter precedent (`convert_schwab_uln_to_silver.py`, 2026-04-17).

### Glacier: intentionally deferred
- 390 GLACIER TRN files in `01_raw/` remain archived. If future work needs them we can trigger Bulk restore (~$0.02 total; 5-12h delay). Not blocking any current consumer.

---

## Artifacts

### Code

| Path | Action | Notes |
|------|--------|-------|
| `data/black_diamond/scripts/bronze/convert_schwab_trn_to_parquet.py` | **Rewritten** | Positional D1 parse (positions 0..50 stable across v01.04/v01.06), full Layer A schema per brief, OneDrive source, ProcessPool(8). Idempotent against `03_silver/TRN/`. |
| `data/black_diamond/scripts/bronze/convert_schwab_trn_to_nna_silver.py` | **New** | Layer B classifier; reads `03_silver/TRN/`, writes `03_silver/TRN_NNA/`. Stable `schwab_txn_key` for canonical_nna merge anti-double-count. |
| `data/schwab/analysis/nna_parity_harness.py` | **New** | Rolls up Layer B by month, compares to Schwab PDF Jul-Dec 2024 ground truth with ±15% acceptance band. Emits `nna_parity_report.csv`. |

### Docs

| Path | Action |
|------|--------|
| `docs/data/schwab_trn_nna_contract.md` | **New** — schema + classifier + merge contract (DS consumer) |
| `org/tier2_senior/0.6.0_AE_PartnerETL/deliverables/pipeline_inventory.xml` | **Updated** — new `<pipeline name="schwab-ingestion-partner-etl">` block at file end |

### S3 writes (to `opal-data-schwab`)

| Prefix | Count | Source | Notes |
|--------|-------|--------|-------|
| `03_silver/TRN/date={YYYYMMDD}/data.parquet` | 496 | OneDrive | 2024-04-12 → 2026-04-20 |
| `03_silver/TRN_NNA/date={YYYYMMDD}/data.parquet` | *pending final — see Summary below* | S3 Layer A | |

---

## Validation — single-day spot check (2024-12-31)

Target: Jessica Lindsey Short Trust wire $20.10M (cited in brief as representative of the BD-undercounted inflows).

**Layer A output (row count 13,473 — matches D1 line count exactly):**
```
acct10 account_id_padded tran_code transaction_source   transaction_detail   trade_date  gross_amount
79128541      0079128541     DPWRF     WIRED FUNDS IN WIRED FUNDS RECEIVED 2024-12-31     2,083,800.00
79128541      0079128541     DPWRF     WIRED FUNDS IN WIRED FUNDS RECEIVED 2024-12-31    18,010,927.40
                                                                                        = 20,094,727.40
```

**Layer B output (213 NNA-eligible rows on 2024-12-31):**
- Direction totals: $22.77M inflow / $1.54M outflow
- Sub-category breakdown (inflow): WIRE $20.09M / TOA $1.87M / DEPOSIT $0.40M / MONEYLINK $0.40M
- Both Jessica Lindsey rows present, `direction=inflow`, `sub_category=WIRE`, stable `schwab_txn_key`

---

## Compiler Tools

| Phase | Tool | Command | Result |
|-------|------|---------|--------|
| 2a    | manual | `head -c 6000 CRS20260402.TRN` + `python3 probe.py` | Validated H1/H2/H3/D1 positions against 3 dates (2024-04, 2024-12, 2026-04) — positions 0..50 stable across format versions. |
| 2a    | `boto3 list_objects_v2` | | Counted 568 S3 TRN files (178 STANDARD + 390 GLACIER) vs 496 OneDrive files. Triaged: OneDrive is primary source. |
| 2b/2c | n/a | | Pure local-source → S3 silver write. No gold script, no Lambda, no IAM, no CloudFront — comp-pipescript / comp-iam / comp-routes not applicable. Role-minimum AE mandate for this scope: `comp-pipescript deployed` does not apply (not a gold-script deploy). |
| 3     | `convert_schwab_trn_to_nna_silver.py --date 20241231` (spot check) | | 213 rows, Jessica Lindsey $20.09M WIRE inflow confirmed. |
| 4     | `nna_parity_harness.py --month-range 2024-07 2024-12` | | *pending Layer B completion — append results* |

---

## Current State + Next Steps

**Current state (updating at session end):**
- Layer A (`03_silver/TRN/`): 496 partitions, 2024-04-12 → 2026-04-20, 0 errors
- Layer B (`03_silver/TRN_NNA/`): backfill running / complete
- No code committed yet — staged at session end

**Next steps:**

- `[0.6.0_AE_PartnerETL]` — Run parity harness (`nna_parity_harness.py --month-range 2024-07 2024-12`); append verdict to this log. Then commit all artifacts as scoped commit with `--only`, push CLOUD with `--follow-tags` if tag warranted.
- `[1.0.0_SA_CTO]` — Review Layer A/B schemas vs brief acceptance criteria (1-7). Flag if any column rename needed before DS integration.
- `[0.4.0_DS_ClientPlatform]` — Brief Phase 6: extend `C_01.canonical_nna.py` to read `03_silver/TRN_NNA/`, apply the 6-tag source_system merge, add `source_system` column. Anti-double-count via `schwab_txn_key`.
- `[0.4.0_DE_PortalFrontend]` — Phase 7 (after DS ships): surface `imputed_pct` in partner_analytics_monthly; add portal indicator.
- `[0.6.0_AE_PartnerETL]` — Follow-up TO: Schwab SFTP automation to replace OneDrive manual delivery (scheduled ingest). Out of this workstream; after DS integrates.

**Not touched this session (out of scope):**
- VA ghost-account classifier fix (Jun 2024 outflow overcount) — DS-lane work on `nna_flows.py`.
- Glacier restore for 01_raw/ 2024-H2 + 2025-H1 (unnecessary; OneDrive covers window).
- Multi-firm generalization (only 0008242234 = 49F today).
- Portal UI changes (DE lane after DS).

---

## Related

| Doc | Purpose |
|-----|---------|
| **Brief:** `docs/briefs/ae-brief-schwab-trn-nna-enrichment.md` | Engineering design (inherited from prior session) |
| **Contract:** `docs/data/schwab_trn_nna_contract.md` | Schema + classifier + merge rules for DS |
| **Investigation log:** `org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-04-21/schwab_trn_nna_enrichment_investigation.md` | Root-cause trace leading to this work |
| **Reference ULN brief:** `docs/briefs/ae-brief-schwab-uln-silver-ingestion.md` | Precedent pattern for same-shape silver producer |
| **Prior ULN log:** `org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-04-17/schwab_uln_silver_ingestion.md` | Backfill procedure reference |
| **Memory:** `~/.claude/projects/.../memory/project_schwab_trn_nna_enrichment.md` | Agent-scoped persistent memory |
