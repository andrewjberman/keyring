# DS~B Session 2 — MDPF_ASSETS.005 WS-D.1 PFDE/PFOE net-assets + holdings ingestion

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-18
**TO:** MDPF_ASSETS.005 (from 2.0.0_SA_COO) — WS-D.1 build
**Project:** MDPF_ASSETS (Opal Aggregate AUA)
**Branch:** CLOUD

## Context

WS-D.1 — DIVZ/IDVZ ETF net-assets flow daily through the ETFS_NETAST TrueShares
probe (`etf_netassets_watch/etf_probe.py`); PFDE/PFOE do not. This TO extends that
probe with a Filepoint issuer-CSV source for the two missing Pathfinder ETFs, and —
per Andrew's 2026-05-18 directive — adds a day-over-day LINE-ITEM holdings record so
the later WS-D.2 ownership decomposition has history from day one. Build spec:
DS~A's MDPF_ASSETS.002 feasibility brief.

## Phase 0 — file-mix + net-assets-method decision record

Verified the live Filepoint CSVs (`FilepointOpalCap.40O6.O6_*`, underscore-joined —
note: `_ETF_Holdings.csv` / `_DailyNAV.csv`, not `/`):

| File | HTTP | Carries | Today's vintage |
|------|------|---------|-----------------|
| `ETF_Holdings.csv` | 200 (14.1KB) | 107 line items both funds; per-row NetAssets + SharesOutstanding; Date | **05/18/2026** (fresh) |
| `DailyNAV.csv` | 200 (548B) | fund-level NAV, Market Price, premium/discount; Rate Date | 05/15/2026 (T-1) |

**Decisions:**
1. **File mix — pull BOTH.** `ETF_Holdings.csv` is the holdings + NetAssets + SharesOutstanding source; it has no fund-level NAV/market-price, so `DailyNAV.csv` is still pulled for `nav` / `market_price`. DailyNAV is NAV-struck post-close so it typically trails the holdings file by one trading day — each value keeps its own `*_as_of` stamp, so the mixed-vintage row is explicit, never silent.
2. **Net-assets SoR — `ETF_Holdings.csv` `NetAssets`** (per Andrew/DS~A gap 3). DailyNAV's `Net Assets` is a cross-check (differs ~$192 on PFDE — different strike vintage).
3. **Reconciliation — `sum(per-holding MarketValue)` vs `NetAssets`**, computed + surfaced in the row `note`, never silently absorbed. The holdings file includes the fund's cash line(s) (FXFXX money-market + Cash&Other), so the sum is near-exact; today PFDE delta -$2,111 (-0.0016%), PFOE -$1,630 (-0.0015%). A widening residual is a data-quality signal.
4. **MSN fallback — msn_id=None for PFDE/PFOE.** MSN's Searches endpoint 404'd; and DS~A established third-party aggregators are materially stale on these funds (~22% off). A stale MSN figure would be worse than a provenance-flagged carry-forward — so the carry-forward tiers, not MSN, are the PFDE/PFOE resilience layer. `fetch_msn` guards on missing msn_id and raises cleanly, so Tier 3 is a no-op for them and the ladder falls to Tier 4.

## Phase 1 — build

Extended `etf_netassets_watch/etf_probe.py` (two-issuer probe):

- `FUNDS` — added `pfde`/`pfoe` with `source_kind="filepoint"` + `filepoint_account`; `divz`/`idvz` gained `source_kind="trueshares"` (existing tier untouched).
- `fetch_filepoint()` — new Tier-1: GET `ETF_Holdings.csv` (net-assets SoR + holdings line items) + `DailyNAV.csv` (NAV/price, best-effort — a DailyNAV failure does not fail the tier). `_filepoint_csv()` caches per-process (one GET per file serves both funds) and asserts the expected header (a silent schema change → Tier-1 failure, gap 2).
- `resolve_fund()` — Tier 1 branches on `source_kind`; Tiers 2-3 measure staleness / carry-forward against the SAME issuer (`live_source`); Tier 4 set extended with `filepoint` + `filepoint_carryforward`.
- Day-over-day holdings artifact — `HOLDINGS_COLUMNS` schema; `write_holdings_day()` → `holdings/{date}.parquet` + S3 `silver/holdings/{date}.parquet`. One row per (date, fund, holding): ticker, CUSIP, security name, shares, price, market value, weight %, is_cash, fund net-assets/shares, data-as-of. `build_rows()` pops the line items off the netassets rows so they never bloat the history CSV / snapshot.
- `probe_row_to_parquet()` — `net_assets` now falls back to `net_assets_reported` when `market_value_computed` is None (a filepoint row whose best-effort DailyNAV draw was missing still has an exact NetAssets — fewer nulls, no behavior change for rows with a price).
- Gaps 1-4 carried: (1) no fabricated history — the true net-assets + holdings series starts at the first probe run; (2) header-assert + non-200 → Tier-1 failure → fall-through; (3) holdings-file NetAssets is SoR; (4) ladder per-fund / two-issuer.

ds-commit-gate clean (py_compile + AST scan + ruff py39). No emoji, ASCII-only.

## Phase 2 — verification

Ran `python etf_probe.py` end-to-end (committed-code probe = the gate mechanism):

| Fund | Source | Net assets | vs 05-15 refs | As-of |
|------|--------|-----------:|---------------|-------|
| DIVZ | trueshares | $241.85M | unaffected | 2026-05-15 |
| IDVZ | trueshares | $158.66M | unaffected | 2026-05-15 |
| PFDE | filepoint | **$131,630,541** | coworker $131.52M (+0.08%), DS~A $131.63M (~0%) — both <1% | 2026-05-18 |
| PFOE | filepoint | **$110,854,025** | coworker $111.33M (-0.43%), DS~A $110.40M (+0.41%) — both <1% | 2026-05-18 |

- Holdings artifact: `holdings/2026-05-18.parquet` — 107 line items (PFDE 84, PFOE 23), correct dtypes, cash lines flagged.
- Reconciliation surfaced in the row note (PFDE -0.0016%, PFOE -0.0015%).
- DIVZ/IDVZ TrueShares tier unaffected — still produced.
- All 5 S3 uploads OK incl. the new `s3://opal-data-etfs/silver/holdings/2026-05-18.parquet`.

AC1-AC5 all PASS.

## Files Modified

| File | Change |
|------|--------|
| etf_netassets_watch/etf_probe.py | Filepoint Tier-1 source + pfde/pfoe FUNDS + per-fund source_kind ladder + day-over-day holdings artifact |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/MDPF_ASSETS.005.dsb-wsd1-pfde-pfoe-netassets-holdings-ingestion.md | status -> complete |
| org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-18/DS_B_session2_mdpf_assets_005_pfde_pfoe_ingestion.md | New — this session log |

S3 (not git — opal-data-etfs is the canonical store, code-only is tracked):
`silver/netassets/2026-05-18.parquet`, `silver/netassets_daily.parquet`, `silver/holdings/2026-05-18.parquet`, `snapshots/snapshot_2026-05-18.json`, `etf_history.csv`.

## Compiler Tools

| Tool | Result |
|------|--------|
| comp-* graph tools | N/A — WS-D.1 extends a local off-the-books probe (`etf_netassets_watch/`), not a pipeline-graph node. Per the TO compiler mandate, stated N/A. |
| Phase-0 source verification | Direct HTTPS GET of the live `ETF_Holdings.csv` + `DailyNAV.csv` (DS~A's MDPF_ASSETS.002 method) — headers confirmed, both funds present, cadence checked. |
| `.tools/ds-commit-gate.sh etf_probe.py` | PASS — py_compile + ds-precommit-check + ruff py39. |
| Phase-3 end-to-end | `python etf_probe.py` — 4/4 funds resolved Tier 1, holdings artifact materialized, S3 uploads OK. |

## Cross-domain note

`etf_netassets_watch/etf_probe.py` is co-owned with ETFS_NETAST. `.owned-paths.yaml` has
no rule for `etf_netassets_watch/**` (known ETFS_NETAST open item) — see the commit note
re: the safe-commit path used. New S3 prefix `silver/holdings/` added — flagged to AE 0.7.0
(ETFS_NETAST.001 owns the opal-data-etfs Terraform adoption); adding objects/prefixes does
not affect the bucket-resource import.

## Current State

MDPF_ASSETS.005 COMPLETE — PFDE/PFOE net-assets + day-over-day holdings ingestion live;
DIVZ/IDVZ unaffected. AC1-AC5 PASS. RAVC2 to COO on commit.

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — MDPF_ASSETS.005 complete. The holdings artifact (`silver/holdings/`) is the durable record WS-D.2 (ETF ownership decomposition) consumes. |
| **AE 0.7.0** | New `silver/holdings/` prefix under opal-data-etfs — heads-up for the ETFS_NETAST.001 Terraform adoption object census (does not affect the bucket import). |
| **CTO 1.0.0** | `.owned-paths.yaml` `etf_netassets_watch/**` path rule is still an open ETFS_NETAST item — second agent (DS~B) has now hit it. |
