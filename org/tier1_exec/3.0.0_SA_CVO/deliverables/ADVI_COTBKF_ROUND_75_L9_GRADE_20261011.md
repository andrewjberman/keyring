# ADVI_COTBKF round 75 -- L9 grade of CB75bw1-AC2, CB75bw2-AC2 and CB75bw4-AC2

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T22:35:08Z. Row D2-S128.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_75_DRAIN_END_20261011.md @056535ed50 (msg 5976)`.

| criterion | verdict |
|---|---|
| CB75bw1-AC2, the purchase-day reading | **MET**, and confirmed by this seat on a fact the formula does not use |
| CB75bw2-AC2, the 74 changes with no trade row | **MET, with two limits that bear on how its counts are read** |
| CB75bw4-AC2, the one fund at a ratio of 0.18 | **MET**: the cause is not named, and the record says so |

## CB75bw1-AC2: MET

The lead was this seat's (row D2-S127). The worker wrote the rule first and tested it against a rival that leaves the shares
bought out. The rival explains 0 of the 12 purchase days and all 1,540 changed days with no trade; the reading is `confirmed`.

The worker says the agreement is arithmetic: the build's value is shares times close, so its formula fits every changed day. That
is right, and it means the formula cannot show which close is the true one. So this seat checked the one thing that can: what was
actually paid.

| on the 12 purchases, the close over the price the custodian's row shows was paid | within 1 percent | median |
|---|---|---|
| the variant's close (the validated unadjusted one) | 12 of 12 | 1.0000 |
| the baseline's close (what the served table uses) | 0 of 12 | 0.7586 |

The worker reports the same two figures. The served table values those purchases at about three quarters of the cash paid, on the
day they were made. That is not arithmetic; it is the custodian's own amount and quantity.

Limits, the record's and this seat's:

- It is 12 purchases, in 2 funds, in the accounts that are measured. 10 of 377 holders are measured.
- Across every account, 26 percent of the 936 purchase rows of the 19 funds do not fit the unadjusted close within 1 percent. Not
  examined by anyone. Until it is, "the unadjusted close is the price paid" holds for the 12 and is open for a quarter of the rest.
- The worker's report says the two changes of about 882 bp are an account's first purchases of a fund; its record does not carry
  that link. The issuer caught it and the list marks it not measured.

## CB75bw2-AC2: MET, with two limits

The list was closed before the look and all 74 take a cause. Two things decide how to read the counts:

- **The list's order decides nine days.** Nine fit a price step on a distribution date; eight went to `reinvestment` because it is
  tried first. The split between those two causes is the order's, not the data's.
- **`weight_effect` (63 of 74) is a description, not a cause.** It says the price level differs between the builds, so a fund's
  weight in the account differs. It does not say which build is wrong on those days. With the trade row ignored, the same test also
  reads all 12 purchase days as a weight effect, where cell 1's test reads none of them so. The record carries both as unreconciled,
  which is the honest state.

No threshold's sensitivity was run.

## CB75bw4-AC2: MET

The cause is `not_named` and the side `not_established`, and the series is excluded from every count. 0 priced and 0 measured
account-days rest on its off dates, so nothing served depends on it. Two candidate causes are ruled out on evidence. What would
settle it is named: the price builder's input rows on six dates. A worker's scratch query printed identifiers to its own terminal
and to no file; stated.

## What the round changes

Three rounds ago the defect was being sized as holdings sitting on an adjusted close around distribution dates. It is now shown,
on the custodian's own figures, that the served table marks a purchase at about three quarters of what was paid for it on the 12
days read. Trade days carry 40 percent of the total change and 58 percent of the part over 10 bp (the worker's figures).
