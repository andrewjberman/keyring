# Drive log -- 2.0.0_SA_COO~MP (sitez) -- 2026-10-13 22:3xZ to 2026-10-14 02:4xZ -- NFRA_MCPORTAL

## Closed decision: C17 round 2 (MP-n-4, the gitstate pointer release) LIVE, drained, and packet at L8

| act | commit / msg |
|---|---|
| Correction to 2.0.0_SA_COO~O: the MCPINDEX r10 release was in flight on 64b3e54658 | msg 22:36Z |
| MP-n-4 A1: step 1's "0 failed" graded at HEAD, with release-tree failures admitted only by the Z-S45 mechanism | @46d8c2160d |
| FWD-1 close-run call queued (R54 opal_asker_query measured LIVE at ad2acc0a93) | open call sitez-20261013T233645Z-3b41 |
| MP-n-4 GO (G-REL4 read; live 7eff14b2e6); act held for OG-bd-2's first claim | @78799578ed |
| ~O yielded the pre-11:00Z slot (r30's window opens 11:00Z) | msgs 33855/33856 |
| COO half SIGNED; branch B measured: last_integrate pointer laptop 1, sitez/dell1/dell2 404 | @7699a36c1e |
| Corrections after msg 33876 (ad2acc0a93 DID serve) and msg 33878 (the AC2 rule; the halves crossed once) | @9323a39fd0, @b40848b9c9, @28683249be |
| MP-n-4 LIVE b0c75d24f1; AC2 cold 9.7 s / 1,336 -> 1.3 s / 136; ledger CLOSED 01:31Z | 52da8c3119, 56447631be |
| Slot handed back to ~O with the new deployed_commit | msg 01:35Z |
| Ledger landed on the trunk (blob-identical); MP-n-4 complete; manifest record by ~MQ | @af71482ff8, @dfc2e769f1 |
| C17 r2 round-close-check MAY-CLOSE; issuer real run on site Z, cold 2.2 s, 4 of 4 boxes read | drain packet @f9f9f3c4b0 to 3.0.0_SA_CVO~Z |

## Also this window

- MX-c-9 (NFRA_MCPINDEX) one-token change to `admin_gateway_breakdown.py`: no collision (msg 33864). It must not land
  between Andrew's FWD-20 read and MP-z-6, unless the link counts stay equal.
- The YCharts pause (msg 33910) and its lift (msg 33923) were relayed to ~MQ. MCPORTAL does not touch YCharts.

## Open

- GW r1 is not closing: MP-z-6 waits on the MC Portal sitting (call 21d9).
- FWD-1 (MP-c-2) waits on call 3b41.
- No MCPORTAL gateway release is queued; NFRA_OPLGTW r30 holds the slot from 11:00Z.
