# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- the ETF Classifier tag wins; `structured` and `commodities` become classes

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_ETF_TAGS_WIN_20260926.md`
blob `8ee2b88a14ddfc9e10524f02b24be9637f6f6a45` @`09cd2a3e50`. The blob is the same at HEAD and on disk (read 2026-09-26
~22:3xZ).
**First half:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_ETF_TAGS_WIN_20260926.md`, as amended @`c516dab84b`
(msgs 101541, 101548).
**Asked by:** 2.0.0_SA_COO~M msg 101538. This seat is not in the act. It carries UIR-50 of the UI review register.

## VERDICT: SIGNED -- Part A as the CTO amended it (16 keys), Part B as the sequence B1 -> census 0/0 -> B2 -> B3, with two named items

- **Part A, 16 keys:**
  - the 15 puts (13 equity, 2 fixed_income) for tickers absent from bd-securities;
  - **VNQ equity -> alternatives**, where the Classifier tag and Andrew's 09-25 REIT rule agree.

  CASH is DROPPED. The ticker collides: in bd-securities, CASH is Pathward Financial Inc (CUSIP 59100U108, real equity);
  in the Classifier, it is a synthetic cash row. Part A rides R4.
- **Part B:**
  - no `structured` or `commodities` value is written until every reader in the request's table admits it;
  - the seed scripts are guarded or retired;
  - a re-run census reads **0 RAISES and 0 silent drops**, with its denominator.

  The census shows why the order is load-bearing: writing today crashes three served producers
  (`holdings_snapshot.py:748/800`, `d06_firm_mix_summary.py:96-98`, `d08_cot_mix_summary.py:51-54`) and silently drops
  the values in eleven more. PHYS is Commodities on Andrew's word.
- **The COT cash-line error** (620 "CASH -- CASH" nodes, $2,866,668.86, served as equity through Pathward's key) goes
  under 2.0.0_SA_COO~M's own half, as the CTO routed it.

## Named item 1 -- the ticker is not an identity: a collision census before B2

CASH shows the Classifier join is keyed by TICKER, and one ticker can name two different securities. Before B2 writes
its 13 keys, 2.0.0_SA_COO~M prints, for each one, the bd-securities security's issuer and CUSIP beside the Classifier
row's intended security: GLD, IAU, SLV, USO, PDBC, VXX, UVXY, QBER, JEPI, PHYS and the rest. Any mismatch is dropped from
B2 the way CASH was dropped from Part A. Part A's 15 puts cannot collide, since their tickers are absent from
bd-securities. VNQ is the Vanguard Real Estate ETF on both sides.

## Named item 2 -- the new classes' colours must not be model colours (O7)

The request notes that the IR portal already has colours for both classes (`tabs/holdings/assetClass.ts:22-23`). The
CTO's ruling requires each new class's colour to be distinct from every model colour (UIR register O7; UIR-37 found blue
and orange each meaning a model in one chart and an asset class in another). The v0.14 portal cell (2.0.0_SA_COO~D, C34)
checks both existing colours against the canonical model palette (`portal/src/lib/modelPortfolioColors.ts`) before B3
shows them.

Not measured by this seat: the reader census rows (`ETF_TAGS_READER_CENSUS_20260926.md`) and the served deltas. They
are the request's.
