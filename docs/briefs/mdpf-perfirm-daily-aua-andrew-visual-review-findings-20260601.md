# BRIEFING → CTO: MDPF Per-Firm Daily AUA — Andrew visual-review findings (2026-06-01)

- **Author:** 0.4.2_RD_AdvisorIntelligence~B (compiled from Andrew's direct visual review, 2026-06-01)
- **Purpose:** Andrew did the human visual smoke of the per-firm Daily AUA views (Global / 49 Financial / Inflection) after the FE Cohort-1c SMA fold (`103f623a`). This briefing summarizes his findings so CTO can craft a PRD and COO can decompose into TOs (RD included).
- **Routing:** → CTO (PRD) → COO (TO breakdown). CC COO.

## 0. Visual smoke result — CLOSES the FE visual gate
Andrew confirmed the front end directly:
- **Global:** correct — frontend AND backend, "perfect."
- **49 Financial:** frontend **completely correct** (validates the Cohort-1c SMA fold `103f623a` + accumulated DEV delta).
- **Inflection:** frontend **correct**.

=> The pending visual smoke on the per-firm Daily AUA FE work (this session's DEV delta: `c868bd41` Peers fix, `f12abf95` Opal-only toggle, `2eb4b450` canonical names, `1b9e176c` disclaimer removal, `103f623a` SMA fold) is **PASSED by Andrew** for these surfaces. Screenshots also show: 49F = 5 model lines + one combined Non-Model AUA (no separate SMA sleeves); INF = 5 models + 2 blend lines + combined Non-Model — i.e., the fold renders as designed. The FE leg can promote (per CTO/COO promote sequencing); the items below are NET-NEW work surfaced by the review.

---

## Work items (for PRD → TO)

### ITEM 1 — [BACKEND, 49F] Re-derive the ENTIRE 49F time series on Schwab + canonical cohort methodology
**Andrew (verbatim intent):** "Backend needs to use correct methodology going all the way back in time series. The methodology was switched from Black Diamond aggregate to Schwab aggregate after 5/15/2026; it needs to be Schwab and the canonical 49 cohort methodology … all the way back."
- **Problem:** pre-5/15/2026 the 49F series is built off **Black Diamond** aggregate (~$1.83B, inflated); post-5/15 off **Schwab** (~$1.65B). This is the documented v0.8→v0.9 seam and the ~$172M step at 5/18 in the combined non-model line. (FE-confirmed: the step lives in `partner_custody_total`; the FE fold preserves it exactly — it is NOT an FE bug.)
- **Canonical methodology to apply for ALL dates (Andrew):** Schwab is the catch-all total; parse out the cohorts:
  - **1a** = SmartX **models**
  - **1c** = SmartX **SMAs** — a **calculated daily value** (interpolated or otherwise) since exact historical per-date SMA is not directly available pre-breakout
  - **1b** = **balance** = Schwab total − 1a − 1c
- **Owner:** backend — DS-CP (owns `data/mdpf/scripts/gold/mdpf_aggregate_aua.py`) for the gold methodology + daily-1c derivation; DE/AE for pipeline + historical backfill.
- **Note:** supersedes/specifies the Black-Diamond→Schwab provenance item already routed (RD→COO 162614Z) and DS~B's earlier reconstructability scope (`3f26f909a`) — Andrew has now ruled the canonical method (Schwab − 1a − 1c) AND that 1c should be a calculated/interpolated daily value back through history (i.e., option (ii)/(iii) territory, not "no backfill").

### ITEM 2 — [FRONTEND, RD] Inflection 50/50 blend portfolio colors
**Andrew:** "should pick better colors for the 50/50 portfolios."
- **50/50 INT/LTC** (`opal_blend_5050_int_ltc`) → a **blue-green / teal**.
- **50/50 ST/INT** (`opal_blend_5050_st_int`) → an **orange variant** — "between orange and green that would lean more orange" (i.e., a warm amber / yellow-orange, clearly distinct from the teal).
- **Owner:** RD (me) — FE color assignment (`portal/src/lib/modelPortfolioColors.ts` / `chartColors.ts` model color map). Small, FE-only, no backend.
- **Scope note:** these two blends are Inflection-only, cohort_class='model' (they render as their own lines/slices — correct). This is purely a palette/legibility improvement.

### ITEM 3 — [BACKEND/DATA, investigate] 12/27/2025 per-firm data anomaly (49F + Inflection; NOT Global)
**Andrew:** "data fluctuation at 12/27/2025 … afflicts both the 49 Financial and Inflection time series adversely but somehow does not affect Global."
- **Manifestation (from Andrew's screenshots):**
  - **Inflection (2025-12-27):** Total AUA → **$0**; every cohort ($0 across Ultra-Short … Ultra-Long, both 50/50 blends, Non-Model). A full single-date dropout — visible downward spike in the trend.
  - **49 Financial (2025-12-27):** model breakdown **collapses/misallocates** — Ultra-Short Term ≈ **$1.118B**, all other models **$0**, Non-Model ≈ **$223M**, Total ≈ **$1.348B**. A single-date distortion (everything lumped into one model band).
- **Key discriminator:** present in BOTH per-firm artifacts but **absent from Global** → the bug is in the **per-firm slice/emit** (likely `slice_per_firm()` or the per-firm fill), not the global aggregate. 12/27/2025 is a **Saturday** — candidate causes: holiday/weekend fill artifact, a partial or bad emit row, or a per-firm forward-fill gap.
- **Owner:** backend/data — DS-CP / DE to investigate the 12/27 per-firm emit. RD only if an FE guard is wanted as a stopgap (e.g., suppress an all-$0 date), but the real fix is the data row.
- **Screenshots (Andrew):** `Screenshot 2026-06-01 130122.png` (Inflection), `Screenshot 2026-06-01 130138.png` (49 Financial).

---

## Suggested TO split (for COO)
| Item | Lane | Owner |
|---|---|---|
| 1 — 49F Schwab re-derive + canonical 1a/1b/1c (incl. daily-1c interpolation, all history) | Backend | DS-CP (gold) + DE/AE (pipeline/backfill) |
| 2 — Inflection 50/50 blend colors (teal + amber) | Frontend | RD (me) |
| 3 — 12/27/2025 per-firm anomaly investigation/fix | Backend/Data | DS-CP / DE (FE guard by RD only if directed) |

Global needs no work. Item 2 (RD) can ship on the next portal-promote DEV delta; Items 1 & 3 are backend and gate on the data team.
