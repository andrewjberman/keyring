# CTO ROUND ANALYSIS -- IRPT_BCKEND round 16 -- 2026-09-22 ~12:2xZ

**Input:** `3.0.0_SA_CVO~B`'s L10 slug `surprise-channel/remediations/REMEDIATION_v7.md` @`4e4808d815`, the round-16 addendum. L9 is `ADJUDICATION_v11` C-S198.

## Coverage read -- round 16 closes; the capture-tool and metadata line is fully closed

- **C-S174 closes as REMEDIATED.** The proof's exclusion now names the browser, host and SSM limbs that were never exercised, and excludes S3 explicitly.
- **R116 passes.** C-S195 (R114-AC3 PASS) is unchanged.
- **Orders:** 0 of 100 open.
- **No further repair of the tool or its metadata is called for.**
- **FWD-2 and FWD-11 are NOT_REALIZED.** Both sit behind the authenticated-render chain, IB-rti-6.

## The authenticated-render chain -- design direction opened with Andrew (~12:1xZ)

**Finding:** the portal refresh token lives **7 days** (`auth-handler/src/jwt.ts:18`, `REFRESH_TOKEN_EXPIRY = '7d'`). A human-captured session therefore expires weekly. It cannot be the standing mechanism for exports, only a one-time unblock.

**Andrew asked why not a service account.** This seat proposed two options:

1. **A dedicated portal user with MFA off**, its secret held in Secrets Manager. This is weaker: it is a full-admin credential, it has no MFA, and it sits on a host.
2. **REC: a short-lived, narrowly scoped render token.**
   - The render job mints the token per run.
   - It has a TTL of minutes and a new `renderer` role.
   - It is signed with the portal's existing JWT key from Secrets Manager.
   - Only the print route and the data APIs that route reads accept it.
   - No password, no MFA bypass, nothing long-lived.

**Andrew's choice is pending:** option 2, option 1, or a one-time capture now while option 2 is built.

**This does not park the drive.** Two things proceed now:
- The design research for option 2 goes to `4.0.0_SA_CRO`. This is the design-fork route under the /self-drive call routing.
- Once Andrew answers, this seat amends the IRPT_BCKEND PRD and `2.0.0_SA_COO~B` cuts round 17 on it.

**Holding pattern:** until then, rti-6 stays parked under its existing un-park rule. If Andrew does the one-time capture, rti-6 re-hands as ruled.

**PUSH STATE:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
