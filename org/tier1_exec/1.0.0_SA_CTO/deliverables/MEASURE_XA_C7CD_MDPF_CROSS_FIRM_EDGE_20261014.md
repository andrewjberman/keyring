# Measurement for XA-20261014T204823Z-c7cd (row MDPF_CANON-D1-S27): MDPF per-firm leaves at the edge, 2026-10-14 ~21:0xZ

**By:** `1.0.0_SA_CTO~DELL1`, through a read-only measurement subagent. Nothing was changed and nothing was deployed. Raw files are in this seat's
session scratchpad (`edge_measure/`).

## Verdict: UNMEASURED-(c) live; the DEPLOYED code admits any valid login

| read | result |
|---|---|
| Distribution | `EVTSA9VEHNZVH` (opalinvest.dev). `/api/general/*` is behavior 19 of 29; no more specific pattern catches `/mdpf/`. |
| viewer-request (deployed) | `auth-validator-edge:23`. Its only path gate on `/api/general` is the two `opal_aggregate.json` paths. Its tier and scoping gates match `/api/scoped/...` only. The bundle contains no `mdpf` string. |
| origin-request (deployed) | `public-data-router:7`: `startsWith("/api/general/mdpf/")` is rewritten to `/platinum/mdpf/`, with no firm check. This equals the repo source. |
| (a) GET `/api/general/mdpf/49financial/aggregate-aua-timeseries.json`, no token | **401**. A malformed bearer: **401**. Auth runs. |
| (b) internal token | **NOT RUN**: the walker is disabled (arming it writes DynamoDB/SSM), and the internal admin needs MFA. |
| (c) partner or demo token for a firm other than 49financial | **NOT RUN**: no checked-in login exists for inflection, cottonwood or demo without a second factor. The portal auth owner or Andrew holds one. |
| CloudFront logging | standard logging `Enabled:false`; no real-time log config on any behavior. **Past foreign fetches cannot be looked up.** |

So: from the deployed bytes, any valid JWT reaches every firm's `platinum/mdpf/<firm>/` leaf. The live 200 for a foreign firm is not observed only
because no foreign-firm login was available.

## REC (`1.0.0_SA_CTO~DELL1`)

Read the deployed artifact as the proof (CLAUDE.md 22a: ground a security-critical branch on the deployed artifact). Treat the gap as LIVE and gate
now, per the ruling's 200 branch. Do not wait for a login.
- **The gate:** `auth-validator-edge` admits `/api/general/mdpf/<firm>/` only when `<firm>` is the claim's firm. The internal firm passes every firm.
  The `demo` tenant and a claim with no firm get `global/` only. The proof is a 403 on a foreign leaf and a 200 on the claim's own leaf. The firm
  slug to leaf-folder map is read from the page's own `effectiveFirmId` use.
- **Applier:** a CloudOps lane through Terraform and `safe-apply`, with a deploy ledger entry. Lambda@Edge publishes a new version, and the
  distribution re-points to it.
- **For Andrew:** past fetches are unknowable, because logging is off. Turning on CloudFront standard logging is a separate ask, and his.

## Found during the measurement (separate, for Andrew)

`portal/.frontend-dev/auth/login-constitution.json` is TRACKED in the portal repo (since `03d719d4`). It carries a plaintext password for a
staff login. The measurement printed it into this seat's local session transcript; it was not used. The value is not repeated here.

-- 1.0.0_SA_CTO~DELL1
