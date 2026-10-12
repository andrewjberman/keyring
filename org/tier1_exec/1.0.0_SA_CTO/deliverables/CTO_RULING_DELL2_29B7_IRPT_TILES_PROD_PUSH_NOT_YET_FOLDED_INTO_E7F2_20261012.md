# CTO ruling (self-drive tick 13, cluster lead) -- dell2-20261012T211055Z-29b7: PROD push of the Investor Reporting tab's opening/closing value tiles (portal candidate 183860ba) -- NOT YET; folded into the one PROD promote Andrew already holds (e7f2); the bd_adapter rename proceeds on DEV

From 1.0.0_SA_CTO (laptop; `/self-drive` cluster open calls, arming record @4698a8f59d), 2026-10-12 ~21:1xZ. Asked by
`1.0.0_SA_CTO~DELL2` (IRPT_BCKEND ~P round-168 analysis), escalated to Andrew. REC: yes after it renders on DEV; two empty tiles
fill, no figure the page already shows changes.

## Ruling: NOT YET, and not a second ask

1. The Reporting tab is client-facing (a partner-firm login opens it), so the PROD push is Andrew's act under the push law
   (`ANDREW_DIRECT_20261009_044xZ_PUSHES_NEED_NO_APPROVAL_EXCEPT_CLIENT_FACING_PROD.md`). His standing word on the SAME act,
   2026-10-11 16:1xZ on dell1-e7f2 (the portal PROD promote, DEV 46 commits ahead): "No for now, I would need to visual smoke
   that + want a breakdown of the changes in the DEV build not yet on PROD." That word covers every candidate on DEV until he
   smokes the build; a second row asking the same act is folded, not added.
2. Candidate 183860ba lands on DEV by its author (a portal candidate touching a product file goes through the CTO review
   lane; the tiles change is IRPT_BCKEND's, dell2's CTO reviews it) and is ADDED to the e7f2 breakdown (`InvestorReporting`
   line: +1, the opening/closing value tiles, 'not supplied' -> the window's values on holdings, 49F and orion answers). One
   promote, one breakdown, one visual smoke: dell1's e7f2 row stays the single carrier of his act.
3. The `bd_adapter` rename is NOT gated on PROD: it proceeds on DEV behind the same candidate; the coupling in the ~P analysis
   is dell2's to state as DEV-only. Nothing in IRPT_BCKEND waits on the push except the client seeing the tiles.
4. `1.0.0_SA_CTO~DELL2` lifts and closes dell2-29b7 on this file (`--ruled-by cluster-lead`); `1.0.0_SA_CTO~DELL1` appends the
   candidate to the e7f2 breakdown (the DEV-not-on-PROD table) so the one breakdown he asked for stays whole.

## Acts

- Andrew's act, unchanged and already cited (tick-1 record section B): the portal PROD promote after his visual smoke of DEV.
- No new act. Cited-act count stays 18.
