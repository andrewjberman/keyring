# Deploy Completion Record
**Date opened:** 2026-09-30T10:20:51.538748+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPMSP r1: grant writer register_tenant op BLAST RADIUS: the writer function mcportal-grant-writer-lambda code package only (no env, layer or role change). BEFORE code CodeSha256=OiLZPOdSVMPhekBLD+87w3UJp0FmGODSFeHxBJiOiaw= (52315 bytes, LastModified 2026-09-29T04:58:59Z, layer v1). ROLLBACK: re-apply the previous package (the main tree at the pre-MS-w-1 lambda_function.py, via the same targeted safe-apply on aws_lambda_function.mcportal_grant_writer).
**Authored by:** 0.9.0_WK_NFRA_MCPMSP~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | writer package build + targeted apply | apply line |  | OPEN |
| L2 | verify | deployed lambda_function.py == HEAD, LIVE_FIRMS empty | AC2+AC3 lines |  | OPEN |

## Log

- 20260930T102051Z OPENED by 0.9.0_WK_NFRA_MCPMSP~3 with 2 leg(s)
