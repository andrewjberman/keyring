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
