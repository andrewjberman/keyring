# Deploy Completion Record
**Date opened:** 2026-09-10T22:40:29.777518+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260910T225443Z
**Deploy:** IRPT_BCKEND IB-s-17: apply the investor-reporting core root (KMS, opal-data-ycharts, 4 DynamoDB tables, 3 queues + 3 DLQs, the declared layout)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of the core root sources and the key grammar | commit hash on the worker branch | commit 34290ce98f on wk-irpt_bckend-1-1: core/{main,kms,s3,dynamodb,sqs,outputs}.tf + _keys/keys.py + _keys/tests/test_keys.py; commit-gate rc=0 on both .py files; 45 of 45 key-grammar tests passed | CLOSED 20260910T225413Z |
| L2 | activation | terraform apply of infra/aws/terraform/investor-reporting/core (state key investor-reporting/core/tfstate) | safe-apply Apply complete line with the resource count | safe-apply rc=0: 'Apply complete! Resources: 17 added, 0 changed, 0 destroyed.' -- halt-gate resolved worker 0.9.0_WK_IRPT_BCKEND~1 and scanned issuer 2.0.0_SA_COO~B; comp-tagauthz PASSED (0 candidates, no access-granting tag overwritten); tombstone-gate CLEAN on 17 creates vs 7 tombstones | CLOSED 20260910T225413Z |
| L3 | verify | post-apply live-state read of the bucket, the four tables and the six queues | the IB-s-17 battery output, every count beside its denominator | IB-s-17 battery arms (a)-(d) HELD on the applied plane, 27 read-only AWS calls: head-bucket 200; SSE aws:kms with key 7f4d3042-10d8-49a7-b55e-3c963cea8111 which IS alias/investor-reporting (alias resolved, arns compared); public-access-block 4 of 4 true; versioning Enabled; layout firms 3 of 3 == registry enabled client firms; bucket carries 0 objects (prefixes DECLARED, not created); 4 of 4 tables SSE-KMS with that key, PITR ENABLED, PAY_PER_REQUEST; 3 of 3 queues + 3 of 3 DLQs KMS-encrypted, MaximumMessageSize 4096, each RedrivePolicy naming its DLQ; 45 of 45 key-grammar tests passed, 7 of 7 II.3 components in a well-formed key, 5 of 5 client/firm-name components refused. Arm (e) correctly read this entry OPEN at that moment. | CLOSED 20260910T225443Z |
| L4 | verify | 0-diff plan on the applied root | terraform plan reading No changes | terraform plan -no-color -input=false -lock=false on infra/aws/terraform/investor-reporting/core, rc=0: 'No changes. Your infrastructure matches the configuration.' -- the applied plane and the record agree | CLOSED 20260910T225443Z |

## Log

- 20260910T224029Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 4 leg(s)
- 20260910T225413Z LEG L1 closed: commit 34290ce98f on wk-irpt_bckend-1-1: core/{main,kms,s3,dynamodb,sqs,outputs}.tf + _keys/keys.py + _keys/tests/test_k
- 20260910T225413Z LEG L2 closed: safe-apply rc=0: 'Apply complete! Resources: 17 added, 0 changed, 0 destroyed.' -- halt-gate resolved worker 0.9.0_WK_IR
- 20260910T225443Z LEG L3 closed: IB-s-17 battery arms (a)-(d) HELD on the applied plane, 27 read-only AWS calls: head-bucket 200; SSE aws:kms with key 7f
- 20260910T225443Z LEG L4 closed: terraform plan -no-color -input=false -lock=false on infra/aws/terraform/investor-reporting/core, rc=0: 'No changes. You
- 20260910T225443Z CLOSED -- all 4 legs proven
