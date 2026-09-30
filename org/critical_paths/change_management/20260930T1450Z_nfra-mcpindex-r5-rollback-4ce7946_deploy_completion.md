# Deploy Completion Record
**Date opened:** 2026-09-30T14:50:30.050675+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-6 ROLLBACK: restore opal-gateway to 2.0.0_SA_COO~RV's 4ce7946426 (my 2e2254156e overwrote it at 14:41:23Z) and roll back the targeted schwab reader-policy apply
**Authored by:** 2.0.0_SA_COO~MI
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| host | ec2-baked-asset | opal-gateway i-07dccb1615503ac99 -> 4ce7946426 | SSM read: server.py rivalfunds routes present, ENABLED_INTEGRATIONS 5 ids, -latest = 4ce7946426 |  | OPEN |
| iam | activation | aws_iam_role_policy.schwab_data_read_policy -> pre-change (no dim_transaction) | simulate dim_transaction explicitDeny both masters, dim_position allowed |  | OPEN |

## Log

- 20260930T145030Z OPENED by 2.0.0_SA_COO~MI with 2 leg(s)
