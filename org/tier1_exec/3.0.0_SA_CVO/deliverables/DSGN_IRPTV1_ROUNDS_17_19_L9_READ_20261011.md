# DSGN_IRPTV1 rounds 17 and 19 -- L9 read (the history reader; the Holdings face)

**From:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T12:29:17Z. Rows DSGN_IRPTV1-D2-S13 and DSGN_IRPTV1-D2-S14.
**Input:** msg 4903 (round 19 IV-e-99 drained @d4fa29cbe1; round 17 IV-e-96 drained @e0253035f6). No judgment criterion is named. The issuer asks a judgment on the reader; the Holdings face is read from one screenshot.

## 1. The history reader (IV-e-99): looser than the contract on purpose

**Sound as a transitional reader, with one gap.** This seat read it on portal DEV.

- It admits the two-key page and the contract's page. Every member that is present is checked as the contract types it. Any other
  key is still refused. The single-request reader is not widened.
- **The gap:** it also admits mixtures neither answer is. A page with `unreadable_rows` and rows without `client_id`, or some rows
  with `client_claim` and some without, passes. The service does not send those today. The reader would not notice if it did.
- It is on DEV, not PROD. The PROD reader is still the exact one, so the re-release of irpt-status still waits on a PROD push, and
  that push changes a client-facing page.
- The tolerance has a named end: the contract-exact reader, after release 5 has been read through the page. That duty needs an owner
  and a row so it is not lost.

## 2. The Holdings face (IV-e-96): it opens on the picked account's split

The screenshot shows the three categories for one account, which is what FWD-1's words name. Read on a synthetic fixture from a
driver, not on the deployed page; no rendered walk has been made.

Three things a reader of that page would trip on, all visible in the one screenshot (row DSGN_IRPTV1-D2-S14):

1. **Two totals with no label between them.** The Identity band says 1,000,000.00 over 2 accounts. The Holdings face says Total
   Assets 500,000.00. Nothing on the page names the picked account; only a "Back to all accounts" link implies one.
2. **The securities do not add up to the total.** The map and the table list 70% and 10%: 400,000.00 of 500,000.00. The SMA 20
   percent has no row and no sentence saying why.
3. The 130% weight the worker saw (row D2-W53-S7) is the same family: weights are taken against a base the page does not state.

The values are fixture values. Whether real data shows the same is for the walk.
