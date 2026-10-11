# ADVI_COTBKF round 64 -- L9 grade of CB64bl1-AC2 (price coverage) and CB64bl3-AC2 (the 24 flagged days)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T10:13:26Z. Rows ADVI_COTBKF-D2-S109 and ADVI_COTBKF-D2-S110.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_64_DRAIN_END_20261011.md @59f48b48ae (msg 4673)`. This seat re-derived the totals of both records from the local tables and printed the cited code lines.
No account id and no client figure is printed here; counts only.

## CB64bl1-AC2: MET

| limb | verdict | this seat's evidence |
|---|---|---|
| each count carries its denominator | **MET** | The 9 kinds sum to the four totals. Each per-kind answer states the kind's unpriced count as its base. Re-derived here: 826 securities, 459 unpriced, 10,090 rows, 6,122 null, 0 partly priced |
| answers (a) and (b) rest on a schema and a count | **MET** | (a) The custodian's positions table has a quantity and no price or value column; printed. (b) The six stores are the build's own list; printed. 0 of 459 is a count over that list |
| no other firm's data was read | **MET** | The six stores are the firm's own two and four market-data stores. No client firm's store is in the list |
| what is not established is said | **MET** | Nine lines, each with the read that would settle it |

**What the record is and is not.** It answers "do we already hold these prices": no. It does not answer what share of account value
is unpriced, and it reads cached copies of 2026-10-08, not the stores as they stand. Both are in its own list.

## CB64bl3-AC2: MET

| limb | verdict | this seat's evidence |
|---|---|---|
| each class's mechanism follows from the cited lines and counts | **MET** | The five cited lines say what the record says they say. Re-derived here: 1,757, 24 and 3; the outflow ratios fall in three bands (4, 17, 3) that fit the four classes, with 0 outside them |
| FORM, DATA and TRUE are told apart on evidence | **MET** | Class D is FORM on a counterfactual the record ran (the withholding as an outflow gives 0.00 on both days). No class is DATA and the record shows why: 0 unpriced positions on the 24 prior days |
| an unexplained day is called unexplained | **MET** | 0 unexplained; the class counts sum to 24 |

**The issuer's doubt, answered.** TRUE here means the arithmetic is right and neither the form nor the data is at fault. It does not
mean the number is fit to serve. On the 3 days above 100 percent the base is under one dollar. That is a rule the table lacks, not a
fault of the classification.

## One finding beyond the 24

The same residual base appears across the whole table, not only on emptied days. Of 107,311 measured days, **207 carry a return
above 100 percent in absolute value**; the round examined 3 of them. 5,437 measured days have a prior value under one dollar, and
55 of those are above 100 percent. The other 152 have a prior value of one dollar or more and were not examined by anyone. Read on the local
returns table, not on the served day files. Row ADVI_COTBKF-D2-S110.
