# ANDREW-DIRECT 2026-08-19 ~1935Z (CRO~A terminal, live) -- VALUATION BASIS: NET/REAL (cash) -- "the Schwab approach is better here"

## VERBATIM

> "I think its more important to view it on a net/real basis, if the cash is not received it
> shouldnt be counted. Aka, i believe the schwab approach is better here."

**Context:** stated immediately after the accrual-gap explanation (the four-cell closure: qt6 EMV
accrual-inclusive vs Schwab net_mv_plus_cash accrual-exclusive; $88.0K firm-wide stub on the $13.7M
direct-bond sliver of a ~$1.77B book; per-account specimen ...2917 = $22.5K on $815K).

## SCOPE AS STATED (recorded, not adjudicated)

Andrew's stated basis preference on the valuation convention: **accrued-but-unreceived income is NOT
counted; value = net/real (cash) basis; Schwab's `net_mv_plus_cash` is the preferred approach.**
This answers the core question of **B_02** (b00_canonical_valuation.py `ACCRUAL_STATUS =
"PENDING-RULING"`, `accrued_income = 0.0` placeholder), which 1.0.0_SA_CTO parked at their gate
tonight (@fee546e533 item 6) as a P3 drive-to-EXACT convention decision. **The formal flip mechanics
(the ruled-status stamp in b00, the convention registry entry) belong at CTO's gate + the owning
DS lane -- this record carries the word to that gate; it does not execute the flip.**

## CONSEQUENCES SURFACED WITH THE RELAY (CRO read, one screen)

1. b00's zero placeholder becomes the RULED answer, not a pending gap: fair_value =
   net_mv_plus_cash, cash basis.
2. The registered harness basis rule (compare on nmpc; BD-EMV residual = the accrual component) is
   now doubly grounded: the residual is BD's basis inflation relative to OUR convention.
3. Every BD-dashboard-vs-us comparison on income-bearing accounts carries a KNOWN, RULED, EXACT
   reconciling item (= the accrual stub); the T1 tie-out oracle should print it as a named line.
4. **GIPS nuance, surfaced by this seat as the ADVI_PERFORMANCE field-contract owner (surfaced, not
   adjudicated):** GIPS requires ACCRUAL accounting for interest income in PERFORMANCE calculations.
   Book-wide the cash-basis TWR error here is negligible (~$88K on ~$1.77B, <1bp). But a BOND-HEAVY
   single account's OWN return series on cash basis saws at coupon dates (the specimen's stub is
   2.8% of account value). A conventional clean resolution exists -- SERVING/AUA on the ruled
   net/real basis, the PERFORMANCE ENGINE accruing interest income internally where GIPS-grade
   per-account returns are claimed -- but whether to split the bases by layer is a design decision
   for CTO to frame and Andrew to word IF per-account GIPS-grade fixed-income returns become a
   served claim. Today's book makes this a parked nuance, not a blocker.
