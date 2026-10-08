# Deploy Completion Record
**Date opened:** 2026-10-08T20:20:14.237135+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T202635Z
**Deploy:** IRPT E6 leg 1: add only ReadPartnerProfileRowForOnBehalfAdvisor GetItem on opal-partner-49financial/cottonwood/inflection to irpt-ycharts-generate-role. CTO half 10dae3bf03; COO TO and GO 107162/107212; leg0 passed. Rollback: remove this statement and targeted safe-apply pre-grant policy saved in deliverables/irpt_e6_20261008/leg1-policy-before.json. No code deploy or other policy change.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | aws_iam_role_policy.generate | exact 0/1/0 saved plan applied; timestamp | safe-apply saved exact plan: 0 added, 1 changed, 0 destroyed; CloudTrail PutRolePolicy at 2026-10-08T20:25:33Z event ff9ed6b1-7328-4f20-bae5-d0e8a0696d54; source 51f4545acd. | CLOSED 20261008T202634Z |
| V1 | verify | irpt-ycharts-generate-role | live policy exact delta and targeted no-change replan | Live get-role-policy after minus ReadPartnerProfileRowForOnBehalfAdvisor equals complete saved pre-policy; new statement GetItem only on exact three partner tables. Targeted replan exit 0, No changes. Evidence deliverables/irpt_e6_20261008/leg1-policy-before.json and leg1-policy-after.json. | CLOSED 20261008T202635Z |

## Log

- 20261008T202014Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
- 20261008T202634Z LEG A1 closed: safe-apply saved exact plan: 0 added, 1 changed, 0 destroyed; CloudTrail PutRolePolicy at 2026-10-08T20:25:33Z event ff9
- 20261008T202635Z LEG V1 closed: Live get-role-policy after minus ReadPartnerProfileRowForOnBehalfAdvisor equals complete saved pre-policy; new statement
- 20261008T202635Z CLOSED -- all 2 legs proven
