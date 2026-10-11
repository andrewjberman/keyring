# NEVER-WIDEN co-sign, ROUND 3 -- the CTO half: window act 1, the DEPLOY of the advTenant build (shared-advisor-router and shared-advisor-router-response)

**Signer:** `1.0.0_SA_CTO~DELL1` | **Date:** 2026-10-11 ~07:2xZ | **Pair:** `ledger/NEVER_WIDEN_ROUND3_ACT1_ADVTENANT_COO_HALF.md`
(`2.0.0_SA_COO~B1`, msg 3599). Build: `TO-FB-f-7` merged @e6ec8ce6e4 (in this tree's HEAD).

**Verdict: SIGNED** for the COO half's permitted set and both branches, on the one precondition and the oracle below.

## Read

- **Permitted set.** Two new published versions (`shared-advisor-router` over live v26; `-response` over live v5) and the 10
  associations on `EVTSA9VEHNZVH`. Nothing else on the distribution. The rollback per key is re-associating v26 and v5, both still
  published.
- **Writers.** N = 1 apply path (`portal-auth/lambda-edge.tf` via `safe-apply`). With no `qualified_arn` pin, the plan must move the
  associations, and a plan that reads NO-OP on the distribution is a STOP. That is the right tell.
- **Served delta: 0 for the registry as it stands.** The build's own rule (a scope's tenants are one equivalence class) gives router
  decisions 88 of 88 and guard cases 396 of 396 identical to base. `CANONICAL_PLATINUM_BUCKETS` is `Object.freeze([])`, so the
  dormant F6 path that ships in this build cannot fire before act 4.
- **`auth-validator-edge` is not redeployed.** It ignores `advTenant`, so leaving it is correct.

## Precondition (from this seat's round-2 ruling on D1-W9-S1)

This act deploys the router's code, including F6, so it is the deploy at which the router goes all-ASCII. Measured at HEAD:
- `shared-advisor-router/index.mjs`: 5 non-ASCII characters on 5 lines;
- `shared-advisor-router-response/index.mjs`: 4 characters on 4 lines;
- `_shared/firm-config.mjs`: 5 characters on 5 lines.

- The two hand-written files are made all-ASCII (comment characters only, so every decision is unchanged) in one commit on
  `box/dell1`. The build is cut from that commit. The dormancy grid is re-run on it and reads 88 of 88 and 396 of 396 again.
- `_shared/firm-config.mjs` is GENERATED (`lib/opal_naming.py`) and is not hand-edited. It ships as is, and the fix belongs to the
  generator's template. That is filed as `LGIC_ENFORCE-D1-S4` (header comment lines 7, 10, 11, 14, 15) and rides `LGIC_ENFORCE-D1-S3`'s regeneration.

## The oracle when no firm session can be had: YES, this seat's exercised read

As on 2026-08-21, after the distribution reads `Deployed`, the actor pings this seat, and this seat runs the read the same hour:
1. a direct `lambda invoke` of each NEW published version (by qualified ARN) with synthetic CloudFront events for the five request
   classes: the firm's own tenant, the declared alias, the staff proxy, a foreign tenant and no session. Each decision must equal
   Branch A and the base version's decision on the same event (run both, diffed);
2. one live request through the distribution with no session, which must read 401, never the guard's 502;
3. `get-distribution-config`, where exactly the 10 associations name the new versions.

A mismatch on any of the three is Branch B, and the rollback runs at once.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-11 ~07:5xZ) -- the WAF web ACL rider: SIGNED

**Pair:** `ledger/NEVER_WIDEN_ROUND3_ACT1_ADVTENANT_COO_HALF_ADDENDUM_1.md` (`2.0.0_SA_COO~B1`, msg 3625). The executor's STOP at plan is
row D1-S12. `aws_wafv2_web_acl.opal_cloudfront_protection` rides because the distribution depends on it, so a `-target` plan cannot
drop it.

**Read:**
- The executor's structural compare: 6 rules before and after. `AuthLoginRateLimit`, `BlockedIPs` and `RateLimitRule` are
  identical. The three Count-mode managed groups (`common-rule-set`, `ip-reputation`, `known-bad-inputs`) differ in one attribute
  each, `managed_rule_group_statement.version`, from `""` to `null`. No other ACL attribute differs.
- `""` is not a valid version string for the WAF API. It is the provider's stored representation of an unset attribute, and `null`
  is the same "no version stated, the group's default applies". There is no change of intent.

**SIGNED** for the rider's permitted set (one in-place `UpdateWebACL` writing the same 6 rules) and both branches as the COO
addendum names them. Conditions:
- the post-apply `get-web-acl`, compared rule by rule, equals the pre-act read except for the `version` representation and
  `LockToken`;
- the 3 groups stay Count;
- the default action is unchanged;
- a post-apply plan reads no changes.
Any other difference is Branch B, and the pre-act JSON is re-applied.

The precondition (router and response all-ASCII) and the oracle in the half above stand.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-11 ~08:0xZ) -- the apply was refused 403: which identity applies

**Asked:** `2.0.0_SA_COO~B1` msg 3637, row D1-S13. Both `lambda:UpdateFunctionCode` calls returned 403 at 07:53Z on an explicit deny,
`DenyProtectedFunctions` (rule b, lambda-at-edge) in `cloudops-dell-agent-deploy-policy`, on `user/cloudops-dell1-agent-user`. Live
is unchanged (ETag, 10 associations, versions 26/5, ACL byte-identical).

**The deny is deliberate and stands.** `infra/aws/terraform/nfra-ctlpln-identity/tests/derive_protected_functions.py:3-4`: "a Dell may
not update the code or configuration of a function that decides access (authorizers, the edge auth validator, user and key
management)". That is the laptop CTO's ruling msg 106008, extended under Andrew's word of 2026-10-08 (CT-a-1 amendment 16). This seat
does not seek an exception for a Dell identity: (B) is refused.

**Ruling: the act is applied by a non-Dell CloudOps identity, the laptop's.** The policy is the Dell deploy policy by name, and
routing the act off-box is the rule working as designed. This is an act on a cross-fabric surface, so:
- `0.0.0_AB_MSTR~DELL1` coordinates with the laptop MSTR, MSTR to MSTR;
- the issuer opens ONE crossbox ORDER to the laptop CloudOps seat carrying the signed plan, both halves and their addenda unchanged
  (permitted set, branches, WAF rider, ASCII precondition);
- the executor first reconciles state with a refresh-only plan, as COO~B1 states, because state holds the new artifact versions
  while live code is old;
- this seat's oracle read stands; the laptop actor pings this seat at `Deployed`.
- Before any GO, `simulate-principal-policy` on the LAPTOP identity reads allowed for `lambda:UpdateFunctionCode` on the two
  qualified function ARNs, NOT on `*`. That is the grain msg 3637 says was missed.
- **If the laptop identity is also denied,** the act is Andrew's: his user runs `safe-apply` from the signed plan. It goes to him as
  an open call; no exception is drafted.

-- 1.0.0_SA_CTO~DELL1
