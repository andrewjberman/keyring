# Andrew-direct 2026-09-27 ~00:1xZ at 2.0.0_SA_COO~M: VNQ is alternatives

Verbatim: "VNQ is alternatives, it's a REIT"

## What it settles

- VNQ (Vanguard Real Estate ETF) is `alternatives`. This agrees with:
  - the ETF Classifier tag (`etf-classifications`: alternatives / Real Estate);
  - Andrew's REIT rule of 2026-09-25 (REIT -> alternatives).
- It closes the question the CTO carried to Andrew in msg 101540 ("VNQ is HELD ... I asked him").
- Before this word arrived, the CTO had already amended its ETF sign-off @c516dab84b (msg 101547). The CRO signed Part A
  as the same 16 keys (msg 101552). Nothing new is signed here; the word confirms the signed direction.

## Act

- VNQ's bd-securities update equity -> alternatives rides Part A (16 keys) with the R4 enable publication, under its
  own ledger. The write set is `IRPT_MVP_M/ETF_TAG_WRITE_SET_20260926.json`.
- Served delta at the 09-22 revisions: 49F $2,558 (2 nodes); INF $0 (3 nodes).
- It does not reopen "established equities stay" (Andrew-direct 2026-09-26 ~02:3xZ): a REIT is not an established
  equity under the REIT rule.
