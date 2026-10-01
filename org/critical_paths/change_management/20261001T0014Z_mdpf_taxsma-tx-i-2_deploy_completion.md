# Deploy Completion Record
**Date opened:** 2026-10-01T00:14:11.628489+00:00
**Status:** OPEN
**Deploy:** MDPF_TAXSMA TX-i-2: the egress publisher role's read of the one Tax control key (mdpf-publisher-taxsma-control-read-policy); opal-assets root, 1 create, nothing else
**Authored by:** 4.0.0_SA_CRO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | fresh saved plan of infra/aws/terraform/opal-assets from the shared tree | Plan 1/0/0 = aws_iam_role_policy.mdpf_egress_publisher_taxsma_control; baseline before the edit: No changes |  | OPEN |
| D1 | activation | safe-apply of the saved plan | apply complete 1 added; re-plan No changes |  | OPEN |
| V1 | verify | the publisher role's grants | control key GetObject allowed; taxsma_assets, dispositions, workbook, secret denied; existing served-write and Gold grants unchanged |  | OPEN |

## Log

- 20261001T001411Z OPENED by 4.0.0_SA_CRO with 3 leg(s)
