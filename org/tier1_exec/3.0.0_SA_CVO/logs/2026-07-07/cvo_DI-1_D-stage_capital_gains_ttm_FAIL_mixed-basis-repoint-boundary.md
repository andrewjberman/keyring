# CVO Finding — DI-1 D-stage belt = FAIL: capital_gains_ttm is a MIXED-BASIS delta (re-point boundary, un-backfilled history)

**Date:** 2026-07-07T00:45Z
**Agent:** 3.0.0_SA_CVO
**Class:** substance-meta (magnitude) — CONFIRMED, grounded (Rule 22 complete: source + live + mechanism)
**Priority:** P1 (client-facing served firm figure, materially wrong)
**Routing:** DS~B (DI-1 re-point / ADVI_INFREF owner) + DS~A (INF_C_03/B_03) ; CC COO (belt-owner) + CTO (tax-lineage design gate). NOT CVO-fixed (substance on code-owned surface).
**Corrects:** the earlier belt premise "DI-1 D-stage capital_gains_ttm self-heals next nightly." It does NOT self-heal — the re-point created a NEW defect at the temporal grain.

## Symptom (grounded, live)
Served `platinum/firm/clients_tab.json` (@00:04:36Z, fresh nightly):
- `tax.capital_gains_ttm       = $101,377,008`
- `tax.unrealized_gain_change_ttm = $101,377,008`  (same value / same defect)
On a firm book with true (native) total unrealized gain = **$13.3M** and AUA $202.5M, a TTM *change in unrealized gain* of $101.4M fails magnitude plausibility (a delta ~7.6x the entire unrealized level).

## Mechanism (grounded — the decisive evidence)
`capital_gains_ttm` (INF_D_00:445-472 `compute_firm_capital_gains_ttm`, TTM_LOOKBACK_DAYS=365) = Σ over accounts of `unrealized_gain`(nearest today) − `unrealized_gain`(nearest 365d-ago), read from `account_performance`.

INF_C_03.account_performance.py was **DI-1 re-pointed to Orion NATIVE total_gain_loss on 2026-07-06** (l.9, l.113) — but ONLY forward; the historical timeseries was NOT backfilled. Live `account_performance` firm `unrealized_gain` by date shows the re-point CLIFF:

| date | firm unrealized_gain | basis |
|---|---|---|
| 2025-07-03 | $80,244,689 | phantom (history) |
| 2026-06-30 | $173,610,218 | phantom |
| 2026-07-01 | $173,848,449 | phantom |
| 2026-07-02 | $174,024,661 | phantom |
| **2026-07-06** | **$13,285,579** | **native (= exact DI-1 native figure)** |

So the 365d delta subtracts a **phantom-basis** year-ago endpoint (~$80M, inflated by the INF_B_03 Finding-1 unit-universe mismatch + fillna(0) phantom) from a **native-basis** today endpoint ($13.3M). A **mixed-basis delta** = a meaningless client-facing number.

Underlying phantom confirmed still live in the derived source: `account_gains` latest partition (2026-07-02) total `unrealized_gain` = **$180.5M** (vs native $13.3M) — Finding 1 (market_value I_B01 raw-txn-units − cost_basis I_B02 canonical-units unit-mismatch: $156.8M; + fillna(0) phantom rows: $23.7M) explicitly DEFERRED as a design item in commit 0ba30a4fd. account_performance's *forward* rows dodge it (native re-point); its *history* does not.

## Blast radius
- AFFECTED: `tax.capital_gains_ttm` + `tax.unrealized_gain_change_ttm` (firm); same computation at per-advisor / per-household / per-client grain (INF_D_02) — all TTM deltas spanning 2026-07-06. (Per-client: 0 of 300 exceed their own AUA, so less glaring per-client, but still mixed-basis.)
- NOT AFFECTED: `book_growth.*` + its quarterly_series — AUA-based (total_aua $178M->$206M), NO re-point boundary -> clean. No visible unrealized chart-cliff in the growth chart.

## Fix direction (DS/CTO — not CVO)
Per Andrew's standing doctrines (raws-over-derived + honest-missing, + "construct the timeseries from the daily PIT native fields"):
1. Backfill `account_performance.unrealized_gain` history from Orion native `tax_unrealized` daily snapshots where they exist -> single-basis (native) throughout -> any TTM delta is well-defined.
2. For dates BEFORE native-snapshot coverage, a 365d delta reaching that far is not single-basis-computable -> honest-missing (null / "unavailable"), NOT a mixed-basis number.
(Fixing INF_B_03 Finding 1 directly is the alternative that also cleans account_gains, but the re-point-to-native path aligns with the DI-1 resolution already chosen.)

## Verdict
DI-1 D-stage belt: **FAIL** (not self-healed). The point-in-time re-point (C_03 forward, C_05) is correct and certified; the TTM/temporal grain is a NEW mixed-basis defect from un-backfilled history. Routed to DS~B + CTO. Not a same-day emergency (a wrong-but-not-catastrophic scalar, no cascade beyond the two TTM fields), but a real client-facing wrong number — should be fixed before the next advisor-facing use of TTM capital gains.
