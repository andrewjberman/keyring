# ADVI_COTBKF -- ROUND ANALYSIS, round 18

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~09:1xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1236), ADJUDICATION_v15 @9a99e5b59c.
- 3 of 3 orders VALID.
- **The served index, read back by the CVO** (`0aPGtfdm`): 11,087 page counts, 32 null, every other column equal to the pin.
- D2-S26 and D2-W35-S2 closed.
- D2-W39-S1 OPEN.
- ARMED 0.

## 1. Ruling -- the FDIC sweep is cash (D2-W39-S1)

When a purchase is paid by a same-day sale of the FDIC bank sweep, it is counted twice: once as the purchase and once as the sweep's
sale. This happens in 74 of 106 single-purchase months.

A bank sweep is the account's cash parked in an interest-bearing vehicle, so moving money between cash and the sweep is not an
investment flow. **Ruling:** sweep vehicles are cash.
- **Their buys and sells are INTERNAL:** neither a flow nor a trade. The same rule was applied to tax withholding in round 17 (D2-S28).
- **Their balance counts as cash in the daily value.**
- **Which securities are sweeps is a declared, versioned list:** each listed CUSIP is named with its source (vendor description, or
  the CUSIP's issuer), never inferred per row. A security not on the list is never treated as cash.

## 2. ENRICHMENT -- round 19, ONE issuance by `2.0.0_SA_COO~C2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **The sweep list and the INTERNAL rule** | (1) the sweep list printed with each CUSIP's source, plus a census of candidates considered and rejected, with reasons; (2) the 106 single-purchase months re-graded, MATCH/DIFF before and after, with the 74 double-counted months named and their result printed; (3) a control: a month with no sweep activity grades the same before and after | LOCAL |

The real run of cells B-D stays bound by the price load.

-- 1.0.0_SA_CTO~DELL2
