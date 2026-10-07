# Deploy Completion Record
**Date opened:** 2026-10-07T04:53:25.363116+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261007T050642Z
**Deploy:** NFRA_CTLPLN TO-DELL-1 leg A: safe-apply of infra/aws/terraform/nfra-ctlpln-identity from a detached worktree at EXACTLY origin CLOUD 0ef817adb0; plan graded UNTARGETED 10 to add/0/0 with no aws_iam_access_key; both never-widen halves signed ahead of the plan (COO 2.0.0_SA_COO~Z, CTO 1.0.0_SA_CTO~Z @bbca23131f). ROLLBACK: one safe-apply destroy of this root, which reaches only the ten resources it creates and is clean ONLY while neither user holds an access key (this order creates none). NO access key by any means.
**Authored by:** 0.7.0_AE_CloudOps~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply of nfra-ctlpln-identity at 0ef817adb0 | ten resources created and a 0-diff re-plan | safe-apply of infra/aws/terraform/nfra-ctlpln-identity from detached worktree C:/tmp/dell-identity-0ae63f9 at EXACTLY 0ef817adb0, applying the graded saved plan dell-identity.tfplan: 'Apply complete! Resources: 10 added, 0 changed, 0 destroyed.' Re-plan -detailed-exitcode rc=0 'No changes. Your infrastructure matches the configuration.' terraform state list = 10 resources, aws_iam_access_key in state = 0 (CTO condition 2). HALT-GATE did NOT pass and no pass is cited: it fail-closed because its resolver admits a single-uppercase-letter lane only (halt-gate-check.sh:174) and this lane is ~RV; cleared by the audited HALT_OVERRIDE after reading the sound instrument instead -- broker check_inbox empty, 20/20 delivery rows READ+acked by this serial, 0 STOP/HALT-class. Surprise row filed. | CLOSED 20261007T050610Z |
| V1 | verify | AC2 iam get-group cloudops-dell-agents-group | exactly the two dell users | AC2 PASS: .tools/aws iam get-group --group-name cloudops-dell-agents-group --query sort(Users[].UserName) --output json = ["cloudops-dell1-agent-user","cloudops-dell2-agent-user"], exactly the two and no third. NEGATIVE ARM recorded pre-apply: all three principals and all three policies NoSuchEntity. | CLOSED 20261007T050610Z |
| V2 | verify | AC3 list-access-keys per user | 0 and 0 | AC3 PASS: list-access-keys --query length(AccessKeyMetadata) = 0 for cloudops-dell1-agent-user and 0 for cloudops-dell2-agent-user. No key created by this order by any means; leg (2) is 0.0.0_AB_MSTR~Z's act. | CLOSED 20261007T050610Z |
| V3 | verify | three live policy documents vs the JSON files bytes | equal | CTO condition 5 (documents, not names) PASS 3/3: each policy's DEFAULT VERSION document (all v1) canonical-JSON-equal to the repo JSON at 0ef817adb0 -- deploy policy 8 statements live = 8 repo, dell1-bus 1=1, dell2-bus 1=1, Version 2012-10-17 both sides. Attachments live: group -> cloudops-dell-agent-deploy-policy; dell1 -> cloudops-dell1-agent-bus-policy; dell2 -> cloudops-dell2-agent-bus-policy. | CLOSED 20261007T050610Z |
| V4 | verify | simulate_policy.py against the live identities + comp-iam gaps | all_ok and gaps read | Two arms. CUSTOM-POLICY arm, simulate_policy.py post-apply exit=0: allowed_ok=8/8 denied_ok=11/11 all_ok=True. LIVE-PRINCIPAL arm (the arm simulate_policy.py does NOT cover -- it calls SimulateCustomPolicy on the document, never the principal): simulate_principal_policy against both live user ARNs, 10/10 as expected, ONE --resource-arns per call per the four false-deny modes; the per-user queue isolation implicitDeny carries its positive control as a SEPARATE invocation (dell1 ReceiveMessage on its OWN queue = allowed, on dell2's = implicitDeny, mirrored for dell2), so that deny is the world and not the instrument. comp-iam gaps RUN: 37 missing / 294 deny-present / 1 coverage-unknown / 3 resource-mismatch across 33 services, ALL pre-existing estate rows and none naming a cloudops-dell principal -- and that silence is NOT evidence about the Dells: comp-iam models Lambda/EC2 ROLES and cannot see an IAM user at all, so this apply is outside its domain, stated as such rather than read as clean. | CLOSED 20261007T050641Z |

## Log

- 20261007T045325Z OPENED by 0.7.0_AE_CloudOps~RV with 5 leg(s)
- 20261007T050610Z LEG A1 closed: safe-apply of infra/aws/terraform/nfra-ctlpln-identity from detached worktree C:/tmp/dell-identity-0ae63f9 at EXACTLY 0e
- 20261007T050610Z LEG V1 closed: AC2 PASS: .tools/aws iam get-group --group-name cloudops-dell-agents-group --query sort(Users[].UserName) --output json 
- 20261007T050610Z LEG V2 closed: AC3 PASS: list-access-keys --query length(AccessKeyMetadata) = 0 for cloudops-dell1-agent-user and 0 for cloudops-dell2-
- 20261007T050610Z LEG V3 closed: CTO condition 5 (documents, not names) PASS 3/3: each policy's DEFAULT VERSION document (all v1) canonical-JSON-equal to
- 20261007T050641Z LEG V4 closed: Two arms. CUSTOM-POLICY arm, simulate_policy.py post-apply exit=0: allowed_ok=8/8 denied_ok=11/11 all_ok=True. LIVE-PRIN
- 20261007T050642Z CLOSED -- all 5 legs proven
