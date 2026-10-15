# Drive log -- 2.0.0_SA_COO~Y2, IRPT_ANLREQ, 2026-10-15 21Z hour (desktop-n8rjv0a)

- 21:0xZ CTO msg 8646 (PRD v0.16 @a4af0e5bba, Andrew: no date selection for prices, T-1) read and acked. Cut AR-y-360 (order `IRPT_ANLREQ.TO-AR-y-360`, commit 0bb931f5b4): the Investor Reporting prospect composer loses its price-date input, says "Prices are the T-1 close.", sends no price_date; Ticket Center and `prospect.ts` untouched. Worker 157 built the local candidate `cand/dell2/anlreq-no-price-date-t1` @c22f4508 (6 new cases pass, mutant fires, scope OK); drained as 7ac19bb2fc.
- AC1 re-graded by the issuer (row IRPT_ANLREQ-D2-S128, 3c26947b3e): 19 folder failures in the sparse worktree are the identical set on origin/PROD e0b43076 (candidate 535 pass, base 529 pass). The worker's instance still records AC1 FAIL; the order stays `pending`.
- Cut AR-y-361 (e7aa6af7f7) for worker row W157-S5: a null as-of renders 'not supplied' on the prospect card; worker 158 sets the as-of to the constant `T-1 close` on the c22f4508 candidate. In flight.
- CTO msg 8659 (addendum 3 @fb11003a1b) acked: ~G2 issues r32, then r33 (irpt-ycharts-generate leg, own pair), then FWD-1 run 3 (this seat); c8c3 after 4 of 4 attachments.
- Not promotable: both portal candidates wait on r32/r33 (the live door requires a price date for Shares) and, being client-facing, on Andrew's word.
