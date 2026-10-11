# ADVI_COTBKF round 68 -- L9 grade of CB68bp4-AC2, CB68bp3-AC2 and CB68bp5-AC2

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T15:08:46Z. Row ADVI_COTBKF-D2-S117.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_68_DRAIN_END_20261011.md @95eab5179c (msg 5186)`. This seat diffed the two at-pin run tables against the served local table itself. Counts and dates only.

## CB68bp4-AC2 (the list at the pin): MET

| limb | verdict | this seat's evidence |
|---|---|---|
| the list is stated against the served table at the served instant's pin | **MET** | Re-derived: at the pin, method_r29 differs from the SERVED table on 2 account-days, on 2014-12-03 and 2020-11-13 |
| the two runs differ in the rule only | **MET** | Re-derived: method_r28 at the pin equals the served table on every row, 0 of 1,691,729 differing. That control is exact, so the only thing left between the two runs is the rule |
| the chain ran from a clean checkout | **MET for tracked code and flags; not to the letter** | One untracked input, a cache of 3,580 price files, was copied in from the pinned directory (row D2-W101-S1). The exact control shows the copy reproduces the served table |
| every changed day is traced to its origin or called unexplained | **MET on the worker's trace** | Both are withholding days with no withdrawal row. This seat did not read the transactions |

**This closes the limb this seat left open at round 66** (row D2-S115): the list a re-mint at the served instant's pin would
replace is 2 day files.

What the list does not hold, and the record says so: 41 withholding days carry a changed flow and are blank under both rules. If
they are priced later, they change too.

## CB68bp3-AC2 (the spin-off claims): NOT MET, on its first limb; the four claims stand

| limb | verdict | evidence |
|---|---|---|
| the print taken as the custodian's is shown to be the custodian's and not a vendor's | **NOT MET** | It is not shown. The store's own label is the portfolio system's snapshot, and the record lists "that the number equals the custodian's own mark" as the code's word, not established |
| each claim follows from the two reconstructions on the dates listed | **MET, vacuously** | There are no dates: the store starts 2026-06-08, after all four events |
| an event with no date to compare on is UNAPPLIED_NO_HELD_DATE, not decided from other evidence | **MET** | All four read so. The second candidate (a price from the custodian's trade rows) is reported apart and decides nothing |

**The verdict changes none of the four claims.** It matters for the next claim made on that store: nobody has shown whose print it is.

**A correction this round makes to round 67, which this seat graded MET.** The "independent" price step that round's record cited
is the vendor's own step divided by the factor (row D2-W103-S2). So it was not a second source. Round 67's first limb still holds,
on the custodian's cost-adjustment rows alone, which is what this seat's grade named. The price evidence should not be cited again.

## CB68bp5-AC2 (the 179 outlier days by cause): MET

| limb | verdict | evidence |
|---|---|---|
| the classes are causes found by reading, each with its cited lines | **MET** | Nine classes, each with file and line; 77 days read row by row and 102 placed by rules drawn from them, and the record says which is which |
| TRUE_RETURN, FORM, DATA and PRICE are told apart on evidence | **MET** | 11 days are true returns, 166 are the form's treatment, 2 are price defects, none is data. The record states that FORM means "not a market return under the present treatment", not that a fix is agreed |
| no day on a base of 100.00 or more is called a leftover without saying what the base is | **MET** | The two exit classes state the base: cash on 113 of 119 days, a money-market fund on 6 |
| the unclassed remainder is printed | **MET** | 0, and the class counts sum to 179 |

Two things the record offers and does not rule, both worth the CTO's read: a prior value of 100.00 does not separate the classes,
while the account's own recent outflow does (152 of 152 exit days against 0 of the other 27); and one security's whole close series
sits about 6.6 times below its traded price, which no one has scanned for in other securities.
