# 49F twin flip — PRODUCT-READINESS FINDING and the determination it changed (CTO, 2026-08-21 ~17:1xZ)
**archetype:** VALIDATE

**In one sentence:** every portal-reachable 49F twin key carries a user-visible product regression
against the legacy serve — history truncation, dimension collapse, or advisor-population loss —
all DECLARED at the pin layer as in-band, NONE decided at the product plane until `0.4.0_DE`'s
P4R-4 named-deltas check measured them (65234, 65284, 65323) an hour before PROD. **The
single-green-Friday product promote of the 49F twins does not happen today. This is a readiness
finding about the SOURCE, not a fire miss and not a port defect.**

## What DE measured (live twin vs live legacy, recursive array-length diff — a top-level shape diff read "identical" on three of these)

| key | legacy | twin | class |
|---|---|---|---|
| `cumulative_chart` | 2020-01-02..2026-08-19 (2,421 d, 352 pts); geo 9 states + Other | 2024-07-08..2026-08-20 (773 d, 111 pts); geo `['Other']` | history truncation + dimension collapse |
| `timeseries_overview` | quarterly 27 / monthly 80 / annual 7 | 9 / 26 / 3 | history truncation |
| `partner_analytics_quarterly`, `_annual` | AUA-by-Office 9 offices; AUA-by-State unassigned 0.069% | Office 100% `'other'`; State 100% unassigned | dimension collapse ×2 |
| `leaderboard` | 163 entries every window | 146; **20 named advisors absent** | population loss — mechanism UNKNOWN (identity coverage? defect?) |
| `mix_summary` | mix_periods 5 quarters | 1 | history truncation |

## Mechanism (CVO 65279/65312 — measured, not inferred)

- The 2024-07-08 floor is **the entire Schwab silver tree's floor** (`dim_balance`, `fact_acc`,
  `dim_position`, `fact_trn`, `fact_sec`, `dim_transaction` all earliest 2024-07-08); the
  canonical series (529 partitions) inherits it. **No recompute/backfill can extend it — the
  source rows do not exist in this plane.** Legacy's 6.6 years are Black-Diamond-side history.
- No geographic dimension among the 11 canonical dims; office/state are plausibly the same class
  (CVO to confirm). The leaderboard −20 is a different mechanism and is the one item that could
  be a DEFECT rather than an extent — it needs its own measurement cell.

## The determination as it now stands

CTO never-widen half **WITHDRAWN on all six portal-reachable keys** (my GIVEN on four was
conditional on exactly the figures that then failed). COO's half was already withheld on the two
history keys; the four-key GIVEN carried the same condition. Held keys (4) + d14 unchanged.
**No consumer-visible key clears the two-halves control today.** DEV registry → all six `'held'`
(DE); promote stood down, worktree torn down, origin/PROD untouched at `8a96c916` (DT/MSTR).

**What STANDS, built today and reusable per key:** the route act (remedy A, exercised, tenant
assertion), the registry-as-data flip, the certs, the pins, the oracle table, the capture
discipline. What changed is the answer to *"is the canonical source ready to serve this
product?"* — measured at the product plane for the first time.

## Carded to Andrew — ONE product-readiness question, six keys

Canonical = Schwab-authority from 2024-07-08, no geo/office/state dims, leaderboard population
short 20 pending mechanism. Legacy = 6.6 years, nine states/offices, 163 advisors. **REC: keep
49F Advisor Intelligence LEGACY-SERVED; commission the gap closures as NAMED programs** (vendor
history feasibility — does the vendor supply pre-2024-07 at grain, does it reconcile; BD-side
attribute dims in canonical; identity coverage for the leaderboard); **re-flip PER KEY as each
closes.** The word "backfill" does not appear in any option until obtainability is measured.

## ⛔ CORRECTIONS within 20 minutes of writing (two measurements that change the REMEDY, not the hold)

1. **HISTORY EXISTS IN THE ESTATE — the "vendor procurement" framing above is RETRACTED** (CVO
   65337, own retraction): `opal-data-bd/gold/canonical/` carries 2,423 dated entries
   2020-01-02..2026-08-21 (performance, nna, holdings, account_gains) — the legacy chart's span.
   The Schwab plane's tree-wide 2024-07-08 floor stands, so the remedy is a **CROSS-PLANE PORT**
   (BD gold → Schwab-authority canonical) with one named feasibility test CVO is running now on my
   word: **do the two vendors' books RECONCILE** (account universe, valuation basis, NNA
   definition) across the 2024-07-08 seam? If not, a splice manufactures a discontinuity in a
   client-facing trend chart — worse than the truncation. Nobody ports until that read lands.
2. **GEOGRAPHY IS NOT SOURCE-LIMITED — "no geography available" was FALSE** (COO 65343, measured
   at Andrew's direct prompt): `schwab/08335338/silver/fact_acc` carries `ac_st` at **100%
   population (7,331/7,331, 48 states)** plus city/zip/country, and the top states ARE the legacy
   chart's set. "No canonical geo DIM" (CVO) is true; the remedy is **an UNBUILT canonical
   dimension over data we already hold** — a scoped dim build (DS lane; dim + two emit sites +
   reader vocabulary + pin refresh), not a program. Sizing is mine; it is small.
3. Still UNMEASURED and stated as such: **OFFICE** (the `views.ofc` collapse — is office a Schwab
   field at grain or BD-side? measure before classing) and the **LEADERBOARD −20 named advisors**
   (identity coverage vs defect — the one item that could be a BUG).

**The hold on all six keys stands regardless — a twin serving `['Other']` today is a product
regression today whatever the remedy costs. What changed is the card: history = port-ability test;
geo = scoped build; office/leaderboard = measure first.**

## Why the afternoon's controls were right and still missed this

Pins measure values against DECLARED bands; certs cover route + value planes; the consumer-plane
capture proved the portal REQUESTS the twin; the never-widen halves were given on KEY SCOPE. Every
one was true and none was about the product plane. "Declared means the pipeline knew, not that
anyone decided a client should see it" (CVO, written into the cert itself). DE's P4R-4
never-blended discipline is the control that catches this class, and it fired one hour out.
