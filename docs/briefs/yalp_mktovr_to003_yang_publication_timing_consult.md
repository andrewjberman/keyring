# YALP_MKTOVR TO-003 — Yang-Pipeline Publication-Timing Consult

**From:** 0.2.0_DS_PortfolioAnalytics (parallel-consult lane per ws COO /allocation #3)
**To:** 0.1.0_DS_MarketIntelligence (TO-003 primary owner) · CC: ws COO 2.0.0_SA_COO · ws CTO 1.0.0_SA_CTO
**Date:** 2026-05-26 ~14:55Z
**Scope:** Provide yang-pipeline `data.pkl` + `model.pkl` publication-timing input for TO-003 shared-date `T*` determination per YALP_MKTOVR PRD v0.1 §3.2 + §6.

---

## Bottom-line recommendation

**`T* = 2026-05-22`** (Friday before this consult). Yang-side binding constraint; verified empirically.

Justification: yang-pipeline weekly cadence; pipeline executed today 2026-05-26T13:41Z (~75min before this consult) emitting `data_pkl.data_as_of = 2026-05-22` and `model_pkl.data_as_of = 2026-05-22`. All downstream yang-side artifacts carry the same `data_as_of`. 2026-05-23/24 = weekend; 2026-05-25 = Memorial Day (US market closed); 2026-05-26 EOD not yet published. So 2026-05-22 is the most-recent business day with full yang-side coverage AND the binding constraint vs. any YCharts-side alternative for the universe in scope.

---

## Empirical evidence — yang-side `data_as_of = 2026-05-22`

Verified 2026-05-26 ~14:50Z direct from S3 + DynamoDB:

| Artifact | `data_as_of` | Path / source | S3 mtime |
|---|---|---|---|
| `data_pkl` (PM upload) | `2026-05-22` | `s3://opal-data-portal-v2/uploads/data 20260522 v1.pkl` | uploaded 2026-05-26T13:41Z |
| `model_pkl` (PM upload) | `2026-05-22` | `s3://opal-data-portal-v2/uploads/model 20260522 v1.pkl` | (same pipeline exec) |
| Pipeline run | exec id `a018bf25-d7c9-4fce-a395-1fd5c58c91bf` | `json/latest/manifest.json` | started 2026-05-26T13:41:13Z |
| `yang-generate-positioning` output | `2026-05-22` | `json/positioning/positioning_data.json` | written 2026-05-26T09:43Z |
| `yang-generate-valuation` output | `2026-05-22` | `json/valuation/valuation_data.json` | (same window) |
| `market-rsi-tiered-generator` Tier-1 | `2026-05-22` (`last_updated`) | `json-tiered/market-overview/rsi-summary.json` | written 2026-05-26T13:44:17Z |
| `market-overview-tiered-generator` Tier-1 | `2026-05-22` (`latest_date` per-index) | `json-tiered/market-overview/summary/all-returns.json` | written 2026-05-26T13:44:21Z |

All page-mount + Tier-1 surfaces consistent: T* = 2026-05-22 is the yang-side anchor today.

---

## Cadence + window characterization

- **`data_pkl` / `model_pkl` frequency:** weekly (per `json/latest/manifest.json` `frequency: "weekly"` for both).
- **PM upload timing:** typical pattern is "this week's Monday-or-Tuesday upload covers prior-Friday data_as_of." Today (Tuesday 2026-05-26) upload at 13:41Z (~09:41 ET) carries Friday 2026-05-22 as_of. The intervening Memorial Day (Mon 2026-05-25) is consistent with the Tuesday-rather-than-Monday upload landing.
- **`attribution_excel` (monthly):** `data_as_of = 2026-05-18` per manifest — separate cadence; in scope only for Positioning/Attribution pages, NOT for Market Overview. Not a `T*` constraint for YALP_MKTOVR.
- **Next likely yang-side publication:** if PM uploads continue Monday cadence, next refresh would be 2026-06-01 (Monday) carrying `data_as_of = 2026-05-29` (Friday); week thereafter 2026-06-08 / 2026-06-05; etc. Probe window is point-in-time on T* = 2026-05-22 per PRD §1 "point-in-time snapshot."

---

## Architectural finding to flag for TO-001 Level-1 mapping

**PRD v0.1 §2.3 names the data flow as `yang-pipeline → json/*.json → market-overview pipeline → json-tiered/market-overview/*.json`.** Empirical inspection of `json-tiered/market-overview/summary/all-returns.json` shows:

```
"data_source": "DynamoDB:opal-portal-market-data"
```

The market-overview pipeline's Tier-1 generator reads from **DynamoDB `opal-portal-market-data`** (not directly from `json/*.json` yang-side output). The L1 yang-pipeline-lineage-map (DS 0.1.0's deliverable from YALP_MDSRC, `docs/reference/yang-pipeline-lineage-map.md`) confirms upstream: **`yang-ingest-dynamodb`** Lambda reads `data_pkl` and writes `DAILY#`/`LATEST` rows to `opal-portal-market-data` + the signature artifact `json/latest/data_pkl.json`. That DDB table is then the *direct* upstream of the market-overview tiered generators.

**Implication for TO-001 Level-1 mapping (DS 0.1.0 primary):** the `market-overview pipeline producer` column should populate two-layer:

```
yang-pipeline upstream producer:  yang-ingest-dynamodb (writes DDB opal-portal-market-data)
                                  ↓
intermediate:                     DynamoDB opal-portal-market-data (DAILY# rows per ticker_id)
                                  ↓
market-overview pipeline:         market-overview-tiered-generator + market-rsi-tiered-generator + ...
                                  ↓
Portal endpoint:                  /api/general/json-tiered/market-overview/*
```

This DOES NOT change `T*` (DDB is keyed by `data_key=DAILY#YYYY-MM-DD`; the latest `2026-05-22` row reflects the same yang-side data state). It DOES affect how each Level-1 row is populated — specifically, the "Yang-processed PKL field" column should resolve via the L1 atomic-field-grain rubric for `data_pkl`'s emitted DDB columns (price, daily_return, etc.) rather than via `json/positioning/*` or `json/valuation/*` paths (those are different pages' yang-side outputs).

Other pages in pod (Positioning / Valuation / FactorTilts / Macro / Correlation) DO use `json/<page>/*.json` directly via separate `yang-generate-<page>` Lambdas — that PRD §2.3 description fits them. Market Overview is the DDB-intermediated branch.

**Not a blocker for TO-003.** Surfaced here so TO-001's Level-1 column populator doesn't get crossed up. Up to DS 0.1.0 to decide whether to amend PRD §2.3 wording or just thread the nuance into TO-001 itself.

---

## YCharts-side considerations (informational; TO-002's domain, not mine)

For DS 0.1.0's TO-002 to confirm — these are checkable from your side, not yang-side:

1. **2026-05-22 YCharts availability:** Friday EOD; standard ticker universe should be present (indices + general_data). High confidence.
2. **Memorial Day Mon 2026-05-25:** US market closed; YCharts will not have 2026-05-25 rows for US equity indices (foreign indices may have alternate-day data). Skip 2026-05-25.
3. **Tue 2026-05-26 EOD:** YCharts typically publishes T+1 EOD by ~next-day-morning. Today 14:55Z (~10:55 ET) is mid-trading-day; 2026-05-26 EOD will not be available until tomorrow morning ET earliest. So 2026-05-26 is NOT a T* candidate today.
4. **Per-asset-class fall-back (PRD §9 risk row):** if any specific asset class shows a yang-vs-YCharts publication-window mismatch for 2026-05-22, route via per-asset-class T* with explicit reasoning. Lean: not needed for 2026-05-22 (all asset-class universes had Friday EOD).

---

## Acceptance check vs PRD §6 TO-003

PRD §6 TO-003 acceptance: *"explicit T* value documented + 1-2 sentence justification (which side was the binding constraint)."*

My side delivers: `T* = 2026-05-22`; binding constraint = yang-pipeline weekly cadence (`data_pkl` + `model_pkl` `data_as_of`), confirmed at pipeline_execution_id `a018bf25-d7c9-4fce-a395-1fd5c58c91bf` 2026-05-26T13:41Z. Earlier business-day candidates (2026-05-15) are stale data; later (2026-05-29) is the next yang-side publication date — future. 2026-05-22 is the unique current-window answer.

DS 0.1.0 confirms YCharts-side coverage; if YCharts has 2026-05-22 published for the relevant ticker universe (high prior), TO-003 closes with `T* = 2026-05-22`. If a specific ticker subset is YCharts-stale at 2026-05-22, fall to per-asset-class T* per PRD §9.

---

## Followups + cross-references

- **Predecessor:** YALP_MDSRC D2/D3 (closed `b8a6e83bf` 2026-05-22) — surface-level mapping; this project's TO-001 Level-1 builds on it.
- **L1 reference:** `docs/reference/yang-pipeline-lineage-map.md` — `yang-ingest-dynamodb` row confirms DDB-intermediate layer.
- **Yang-pipeline manifest:** `s3://opal-data-portal-v2/json/latest/manifest.json` is the canonical freshness signature; cite in TO-003 deliverable.
- **PRD anchor:** YALP_MKTOVR.md commit `63439b288` v0.1 — TO-003 §6 row.

Consult-only deliverable; no code edits. Ready for DS 0.1.0 to fold into TO-003 when GO'd by ws COO.
