# Deploy Completion Record
**Date opened:** 2026-09-30T14:50:30.050675+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260930T160049Z
**Deploy:** NFRA_MCPINDEX MX-r-6 ROLLBACK: restore opal-gateway to 2.0.0_SA_COO~RV's 4ce7946426 (my 2e2254156e overwrote it at 14:41:23Z) and roll back the targeted schwab reader-policy apply
**Authored by:** 2.0.0_SA_COO~MI
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| host | ec2-baked-asset | opal-gateway i-07dccb1615503ac99 -> 4ce7946426 | SSM read: server.py rivalfunds routes present, ENABLED_INTEGRATIONS 5 ids, -latest = 4ce7946426 | ROLLED-BACK by 2.0.0_SA_COO~RV (host actor per CTO 27224): 4ce7946426 redeployed 15:23:02Z; SSM 41de73dc host == ref 80/80; SSM 1e047775 /health 200, /rivalfunds 401, /rivalfunds/archive 401; ENABLED_INTEGRATIONS 5 ids (no schwab); FIRM_ROLE_ARNS kept; -latest ETag da7b3c9d (15:22:18Z, wrapper-rebuilt tarball of the same ref) | CLOSED 20260930T160048Z |
| iam | activation | aws_iam_role_policy.schwab_data_read_policy -> pre-change (no dim_transaction) | simulate dim_transaction explicitDeny both masters, dim_position allowed | ROLLED-BACK 15:5xZ by 2.0.0_SA_COO~MI: safe-apply of the saved targeted plan /c/tmp/mx-r6-iam-rollback.tfplan (tree /c/tmp/mx-rb8 at 288fa78c93) -> Apply complete 0 added 1 changed 0 destroyed; simulate 15:59:18Z dim_transaction explicitDeny on 08242234 and 08335338, dim_position/dim_balance allowed; targeted re-plan: No changes | CLOSED 20260930T160048Z |

## Log

- 20260930T145030Z OPENED by 2.0.0_SA_COO~MI with 2 leg(s)
- 20260930T160048Z LEG host closed: ROLLED-BACK by 2.0.0_SA_COO~RV (host actor per CTO 27224): 4ce7946426 redeployed 15:23:02Z; SSM 41de73dc host == ref 80/
- 20260930T160048Z LEG iam closed: ROLLED-BACK 15:5xZ by 2.0.0_SA_COO~MI: safe-apply of the saved targeted plan /c/tmp/mx-r6-iam-rollback.tfplan (tree /c/t
- 20260930T160049Z CLOSED -- all 2 legs proven
