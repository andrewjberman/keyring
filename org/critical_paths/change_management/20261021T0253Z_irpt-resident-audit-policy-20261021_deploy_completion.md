# Deploy Completion Record
**Date opened:** 2026-10-21T02:53:45.410162+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T030011Z
**Deploy:** IRPT_ANLREQ TO-APPLY-AUDITPOLICY (re-pinned pair, GO 11786): ONE new customer-managed IAM policy (Put-only WriteTheAnalysisAudit on three opal-data-irpt analysis_audit prefixes and a KMS statement narrowed to them) and its attachment to irpt-ycharts-runner-role; the earlier ledger irpt-resident-audit-policy-20261020 is CLOSED as refused by gate
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | before-reads: five inline policies with sha256, attached list, the new policy absent, baseline simulations on a sample audit key | R0 baseline implicitDeny put on the audit key | R0 baseline implicitDeny put on the audit key at 02:54Z: five inline policies read (hashes equal the 20261020 R0: 693ccc20, 387ffb24, 7622ce68, ed04ec88, c970dc35), attached [AmazonSSMManagedInstanceCore]; irpt-audit-write-policy NoSuchEntity; s3 Put/Get/GetVersion/Delete on the sample audit key and Put on another family implicitDeny, control Put on ycharts_opal_reports allowed; KMS audit-key context allowed via the role's other inline policies; COO blob 9f065fb2a5 and re-signed CTO half bound to it; pins 0e084af9b8 and 2e9a61e656 equal at HEAD 382ebe4a5a; open-deploys 50 worktrees 149 entries, 14 terminal and 2 non-terminal name the stack/role/IAM wording: d12 (SMS, held) and a18 (NFRA_TRNSPT, HELD-SOVEREIGN-GATED, its own second_reader roles in another stack, names this role only as a read-evidence gate; no apply in flight) | CLOSED 20261021T025458Z |
| C | verify | scoped plan at trunk HEAD reads 2 to add 0 to change 0 to destroy with exactly the two audit statements and the one attachment | plan output and document read | C plan 2 to add 0 to change 0 to destroy from a throwaway detached worktree at trunk d582c683af8 (resident_audit_policy.tf blob 0e084af9b8 and resident.tf blob 2e9a61e656 equal; fmt -check rc 0; init; saved plan with the two -target flags): aws_iam_policy.resident_audit_write irpt-audit-write-policy (create) with exactly two statements, WriteTheAnalysisAudit (Allow, s3:PutObject only, exactly arn:aws:s3:::opal-data-irpt/irpt/{49financial,cottonwood,inflection}/platinum/analysis_audit/*; bucket is opal-data-irpt) and AuditEncryptionViaS3ForAuditPrefixesOnly (kms:Decrypt and kms:GenerateDataKey on the system key, ViaService s3.us-east-1.amazonaws.com, context list equal to the same three prefixes), compact size 895 bytes; attachment runner_resident_audit_write (create) to irpt-ycharts-runner-role only; nothing changed or destroyed | CLOSED 20261021T025608Z |
| A | activation | safe-apply of the saved plan | Apply complete 2 added 0 changed 0 destroyed | safe-apply 2026-10-21T02:56:36Z to 02:57:52Z rc 0: Apply complete! Resources: 2 added, 0 changed, 0 destroyed (irpt-audit-write-policy and its attachment to irpt-ycharts-runner-role); halt gate passed without HALT_ACK | CLOSED 20261021T030010Z |
| V | verify | after-reads G1 to G3: inline policies unchanged, new policy exact, simulations, replan No changes | G1 G2 G3 lines | G1 five inline policies' canonical sha256 equal R0; attached list R0 plus irpt-audit-write-policy; default version v1 holds exactly the two statements; entities: the runner role only. G2 Put allowed (matched irpt-audit-write-policy), Get/GetVersion/Delete implicitDeny on the audit key, Put on another family unchanged implicitDeny, KMS allowed. G3 replan of the same targets: No changes | CLOSED 20261021T030010Z |

## Log

- 20261021T025345Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261021T025458Z LEG R0 closed: R0 baseline implicitDeny put on the audit key at 02:54Z: five inline policies read (hashes equal the 20261020 R0: 693ccc
- 20261021T025608Z LEG C closed: C plan 2 to add 0 to change 0 to destroy from a throwaway detached worktree at trunk d582c683af8 (resident_audit_policy.
- 20261021T030010Z LEG A closed: safe-apply 2026-10-21T02:56:36Z to 02:57:52Z rc 0: Apply complete! Resources: 2 added, 0 changed, 0 destroyed (irpt-audi
- 20261021T030010Z LEG V closed: G1 five inline policies' canonical sha256 equal R0; attached list R0 plus irpt-audit-write-policy; default version v1 ho
- 20261021T030011Z CLOSED -- all 4 legs proven
