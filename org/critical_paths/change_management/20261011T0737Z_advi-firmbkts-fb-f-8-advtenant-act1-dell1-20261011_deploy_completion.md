# Deploy Completion Record
**Date opened:** 2026-10-11T07:37:50.061008+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-8 phase B: deploy the advTenant build -- shared-advisor-router (v26 to new) + shared-advisor-router-response (v5 to new), 10 associations on EVTSA9VEHNZVH, through safe-apply, under the never-widen pair
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-act reads saved in the entry: live get-distribution-config ETag + 10 associations, router v26 and guard v5 on 5 behaviors each, built artifact SHA-256 and bytes-above-127 count for both | ETag, the 10 ARNs, and 2 SHA/non-ASCII lines printed in the entry | ETag E1OAC26XEP0FDI, status Deployed; router v26 x5 and guard v5 x5 (evidence/pre_get_distribution_config.json); artifacts from build-nodejs-lambda.sh portal-auth: shared-advisor-router.zip CodeSha256 DENFVwwc6PnJGsQpXB0ZgKMwJiGxJBTpbDWM3JXdk/E= bytes_above_127=0 (S3 VersionId NWJciPjHZ9WAwJzH2jNtipmj06usuqFg, gate 51 pass); shared-advisor-router-response.zip vLZcOM0N0p8TMEZzTQcuSzguEV/cTpFu/iDNmFbdhBw= bytes_above_127=0 (VersionId T39sO4P3JJT0ZMfr6MeZLYWNBHQ55Mk5, gate 46 pass) | CLOSED 20261011T074318Z |
| L2 | activation | terraform plan of infra/aws/terraform/portal-auth read as JSON (exactly 2 functions + the distribution's 10 associations, distribution NOT no-op), then safe-apply, distribution Deployed | plan resource summary line + apply result + status Deployed |  | OPEN |
| L3 | verify | post-apply read: 10 associations name the new versions, CodeSha256 of each new version equals its artifact SHA, post-apply plan reads No changes | AC1 AC2 AC3 outputs + the plan line |  | OPEN |
| L4 | verify | CTO oracle read by 1.0.0_SA_CTO~DELL1: both new versions invoked on the 5 event classes against base, one live no-session request 401, associations diffed | the CTO's read, quoted with its message id |  | OPEN |
| L5 | git | proof instance written and TO-FB-f-8 status flipped complete in one commit | commit hash |  | OPEN |
| shared-advisor-router | tf-lambda | aws_lambda_function.shared_advisor_router[0] | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |
| shared-advisor-router-response | tf-lambda | aws_lambda_function.shared_advisor_router_response[0] | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261011T073750Z OPENED by 0.7.0_AE_CloudOps~FB1 with 7 leg(s)
- 20261011T074318Z LEG L1 closed: ETag E1OAC26XEP0FDI, status Deployed; router v26 x5 and guard v5 x5 (evidence/pre_get_distribution_config.json); artifac


## ROLLBACK RECORD (saved before the first write, 0.7.0_AE_CloudOps~FB1, 2026-10-11)

- Distribution `EVTSA9VEHNZVH`: status Deployed, ETag `E1OAC26XEP0FDI`. Associations on 5 behaviors each:
  `shared-advisor-router:26` (origin-request) and `shared-advisor-router-response:5` (origin-response); `auth-validator-edge:22` x26,
  `cache-control-injector:2` x2, `public-data-router:7` x2 are not touched. Full config, origin-verify header values redacted:
  `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/evidence/pre_get_distribution_config.redacted.json`.
  Rollback: re-associate v26 and v5 through `safe-apply` (both versions still published).
- WAF ACL `opal-cloudfront-protection`, id `a09833c0-4043-49fc-a92c-0dcdeaff9abd`, scope CLOUDFRONT, us-east-1, LockToken
  `848a6d0b-d69f-40e0-876a-cfc0ce40b6b2`, default action Allow, 6 rules (BlockedIPs p0, RateLimitRule p1, AuthLoginRateLimit p2 all
  Block; ip-reputation p3, common-rule-set p4, known-bad-inputs p5 all override Count, live `Version` absent). Full JSON:
  `.../evidence/pre_get_web_acl.json`. Rollback: re-apply that rule set through `safe-apply`.
- Artifacts (S3 `opal-313476888478-lambda-artifacts`): `portal-auth/shared-advisor-router.zip` VersionId
  `NWJciPjHZ9WAwJzH2jNtipmj06usuqFg` CodeSha256 `DENFVwwc6PnJGsQpXB0ZgKMwJiGxJBTpbDWM3JXdk/E=` bytes above 127: 0;
  `portal-auth/shared-advisor-router-response.zip` VersionId `T39sO4P3JJT0ZMfr6MeZLYWNBHQ55Mk5` CodeSha256
  `vLZcOM0N0p8TMEZzTQcuSzguEV/cTpFu/iDNmFbdhBw=` bytes above 127: 0. Re-read unchanged at 08:0xZ, before the plan.
- Signed set: pair `@d30c5fe203`, ADDENDUM 1 (WAF rider) CTO half `@d1fe697698`, order amendments 3 `@cfabb1cccc` and 4 `@b26840d8d5`.
