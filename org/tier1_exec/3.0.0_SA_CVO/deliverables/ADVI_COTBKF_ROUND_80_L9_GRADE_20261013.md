# ADVI_COTBKF round 80 -- L9 grades of two judgment criteria

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-13 ~16:4xZ. In bound: `2.0.0_SA_COO~C2` was seated on Andrew's card 6
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_122xZ_ANSWERS_TO_NINE_DELL2_CARDS.md`), so fc10 addendum 2 reaches it.
**Asked by:** msg 7067, packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_80_DRAIN_END_20261013.md` @c47cd08791.
**Result: CB80cb1-AC2 PASS (with one note); CB80cb2-AC2 PASS.**

## CB80cb1-AC2 -- PASS

The record: `deliverables/0.9.0_WK_ADVI_COTBKF~155/THREE_EQUITIES.json` (read by this seat).
- **The price paid decides, with the numbers shown.** Each equity carries `price_paid_check` and `ratios`. For APH, one sale on
  2025-04-22 against the held day 2025-04-21: store 0.9672 of the price paid, build 0.487, served 0.487, so the store is the side that
  matches.
- **"Served" is read from what is served.** `served_price_is` names the minted copy and the 47 partitions. For APH: the minted close
  equals the build on all 48 held account-days, and the 47 partitions hold no APH name.
- **A cause only where a step equals a split ratio on the split's date.** All 5 are `not_established`. The steps are shown with
  `steps_within_1pct_of_split_ratio` 0, and vendor split dates are recorded as not on disk, with the reason.
- **No account id or amount.** The record has 0 runs of 8 or more digits and no amount key. The one price paid shown is a per-share
  trade price, which the criterion's first clause requires.
- **Note (not a fail):** the top-level `served_error_account_days` = 48 counts APH only, although CTVA's entry records 115 served
  account-days at 0.15 of the store. A reader of the top-level figure undercounts the served errors. The packet states both.

## CB80cb2-AC2 -- PASS

The record: `deliverables/0.9.0_WK_ADVI_COTBKF~156/FUND_CLOSES_READ_BACK.json` (read by this seat).
- **The test is round 76's, unchanged:** the record's `test` text is byte-equal (5,070 characters) to the rule in round 76's record
  `deliverables/0.9.0_WK_ADVI_COTBKF~140/FUNDS_BY_TRADES.json` (this seat compared them).
- **Presence is counted against held trading days with the denominator:** 5,730 present of 20,718 held, 14,988 absent, split by cause.
- **The split arm is worded as ruled:** "rests on dell1's word alone ... was not tested and is not claimed as passed."
- **Nothing re-priced or re-minted:** reads only, per the packet.
- The 33 runs of 8 or more digits are CUSIPs (public security ids) and decimal digits, not account ids.

-- 3.0.0_SA_CVO
