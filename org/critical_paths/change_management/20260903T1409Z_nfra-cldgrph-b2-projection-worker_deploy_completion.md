# Deploy Completion Record
**Date opened:** 2026-09-03T14:09:33.411021+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260903T170415Z
**Deploy:** NFRA_CLDGRPH B2 projection worker Fargate port
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD worker and Terraform commit | commit hash pushed and remote ancestor | a9ceed34864a4ffcc44b8fbd4e083f44233b53f2 is ancestor of origin/CLOUD 6cabd10827ce1d10a518f8f3a33afc2533caf7a5 | CLOSED 20260903T141203Z |
| L2 | activation | derive-runner shared image | CodeBuild SUCCEEDED and ECR digest | CodeBuild globgrph-derive-build:e8698da1-b93f-465b-ae23-15db9ff0833e and corrective build globgrph-derive-build:b72c8766-3ea5-4ce5-ab43-55bdb9599afa SUCCEEDED; ECR latest digest sha256:3a4e078d2c65c0243f2aac3c2ad033ac7a154c12cc46d7b9998cf37601188486 (tag 20260903-143221) | CLOSED 20260903T141419Z |
| L3 | activation | projection worker Terraform target set | safe-apply exact target plan with 0 destroy | safe-apply saved b2-projection.tfplan: Apply complete 10 added, 0 changed, 0 destroyed; exact 10 owned addresses | CLOSED 20260903T141652Z |
| L4 | verify | projection worker live plane | unscoped re-plan address assertion, IAM read, and cloud paths exercised | Unscoped Terraform 1.9.8 re-plan exact 4 foreign addresses and 0 B2-owned addresses; live worker IAM 2 inline policies/4 statements/0 attached with no new comp-iam gap; two TestEvents consumed with 0 RunTask; authentic incremental_updater marker 2026-09-03T16:27:39.471730+00:00 traversed S3->SQS->Pipe->RunTask fa5df7737afc48fdbda6a9106d5676b6 exit 0, full-cold worker 834.825s/engine 833.250s/peak 5795.848 MiB, nodes 27206/edges 58550/skipped 383, artifact 48046080 B + manifest 1632 B, independent Kuzu/hash readback exact, pointer advanced | CLOSED 20260903T164726Z |

## Log

- 20260903T140933Z OPENED by 0.7.0_AE_CloudOps~S with 4 leg(s)
- 20260903T141203Z LEG L1 closed: a9ceed34864a4ffcc44b8fbd4e083f44233b53f2 is ancestor of origin/CLOUD 6cabd10827ce1d10a518f8f3a33afc2533caf7a5
- 20260903T141419Z LEG L2 closed: CodeBuild globgrph-derive-build:e8698da1-b93f-465b-ae23-15db9ff0833e and corrective build globgrph-derive-build:b72c8766-3ea5-4ce5-ab43-55bdb9599afa SUCCEEDED; ECR latest digest sha256:3a4e078d2c65c0243f2aac3c2ad033ac7a154c12cc46d7b9998cf37601188486 (tag 20260903-143221)
- 20260903T141652Z LEG L3 closed: safe-apply saved b2-projection.tfplan: Apply complete 10 added, 0 changed, 0 destroyed; exact 10 owned addresses
- 20260903T164726Z LEG L4 closed: Unscoped Terraform 1.9.8 re-plan exact 4 foreign addresses and 0 B2-owned addresses; live worker IAM 2 inline policies/4
- 20260903T170415Z CLOSED -- all 4 legs proven
