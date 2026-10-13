# TCKT_VNEXT round 16 -- L8 drain-end packet for `3.0.0_SA_CVO`: two cottonwood test tickets closed by one crawl sitting (no judgment criterion)

**From:** `2.0.0_SA_COO~V2`, 2026-10-13 ~09:3x ET. **Order:** `org/tier2_senior/0.7.0_AE_CloudOps~TV2/task_orders/TCKT_VNEXT.TO-RUN-R16-cw2.close-two-cottonwood-test-tickets-by-crawl-dell2.md`
(issued @4187535279, AMENDMENT 1 @06bd872615; the applier's result and proof @724958d31f; the issuer flipped `complete`). **Cell:** `R16-cw-2` of
`decompositions/TCKT_VNEXT_DECOMP_R16.md`. **Risk:** WORLD. **Authority:** Andrew card 7 "Yes do it" (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_122xZ_ANSWERS_TO_NINE_DELL2_CARDS.md`), under the never-widen pair
`deliverables/2.0.0_SA_COO~V2/R2_RUN/R2_CW1_CRAWL_PAIR.md` (blob `b172afe6c4`): COO halves AMENDMENT 1 and 2, CTO halves AMENDMENT 1
@4fea908a37 and AMENDMENT 2 @02234ccce1, all SIGNED.

## What was done and read

- **Sitting 1 STOPPED before any ticket write** (the applier's script pressed the board tab before sign-in finished; msg 6920). This
  seat re-read both targets and the card-1 ticket open at 12:56Z. The second sitting was authorised by the CTO's AMENDMENT 2.
- **Sitting 2 (msg 6942):** one identity (`tckt-r2-crawler-20261013@opal.invalid`, LIST `["cottonwood"]`), one token `iat` 13:08:28Z to `exp`
  13:20:28Z, four writes made by the board page (claim and complete for each ticket, HTTP 200 each). Mail branch after each claim:
  `WE_CLIENT_SEND_FAILED` on both (no mail reached any person). Row deleted 13:20:33Z, after `exp`, read ABSENT. Ledger closed.
- **Re-read by this seat, live, ConsistentRead:** `TCK-20261009-a1052909` and `TCK-20261012-13cd3a1d` both `completed`, assignee the
  identity's address, three events each; `TCK-20261012-c546fead` (card 1) `open`, no assignee, one event; the identity row key reads
  ABSENT, beside a positive control (the walker row's key reads PRESENT).
- **The order's one mechanical criterion, re-run by this seat after a fix to the check:** `CW2-OK two tickets completed by the identity;
  row absent after exp; card-1 ticket still open`. The check had a defect of this seat's: `aws dynamodb get-item` prints NOTHING for an
  absent item, and the check parsed that as JSON, so it printed FAIL in the good state. The applier found it, ran a scratch copy, and
  did not edit the file. The fix (empty output is an absent item) is committed with this packet; a ticket read that comes back empty
  still FAILS the check, so the fix can only pass the identity row.
- `python .tools/round-close-check.py --project TCKT_VNEXT --round 16`: orders=1, judgment=0, verdict=MAY-CLOSE.

## Not measured, or weaker than it reads

- **The zero-call read is zero by absence of traffic:** the applier found no data-refresh event from any caller after
  2026-10-12T19:00:06Z (447 streams searched). Its first pass searched 0 streams and is recorded as VOID. So the read shows no call in the
  window; it does not show the identity was refused one. The refusal arm was not run (the CTO's ruling dropped the probe).
- The applier's result file lists `blocked_requests`: GET requests the board page made to advisor-intelligence platinum files, blocked by
  the crawler's own guard. They show the page asks for those files on load; they were not sent. No row is raised by this seat; the CVO
  may read the list in the result file.
- The distribution-list notice and the table's item count were not read. The CodeSha256 of the ticket Lambda read by the applier
  (`4sDK8P5m...`) is the same build the round-9 apply left; this seat did not diff it against the tree again.

## Rows and grades

No surprise row was raised in round 16 and none was touched. No judgment criterion, so no L9 grade is owed.

## Next

The CTO closes open calls `fbb1` and `5cb1` on this read (its msg 6913). Round 17 has no cell until a staff request names
`TCK-20261012-c546fead` (card 1) and TR-dp-24 posts.
