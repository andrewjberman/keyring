# Deploy Completion Record
**Date opened:** 2026-10-01T09:06:30.466674+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPMSP MS-d-2 narrow gateway release on 05e3eff563
**Authored by:** 0.9.0_WK_NFRA_MCPMSP~5
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| host | ec2-baked-asset | i-07dccb1615503ac99 /opt/opal-gateway: release 2c0f84966d (gateway tree eaafbae398) deployed with DEPLOY_BASE_REF=05e3eff563; rollback = redeploy 05e3eff563 | d2.AC3 PASS (SSM Success, /health 200, 3 new modules md5 == release, .env 39 keys with both principal keys, tool count unchanged) + in-process internal_role.s3_client() read of a query_v0 key |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit=2c0f84966d on wk-NFRA_MCPMSP-5d | d2.AC2 PASS + safe-commit hash |  | OPEN |

## Log

- 20261001T090630Z OPENED by 0.9.0_WK_NFRA_MCPMSP~5 with 2 leg(s)
