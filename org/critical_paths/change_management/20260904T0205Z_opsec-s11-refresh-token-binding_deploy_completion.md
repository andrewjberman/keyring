# Deploy Completion Record
**Date opened:** 2026-09-04T02:05:37.682419+00:00
**Status:** OPEN
**Deploy:** TO-OP-S-9-11 OP-s-11: refresh-token sub re-bound from the email to an opaque per-row binding; old-shape tokens accepted for one 7d window so nobody is signed out
**Authored by:** 0.7.0_AE_CloudOps~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | source commit of jwt.ts/auth.ts/types.ts on SITEZ | commit hash bb09d1db76 |  | OPEN |
| L2 | s3-prefix | bun ESM bundle rebuilt and uploaded to portal-auth/opalinvest-auth-handler.zip | new content-sha256 differing from Rc1hWCMRTnb6feMoH2V4IhNuLxyY_bdL |  | OPEN |
| L3 | activation | terraform apply updates opalinvest-auth-handler; live CodeSha256 equals the new S3 content-sha256 | get-function-configuration read |  | OPEN |
| L4 | verify | COMPATIBILITY: the OLD-SHAPE refresh token minted 00:53Z (pre-change) still returns 200 -- nobody signed out; and a NEW-SHAPE token exercises the binding branch | both HTTP responses pasted |  | OPEN |
| L5 | verify | S11-AC2 probe: fixture deleted and re-created on the SAME email, old refresh token REFUSED, against the captured positive control that it worked at 00:53Z and 01:20Z | request and response pasted |  | OPEN |

## Log

- 20260904T020537Z OPENED by 0.7.0_AE_CloudOps~X with 5 leg(s)
