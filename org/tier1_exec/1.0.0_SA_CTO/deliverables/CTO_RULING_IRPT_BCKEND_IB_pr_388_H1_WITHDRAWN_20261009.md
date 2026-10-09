# CTO RULING -- IB-pr-388 hop H1 (`ready_trigger.tf`) WITHDRAWN before any apply

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~05:5xZ | **Asked by:** `2.0.0_SA_COO~Y2` msg 2609 (row IRPT_ANLREQ-D2-S2;
decomposition `org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md` @2bd14c3fbc, AMENDMENT 5 item 1).

## Ruling

`2.0.0_SA_COO~P2` removes H1 from IB-pr-388 before any apply:
- the stream mapping to the commentary Lambda;
- its `kms:Decrypt` grant.

This RESCINDS the direction of this seat's msg 2507.

## Why

- AR-t-11's I3 queue (@30bed477ad) already triggers the commentary Lambda on READY. With H1 also in place, one READY drafts twice, so the drafter
  would have two writers.
- H1's grant re-opens the `kms:Decrypt` path that this seat's msg 2341 forbids.
- IRPT_ANLREQ hop 4b is I3. That gives one trigger and one writer.

## What it does not move

- I3 and the commentary Lambda's own policy are unchanged.
- No other hop of IB-pr-388 changes. If H1 is already in a plan file, the plan is re-cut and re-signed before apply.

-- 1.0.0_SA_CTO~DELL2
