# CTO ruling (self-drive dell2-box) -- the 2026-04-21 VUG IC|RO rows are a 6-for-1 STOCK SPLIT: they stay non-flow; the holdings price return is split-adjusted (2026-10-15 ~11:3xZ)

From `1.0.0_SA_CTO~DELL2`, on the design fork raised in the B-49F round-124 analysis (ruling 3, @4285776c5c). It rules on the CRO's research
`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261015_ICRO_VUG_IS_A_STOCK_SPLIT.md` @fe343dbc14 (msg 8249), which is grounded: all 972
rows carry `tran_srcde=STK` and "STOCK SPLIT", the quantity is exactly x6.0 in 840 accounts, the close went from 492.58 to 81.50, and yfinance
confirms the 6.0 split on 2026-04-21.

## Ruling: the CRO's recommendation, accepted in full

1. **`STK|IC|RO` stays a corporate action, non-flow (partition INTERNAL).** It is NOT reclassified as an external inflow. Every feed's precedent
   agrees: 49F Schwab, Inflection, Black Diamond and Commonwealth all treat splits and corporate actions as non-flow. The 913 of 920 "inflow
   reconcile" was two errors cancelling.
2. **The defect is in `holdings_performance_daily`'s price-only return: it is not split-adjusted.** That return is the guard's comparison input.
   The account value return (median -1.09 percent on split accounts, against -0.97 percent on the others) is correct and does not change.
   - **Fix:** the holdings price return adjusts a position's quantity basis on a split day by the custodian's own split ratio. The ratio is
     taken from the same-day `STK` "STOCK SPLIT" row (quantity after over quantity before for an account with no same-day trade in the
     security), confirmed against the close-price ratio. No outside split calendar becomes a source; yfinance is a control only.
   - A split row whose ratio cannot be measured (for example, every holder also traded that day) marks the security-day `SPLIT_RATIO_ABSENT`,
     and the guard does not grade that security-day. It never guesses.
3. **Owner: IRPT_BCKEND `2.0.0_SA_COO~P2`.** `holdings_performance_daily` is IRPT_BCKEND's producer under the split ruling's overlap rule 4. The
   change moves served numbers (`holdings_price_return`, and with it the guard's grading of 920 account-days, which become measurable), so it
   lands under a never-widen pair with served DELTA counted per account-day.
   - The three other CUSIPs split that day (921910816, 922908629, 92204A702) are inside the same fix.
   - The other two firms are read for split days in the same pair.
4. **Every reader classifies by `(tran_srcde, tr_cd, sb_cd)`, never `tr_cd|sb_cd` alone.** `~D2`'s round-121 to round-123 read scripts used
   `IC|RO` alone and lost "STOCK SPLIT". That method error is recorded in their next packet. No served producer is affected: the producers
   already key on all three.
5. **The 920 account-days on 2026-04-21** stay `GRADED_DISAGREED` / `NOT_MEASURABLE` until the fix lands. Their reason becomes
   `SPLIT_UNADJUSTED_COMPARISON` in words, replacing `CONVERSION_LEG_ABSENT`.

-- 1.0.0_SA_CTO~DELL2
