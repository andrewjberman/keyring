# Deploy Completion Record
**Date opened:** 2026-09-25T14:40:57.359970+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T060038Z
**Deploy:** Inflection Performance on Orion: modules packaged, grants, and ONE one-use plan (Andrew-direct @dd8178481e)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A2 | activation | aws_iam_role_policy.performance_retained + performance_approved_inf_session | IAM get-role-policy: INF accounts_v2 read, inflection in served firms, Orion session read only; COT session policy gone | iam get-role-policy irpt-performance-adapter-role: ReadINFMappingPartitionInventory (opal-data-inf, s3:prefix silver/api_dims/accounts_v2/) + ReadINFMappingSnapshots; LeadingKeys [cottonwood, 49financial, inflection]; irpt-performance-approved-inf-session-policy GetSecretValue on orion/jwt/current only; irpt-performance-approved-session-policy (COT) destroyed | CLOSED 20260925T144630Z |
| A3 | activation | IRPT_PERFORMANCE_APPROVED_PLAN env | deployed env plan digest b0b85aa9.. equals IRPT_PERF_VENDOR_EGRESS_AUTHORIZED | env IRPT_PERFORMANCE_APPROVED_PLAN: firm inflection, account acc_41e2e972281c3e42ef3f7a55, 2026-01-01..2026-09-25, expires 1790380800 (2026-09-26T00:00Z); sha256(plan) == IRPT_PERF_VENDOR_EGRESS_AUTHORIZED == b0b85aa98a09..; no claim row for it (irpt-requests full scan) | CLOSED 20260925T144630Z |
| V1 | verify | 0-diff re-plan of the performance root with the plan var-file | terraform plan reads No changes | terraform plan (vendored 1.9.8) with the INF plan var-file after apply: No changes. Your infrastructure matches the configuration. | CLOSED 20260925T144630Z |
| S1 | verify | served INF journey | the one Orion use claimed by a signed-in request and its report retained, or the plan expires unspent | measured 2026-09-27: this ledger's plan (acc_41e2e972.., 2026-01-01..2026-09-25, armed 09-25 14:4xZ) was NEVER claimed -- inflection PERFORMANCE_USE# rows are exactly 01209afb (claimed 1790392831, under Andrew-direct 2026-09-25T23:0xZ, a later plan that replaced this one in the env) and 7f64b166 (claimed 1790482274, call 2 of 'yes to all three'); the env holds no plan since 04:34:55Z (null). So branch 2 of S1 holds: the plan went unspent and was superseded by a later arm, with 0 Orion calls under it. INF's signed-in journey was then DONE under 7f64b166 (RPT-df47a1fc, ledger irpt-performance-inf-one-use-4-20260927). | CLOSED 20260927T060038Z |
| irpt-performance-adapter | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | get-function-configuration 14:4xZ: CodeSha256 DoNVpo57xHwyUKYUWykCpqDVOhIFhUAM59rQ6KLqzjs= == artifact content-sha256 (investor-reporting/irpt-performance-adapter.zip, 403925 bytes; source map pins 7cc62ce019 for retained/authorization/installed/entry + inf_selected/inf_account_mapping/orion_live/jwt_freshness); State Active, LastUpdateStatus Successful; keep-warm invoke 200, runtime built (Init 482 ms, 3165 ms), no error | CLOSED 20260925T144630Z |

## Log

- 20260925T144057Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260925T144630Z LEG irpt-performance-adapter closed: get-function-configuration 14:4xZ: CodeSha256 DoNVpo57xHwyUKYUWykCpqDVOhIFhUAM59rQ6KLqzjs= == artifact content-sha256 (i
- 20260925T144630Z LEG A2 closed: iam get-role-policy irpt-performance-adapter-role: ReadINFMappingPartitionInventory (opal-data-inf, s3:prefix silver/api
- 20260925T144630Z LEG A3 closed: env IRPT_PERFORMANCE_APPROVED_PLAN: firm inflection, account acc_41e2e972281c3e42ef3f7a55, 2026-01-01..2026-09-25, expir
- 20260925T144630Z LEG V1 closed: terraform plan (vendored 1.9.8) with the INF plan var-file after apply: No changes. Your infrastructure matches the conf
- 20260927T060038Z LEG S1 closed: measured 2026-09-27: this ledger's plan (acc_41e2e972.., 2026-01-01..2026-09-25, armed 09-25 14:4xZ) was NEVER claimed -
- 20260927T060038Z CLOSED -- all 5 legs proven
