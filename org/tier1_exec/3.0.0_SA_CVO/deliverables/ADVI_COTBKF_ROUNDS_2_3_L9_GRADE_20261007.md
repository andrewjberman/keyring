# ADVI_COTBKF rounds 2 and 3 -- L9 grade of the three judgment criteria

**Grader:** 3.0.0_SA_CVO, 2026-10-07 ~03:4xZ. **Orders:** TO-CB-b-3, TO-CB-c-3, TO-CB-c-4, all `complete`.
**Rows:** `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/adjudications/ADJUDICATION_v2.md` and
`remediations/REMEDIATION_v1.md` (co-committed). Every figure below was read at this seat, not taken from a report.

| criterion | grade | one line |
|---|---|---|
| CB2b3-AC3 (price-store census) | **NOT MET** | A CUSIP-keyed daily closing-price store was not named, and no position-level store was read. |
| CB3c3-AC3 (crosswalk) | **MET** | Every checked match holds; no not-matched reason hides a match at the rule's bar. |
| CB3c4-AC3 (account links) | **MET** | All 180 links hold on both sides; one client reads as one line across two changes. |

## CB2b3-AC3 -- NOT MET

The criterion asks that an UNPRICED security be unpriced by Opal, not merely by the stores the cell knew.

- **Denominator.** The account has 40 buckets. The census names stores in 10. I listed the other 30.
- **The missed store.** `opal-data-49financial`, `gold/advi/canonical/canonical_positions/date=<d>/data.parquet`: 565 daily
  partitions from 2024-07-08 to 2026-10-05, with `cusip` and `closing_price` on every row.
- **Its reach.** The 2026-10-05 partition alone prices 912 of the 4,634 Commonwealth CUSIPs, matched by CUSIP:

  | asset type | priced in that one partition | universe |
  |---|---|---|
  | Equity | 572 | 1,830 |
  | ETF | 193 | 349 |
  | Mutual Fund | 137 | 978 |
  | Mutual Fund (Closed End) | 6 | 99 |
  | Fixed Income | 3 | 778 |
  | Alternative Investment | 1 | 22 |

- **Why it matters.** The census matched 0 securities by CUSIP in its five large stores, and 0 Fixed Income. Four more
  position-level stores are named `DERIVED_NOT_READ` without a read, although a custodian mark on a held position is a
  close for that security on that day.
- **Not measured here.** How many of the 912 are new to the 1,506 already priced, and the covered days inside the needed
  window. The re-run answers both.
- **A ruling is needed first.** The store belongs to another firm (49 Financial). The cross-firm law forbids a pipeline
  tree referencing another firm's data. The census already reads the bd and inf price files for a Cottonwood universe,
  and row W6-S2 says that question was never resolved. It is 1.0.0_SA_CTO's to rule whether MARKET prices are within that law.

The other 29 unnamed buckets hold no per-security daily price series. The `holdings_performance_daily` and
`account_return_daily` tables are account-level; `insurance_nav_current` is one current value per insurance account.

## CB3c3-AC3 -- MET

- All 439 matches are rule R2. No current account is matched twice.
- **Positions-basis matches (9):** recomputed with my own code from the 2026-06-23 positions and the current account's first
  holdings: 9 of 9 hold.
- **Rebuilt-basis matches (430):** the current account's first holdings fall 0 to 10 days after the in-kind exit date in
  430 of 430.
- **Not matched:** no row scores 0.8 or more. Seventeen score 0.65 to 0.8 and are listed with their candidate and score.
- **One gap, below the bar.** The cutoff (last activity before 2026-04-22) keeps an account from being scored. B3S775239
  left in kind on 2026-04-07. Three current accounts hold the same quantity of 3 of its CUSIPs: under the 80% bar, so
  not a hidden match, but the reason "closed before current history" is not what happened to it. Row W10-S4 carries it.

## CB3c4-AC3 -- MET

- **Every link checked.** 2,652 of 2,652 evidence items have the exit row on the old account (within 20 days of its last
  trade) and the receipt on the new account (one `li` row, or the same-day sum of `li` rows), each within 0.001.
- 175 of 180 links share the advisor; 164 are a `cv`-prefixed number moving to the same number without the prefix.
- **One line across a change (FWD-9's DONE WHEN):** `cvB3S606716 (2013-08-13..2016-02-08) -> B3S606716 (2016-02-05..2016-11-01)
  -> 0QF886265 (2016-10-25..2021-01-04)`.
- **The applied rule differs from the order's literal rule,** which gives 0 links because the exit rows empty the book. The
  applied reading (holdings just before the in-kind exit) is printed in the output and is what the 2,652 items verify.
- **Limit, row W11-S2:** links exist only for the 459 accounts that ended before 2018. Of the 148 targets that are not old
  accounts, 46 stopped trading before 2026, so those clients' lines may not reach their newest account.

## The three cache hazards

W6-S4, W10-S3 and W11-S3 were ARMED: each real-data criterion met its 120-second bound only against a cache in a worktree
due for removal. 2.0.0_SA_COO~C copied the caches to the shared tree (rows S4, S5, S6). I ran all three criteria there:
9.7 s, 6.4 s and 3.1 s, each rc 0 with its expected line. All three are DISARMED and closed. A clean tree on another
device needs one cold run first; the price read took 5 to 19 minutes cold.

## For the round analysis

1. The cross-firm ruling for market prices, then the coverage re-run (row W6-S2).
2. The rule-30 ruling for a new script that reads an old store's address from a record file under `org/` (row W6-S5).
3. Links for every account that ends before 2026-06-23, so a line reaches its newest account (row W11-S2).
4. Score in-kind exits whatever their date; 17 near-matches wait for a person (row W10-S4).
5. Gate precision, for the gates' owner: the silver-ids check keys on a `build_` name prefix, and the naming gate grades
   a slash-bearing label as a key (row W7-S1, dismissed).

-- 3.0.0_SA_CVO
