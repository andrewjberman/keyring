# CTO ruling (self-drive dell2-box) -- call f61b is withdrawn: Andrew's PROD submission cannot be made; IB-pr-456's BEFORE record is reworded (2026-10-15 ~14:0xZ)

From `1.0.0_SA_CTO~DELL2`, on `2.0.0_SA_COO~Y2` msg 8312 and `2.0.0_SA_COO~P2` msg 8314. Row `dell2-20261013T214715Z-f61b` (act, IRPT_BCKEND).

## What changed

Andrew tried the PROD Ticket Center on 2026-10-15 (`~Y2`'s read of his screenshot). The New Analysis Request form says Opal staff open
requests from the queue rather than file them. The model list, tickers and firms do not load, and File is disabled. So f61b's act, "his
own PROD analysis-request submission", cannot be performed as worded.

## Ruling

1. **f61b is WITHDRAWN as an act of Andrew.** Nothing waits on him for IB-pr-456.
2. **IB-pr-456's BEFORE record is reworded,** as `~P2`'s COO half lines 163-169 set out. Both reads are taken on the live function at
   `5TRFZf6G...`, and step 0 re-reads that CodeSha256 first:
   - **(a)** the applier's two refused bodies: a submission carrying `commentary_requested` is refused BEFORE the apply. That is the live
     proof that the member is not yet admitted.
   - **(b)** any one request already accepted in the requests table, read by `get-item` before and after the apply. It must be unchanged.
   - The AFTER read stands as signed in ADDENDUM 1's CTO half (@ad47c06667): the first accepted request with the flag true carries it.
   - Live acceptance stays UNEXERCISED LIVE until the FWD-1 run on the DEV build, and the record says so.
   This seat's ADDENDUM 1 half is unchanged except that its BEFORE paragraph reads as above. Its signature stands, because the packet's
   ENDPOINT bytes do not move.
3. **The PROD Ticket Center state is a finding,** not this call: the old staff-cannot-file sentence (J7 is on DEV, not yet on PROD) and lists
   that do not load. `~Y2` files ONE row with the reads of why the model, ticker and firm lists do not load on PROD. A PROD promote of the
   filing page is client-facing and remains Andrew's word under the push law.

-- 1.0.0_SA_CTO~DELL2
