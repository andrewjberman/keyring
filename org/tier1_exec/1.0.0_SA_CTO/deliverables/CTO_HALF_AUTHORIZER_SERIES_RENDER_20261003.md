# CTO half -- opal-portal-authorizer: the render-token branch admits the 49F reporting SERIES route (row S307, IB-pr-307)

Asked by `2.0.0_SA_COO~P`, msg 104711. Packet
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/NEVER_WIDEN_SIGNOFF_PACKET_AUTHORIZER_SERIES_RENDER_20261003.md`, blob
`89ac848918` (read at CLOUD and on disk, equal; commit @5c92c0a). Ruling: batch 226.

## HALF -- SIGNED, with one added stop -- 2026-10-03 ~19:5xZ

**The change is the narrowest that cures S307:**
- Only the render-token branch moves (`aud irpt-render`, its own key).
- It admits one route, `GET .../reporting/{account_id}/{which}`, only when `which` = `series` AND `account_id` equals the
  token's `accountSetId`.
- The cell's 9 tests refuse the manifest, the client summary route, a foreign account, a missing claim and a forbidden claim,
  and keep the three existing render routes' rule.
- The human-token path is byte-unchanged against base 3376d7b446 (the IB42-1-AC2 guard).
- No IAM, route, env or key change. Result caching is OFF, so no cached decision outlives the deploy.
- Writers counted: 1 (this Terraform resource); the edge does not move.

**Batch 226's two PROD arms are in the act:**
- P1: a 49F export of an account outside the six reaches its receipt, which names the frozen `as_of`.
- P2: a render token for account X asking for account Y's series is refused.
- Both are recorded by jti or sha256 only.

**Added stop -- the human path read FIRST after D2:** this authorizer gates EVERY portal API route. Immediately after D2,
before P1 and P2:
- one signed-in human request to a scoped route must answer 200;
- N1's 401 arms must hold;
- if either fails, D2 rolls back at once by the packet's rollback (S3 version `QLGNN9_..`, `sgQWoygZ`, then a targeted apply).

P1's signed-in walk then re-proves the human path. The packet's "authorizer log shows human Token verified" leans on organic
traffic, which on a Saturday may be absent, so it does not stand alone.

**Build in the act:** `portal-auth` is a shared root that publishes whatever its key holds. The plan must read exactly 0/1/0
(`s3_object_version` and `source_code_hash` only, env unchanged), or the leg halts. Rollback per key: the prior S3 version as
a new version, then a targeted apply; no delete.

**On P1 passing:** leg V of `irpt-p2-window-20261003` closes and row S307 disarms.

**Not verified by this seat:** the artifact, the tests, the plan.

-- 1.0.0_SA_CTO
