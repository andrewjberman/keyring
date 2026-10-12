# ADVI_COTBKF round 79 -- L9 grade of CB79ca1-AC2, CB79ca2-AC2 and CB79ca3-AC2

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T02:45:15Z. Row D2-S133.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_79_DRAIN_END_20261012.md @324559b1ec (msg 6393)`. Three reads; nothing built, served or fetched.

| criterion | verdict |
|---|---|
| CB79ca1-AC2, the securities history as it stands | **MET** |
| CB79ca2-AC2, tickers with several names; and the basis value against the split scaling | **MET** |
| CB79ca3-AC2, what wrote the live store | **MET** |

## CB79ca1-AC2: MET

The history is another box's. The worker read the tree only and made no call to it; `covered=0` is written as NOT READ and not as
absent; `not_established` is used for whether the history exists. That is every limb of the criterion.

**This seat's own read closes a gap in its review of PRD v0.10.** That review signed a contract resting on the other box's column
having later splits undone, and said nobody at this desk had read it. This seat has now printed the code that makes the column:
the as-traded close is the vendor's close times every split ratio dated strictly after the day. So the property holds in the
writer's code. It is still a read of code and not of a landed value: by the owning box's own relayed count the series store holds
0 objects and its writer is off, so there is no landed column yet to check.

## CB79ca2-AC2: MET

**The order of the value and the scaling,** printed by this seat at the cited lines: the value is written inside the
substitution; the price input is written; then the split plan runs and is applied, and only under one method. The record's
reading is the code's. It is what PRD v0.10 was corrected on.

**Tickers with several names.** The denominators run down from 1,720 held securities to 769 priced by ticker to 133 on a many-name
ticker; 111 of those carry identical names and are said to be indistinguishable, not wrong; 8 whose own name cannot be identified
are their own class. Not from own rows: 4 securities, 26 measured account-days. Small, and stated with what it cannot tell (the 4
may be old and new labels of one security). Not re-derived by this seat.

## CB79ca3-AC2: MET

The live store object is the earlier version minus 1,623 rows, and it was put by this project's own rewrite of 2026-10-09, read
from that act's ledger entry. Who wrote the earlier version is `not_established`. The criterion asked for exactly that
discipline: which code from the object's columns, which run from a record, and not established where there is none.

This answers row D2-W149-S1 in part: the live object is this project's own, and the object it was cut from still has no author.

## Three rows

- **D2-W152-S1 matters most and is not explained:** for three equities the build's price on the last store day is one half, about
  one seventh and one tenth of the store's own row. Ratios like those are the size of a split. The round's own finding is that a
  point can leave the build marked and unscaled, or be scaled when it should not be. This is the first place that reading meets
  data, and it is outside the funds C-BASIS re-prices. Whether any of the three is held on a measured day was not read.
- **D2-W151-S1** (the build's split step on top of an already split-undone close would scale twice): a reading of two code paths,
  not measured. PRD v0.10 rules the step is not applied to fund points; the row stays open until that is built and shown.
- **D2-W153-S1** corrects an earlier round's class for the store's earlier version. A correction of the record.
