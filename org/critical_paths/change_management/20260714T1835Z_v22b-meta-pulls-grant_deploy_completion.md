# Deploy Completion Record
**Date opened:** 2026-07-14T18:35:00+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260716T130343Z
**Deploy:** V2-2(b): MonolithSchwabMetaPullsWrite statement-add (0/1/0) on quartz-si2-monolith-write -- PutObject schwab/{m}/meta/pulls/* only; CTO gate SIGNED + GO 20260714T183215Z
**Authored by:** 0.6.2_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | terraform | safe-apply canonical-schwab-ec2 (0/1/0 statement-add) + 0-diff re-plan | re-plan 0/1/0 immediately pre-apply + safe-apply complete + post-apply 0-diff plan | re-plan 0/1/0 immediately pre-apply; safe-apply (HALT_ACK routine) completed 2026-07-14 ~18:36Z; post-apply plan verdict verbatim: "No changes. Your infrastructure matches the configuration."; module infra/aws/terraform/canonical-schwab-ec2 (aws_iam_role_policy.schwab_si2_monolith_write); CTO IAM gate SIGNED + apply GO 20260714T183215Z (statement reviewed at source @ c03a8529c); tag schwab-si2-iam-v1.4.0 | CLOSED 20260716T130342Z |
| L2 | verify | get-role-policy APPLIED + simulate battery (target x2, positive control separate, negatives x3) | live get-role-policy APPLIED truth + simulate battery (ONE --resource-arns per call, positive control a SEPARATE invocation) | APPLIED truth RE-VERIFIED LIVE 2026-07-16 ~12:5xZ on the primitive (NOT the 07-14 self-report): aws iam get-role-policy --role-name quartz-si2-spike-role --policy-name quartz-si2-monolith-write -> Sid MonolithSchwabMetaPullsWrite = Allow s3:PutObject on EXACTLY arn:aws:s3:::opal-data-assets/schwab/08242234/meta/pulls/* + arn:aws:s3:::opal-data-assets/schwab/08335338/meta/pulls/*, Condition NONE (so no --context-entries owed). Simulate battery 6/6 @ 2026-07-14 ~18:37Z, SIX SEPARATE invocations, ONE --resource-arns each: T1 0824 meta/pulls allowed; T2 0833 meta/pulls allowed; P1 positive control (pre-existing _ops grant) allowed as a SEPARATE invocation; N1 opal-data-bd/49f explicitDeny; N2 opal-data-inf Door-6 pipeline-complete.json explicitDeny (SIMULATION ONLY, no write); N3 meta/conversions implicitDeny (pen-separation) | CLOSED 20260716T130342Z |

## Log

- 20260714T183500Z OPENED by 0.6.2_AE_PartnerETL with 2 leg(s) (hand-authored sentinel -- NOT via deploy_ledger.py open)
- 2026-07-16T~12:5xZ schema-repair by 0.6.2: the 07-14 close @ bcddb202f was a HAND-EDIT of this sentinel (tool never ran, so the sentinel stayed LIVE and the gate correctly read L1+L2 stranded -> RED for ~40h). Adding the log + proof_required/proof scaffolding the tool needs to execute its OWN close+unlink. Same class as 0.5.0's c4 @ f0f2a002b. The DEPLOY was never half-landed; the GATE INPUT was. Never hand-edit a sentinel.
- 20260716T130342Z LEG L1 closed: re-plan 0/1/0 immediately pre-apply; safe-apply (HALT_ACK routine) completed 2026-07-14 ~18:36Z; post-apply plan verdict
- 20260716T130342Z LEG L2 closed: APPLIED truth RE-VERIFIED LIVE 2026-07-16 ~12:5xZ on the primitive (NOT the 07-14 self-report): aws iam get-role-policy 
- 20260716T130343Z CLOSED -- all 2 legs proven
