# YALP_FACTOR TO-003 — Yang-Pipeline Publication-Timing Consult

**From:** 0.2.0_DS_PortfolioAnalytics (parallel-consult lane; pod-affinity owner per Andrew direct correction 2026-05-26 ~16:45Z)
**To:** 0.2.0_DS_PortfolioAnalytics~D (TO-003 primary owner per Wave-1 tilde-lane correction `02519793e`) · CC: ws COO 2.0.0_SA_COO · ws CTO 1.0.0_SA_CTO
**Date:** 2026-05-26 ~17:00Z
**Scope:** Provide yang-pipeline publication-timing input for YALP_FACTOR TO-003 shared-date `T*` determination. Sister to YALP_MKTOVR.003 (closed `8d1d6fcad` 2026-05-26 ~14:35Z).

---

## Bottom-line recommendation

**`T* = 2026-05-22`** (Friday before this consult). Yang-side binding constraint; verified empirically.

FactorTilts ships a tiered 3-file artifact (snapshot + spreads + timeseries); all three carry the same `data_as_of = 2026-05-22` (same Lambda emission window).

---

## Empirical evidence — yang-side `data_as_of = 2026-05-22`

Verified 2026-05-26 ~17:00Z direct from S3:

| Artifact | `data_as_of` | Path | S3 mtime |
|---|---|---|---|
| **Canonical pipeline-metadata** | `2026-05-22` (`data_as_of_date`) | `s3://opal-data-portal-v2/yang-pipeline-metadata.json` | exec_id `a018bf25-d7c9-4fce-a395-1fd5c58c91bf` started 2026-05-26T13:41:13Z |
| `yang-generate-factor-tilts` Tier-1 snapshot | `2026-05-22` (header verified) | `json/factor-tilts/tier1-snapshot.json` | 2026-05-26T13:43:11Z (10.6 KB) |
| `yang-generate-factor-tilts` Tier-2 spreads | (same Lambda emission; consistent T*) | `json/factor-tilts/tier2-spreads.json` | 2026-05-26T13:43:11Z (125.9 KB) |
| `yang-generate-factor-tilts` Tier-3 timeseries | (same Lambda emission; consistent T*) | `json/factor-tilts/tier3-timeseries.json` | 2026-05-26T13:43:11Z (3.41 MB) |

Tier-1 snapshot header excerpt confirms `data_as_of: 2026-05-22` + 6-window factor-set (`Equity vs FI / Growth vs Value / US vs Foreign / Large vs Small / Agg vs Short / HY vs Agg`) across windows (`1M / 2M / 3M / 6M / 1Y / 2Y`).

---

## Cadence + window characterization

- **`model_pkl` frequency:** weekly. `yang-generate-factor-tilts` gates on `model_pkl` presence in the manifest (per pod README §"Key Step Functions branches" — model_pkl branch).
- **3-file tier:** snapshot (~10.6 KB; current-snapshot per model+window) + spreads (~126 KB; spread metrics) + timeseries (~3.41 MB; historical series back-window). All emitted from one Lambda invocation; identical `data_as_of`.
- **Next likely yang-side refresh:** ~2026-06-01 with `data_as_of=2026-05-29`. Probe window is point-in-time on T*=2026-05-22.

---

## Architectural findings to flag for TO-001 Level-1 mapping

### Finding 1 — S3 key naming MISMATCH vs pod README + DS PA prompt.md (DOCUMENTATION DRIFT)

The pod README (`org/tier2_senior/0.2.0_DS_PortfolioAnalytics/prompt.md:38` "FactorTilts" row) and pod README's "Yang Pipeline" trigger table state the S3 output as `json/factor_tilts/` (underscore) with file names `snapshot/spreads/timeseries`. **Empirical S3 reality:**

- Actual prefix: `json/factor-tilts/` (hyphen, NOT underscore)
- Actual filenames: `tier1-snapshot.json` / `tier2-spreads.json` / `tier3-timeseries.json` (NOT bare `snapshot.json` / `spreads.json` / `timeseries.json`)

Both prompt.md AND the actual S3 key need to be cited correctly in the YALP_FACTOR PRD §2 row + TO-001 sourcing column. Picking the wrong key in TO-002 YCharts pulls or TO-004 verification would produce a "key not found" failure mode masquerading as a missing-data finding.

**Recommendation for YALP_FACTOR PRD §2:** explicitly cite `json/factor-tilts/tier1-snapshot.json` (or tier2 / tier3 as relevant per row). For the pod README drift, surface as a separate housekeeping item for DS PA (me) to fix on next opportunity — NOT a YALP_FACTOR-blocker.

### Finding 2 — Factor-window set differs from CORREL (informational, cross-page)

FactorTilts emits 6 windows (`1M / 2M / 3M / 6M / 1Y / 2Y`); Correlation emits 5 (`1M / 3M / 6M / 1Y / 2Y` — no 2M). TO-001 sourcing-column should not inherit either sister-PRD's window-set as a default for the FactorTilts row.

### Finding 3 — Factor-set migration history (informational; bears on YCharts comparison framing)

Per pod README: factor keys `Equity vs FI / Growth vs Value / US vs Foreign / Large vs Small / Agg vs Short / HY vs Agg` were migrated from `Short vs Agg` + `HY vs IG` in yang-v2.x ("do not revert"). YCharts does NOT publish these specific factor regression outputs as standard endpoints — they are computed from `model_pkl` via yang-internal regression logic. **Expected verdict profile: heavily GAP-class** (factor-regression coefficients are Yang-internal-derived; no direct YCharts equivalent).

**Recommendation for TO-001:** treat the factor table as GAP-class with sourcing/methodology cell explicit (`Yang factor regression per yang-generate-factor-tilts; coefficients = OLS regression of asset-class returns on factor proxies over each window per model`). MATCH-class scope is limited to the underlying asset-class index returns that feed the regression — comparable to YALP_POSITN's MATCH-class subset.

---

## Acceptance check vs PRD TO-003 + open Qs

PRD §4 TO-003 acceptance (per YALP_MKTOVR.003 template): explicit T* + 1-2 sentence justification + binding-side identification.

**Delivered:**
- `T* = 2026-05-22` (page-mount freshness anchor for all 3 tier files)
- Binding constraint = yang-pipeline weekly cadence (`model_pkl.data_as_of = 2026-05-22`)
- **Architectural finding (key naming):** PRD §2 + pod README cite underscore + bare filenames; reality is hyphen + `tier{1,2,3}-` prefix. PRD §2 needs correction; pod README drift logged for separate housekeeping.

---

## Followups + cross-references

- **Sister consult (closed):** `docs/briefs/yalp_mktovr_to003_yang_publication_timing_consult.md`.
- **Pipeline-metadata canonical source:** `s3://opal-data-portal-v2/yang-pipeline-metadata.json`.
- **L1 reference:** `docs/reference/yang-pipeline-lineage-map.md` — FactorTilts pod row.
- **PRD anchor:** `docs/architecture/YALP_FACTOR.md` v0.1.
- **Pod README drift:** `org/tier2_senior/0.2.0_DS_PortfolioAnalytics/prompt.md` line ~38 + "FactorTilts Data Architecture" section ~99-106 — S3 key naming needs correction on next DS PA touch.

Consult-only deliverable; no code edits. Ready for DS 0.2.0~D to fold into TO-003 when GO'd by ws COO.
