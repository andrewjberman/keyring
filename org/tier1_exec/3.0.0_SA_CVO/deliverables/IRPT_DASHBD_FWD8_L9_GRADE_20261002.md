# IRPT_DASHBD FWD-8 -- L9 grade on the round-4 like-day tie-out (3.0.0_SA_CVO, 2026-10-02 ~18:5xZ)

Asked by `2.0.0_SA_COO~P` msg 104336 (drain end
`deliverables/2.0.0_SA_COO~P/IRPT_DASHBD_ROUND4_B_DRAIN_END_20261002.md`, DB-b-10 merged @8b1df51795).

**FWD-8 (PRD :91-96):** "A return figure a person can defend: total return, before advisory fees and labelled so, and a
day the data cannot support says so instead of showing a plausible wrong number. DONE WHEN EXERCISED -- the 49 Financial
figure tied out against Black Diamond's own return. ACCEPT for an account and window the two returns agree within a
tolerance Andrew accepts and every day they disagree carries a stated reason; a misdated or missing deposit can never
show up as a huge gain or a total loss; the old 'time-weighted, net of ...' label [is gone]."

## Verdict: NOT REALIZED. EXERCISED yes; ACCEPT not met on two of its clauses.

| clause | this seat's read | result |
|---|---|---|
| EXERCISED: tied out against Black Diamond's own return | 3 performancePeriod calls under Andrew's card-4 word (@0abef798f7); 14 pairs on 3 of 5 accounts (2 have no BD id), each a maximal gap-free run by `lib/trading_calendar.py`; 14 of 14 like-day (BD daysHeld = Opal linked days) | MET |
| the record reproduces | the largest pair (0027265115, 2026-06-25..07-06) re-derived both ways: Opal's served gold, 7 of 7 days linked = +3.4935%; BD's raw response `timeWeightedReturns.return` 0.022805706 = +2.2806%; both equal the record | MET (1 of 14 re-derived) |
| agree within a tolerance Andrew accepts | measured: median abs_diff 0.1637 pct, max 1.2130 pct, 14 of 14 pairs; 10 of 14 under 0.35 pct; 3 above 0.45 pct (1.21, 0.71, 0.46). No tolerance is ruled: PRD Q2 (:322-326) makes it 1.0.0_SA_CTO's ruling on the measurement (round-1 ruling 23 refused 3.7 pct), and Andrew's word overrides | NOT GRADABLE until ruled. This seat does not set the number; the measurement above is the input |
| every disagreeing day carries a stated reason | the tie-out has no reason field on any of its 14 pairs. The largest has a findable cause: Opal books income +0.4627 pct on 06-25 alone, BD nets the window's income at -2,470.31 on an account about 47 pct short (as of 10-01): an income-sign difference on short positions (inferred). Row IRPT_DASHBD-S22 | NOT MET |
| a misdated or missing deposit never shows as a huge gain or total loss | C-GUARD in the served gold (FLOW_UNRECONCILED fallback, plausibility band) graded at round 1 (ADJUDICATION_v1 / REMEDIATION_v1: S5 closed, 1,071 emitted returns, 0 outside the band); not re-read this round | MET on the round-1 read |
| the label | the dashboard face (portal item 39b7a0fc on PROD v2.1.194) says "before advisory fees", "Data through" (DashboardPerformance.tsx:241); graded on a test run, no signed-in page | MET on a test run |

## What closes FWD-8

1. `1.0.0_SA_CTO` rules `tieout_tolerance` from this measurement (PRD Q2), or Andrew gives his number.
2. The tie-out states a reason for every pair outside it; for 0027265115's 06-25 window, the income treatment of short
   positions is read in the producer and either fixed (dividends paid on shorts as negative income) or stated as the
   reason. Row S22, owner `2.0.0_SA_COO~P`.
3. The two unmapped accounts (0035940058, 0091939812) stay out until they have a BD id; 3 of 5 is the sample.

**Limits.** 1 of 14 pairs re-derived end to end; the other 13 are the record's. The short allocation was read at the
2026-10-01 as-of point, not in June. No page was walked. The population tie-out (P-5) needs another vendor word.

-- 3.0.0_SA_CVO

## CORRECTION, 18:5xZ -- the count of pairs within 0.35 pct was wrong

This grade's agreement row said "10 of 14 under 0.35 pct; 3 above 0.45 pct". The record reads **11 of 14 within 0.35
pp and 3 beyond**: 0027265115 2026-06-25 (1.2130), 0084073310 2026-08-21 (0.7078), 0027265115 2026-04-09 (0.4555). The
pair at 0.3307 (0076459710, 2026-08-11) is within. Read from `TIEOUT_49F_BLACKDIAMOND_R4.json`, 14 pairs, at 18:5xZ.
The CTO's ruling (batch 181 @57e16650b5, msg 104363) quotes the wrong count ("10 of 14", "the four pairs beyond"); the
tolerance it rules (0.35 pp) is unaffected, and the pairs owing a stated reason are three, not four.

**FWD-8 under the ruling:** still NOT REALIZED. The three pairs beyond 0.35 pp owe stated reasons; S22 (the short
account's income sign, the largest) is a defect to fix and re-measure, never accept.

-- 3.0.0_SA_CVO

## Round 8 re-grade, 02:xZ 2026-10-03 -- FWD-8 on method_version 2 (~P msg 104505, DB-b-15 merged @ce1d4a0530)

**Verdict: ACCEPT MET ON THE METHOD; NOT REALIZED AS SERVED.** Method version 2 is on CLOUD and was measured locally. The
served gold is still version 1, and the record says nothing is served (`IRPT_DASHBD_ROUND8_B_DRAIN_END_20261003.md:53-60`).
FWD-8 is "a return figure a person can defend". The figure served today for 0027265115 06-25..07-06 is still the
1.21 pp one, and its cause (C-VALUE leaving out the margin balance) is an Opal defect under batch 181. The grade
realizes when the P-2 packet serves version 2.

| clause | this seat's read | result |
|---|---|---|
| tolerance | 0.35 pp, ruled by batch 181 under PRD ruling 11 | ruled |
| within | `TIEOUT_49F_BLACKDIAMOND_R8.json`: 10 of 14 at or under 0.35 pp; max 0.4998 (was 1.2130) | 10 of 14 |
| beyond, with reasons | 4 of 4 carry one (below); each reason re-read against Black Diamond's raw response (`~1/RAW_BD_PERIOD_<acct>.sanitised.json.gz`) | MET |
| defects fixed and re-measured | S22's cause was the missing margin balance, not the income sign this seat inferred at round 4. Fixed in the producer (DB-b-15), re-measured, not served | fixed on CLOUD; NOT SERVED |
| label and guard | unchanged since round 4 | MET on earlier reads |

**The four pairs beyond 0.35 pp, re-derived:**

| pair | stated reason | this seat's read | holds |
|---|---|---|---|
| 0027265115 06-25..07-06, 0.4738 | MARGIN INT ADJ is return (batch 195); BD books it as a flow | Read from Schwab silver (`opal-data-assets/schwab/08335338/silver/dim_balance/`): 06-24 965,341.13 + 4,816.69, and 07-06 999,065.64 - 2,185.99. Equity ratio 0.027544 equals the producer's figure. BD 0.022806; difference 0.4738 pp. BD value minus accrual minus equity = 0.00 at both endpoints. BD netAdditions 4,402.22 | YES |
| 0076459710 08-11..08-19, 0.4998 | BD accrual outside Opal (batch 193) | BD accrual 28.88 -> 6,051.28 = +6,022.40 = 0.4999 pp of BMV; residual 0.0001 | YES |
| 0076459710 08-21..09-09, 0.4608 | the same, reversing | accrual -5,766.11 = 0.4501 pp; income 5,659.35 received in this window; residual 0.0107 | YES |
| 0084073310 03-20..08-04, 0.4045 | BD net of a fee; Opal gross (C-FEERAIL; FWD-8's own "before advisory fees") | fees 3,020.96 = 0.3961 pp of BMV; EMV/BMV - 1 = 0.239661 = BD's reported return, so the fee sits inside BD's return; residual 0.0084 | YES |

**Ruling text.** Batch 193's grounding says that, with the margin balance added, "the three pairs beyond 0.35 pp fall to
0.0044, 0.0264 and 0.0493 pp". The 0.0044 is the counterfactual with the 4,429.53 credit also treated as a flow. The
margin balance alone gives 0.4738. Batch 195 states the pair correctly at about 0.47. The other two figures match R8.

**What closes FWD-8.** The P-2 packet serves method version 2: producer re-pin, landed gold rewritten, method row. Then
this seat reads one pair from served gold (`method_version` = 2 on the rows) and reproduces it.

**Limits.** One pair was re-derived from silver; the other three were checked on the Black Diamond side only. Opal's
per-day flows were not re-read. Rows W2-S1..S3 are read at the compile.

-- 3.0.0_SA_CVO

## FWD-8 REALIZED on served gold, 18:5xZ 2026-10-03 (P-2 window `irpt-p2-window-20261003`, leg V's FWD-8 pair)

P-2 is served: the A1-A5 legs rewrote 562 days of `account_return_daily` on method_version 2 and published 6,863 accounts;
the method row `dim_return_method/method_version=2` landed at 17:50:57Z (~P msg 104695; ledger legs A1-A10, B1 and B2
closed). PROD portal is 98a98e70 (v2.1.197).

| read (served gold, `opal-data-49financial/irpt/49financial/gold/account_return_daily/`) | result |
|---|---|
| 0027265115 2026-06-25..07-06: 7 of 7 trading days, method_version 2 on every row; chained `total_return_daily` 0.027544; Black Diamond 0.022806; 0.4738 pp | equals the round-8 measurement and this seat's silver re-derivation (a108c6bd93) |
| 0076459710 2026-08-11..08-19: 7 of 7, version 2; 0.037748 against 0.042747; -0.4998 pp | equals round 8 (accrual, stated) |
| 0084073310 2026-08-21..10-01: 29 of 29, version 2; 0.069120 against 0.068856; 0.0264 pp | equals round 8 (within) |
| method row: `method_version=2/data.parquet`, 22 columns; sha256 of the sorted `name:type` lines = 73e80ef7.. = contract 0.3.0's `schema_hash`; `tieout_tolerance_proposed` typed double | PASS (row W5-S2's dependency held) |

**FWD-8: REALIZED.**
- The served figure is the one this seat graded on the method: 10 of 14 pairs within 0.35 pp, and the 4 beyond carry
  stated non-defect reasons under batches 181, 193 and 195 and C-FEERAIL.
- The label ("before advisory fees") and C-GUARD were graded earlier.
- One pair of each kind (beyond-with-reason, accrual and within) was reproduced from served rows.

**Clocks advanced in place (state fields only):**
- S22 (REMEDIATION_v2): REMEDIATED and closed. Its 1.21 pp pair now serves at 0.4738 pp with the stated reason.
- W1-S18 (REMEDIATION_v3): REMEDIATED and closed. Version 2 is served, and the closing read named in the row is done.
- W1-S19 and W2-S3 (REMEDIATION_v3): REMEDIATED and closed. Contract 0.3.0 carries the four columns, and the served row's
  hash matches it.
- W5-S2 (REMEDIATION_v4): REMEDIATED and closed (hash above).
- Not moved: W1-S12, W1-S13, W1-S14, W4-S1 and W4-S2 have their own closing reads, which this seat makes at the window's
  V leg or the first scheduled fires. W1-S17 closes at A2's read of a short DIV debit in served income, not yet made.

**Limits.** 3 of 14 pairs were re-read from served rows; the other 11 are the round-8 record, on the same method now served.

-- 3.0.0_SA_CVO
