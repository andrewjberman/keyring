# 0.4.0_DS_ClientPlatform — Evening Session: 49F Alternatives Investigation + BDPL Refactor Plan

**Date:** 2026-04-14 (EDT)
**Session span:** ~13:30 EDT → ~17:00 EDT
**Agent:** 0.4.0_DS_ClientPlatform
**Mode:** No MCP / no inbox / Andrew-direct only (per session directive)

---

## Startup

Session started as direct conversation with Andrew (no MCP, no outbound). Trigger: "49 Financial Alternatives position is ~$62M today but portal was showing $84-93M a couple days ago, and historical range since June 2025 has been $65-72M. Why?"

---

## Work Completed This Session

| Work Item | Type | Commit | Path |
|---|---|---|---|
| 49F Alternatives value stability investigation | Research | — | — |
| BNP Paribas $23M phantom diagnosis | Research | — | — |
| BDPL Asset Dim + Canonical Prices + Classification refactor brief | Design | (staged) | `org/tier2_senior/0.4.0_DS_ClientPlatform/briefs/2026-04-14_asset_dim_and_canonical_prices_refactor.md` |
| Schwab OneDrive → S3 sync script + backfill (6 trade dates) | Infra | (uncommitted; AE-modified for SSE) | `data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py` |
| Silver RPS/TRN converters run for 04-06 → 04-13 | Pipeline | — | `s3://opal-data-schwab/silver/RPS/`, `silver/TRN/` |
| Gold vs silver reconciliation (49F) | Research | — | — |
| BDPL_ASTDIM.W2 — BD `asset_super_class` recon doc | Deliverable | `39692589` | `data/black_diamond/recon/bd_asset_super_class_values.md` |
| BDPL_ASTDIM.W4 — `build_bd_assets_dim.py` builder + live write | Deliverable | `39692589` | `data/black_diamond/scripts/silver/build_bd_assets_dim.py`, `s3://opal-data-bd/silver/bd_assets_dim.parquet` |

---

## Core Findings — 49F Alternatives Instability

### The symptom

- Portal showed 49F Alternatives at $84-93M a few days ago; current (2026-04-10 gold run) = $61.8M
- Historical monthly (`s3://opal-data-bd/gold/firm_mix_views.json`): ~$89-90M in Apr/May 2025, step-down to ~$72M on 2025-06-10, gradually drifted to ~$65M by year-end, ~$62M current
- Daily series (`firm_mix_views_daily.json`): alt swung $95M (04-07) → $97M (04-08) → $84M (04-09) → $62M (04-10)
- Firm total AUA is stable at ~$1.6B across all four days — so this isn't from position additions/removals

### The $23M BNP Paribas phantom (single biggest root cause)

Account `z0819189891` holds a BNP Paribas bond (CUSIP `05613L3H2`, 215,000 face-value units, cost $1.0188/unit = 101.88% of par). Real MV ≈ $219K. Gold was reporting **$23,007,150** because:

1. Our gold layer tagged this lot with ticker `BNPQF` (the BNP Paribas equity ADR — wrong ticker; this bond has no ticker)
2. `build_canonical_prices_v2.py` looked up `BNPQF` on Yahoo → got equity ADR price $107.01
3. Market value = 215,000 units × $107.01 = $23,007,150 phantom

**Pattern replicates.** Scanning 49F for `cost_per_unit < $5 AND current_price > $20 AND price_quality='yahoo_finance'` turned up two more bond-priced-as-equity phantoms:
- `WELLS FARGO & CO 4.15% 01/24/2029` → tagged WFC equity, $860K phantom (real ~$9K)
- `NEWMONT CORP 2.8% 10/01/2029` → tagged NEM equity, $595K phantom (real ~$4K)

Total confirmed bond phantoms on 49F: **~$24.3M**. All have CUSIP present in BD asset_dim but classification / ticker resolution failed upstream.

### BD's classification has no "Alternatives" bucket

Reconciled 49F holdings 04-10 ($1,653M from gold/holdings_lots) against the BD asset_dim. BD's `Asset SuperClass` taxonomy:

```
Equities                    $1,223M   (74.6%)
Fixed Income                $  319M   (19.4%)
To Be Classified            $   70M   ( 4.3%)  — catch-all (structured notes, annuities, CITs, balanced funds, ADR mislabels)
Cash & Cash Equivalents     $   21M   ( 1.3%)
Unclassified                $    5M   ( 0.3%)
DIVERSIFIER                 $    2M   ( 0.1%)
```

BD does not classify anything as "Alternatives." Our portal's Alternatives bucket is derived downstream in `D_03.composition_artifacts.py` / `D_00b.portal_timeseries.py` / `C_06.client_mix_timeseries.py` via `classify_series` → DynamoDB `ETFClassifier` + `B_01b.classify_new_securities.py` keyword heuristics.

**Andrew's decision (2026-04-14):** BD's "To Be Classified" = Alternatives in our book. TBC contents are Shield/Buffer/Point-to-Point structured notes ($27M), CITs/balanced/target-date funds ($10M), private fund feeders / annuities / options / misclassified ADRs — all legitimately alternative for Opal's taxonomy.

### Root causes

1. **Gold layer can't join to BD asset_dim on a durable key** — `holdings_lots` has ticker + asset_name only. No CUSIP, no `asset_id`, no `TransactionID`. `silver/transactions` has `asset_id` + `transaction_id` but drops `cusip` from the BD xlsx source.
2. **`build_canonical_prices_v2.py` routes to Yahoo by ticker regardless of asset class** — Fixed Income and TBC assets that happen to have an equity-matching ticker produce face-value × equity-price phantoms. BNP is the archetype.
3. **Classification is derived downstream from keyword heuristics instead of BD's authoritative `Asset SuperClass`** — introduces drift, especially on preferreds, CLOs, hedged-equity products, convertibles.

---

## Gold vs Silver Reconciliation — 49F on 2026-04-10

**Important correction mid-session:** initial reconciliation used raw `gold/holdings_lots` ($1,890M) vs silver/allocations ($1,682M), which looked like a $208M overstatement. That was apples-to-oranges — raw holdings_lots is an internal stage. The gold PIPELINE output (`gold/firm_mix_views.json`, `firm_composition.json`) already applies AP gate + architect-lookup + ghost exclusion and outputs $1,625M. The correct comparison:

```
Silver authoritative (allocations.account_market_value):     $1,681,963,293
Gold pipeline output (firm_mix_views, firm_composition):     $1,624,913,423
Delta:                                                          -$57,049,871  (-3.39%)
  ... of which cash (silver includes cash, gold doesn't):     -$40,496,558
  ... residual non-cash gap:                                   -$16,553,313  (-1.01%)
```

"Always within a couple percent" is real. The -$57M gap is ~71% cash (structurally addressable via cash-as-position refactor) and ~29% residual position-coverage gap (a mix of multi-custodian plan sleeves, bond price drift, illiquid-asset valuation lag).

### The $200M raw-holdings-lots noise (already filtered by pipeline)

Gold `holdings_lots` carries **2,073 accounts ($237M)** that are not in current `silver/allocations`. Breakdown:

- **149 accts ($36.1M) validated by Schwab RPS 04-10** — real Schwab-only positions missing from silver allocations (silver allocations scope is partial for Schwab relationships).
- **1,924 accts ($201M) orphaned** — no Schwab mapping, not in Schwab RPS. 90% of positions acquired pre-2023. Holdings are 401(k) institutional share classes (Kensington KAMIX, JHQTX, PIMIX, MFS RERGX, Cohen & Steers LPXIX) — the signature of deprecated recordkeeper integrations (Empower / Fidelity / Principal).

Position-level overlap test on rel `z0880615` (Waldrop, 14 accounts): **zero exact unit matches** between orphan and joint accounts under the same relationship. Naming is similar ("SLAT Managed" vs "SLAT - Managed", "Waldrop Investments LLC" vs "WALDROP INVESTMENTS LLC-CORPORATION") but underlying positions differ. These are not account-ID renumbering / dedup candidates — they're distinct real accounts where BD's reporting coverage changed over time.

**Andrew's direction:** do not auto-retire these orphans. They may represent real AUA tracked under different account_ids or at non-Schwab custodians our pipeline has lost visibility on. The pipeline's existing architect-filter already drops them from firm aggregations correctly; `holdings_lots` orphan cleanup is hygiene, not a reconciliation fix.

### Schwab validation confirmed coverage is essentially complete

Of Schwab's entire 04-10 RPS universe (5,610 accounts, $1,493M), only **15 accounts ($2.7M — 0.18%)** lack a BD↔Schwab mapping. The mapping at `s3://opal-data-bd/gold/dimensions/schwab_bd_account_mapping.parquet` is therefore a reliable authority for "this account exists at Schwab."

---

## Infrastructure Work — Schwab OneDrive → S3 Sync

### Canonical download location discovered

Schwab SI2 Desktop client writes per-account CRS files to:
```
C:\Users\AndrewBerman\OneDrive - Opal Capital\Documents\Schwab Data Delivery\08242234\
```

`08242234` is 49F's Schwab master account number. Configured in the client's `user.config` as `AccountPreferenceSetting.08242234.Destination` (overrides the empty `DefaultDirectory` = `Downloads\schwab_downloads`). 13 file extensions per trade date: `ACC, RLD, RLW, RPS, SEC, TCF, TCFX, TNN, TRN, ULN, ULT, UPN, UPT`.

### New sync script

`data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py`
- Scans OneDrive account dir, set-diffs against `s3://opal-data-schwab/01_raw/` and `bronze/rps/`, uploads only missing files
- Bucket policy requires `x-amz-server-side-encryption=AES256` (added to `ExtraArgs` per AE's linter correction)
- Idempotent — safe to rerun daily

### Backfill run

Silver RPS was stale at 2026-04-02. Uploaded 70 files covering 6 new trade dates (04-06, 04-07, 04-08, 04-09, 04-10, 04-13; 04-03 absent from Schwab's delivery). Ran RPS + TRN silver converters — both succeeded, silver now current through 04-13. ACC converter failed on duplicate `state` column in source file; non-blocking (ACC wasn't needed for this session's reconciliation). Post-fix validation against Schwab RPS 04-10 changed nothing material — 149 Schwab-validated accounts (from 152 against 04-02), accuracy 150 of 152 within 5%. Confirmed the gold-only orphans aren't a Schwab-data-lag problem.

---

## Brief Filed

`org/tier2_senior/0.4.0_DS_ClientPlatform/briefs/2026-04-14_asset_dim_and_canonical_prices_refactor.md`

11 work packages covering the full refactor:
- **WP-1** (AE): `bronze/assets/` + `silver/assets/` pipeline mirroring silver/fees pattern
- **WP-2** (DS): `silver/bd_assets.parquet` dim with CUSIP/AssetID/Ticker indexes
- **WP-3** (AE): CUSIP backfill into `silver/transactions`
- **WP-4** (DS): Enrich `gold/holdings_lots` + `positions_cube` with cusip/asset_id
- **WP-5** (DS+AE): `build_canonical_prices_v2.py` refactor — CUSIP-primary, SuperClass-aware routing, never-Yahoo for Fixed Income/TBC, append-only daily ledger with weekend/holiday roll-forward, cash-as-position (with dual-classification + configurable fold-to-fixed-income per Opal convention)
- **WP-6** (DS): Classification refactor — BD `Asset SuperClass` primary, DDB `ETFClassifier` fallback-only, TBC + DIVERSIFIER → alternatives per Andrew's decision
- **WP-7** (DS): Phantom valuation scan as permanent nightly diagnostic
- **WP-8** (DS): 49F Alternatives time-series regression test (acceptance criterion)
- **WP-9** (DS): CUSIP-keyed FIFO replay + phantom reclassification (addresses `adhc_histry_005_phantom_schwab.py` 10,832 phantom / $177M figure)
- **WP-10** (DS): Account-ID lifecycle + cash-as-position + reconciliation harness (reframed mid-session — dominant work is cash closure + residual gap chasing, not orphan retention dedup)
- **WP-11** (DS): Scoped price overrides for three confirmed bond phantoms (BNP/WFC/NEWMONT, ~$24.3M) — tactical fix, one-day ship independent of refactor

CTO subsequently issued project `BDPL_CNPRCS` covering WP-3..9+11 and project `BDPL_ASTDIM` covering WP-1/W2/W4 with task-order decomposition.

---

## BDPL_ASTDIM.W2 — COMPLETE (`39692589`)

**Deliverable:** [`data/black_diamond/recon/bd_asset_super_class_values.md`](../../../../data/black_diamond/recon/bd_asset_super_class_values.md)

Enumerated BD's 6 distinct `asset_super_class` values over the compacted `silver/bd_assets.parquet` (3,449,107 txn rows, 10,937 unique `asset_id`, date range 2020-03-06 → 2026-04-13):

| super_class (asset-level) | assets | % |
|---|---:|---:|
| Equities | 5,385 | 49.24% |
| To Be Classified | 2,571 | 23.51% |
| Fixed Income | 2,215 | 20.25% |
| Unclassified | 572 | 5.23% |
| DIVERSIFIER | 164 | 1.50% |
| Cash & Cash Equivalents | 30 | 0.27% |

**Coarse bucket identification signal:** `asset_class == asset_super_class` is 100% for TBC and Unclassified, 0% for the other four super_classes. TBC + Unclassified = 3,143 assets (28.74% of book) — these are BD's explicit "I don't know" buckets and qualify for ETFClassifier fallback.

**Blend rule proposed:**
- BD wins for non-coarse values (`Equities`, `Fixed Income`, `Cash & Cash Equivalents`, `DIVERSIFIER`)
- ETFClassifier consulted for coarse values (`To Be Classified`, `Unclassified`); translation: `equity` → `Equities`, `fixed_income` → `Fixed Income`, `alternatives` → `DIVERSIFIER`, empty → retain BD coarse
- Provenance column `super_class_source` ∈ {`bd`, `etf_classifier_fallback`, `bd_coarse`}
- Never supersede BD non-coarse (PRD D3 "do not supersede" principle)

**Data quirk noted:** BD sends `'Cash & Cash Equivalents '` with trailing whitespace. Blend script strips it before comparison.

---

## BDPL_ASTDIM.W4 — COMPLETE (`39692589`)

**Deliverable:**
- Script: [`data/black_diamond/scripts/silver/build_bd_assets_dim.py`](../../../../data/black_diamond/scripts/silver/build_bd_assets_dim.py)
- Output: `s3://opal-data-bd/silver/bd_assets_dim.parquet` (10,937 rows, 884,599 bytes)
- Uploaded to: `s3://opal-data-bd/code/silver/build_bd_assets_dim.py`

**Scope-update coordination:** wrote to NEW path `silver/bd_assets_dim.parquet` rather than clobbering AE's current `silver/bd_assets.parquet` (which is txn-level, 3.45M rows). AE coordination on rename/swap deferred per W4 objective note.

**Blend result:**
```
bd                         7,794   (71.3%)  — BD's own non-coarse classification
etf_classifier_fallback    2,580   (23.6%)  — BD coarse, ETFClassifier resolved
bd_coarse (retained)         563   ( 5.1%)  — BD coarse, ETFClassifier couldn't resolve either
```

**Coarse tail shrank from 28.7% (raw) to 5.1% (blended).**

**Final blended distribution:**
```
Equities                    6,294    (+909 via ETF fallback)
Fixed Income                2,731    (+516)
DIVERSIFIER                 1,319  (+1,155)
To Be Classified              514    (from 2,571)
Unclassified                   49    (from 572)
Cash & Cash Equivalents        30    (unchanged)
```

**Opal 4-class mapping layer (per BDPL_CNPRCS Q1):**
```
equity          6,294
fixed_income    2,731
alternatives    1,833  (DIVERSIFIER 1,319 + TBC 514 folded per Andrew 2026-04-14)
other              49  (Unclassified residual)
cash               30
```

**Acceptance criteria:**
- AC1 row count ≥ 10,000: **PASS** (10,937)
- AC2 zero duplicate `asset_id`: **PASS** (dups=0)
- AC3 super_class non-null ≥ 95%: **PASS** (100.00%)
- AC4 blend recon counts logged: **PASS**
- AC5 script uploaded to `s3://opal-data-bd/code/silver/`: **PASS**
- AC6 MCP COMPLETE to COO: deferred (no-MCP session)

**Key coverage on dim:** cusip 90.5%, ticker 70.8%, symbol 100%, alternative_identifier 10%.

---

## Dim Table — Downstream Consumer Contract

`silver/bd_assets_dim.parquet` schema (one row per `asset_id`):

```
asset_id                     — BD system key (primary key)
cusip                        — durable identifier where present (90.5% coverage)
alternative_identifier       — internal BD identifier for structured products
symbol, ticker               — public market symbols
asset_name, asset_display_name, original_asset_name
asset_super_class_bd         — BD's raw super_class (whitespace stripped)
asset_super_class_blend      — blended value (BD wins; ETF fallback on coarse)
super_class_source           — 'bd' | 'etf_classifier_fallback' | 'bd_coarse'
asset_class                  — BD finer class
asset_segment                — BD finest segment
opal_asset_class             — Opal 4-class (equity/fixed_income/alternatives/cash/other)
coupon_rate, first_payment_date, last_payment_date
custodial_cost_basis_sync
first_seen_trade_date, last_seen_trade_date, txn_count
built_at                     — ISO timestamp
```

Consumers in WP-4/5/6 join on `asset_id` (primary) or `cusip` (fallback for pre-WP-3 gold tables without asset_id).

---

## Open Items Carried Forward

- **BDPL_ASTDIM W3** (silver per-date converter) — not yet run locally this session; would advance date-partitioned `silver/assets/` layout. AE scope item.
- **BDPL_ASTDIM W5/W6/W7** — AE infra work (TypeScript downloader, SSM doc, Lambda trigger, EventBridge rule 22:10 UTC, Terraform apply + `bd-v2.24.0` tag). Not DS scope.
- **BDPL_CNPRCS WP-11 tactical fix** — three bond scoped-overrides (BNP/WFC/NEWMONT) still pending scheduling. Entries specified in the brief §6 and `_SCOPED_PRICE_OVERRIDES` format captured.
- **AE coordination on silver/bd_assets.parquet rename/swap** — current txn-level file remains at its path; dim is at new path. Either AE moves txn-level → per-date partitions (W3) or DS relocates dim after AE confirms.
- **ACC converter duplicate-`state`-column bug** — failed during today's bronze-to-silver run, not blocking reconciliation work but should be fixed before ACC silver is needed.

---

## Paths Referenced (quick index)

### Brief + PRD
- `org/tier2_senior/0.4.0_DS_ClientPlatform/briefs/2026-04-14_asset_dim_and_canonical_prices_refactor.md`
- `docs/architecture/BD_CANONICAL_PRICES_CLASSIFICATION_REFACTOR.md`
- `docs/architecture/BD_ASSET_DIM_PIPELINE.md`

### Task orders addressed this session
- `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/BDPL_ASTDIM.W2.ds-super-class-recon.md`
- `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/BDPL_ASTDIM.W4.ds-build-bd-assets-dim.md`

### Deliverables
- `data/black_diamond/recon/bd_asset_super_class_values.md` (W2)
- `data/black_diamond/scripts/silver/build_bd_assets_dim.py` (W4)
- `data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py` (infra)

### Source / reference files consulted
- `data/black_diamond/scripts/gold/lib/etf_classifier.py`
- `data/black_diamond/scripts/gold/D_03.composition_artifacts.py`
- `data/black_diamond/scripts/gold/D_00b.portal_timeseries.py`
- `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`
- `data/black_diamond/scripts/gold/B_01b.classify_new_securities.py`
- `data/black_diamond/scripts/silver/convert_fees_to_silver.py` (pattern reference for WP-1)
- `data/black_diamond/scripts/silver/bd_price_update.py` (WP-11 target: `_SCOPED_PRICE_OVERRIDES`)
- `data/black_diamond/scripts/silver/inject_scoped_overrides.py`
- `data/black_diamond/scripts/diagnostics/adhc_histry_005_phantom_schwab.py` (WP-9 target)

### S3 artifacts
- `s3://opal-data-bd/silver/bd_assets.parquet` (AE-compacted txn-level, 3.45M rows)
- `s3://opal-data-bd/silver/bd_assets_dim.parquet` (W4 output, 10,937 rows) — NEW
- `s3://opal-data-bd/silver/assets/{YYYY-MM-DD}.parquet` (W3 partitioned, 1,824 dates)
- `s3://opal-data-bd/silver/allocations/2026-04-10.parquet`
- `s3://opal-data-bd/gold/firm_mix_views.json` / `firm_mix_views_daily.json`
- `s3://opal-data-bd/gold/views/firm_composition.json`
- `s3://opal-data-bd/gold/holdings_lots/2026-04-10.parquet`
- `s3://opal-data-bd/gold/dimensions/schwab_bd_account_mapping.parquet`
- `s3://opal-data-schwab/silver/RPS/date=20260410/data.parquet` (fresh this session)
- `s3://opal-data-bd/code/silver/build_bd_assets_dim.py`

---

## Session end

Both BDPL_ASTDIM tasks complete on CLOUD (`39692589`). Brief and PRDs standing for CTO / AE consumption. No MCP sent per session directive — Andrew has the commit hash + summary.
