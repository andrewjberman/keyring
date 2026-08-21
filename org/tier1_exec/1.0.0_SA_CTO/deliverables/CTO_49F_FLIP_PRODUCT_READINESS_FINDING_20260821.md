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

## Why the afternoon's controls were right and still missed this

Pins measure values against DECLARED bands; certs cover route + value planes; the consumer-plane
capture proved the portal REQUESTS the twin; the never-widen halves were given on KEY SCOPE. Every
one was true and none was about the product plane. "Declared means the pipeline knew, not that
anyone decided a client should see it" (CVO, written into the cert itself). DE's P4R-4
never-blended discipline is the control that catches this class, and it fired one hour out.
