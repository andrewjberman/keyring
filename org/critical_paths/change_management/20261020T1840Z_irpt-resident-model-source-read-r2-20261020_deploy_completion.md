# Deploy Completion Record
**Date opened:** 2026-10-20T18:40:59.897291+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-MODELGRANT v2: one-statement IAM grant (s3:GetObject on two exact keys of opal-data-portal-v2) on aws_iam_role_policy.runner_resident, re-pin 680818fdb3e
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | before-reads: live policy Sid list and sha256, four baseline simulations | R0 baseline implicitDeny on all four |  | OPEN |
| C | verify | scoped plan at the re-pin reads 0 to add 1 to change 0 to destroy with exactly one added statement | plan output and diff read |  | OPEN |
| A | activation | safe-apply of the saved plan | Apply complete 0 added 1 changed 0 destroyed |  | OPEN |
| V | verify | after-reads G1 to G4: byte-equal other statements, simulation, replan No changes, host-role reads of both objects | G1 G2 G3 G4 lines |  | OPEN |

## Log

- 20261020T184059Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
