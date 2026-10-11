# ADVI_COTBKF round 72 -- L9 grade of CB72bt1-AC2, CB72bt2-AC2 and CB72bt3-AC3

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T19:08:24Z. Row ADVI_COTBKF-D2-S123.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_72_DRAIN_END_20261011.md @73ef7b3c0d (msg 5617)`.

| criterion | verdict |
|---|---|
| CB72bt1-AC2, the reinvestment-price check | **MET** |
| CB72bt2-AC2, where an unadjusted value sits | **MET, on a comparison the order did not state beforehand** |
| CB72bt3-AC3, the re-mint mode repaired | **MET; one printed count overstates** |

## CB72bt1-AC2: MET

This seat applied the rule as the record writes it, with its own script, to the custodian's rows and the build's price table.

| | worker | this seat |
|---|---|---|
| fund reinvestment dates | 4,568 | 4,568 |
| with a same-date close | 796 | 796 |
| confirmed adjusted / confirmed not / nothing to test on | 19 / 15 / 236 | 19 / 15 / 236 |
| series read differently | | 0 of 270 |

- No vendor series enters: the reading uses the custodian's rows and the build's own close.
- Too few dates reads nothing-to-test-on: two of this seat's own nine fall there under the 5-date minimum, and the worker kept the rule.
- The reach is on the confirmed set only: no row outside it carries one.
- The rule's timestamp (18:37:42Z, after the nine, before the table) is the worker's statement; this seat cannot verify a clock.

**What the number means.** 19 is what this instrument can see, not the size of the defect. It reads 34 of 270 series. 236 unreadable
is not a clearance.

## CB72bt2-AC2: MET, qualified

| the cached unadjusted close against the reinvestment price, nine funds, 93 dates, within 0.5 percent | worker | this seat |
|---|---|---|
| same day | 45 | 44 |
| the trading day before | 88 | 88 |
| the trading day after | | 32 |
| the adjusted close, same day | 1 | 1 |

The day-before match is real and is specific to that day: the day after matches on 32. Nothing was fetched, the yardstick is the
custodian's rows, and no rule was changed. The difference of one on the same-day count was not chased.

The qualification is the worker's own and it stands. The order asked for a same-day match and there is none; the day-before reading
was found after looking. It is a finding to confirm, not yet a rule to build on. Why the custodian's row trails by a day is inferred.

## CB72bt3-AC3: MET

Read by this seat in the merged code and by running the tests:

- A key's state is read from the bucket after the stop, against the capture; the list built before the writes is gone.
- All 11 refusals in the function sit above the line that announces the writes; the three write calls sit below it.
- 0 delete calls in the file. The mode ran against the tests' faked bucket only. The re-mint tests: 99 passed on this seat's run.
- What a hard kill leaves is stated plainly in the code's comment, its help text and the record.

**One overstatement.** The printed line reads `described=18 not_described=0`. The record's own list holds one point still not
described: a hard kill. The line should not count it.

**One limit the worker states.** The "before" state is the capture's, not a fresh read. A second writer between the capture check and
the writes would be reported as written by this run.

## Not done by this seat

The 25 split-shaped tickers, the 76 and 121 coverage counts, and the reach of 712 were not re-derived. The planted mutants were not re-run.
