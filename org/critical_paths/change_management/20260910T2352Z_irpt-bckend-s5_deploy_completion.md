# Deploy Completion Record
**Date opened:** 2026-09-10T23:52:05.890031+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260910T235708Z
**Deploy:** IRPT_BCKEND IB-s-5: apply the FirmDestinationPolicy IAM half on the investor-reporting core root (3 firm role stubs + 1 quarantine role stub, per-firm S3 prefix conditions, the generated policy document)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of roles.tf, iam_firm_conditions.tf, outputs.tf and the ingestion gate | commit hash on the worker branch | commit 14ad90c621 on wk-irpt_bckend-1-1: core/{roles,iam_firm_conditions,outputs}.tf + _gate/gate.py + _gate/tests/{test_gate,test_policy_completeness}.py; commit-gate rc=0 on all three .py files; 19 gate tests + 3 completeness tests passed against a scratch preview policy | CLOSED 20260910T235707Z |
| L2 | activation | terraform apply of infra/aws/terraform/investor-reporting/core (state key investor-reporting/core/tfstate) | safe-apply Apply complete line with the resource count | safe-apply rc=0: 'Apply complete! Resources: 13 added, 0 changed, 0 destroyed.' -- halt-gate scanned issuer 2.0.0_SA_COO~B; comp-tagauthz PASSED (0 candidates); tombstone-gate CLEAN on 13 creates vs 7 tombstones | CLOSED 20260910T235708Z |
| L3 | verify | post-apply live-state read of the roles, policies and the generated policy document via the IB-s-5 battery | the battery output, every count beside its denominator | IB-s-5 battery arms (a)-(e) HELD on the applied plane: 3 of 3 firms x 6 of 6 destination kinds land only in their own firms/<id>/ prefix; a cross-firm destination request refused, the same-firm call then succeeded; 4 of 4 fixtures (unknown/spoofed/contradictory/Opal-origin) never became a firm, with the policy's own outcome type on each; 3 of 3 immutability mutation attempts raised; the completeness test passed at HEAD (rc=0, 3 passed) and FAILED naming a planted 4th firm (rc=1) when pointed at a scratch registry. Arm (f) correctly read this entry OPEN at that moment. | CLOSED 20260910T235708Z |
| L4 | verify | 0-diff plan on the applied root | terraform plan reading No changes | terraform plan -no-color -input=false -lock=false on infra/aws/terraform/investor-reporting/core, rc=0: 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260910T235708Z |

## Log

- 20260910T235205Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 4 leg(s)
- 20260910T235707Z LEG L1 closed: commit 14ad90c621 on wk-irpt_bckend-1-1: core/{roles,iam_firm_conditions,outputs}.tf + _gate/gate.py + _gate/tests/{test
- 20260910T235708Z LEG L2 closed: safe-apply rc=0: 'Apply complete! Resources: 13 added, 0 changed, 0 destroyed.' -- halt-gate scanned issuer 2.0.0_SA_COO
- 20260910T235708Z LEG L3 closed: IB-s-5 battery arms (a)-(e) HELD on the applied plane: 3 of 3 firms x 6 of 6 destination kinds land only in their own fi
- 20260910T235708Z LEG L4 closed: terraform plan -no-color -input=false -lock=false on infra/aws/terraform/investor-reporting/core, rc=0: 'No changes. You
- 20260910T235708Z CLOSED -- all 4 legs proven
