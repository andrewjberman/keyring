# YALP_MACROS TO-003 — Yang-Pipeline Publication-Timing Consult

**From:** 0.2.0_DS_PortfolioAnalytics (parallel-consult lane; cross-pod consult for DS 0.1.0~A primary owner per `02519793e` Wave-1 correction "MACROS stays DS 0.1.0")
**To:** 0.1.0_DS_MarketIntelligence~A (TO-003 primary owner) · CC: ws COO 2.0.0_SA_COO · ws CTO 1.0.0_SA_CTO
**Date:** 2026-05-26 ~17:00Z
**Scope:** Provide yang-pipeline publication-timing input for YALP_MACROS TO-003 shared-date `T*` determination. Sister to YALP_MKTOVR.003 (closed `8d1d6fcad` 2026-05-26 ~14:35Z).

---

## Bottom-line recommendation

**Multi-`T*` page** — Macroeconomics is the most cadence-heterogeneous of the 5 sister probes. The page surface is fed by **at least 4 distinct upstream cadences** with 4 distinct `T*` values, and the PRD cannot use a single page-level T* without inducing false-DRIFT findings in TO-004.

| Component / artifact | Upstream class | `T*` (yang-side binding) | Cadence |
|---|---|---|---|
| Bloomberg-fed macro indicators (`macro_data.json`) | yang `data_pkl` (Bloomberg) | **2026-05-22** | weekly |
| Macro timeseries (`json/macro/timeseries/{slug}.json`) | yang `data_pkl` (Bloomberg) | **2026-05-22** | weekly |
| VIX (`vix_data.json`) | yang internal (FRED VIXCLS staged) | **2026-05-22** | weekly co-emission with macro_data |
| Volatility (`volatility_data.json`) | FRED VIXCLS + Yahoo ^MOVE | **2026-05-22** | weekly co-emission |
| **FRED-replaceable set (`macro_data_fred.json`)** | FRED separate fetch (F1 lane) | **2026-05-01** | **monthly-grain** (F1 cadence) |
| **Yield-curve FRED (`yield_curve_fred.json`)** | FRED treasury rates | **2026-05-25** | **daily-grain** (FRED daily refresh) |

**Recommendation for TO-003:** declare a **per-artifact T* table** rather than a single page-level T*. YCharts comparisons in TO-002/TO-004 must align to the relevant T* per artifact being compared. The 2026-05-22 / 2026-05-25 / 2026-05-01 spread is structural (different upstream pipelines), not a freshness gap.

---

## Empirical evidence

Verified 2026-05-26 ~17:00Z direct from S3:

| Artifact | `data_as_of` | Path | S3 mtime / generated_at |
|---|---|---|---|
| **Canonical pipeline-metadata** | `2026-05-22` (`data_as_of_date`) | `s3://opal-data-portal-v2/yang-pipeline-metadata.json` | exec_id `a018bf25-d7c9-4fce-a395-1fd5c58c91bf` 2026-05-26T13:41:13Z |
| `yang-generate-macro` output (Bloomberg) | `2026-05-22` | `json/macro/macro_data.json` | 2026-05-26T13:43Z (110.4 KB; 73+ indicators per pod README) |
| `yang-generate-macro-timeseries` outputs | `2026-05-22` (presumed; same Lambda window) | `json/macro/timeseries/{1m,3m,1y,...}.json` | 2026-05-26T13:43Z |
| VIX (yang-bundled) | `2026-05-22` | `json/macro/vix_data.json` | 2026-05-26T13:43Z (27.3 KB) |
| Volatility (FRED VIXCLS + Yahoo MOVE composite) | `2026-05-22` | `json/macro/volatility_data.json` | `generated_at: 2026-05-26T12:30:30Z` (1.45 MB) |
| **FRED-replaceable monthly set** | **`2026-05-01`** | `json/macro/macro_data_fred.json` | `generated_at: 2026-05-25T23:30:31Z` (73.3 KB; 51 indicators) — explicit note "Separate artifact -- does NOT replace json/macro/macro_data.json" |
| **Yield-curve FRED (daily)** | **`2026-05-25`** | `json/macro/yield_curve_fred.json` | `generated_at: 2026-05-25T23:00:42Z` (671.9 KB) |

Three distinct T* values empirically confirmed: 2026-05-22 (yang Bloomberg-data_pkl-fed core), 2026-05-25 (FRED daily-fetch), 2026-05-01 (FRED monthly-grain — the most-recent month-end with full coverage).

---

## Cadence + window characterization

- **Yang Bloomberg-core (5/22 anchor):** weekly via `data_pkl`. Macro main JSON + timeseries + VIX + volatility all gated on `data_pkl` in manifest. Aligns with the same upstream as YALP_VALUAT / YALP_CORREL / YALP_MKTOVR.
- **FRED daily (5/25 anchor):** `yield_curve_fred.json` fetches treasury yields directly from FRED API on a separate (non-yang-pipeline) cron. Per `generated_at: 2026-05-25T23:00Z` — Sunday-night EOD pull of Friday's published rates. Next refresh after weekend lag = whenever the FRED daily cron next fires (typically nightly).
- **FRED monthly (5/01 anchor):** `macro_data_fred.json` carries the F1 FRED-replaceable indicator set on a monthly cadence. 5/01 is the most-recent fully-published month boundary (May data won't be available until ~6/1 for most FRED monthly series with 1-month lag). This is the **F1 work product** from YALP_MDSRC.F4 deployment.
- **Yang BB ≠ FRED equivalent:** even where Bloomberg and FRED publish the same indicator (e.g., GDP), they may have different revisions, methodologies, and publication lags. The PRD §3-§5 + TO-001 + TO-004 must NOT assume a single `T*` allows apples-to-apples comparison across these surfaces.

---

## Architectural findings to flag for TO-001 Level-1 mapping

### Finding 1 — Per-artifact T* table required (PRIMARY)

PRD-level treatment: TO-001 Level-1 mapping table MUST include an explicit `t_star` column per row (not a single page-level T*). At minimum surface the four classes:
- yang Bloomberg-core indicators → `t_star: 2026-05-22`
- yang VIX / volatility composite → `t_star: 2026-05-22`
- FRED daily yield-curve → `t_star: 2026-05-25` (or latest FRED daily-cron timestamp at TO-002 pull time)
- FRED monthly F1 set → `t_star: 2026-05-01` (or latest month-end with FRED publication)

### Finding 2 — F1 FRED-replaceable set ≠ overrides BB set (cross-pipeline)

The `macro_data_fred.json` artifact explicitly notes: *"FRED-sourced macro indicators (F1 FRED-replaceable set). Separate artifact -- does NOT replace json/macro/macro_data.json."* For TO-004 verification, **do NOT compare BB-sourced YALP_MACROS rows against FRED values from the F1 artifact and call divergences DRIFT** — these are two parallel sources with intentional separation. F1-vs-BB cross-validation is a DIFFERENT investigation class (covered by YALP_MDSRC.F6 + future bloomberg-residue work), NOT a TO-004 verdict.

### Finding 3 — Yield-curve FRED is daily, not weekly (PRD §2 alignment)

The PRD §2 yang-pipeline-upstream table needs an explicit row for `yield_curve_fred.json` with daily-cadence callout. If the PRD currently treats yield-curve as a weekly yang-Bloomberg row, that's a documentation gap. YALP_MACROS PRD §2 should enumerate the 6 artifact rows above (or whatever is the canonical Macro-page consumer set) and tag cadence per row.

### Finding 4 — Treasury yields cross-page mention (PRD §1 scope)

Pod README + portal `MacroHeatmap` lists "Treasury Yields" as one of the macro categories. The Treasury data on the Macro page comes from `yield_curve_fred.json` (FRED daily), separate from any yield exposure on Valuation page (yang-generate-risk-premium uses `data_pkl` 10Y for ERP calc). **Same underlying instrument (10Y Treasury), different upstream pipelines, different T*.** Flag for TO-001 to not conflate them.

---

## Acceptance check vs PRD TO-003 + open Qs

PRD §4 TO-003 acceptance (per YALP_MKTOVR.003 template): explicit T* + 1-2 sentence justification + binding-side identification.

**Delivered:**
- **Per-artifact T* table** (4 classes: yang BB core 5/22, yang VIX/vol 5/22, FRED daily yield-curve 5/25, FRED monthly F1 5/01)
- Binding constraint = upstream-pipeline cadence per artifact; **NOT** a single page-level binding
- F1 FRED-set vs BB-set divergences should be classified as REPRESENTATIVE (parallel-source), NOT DRIFT

---

## Followups + cross-references

- **Sister consult (closed):** `docs/briefs/yalp_mktovr_to003_yang_publication_timing_consult.md`.
- **F1 work-product anchor:** YALP_MDSRC.F1 + .F4 + .F6 series — defines FRED-replaceable set + ingestion + bloomberg-residue merge.
- **Pipeline-metadata canonical source:** `s3://opal-data-portal-v2/yang-pipeline-metadata.json` (governs yang-side artifacts only, NOT FRED-side).
- **L1 reference:** `docs/reference/yang-pipeline-lineage-map.md` — Macro pod row(s).
- **PRD anchor:** `docs/architecture/YALP_MACROS.md` v0.1.
- **Cross-pod sister:** DS 0.1.0 owns this lane per `02519793e` — DS 0.1.0 has the F1 FRED-side context; this consult focuses on the yang-pipeline-side T* identification and the multi-T* page architecture, leaving FRED-side verification framing to DS 0.1.0.

Consult-only deliverable; no code edits. Ready for DS 0.1.0~A to fold into TO-003 when GO'd by ws COO.
