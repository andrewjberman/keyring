# Deploy Completion Record
**Date opened:** 2026-10-16T13:46:23.904119+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / collector repair: the 13:31Z scheduled fire timed out at 300 s (row TCKT_MTADTA-D1-S11); owner 2.0.0_SA_COO~S1 (held since 2026-10-16T13:46:34.624460+00:00)
**Deploy:** TCKT_MTADTA round 2: secret values, three subscriptions, scheduled fires
**Authored by:** 0.7.0_AE_CloudOps~TM1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| secret-values | activation | m365-metadata/trino/api-credentials (Andrew's act) and m365-metadata/trino/subject-key (this seat) | r2_check_r2.py app -> R2-APP-OK | r2_check_r2.py app -> R2-APP-OK keys=tenant_id,client_id,client_secret (13:2xZ); subject-key written once, 64 chars, never printed | CLOSED 20261016T134634Z |
| subscriptions | activation | Office 365 Management API Audit.Exchange, Audit.SharePoint, Audit.General | three starts HTTP 200 and r2_check_r2.py subs -> R2-SUBS-OK | 2026-10-16T13:22:40Z Audit.Exchange HTTP 200, Audit.SharePoint HTTP 200, Audit.General HTTP 200; r2_check_r2.py subs -> R2-SUBS-OK Audit.Exchange,Audit.General,Audit.SharePoint | CLOSED 20261016T134634Z |
| fires | verify | two clean scheduled collector fires after the start time | two scheduled fires with Status other than timeout and CloudWatch Errors = 0 |  | OPEN |

## Log

- 20261016T134623Z OPENED by 0.7.0_AE_CloudOps~TM1 with 3 leg(s)
- 20261016T134634Z LEG secret-values closed: r2_check_r2.py app -> R2-APP-OK keys=tenant_id,client_id,client_secret (13:2xZ); subject-key written once, 64 chars, nev
- 20261016T134634Z LEG subscriptions closed: 2026-10-16T13:22:40Z Audit.Exchange HTTP 200, Audit.SharePoint HTTP 200, Audit.General HTTP 200; r2_check_r2.py subs -> 
- 20261016T134634Z HELD-SOVEREIGN-GATED gate=external/collector repair: the 13:31Z scheduled fire timed out at 300 s (row TCKT_MTADTA-
