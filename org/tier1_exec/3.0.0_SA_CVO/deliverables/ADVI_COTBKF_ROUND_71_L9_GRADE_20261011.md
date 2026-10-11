# ADVI_COTBKF round 71 -- L9 grade of CB71bs1-AC2 (the dividend-adjusted fund series)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T18:22:31Z. Row ADVI_COTBKF-D2-S122.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_71_DRAIN_END_20261011.md @70281800e0 (msg 5530)`. Record graded: the worker's `DIVIDEND_ADJUSTED_SERIES.md` and `.json` @363f03e5fc.

**Verdict: CB71bs1-AC2 MET for the nine and for the count as a count. One limb is not met for 63 of the 72: their reading does not
rest on an independent source.**

## This seat's own check, on a third source

The worker's reading for the nine failed the order's own example threshold, and its rule was set after its first run. A reading
on those terms needs a check that the rule did not shape. This seat made one.

When a distribution is reinvested, the custodian's row carries the dollars and the shares bought. Dollars over shares is the price
the fund actually traded at that day. It is not the store's series and it is not the vendor's.

| | |
|---|---|
| reinvestment rows for the nine | 1,121, in 221 events |
| events with a build close on the same date | 92 |
| build close BELOW the traded price by more than 0.5 percent | **87 of 92** |
| build close above it by more than 0.5 percent | 1 |
| funds of the nine that show it | **9 of 9** |
| lowest ratio of build close to traded price | 0.47 |
| the ratio over time | higher in the last third of each fund's dates than in the first, in 9 of 9 |

So the reading holds on a source the rule never touched: for these nine the build's close is not the price the fund traded at, it
is lower on the earlier dates, and it is near the traded price at the newest ones (2026). That is the shape of a
back-adjusted series.

**The size is large.** The lowest ratios, near half, are on 2020 dates. The worker's slope of 1.6 to 2.3 says the adjustment is larger
than the funds' distributions imply; this check did not measure the distributions and is consistent with that reading.

## The four limbs

| limb | verdict | why |
|---|---|---|
| distributions from a source independent of the close series | **MET for the nine. NOT MET for the other 63** | The nine use the custodian's distribution rows. The table-wide test reads the vendor's adjusted close over its own unadjusted close, and the store's close came from that vendor. The record says so |
| each reading follows from the comparison; UNDECIDED where it does not | **MET** | The nine are confirmed above. The 124 untested, one of them undecided, are stated as untested and none is counted as clean |
| the count states tested and untested | **MET** | 270 series: 73 substituted, 197 left; 73 tested, 72 read adjusted, 1 not; 124 untested, by reason |
| no correction sized on what was not tested | **MET** | No correction is sized at all |

## What this seat did not do

- The 92 matched events are of 221; the other 129 fall on dates the local price table does not hold for that security and were not
  examined. The price table is the round 34 build's; the record says the as-traded basis changes no date for the nine.
- The 63 other series, the reach (3,187 measured account-days) and the untested 124 are the worker's and were not re-derived.
- No return was recomputed, by the worker or by this seat.

## For the analysis

The size matters more than the label. On real trade dates these closes are light by up to half.
The basis rule left them on the store because they matched neither series it knows. A series that matches neither is the one that
most needs a decision, and the rule's default for it is to keep it.
