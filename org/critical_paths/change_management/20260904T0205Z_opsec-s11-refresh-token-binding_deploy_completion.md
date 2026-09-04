# Deploy Completion Record
**Date opened:** 2026-09-04T02:05:37.682419+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260904T022055Z
**Deploy:** TO-OP-S-9-11 OP-s-11: refresh-token sub re-bound from the email to an opaque per-row binding; old-shape tokens accepted for one 7d window so nobody is signed out
**Authored by:** 0.7.0_AE_CloudOps~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | source commit of jwt.ts/auth.ts/types.ts on SITEZ | commit hash bb09d1db76 | commit bb09d1db76 (jwt.ts refreshBinding + generateRefreshToken(user); auth.ts dual-shape refresh(); types.ts RefreshTokenPayload). tsc --noEmit exit 0, zero type errors. | CLOSED 20260904T022052Z |
| L2 | s3-prefix | bun ESM bundle rebuilt and uploaded to portal-auth/opalinvest-auth-handler.zip | new content-sha256 differing from Rc1hWCMRTnb6feMoH2V4IhNuLxyY_bdL | build-nodejs-lambda.sh portal-auth opalinvest-auth-handler: bun 1.3.14, --format=esm, 90 modules, 124.37 KB, handler export validated. New zip SHA256 X8YBkwUqnuTDLW7XvqovWT9+TujBXbTaXQaEdwHxwZc= replacing 5XvFxdr07h4AxhWMVPrkgFVD9g5NCRf2HbtJ1Q0jUYw=. VERIFIED BY PULLING THE UPLOADED OBJECT BACK DOWN AND READING IT, not by trusting rc=0: the bundle carries the binding function (PK\|\|USER#email, createdAt\|\|created_at, sha256, digest hex slice 0,32) and the claim set {sub:binding, email, type:refresh}, and still ZERO exact references to the legacy opal-users table. Source-map commit aa30bd1360. | CLOSED 20260904T022053Z |
| L3 | activation | terraform apply updates opalinvest-auth-handler; live CodeSha256 equals the new S3 content-sha256 | get-function-configuration read | Targeted apply of aws_lambda_function.auth_handler: plan showed ONLY source_code_hash and s3_object_version changing (0 add, 1 change, 0 destroy); 'Modifications complete after 6s'. LIVE get-function-configuration CodeSha256 = X8YBkwUqnuTDLW7XvqovWT9+TujBXbTaXQaEdwHxwZc=, byte-equal to the built artifact, LastModified 2026-09-04T02:14:11Z. Targeted rather than unscoped so the documented perpetual WAF churn (Z-S68/Z-S75) could not ride this ledger. | CLOSED 20260904T022053Z |
| L4 | verify | COMPATIBILITY: the OLD-SHAPE refresh token minted 00:53Z (pre-change) still returns 200 -- nobody signed out; and a NEW-SHAPE token exercises the binding branch | both HTTP responses pasted | THREE ARMS, one of them a negative control. (a) COMPATIBILITY / nobody-signed-out: the OLD-SHAPE refresh token minted 00:53Z, which physically predates the deploy, returned HTTP 200 with a 775-char accessToken AFTER the apply. (b) BINDING BRANCH: a NEW-SHAPE token carrying the correct sha256 binding returned HTTP 200. (c) NEGATIVE CONTROL, without which (b) proves nothing: a NEW-SHAPE token with a deliberately WRONG binding (32 zeroes) was REFUSED HTTP 404 'User not found' -- so the binding is genuinely evaluated, and the refusal wears the same generic message as a missing account, adding no enumeration signal. | CLOSED 20260904T022053Z |
| L5 | verify | S11-AC2 probe: fixture deleted and re-created on the SAME email, old refresh token REFUSED, against the captured positive control that it worked at 00:53Z and 01:20Z | request and response pasted | S11-AC2 / FWD-11 SERVED, fixture demo@demo.test under OP-x-1 bound (1). Deleted PK=USER#demo@demo.test and re-created on the SAME email as createUser would (new random PK USER#usr_fc66989493f7, new createdAt 2026-09-04T02:18:31Z). BOTH stale tokens REFUSED HTTP 404: the OLD-shape token (createdAt-vs-iat guard) and the NEW-shape token carrying the pre-delete binding (binding mismatch). CONTROL, so the refusals are the binding and not a broken endpoint: a token bound to the RE-CREATED row returned HTTP 200. POSITIVE CONTROL from before the delete: that same old-shape token returned 200 at 00:53Z and again at 01:20Z. Fixture then RESTORED and verified BYTE-IDENTICAL to the captured original (19 attributes), and the original token works again -- the estate is exactly as found. | CLOSED 20260904T022054Z |

## Log

- 20260904T020537Z OPENED by 0.7.0_AE_CloudOps~X with 5 leg(s)
- 20260904T022052Z LEG L1 closed: commit bb09d1db76 (jwt.ts refreshBinding + generateRefreshToken(user); auth.ts dual-shape refresh(); types.ts RefreshTok
- 20260904T022053Z LEG L2 closed: build-nodejs-lambda.sh portal-auth opalinvest-auth-handler: bun 1.3.14, --format=esm, 90 modules, 124.37 KB, handler exp
- 20260904T022053Z LEG L3 closed: Targeted apply of aws_lambda_function.auth_handler: plan showed ONLY source_code_hash and s3_object_version changing (0 
- 20260904T022053Z LEG L4 closed: THREE ARMS, one of them a negative control. (a) COMPATIBILITY / nobody-signed-out: the OLD-SHAPE refresh token minted 00
- 20260904T022054Z LEG L5 closed: S11-AC2 / FWD-11 SERVED, fixture demo@demo.test under OP-x-1 bound (1). Deleted PK=USER#demo@demo.test and re-created on
- 20260904T022055Z CLOSED -- all 5 legs proven
