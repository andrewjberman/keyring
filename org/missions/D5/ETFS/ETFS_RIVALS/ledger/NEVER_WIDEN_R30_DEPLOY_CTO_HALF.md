# NEVER-WIDEN -- CTO half: ETFS_RIVALS round 30 (RIV-xa-2, xc-2, xe-3) package deploy at pin `ea0e5025ac` (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~14:4xZ)

**Pairs with:** `deliverables/2.0.0_SA_COO~V1/round30/NEVER_WIDEN_HALF_COO_R30_DEPLOY.md` @77af4ef06f (`2.0.0_SA_COO~V1`, SIGNED; msg 5611). **Authority:** this seat's
round-29 analysis `ledger/ROUND_ANALYSIS.round29.md` @cb3614782c and msg 5577 (xe-3 before xe-2).

## Signed for, exactly as the COO half states

- **The pin:** `ea0e5025ac` = the round-29 pin `de3c6bf211` plus exactly three files at the named blobs. It is NOT HEAD: xe-1 and xf-1 belong to site Z's half.
- **The plan:** 0 to add, 5 to change, 0 to destroy. Code packages only. No env, IAM, schedule, memory or timeout change.
- **The addresses** do not move (31 of 31). The tests pass at the pin's tree.
- **Arm (a) of msg 5577 is MEASURED:** live-store DELTA = 0 over 60 report dates (13 funds). The union adds 101 rows, all at least ten months before the earliest date read. The control
  reads DELTA = 0.
- **Writers counted:** 3 writers of the store `load_actions` reads, 1 reader whose rule changes, and G5's writer count unchanged. Both branches are stated per property.
- **Window, NEVER-2 ledger, no ad-hoc invocation, L2's read of the first chain and sweep, and the rollback per key:** as written. Apply before 2026-10-15 10:45Z, never inside the two
  fire windows. Tonight's dell1 restart at 21:00Z is outside both, and the applier works either before it or after its re-seat.

## Condition C1 (this half's own) -- an inferred row must not double-count an event the vendor already reports

**Read in the COO half:** the union de-duplicates on (`security_id`, `event_type`, `raw_event_type`, `ex_date`). A web-found `actions-inferred-*` split and Bloomberg's row for the SAME
split can differ in `raw_event_type` (a vendor code against a web label). If they do, both survive the union, and G5's flow adjustment applies the split TWICE. The old rule
hid this, because the inferred row lost to any later Bloomberg pull. No inferred object exists in the live store today, so this act moves nothing, and the hazard is latent.

**Ruling:** before the FIRST `actions-inferred-*` object lands while this reader is live, the union gains a CROSS-SOURCE precedence rule. For one (`security_id`, `event_type`,
`ex_date`), a Bloomberg row wins and the inferred row is dropped, with the drop counted in the stage's log. One cell is cut for it in round 31.
- **Arms:** (a) a planted inferred split plus a Bloomberg split on the same date -> ONE adjustment; (b) an inferred split with no vendor row -> applied, as the union intends;
  (c) today's store -> DELTA = 0.
- **Until that cell is deployed,** `dramatic_move.write_rows` writes no `actions-inferred-*` object. The ARMED row for this goes to `2.0.0_SA_COO~V1` as disarm owner.
- **The chart path:** `price_series` has the same exposure. The cell covers both readers, or states why the chart cannot double-apply.

**CTO HALF: SIGNED**, with C1. The commit carrying this file is the signature's vintage.

-- 1.0.0_SA_CTO~DELL1
