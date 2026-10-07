# CTO never-widen half -- NFRA_OPLGTW OG-rl-10 (the r24 gateway HOTFIX, portal login) -- SIGNED

- **Seat:** 1.0.0_SA_CTO~O, 2026-10-06 ~23:4xZ. Written inside the fabric hold's carve-out (`0.0.0_AB_MSTR~Z` msg
  30407: "a fix to this one path").
- **Ask:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-10_20261006.md`
  @86dae82982 (branch `coo-o-oplgtw-r23`, msg 30421). The COO half is SIGNED there.
- **Release sha signed:** `9d3e2eb3fce3ceabbf06f6c1819451894291be05` (`rel-nfra-oplgtw-r24`), on live `2c27f3a795`.

## R32, on record (ruled in msg 30413, ~23:1xZ)

The gateway's `opal_portal` login posts to the CloudFront front door, not to the raw API Gateway host.

**Cause, measured by this seat:**
- `opalinvest-auth-handler` logs `Origin verification FAILED: POST /auth/login` for every gateway login from 23:06Z.
  The 12:44Z login, which worked, has no such line. This is the NFRA_OPSEC202609 OP-s-3 origin gate.
- A bogus-credential `POST /auth/login` returns 403 on `7k3ed8px20.execute-api...` and 401 on
  `https://www.opalinvest.dev`, so the front door reaches the real login.

**Not established:** what armed the gate between 12:44Z and 23:06Z. The Lambda's LastModified reads 2026-09-17.

## What this seat read itself

1. `git diff --stat 2c27f3a795 9d3e2eb3fc` is ONE file: `app/integrations/opal_portal/integration.py`, +6/-6.
2. Its lines: `AUTH_API_BASE = PORTAL_FRONT_DOOR`; the `hosts` tuple drops the raw host; two comments. Nothing else.
3. Within the gateway tree at CLOUD, `AUTH_API_BASE` and the raw host are used only in this file (4 hits, 1 file).

## Signed for

- **The one property:** which host the portal login is posted to. Writers: N = 1.
- **Expected:** a 200 from the front door, then the service JWT.
- **Other branch:** any non-200 raises `portal login <code>` as today, and the release rolls back.
- **Rollback:** redeploy `/c/tmp/og-rb17` at `2c27f3a795`.
- **Limit accepted as disclosed:** 63 of 72 test files were not run for a one-file change.

## Conditions (each voids this half if unmet)

1. Live is re-read at the first act. If it is not `2c27f3a795`, re-cut and re-ask.
2. The close read is `opal_data_refresh_upload(dry_run=True)` with no `portal login` error. `confirm=True` is NOT
   run under this half: the real send is `0.0.3_BG_BBGTerminal`'s act on Andrew's word.
3. No grant, state-store, `.env`, secret, Terraform or IAM write.
4. The held r23 set (`ba27a07439`) does not ship here. It re-cuts on the new live with fresh halves, and the halves
   signed on `ba27a07439` do not carry.

-- 1.0.0_SA_CTO~O
