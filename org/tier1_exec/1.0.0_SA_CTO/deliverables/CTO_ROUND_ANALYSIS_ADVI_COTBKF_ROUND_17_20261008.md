# ADVI_COTBKF -- ROUND ANALYSIS, round 17

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~02:0xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1181), ADJUDICATION_v14 @513e56bdbc.
- 3 of 3 orders VALID.
- CB17q1-AC3 MET.
- D2-S27 and D2-S28 closed; D2-S26 remedied, not served.
- D2-W35-S2 OPEN, for this seat's ruling. ARMED 0.

## 1. Ruling -- a negative base reads blank (D2-W35-S2)

A daily return divides the day's change by the prior day's value. When that value is negative (an overdrawn cash line, or a short position
large enough to make the account negative), the ratio is not a return:
- its sign inverts;
- its size is unbounded near zero.

Chaining it into a month would distort the month without any visible signal.

**Ruling:** a day whose prior-day value is zero OR negative reads BLANK, never computed, with reason `NON_POSITIVE_BASE`.
- A month containing such a day reads UNGRADED, with the count of blank days, under the same rule as an unpriced day (C-GAP).
- It is never interpolated.

This is the start rule's behaviour, now made explicit for the end rule. The 26,903 affected days are counted and stay visible.

## 2. ENRICHMENT -- round 18, ONE issuance by `2.0.0_SA_COO~C2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **The non-positive-base rule** applied in the end rule, then re-graded | (1) a stub test: a negative prior-day value gives a blank day with `NON_POSITIVE_BASE`, and the zero case behaves as before; (2) the re-grade prints blank days by reason (NON_POSITIVE_BASE, UNPRICED) and graded months MATCH/DIFF, before and after | LOCAL |
| E2 | **The document index re-applied with page counts** (D2-S26: 11,087 of 11,119 read from the PDFs) | (1) the index builder reads the counts, the 32 unreadable listed with reasons; (2) a re-apply packet with both halves, pins re-read at the apply (the round-13 pattern) | SERVED |
| E3 | **The remaining flow-month DIFF** (a new question after D2-S28: 242 MATCH) | (1) the flow-month DIFFs classed by flow type and size; the largest class named with three example accounts, read against their transactions; no fix in this item | LOCAL |

Cells B-D's real run stays bound by the price load (7.8% priced).

-- 1.0.0_SA_CTO~DELL2
