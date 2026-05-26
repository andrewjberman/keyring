# YALP_POSITN TO-003 — Yang-Pipeline Publication-Timing Consult

**From:** 0.2.0_DS_PortfolioAnalytics (parallel-consult lane; pod-affinity owner per Andrew direct correction 2026-05-26 ~16:45Z)
**To:** 0.2.0_DS_PortfolioAnalytics~C (TO-003 primary owner per Wave-1 tilde-lane correction `02519793e`) · CC: ws COO 2.0.0_SA_COO · ws CTO 1.0.0_SA_CTO
**Date:** 2026-05-26 ~17:00Z
**Scope:** Provide yang-pipeline publication-timing input for YALP_POSITN TO-003 shared-date `T*` determination per PRD v0.1 §4. Sister to YALP_MKTOVR.003 (closed `8d1d6fcad` 2026-05-26 ~14:35Z).

---

## Bottom-line recommendation

**Per-component `T*` split** — Positioning page is the only sister-probe of the 5 with a **structural multi-T* surface** because the two upstream Lambdas have **different cadences**.

| Component | Upstream artifact | `T*` (yang-side binding) | Cadence |
|---|---|---|---|
| Positioning + PositioningSummary | `json/positioning/positioning_data.json` | **2026-05-22** | weekly (model_pkl) |
| HoldingsTab | `json/positioning/holdings_attribution_data.json` | **2026-05-18** | monthly (attribution_excel) |

**Recommendation for TO-003:** declare **two T* values** explicitly — `T*_positioning = 2026-05-22` and `T*_holdings = 2026-05-18`. YCharts-side pulls in TO-002 must align to the relevant T* per component being compared. Do NOT use a single composite T*; the cadence mismatch is structural (PM uploads `attribution_excel` monthly, separate from weekly `model_pkl`).

---

## Empirical evidence

Verified 2026-05-26 ~17:00Z direct from S3:

| Artifact | `data_as_of` | Path | S3 generated_at | Cadence-source |
|---|---|---|---|---|
| **Canonical pipeline-metadata** | `2026-05-22` (`data_as_of_date`) | `s3://opal-data-portal-v2/yang-pipeline-metadata.json` | exec_id `a018bf25-d7c9-4fce-a395-1fd5c58c91bf` started 2026-05-26T13:41:13Z | weekly |
| `yang-generate-positioning` output | `2026-05-22` | `json/positioning/positioning_data.json` (gzip) | 2026-05-26T13:43:10Z | model_pkl (weekly) |
| `yang-generate-holdings-attribution` output | **`2026-05-18`** (both `as_of_date` + `data_as_of`) | `json/positioning/holdings_attribution_data.json` | `generated_at: 2026-05-19T11:37:15Z` (last regenerated 1 week ago) | attribution_excel (monthly) |
| `yang-generate-allocation-summary` output | (derived from holdings + model_pkl) | `json/positioning/allocation_summary.json` | 2026-05-26T13:43:14Z | model_pkl trigger (consumes prior-run holdings) |
| `yang-generate-etf-returns` output | `2026-05-22` | `json/benchmarks/etf_returns.json` | 2026-05-26T13:43:08Z | model_pkl (weekly) |

The 2026-05-19 mtime on `holdings_attribution_data.json` (NOT regenerated in today's 2026-05-26T13:41Z pipeline run) is decisive: `attribution_excel` was not in today's manifest, so the holdings-attribution branch did not re-execute. The 2026-05-18 `data_as_of` was the value at the May monthly upload window.

---

## Cadence + window characterization

- **`model_pkl` frequency:** weekly. Triggers `yang-generate-positioning`, `yang-generate-etf-returns`, `yang-generate-allocation-summary` (per pod README §"Key Step Functions branches" — model_pkl branch).
- **`attribution_excel` frequency:** **monthly**. Triggers `yang-generate-holdings-attribution` only (per pod README same section). The May upload landed 2026-05-19; the next is expected mid-June (~2026-06-15 to 2026-06-22 historical pattern).
- **Cross-dependency note:** `yang-generate-allocation-summary` reads `holdings_attribution_data.json` from S3 (previous run) + the current `model_pkl`. Per pod README + yang-v2.1.5 SFN reorder (commit `03cfdd66`), allocation-summary now runs AFTER holdings-attribution in same-manifest runs. **But on today's run, attribution_excel was NOT in the manifest**, so allocation-summary picked up the existing 2026-05-18-as_of holdings file. Allocation-summary's effective `data_as_of` is therefore **composite** — weights from 5/22 model_pkl × allocation breakdown from 5/18 holdings.

---

## Architectural findings to flag for TO-001 Level-1 mapping

### Finding 1 — T*_holdings ≠ T*_positioning (REQUIRES PRD treatment)

PRD §2 + §4 implicitly assume single T* for the page. The 4-day gap (5/22 vs 5/18) is structural; treating it as a single T* will produce a misleading verdict in TO-004 (e.g., comparing YCharts 5/22 prices against Yang 5/18 holdings would falsely flag positioning drift that is purely cadence-driven).

**Recommendations:**
- TO-001 Level-1 mapping table: add explicit `t_star` column per row (not a single page-level T*).
- TO-002 YCharts pulls: align per-component — pull 5/22 for positioning-comparable surfaces, pull 5/18 (or the nearest YCharts-available date ≤5/18) for holdings-comparable surfaces.
- TO-004 verdict logic: when a comparison spans both components, document the T* of each side and treat cadence-mismatched fields as **REPRESENTATIVE-class** (not DRIFT) unless the same-T* comparison also shows divergence.

### Finding 2 — Allocation-summary composite T* (cross-cadence artifact)

`json/positioning/allocation_summary.json` is a **composite-T* artifact** (weights @5/22 × breakdown @5/18). For TO-001 sourcing-column, document as: `t_star_weights: 2026-05-22 / t_star_breakdown: 2026-05-18 / methodology: composite per yang-generate-allocation-summary; allocation-summary inherits prior-run holdings when attribution_excel not in current manifest`. Avoid asserting a single date for this artifact.

### Finding 3 — GAP-heavy verdict profile (PRD §5 Q1; confirmed)

PRD §5 Q1 expected ~50-70% of Positioning fields as GAP-class (Yang/BD-internal allocation metadata, ETF DynamoDB classifications, cross-pipeline `aum-metrics.json`). **Confirmed empirically:** `holdings_attribution_data.json` portfolio entries contain Yang-internal `code`, `name`, Fund Selection / Style Allocation / Asset Allocation breakdowns — all derived from `attribution_excel` (Yang/PM-internal workbook), no YCharts equivalent. PRD §5 Q1 lean (document-GAP-with-methodology) is the right approach; v1 deliverable does NOT require YCharts-portfolio-analytics synthesis.

### Finding 4 — `aum-metrics.json` cross-pipeline cite (PRD §5 Q2)

PRD §5 Q2 flagged cross-pipeline BD `aum-metrics.json` dependency for portal portfolio AUM rollups. **Confirmed:** positioning_data.json header references `data_pkl + model.pkl + cross-pipeline aum-metrics.json`. BD-side derivation is out-of-YALP-scope; TO-001 sourcing column should cite as `BD-pipeline-internal (out-of-scope per PRD §5 Q2)`.

---

## Acceptance check vs PRD §4 TO-003 + §5 open Qs

PRD §4 TO-003 acceptance: explicit T* + 1-2 sentence justification + binding-side identification.

**Delivered:**
- **Two T* values:** `T*_positioning = 2026-05-22` (yang weekly model_pkl) + `T*_holdings = 2026-05-18` (yang monthly attribution_excel from 2026-05-19 PM upload window)
- Binding constraint = both yang-side; YCharts is not the binding constraint for any component
- **PRD §5 Q1 (GAP-heavy verdict framing):** CONFIRMED — document-GAP-with-methodology is correct lean; MATCH-class index-return subset is the actual cutover-trust signal
- **PRD §5 Q2 (cross-pipeline `aum-metrics.json`):** CONFIRMED — cite-only in sourcing column; out-of-scope verification

---

## Followups + cross-references

- **Sister consult (closed):** `docs/briefs/yalp_mktovr_to003_yang_publication_timing_consult.md`.
- **Pipeline-metadata canonical source:** `s3://opal-data-portal-v2/yang-pipeline-metadata.json`.
- **Future sister:** Attribution page YALP probe (shares `holdings_attribution_data.json` + `allocation_summary.json`) will inherit the same dual-T* structure surfaced here.
- **L1 reference:** `docs/reference/yang-pipeline-lineage-map.md` — Positioning + Attribution pod rows.
- **PRD anchor:** `docs/architecture/YALP_POSITN.md` v0.1.

Consult-only deliverable; no code edits. Ready for DS 0.2.0~C to fold into TO-003 when GO'd by ws COO.
