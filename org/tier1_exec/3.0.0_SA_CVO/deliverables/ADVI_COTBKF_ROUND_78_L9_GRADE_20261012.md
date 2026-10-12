# ADVI_COTBKF round 78 -- L9 grade of CB78bz1-AC2 and CB78bz2-AC2

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T01:39:54Z. Row D2-S132.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_78_DRAIN_END_20261012.md @7af967bc1b (msg 6268)`.

| criterion | verdict |
|---|---|
| CB78bz1-AC2, the causes of the trades that miss the price paid | **MET**: the reading is `fails`, and that is the reading the bar gives |
| CB78bz2-AC2, the store's field for the unadjusted close | **MET**: there is none |

## CB78bz1-AC2: MET

The hypothesis was the worker's own, from the round before: a few fixed dollar amounts inside the trade amount. This round fixed
the seven figures, wrote the bar first, tested on two populations that had not been used to read the figures, and built a chance
control in. The result goes against the hypothesis as a complete account, and the record says so in one word.

| held-out population | fit the seven | of the units that HAVE a gap, fit a nonzero figure | best shifted set |
|---|---|---|---|
| the substituted funds | 98.2 percent | 71.1 percent | 0.47 percent |
| seven failing funds outside the nineteen | 92.1 percent | 43.1 percent | 0.29 percent |

The first column is mostly units with no gap at all. The second is the one that tests a charge, the worker put it in the bar
before the run, and it reads 71 and 43 against a bar of 90. So: a real effect, far above chance, and incomplete. A 12-dollar
figure seen on the units that fit none is marked post hoc and kept out of every count. That is the criterion met: the bar was
written first and the reading follows the bar, against the worker's own idea.

The worker's first run used the wrong close and its own in-sample check caught it (2 of 936). It changed the close to the one the
test's text defines and no constant, window or threshold. Disclosed as a row.

What the charge is, is not established: nothing on disk names it.

**A consequence for round 76.** The 15 failing funds were classed with an allowance built from these seven figures. The figures
have now failed as a complete set. The allowance only ever took units OUT of the failing count, so it cannot have made a fund
fail; it may have let one pass. The record carries this as unreconciled and does not re-class; that is the right state until a
ruling.

## CB78bz2-AC2: MET

The price store has one price column. For the 15 funds it is not the unadjusted close. So the corrected basis has no field in the
store to come from; it exists only in a vendor cache that is a folder on one box.

This seat's own script of the round before, over the same local data, gives two of the record's counts: 29,834 held dates for the
15 funds and 20,718 with a cached unadjusted close, and the build's close at a per-fund median of 0.5647 to 0.9179 of it. This
seat printed the landing's lines: one price column, filled from a field named `as_traded_close`. It did not print the writer's.

**Two rows from this cell matter more than its answer:**

- **The live store object is not what the writer in the tree produces** (row D2-W149-S1): it lacks a column the writer writes and
  carries a source value the writer never assigns. So reading the writer's code does not tell anyone how these prices got there.
- **The store's ticker is not one security** (row D2-W149-S2): 308 of 4,000 tickers carry more than one asset name, about half the
  rows have no ticker, and the build reads the store by ticker. That is a second defect in the same store, independent of the
  adjustment, and it reaches past the 15 funds.

## For the addendum

The round's two answers bound what the fund-basis addendum can say. The right close for these funds is known and held, for every
held trading day. It is held in a place no build reads, from one pull, on one box. A basis rule that names it
names a source that does not yet exist as a source.
