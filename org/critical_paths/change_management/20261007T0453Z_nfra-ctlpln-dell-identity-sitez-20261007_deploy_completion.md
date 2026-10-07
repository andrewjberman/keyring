# Deploy Completion Record
**Date opened:** 2026-10-07T04:53:25.363116+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN TO-DELL-1 leg A: safe-apply of infra/aws/terraform/nfra-ctlpln-identity from a detached worktree at EXACTLY origin CLOUD 0ef817adb0; plan graded UNTARGETED 10 to add/0/0 with no aws_iam_access_key; both never-widen halves signed ahead of the plan (COO 2.0.0_SA_COO~Z, CTO 1.0.0_SA_CTO~Z @bbca23131f). ROLLBACK: one safe-apply destroy of this root, which reaches only the ten resources it creates and is clean ONLY while neither user holds an access key (this order creates none). NO access key by any means.
**Authored by:** 0.7.0_AE_CloudOps~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply of nfra-ctlpln-identity at 0ef817adb0 | ten resources created and a 0-diff re-plan |  | OPEN |
| V1 | verify | AC2 iam get-group cloudops-dell-agents-group | exactly the two dell users |  | OPEN |
| V2 | verify | AC3 list-access-keys per user | 0 and 0 |  | OPEN |
| V3 | verify | three live policy documents vs the JSON files bytes | equal |  | OPEN |
| V4 | verify | simulate_policy.py against the live identities + comp-iam gaps | all_ok and gaps read |  | OPEN |

## Log

- 20261007T045325Z OPENED by 0.7.0_AE_CloudOps~RV with 5 leg(s)
