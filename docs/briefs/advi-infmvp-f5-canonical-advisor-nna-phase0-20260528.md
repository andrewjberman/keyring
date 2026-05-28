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

**Empirical finding (two parts):**

1. **Three of four surfaces ARE canonical-consistent** — the Segment Analytics **snapshot** donut (`views.nna`, INF_D_04), the **Lifetime Activity** panel (`book.json` + `timeseries.json`, INF_D_02), and the combined `partner_analytics.json` windows — all sum the same source (`gold/canonical/canonical_nna_{date}.parquet`, I_C01) and are each internally correct. Their apparent disagreement is **window-semantics**: each shows the same canonical series over a different, non-comparable window, with no shared per-advisor field rendered identically.

2. **The Segment Analytics CONTINUOUS chart (`cumulative_chart.json` `nna_adv`/`nna_geo`, INF_D_00d) is NUMERICALLY WRONG** — a genuine data-correctness bug, not just a window mismatch. `build_nna_adv_view` weekly-**samples** the NNA series (keeps 1 day per week via `_weekly_sample`, `daily[daily['date'].isin(sampled_dates)]`) and **discards the other ~6 days' flows**. Weekly-sampling is correct for AUA (a *stock* — sampling the level is lossless) but **corrupts NNA (a *flow*)**. Empirical: Peter's canonical NNA over the chart's exact 2Y window (all 476 flow-days) = **+$18.28M**; the weekly-sampled chart keeps 104 days → **+$7.32M** — **60% of the flow lost**.

This means the fix has two parts: (a) emit ONE shared canonical field/series all surfaces read (window totals + a bucket-summed per-period series), and (b) the continuous chart repoints to the canonical series (its buggy `nna_adv`/`nna_geo` are superseded — no sampling, flows bucket-summed correctly).

---

## Empirical reconciliation (Peter Lee, live S3 2026-05-28)

All values below are sums of `canonical_nna.net_nna` (signed external flow = `daily_inflow + daily_outflow`), grouped by `advisor_key='peter_lee'`. Cross-checked across four live artifacts:

| Surface (artifact) | Window/semantic | Peter NNA | Canonical cross-check |
|---|---|---|---|
| Snapshot donut `partner_analytics_quarterly.json` `views.nna.current.adv` | 2026 Q2 partial (= QTD) | **−$805,260.55** | == `partner_analytics.json` combined **QTD** by_advisor (−$805,260.55) ✓ EXACT |
| Snapshot donut `views.nna.q1.adv` | calendar **Q1 '26** (Jan–Mar) | **+$2,354,781.18** | single-quarter slice — **this is the screenshot +$2.35M** |
| Continuous `cumulative_chart.json` `nna_adv` (INF_D_00d) | weekly-SAMPLED 2Y series | net **+$7.32M** over 2Y (sampled) | **WRONG** — canonical all-days over same window = **+$18.28M**; sampler dropped **60%** of flow (stock-vs-flow bug). The −$274K screenshot hero is an artifact of the FE diffing this corrupted, mostly-empty series. |
| Lifetime `book.json` `headline.ytd_nna` | **YTD** 2026 | **+$1,549,520.63** | == combined **YTD** by_advisor (+$1,549,520.63) ✓ EXACT |
| Lifetime `timeseries.json` last `nna_canonical` | **MAX** (since inception) | **+$108,959,119.23** | == combined **MAX** by_advisor ($108,959,119.23) ✓ EXACT |

**Conclusion:** +$2.35M (snapshot, Q1'26 *quarter*) and −$274K (continuous, trailing-1Y *cumulative*) are the **same canonical series over different windows** — both correct. The user reads them as contradictory because (a) the surfaces use incompatible window vocabularies and (b) no single shared "Advisor-NNA per window" field is surfaced identically across panels.

### The three window vocabularies today
- **Snapshot** (`views.nna[period].adv`, INF_D_04): single **calendar-quarter** slices — `current`=QTD, `q1/q2/q3`= prior calendar quarters.
- **Continuous** (`cumulative_chart.nna_adv`, INF_D_00d): **cumulative** running total over the selected **1Y / 3Y / Max** Window.
- **Lifetime Activity** (`book.json` + `timeseries.json`, INF_D_02 + advisor-publisher): **YTD** headline + **since-inception cumulative** area series.

---

## Q2 RESOLUTION

> **The canonical Advisor-NNA SOURCE already exists and is the single source of truth: `gold/canonical/canonical_nna_{date}.parquet` (I_C01).** No competing *definition* exists. The snapshot donut, Lifetime panel, and combined-windows block all derive from it correctly. The **continuous chart also reads it but corrupts it via lossy weekly-sampling** (the only true calc bug, not a definition divergence).

Two missing pieces, both now shipped in `INF_D_00f`: (1) a **single per-advisor × window × fee-view canonical aggregate field** over a **unified window vocabulary** that all surfaces read for their NNA display; (2) a **bucket-summed per-period series** the continuous chart repoints onto so it stops sampling.

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

## EMIT (ADDITIVE — Rule 17 spirit) — SHIPPED

New script `data/orion/scripts/gold/INF_D_00f.advisor_nna_canonical.py` → `platinum/firm/advisor_nna_canonical.json`. Fully additive (net-new artifact; touches no existing series). Structure:

    firm: { windows: {<window>: {nna,inflows,outflows,account_count, fee_paying:{...}, no_fee:{...}}}, series: {weekly,monthly,quarterly: [{period,period_end,nna,inflows,outflows}]} }
    advisors: { <advisor_key>: { windows: {...}, series: {...} } }

- **windows** (totals): QTD, YTD, MAX, 1Y, 3Y, q_current, q1, q2, q3 — each with fee_paying/no_fee split (F4 tie-out).
- **series** (per-period): weekly/monthly/quarterly, **bucket-summed** (the correct flow aggregation — supersedes INF_D_00d's lossy sampling).

Computed once from `canonical_nna` (same logic proven exact in `INF_09.build_combined_partner_analytics` + `INF_D_00c` leaderboard). Validated canonical-exact (Peter QTD/YTD/MAX/q1 to the cent; firm==sum(advisors); fee_paying+no_fee==total; quarterly-series-sum==MAX-window).

**Cohort dimension (new-vs-existing client):** NOT in v1 of this emit — flagged as an additive follow-on reusing the F11 `hh_lifecycle` inception classification. Core spine (advisor × window × fee_view) shipped first; COO/CVO to confirm whether the client-type cohort split is needed in F5 or rides with F4.

Downstream (COO authors at emit-RAVC2):
- **RD (0.4.2):** repoint snapshot donut + continuous (hero totals → `windows`; area/tooltips → `series`) + Lifetime Activity to read `advisor_nna_canonical` for the matching window. The continuous repoint also FIXES the 60%-flow-loss bug (it stops reading the sampled `nna_adv`). Align window vocab/labels.
- **CVO (3.0.0):** RIGID empirical gate — Peter + 1 control, displayed Advisor-NNA identical across all three surfaces for every window × fee_view, on real data.

---

## AC5-DS-self-check (reconciliation of −$274K vs +$2.35M)

**Resolved into two distinct causes, not one:**

1. **+$2,354,781 (snapshot) is correct** — it is Peter's **calendar Q1 '26** net external flow (snapshot donut with Q1 selected), `Σ canonical_nna.net_nna` over Jan–Mar 2026. Verified canonical-exact against the combined windows block (snapshot `current` = QTD −$805,261; book ytd = YTD +$1,549,521; timeseries last = MAX +$108.96M — all matched to the cent).
2. **−$274K (continuous) is WRONG** — it is NOT simply a different window. The continuous `nna_adv` weekly-**samples** the NNA flow series (INF_D_00d), keeping ~104 of 476 flow-days and dropping **60%** of Peter's flow (+$18.28M canonical all-days → +$7.32M sampled over the same 2Y window). The −$274K hero is the FE's endpoint-diff over this corrupted, mostly-empty series.

So the spine defect is BOTH (a) mismatched/unlabeled window vocabularies across the canonical-correct surfaces AND (b) a real flow-sampling bug in the continuous chart. The canonical artifact resolves both: window totals give every surface one identical number per window×fee_view, and the bucket-summed `series` gives the continuous chart a correct per-period source (sum-within-period, no sampling) to repoint onto.
