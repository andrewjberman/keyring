# ADVI_COTBKF round 73 -- L9 grade of CB73bu1-AC2 and CB73bu2-AC3

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T20:12:07Z. Rows D2-S124 (the grade) and D2-S125 (a finding of this seat's).
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_73_DRAIN_END_20261011.md @f3bffdeb6f (msg 5731)`.

| criterion | verdict |
|---|---|
| CB73bu1-AC2, the three-date read and the sizing | **MET** |
| CB73bu2-AC3, the re-mint mode's two edges | **MET** |

## CB73bu1-AC2: MET

This seat applied the rule as the record writes it, with its own script.

| | worker | this seat |
|---|---|---|
| funds with a reinvestment row and a cached close | 101 | 101 |
| compared cells | 944 | 944 |
| equal on the same day / the day before / the day after | 794 / 744 / 579 | 794 / 744 / 579 |
| funds by winner: same / before / after / undecided | 17 / 15 / 0 / 69 | 17 / 15 / 0 / 69 |
| the nine | 6 before, 3 undecided | 6 before, 3 undecided |
| funds whose cached close the custodian's price validates | 42 | 42 |

- The convention rests on the funds beyond the nine and reads `undetermined` under the rule; the worker did not bend it to the nine.
- A cached close sizes a fund only where the custodian's price validates it: 42, and the 59 others are all too few cells.
- The reach is stated as a floor with what is unsized beside it. Nothing was fetched.
- The rule's timestamp is the worker's statement. This seat's round 72 result for the nine was known to the worker, who says so.

Not re-derived by this seat: the split of the 42 into 21 adjusted and 21 not; the reach of 1,874 measured account-days.

## A finding of this seat's: the date convention splits by fund family

The record says no split by kind, build group or period separates the funds that follow the day before from those that follow the
same day, and that no sponsor field is on disk. The custodian's own security description carries the family name. Read by its
first two words, over the 32 decided funds:

| | follow the day before | follow the same day |
|---|---|---|
| American Funds | **12** | 1 |
| every other family | 3 | 16 |

So there may be a convention after all, by sponsor: the custodian's reinvestment row for an American Funds fund is dated the trading
day after the price it was reinvested at, and for the others it is dated the same day. Eight of the nine of the earlier rounds are American
Funds (the ninth, the one that matched on the same day, is not), which is why the nine looked like a rule. This is a count on 32 funds, with one exception each way and three other families
on the before side; it is a lead to test on its own stated rule, not a result. Row D2-S125.

## CB73bu2-AC3: MET

Read by this seat in the merged code, and by running the tests (120 passed):

- A second writer in the gap is refused: every write of a planned key carries a condition on the captured version, and a refused
  key is printed as changed by another writer. The issuer counts seven planted cases over each kind of key. On the tests' faked bucket only.
- A key another writer changed is never printed as this run's write: a key reads as written only when this run's own write
  returned and the bucket still holds that version.
- The record, the help text, the code's comment and the printed line now agree on the hard kill: not described (the issuer's line: 18 of 19 points described).
- 0 delete calls in the file. The mode was not run against a real bucket.

The limits are the record's own and are stated: whether the real bucket honours the condition is untested; a rewrite of identical
bytes in the gap passes; a writer after a clean run's last write is not looked for.
