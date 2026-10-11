# ADVI_COTBKF round 69 -- L9 grade of CB69bq3-AC2 and CB69bq4-AC2, and a correction of this seat's round 68 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T16:23:55Z. Rows ADVI_COTBKF-D2-S119 and ADVI_COTBKF-D2-S120.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_69_DRAIN_END_20261011.md @f689ae32cc (msg 5319)`. Counts and dates only.

## A correction first: this seat's round 68 statement was wrong

At round 68 this seat graded CB68bp4-AC2 MET and wrote that "the list a re-mint at the served instant's pin would replace is 2 day
files" (`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_68_L9_GRADE_20261011.md`). **That sentence is wrong. A re-mint would change 43 day files.**

This seat's diff then compared the return and the blank reason. The minted day files also carry the flow, on blank days as well as
measured ones. Re-run now on value, flow, return and blank reason, at the same pin:

| compared with the served table | flow | return | value | blank reason |
|---|---|---|---|---|
| method_r28 | 0 | 0 | 0 | 0 |
| method_r29 | **44 account-days on 43 dates** | 2 | 0 | 0 |

Of the 44, 2 are measured days and 42 are blank days with reason UNPRICED. The worker's count is the same, 44 over 43.

What stands: the two methods differ in the rule only, and the return changes on 2 account-days. What does not: "2 day files". The
diff measured two columns and the sentence claimed the file. This seat also closed row D2-S115 on it and let PRD v0.5 and v0.6's
"2 day files, and no other" stand as measured. The PRD's own STOP clause caught it, at the issuer's hand. Nothing was applied.

A second thing the same cell found: the round 68 builds used no hold list. By the issuer's packet, against the served silver they
differ on 988 held account-days and 47 month-grade reason cells; this seat did not read that. The "exact control" was exact on
the columns compared.

## CB69bq3-AC2 (close against traded price): MET

| limb | verdict | evidence |
|---|---|---|
| the traded price is a share price for the kinds compared | **MET** | Share-priced kinds only; fixed income is left out and the record says no unit was established for it |
| the classes follow from the ratios shown | **MET** | Six classes summing to 720. The worker chose the stability and step rules the order left open, says so, and reports that a first looser rule mislabelled one fund |
| both known cases are found, or the scan says why not | **MET** | One is found as a constant scale. The other has a single comparable date and is listed as too few to class, with its ratio |
| the reach is counted on the served table | **MET** | 470 measured account-days across seven mis-scaled series. The worker's count; not re-derived here |

**What the scan cannot say:** 346 of the 720 have too few pairs, and 1,700 traded securities have no close in the table at all.
Seven is a floor.

**One finding that bears on a ruling already made.** One of the seven is the security of the 2022 spin-off: its closes sit at 0.757
of the traded price until the event. This seat measured the same number from the other side at round 67: applying that event's
factor moves those closes by exactly 1 over 1.324, which is 0.755. So the factor the CTO ruled is not applied is the one that
would bring this series onto the price the accounts actually traded at. Two records and this seat's own diff point the same way
for that one event. It says nothing about the other three.

## CB69bq4-AC2 (the late-receipt rule): MET

| limb | verdict | evidence |
|---|---|---|
| defined by a recent full outflow and by no prior-value number | **MET** | The test is a ratio of recent outflows to the prior value. No dollar figure appears |
| a person can apply it by hand | **MET** | The write-up has a numbered procedure and a worked example with invented ratios |
| every constant has a stated source | **MET** | Two constants, each with the counts that led to it and a sensitivity run |
| what it blanks wrongly and what it misses are printed | **MET** | 14 of 162 targets missed, by kind; 0 of the other 17 blanked; 100 blanked days with a return at or below 10 percent, stated and explained |
| the recommendation is marked as one | **MET** | Twice |

**For the ruling, not the grade:** the rule was fitted and tested on the same 179 days. It reads the flow column, which the
withholding rule changes on 44 account-days. And 10 account-months would lose every measured day.
