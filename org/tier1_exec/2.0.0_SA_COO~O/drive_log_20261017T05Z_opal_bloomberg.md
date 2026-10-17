# Drive log -- 2.0.0_SA_COO~O -- NFRA_OPLGTW -- 2026-10-17 05Z (host opal_bloomberg)

## Substantive ticks since the 03Z log (ticks 113 to 124)

- `OG-en-20` merged (`d9364e3e9c`; AC1 2 of 2 and AC3 33 of 33 in both orders, this seat's run): `mallopt(M_ARENA_MAX, 2)` once at import, `READ_WORKERS` 8. Six worker environment notes dispositioned (Z-S344 to Z-S349).
- `OG-ap-35` (CTO ruling 35321, Alyssa's no-download, call bd68) DONE: Phase A usage 0 `download_filtered` calls since activation (positive control seen), ask sha256 `224a80d8`, halves CTO `df73e21192` (+CT1: the audit summary says Andrew did not approve in person), COO `4aea561614` (C1-C7), CVO `03311f4476`; Phase B one `activate` (revision 4 to 5), `ag1.AC2` PASS (my run), the `email_deny` hash equal before and after, the host read-back refuses her download and answers list, describe, query; ledger CLOSED; result sent to the CTO for Andrew. No call as her, no contact.
- `OG-ap-32` closed SUPERSEDED (A4, `ad05c0a218`). `OG-ap-34` cut (`53cac446ff`): the fourth release with a memory gate in Phase A. Phase A (04:25Z): release `9d5b712557` on the live ref `d3ae88be46`, `ap34.AC1` PASS (my run), ask sha256 `bdccc464`, memory gate in a fresh process on the host: RSS 369.7, 362.9, 339.4, 329.0 MB after pages 1 to 4, median growth -10.4 MB per page, host peak 45.9 percent, first page 30.4 s. Halves: CTO `9bbfd119eb` (CT1: the chain in the service process; CT2), COO `1c5a9ba7ee` (C1-C8), CVO `b94a795131`. Phase B GO 04:43Z.
- `OG-ap-34` Phase B STOPPED before the deploy (35363): the stand-in cannot reach the running service (RS256 bearer; reaching it means impersonating a roster principal). CTO decision 35368 restated CT1 as (a): pre-deploy full 12-page chain in a fresh process with the service's VmRSS beside it (a fail means no deploy); post-deploy 30-minute read-back every 60 s, rollback on service growth over 300 MB or host over 80 percent; the /mcp window calls served are counted. GO re-sent 04:49Z.
- Andrew-direct (via `2.0.0_SA_COO~MP`, 04:4xZ): the three routes `/sprint`, `/rivalfunds`, `/yearinreview` read "clear + go". Z-S312's disarm condition is met: ruling row Z-S351 (`4271551862`), disarm word to the CVO. Z-S135 ruled (Z-S341). Disarm word for Z-W94-S2 waits on the CTO's answer about the hashed account-id list (MSTR will not mint it).
- Still staged: `OG-ap-33` (land the HVST line on trunk; waits for `OG-ap-34` live).

## Next

`OG-ap-34` Phase B (pre-deploy chain, deploy, read-back, `CODE5_SERVED.json`); `ap34.AC2` my own read; MI and MP told the live commit; the CVO re-grades `OG-ap-31` AC3 on the page chain; `OG-ap-33` GO; Z-S338 disarm once memory holds on the live service; the round-40 slug after every order is terminal and every BLOCKING or ARMED row is dispositioned.

Push state: LOCAL (box/sitez ahead of origin; not pushed this hour).
