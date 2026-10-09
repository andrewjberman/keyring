# ADVI_BILLING round 1 -- L9 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~07:4xZ, on `2.0.0_SA_COO~B2` msgs 2807 and 2809. Row D2-S1.

| criterion | verdict | evidence |
|---|---|---|
| AB1-3-AC3: an advisor can answer "why is my fee this number?" from the panel alone | MET | This seat viewed the real-data render on dell2; its hash matches the record, and it stays outside git. The "Fee for 2026Q3" panel shows, per account: the schedule (49F - Flat 1, 100 bps), the value charged, 64 of 251 days, the computed fee, the Schwab debit and the difference, each line labelled "Differs from Schwab" with its reason. "How the fee is built" works each account as value x 0.01 x 64/251, then the household sum against the debit. The platform fee line says its schedule is not held in Opal, so it shows the debit only (as AMENDMENT 1 A3 ruled) |

**Notes (no grade change):**
- The difference reasons are candidates, not a measured cause: a valuation basis that differs, or the prior-quarter true-up, whose method is
  marked unknown. That is honest, and FWD-1's ACCEPT admits a difference shown with its reason. A measured reason is a later enrichment.
- The surrounding household page carries the colour-law defects the record names (dark default containers, translucent ink). They are not
  this panel's.
- W1-S6: any in-firm viewer can read any household's fee object. That is parity with the existing relationship route, carried to the CTO.
