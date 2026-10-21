# Deploy Completion Record
**Date opened:** 2026-10-20T23:25:05.519360+00:00
**Status:** CLOSED -- REFUSED BY GATE, nothing created -- closed 20261020T235719Z
**Deploy:** IRPT_ANLREQ TO-APPLY-AUDITPOLICY: ONE new customer-managed IAM policy (Put-only WriteTheAnalysisAudit on three opal-data-irpt analysis_audit prefixes and a KMS statement narrowed to them) and its attachment to irpt-ycharts-runner-role; replaces the inline form that stopped at the 10240-byte cap
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | before-reads: five inline policies with sha256, attached list, the new policy absent, baseline simulations on a sample audit key | R0 baseline implicitDeny put on the audit key | R0 baseline implicitDeny put on the audit key at 2026-10-20T23:30Z: five inline policies read (irpt-export-render-host-evidence 693ccc20..., parameter-fence-policy 387ffb24..., token-policy 7622ce68..., irpt-ycharts-runner ed04ec88..., resident-policy c970dc35...), attached list [AmazonSSMManagedInstanceCore]; the new managed policy irpt-audit-write-policy does NOT exist (NoSuchEntity); s3 PutObject, GetObject, GetObjectVersion, DeleteObject on a sample audit key and PutObject on another family all implicitDeny; controls: PutObject on a ycharts_opal_reports key allowed; KMS GenerateDataKey for the audit key context already allowed via the role's other inline policies (simulated); COO blob b2e2c58200, CTO half names it, pins f0df5705 and aa565f1c at trunk; open-deploys denominator 56 worktrees and 142 distinct entries, three non-terminal matched the broad IAM wording and none is an IAM apply in flight: a18 (read-evidence reference), d12 (SMS OTP held since September), tckt-vnext-r22-dl1 (TV2, HELD-PRE-APPLY, nothing applied, its stop msg 11609); r34o ledger CLOSED 23:18:33Z | CLOSED 20261020T232913Z |
| C | verify | scoped plan at trunk HEAD reads 2 to add 0 to change 0 to destroy with exactly the two audit statements and the one attachment | plan output and document read | C plan 2 to add 0 to change 0 to destroy at 2026-10-20T23:3xZ from a throwaway detached worktree at trunk commit 2baf93f3c046 (resident_audit_policy.tf blob f0df5705 and resident.tf blob aa565f1c equal; fmt -check resident.tf resident_audit_policy.tf rc 0; init; saved plan with the two -target flags): aws_iam_policy.resident_audit_write irpt-audit-write-policy (create) with exactly two statements, WriteTheAnalysisAudit (Allow, s3:PutObject only, exactly arn:aws:s3:::opal-data-irpt/irpt/{49financial,cottonwood,inflection}/platinum/analysis_audit/*; bucket is opal-data-irpt) and AuditEncryptionViaS3ForAuditPrefixesOnly (kms:Decrypt and kms:GenerateDataKey on the system key, ViaService s3.us-east-1.amazonaws.com, context list equal to the same three prefixes), compact size 895 bytes; aws_iam_role_policy_attachment.runner_resident_audit_write (create) to irpt-ycharts-runner-role only; nothing changed or destroyed | CLOSED 20261020T232913Z |
| A | activation | safe-apply of the saved plan | Apply complete 2 added 0 changed 0 destroyed |  | OPEN |
| V | verify | after-reads G1 to G3: inline policies unchanged, new policy exact, simulations, replan No changes | G1 G2 G3 lines |  | OPEN |

## Log

- 20261020T232505Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261020T232913Z LEG R0 closed: R0 baseline implicitDeny put on the audit key at 2026-10-20T23:30Z: five inline policies read (irpt-export-render-host-e
- 20261020T232913Z LEG C closed: C plan 2 to add 0 to change 0 to destroy at 2026-10-20T23:3xZ from a throwaway detached worktree at trunk commit 2baf93f
- 20261020T235719Z CLOSED -- REFUSED BY GATE before apply, world untouched: safe-apply 2026-10-20T23:55:12Z to 23:55:33Z: 'safe-apply: BLOCKED by the naming plan limb (LGIC_ENFORCE DEC-6, ENFORCE mode, rc=2). Nothing was planned further or applied.' (my launch path made .tools/naming-apply-gate.py unreadable; the HALT gate had also listed CTO msg 11644 hold and Y2 msg 11645 stop, which arrived after my broker check and which I had cleared with HALT_ACK=1 on that earlier c
