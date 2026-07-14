# DEPLOY-COMPLETION LEDGER -- V2-2(b) MonolithSchwabMetaPullsWrite grant

**Slug:** v22b-meta-pulls-grant . **Author:** 0.6.2_AE_PartnerETL . **Opened:** 2026-07-14T18:35Z
**Authorization:** CTO IAM gate SIGNED + apply GO 20260714T183215Z (statement reviewed at source @ c03a8529c).
**Change:** ONE statement-add (plan 0/1/0) on `aws_iam_role_policy.schwab_si2_monolith_write`
(quartz-si2-monolith-write, role quartz-si2-spike-role): `MonolithSchwabMetaPullsWrite` -- s3:PutObject on
`opal-data-assets/schwab/{08242234,08335338}/meta/pulls/*` ONLY (never meta/* -- pen-separation from
meta/conversions/). Module: `infra/aws/terraform/canonical-schwab-ec2`.

## Legs

| leg | what | status |
|---|---|---|
| L1 | safe-apply the 0/1/0 plan + 0-diff re-plan | **CLOSED 18:36Z** -- re-plan 0/1/0 immediately pre-apply; safe-apply (HALT_ACK routine) completed; post-apply plan = "No changes. Your infrastructure matches the configuration." |
| L2 | verify battery (22a full strength) | **CLOSED 18:37Z** -- evidence below, 6/6 as designed |

## L2 evidence (verbatim, 2026-07-14 ~18:37Z)

**APPLIED truth (live get-role-policy, quartz-si2-spike-role / quartz-si2-monolith-write):**
statement `MonolithSchwabMetaPullsWrite` live with EXACTLY
`s3:PutObject` on `opal-data-assets/schwab/{08242234,08335338}/meta/pulls/*`.

**Simulate battery -- SIX SEPARATE invocations, ONE --resource-arns each (no conditions on the
PutObject statements, so no context-entries owed):**

```
T1  target 0824 meta/pulls:   s3:PutObject  .../schwab/08242234/meta/pulls/20260714T000000Z.json  allowed
T2  target 0833 meta/pulls:   s3:PutObject  .../schwab/08335338/meta/pulls/20260714T000000Z.json  allowed
P1  positive control (pre-existing _ops grant, SEPARATE invocation):
                              s3:PutObject  .../schwab/08242234/_ops/daily_pull/runs/x.json       allowed
N1  negative firm bucket:     s3:PutObject  arn:aws:s3:::opal-data-bd/49f/bronze/anything.zip     explicitDeny
N2  negative Door-6 sentinel (SIMULATION ONLY, no write):
                              s3:PutObject  arn:aws:s3:::opal-data-inf/gold/meta/pipeline-complete.json  explicitDeny
N3  negative pen-separation:  s3:PutObject  .../schwab/08242234/meta/conversions/forged.json      implicitDeny
```

Reading: both targets allow (the new grant, both masters); the positive control allows on a grant that
predates this change (the instrument can say yes independently of the target); the bd plane and Door-6
sentinel are EXPLICIT denies (the standing guardrails outrank any Allow); meta/conversions is implicitDeny
(the box cannot forge a conversion record -- the pen-separation this statement was scoped for).

**Tag:** `schwab-si2-iam-v1.4.0`. **Status: CLOSED, 2/2 legs, 2026-07-14 ~18:38Z.**
