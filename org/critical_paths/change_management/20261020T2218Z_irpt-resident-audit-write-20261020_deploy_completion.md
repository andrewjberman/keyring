# Deploy Completion Record
**Date opened:** 2026-10-20T22:18:06.637969+00:00
**Status:** CLOSED -- STOPPED AT A, NOTHING APPLIED (IAM PutRolePolicy 409 LimitExceeded: the role's inline policies total 10131 of 10240 bytes and the grant adds 522; the live policy is unchanged) -- closed 20261020T222632Z
**Deploy:** IRPT_ANLREQ TO-APPLY-AUDITGRANT: Put-only statement WriteTheAnalysisAudit and three KMS context-list entries on aws_iam_role_policy.runner_resident for the resident host role, resident.tf blob efa98ea249
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | before-reads: live policy Sid list, KMS context list length, sha256, baseline simulations on a sample audit key | R0 baseline implicitDeny put on the audit key | R0 baseline implicitDeny put on the audit key at 2026-10-20T22:20Z: 15 Sids, WriteTheAnalysisAudit absent, KMS context list 21 entries with no analysis_audit entry; s3 PutObject, GetObject, GetObjectVersion, DeleteObject on a sample audit key and PutObject on another family all implicitDeny; controls: PutObject on a ycharts_opal_reports key allowed; KMS GenerateDataKey simulation for the audit key context = allowed at baseline, matched by the role's OTHER inline policies irpt-export-render-host-evidence and irpt-ycharts-runner (simulated, not measured live); open-deploys denominator 56 worktrees and 137 distinct entries, none non-terminal on the ycharts stack, the role or its policy (a18 read-evidence reference only); no other IB2 act open; COO blob 0d1ab2373f, CTO half names it, resident.tf blob efa98ea249 at trunk | CLOSED 20261020T222109Z |
| C | verify | scoped plan at the trunk commit reads 0 to add 1 to change 0 to destroy with exactly one added statement and three KMS entries | plan output and diff read | C plan 0 to add 1 to change 0 to destroy at 2026-10-20T22:2xZ from a throwaway detached worktree at trunk commit 480ceeae884ad29b (resident.tf blob efa98ea249 equal, fmt -check resident.tf rc 0, init, scoped -target plan saved); only attribute changed: policy; Sids 15 -> 16, exactly one new statement WriteTheAnalysisAudit (Allow, s3:PutObject only, no Condition) on exactly arn:aws:s3:::opal-data-irpt/irpt/{49financial,cottonwood,inflection}/platinum/analysis_audit/* (bucket is opal-data-irpt); KMS condition list 21 -> 24 adding exactly the same three, 0 removed, rest of that statement equal; 0 other statements changed; before sha256 c970dc35... equals the model grant's after value; planned sha256 2797b184...8aff | CLOSED 20261020T222246Z |
| A | activation | safe-apply of the saved plan | Apply complete 0 added 1 changed 0 destroyed | A NOT APPLIED: safe-apply 2026-10-20T22:24:33Z..22:25:27Z (first attempt 22:23:34Z blocked by the halt gate on routine already-READ messages, none STOP-class, broker 0 not-READ; nothing applied then; re-run with HALT_ACK=1) was refused by IAM: PutRolePolicy 409 LimitExceeded 'Maximum policy size of 10240 bytes exceeded for role irpt-ycharts-runner-role'; the live resident policy sha256 c970dc35... re-read equal to R0 (nothing changed); measured: the role's five inline policies total 10131 bytes (limit 10240, headroom 109); the grant adds +522, would total 10653, over by 413 | CLOSED 20261020T222631Z |
| V | verify | after-reads G1 to G3: byte-equal other statements, simulations, replan No changes | G1 G2 G3 lines | V NOT-RUN: nothing applied, so no after-reads G1 to G3 | CLOSED 20261020T222631Z |

## Log

- 20261020T221806Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261020T222109Z LEG R0 closed: R0 baseline implicitDeny put on the audit key at 2026-10-20T22:20Z: 15 Sids, WriteTheAnalysisAudit absent, KMS context l
- 20261020T222246Z LEG C closed: C plan 0 to add 1 to change 0 to destroy at 2026-10-20T22:2xZ from a throwaway detached worktree at trunk commit 480ceea
- 20261020T222631Z LEG A closed: A NOT APPLIED: safe-apply 2026-10-20T22:24:33Z..22:25:27Z (first attempt 22:23:34Z blocked by the halt gate on routine a
- 20261020T222631Z LEG V closed: V NOT-RUN: nothing applied, so no after-reads G1 to G3
- 20261020T222632Z CLOSED -- all 4 legs proven
