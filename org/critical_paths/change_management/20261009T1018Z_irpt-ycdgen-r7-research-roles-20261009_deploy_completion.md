# Deploy Completion Record
**Date opened:** 2026-10-09T10:18:25.990129+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN APPLY-r7: per-firm research roles for 49financial and inflection plus the runner 3-ARN AssumeRole list, planned at box/dell2 HEAD 2efb289ea8 which contains the required 23e39f11d7
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | plan the ycharts root at HEAD and SAVE it | exactly +2 aws_iam_role.ycdgen_research, +2 aws_iam_role_policy.ycdgen_research, ~1 aws_iam_role_policy.runner_resident with the AssumeRole list at 3 ARNs and Opal-report prefixes plus their KMS list at 3 firms; ANYTHING else is a STOP |  | OPEN |
| S1 | verify | the 3x3 simulate BEFORE the apply, a CTO condition | for each of the 3 research role policies, s3:GetObject and s3:PutObject on its OWN firm prefix and on each OTHER firm prefix: expect 3 allowed and 6 denied, all printed, and ANY off-diagonal allow is a STOP |  | OPEN |
| A1 | activation | safe-apply the SAVED plan | the apply consumes the plan that was read and graded, not a re-plan |  | OPEN |
| V1 | verify | the read-back | iam get-role on the two new roles plus cottonwood, and the runner policy AssumeRole Resource equal to EXACTLY the 3 ARNs; each firm report prefix is address() output |  | OPEN |

## Log

- 20261009T101825Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 4 leg(s)
