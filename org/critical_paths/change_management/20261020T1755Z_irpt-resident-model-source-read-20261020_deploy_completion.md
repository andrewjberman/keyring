# Deploy Completion Record
**Date opened:** 2026-10-20T17:55:27.373528+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-MODELGRANT: one-statement IAM grant (s3:GetObject on two exact keys of opal-data-portal-v2) on aws_iam_role_policy.runner_resident for the resident host role
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | before-reads: live policy sid list and sha256, four baseline simulations | R0 baseline implicitDeny on all four |  | OPEN |
| C | verify | scoped plan at the pin 50f7c709af2 reads 0 to add 1 to change 0 to destroy with exactly one added statement | plan output and diff read |  | OPEN |
| A | activation | safe-apply of the saved plan | Apply complete 0 added 1 changed 0 destroyed |  | OPEN |
| V | verify | after-reads G1 to G4: byte-equal other statements, simulation, replan No changes, host-role reads of both objects | G1 G2 G3 G4 lines |  | OPEN |

## Log

- 20261020T175527Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
