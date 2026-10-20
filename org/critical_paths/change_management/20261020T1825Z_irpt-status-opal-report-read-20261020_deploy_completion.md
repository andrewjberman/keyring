# Deploy Completion Record
**Date opened:** 2026-10-20T18:25:49.876997+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-STATUSGRANT: irpt-status-role reads the YCHARTS_OPAL_REPORT PDF family: one statement's resource list extended by three entries on aws_iam_role_policy.irpt_status, drained commit 9b614db42a1
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | before-reads: live policy Sid list, retained-families resources, sha256, simulation get and getversion on the 7b PDF key | R0 baseline implicitDeny get and getversion |  | OPEN |
| C | verify | scoped plan at the drained commit reads 0 to add 1 to change 0 to destroy with exactly three added resource entries | plan output and diff read |  | OPEN |
| A | activation | safe-apply of the saved plan | Apply complete 0 added 1 changed 0 destroyed |  | OPEN |
| V | verify | after-reads G1 to G3: byte-equal other statements, simulation, replan No changes | G1 G2 G3 lines |  | OPEN |

## Log

- 20261020T182549Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
