# SIGN-OFF (1.0.0_SA_CTO half) -- the ETF Classifier tag wins; `structured` and `commodities` become asset classes

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_ETF_TAGS_WIN_20260926.md`
blob `8ee2b88a14ddfc9e10524f02b24be9637f6f6a45` (2.0.0_SA_COO~M msg 101536).
**Rules:**
- CTO 101511, ruled (a);
- Andrew-direct @`714ba46408`: tags already in the ETF Classifier keep their class;
- Andrew-direct 09-25 @`705be61575`: "Real estate is alternative, but only if investment oriented (e.g. a reit)".

**Signed:** 1.0.0_SA_CTO, 2026-09-26 ~22:2xZ.

## Part A (rides R4): SIGNED for 15 of 17 keys; TWO HELD

**Signed:** the 15 puts (13 equity, 2 fixed_income), for tickers absent from bd-securities. For every reader that
already defaults an absent ticker to equity they are equal-class, and no reader crashes on these values.

**HELD (not written):**
- **VNQ (alternatives -> equity).** It sits where two Andrew rules conflict. The Classifier tags it equity, while his
  09-25 rule says an investment-oriented REIT is an Alternative, and VNQ is a REIT fund. That is his call, put to him
  the same turn. It stays at alternatives until he rules.
- **CASH (fixed_income -> equity, COT $2.87M).** Name the security the "CASH" ticker is (issuer and fund type) and
  the Classifier row's basis. If it is a cash or money-market vehicle, an equity tag is a Classifier error to raise,
  not a class to copy. The CTO rules on the identification.

## Part B: SIGNED as the sequence B1 -> B2 -> B3

- **B1:** every reader in the request's table admits both classes, under its own owner and deploy rules. The
  seed scripts (`seed_canonical_securities.py`, `seed_bd_securities.py`) are guarded or retired, so a re-run cannot
  undo the write.
- **Gate to B2:** the reader census, re-run, reads 0 RAISES and 0 silent drops for `structured` and `commodities`,
  printed with its denominator.
- **B2:** the 13 keys under a ledger, including PHYS as Commodities on Andrew's word.
- **B3:** the next Holdings publication.
- The served deltas as stated: 49F about $21.5M, INF $1.75M, COT about $12.8M.

**Rollback per key:** as stated.

**B1 routing:** 2.0.0_SA_COO~M sends each owner its row. Where an owner seat is not live, it names that to
0.0.0_AB_MSTR for seating. The portal rows go to 2.0.0_SA_COO~D (C34).

## Second half

**4.0.0_SA_CRO.**
