# Deploy Completion Record
**Date opened:** 2026-10-07T16:21:00.433493+00:00
**Status:** OPEN
**Deploy:** MDPF_HEALGAP.TO-HG-d2 (laptop box): targeted apply of cot_rebalancer_reattempt.tf -- aws_cloudwatch_event_target.cot_rebalancer_reattempt + aws_lambda_permission.cot_rebalancer_reattempt on existing rule cot-bronze-complete, invoking cot-rebalancer-runner with {mode:pull}
**Authored by:** 0.7.0_AE_CloudOps~F
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | act-0 live SKIP probe of cot-rebalancer-runner (CTO half condition 1) | response+log verdict SKIP-IDEMPOTENT and bronze rebalancer_*/<today>/ count unchanged | act-0 probe 2026-10-07T16:15:36Z, RequestResponse invoke of cot-rebalancer-runner payload {"mode":"pull"}, StatusCode 200, no FunctionError, RequestId 6fe29f10-fadc-4f05-9070-95b68cc7f072. Response: {"verdict": "SKIP-IDEMPOTENT", "as_of": "2026-10-07"}. Log tail (decoded LogResult): 'cot-rebalancer-runner invoked 2026-10-07T16:15:36Z firm=cottonwood bucket=opal-data-assets date=2026-10-07' then the same verdict; Duration 94.43 ms, Init 553.41 ms. Bronze s3api counts blackdiamond/cottonwood/bronze/rebalancer_{models,accounts,model_detail}/2026-10-07/ BEFORE 1/5/91=97, AFTER 1/5/91=97 (delta 0); newest model_detail key LastModified 2026-10-07T06:00:56Z; stamp meta/2026-10-07-complete.json unchanged 11679 B @2026-10-07T06:00:58Z. Live CodeSha256 QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk= re-read immediately before the invoke. Branch A proven live; the apply is authorized to proceed. | CLOSED 20261007T162217Z |
| L2 | verify | terraform plan -target on exactly the two resources, CHECKPOINT_DISABLE=1 | plan reads 2 to add, 0 to change, 0 to destroy; the change lines printed here |  | OPEN |
| L3 | activation | .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply with the same two -targets | apply output tail + 0-diff re-plan |  | OPEN |
| L4 | verify | HG1-d2-AC1 and HG1-d2-AC2 from hg_d2_applied.py | WIRED-OK and UNCHANGED-OK |  | OPEN |
| L5 | git | ledger close + record-terraform-deploy.sh (lambda-source-map.json, opal-assets CHANGELOG.json) | commit hash, exact pathspec |  | OPEN |

## Log

- 20261007T162100Z OPENED by 0.7.0_AE_CloudOps~F with 5 leg(s)
- 20261007T162217Z LEG L1 closed: act-0 probe 2026-10-07T16:15:36Z, RequestResponse invoke of cot-rebalancer-runner payload {"mode":"pull"}, StatusCode 20
