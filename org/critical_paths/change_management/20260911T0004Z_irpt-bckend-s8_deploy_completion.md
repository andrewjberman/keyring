# Deploy Completion Record
**Date opened:** 2026-09-11T00:04:39.757689+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-s-8: apply the investor-reporting/ycharts root -- YCharts runner host APPLIED STOPPED, its role, its security group and the two SSM documents
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | terraform root infra/aws/terraform/investor-reporting/ycharts (state key investor-reporting/ycharts/tfstate) -- 9 resources ADD, 0 change, 0 destroy | safe-apply Apply complete line |  | OPEN |
| L2 | verify | the host is STOPPED on the live plane | aws ec2 describe-instances State.Name == stopped |  | OPEN |
| L3 | verify | the root is CONVERGED after the apply | terraform plan: No changes. Your infrastructure matches the configuration. |  | OPEN |
| L4 | git | the runner, the terraform, the ledger sentinel and the deliverables on wk-irpt_bckend-1-3 | commit hash |  | OPEN |

## Log

- 20260911T000439Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 4 leg(s)
