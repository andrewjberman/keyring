# YALP_CORREL TO-003 — Yang-Pipeline Publication-Timing Consult

**From:** 0.2.0_DS_PortfolioAnalytics (parallel-consult lane; pod-affinity owner per Andrew direct correction 2026-05-26 ~16:45Z routing Pod 2 pages to DS 0.2.0 variants)
**To:** 0.2.0_DS_PortfolioAnalytics~B (TO-003 primary owner per Wave-1 tilde-lane correction `02519793e`) · CC: ws COO 2.0.0_SA_COO · ws CTO 1.0.0_SA_CTO
**Date:** 2026-05-26 ~17:00Z
**Scope:** Provide yang-pipeline publication-timing input for YALP_CORREL TO-003 shared-date `T*` determination. Sister to YALP_MKTOVR.003 (closed `8d1d6fcad` 2026-05-26 ~14:35Z).

---

## Bottom-line recommendation

**`T* = 2026-05-22`** (Friday before this consult). Yang-side binding constraint; verified empirically.

Correlation page is the cleanest of the 5 sister probes — single Lambda (`yang-generate-correlation`), single S3 artifact, single `data_as_of` header, single cadence (weekly with `data_pkl`).

---

## Empirical evidence — yang-side `data_as_of = 2026-05-22`

Verified 2026-05-26 ~17:00Z direct from S3:

| Artifact | `data_as_of` | Path | S3 generated_at |
|---|---|---|---|
| **Canonical pipeline-metadata** | `2026-05-22` (`data_as_of_date`) | `s3://opal-data-portal-v2/yang-pipeline-metadata.json` | exec_id `a018bf25-d7c9-4fce-a395-1fd5c58c91bf` started 2026-05-26T13:41:13Z |
| `yang-generate-correlation` output | `2026-05-22` | `json/correlations/correlation_data.json` | `metadata.generated_at: 2026-05-26T13:43:07.872043Z` |

Header confirms `ticker_count: 59` + `periods_available: ["1M", "3M", "6M", "1Y", "2Y"]`.

---

## Cadence + window characterization

- **`data_pkl` frequency:** weekly. `yang-generate-correlation` gates on `data_pkl` presence in the manifest (per pod README §"Key Step Functions branches" — data_pkl branch).
- **Underlying ticker universe:** 59 tickers with price history (50+ per pod README §"Correlation Data Architecture"). All sourced from `data_pkl` price-history slice.
- **Next likely yang-side refresh:** ~2026-06-01 with `data_as_of=2026-05-29`. Probe window is point-in-time on T*=2026-05-22.

---

## Architectural findings to flag for TO-001 Level-1 mapping

### Finding 1 — Period set divergence vs FactorTilts (informational, cross-page)

`yang-generate-correlation` emits 5 periods (`1M / 3M / 6M / 1Y / 2Y`). `yang-generate-factor-tilts` emits 6 windows (`1M / 2M / 3M / 6M / 1Y / 2Y`). The two pod-mates differ on whether `2M` is a supported window. Not a YALP_CORREL TO-003 blocker; flagging because TO-001 sourcing-cell may otherwise inherit a "6 windows" assumption from sister-PRD context.

### Finding 2 — Lower-triangular matrix shape (informational; bears on TO-001 grain)

Per pod README: `correlation_data.json` ships the **full pre-computed lower-triangular matrix** for all 5 periods; client filters client-side. This means TO-001 Level-1 grain = `pair × period` (NxN/2 per period × 5 periods = ~8,700 cells for 59 tickers). TO-004 verification should sample-N pairs × periods rather than attempt full grid (consistent with YALP_MKTOVR §7 sampling lean).

### Finding 3 — YCharts pair correlation availability (TO-002 / TO-003 boundary)

YCharts does NOT publish pre-computed pair correlations as a standard endpoint (correlation is typically a derived computation on the consumer side). For YALP_CORREL TO-002/TO-004, the comparison surface is likely **per-ticker price-history alignment** (do YCharts daily-price series for ticker X match Yang's `data_pkl` slice for ticker X at T*=2026-05-22?) — NOT direct correlation-value comparison. Confirm framing with TO-001 author before TO-002 pulls. If correlation-value comparison is required, DS-lane must compute YCharts-side correlations from pulled price series under the same yang-formula (Pearson on daily returns over each period) — adds TO-004 scope.

---

## Acceptance check vs PRD TO-003 + open Qs

PRD §4 TO-003 acceptance (per YALP_MKTOVR.003 template): explicit T* + 1-2 sentence justification + binding-side identification.

**Delivered:**
- `T* = 2026-05-22` (page-mount freshness anchor for `correlation_data.json`)
- Binding constraint = yang-pipeline weekly cadence (`data_pkl.data_as_of = 2026-05-22`)
- Correlation-value comparison vs price-history comparison framing flagged for TO-001 author resolution before TO-002 dispatch

---

## Followups + cross-references

- **Sister consult (closed):** `docs/briefs/yalp_mktovr_to003_yang_publication_timing_consult.md` — methodology template.
- **Pipeline-metadata canonical source:** `s3://opal-data-portal-v2/yang-pipeline-metadata.json`.
- **L1 reference:** `docs/reference/yang-pipeline-lineage-map.md` — Correlation pod row.
- **PRD anchor:** `docs/architecture/YALP_CORREL.md` v0.1.

Consult-only deliverable; no code edits. Ready for DS 0.2.0~B to fold into TO-003 when GO'd by ws COO.
