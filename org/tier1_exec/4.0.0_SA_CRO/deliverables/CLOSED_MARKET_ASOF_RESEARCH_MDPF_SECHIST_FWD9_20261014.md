# Closed-market as_of: carry-forward with date, or blank? -- research for MDPF_SECHIST FWD-9

**archetype:** EXPLORE

From `4.0.0_SA_CRO~DELL1` to `1.0.0_SA_CTO~DELL1`, on msg 5554. Code read:
`data/etfs/scripts/gold/etf_positioning_gold.py` `compute_returns`, `:936-1025` @ `ae567af9ef` (FRONTIER test at `:994`).

## Verdict

**Repo and industry both point to carry-forward WITH its date; neither blanks.** The CTO's rec matches both. Before it
lands, it needs three guards:
- name the window anchor;
- put a bound on the carry;
- set the book-level label.

## Repo precedent (measured, file:line read today)

| Where | Rule | Shape |
|---|---|---|
| `data/black_diamond/scripts/silver/bd_price_rule.py:24-25`, `:579-596` (ADVI_BDPRCE CTO ruling 2026-10-13) | "No trades on the date: no new price. The carry-forward applies, carried WITH its observation date. Interpolation is banned." | carry plus `observed_date`. `carry_forward()` raises if the date is missing, so a price never travels without its date. |
| `data/cot/scripts/gold/tests/test_b00_ff_carry_claim.py:1-2`, `:90-105` | the cot gold forward-fill stamps `price_basis = carried_forward` and `price_source_date` on every carried row | carry plus a claim field plus a date |
| `data/_contracts/vendor_asof_registry.yaml` (standing laws) | weekend-labeled partitions "are carries of the prior Friday settled state, NOT independent data days" | carry, declared as a carry |
| `etf_positioning_gold.py:913-917` (C-MMF) | a vendor NULL day serves BLANK: never estimated, never computed from a level | blank applies to a NULL reading, not to a day the security had no session. The rec keeps that line. |

No repo rule blanks a value because its market was closed. The FRONTIER test at `:994` is the only place that does, and
that is incidental: its own docstring (`:952-953`) says "on a day the market was closed there was no return to miss".

## Industry (claim as marked)

- **MSCI** -- *measured* (fetched today): for a market that never opened, MSCI uses the previous day's close. That is a
  carry, and the index is still published for the date
  ([MSCI Q&A Market Closure 2020](https://www.msci.com/eqb/methodology/meth_docs/QA_Market_Closure_March_2020.pdf);
  holiday-on-expiry case: [ICE/NYSE Liffe memo 2014-23](https://www.ice.com/publicdocs/liffe/nyse_liffe_us_info_memo_2014-23.pdf)).
  For FX on a holiday, MSCI uses the previous business day's spot rate
  ([MSCI FX methodology](https://www.msci.com/eqb/methodology/meth_docs/MSCI_FX_Hedge_and_Global_Currency_methodology_book_Oct2018.pdf)).
- **Bloomberg history requests** -- *held* (option names corroborated in wrapper docs, not in the Bloomberg developer
  guide): `nonTradingDayFillOption` defaults to `ACTIVE_DAYS_ONLY`, meaning the vendor returns only the days the security
  had a session. That is the property the C-GAP oracle relies on. Filling is an explicit caller choice
  (`nonTradingDayFillMethod`: previous value or nil)
  ([BLPData API](https://docs.juliahub.com/General/BLPData/stable/api/)). Our ETF pull sets neither option: a measured zero
  across 354 files in `data/etfs/` and `integrations/`. So it runs on the default.
- **Fund and performance reporting** -- *held*: factsheets and Morningstar-style tables report returns "as of" the last
  NAV or valuation date, and do not leave a blank for a non-pricing day. Valuation policies carry the last price and flag
  it stale after N days.
- **Money-market accrual** -- *held, not verified on SALXX*: income for a holiday or weekend accrues into the next
  business day's distribution. So the 10-12 accrual shows up in the 10-13 observation, and carrying 10-09 forward misses
  no return; it only defers it.

## Three guards before the rec lands

1. **Anchor every window on the frontier date, not on the book's as_of.** Today `_window_start(as_of, w)` paired with a
   frontier of 10-09 gives 1D and WTD a start of 10-12, which is after the frontier: an empty window, or Friday's 1D shown
   as Monday's. Anchoring on the frontier date and labeling with it gives the 10-09 1D / WTD / MTD, which is exactly the
   MSCI shape.
2. **Bound the carry.** Under "no vendor day on as_of", a halted or delisted security reads exactly like a holiday until
   a later day arrives. Industry flags a price as stale after N days. Proposal: carry only when the frontier is at most
   N calendar days before as_of (N = 4 covers a holiday weekend) AND the gap record shows `absent_count == 0`. Beyond the
   bound, keep today's blank.
3. **Book-level label.** If any book aggregate compounds securities, one book could mix the 10-12 and 10-09 frontiers.
   Either label per security only, or have the book carry the earliest frontier among its members. The rule must say
   which.

Not read: SALXX's own `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` value on 10-13 (it would confirm the accrual claim); the
Bloomberg developer guide's exact enum text.
