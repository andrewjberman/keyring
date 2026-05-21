# BRIEF: 4 Bloomberg maturity-band bonds — cross-vendor analysis (C2 pre-stage Track 2)

**Date:** 2026-05-21
**Author:** 0.1.0_DS_MarketIntelligence
**Audience:** 2.0.0_SA_COO — a cross-vendor decision needs an Andrew/architectural ruling (per the COO C2 pre-stage GO). CC 1.0.0_SA_CTO.
**Context:** C2 pre-stage Track 2. 4 of the 9 A4 blocked-pending-symbol entities are Bloomberg maturity-band bond indices with no YCharts Bloomberg-vendor match. This brief works the candidate mapping; the substitution decision is escalated, not made.

---

## 1. The 4 entities

| Portal name | Bloomberg ticker | A4 status |
|---|---|---|
| Bloomberg 0-1 Year Treasury | I22917US Index | blocked-pending-symbol |
| Bloomberg 0-5 Year High Yield | BEJKTRUU Index | blocked-pending-symbol |
| Bloomberg 0-5 Year TIPS | LTP5TRUU Index | blocked-pending-symbol |
| Bloomberg 20+ Year Treasury | LT11TRUU Index | blocked-pending-symbol |

## 2. What A4 Batch 0 established

~A scanned the **full YCharts index taxonomy** (`/indices/asset_class/root/index_list`, all 164 asset-class nodes). Finding: YCharts' Bloomberg index set (18 indices) does **not** carry these 4 maturity-band variants — it carries the broad parents (`^BBUSCOHYTR` broad US Corporate HY, `^BBUTISTR` broad US TIPS, `^BBUSTTR` blended US Treasury) but not the maturity-banded children. YCharts **does** carry **ICE-vendor** maturity-band Treasury indices: `^ICEUT2YTR` (ICE 20+ Yr Treasury), `^ICEUST13YT` (ICE 1-3 Yr), `^ICEUSTSBTR` (ICE Short Bond), `^ICEUT12YTR` (ICE 10-20 Yr).

The taxonomy view is complete; what it does **not** cover is the browser-in-loop securities-search route (the SPA `/search/` — same gap as the 5 securities-search entities), which could still surface these under a non-index path.

## 3. Per-bond candidate analysis

| Bloomberg entity | Same-maturity-band YCharts candidate | Assessment |
|---|---|---|
| **20+ Year Treasury** | `^ICEUT2YTR` — ICE 20+ Yr Treasury | **Clean band match.** Same instrument definition (20+yr US Treasury, total return); only the index vendor differs (Bloomberg LT11TRUU vs ICE). A viable cross-vendor substitution — pending a return-fidelity check. |
| **0-1 Year Treasury** | none exact — ICE has 1-3 Yr (`^ICEUST13YT`) and "Short Bond" (`^ICEUSTSBTR`), neither is the 0-1yr band | **No clean match.** 0-1yr is ultra-short; the nearest candidates are a different band. Needs a browser-in-loop search first; failing that, a near-band proxy with a documented basis difference, or stays-Bloomberg-pkl. |
| **0-5 Year High Yield** | none — no 0-5yr-band HY index found (Bloomberg or ICE); only broad HY | **No match.** A maturity-banded HY index is not in the YCharts taxonomy at all. Browser-in-loop search first; likely a genuine gap. |
| **0-5 Year TIPS** | none — no 0-5yr-band TIPS found; only broad TIPS | **No match.** Same as 0-5yr HY — no maturity-banded TIPS in the taxonomy. Browser-in-loop search first; likely a genuine gap. |

**Net: 1 of 4 has a clean cross-vendor candidate** (20+ Yr Treasury → ICE). The other 3 have no maturity-band match in the YCharts index taxonomy.

## 4. The decision needed (escalated to COO / Andrew)

A4 / A3 did not pre-decide cross-vendor substitution — it is a fidelity + product call. Two questions:

1. **Is a Bloomberg→ICE vendor substitution acceptable** for a portal series the portal labels "Bloomberg 20+ Year Treasury"? ICE and Bloomberg 20+yr Treasury indices track the same bonds but differ in rebalancing/pricing — a small, documentable basis difference. If yes, `^ICEUT2YTR` resolves that entity (pending a return-fidelity check on capture).
2. **For the 3 with no band match** (0-1 Yr Treasury, 0-5 Yr HY, 0-5 Yr TIPS) — accept a near-band / broad-parent proxy with a documented basis difference, or keep them on the manual Bloomberg `data_pkl` feed? These are the genuine candidates for a stays-Bloomberg-pkl carve-out (a small one — 3 entities).

## 5. Recommendation (DS, for the COO/Andrew decision)

- **20+ Yr Treasury:** if the Bloomberg→ICE swap is sanctioned, adopt `^ICEUT2YTR` — subject to a return-fidelity check (capture both series, compare; the check needs a YCharts session, so it folds into the recapture batch / dedicated-seat work).
- **0-1 Yr Treasury, 0-5 Yr HY, 0-5 Yr TIPS:** run the browser-in-loop YCharts securities-search first (bundle with the 5 securities-search entities — one capture task). Only if that also fails are they a true gap; then the proxy-vs-stays-Bloomberg-pkl call applies.
- **Fidelity checks are capture-gated** — they need a YCharts session, so they execute in the recapture batch, not in C1-independent pre-stage. This brief is the C1-independent part: the candidate mapping + the escalation.

## 6. C2 impact

The C2 pull-spec (`mdsrc-c2-pull-spec-prestage-20260521.csv`) carries all 4 as `BLOCKED — yc_symbol unresolved`. On the COO/Andrew ruling: up to 1 (or, with proxies, up to 4) flip to a resolved YCharts symbol; any that stay are an explicit, small stays-Bloomberg-pkl carve-out for C2 — at most 3 entities, not a structural problem.
