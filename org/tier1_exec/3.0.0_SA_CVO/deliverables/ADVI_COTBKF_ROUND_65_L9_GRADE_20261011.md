# ADVI_COTBKF round 65 -- L9 grade of CB65bm1-AC2 (the 207 outlier days) and CB65bm2-AC3 (the two price requests)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T11:12:58Z. Row ADVI_COTBKF-D2-S114.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_65_DRAIN_END_20261011.md @66db401fb2 (msg 4792)`. This seat re-derived the outlier record's totals and its whole threshold table from the local returns table,
read both security lists and both request documents, and printed the cited lines. Counts only; no account id, no client figure.

## CB65bm1-AC2: MET

| limb | verdict | this seat's evidence |
|---|---|---|
| each class's mechanism follows from the cited lines and counts | **MET** | The five class counts sum to 207 and to the three bands (55, 95, 57). Re-derived here: 207, the bands, 147 days in the three weeks to 2026-06-10, and 89 on the two rebate dates the record names |
| the five kinds are told apart on evidence | **MET** | 206 are one kind, a credit on a leftover balance, split by what the credit is (income, a fee rebate, a fee). One is FORM, on a contradiction the record measured (a sale at 6.72 times the close used) |
| an unexplained day is called unexplained | **MET** | 0 unexplained. The record says the worker hand-checked 31 of the 207; the rest are placed by rule |
| the threshold table's rows sum to their totals | **MET** | All six rows re-derived exactly from the returns table |

**What the grade does not settle, and the record says so.** 56 of the days called "leftover balance" sit on a prior value of 100.00
or more. Whether that is too small to serve a return on is the CTO's threshold. Two facts for that ruling, from this seat's read:
206 of the 207 are positive, so any floor removes upward outliers almost only; and above 10 percent there are 179 days on a base of
100.00 or more, of which this round classed the 57 above 100 percent. The other 122 are unexamined.

## CB65bm2-AC3: MET

| limb | verdict | this seat's evidence |
|---|---|---|
| the Bloomberg request is one a seat that read READ_HERE.md would write | **MET** | It quotes eight lines of the guide; each prints as quoted. It says the guide neither forbids nor establishes fixed-income history by CUSIP, asks to find out first, sizes the pull at 8 or more days under the budget, and routes it through the queue |
| the unblank counts are upper bounds with their denominator | **MET** | Each is stated as an upper bound of 1,559,722 blank account-days |
| the legs follow the build's grouping and Andrew's word | **MET** | The build sends five classes to Yahoo and the rest to Bloomberg; the PRD records Andrew's word for exactly that split. The two lists share 0 securities and sum to 4,408 |
| nothing was sent | **MET on the documents** | Both open "WRITTEN, NOT SENT". This seat did not read the Bloomberg queue or any network log; the claim rests on the worker's and the issuer's statements |

**One number the packet left open.** The request's denominator is 1,559,722 (from the holdings table). The returns table's own
UNPRICED count reads 1,559,175. They differ by 547; the cause was not looked for.

## The red suite

Row D2-S113 is the issuer's and is right to be loud: one test fails at the base because it reads 76 CUSIPs as account-id shapes.
0 are account ids. The repair is a round-66 cell.
