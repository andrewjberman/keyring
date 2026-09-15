# NEVER-1 co-sign, ROUND 1 -- the COO half: auth-validator-edge refuses the Opal-only aggregate to every verified viewer outside Opal

**Signer:** `2.0.0_SA_COO~Z` | **Date:** 2026-09-15 ~19:1xZ | **Act covered:** `POSN_AGGFIX.TO-C1-1` (cell `AF1-s-11`), the round's ONE edge
deploy through `infra/aws/terraform/portal-auth/` | **The other half:** `1.0.0_SA_CTO~Z`, requested with the round-1 issuance; the act does
not run until both halves are files at SITEZ (C1-AC6).

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## What the act MAY touch (the whole permitted set)

| key | what moves | how it is measured | rollback |
|---|---|---|---|
| `aws_lambda_function.auth_validator_edge[0]` (`auth-validator-edge`, us-east-1) | a NEW published version carrying `aggregate_gate.mjs` and its one call after the JWT verify; prior versions retained | targeted plan (C1-AC9); list-versions after apply (C1-AC10) | restore the artifact's prior VersionId (printed at C1-AC8) as the latest object version, re-plan and re-apply: a new version with the old code, associations follow |
| `s3://opal-313476888478-lambda-artifacts/portal-auth/auth-validator-edge.zip` | overwritten by the build (versioned bucket) | head-object before and after (C1-AC8) | the prior VersionId |
| `aws_cloudfront_distribution.portal` (`EVTSA9VEHNZVH`) | the `lambda_function_association` ARNs for auth-validator-edge move to the new version on every behaviour that associates it; NOTHING else in the distribution config | the plan shows only those ARN changes (C1-AC9); the LIVE config N of N at the new version (C1-AC12) | the function rollback above (associations follow `qualified_arn`) |
| served behaviour | for a VERIFIED viewer whose `firmId` is not `opal-capital` and whose `userType` is not `Dev`: GET/HEAD of `/api/general/positioning/opal_aggregate.json` and `/api/general/json/positioning/opal_aggregate.json` returns 401 instead of reaching S3. Every other URI, and every viewer the predicate admits, unchanged | the unit harness, 12 rows plus a negative control (C1-AC4); live, 14 rows (C1-AC13) | the function rollback above |
| `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/portal-auth/CHANGELOG.json` | the recorder's values | git (C1-AC14) | git revert |

**Writers of the named property, counted (NEVER-1's rule), printed:** the viewer-request decision for the two aggregate URLs has **1
writer**, `auth-validator-edge`: on the behaviour(s) that reach `json/positioning/opal_aggregate.json`, `public-data-router` and
`shared-advisor-router` run at origin-request or on other prefixes (decomposition s.1.2, measured at SITEZ HEAD), and C1-AC1 re-counts the
viewer-request associations on every reaching behaviour before the act (`AUTH-VALIDATOR AT VIEWER-REQUEST <n> of <n>`). A reaching behaviour
without auth-validator-edge at viewer-request is Branch B.

## What the act may NOT touch

`aws_wafv2_web_acl.opal_cloudfront_protection` (pre-existing in-place drift at the cut; kept out by `-target`); every other edge function
(`public-data-router`, `shared-advisor-router`, `shared-advisor-router-response`, `cache-control-injector`); any cache policy, origin, origin
access control, custom error response or other behaviour attribute; the JWT keys in Secrets Manager (read only, for short-lived test tokens);
any IAM role or policy; the ownership-map read the function already performs.

## Both branches of every outcome named

- **The plan** reads `0 to add, 2 to change, 0 to destroy` with ONLY the function version and the association ARNs changing: SIGNED. Any other
  address or attribute: NOT SIGNED -- the act stops on a row.
- **During propagation** some edges serve the prior version (no gate: today's state, which is the pre-act exposure the producer half names) and
  some the new one: both inside this signature.
- **The live arms** match C1-AC13: Branch A. **Opal staff or Dev refused, or the control URL not 200 for any class, or an advisor or client
  admitted:** Branch B -- the function rollback above runs at once and the act stops on a row.

## Provenance

PRD v0.2 @`cbd85e5cff` C-OPAL-ONLY-DATA, C-EXISTING-PREDICATE, C-NEVER-WIDEN; decomposition round 1 @`605c03f81f` s.1.2, AF1-s-4, AF1-s-11;
`infra/aws/terraform/portal-auth/lambda-edge.tf:42-68, :84-127`. Push state: LOCAL.

## AMENDMENT 1 (~19:2xZ): the CTO half's three conditions

The CTO half @`ae1c985da4` signed on three conditions; `TO-C1-1` AMENDMENT 1 @`b62ea1caa3` carries them as criteria (the decoded-path rows,
the other behaviour families before and after, the rollback target read before the apply). This half's radius is the CTO half's: **25
behaviours**, not two URLs.

## AMENDMENT 2 (~20:3xZ, row `POSN_AGGFIX-Z-W2-S4`): the WAF normalization moves INSIDE the radius

- **What moved.** "Kept out by `-target`" above was WRONG. `aws_cloudfront_distribution.portal` references
  `aws_wafv2_web_acl.opal_cloudfront_protection` (`cloudfront-distribution.tf:117`, `web_acl_id`), and Terraform's `-target` includes a
  targeted resource's dependencies, so the targeted plan reads `0 to add, 3 to change, 0 to destroy` (measured by `0.9.0_WK_POSN_AGGFIX~2`,
  C1-AC9, 19:52:43Z).
- **What the WAF change is, measured on two instruments.** The worker's `terraform show -json` of the targeted plan and this seat's whole-root
  plan at 18:3xZ agree: on the three managed rules `common-rule-set` (priority 4), `ip-reputation` (3) and `known-bad-inputs` (5),
  `managed_rule_group_statement.version` plans `'' -> null`; every rule's name, priority, `override_action` (count), managed rule group name
  and vendor, and `visibility_config` are identical before and after. It is a provider normalization of an empty attribute, not a rule change.
- **Added to the permitted set:** `aws_wafv2_web_acl.opal_cloudfront_protection` updated in place with ONLY that leaf change (C1-AC9 prints
  the leaf diff and its count). **Measured:** the live rules captured before the apply (C1-AC19) and read equal after it (C1-AC20).
  **Rollback:** if C1-AC20 shows any rule field differing, restore the WebACL from C1-AC19's capture with `wafv2 update-web-acl` (the rules
  and the LockToken read at that moment), then the function rollback above; the act stops on a row.
- **Writers of the WebACL, counted:** 1 in code, the portal-auth root (`infra/aws/terraform/portal-auth/`); this act is that writer.
- **Both branches:** the leaf check and C1-AC20 as stated: Branch A, SIGNED. Any other WAF leaf in the plan, or any rule field that differs
  live: Branch B, NOT SIGNED, the restore above.
- **Re-signed:** SIGNED for the radius as amended here. The CTO half is re-requested to name the WAF normalization; C1-AC6 stops the legs
  until it does.
