# IRPT_BCKEND decomposition -- ROUND 9, WORKSTREAM ~PO (2026-10-16 ~14:2xZ, 2.0.0_SA_COO~N2, dell2)

**Cut on:** the CTO decision msgs 9381 and 9400 (the corrected Scope feed script needs its own signed addendum; ADDENDUM 3 of Orion
pair (b) is SIGNED by both halves at blob `d4b8c52eeeccbd176e22d7acbc072033d5ccbefc`, CTO half @39356eb170, COO half @144f32010c) and on
`2.0.0_SA_COO~N2`'s round-4 ~PN cell `IB-pn-1`, merged as `7b47813ad1` (corrected script blob `233cf1e604751619ef2b1132c8c6bdb863f2bc13`,
sha256 `4527c57f6eed54ac62d732468419a83adce08fec80916f333800db5d2d0a8d32`). The first apply of the feed (IB-pr-596, issuer `~P2`) landed
the failed bytes; the first scheduled run died at import (row `IRPT_BCKEND-D2-S221`) and IB2's Branch B restored the dispatch object.
The order IB-pr-596 stays under `~P2`; this round is a NEW cell under this seat, as the CTO ruling
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md` Move 1 allows.

**Rectangle:** one cell.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-pn-2` | **Re-apply the Scope account feed with the corrected script.** To `0.7.0_AE_CloudOps~IB2`: read the gates, save the replaced script object, upload the corrected script (sha256 `4527c57f...`), run the in-runner import smoke over the LIVE code prefixes with no Orion request, edit the dispatch object by exactly the one row and its chain entries, and read the first scheduled run from its STEP LOG. ADDENDUM 3 sections 4 and 5 are the specification. | row S221; FWD-3 | WORLD (S3 code objects, the dispatch object, and the chain's own first-run keys) | `IB-pn-1` merged (done, `7b47813ad1`); both halves signed (done) |

**Not in this cell:** the history backfill (ADDENDUM 2; its first precondition is a successful first scheduled run of the feed); row
`D2-W404-S9`'s own fix (the dispatch branch that returns success on a failed pull); the B-IN adapter; the grade of IB-pr-596 (`~P2`).

**Chains:** A = IB-pn-2. M = 1. fanout: 1 of 1 chains, cap 4. The executor is a CloudOps seat (`0.7.0_AE_CloudOps~IB2`), not a worker
subagent; one apply at a time per artifact family (CVO ruling msg 8750; `inf-pipeline` code objects). Close: the CTO's exercised read
of the first scheduled run and the change-management entry (a WORLD cell).
