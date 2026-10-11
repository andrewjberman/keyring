# ADVI_COTBKF round 70 -- L9 grade of CB70br2-AC2, CB70br3-AC2, CB70br4-AC2 and CB70br5-AC3

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T17:14:12Z. Row ADVI_COTBKF-D2-S121.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_70_DRAIN_END_20261011.md @28d71b3241 (msg 5417)`. This seat recounted the 2022 pairs table, read the re-mint mode's code, and reconciled the two flow counts
itself. Counts, dates and ratios only.

## CB70br2-AC2 (the 2022 spin-off's evidence): MET

| limb | verdict | evidence |
|---|---|---|
| every number is this cell's own derivation | **MET** | The table of 42 dated pairs is the cell's. This seat recounted it and both ratio columns recompute exactly from its price columns |
| the after-event dates are in the table as the negative arm | **MET** | 26 dates on or after the event: without the factor 26 of 26 sit within 2 percent; with it, 0 |
| the traded price is shown to come from the custodian's delivered rows | **MET on the record** | Each row carries the delivered file's name and a hash. The bronze bytes were not opened, by the worker or by this seat |
| the reading follows from the rule as worded | **MET** | Before the event: 0 of 16 without the factor, 15 of 16 with it. That is APPLY under the round 68 rule, and the negative arm shows the factor would be wrong after the event |
| the reach is counted on the served table | **MET** | 28 measured account-days in one account; 3,434 priced holding account-days. The returns that would move were not computed |

One date of 16 does not fit (1.03 with the factor), and no cause is given. It does not change the reading.

## CB70br3-AC2 (the scan widened): MET

| limb | verdict | evidence |
|---|---|---|
| each widening is reported separately and a wider pairing does not manufacture a class | **MET** | Seven widenings, each counted; pairs across a day gap or from a reinvestment row are labelled. The one new class it adds rests on 3 pairs and the record says so |
| the 1,700 are characterised | **MET** | 1,610 have no row under any key in the six caches; 90 only under a ticker more than one security claims. They carry 61.5 percent of the table's not-measurable account-days |
| the headline sentence carries all the numbers | **MET** | 8, with 334, 44 and 1,700 beside it, in one sentence |
| fixed income is classed only if its unit is shown | **MET** | The unit is shown and there are 0 comparable pairs, so it is not classed |

**The finding that matters most is not in the count.** Nine fund series start at about half the traded price and step up at
distribution dates. That is the shape of a dividend-adjusted close used as a price. It was read by eye and not tested (row
D2-W113-S1). If it holds, the served table values those funds low in the past and the count of wrong series is not 8.

## CB70br4-AC2 (the late-receipt rule out of sample): MET

| limb | verdict | evidence |
|---|---|---|
| the split was fixed before any outcome and no account is in both halves | **MET** | By the parity of a hash of the account id |
| each half's constants come from that half's evidence alone | **MET** | And they differ: neither half chose round 69's pair |
| the r29 run uses a build with the served hold list, or says it does not | **MET** | It does |
| the record states inputs to a verdict and recommends nothing | **MET** | It recommends nothing |

**What the record shows, for the ruling:** the rule does not hold its constants out of sample. Fitted on one half and tested on the
other, it blanks 72 of 77 target days one way and 37 of 85 the other. Time was not held out. It is not ready to adopt.

## CB70br5-AC3 (the re-mint path): MET

| limb | verdict | evidence |
|---|---|---|
| every refusal fires before any write, by test | **MET** | 37 tests on a versioned fake bucket (the worker's). Read by this seat in the code: every refusal precedes the write loop |
| an unlisted differing day refuses | **MET** | Read in the code |
| a moved capture refuses | **MET** | Read in the code |
| nothing is deleted | **MET** | The file holds no delete or copy call |
| the mint path is unchanged | **MET on the issuer's read** | Not diffed by this seat |
| the mode was not run against the bucket | **MET on the worker's and issuer's statements** | The issuer's real verify of the served table still reads 3,325 of 3,325 |

**One thing for the pair that will use it.** On a failed read-back the mode stops, prints the keys it wrote, and rolls nothing back.
That leaves a served table half replaced. The pair has to name the rollback per key from the captured versions and who runs it,
because the mode will not.

## The two flow counts, reconciled

Round 69 left 44 over 43 against 47 over 46 unreconciled, and row D2-W114-S1 says this seat's 44 was a tolerance. It was. Compared
exactly, the flow differs on 47 account-days over 46 dates. On 3 of them the difference is below 1e-12 on a value of zero:
floating-point residue, which fits the days the round 66 record describes, where the withholding amounts net to zero
(this seat did not read those rows). So 44 account-days carry a real change of flow, and 47
rows differ in their bytes. A re-mint that compares bytes will see the larger number.
