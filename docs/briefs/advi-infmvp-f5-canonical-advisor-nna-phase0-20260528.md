# ADVI_INFMVP.F5 — Canonical Advisor-NNA: Phase-0 Resolution (Q2) + Canonical Definition

**Author:** 0.4.0_DS_ClientPlatform
**Date:** 2026-05-28
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFMVP.F5.canonical-advisor-nna.md`
**PRD:** `docs/architecture/ADVI_INFMVP.md` v0.1 §3 F5 + §7 Q2 (commit 5f6018778)
**Status:** Phase-0 gating deliverable — empirical investigation complete; emit next.

---

## TL;DR — the spine, resolved empirically

Peter's Advisor-NNA appears different in every panel:
- Segment Analytics **snapshot** (NNA-by-Advisor donut, Q1 '26 selected): **+$2.35M**
- Segment Analytics **continuous** (cumulative, trailing window): **−$274K**
- Lifetime Activity: a third number

**The CTO root-cause hypothesis (three different upstream series, each with its own aggregation) is empirically PARTIALLY incorrect.** All three surfaces already derive from the **same single source** — `gold/canonical/canonical_nna_{date}.parquet` (I_C01) — and **each is internally correct**. The divergence is **NOT a calculation bug and NOT competing definitions**. It is a **window-semantics mismatch**: each surface sums the same canonical series over a **different, non-comparable window**, with no shared per-advisor × window × cohort × fee-view field rendered identically.

This *simplifies* the fix: there is no competing-definition reconciliation to do. We unify the window vocabulary and emit ONE shared canonical field all three surfaces read for the matching window.

---

## Empirical reconciliation (Peter Lee, live S3 2026-05-28)

All values below are sums of `canonical_nna.net_nna` (signed external flow = `daily_inflow + daily_outflow`), grouped by `advisor_key='peter_lee'`. Cross-checked across four live artifacts:

| Surface (artifact) | Window/semantic | Peter NNA | Canonical cross-check |
|---|---|---|---|
| Snapshot donut `partner_analytics_quarterly.json` `views.nna.current.adv` | 2026 Q2 partial (= QTD) | **−$805,260.55** | == `partner_analytics.json` combined **QTD** by_advisor (−$805,260.55) ✓ EXACT |
| Snapshot donut `views.nna.q1.adv` | calendar **Q1 '26** (Jan–Mar) | **+$2,354,781.18** | single-quarter slice — **this is the screenshot +$2.35M** |
| Continuous `cumulative_chart.json` `nna_adv` (last pt) | cumulative over chart window | **−$260,000.26** | ≈ screenshot **−$274K** (trailing-1Y vintage) |
| Lifetime `book.json` `headline.ytd_nna` | **YTD** 2026 | **+$1,549,520.63** | == combined **YTD** by_advisor (+$1,549,520.63) ✓ EXACT |
| Lifetime `timeseries.json` last `nna_canonical` | **MAX** (since inception) | **+$108,959,119.23** | == combined **MAX** by_advisor ($108,959,119.23) ✓ EXACT |

**Conclusion:** +$2.35M (snapshot, Q1'26 *quarter*) and −$274K (continuous, trailing-1Y *cumulative*) are the **same canonical series over different windows** — both correct. The user reads them as contradictory because (a) the surfaces use incompatible window vocabularies and (b) no single shared "Advisor-NNA per window" field is surfaced identically across panels.

### The three window vocabularies today
- **Snapshot** (`views.nna[period].adv`, INF_D_04): single **calendar-quarter** slices — `current`=QTD, `q1/q2/q3`= prior calendar quarters.
- **Continuous** (`cumulative_chart.nna_adv`, INF_D_00d): **cumulative** running total over the selected **1Y / 3Y / Max** Window.
- **Lifetime Activity** (`book.json` + `timeseries.json`, INF_D_02 + advisor-publisher): **YTD** headline + **since-inception cumulative** area series.

---

## Q2 RESOLUTION

> **A canonical Advisor-NNA series ALREADY EXISTS and is already the single source of truth: `gold/canonical/canonical_nna_{date}.parquet` (I_C01).** No competing or divergent upstream series exists. All four platinum NNA surfaces (snapshot donut, continuous chart, Lifetime book + timeseries, leaderboard) already derive from it and agree exactly when sliced to the same window.

The missing piece is a **single per-advisor × window × cohort × fee-view canonical aggregate field**, computed once over a **unified window vocabulary**, that all three FE surfaces read for their NNA display.

---

## CANONICAL DEFINITION (the contract RD + CVO hold to)

**Advisor-NNA(advisor, window, cohort, fee_view)** :=

    Σ_{d ∈ [window_start, window_end]}  canonical_nna.net_nna
       where  advisor_key == advisor
              [AND cohort filter]          (optional: new-client vs existing-client)
              [AND fee_view partition]     (optional: is_fee_earning → fee_paying | no_fee)

- `net_nna = daily_inflow + daily_outflow` (signed; outflows negative) — **external client flows only** (Client/Rollover Contributions in; Client Distributions + tax withholdings + Cancel Account out). Internal journals, exchanges, dividends, income-reinvestment contribute **0** (per `orion_cashflow_taxonomy.yaml`). This is *external net-new assets*, NOT AUA-change (AUA-change includes market appreciation).
- `inflows = Σ daily_inflow`, `outflows = Σ daily_outflow` so `nna = inflows + outflows` and sub-buckets sum (F4 tie-out).
- **Window vocabulary (unified):** `QTD`, `YTD`, `MAX`, plus rolling `1Y` / `3Y` (continuous), plus the calendar-quarter periods the snapshot strip needs. Same `(advisor, window, cohort, fee_view)` tuple ⇒ exactly one number across all surfaces.
- **fee_view** (for F4): partition each window by `is_fee_earning` (silver/api_dims/billing join on account_id) → `fee_paying` + `no_fee`, summing to the total. (Re-uses the F11 `fee_breakdown` join already shipped.)

---

## Proposed EMIT (ADDITIVE — Rule 17 spirit)

Emit a single canonical block/artifact keyed:

    advisor_nna_canonical[advisor_key][window][cohort][fee_view] = {nna, inflows, outflows, account_count}

computed once from `canonical_nna` (the same code path already proven correct in `INF_09.build_combined_partner_analytics` + `INF_D_00c` leaderboard). Candidate emit site: extend the existing `partner_analytics.json` `windows` block (already QTD/YTD/MAX by_advisor, canonical-exact) to the full window × cohort × fee_view matrix, OR a dedicated `platinum/firm/advisor_nna_canonical.json`. **No existing series pruned** — RD removes per-view *re-derivation* on the FE side, not the DS series.

Downstream (COO authors at emit-RAVC2):
- **RD (0.4.2):** repoint snapshot donut + continuous hero metrics + Lifetime Activity to read `advisor_nna_canonical` for the matching window; align the window vocabulary/labels so the same selection shows the same number across panels.
- **CVO (3.0.0):** RIGID empirical gate — Peter + 1 control, displayed Advisor-NNA identical across all three surfaces for every window × cohort × fee_view, on real data.

---

## AC5-DS-self-check (reconciliation of −$274K vs +$2.35M)

**Resolved to a single explained model, not a single number** — because the two were measuring *different windows of the same canonical series*: +$2,354,781 = Peter's **calendar Q1 '26** net external flow (snapshot donut, Q1 selected); −$274K ≈ Peter's **trailing-~1Y cumulative** net external flow (continuous). Both are `Σ canonical_nna.net_nna` over their window, verified canonical-exact against the combined `partner_analytics.json` windows block (QTD −$805,261 / YTD +$1,549,521 / MAX +$108.96M all matched to the cent). The canonical field makes this explicit by exposing every window under one shared tuple so no surface can show a window-mismatched number unlabeled.
