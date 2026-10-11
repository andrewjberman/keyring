# Deploy Completion Record
**Date opened:** 2026-10-11T07:37:50.061008+00:00
**Status:** SUPERSEDED -- nothing stranded, the act was NOT completed by this lane (6 of 7 legs NOT PERFORMED) -- closed 20261011T080900Z by 0.7.0_AE_CloudOps~FB1
**Deploy:** ADVI_FIRMBKTS TO-FB-f-8 phase B: deploy the advTenant build -- shared-advisor-router (v26 to new) + shared-advisor-router-response (v5 to new), 10 associations on EVTSA9VEHNZVH, through safe-apply, under the never-widen pair
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

> ### SUPERSEDED. READ THE LEG TABLE: "closed" THERE MEANS *DISPOSED OF*, NOT *DONE*.
>
> Leg L1 (the pre-act reads and the two built artifacts) was performed. Legs L2 to L5 and the two tf-lambda legs lead with
> **NOT PERFORMED** and carry their supersession evidence in the proof column; no proof was manufactured.
>
> **WHY:** the signed apply ran at 07:53:53Z under `user/cloudops-dell1-agent-user` and both `lambda:UpdateFunctionCode` calls were
> refused 403 by an explicit deny in `cloudops-dell-agent-deploy-policy` (row `ADVI_FIRMBKTS-D1-S13`). The act is re-addressed to the
> laptop CloudOps lane `~FBL` under crossbox ORDER `XB-20261011T080600Z-ba12` (TO-FB-f-8 amendment 6 @7bc01f770a, CTO ADDENDUM 2
> @30bdd99110). **NEVER-2 is satisfied by measurement, not by this header:** live AWS read 2026-10-11T08:08:32Z -- distribution
> `EVTSA9VEHNZVH` ETag `E1OAC26XEP0FDI` Deployed, router `:26` x5, guard `:5` x5, latest published versions 26 and 5, the WAF ACL's
> 6 rules byte-identical to the pre-act read (`evidence/final_get_web_acl.json` against `evidence/pre_get_web_acl.json`).
>
> **TWO THINGS THIS CLOSE DOES NOT UNDO, for the next lane:** (1) the two S3 objects
> `portal-auth/shared-advisor-router.zip` (VersionId `NWJciPjHZ9WAwJzH2jNtipmj06usuqFg`) and `...-response.zip`
> (`T39sO4P3JJT0ZMfr6MeZLYWNBHQ55Mk5`) hold this lane's builds at HEAD `acf8a16706`+, 0 bytes above 127; (2) the shared Terraform state
> for `portal-auth` records those two VersionIds on the functions while live code is the old build, so a plan lists only the ACL
> until a new VersionId exists (`evidence/state_vs_live_after_attempt.txt`, `evidence/step2a_refresh_only_plan.out`; the state
> object's version id before any reconcile: `fSTYD2_FNp1pEGyyGwiacP3Tz_QtztS9`). Step 2's rebuild at the retry uploads a new one.

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-act reads saved in the entry: live get-distribution-config ETag + 10 associations, router v26 and guard v5 on 5 behaviors each, built artifact SHA-256 and bytes-above-127 count for both | ETag, the 10 ARNs, and 2 SHA/non-ASCII lines printed in the entry | ETag E1OAC26XEP0FDI, status Deployed; router v26 x5 and guard v5 x5 (evidence/pre_get_distribution_config.json); artifacts from build-nodejs-lambda.sh portal-auth: shared-advisor-router.zip CodeSha256 DENFVwwc6PnJGsQpXB0ZgKMwJiGxJBTpbDWM3JXdk/E= bytes_above_127=0 (S3 VersionId NWJciPjHZ9WAwJzH2jNtipmj06usuqFg, gate 51 pass); shared-advisor-router-response.zip vLZcOM0N0p8TMEZzTQcuSzguEV/cTpFu/iDNmFbdhBw= bytes_above_127=0 (VersionId T39sO4P3JJT0ZMfr6MeZLYWNBHQ55Mk5, gate 46 pass) | CLOSED 20261011T074318Z |
| L2 | activation | terraform plan of infra/aws/terraform/portal-auth read as JSON (exactly 2 functions + the distribution's 10 associations, distribution NOT no-op), then safe-apply, distribution Deployed | plan resource summary line + apply result + status Deployed | NOT PERFORMED TO COMPLETION -- the signed apply ran 07:53:53Z and both lambda:UpdateFunctionCode calls were refused 403 (explicit deny, cloudops-dell-agent-deploy-policy, row ADVI_FIRMBKTS-D1-S13); the ACL write ran and left AWS byte-identical; the distribution update never ran; superseded: act 1 is re-addressed to the laptop lane ~FBL under crossbox ORDER XB-20261011T080600Z-ba12 (TO-FB-f-8 amendment 6 @7bc01f770a, CTO ADDENDUM 2 @30bdd99110) | CLOSED 20261011T080900Z |
| L3 | verify | post-apply read: 10 associations name the new versions, CodeSha256 of each new version equals its artifact SHA, post-apply plan reads No changes | AC1 AC2 AC3 outputs + the plan line | NOT PERFORMED -- no association moved and no new version was published; live read 2026-10-11T08:08:32Z: ETag E1OAC26XEP0FDI Deployed, router :26 x5, guard :5 x5, latest versions 26 and 5, ACL 6 of 6 rules identical to the pre-act read; superseded: act 1 is re-addressed to the laptop lane ~FBL under crossbox ORDER XB-20261011T080600Z-ba12 (TO-FB-f-8 amendment 6 @7bc01f770a, CTO ADDENDUM 2 @30bdd99110) | CLOSED 20261011T080900Z |
| L4 | verify | CTO oracle read by 1.0.0_SA_CTO~DELL1: both new versions invoked on the 5 event classes against base, one live no-session request 401, associations diffed | the CTO's read, quoted with its message id | NOT PERFORMED -- no new version existed to hand the CTO oracle, so no read was asked; superseded: act 1 is re-addressed to the laptop lane ~FBL under crossbox ORDER XB-20261011T080600Z-ba12 (TO-FB-f-8 amendment 6 @7bc01f770a, CTO ADDENDUM 2 @30bdd99110) | CLOSED 20261011T080900Z |
| L5 | git | proof instance written and TO-FB-f-8 status flipped complete in one commit | commit hash | NOT PERFORMED by this lane -- no proof instance written and the order's status not flipped; the order is re-addressed (amendment 6); superseded: act 1 is re-addressed to the laptop lane ~FBL under crossbox ORDER XB-20261011T080600Z-ba12 (TO-FB-f-8 amendment 6 @7bc01f770a, CTO ADDENDUM 2 @30bdd99110) | CLOSED 20261011T080900Z |
| shared-advisor-router | tf-lambda | aws_lambda_function.shared_advisor_router[0] | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | NOT PERFORMED -- UpdateFunctionCode refused 403, no new version; live version 26 x5; superseded: act 1 is re-addressed to the laptop lane ~FBL under crossbox ORDER XB-20261011T080600Z-ba12 (TO-FB-f-8 amendment 6 @7bc01f770a, CTO ADDENDUM 2 @30bdd99110) | CLOSED 20261011T080900Z |
| shared-advisor-router-response | tf-lambda | aws_lambda_function.shared_advisor_router_response[0] | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | NOT PERFORMED -- UpdateFunctionCode refused 403, no new version; live version 5 x5; superseded: act 1 is re-addressed to the laptop lane ~FBL under crossbox ORDER XB-20261011T080600Z-ba12 (TO-FB-f-8 amendment 6 @7bc01f770a, CTO ADDENDUM 2 @30bdd99110) | CLOSED 20261011T080900Z |

## Log

- 20261011T073750Z OPENED by 0.7.0_AE_CloudOps~FB1 with 7 leg(s)
- 20261011T074318Z LEG L1 closed: ETag E1OAC26XEP0FDI, status Deployed; router v26 x5 and guard v5 x5 (evidence/pre_get_distribution_config.json); artifac
- 20261011T080900Z LEG L2 closed: NOT PERFORMED TO COMPLETION -- the signed apply ran 07:53:53Z and both lambda:UpdateFunctionCode calls were refused 403 
- 20261011T080900Z LEG L3 closed: NOT PERFORMED -- no association moved and no new version was published; live read 2026-10-11T08:08:32Z: ETag E1OAC26XEP0
- 20261011T080900Z LEG L4 closed: NOT PERFORMED -- no new version existed to hand the CTO oracle, so no read was asked; superseded: act 1 is re-addressed 
- 20261011T080900Z LEG L5 closed: NOT PERFORMED by this lane -- no proof instance written and the order's status not flipped; the order is re-addressed (a
- 20261011T080900Z LEG shared-advisor-router closed: NOT PERFORMED -- UpdateFunctionCode refused 403, no new version; live version 26 x5; superseded: act 1 is re-addressed t
- 20261011T080900Z LEG shared-advisor-router-response closed: NOT PERFORMED -- UpdateFunctionCode refused 403, no new version; live version 5 x5; superseded: act 1 is re-addressed to
- 20261011T080900Z CLOSED AS SUPERSEDED -- L1 proven; L2 to L5 and the two tf-lambda legs carry NOT PERFORMED proofs (the tool's wording 'all legs proven' means each carries a proof string, not that it was done)

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

## APPLY ATTEMPT 2026-10-11 07:53:53Z to 07:54:41Z -- FAILED, nothing live changed (0.7.0_AE_CloudOps~FB1)

- `safe-apply` of the saved plan (4 updates, equal to the signed set): seat gates ADMITTED/CLEAR, comp-tagauthz PASSED. Result:
  `aws_wafv2_web_acl.opal_cloudfront_protection` Modifications complete after 19s; BOTH `aws_lambda_function` updates failed,
  `lambda:UpdateFunctionCode` 403 AccessDeniedException "with an explicit deny in an identity-based policy:
  arn:aws:iam::313476888478:policy/cloudops-dell-agent-deploy-policy" for `user/cloudops-dell1-agent-user`. The distribution update did
  not run. `.../evidence/apply_attempt_safe-apply.out`, `deny_policy_cloudops-dell-agent-deploy-policy.json`.
- Live after the attempt (read): distribution ETag `E1OAC26XEP0FDI` Deployed, router `:26` x5 and guard `:5` x5, no new Lambda version
  (latest 26 and 5), ACL 6 rules byte-identical to the pre-act JSON, LockToken unchanged `848a6d0b-...`, 3 rules Count, default action Allow.
  Nothing to roll back. `.../evidence/post_apply_get_web_acl.json`.
- Terraform STATE diverges from live: `s3_object_version` of both functions now holds the NEW artifact versions while the code live is the
  old build (`.../evidence/state_vs_live_after_attempt.txt`). A plan of portal-auth now lists only the ACL, so the two functions and the
  distribution read CLEAN although nothing deployed. The ACL churn is back in the plan after its own apply (the write is a no-op in AWS).
- Legs L2 to L5 stay OPEN. Row `ADVI_FIRMBKTS-D1-S13` BLOCKING. Entry window ends about 11:37Z.

## STEP 2a (amendment 5 @ec0093b72c) -- state reconcile MEASURED, not performed (0.7.0_AE_CloudOps~FB1, 2026-10-11T08:02:06Z)

- Pre-reconcile state object `s3://opal-313476888478-terraform-state/portal-auth/tfstate`: VersionId
  `fSTYD2_FNp1pEGyyGwiacP3Tz_QtztS9`, LastModified 2026-10-11T07:54:43Z (written by the refused apply), 264926 bytes.
- `terraform plan -refresh-only` of portal-auth (read-only, saved plan not applied): resource_drift lists ONE object,
  `aws_wafv2_web_acl.opal_cloudfront_protection` (attribute `rule`, the `version` empty string re-read); the two functions and the
  distribution list NO drift. `.../evidence/step2a_refresh_only_plan.out`.
- Reading: a refresh updates only attributes the API returns. `s3_object_version` is a configuration-side attribute the Lambda API
  does not return, so a refresh-only apply cannot move it back; it would write the state file with the ACL re-read and nothing else.
  No state write was made. The plan will list the two functions again only when the S3 objects carry a new VersionId (step 2's
  rebuild at the retry uploads one) or when the owner corrects the state.
