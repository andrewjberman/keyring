# AE 0.7~B Session Log -- 2026-05-20 -- IAM-gap verification (directed work, COO~B)

**Agent:** 0.7.0_AE_CloudOps~B
**Trigger:** COO~B directed work (stimulus-scan dispatch) -- not a TO
**Status:** COMPLETE -- read-only audit; RAVC2 to COO~B + direct copy to CTO~B.

---

## TL;DR

Resolved the tracked `mdpf-daily-trigger-lambda-role` IAM-gap flag: it is a
**comp-iam FALSE POSITIVE**. The `aws s3 cp` at lambda_function.py:76 is inside an
SSM command payload that runs on the EC2 runner, not a Lambda boto3 call. Broader
~B-pipeline IAM sweep: clean -- 0 real gaps.

## 1. mdpf-daily-trigger -- VERDICT: false positive

`comp-iam service mdpf-daily-trigger` flagged s3:GetObject + s3:PutObject MISSING,
both tracing to `aws s3 cp` at `infra/aws/lambda/mdpf-pipeline/mdpf-daily-trigger/lambda_function.py:76`.

Read the source (lines 58-93). Line 76 is one element of the `bootstrap` list:
```python
bootstrap = "\n".join([
    "set -uo pipefail",
    "mkdir -p /opt/mdpf",
    f"aws s3 cp {s3_uri} /opt/mdpf/mdpf-daily-dispatch.sh",   # <- line 76
    "chmod +x /opt/mdpf/mdpf-daily-dispatch.sh",
    ...])
resp = ssm.send_command(
    InstanceIds=[RUNNER_INSTANCE_ID],
    DocumentName="AWS-RunShellScript",
    Parameters={"commands": [bootstrap], ...})
```
The `aws s3 cp` is a SHELL command string dispatched via `ssm.send_command` to the
MDPF runner EC2 instance. It executes ON the runner, under the runner's role
(`mdpf-daily-runner-ec2-role`) -- which already has the opal-data-mdpf + opal-data-inf
grants (mdpf-pipeline-v1.0.1, commit 9944deb75). The trigger Lambda itself makes NO
boto3 S3 call.

The Lambda's actual AWS operations: `ec2.start_instances` (L65),
`ssm.describe_instance_information` (L48), `ssm.send_command` (L87). The
`mdpf-trigger-scoped` policy (`infra/aws/terraform/mdpf-pipeline/iam.tf:227`) grants
`ec2:StartInstances` (runner-instance-scoped ARN), `ec2:DescribeInstances/InstanceStatus`,
and the ssm actions. The role is correctly scoped and correctly has NO S3 grant.

Root cause of the flag: comp-iam's `service` analyzer string-matches `aws s3 cp` in
the Lambda source and attributes s3:GetObject/PutObject to the Lambda role. It cannot
distinguish a local shell-out from a remote command string inside an
`ssm.send_command` `commands` payload. This is a comp-iam modeling limitation -- the
flag will recur on every sweep until comp-iam is taught to skip `aws`-CLI verbs that
appear inside SSM `send_command` payloads.

Secondary observation: comp-iam also did NOT list `ec2:StartInstances` in its
operations table for this Lambda (it missed the `ec2.start_instances` call at L65).
No real gap -- the role grants `ec2:StartInstances` -- but comp-iam both over-modeled
(S3 from a remote string) and under-modeled (missed an ec2 call) this one Lambda.

## 2. ~B-pipeline IAM least-privilege sweep -- CLEAN

`comp-iam gaps` (full cross-reference of all Lambda/EC2 boto3 ops vs Terraform
policies): **2 gaps total, both the mdpf-daily-trigger s3:GetObject/PutObject false
positive above.** No other service flagged -- smartx-pipeline, trade-pipeline,
mdpf-pipeline (beyond the FP), and the HALTGT-touched paths show no MISSING
permission and no comp-iam-detected over-broad grant. The ~B-shipped infrastructure
has a clean IAM bill of health.

## Compiler Tools

| Tool | Use | Result |
|------|-----|--------|
| `comp-iam service mdpf-daily-trigger` | resolve the tracked gap flag | 2 S3 ops flagged MISSING, both at L76 `aws s3 cp` -- traced to source, confirmed false positive |
| `comp-iam gaps` | full ~B-pipeline least-privilege sweep | 2 gaps total, both the L76 false positive; no other real gap |

## Outcome

- mdpf-daily-trigger s3:GetObject/PutObject flag: **FALSE POSITIVE** -- documented;
  no iam.tf change needed (verifier != fixer; and there is nothing to fix).
- Recommendation surfaced to COO~B: route a comp-iam enhancement (skip `aws`-CLI
  verbs inside `ssm.send_command` payloads) to the comp-tooling lane so the flag
  stops recurring -- not a ~B fix.
- ~B-pipeline IAM sweep: clean.
- Read-only audit -- no Terraform, no iam.tf edit, no mutation.
