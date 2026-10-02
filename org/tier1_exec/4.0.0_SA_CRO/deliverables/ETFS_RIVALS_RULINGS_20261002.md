# ETFS_RIVALS open-call rulings -- 4.0.0_SA_CRO~RV, 2026-10-02

Authority: Andrew-direct ~04:57Z, "CRO~RV has adjudication ability for any open calls on the ETFS_RIVALS" (record
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261002_045xZ_RV_TEAM_ETFS_RIVALS_ADJUDICATION_AND_EGRESS_TONIGHT.md`).
One section per call, appended as calls arrive. Andrew may overrule any ruling.

## CALL 1 -- RIV-rk-1 price source (2.0.0_SA_COO~RV msg 28214, 05:13Z)

**Call.** G4 `security_market` holds one date (2026-09-29), so rk-1's MTD/QTD/YTD/R30 contribution reads almost all
`missing` and the rankings component is empty for the demo. COO recommendation: when G4 has no price, fall back per
(security, day) to the holding's own reported price, `market_value / quantity` from the fund's G1 report on d and d-1.

**Ruling: ACCEPTED, with five conditions.** The basis is sound for this measure. Contribution is to the FUND's return,
and the fund's own reported valuation is the price its NAV used, so within one fund the implied price is consistent.
G1 carries `quantity`, `market_value` and `position_type` per position (`gold_canonical_shape.py:133`, `:485`, `:584`).

1. **One source per daily return.** Source order per (security, day): `g4_tri`, then `g4_close`, then `holding_implied`,
   else `missing`. A day's return uses the SAME source at both endpoints (d-1 and d), never one source at each end.
2. **Only a priceable position gets an implied price:** a security holding (not cash, not a derivative, swap, future,
   option or forward), with `quantity > 0` and `market_value` non-null on both d-1 and d. Anything else is `missing` with
   its reason.
3. **Corporate-action guard (refused, never inferred; the RIV-h-5 doctrine).** When `quantity` changed between d-1 and d
   AND the implied price ratio departs from 1 by more than a PROVISIONAL band (`|p_d / p_(d-1) - 1| > 0.25`, kept in
   `guardrails_config.json`), the day is `missing` with reason `corporate_action_suspected`. A split's signature is
   quantity times k with price divided by k, and pricing it would give a false -50% contribution on a 2:1 split.
4. **No gap filling.** A return exists only where the fund has reports on both d-1 and d (trading-day adjacency,
   `lib/trading_calendar.py`). A missing report leaves that day unpriced; nothing is interpolated.
5. **Contract column, at row grain.** A contract row aggregates many days, so a single per-day source does not fit it.
   The `price_source` column takes the one source shared by every priced day of the row, else `mixed`, else `missing`
   (enum `g4_tri | g4_close | holding_implied | mixed | missing`). Add `n_days_holding_implied` beside `n_days_priced`.
   `claim` stays `INFERRED`. Readers stay column-optional (A1 ruling 3).

**Disclosure (demo-facing).** Implied returns are price-only. They exclude dividends and are measured at the report's
valuation date. Where `price_source` is present, the ranking tables state their basis in the caption (for example "priced
from the funds' own reports"), so the ranking is never read as a total-return figure.

**What this does not settle.** G4 history still lands in round 6. When it does, `g4_*` takes precedence automatically
and the rankings re-rank. The day-over-day shift from that re-rank is expected, not a defect.

**Carrier.** The issuer amends the rk-1 cell text and the `holding_contribution` contract in the decomposition, and the
order's text, in its own commit. That commit names the gate limb that graded the change (rule 27, L5/L6 issuer amendment).
