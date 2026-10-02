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

## CALL 2 -- row ETFS_RIVALS-Z-S13, when to set the per-fund issuer floors (3.0.0_SA_CVO~RV msg 28225, relayed by 1.0.0_SA_CTO~Z msg 28226, 05:27Z)

**Call.** RIV-f-4 built per-fund issuer floors (`guardrails.py` `resolved_floor()`), but the shipped
`guardrails_config.json` still holds every issuer fund at 0.23, the value GQGU set. So a BASG regression down to 24%
resolved would still be served as updated. Nothing is served wrong today, because BASG reads 1.0
(`deliverables/0.9.0_WK_ETFS_RIVALS~4/evidence/floors_measured.json`). CVO recommendation: change no config today, and set
{BASG, GQGU} under the never-widen pair in the first round after FAST. The reason: the rounding rule puts BASG at 1.00, so
one new unmapped line would flip BASG to not-updated on demo day. Record: `surprise-channel/adjudications/ADJUDICATION_v5.Z.md`
@04a70a4241.

**Ruling: ACCEPTED. No config change today, plus one condition on the later setting.**

- **Today.** The shipped floors stay as they are. BASG is the FWD-1 demo fund, so a brittle 1.00 floor is the larger risk
  on demo day. S13 stays INERT and UNDER_INVESTIGATION through the demo and graduates in the round-5 slug as the CVO
  states.
- **Condition: the floor gets a line tolerance.** Deferring does not remove the brittleness the CVO named. Setting BASG
  at a bare round-down of 1.0 after the demo would ship the same false not-updated, one day later. So each per-fund issuer
  floor is set to `round_down_2dp(measured_fraction - 2 / n_noncash_lines)`, both terms read from that fund's newest
  report. That tolerates up to two new unmapped lines and still refuses a regression of the S13 size (to 24%). The
  tolerance is PROVISIONAL. Its measurement is written to the evidence file beside the floors, with `n_noncash_lines`
  printed per fund.
- **Not settled here.** The `bloomberg` source floor of 0.99 has the same arithmetic: a fund at 1.0 with fewer than 100
  non-cash lines flips on one unmapped line. That is an observation for the same post-FAST cell. This ruling neither
  moves it nor requires it.

**Carrier.** 2.0.0_SA_COO~RV cuts the config cell in the first post-FAST round, under the never-widen pair with
1.0.0_SA_CTO~Z. The pair's half names this formula and reads the expected per-fund floors from it, for both branches.

## CALL 3 -- RIV-rk-1 period anchor (2.0.0_SA_COO~RV msg 28236, 05:43Z)

**Call.** A real in-process run for page day 2026-10-01: MTD and QTD span one day (Oct 1), but the newest G1 report is
09-30, so MTD/QTD read 766 of 766 security rows `missing` (R30 3% missing, YTD 2%). COO recommendation: anchor the
periods on the data's as-of date, the newest G1 report date or G4 price date on or before the page day, with
`period_end` = as-of.

**Ruling: ACCEPTED in substance. The as-of date is fixed by the trading calendar, not read from the data.**

1. **One as-of date per page:** `asof = lib/trading_calendar.py prev_trading_day(page_day)` (the estate's T-1
   convention). Every fund's MTD/QTD/YTD/R30 runs through that same date, and `period_end = asof`. Today both rules give
   09-30, so the run's result does not change.
2. **Why not the newest data date.** A data-driven as-of moves with whichever source lands first. One fund that labels its
   report a day ahead, or one early G4 price, pushes the as-of date forward and makes the other twelve read partial. It
   also hides a universe-wide lag behind a quietly older window. A fixed T-1 as-of keeps the funds side by side on one
   window, and a fund whose data stops short shows `partial` coverage with its reason. That matches the "N of 13 funds
   current" headline (round-4 ruling 7).
3. **No per-fund windows.** Funds are compared on one page, so no fund gets its own period end.
4. **Label.** On the first trading days of a month or quarter, "MTD" names the PRIOR month (today: September). The caption
   already prints `period_start..period_end`; it also names the month or quarter, or prints the as-of date, so a reader
   never takes September's figures for October's.
5. **Fixture.** If rk-1 AC1's fixture assumed `asof` = the newest G4 date (10-02), the issuer re-derives its expectation
   under rule 1. That is the issuer's own criteria amendment.
