# ADVI_BILLING round 3 -- FWD-3 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~10:1xZ, on `2.0.0_SA_COO~B2` msg 3103. Real render: portal DEV 6d383958, household
z08219260. The PNG is private on dell2; its hash matches the record, and this seat viewed its fee panel. Row D2-S5.

| FWD-3 ACCEPT clause | on real data |
|---|---|
| the value it was charged on | shown per account |
| the schedule and tiers | shown (49F - Flat 1, 100 bps, flat; no tiers exist) |
| any adjustment for money moved in or out during the quarter | **stated: "No money moved in or out this quarter"**, from the served `flows_in_period: []` |
| anything left out | **stated: "Nothing excluded"**, from the served `excluded_value: 0` |
| per account and household, "why is my fee this number?" | shown (round 1's AB1-3-AC3 MET) |

**Verdict: REALIZED.** A null or absent value would read "not computed for this quarter", never "none". That is the repair the CTO asked
for on the first candidate.

**Correction to this seat's round-2 remedy (D2-S4).** It also asked for the prior-quarter true-up read from a SMArtX statement. That
true-up sits inside Schwab's debit, so it explains the debit difference (FWD-1's comparison, carried by E2). It is not part of how Opal
works out the fee, so FWD-3 does not wait on it.
