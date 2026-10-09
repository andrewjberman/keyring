# CTO RULING -- row MDPF_SECCLASS-D1-S8: placing 49F Holdings' missing CUSIP request on dell2

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~09:0xZ | **Asked by:** dell1 `1.0.0_SA_CTO~DELL1` (frame c2ddde9c), relayed by `0.0.0_AB_MSTR~DELL2` msg 2958.
**Dell1's finding:** `CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUNDS_13_15_20261009.md` section 2. 49F Holdings never asks for the CUSIP row, so SECCLASS e56's acceptance 1 stays NOT MET.

## The split

- **The CUSIP fallback in the producer** is `holdings_snapshot.py`'s `CUSIP:<security_id>` lookup after a symbol miss. It is SC-e-56, placed on dell1 under `~M1` by
  laptop decision 106191 (one file, one writer). **Dell2 does not touch `holdings_snapshot.py`.**
- **The 49F side:** a fallback can only fire on a node that carries a CUSIP `security_id`. Row D1-S8 names "SmartX-path nodes carry no CUSIP namespace".
  - The node's identifier is built by the 49F builder: `holdings_49f.py` `_security_identifier()`, about `:163-169`, which puts CUSIP first where it has
    one.
  - The SmartX-path nodes reach Holdings without that identifier.
  - That builder is IRPT_BCKEND's file on dell2.

## Ruling: PLACED in IRPT_BCKEND, workstream `2.0.0_SA_COO~P2`

1. **One cell (`~P2`'s next round):** the 49F SmartX-path nodes carry the account's CUSIP as `security_id {namespace: "CUSIP", value}` wherever the source row holds
   one. Where it holds none, the node is LISTED as `no CUSIP in source`, never given an invented id.
   - **Test:** one SmartX-path node from the round-6 sample carries CUSIP; a node without one is listed.
2. **It is a served move** (it changes Holdings' input), so its release rides IRPT_BCKEND's pair. It is NOT cut until dell1's SC-e-56 fallback is live; the two
   ship in that order, so a CUSIP id never meets a producer that ignores it.
3. **The reply to dell1** is this file plus the cell id once `~P2` cuts it. The fix hash follows at the drain.

-- 1.0.0_SA_CTO~DELL2

## AMENDMENT 1 (~09:3xZ, `~P2` msg 2999, row D2-W267-S1): SmartX holds no CUSIP -- (a), join via 49F's own security master

**Measured by worker `~267`:** live `fact_allocation_positions` (date 2026-10-08, 122,164 rows) carries tickers (160 distinct) and UUID symbol ids. 0 rows match a CUSIP
pattern.

**RULING: (a).** The CUSIP is sourced from 49F's Schwab security master (`dim_asset`, which the builder already reads), keyed by ticker.

**Conditions:**
- **A ticker that maps to exactly ONE CUSIP carries it.** Zero or several means the node is LISTED (`no unique CUSIP for ticker`). Nothing is invented and
  nothing is picked.
- **The identifier carries its claim.** The node's fact names the join, `cusip_basis: joined_via_ticker(dim_asset@<as_of>)`, so a consumer can reject an
  inferred id (value-carries-its-claim law). It is never presented as SmartX-reported.
- **The data stays in the same firm.** Only 49F's own master is read, with no cross-firm reference.
- **Tests:**
  - a unique-ticker node carries CUSIP with its basis;
  - an ambiguous ticker is listed;
  - a counts-only census on live 49F prints carried, listed-ambiguous and listed-absent.

The order of release is unchanged: after dell1's SC-e-56 is live.

-- 1.0.0_SA_CTO~DELL2

## AMENDMENT 2 (~10:1xZ, `~P2` msg 3100, row W265-S1): SC-e-56 is live only in the ORDERED key, which no 49F fire runs

**Measured:**
- Dell1's "SC-e-56 is LIVE" (relay msg 3096) is true of `s3://opal-data-mdpf/.../investor-reporting.tar.gz`, version W2Wragr, which carries @01e843ce2e.
- The 49F holdings fire (`irpt-holdings-refresh-lambda`) runs `s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting-holdings.tar.gz`.
  Its `holdings_snapshot.py` is `55a5ac98`, WITHOUT @01e843ce2e.
- IB-pr-402 and 404 land that per-firm bundle narrow, deliberately without e56.
- **So the CUSIP fallback is NOT where the 49F fire runs.** Releasing IB-pr-403 alone would leave e56's acceptance 1 NOT MET.

**RULING (REC adopted):**
- After IB-pr-404 lands, ONE 49F-only narrow release carries both:
  - dell1's e56 port, @01e843ce2e's `holdings_snapshot.py` delta (dell1 `~M1` is the one writer, decision 106191, and its RELEASE goes through IRPT_BCKEND's
    path);
  - IB-pr-403's `holdings_49f.py`.
  It is built on the post-404 bytes, with the 402 digest-gate discipline.
- **Its pair:**
  - `~P2`'s COO half;
  - dell1 `~M1`'s COO half for the e56 member (cross-box, through MSTR);
  - this seat's CTO half.
  The packet replays a symbol-miss node falling back to CUSIP, and the FWD-14 gate is unchanged.
- **The other two firms' bundles are untouched.**
- **e56 acceptance 1 closes on the first served 49F fire after that release.** The reply to dell1 says the e56 code is live in a key the fire does not read.

-- 1.0.0_SA_CTO~DELL2
