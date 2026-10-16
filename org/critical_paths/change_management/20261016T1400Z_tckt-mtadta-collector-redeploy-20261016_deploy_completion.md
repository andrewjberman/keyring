# Deploy Completion Record
**Date opened:** 2026-10-16T14:00:59.394582+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T140321Z
**Deploy:** TCKT_MTADTA round 2 item 5a: redeploy the collector Lambda (time budget, parallel fetch, timeout 900)
**Authored by:** 0.7.0_AE_CloudOps~TM1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| apply | activation | aws_lambda_function.collector in infra/aws/terraform/trino (code hash and timeout only) | plan = 1 in-place update, 0 add, 0 destroy, 0 replace; safe-apply rc=0 | plan 0 add / 1 change / 0 destroy (aws_lambda_function.collector in place: source_code_hash, timeout); safe-apply rc=0 Apply complete 0 added 1 changed 0 destroyed at 2026-10-16T14:02:53Z | CLOSED 20261016T140321Z |
| live-config | verify | m365-metadata-trino-collector-lambda Timeout and CodeSha256 | get-function-configuration Timeout=900 and CodeSha256 equals the built zip | get-function-configuration: Timeout 900, CodeSha256 Vdi5YOJMM7Uxu25BfX0HMVUDkhvULY+tkR02lZKWMq4= equals the sha256 of the built zip; State Active, LastUpdateStatus Successful | CLOSED 20261016T140321Z |

## Log

- 20261016T140059Z OPENED by 0.7.0_AE_CloudOps~TM1 with 2 leg(s)
- 20261016T140321Z LEG apply closed: plan 0 add / 1 change / 0 destroy (aws_lambda_function.collector in place: source_code_hash, timeout); safe-apply rc=0 A
- 20261016T140321Z LEG live-config closed: get-function-configuration: Timeout 900, CodeSha256 Vdi5YOJMM7Uxu25BfX0HMVUDkhvULY+tkR02lZKWMq4= equals the sha256 of th
- 20261016T140321Z CLOSED -- all 2 legs proven
