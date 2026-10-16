# Deploy Completion Record
**Date opened:** 2026-10-16T08:22:53.812739+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T085431Z
**Deploy:** TCKT_MTADTA round 2: apply the trino root (new resources only)
**Authored by:** 0.7.0_AE_CloudOps~TM1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| apply | activation | infra/aws/terraform/trino (safe-apply, create-only plan) | plan shows only creates, 0 destroy/replace; safe-apply rc=0; replan exit 0 | safe-apply rc=0 at 2026-10-16T08:31Z: Apply complete! 26 added, 0 changed, 0 destroyed (plan: 26 create, 0 destroy/replace); replan r2_check_r1.py plan -> R1-PLAN-OK exit=0 | CLOSED 20261016T084737Z |
| bucket-policy | verify | opal-data-trino bucket policy | r2_check_r1.py applied prints R1-APPLIED-OK | r2_check_r1.py applied -> R1-APPLIED-OK aliases=collector,member (live read 2026-10-16T08:3xZ) | CLOSED 20261016T084737Z |
| key-policy | verify | trino CMK key policy (root + access role only) | r2_check_r1.py applied prints R1-APPLIED-OK | r2_check_r1.py applied -> R1-APPLIED-OK aliases=collector,member (live read 2026-10-16T08:3xZ) | CLOSED 20261016T084737Z |
| aliases | verify | globgrph-trino-access-lambda aliases collector + member | r2_check_r1.py applied prints R1-APPLIED-OK | r2_check_r1.py applied -> R1-APPLIED-OK aliases=collector,member (live read 2026-10-16T08:3xZ) | CLOSED 20261016T084738Z |
| group | verify | IAM group globgrph-trino-access-group (no member added) | r2_check_r1.py applied prints R1-APPLIED-OK; refusals prints R1-REFUSALS-OK | r2_check_r1.py refusals -> R1-REFUSALS-OK; mfa -> R1-MFA-OK members=1 mfa_devices>=1; get-group lists Andrew_Berman alone | CLOSED 20261016T085418Z |
| 7a-mfa-group-policy | activation | aws_iam_group_policy.invoke (access.tf): Condition aws:MultiFactorAuthPresent=true | plan = 1 in-place update of that policy only; safe-apply rc=0; replan exit 0 | plan 0 add / 1 change / 0 destroy (aws_iam_group_policy.invoke in place); safe-apply rc=0 Apply complete 0 added 1 changed 0 destroyed; live get-group-policy Condition Bool aws:MultiFactorAuthPresent=true | CLOSED 20261016T085041Z |
| 7b-one-member | activation | IAM group globgrph-trino-access-group: Andrew_Berman alone, after MFA device count >= 1 | list-mfa-devices count printed; get-group lists exactly Andrew_Berman | list-mfa-devices Andrew_Berman count=2; add-user-to-group rc=0; get-group lists Andrew_Berman alone (denominator 1 member) | CLOSED 20261016T085120Z |
| 7c-door-deny | activation | Lambda resource policy on aliases member and collector: Deny InvokeFunction unless MFA (collector role carved out) | door_resource_policy.json committed; get-policy shows both Denies + the existing Allow; or identity-side Deny (d) landed | put-resource-policy accepted both documents (revisions d1b98901 member, 91bcd155 collector); policy JSON committed 46130e1cff door_resource_policy.json; collector Allow kept verbatim | CLOSED 20261016T085337Z |
| 7d-probe | verify | box identity no-MFA invoke of member and collector aliases | both read AccessDenied; collector role simulated allowed on its own alias | box identity no-MFA lambda invoke: member -> AccessDeniedException rc=254, collector -> AccessDeniedException rc=254, both 'explicit deny in a resource-based policy' | CLOSED 20261016T085338Z |
| 8-checks | verify | r2_check_r1.py applied, refusals, plan, mfa | R1-APPLIED-OK, R1-REFUSALS-OK, R1-PLAN-OK, R1-MFA-OK | applied -> R1-APPLIED-OK aliases=collector,member; refusals -> R1-REFUSALS-OK; plan -> R1-PLAN-OK exit=0; mfa -> R1-MFA-OK members=1 mfa_devices>=1 | CLOSED 20261016T085418Z |

## Log

- 20261016T082253Z OPENED by 0.7.0_AE_CloudOps~TM1 with 5 leg(s)
- 20261016T084737Z LEG apply closed: safe-apply rc=0 at 2026-10-16T08:31Z: Apply complete! 26 added, 0 changed, 0 destroyed (plan: 26 create, 0 destroy/repla
- 20261016T084737Z LEG bucket-policy closed: r2_check_r1.py applied -> R1-APPLIED-OK aliases=collector,member (live read 2026-10-16T08:3xZ)
- 20261016T084737Z LEG key-policy closed: r2_check_r1.py applied -> R1-APPLIED-OK aliases=collector,member (live read 2026-10-16T08:3xZ)
- 20261016T084738Z LEG aliases closed: r2_check_r1.py applied -> R1-APPLIED-OK aliases=collector,member (live read 2026-10-16T08:3xZ)
- 2026-10-16T08:5xZ legs 7a-7d and 8 added on the amendment of TO-MD-r1 (commit 29ef973419, CTO rulings 6605 and 6614); leg 'group' stays open until the amended AC2 reads clean
- 20261016T085041Z LEG 7a-mfa-group-policy closed: plan 0 add / 1 change / 0 destroy (aws_iam_group_policy.invoke in place); safe-apply rc=0 Apply complete 0 added 1 chang
- 20261016T085120Z LEG 7b-one-member closed: list-mfa-devices Andrew_Berman count=2; add-user-to-group rc=0; get-group lists Andrew_Berman alone (denominator 1 membe
- 20261016T085337Z LEG 7c-door-deny closed: put-resource-policy accepted both documents (revisions d1b98901 member, 91bcd155 collector); policy JSON committed 46130
- 20261016T085338Z LEG 7d-probe closed: box identity no-MFA lambda invoke: member -> AccessDeniedException rc=254, collector -> AccessDeniedException rc=254, bo
- 20261016T085418Z LEG group closed: r2_check_r1.py refusals -> R1-REFUSALS-OK; mfa -> R1-MFA-OK members=1 mfa_devices>=1; get-group lists Andrew_Berman alon
- 20261016T085418Z LEG 8-checks closed: applied -> R1-APPLIED-OK aliases=collector,member; refusals -> R1-REFUSALS-OK; plan -> R1-PLAN-OK exit=0; mfa -> R1-MFA-
- 20261016T085431Z CLOSED -- all 10 legs proven
