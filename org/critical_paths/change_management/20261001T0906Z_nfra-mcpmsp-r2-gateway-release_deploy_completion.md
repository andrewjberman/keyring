# Deploy Completion Record
**Date opened:** 2026-10-01T09:06:30.466674+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T091939Z
**Deploy:** NFRA_MCPMSP MS-d-2 narrow gateway release on 05e3eff563
**Authored by:** 0.9.0_WK_NFRA_MCPMSP~5
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| host | ec2-baked-asset | i-07dccb1615503ac99 /opt/opal-gateway: release 2c0f84966d (gateway tree eaafbae398) deployed with DEPLOY_BASE_REF=05e3eff563; rollback = redeploy 05e3eff563 | d2.AC3 PASS (SSM Success, /health 200, 3 new modules md5 == release, .env 39 keys with both principal keys, tool count unchanged) + in-process internal_role.s3_client() read of a query_v0 key | deploy rc=0 (log /c/tmp/ms-d2-deploy.log), base guard equal 05e3eff563 at both reads, uploaded git-ref 2c0f84966dc452d367ab1e4fc5d4849f08c1625e (S3 LastModified 2026-10-01T09:08:28Z), deploy SSM 2470cda4-dc66-4582-aa27-6391fa6f0bc1 Success; d2.AC3 (SSM 653c22a1-a7e2-4ff9-9a9e-ac344b2a51c7 Success): /health=200; internal_role/sender_gate/admin_refusals md5 match release blobs; tenant_registry present; INTERNAL_READER_ROLE_ARN lines=1; MSP_CALLING_IDENTITIES lines=1; .env keys=39; MASTER_ADMIN_PRINCIPALS lines=1; WRITE_CAPABLE_PRINCIPALS lines=1; RESULT: PASS exit=0. Tool count in-process on host (SSM 8c52a4fb-4a15-4a52-a123-45d4b8ab611c, host .env loaded, tools.mcp + integrations.register_enabled with the 7 ENABLED ids): total 60 (native 37, integration 23), identical to 60 (37+23) recorded at MX-r-7 on 05e3eff563; both MX-r-7 tools present; 0 added 0 removed. In-process internal_role.s3_client() on host (SSM 0a7c1772-d901-4b3d-9998-f706f228fe1e): ARN set, client not None, assumed-session credentials (ASIA prefix), head_object json/benchmarks/model_portfolio_timeseries.json (a query_v0 catalog key) HTTP 200 len 763915, query_v0._fetch_capped ok bytes_read=763915, no InternalRoleUnavailable. No principal value printed. | CLOSED 20261001T091938Z |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit=2c0f84966d on wk-NFRA_MCPMSP-5d | d2.AC2 PASS + safe-commit hash | EC2_MANIFEST.json services.opal-gateway deployed_commit=2c0f84966dc452d367ab1e4fc5d4849f08c1625e previous=05e3eff56307409fab574bba620ec22ba9dd0456 committed 33cb168186 on wk-NFRA_MCPMSP-5d; d2.AC2: descends=yes, gateway files shipped 17, outside round 2's set 0, three new modules 3 of 3, RESULT: PASS exit=0 | CLOSED 20261001T091939Z |

## Log

- 20261001T090630Z OPENED by 0.9.0_WK_NFRA_MCPMSP~5 with 2 leg(s)
- 20261001T091938Z LEG host closed: deploy rc=0 (log /c/tmp/ms-d2-deploy.log), base guard equal 05e3eff563 at both reads, uploaded git-ref 2c0f84966dc452d36
- 20261001T091939Z LEG manifest closed: EC2_MANIFEST.json services.opal-gateway deployed_commit=2c0f84966dc452d367ab1e4fc5d4849f08c1625e previous=05e3eff5630740
- 20261001T091939Z CLOSED -- all 2 legs proven
