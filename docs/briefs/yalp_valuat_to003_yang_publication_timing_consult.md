# YALP_VALUAT TO-003 — Yang-Pipeline Publication-Timing Consult

**From:** 0.2.0_DS_PortfolioAnalytics (parallel-consult lane; pod-affinity owner per YALP_VALUAT §4 lane note + Andrew direct correction 2026-05-26 ~16:45Z)
**To:** 0.1.0_DS_MarketIntelligence~B (TO-003 primary owner for YALP_VALUAT per PRD §4 — note: lane assignment per PRD v0.1 §4 cites DS 0.1.0~B; verify against latest COO dispatch) · CC: ws COO 2.0.0_SA_COO · ws CTO 1.0.0_SA_CTO
**Date:** 2026-05-26 ~17:00Z
**Scope:** Provide yang-pipeline publication-timing input for YALP_VALUAT TO-003 shared-date `T*` determination per PRD v0.1 §4. Sister project to YALP_MKTOVR.003 (closed `8d1d6fcad` 2026-05-26 ~14:35Z).

---

## Bottom-line recommendation

**`T* = 2026-05-22`** (Friday before this consult). Yang-side binding constraint; verified empirically against the authoritative pipeline-metadata.json + each Valuation-page Lambda's emitted `data_as_of`.

Same constraint logic as YALP_MKTOVR.003: yang-pipeline weekly cadence; 2026-05-26T13:41Z execution emitted `data_as_of_date=2026-05-22`; 2026-05-23/24 weekend; 2026-05-25 Memorial Day; 2026-05-26 EOD not yet published.

---

## Empirical evidence — yang-side `data_as_of = 2026-05-22`

Verified 2026-05-26 ~17:00Z direct from S3:

| Artifact | `data_as_of` | Path | S3 generated_at |
|---|---|---|---|
| **Canonical pipeline-metadata** | `2026-05-22` (`data_as_of_date`) | `s3://opal-data-portal-v2/yang-pipeline-metadata.json` | exec_id `a018bf25-d7c9-4fce-a395-1fd5c58c91bf` started 2026-05-26T13:41:13Z |
| `yang-generate-valuation` output (Valuation main view) | `2026-05-22` | `json/valuation/valuation_data.json` | 2026-05-26T13:43Z mtime (2.16 MB) |
| `yang-generate-risk-premium` output (RiskPremiumTab) | `2026-05-22` (header confirms both `erp` + `credit_spreads` paths) | `json/valuation/risk_premium_data.json` | `generated_at: 2026-05-26T13:43:08Z` |

Both Valuation-page Lambdas anchor on the same upstream `data_pkl` (per pod README §"Valuation Data Architecture"). T*=2026-05-22 is the unambiguous answer for the Valuation page.

---

## Cadence + window characterization

- **`data_pkl` frequency:** weekly (yang-pipeline manifest). Both `yang-generate-valuation` + `yang-generate-risk-premium` are gated on `data_pkl` presence in the manifest (per pod README §"Key Step Functions branches").
- **PM upload pattern:** Tuesday-after-holiday-week upload (today 2026-05-26 ~09:41 ET) carrying Friday 2026-05-22 as_of — consistent with the standard cadence skipping Mon Memorial Day.
- **Next likely yang-side refresh:** if PM resumes Monday cadence next week, refresh ~2026-06-01 with `data_as_of=2026-05-29`. Probe window is point-in-time on T*=2026-05-22.

---

## Architectural findings to flag for TO-001 Level-1 mapping

### Finding 1 — FRED cache freshness for IG/HY OAS series (PRD §2 + §5 Q2)

`yang-generate-risk-premium` reads ICE BofA IG (`BAMLC0A0CM`) + HY (`BAMLH0A0HYM2`) OAS data from the **yang-side FRED cache** (`cache/fred/BAMLC0A0CM.csv` + `cache/fred/BAMLH0A0HYM2.csv`), NOT direct from FRED API at Lambda runtime. The cache mtime gates whether 2026-05-22 OAS readings are present in the artifact. The artifact `note` field confirms: *"Credit spreads: monthly (786 pts). ERP: monthly (437 pts). NO SAMPLING."* — both ERP + OAS are emitted as **monthly** series, not daily, so the binding T* for these specific surfaces is the latest **month-end** with cache coverage, not 2026-05-22 per se. For 2026-05-22 falling mid-month, the relevant comparison point is the **April-2026 month-end** ERP/OAS value (or whichever month-end was last cached).

**Implication for YALP_VALUAT TO-001 + TO-004:** the Yang-side ERP + credit-spread values are **monthly-grain** anchored on month-end dates, NOT on T*=2026-05-22 specifically. YCharts comparison should be apples-to-apples on the same month-end (likely 2026-04-30). T*=2026-05-22 governs the **page-mount-time freshness** of the artifact, NOT the data-grain of the metrics inside.

### Finding 2 — Yang-derived ERP GAP-class confirmation (PRD §3 + §5 Q1)

Empirically confirmed: `risk_premium_data.json` declares `data_source.erp = "Yang PKL (S&P 500 P/E + 10Y Treasury)"`. This is a **derived metric** (Yang-internal computation from S&P 500 fundamentals + 10Y yield), with NO direct YCharts equivalent. Aligns with PRD §3 expectation + §5 Q1 lean (document as GAP-class with sourcing/methodology cell explicit). Recommend: TO-001 enumerate ERP as `verdict_class: GAP (sourcing/methodology: "Yang ERP derived from S&P 500 fwd P/E inversion - 10Y Treasury yield, per yang-generate-risk-premium Lambda")`.

### Finding 3 — IG/HY OAS source-of-truth (PRD §5 Q2 + §3)

Yang's FRED cache (`cache/fred/BAMLC0A0CM.csv`) ultimately sources from ICE BofA via FRED. If YCharts also serves these series, the upstream is the same ICE BofA submission. **Expected verdict: MATCH-class.** Verify mtime + last-row date in the cache CSV before TO-004 comparison; if cache is stale (>1mo without refresh), document the staleness as a finding even if the comparison logic returns MATCH for the cached value.

---

## Acceptance check vs PRD §4 TO-003 + PRD §5 open Qs

PRD §4 TO-003 acceptance (implied per YALP_MKTOVR.003 template): explicit T* value + 1-2 sentence justification + binding-side identification.

**Delivered:**
- `T* = 2026-05-22` (page-mount freshness anchor)
- Binding constraint = yang-pipeline weekly cadence (`data_pkl.data_as_of` = 2026-05-22)
- **Methodology refinement:** for ERP + IG/HY OAS, the data-grain is monthly (anchored on month-end); use the most recent month-end for value comparison
- **PRD §5 Q1 (Yang ERP GAP-class):** CONFIRMED yes — GAP-class with explicit sourcing/methodology cell
- **PRD §5 Q2 (IG/HY OAS source conflict):** likely MATCH-class (both ICE BofA upstream); empirical verification in TO-004

---

## Followups + cross-references

- **Sister consult (closed):** `docs/briefs/yalp_mktovr_to003_yang_publication_timing_consult.md` — methodology template; T*-discovery pattern.
- **Pipeline-metadata canonical source:** `s3://opal-data-portal-v2/yang-pipeline-metadata.json` — single authoritative `data_as_of_date`; recommend citing in TO-004 + TO-VAL for audit trail.
- **L1 reference:** `docs/reference/yang-pipeline-lineage-map.md` §6.1 + §6.2 (Valuation pod rows).
- **PRD anchor:** `docs/architecture/YALP_VALUAT.md` v0.1 — TO-003 + §5 open Qs answered above.

Consult-only deliverable; no code edits. Ready for DS 0.1.0~B (or revised lane assignment) to fold into TO-003 when GO'd by ws COO.
