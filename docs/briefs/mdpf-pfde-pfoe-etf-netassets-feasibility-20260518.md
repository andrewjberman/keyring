# MDPF_ASSETS WS-D.1 — PFDE / PFOE ETF Net-Assets Source Feasibility

**Finding brief — Phase 0 (investigation)**
**TO:** MDPF_ASSETS.002 (`dsa-pfde-pfoe-etf-netassets-source-feasibility`)
**Author:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-18
**PRD:** `docs/architecture/MDPF_ASSETS.md` v0.1 — §3.3, §4 WS-D.1, §7 Q4

---

## Verdict — one line

**PFDE and PFOE are NOT TrueShares funds.** They are **Pathfinder ETFs**, and their net-assets data is available as a **clean public CSV** (`pathfinderetfs.com/assets/data/FilepointOpalCap.40O6.O6_DailyNAV.csv`) carrying every field the `ETFS_NETAST` probe needs. The probe's *architecture* replicates; its *Tier-1 acquisition mechanism does not* — Pathfinder is a structured CSV download, not an HTML regex-scrape. The CSV path is **simpler and more robust** than the existing TrueShares scrape. **SHIP-feasible** at Phase 1.

---

## AC1 — PFDE / PFOE net-assets source CONFIRMED

### The funds

| Ticker | Fund name | CUSIP | Inception | Issuer brand |
|--------|-----------|-------|-----------|--------------|
| PFDE | Pathfinder Disciplined US Equity ETF | 75526L670 | 2025-12-30 | Pathfinder ETFs |
| PFOE | Pathfinder Focused Opportunities ETF | 75526L688 | 2025-12-30 | Pathfinder ETFs |

PFDE/PFOE are **not** on the TrueShares platform. `https://www.true-shares.com/etf/pfde` and `.../pfoe` both return **HTTP 404** (verified 2026-05-18). The TrueShares slug pattern still works for DIVZ/IDVZ (`.../etf/divz` returns the live fund page) — so the 404 is fund-specific, not a sitewide change. DIVZ/IDVZ = "Polen Dividend Income ETF" family on TrueShares; PFDE/PFOE = a separate issuer.

### The source — Pathfinder / Filepoint daily CSV

The Pathfinder fund pages (`pathfinderetfs.com/pfde`, `/pfoe`) are **template HTML with placeholder values** (`XX.XX`, `XX/XX/XXXX`) — the real numbers are loaded client-side by `assets/js/app.js`, which `$.ajax`-GETs a set of CSV files. The site is built on the **Filepoint** ETF-website platform; the data files are namespaced `FilepointOpalCap.40O6.O6_*` ("OpalCap" = Opal Capital — these are confirmed Opal's funds).

**Canonical net-assets source — one CSV covers both funds:**

```
https://pathfinderetfs.com/assets/data/FilepointOpalCap.40O6.O6_DailyNAV.csv
```

| Field | Mechanism | Cadence |
|-------|-----------|---------|
| Access | Plain HTTPS GET, public, no auth, no JS needed | — |
| Format | CSV, header row + one row per fund (PFDE, PFOE) | — |
| Refresh | Post-close, after the NAV strike | Daily (trading days) |

**`DailyNAV.csv` columns (verified 2026-05-18, Rate Date 05/15/2026):**

`Fund Name, Fund Ticker, CUSIP, Net Assets, Shares Outstanding, NAV, NAV Change Dollars, NAV Change Percentage, Market Price, Market Price Change Dollars, Market Price Change Percentage, Premium/Discount Percentage, Rate Date, Median 30 Day Spread Percentage`

| Ticker | Net Assets | Shares Outstanding | NAV | Market Price | Rate Date |
|--------|-----------:|-------------------:|----:|-------------:|-----------|
| PFDE | $131,630,348.84 | 4,830,000 | 27.2527 | 27.2736 | 05/15/2026 |
| PFOE | $110,396,808.72 | 4,830,000 | 22.8565 | 22.8783 | 05/15/2026 |

This CSV carries **all four fields the `ETFS_NETAST` probe records** — `net_assets`, `shares_outstanding`, `nav`, `market_price` — plus the per-row `Rate Date` (the data-vintage / "as of" stamp). It is a strictly richer source than the TrueShares HTML scrape, with no layout-change fragility.

### Companion Filepoint CSVs (same prefix, same host)

| File | Content | Relevance |
|------|---------|-----------|
| `..._DailyNAV.csv` | Current day NAV/net-assets/shares, both funds | **WS-D.1 primary source** |
| `..._DailyNAVHistorical.csv` | NAV + Market Price + Premium/Discount, both funds, from inception 2025-12-30 (191 rows) | WS-D.1 backfill — **see gap below** |
| `..._ETF_Holdings.csv` | Per-holding line items, both funds (PFDE + PFOE), with per-row `NetAssets` + `SharesOutstanding`; Date 05/18/2026 | **WS-D.2** ownership decomposition (`held_partner`) — out of scope here, but noted: clean line-item holdings exist |
| `..._MonthlyPerformance.csv` / `..._QuarterlyPerformance.csv` | Return series | Not needed for net-assets |

### Third-party aggregators are stale — do not use

Investing.com / Yahoo carry PFDE/PFOE but with materially stale net-assets (e.g. Investing.com showed PFOE AUM ≈ $104.68M vs the issuer CSV's $110.40M; web search returned PFDE ≈ $102.91M vs the issuer's $131.63M). The Pathfinder/Filepoint CSV is the authoritative, current source.

---

## AC2 — Feasibility verdict: does the `ETFS_NETAST` probe structure replicate?

**Architecture replicates; Tier-1 mechanism does not. Net assessment: feasible and lower-risk than the existing TrueShares tier.**

`etf_netassets_watch/etf_probe.py` is a per-fund **source ladder** (Tier 1 TrueShares HTML scrape → Tier 2 carry-forward → Tier 3 MSN API → Tier 4 stale carry-forward → Tier 5 null) writing a unified row schema to `etf_history.csv` + per-day parquet + consolidated `silver/netassets_daily.parquet` + JSON snapshot, all pushed to `s3://opal-data-etfs/`.

| Probe element | Replicates for PFDE/PFOE? | Note |
|---------------|---------------------------|------|
| Per-fund `FUNDS` config list | YES | Add `pfde` / `pfoe` entries |
| Tier 1 acquisition | **NO — different mechanism** | TrueShares = regex-scrape of `true-shares.com/etf/{slug}` static HTML. Pathfinder = direct CSV GET of `FilepointOpalCap.40O6.O6_DailyNAV.csv`. A **new source function** (`fetch_filepoint`) is required — CSV parse, not HTML regex. **Easier**: structured columns, no `TS_PATTERNS` layout fragility. |
| One fetch → both funds | YES (improvement) | The single `DailyNAV.csv` carries PFDE + PFOE — one HTTP call covers both, vs TrueShares' one-page-per-fund. |
| Tier 3 MSN fallback | YES (as-is) | MSN is ticker-generic; PFDE/PFOE are public NASDAQ tickers. Needs each fund's MSN `msn_id` (looked up once). Same caveat as today: MSN net-assets is month-end, price is live. |
| Carry-forward tiers (2, 4) | YES (as-is) | Source-agnostic — operate on `etf_history.csv` rows. |
| Row schema / parquet / snapshot / S3 layout | YES (as-is) | `CSV_FIELDS` / `PARQUET_COLUMNS` are source-neutral; `source` tag just gains a `filepoint` value. |
| `net_assets_as_of` stamp | YES | Map from the CSV `Rate Date` column (already an explicit data-vintage field — cleaner than TrueShares' "As of:" HTML anchor). |

### Gaps / risks to carry into the WS-D.1 Phase-1 build TO

1. **Historical net-assets backfill is partial.** `DailyNAVHistorical.csv` carries NAV + Market Price from inception (2025-12-30) but **no `Net Assets` and no `Shares Outstanding`**. The probe's `net_assets` is `nav × shares` — so historical net-assets cannot be reconstructed exactly without a historical shares series (and shares-outstanding for a 4.5-month-old fund moves with creation units). Phase-1 options: (a) backfill NAV-only history and start the true net-assets series from the first daily-probe run; (b) treat history net-assets as `NAV × current shares` approximation, flagged `inferred=true`. Recommend (a) — consistent with the probe's `inferred` provenance discipline; the funds are young so the lost history is small.
2. **URL embeds a Filepoint client code** (`40O6.O6`). If Filepoint rotates the namespace the URL breaks silently. Phase-1: treat a non-200 / schema-mismatch as a Tier-1 failure that falls through to the MSN tier, and assert the expected header row.
3. **`net_assets` definition differs slightly across the two Filepoint files.** `DailyNAV.csv` `Net Assets` (NAV-struck, Rate Date 05/15) = $131,630,348.84 for PFDE; `ETF_Holdings.csv` `NetAssets` (holdings-sum, Date 05/18) = $131,630,541.00. Use `DailyNAV.csv` as the net-assets system-of-record; `ETF_Holdings.csv` is for WS-D.2 line-item attribution only.
4. **DIVZ/IDVZ stay on the TrueShares tier.** The probe becomes two-issuer: DIVZ/IDVZ → TrueShares scrape; PFDE/PFOE → Filepoint CSV. Keep the source ladder per-fund (it already is) and branch Tier 1 on a per-fund `source_kind` key.

---

## Concrete paths for the WS-D.1 Phase-1 build TO

| Input | Path / mechanism |
|-------|------------------|
| PFDE/PFOE daily net-assets (primary) | `GET https://pathfinderetfs.com/assets/data/FilepointOpalCap.40O6.O6_DailyNAV.csv` — CSV, both funds, daily post-close |
| PFDE/PFOE history (NAV/price only) | `GET https://pathfinderetfs.com/assets/data/FilepointOpalCap.40O6.O6_DailyNAVHistorical.csv` — from 2025-12-30 |
| PFDE/PFOE holdings (WS-D.2) | `GET https://pathfinderetfs.com/assets/data/FilepointOpalCap.40O6.O6_ETF_Holdings.csv` — line items + per-row net-assets/shares |
| Probe to extend | `etf_netassets_watch/etf_probe.py` — add a `fetch_filepoint(fund)` Tier-1 source + `pfde`/`pfoe` `FUNDS` entries with `source_kind="filepoint"` |
| Output (unchanged) | `s3://opal-data-etfs/silver/netassets/{date}.parquet`, `silver/netassets_daily.parquet`, `snapshots/`, `etf_history.csv` — schema already source-neutral |
| Fallback | MSN Tier-3 (`msn_id` per fund, looked up once) — covers a Filepoint outage |

**Phase-1 effort:** small. One new ~40-line CSV-source function, two `FUNDS` entries, a per-fund `source_kind` branch in `resolve_fund`. No schema change, no new S3 layout. The off-the-books probe graduating to managed is tracked separately under `ETFS_NETAST` (Terraform-adoption of `opal-data-etfs`).

---

## Compiler Tools

| Tool | Result |
|------|--------|
| `aws s3 ls s3://opal-data-etfs/snapshots/` + `silver/` (TO Phase-0 mandate) | `snapshots/snapshot_2026-05-15.json` (DIVZ/IDVZ, last trading day — weekend gap, not stale); `silver/netassets_daily.parquet` + `silver/netassets/{date}.parquet` 2025-05-30 → 2026-05-15 present. The `ETFS_NETAST` DIVZ/IDVZ probe template is live and healthy — confirmed as the replication baseline. |

No `comp-*` graph tool applies — this is an external-source feasibility probe, not a pipeline-graph trace. The empirical probes were direct HTTPS GETs of the issuer sites + the live `DailyNAV.csv`.

---

## Recommendation to COO

**SHIP-feasible.** Author the WS-D.1 Phase-1 build TO: extend `etf_netassets_watch/etf_probe.py` with a Filepoint CSV Tier-1 source for PFDE/PFOE. The source is confirmed, public, daily, and structurally cleaner than the existing TrueShares scrape. Carry gaps 1-4 above into the build TO's scope. The build TO co-owns `etf_probe.py` with `ETFS_NETAST` — needs a `<cross_domain_coordination>` block per PRD §6.4.
