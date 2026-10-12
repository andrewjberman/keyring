# ADVI_COTBKF round 74 -- L9 grade of CB74bv1-AC2, CB74bv2-AC2 and CB74bv3-AC2

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T21:47:49Z. Row D2-S127.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_74_DRAIN_END_20261011.md @1732725e87 (msg 5893)`.

| criterion | verdict |
|---|---|
| CB74bv3-AC2, the first return number | **MET**, and this seat can explain part of what the record left unexplained |
| CB74bv2-AC2, the validation rule | **MET** |
| CB74bv1-AC2, the family split | **MET**: the reading is `not established`, and that is the right reading |

## CB74bv3-AC2: MET

This seat ran its own script over the served copy and the worker's two builds.

| | worker and issuer | this seat |
|---|---|---|
| served against baseline, measured on both | 107,316 | 107,316 |
| differing | 0 | 0 |
| baseline against variant, changed | 1,575 (floor 1e-9) | 1,577 (floor 1e-12) |
| under 1 bp / 1 to 10 / over 10 | 1,054 / 425 / 96 | 1,056 / 425 / 96 |
| largest | 882.0 bp | 882.0 bp |
| higher / lower | 828 / 747 | 828 / 749 |

The difference of two is the floor: both sit under 1 bp. The baseline is shown equal to the served table before any variant number
is read; the variant is a copy of one input and no code edit; the number is given in bands for the validated funds only and the
record says it is not the size of the defect. Nothing was served. All 1,577 changes sit in 9 accounts.

### The 882 basis points, and why returns go UP

The record leaves two things unexplained. This seat looked at both.

**The largest change is not a price step.** For that fund the variant price over the baseline price is one constant on every one
of the ten trading days around 2025-10-24. Both prices rise by the same proportion that day.

**It is a purchase.** Of the 96 changes over 10 bp, 22 fall on a day the account has a share-moving row in one of the five
exposed funds:

| what the account did that day | changes over 10 bp | variant higher | variant lower |
|---|---|---|---|
| bought the fund | 12 | 12 | 0 |
| sold the fund | 2 | 0 | 2 |
| a reinvestment | 8 | 1 | 7 |
| none of these | 74 | 31 | 43 |

The two largest changes, 882.0 and 881.7 bp, are both purchase days. The reading that fits: the baseline values newly bought
shares at a close that is too low, so the day of purchase shows a loss that did not happen, and the unadjusted close removes it.
A sale reverses it. That is why returns rise, which a dividend adjustment alone would not do.

**What this does not explain:** the 74 over-10-bp changes with no such row that day, and the 1,481 smaller ones. This seat counted
and did not recompute a return. It is a mechanism that fits 14 of 14 trade days, offered as a lead to confirm.

**Why it matters.** The reach was being read as a dividend effect on distribution dates. If this holds, the larger error is on
trade days, and it would reach the served return of an account on any day it bought or sold a fund whose close is adjusted.
That is not measured.

## CB74bv2-AC2: MET

- The rule's numbers do not follow the yield: raising the minimum from 5 dates to 10 cut the validated set from 42 to 33.
- `refuted` needs positive evidence and found none: 0 refuted under every threshold tried. The record says the refuting arm was
  never exercised on this population; it should not be read as "no fund is refuted".
- No validated fund rests only on dates where the adjusted close also matches (0 of 33).
- This cell fetched nothing. Not re-derived by this seat: the 33.

## CB74bv1-AC2: MET

The lead was this seat's own (row D2-S125). The worker reproduced it, wrote the rule before the further counts, and tested it on
funds that did not suggest it. On those 17 funds the family's convention holds on 15 cells to 10, under the rule's line. The
reading is `not established`, and share class explains the decided funds as well as family does. No pricing rule is proposed.
That is the correct end of a lead that did not hold up, and row D2-S125 closes on it.
