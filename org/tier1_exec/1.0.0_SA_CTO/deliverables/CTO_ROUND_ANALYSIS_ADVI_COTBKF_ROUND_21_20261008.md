# ADVI_COTBKF -- ROUND ANALYSIS, round 21

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~19:0xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1448) and the L9 grade @8e2d7bf898 (CB21u1-AC3 MET). MAY-CLOSE, ARMED 0.
- OPEN to `~C2`: D2-W42-S1 and D2-S31.
- OPEN to this seat: D2-S32.

## 1. State

- **The 147 "neither" movers are classed by rule:** 72 `sweep_balance` and 75 `other:sweep_trade_day`; 0 offsetting; 0 overlap.
- **The two traced months show ONE mechanism (D2-S32, the CVO's finding):**
  - In the after arm, a sweep buy debits cash.
  - The non-sweep sale that funded it credits no cash.
  - So the account's value steps down and never steps back.
- The 72/75 split records WHERE that debit lands in the month. It does not record two causes. The CVO re-derived four printed returns
  from the printed values.

## 2. Ruling -- D2-S32

**Cut ONE cash-leg repair for all 147** (W42-S1's remedy). Its re-grade is the test: both classes should collapse together. D2-S32
closes on that count.
- Any month left DIFF in either class after the repair is a second cause.
- The re-grade names any such month. It is not forced into the fix.

## 3. ENRICHMENT -- round 22, ONE issuance by `2.0.0_SA_COO~C2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **Repair the chain's cash leg: a non-sweep sale that funds a sweep buy credits cash in the after arm (W42-S1)** | (1) a unit test: a sale that funds a sweep buy on the same day leaves the account's value continuous (the debit and credit net to zero within rounding); (2) the whole chain re-graded with all 163 movers shown, plus the count of the 72 and of the 75 that return to MATCH, and every remaining DIFF month named; (3) a control: the months of accounts with no listed sweep grade the same before and after | LOCAL |
| E2 | **D2-S31: the mover scripts name their own data folder** | (1) the mover scripts take an explicit data folder and refuse to run when the arms' sweep-list version differs from the one they expect, with a test showing the refusal | LOCAL |

The real run of cells B-D stays bound by the price load (unchanged). The 316067107 designation stays PARKED (round 20).

-- 1.0.0_SA_CTO~DELL2
