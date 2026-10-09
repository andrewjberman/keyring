# IRPT_ANLREQ TO-APPLY-R13b -- L9 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~12:1xZ, on `2.0.0_SA_COO~V2` msg 3249 (packet `ledger/L8_PACKET.TICKET.R2.md`
@286c613247, ADDENDUM 2). Row IRPT_ANLREQ-D2-S13.

| criterion | verdict | evidence |
|---|---|---|
| TO-APPLY-R13b AC2: the five after-reads | MET | This seat's live read: opal-ticket-api CodeSha256 `HK82TEd0...`, LastModified 11:43:28Z, Successful, 8 env keys. The committed `lambda_function.py` hashes `67068626...`, the single member the applier downloaded and hashed. The applier's reads: env names unchanged with COMMENTARY_ALLOWED_FIRMS byte-exact; POST /tickets and POST /tickets/{id}/package both 401, beside a positive control; ItemCount 13 -> 13; full replan rc 0 |

**Note:** this release carries `~O2`'s `trade_request` type with the I5' and I7 changes, applied by the substitute lane `~AR2` under ruling
@5ff94852a6.
