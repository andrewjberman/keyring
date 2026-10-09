# IRPT_ANLREQ TO-APPLY-V12 -- L9 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~10:4xZ, on `2.0.0_SA_COO~V2` msg 3157 (packet `ledger/L8_PACKET.TICKET.R1.md`
@dbf6323d9b, ADDENDUM 1). Row IRPT_ANLREQ-D2-S7.

| criterion | verdict | evidence |
|---|---|---|
| TO-APPLY-V12 AC2: the after-reads (deployed file, env, unauthenticated POST, ItemCount, replan) | MET | This seat's live read: CodeSha256 = the uploaded package `IMJsVN6U...`, LastModified 08:22:45Z, Successful, 8 env keys. `lambda_function.py` at pin 86454002bf hashes `04f5727b...`, the member the applier downloaded and hashed. The applier's reads: POST 401, ItemCount 13 unchanged, replan 0-diff. Ledger closed 5/5 |

**Notes:** the applier stopped when the pin and HEAD differed in two paths, and was amended to build in a worktree detached at the pin.
That is the right act. HEAD's `trade_request` edit (`~O2`) is therefore not in this deploy; it ships in its own ticket release.
