# Deploy Completion Record
**Date opened:** 2026-10-20T13:31:21.793310+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T134117Z
**Deploy:** NFRA_FIDUPL FU-s-9: AutoShutdown=disabled tag, stop step removed, DescribeInstanceStatus grant, repaired sign-in files delivered
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of canonical-fidelity-ec2 (tags, automation document, automation role policy) | apply output: 0 add, 3 change, 0 destroy; then plan No changes | safe-apply rc=0 of saved plan: Apply complete! 0 added, 3 changed (aws_instance.box tags, aws_ssm_document.run, aws_iam_role_policy.automation), 0 destroyed; root commit 109bed2f6b; no automation execution InProgress before the apply (0 of 1 total, the one being the Failed b065d07e) | CLOSED 20261020T134116Z |
| L2 | verify | AutoShutdown=disabled tag live on i-028e830f7226cc685 | r1_checks fu8t R1-FU8T-OK | r1_checks fu8t: R1-FU8T-OK AutoShutdown=disabled on the instance | CLOSED 20261020T134116Z |
| L3 | verify | live automation document version has no stop step | r1_checks fu8d R1-FU8D-OK | r1_checks fu8d: R1-FU8D-OK no stop step in live document version 3 | CLOSED 20261020T134116Z |
| L4 | ec2-baked-asset | signin.py and signin_recon.py re-delivered to /opt/fidelity-uploader | SSM md5 of the RUNNING files equals the repo (fu9m R1-FU9M-OK) | SSM md5sum of the RUNNING files: signin.py 60ba9535f4b1831f96a1a0384886f5e3, signin_recon.py 59adb2f0caa4964220df8bc963155280, both equal the repo at HEAD 70d4dace80 (contains 46c10823e4); r1_checks fu9m: R1-FU9M-OK signin.py,signin_recon.py match the repo on the box; box left RUNNING | CLOSED 20261020T134117Z |
| L5 | verify | automation role allowed ec2:DescribeInstanceStatus and plan reads No changes | fu8p R1-FU8P-OK; fu7a R1-FU7A-OK | r1_checks fu8p: R1-FU8P-OK the automation role is allowed ec2:DescribeInstanceStatus; r1_checks fu7a: R1-FU7A-OK No changes. | CLOSED 20261020T134117Z |

## Log

- 20261020T133121Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 5 leg(s)
- 20261020T134116Z LEG L1 closed: safe-apply rc=0 of saved plan: Apply complete! 0 added, 3 changed (aws_instance.box tags, aws_ssm_document.run, aws_iam_
- 20261020T134116Z LEG L2 closed: r1_checks fu8t: R1-FU8T-OK AutoShutdown=disabled on the instance
- 20261020T134116Z LEG L3 closed: r1_checks fu8d: R1-FU8D-OK no stop step in live document version 3
- 20261020T134117Z LEG L4 closed: SSM md5sum of the RUNNING files: signin.py 60ba9535f4b1831f96a1a0384886f5e3, signin_recon.py 59adb2f0caa4964220df8bc9631
- 20261020T134117Z LEG L5 closed: r1_checks fu8p: R1-FU8P-OK the automation role is allowed ec2:DescribeInstanceStatus; r1_checks fu7a: R1-FU7A-OK No chan
- 20261020T134117Z CLOSED -- all 5 legs proven
