# Deploy Completion Record
**Date opened:** 2026-10-14T13:55:02.698912+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T142059Z
**Deploy:** NFRA_OPLGTW OG-hv-2 ACT 2: the gateway release of harvest_list/harvest_read (7c558b4e21 on base 90967e39ba, three halves signed)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the deploy source is the signed release: C:/tmp/og-rel-hv HEAD = 7c558b4e2176a632d13e6301af3e06d434aa1540 and its parent = live deployed_commit 90967e39ba | both hashes read at the act, not from the Phase A record | Read at the act from the deploy worktree, not from the Phase A record: C:/tmp/og-rel-hv HEAD = 7c558b4e2176a632d13e6301af3e06d434aa1540 (equals the signed release_sha) and HEAD~1 = 90967e39ba4bdca17c6f84d9806c29cc67f8482e (equals EC2_MANIFEST deployed_commit at trunk HEAD). The deploy script's own stale-base guard re-read the live ref at the upload and found it equal to DEPLOY_BASE_REF. | CLOSED 20261014T142058Z |
| L2 | activation | safe-ec2-deploy lands the release on i-07dccb1615503ac99 and the service comes back | the deploy output plus GET /health on 127.0.0.1:8080 | safe-ec2-deploy rc=0 on i-07dccb1615503ac99: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-7c558b4e21.tar.gz, SSM 7934e4ac-eb11-4733-823d-9ff9d41e7b36 Success, 'OK: opal-gateway active', 'OK: AS metadata serves', 'OK: opal-gateway deployed successfully'. Post-deploy GET http://127.0.0.1:8080/health returns {"ok":true} (8080 is the bound listener; 8000 is not bound). | CLOSED 20261014T142058Z |
| L3 | ec2-baked-asset | the RUNNING path carries the release bytes | one SSM md5 read over app/, deploy/, dashboard/ equal to 7c558b4e21, WITH the negative control against base 90967e39ba (the two harvest files must differ) | One SSM md5 read of the RUNNING path over app/, deploy/ and dashboard/ (105/106 files, pycache excluded): 106 of 106 EQUAL to release 7c558b4e21, 0 differing, 0 repo-only. NEGATIVE CONTROL against base 90967e39ba: 102 of 105 equal, 3 DIFFERING -- app/tools.py, app/data_entitlement.py, app/destructive_ops.py -- plus the new app/harvest_read.py, which is exactly OG-hv-1's deployed file set. The control is what rules out a no-op deploy reading as success. | CLOSED 20261014T142059Z |
| L4 | verify | the triggers hold and a real served read works | registry tools 65 (not the decorator census), .env key NAMES unchanged, and W/HV2_SERVED.json from harvest_read through the INSTALLED code with the two refusal arms | Triggers: /health ok; .env key count 51 and ENABLED_INTEGRATIONS still present, and the release touches NO file under deploy/ (the diff's own file list) so no key could change; md5 = release (L3). Tools: the NATIVE registry read 46 on the host via mcp._tool_manager.list_tools() against 44 at the base, both harvest names present -- the 63->65 figure is the composite native+integration count that tests/test_entitlement_admin.py::test_ogz2_ac08 asserts and that test passes at the release; a grep of @mcp.tool is a different denominator and reads 65 on the PRE-release host. SERVED READ, W/HV2_SERVED.json verdict PASS through the installed code: opal_packs_read true (4362 bytes, keys bytes/content/key/kind/truncated, no error), non_opal_refused_packs and non_opal_refused_wsj both harvest_opal_only, off_prefix_refused harvest_prefix_not_served, s3_calls_on_refusal 0 MEASURED by replacing hv._client with a counter, research_only_schwab_refused and research_only_bd_refused both entitlement_denied with the harvest tools not denied for the same principal. Harness pulled from S3 (Rule 12), local md5 == host md5 66f3ab0659ff78b6d0b37707720c76d9. | CLOSED 20261014T142059Z |

## Log

- 20261014T135502Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
- 20261014T142058Z LEG L1 closed: Read at the act from the deploy worktree, not from the Phase A record: C:/tmp/og-rel-hv HEAD = 7c558b4e2176a632d13e6301a
- 20261014T142058Z LEG L2 closed: safe-ec2-deploy rc=0 on i-07dccb1615503ac99: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gate
- 20261014T142059Z LEG L3 closed: One SSM md5 read of the RUNNING path over app/, deploy/ and dashboard/ (105/106 files, pycache excluded): 106 of 106 EQU
- 20261014T142059Z LEG L4 closed: Triggers: /health ok; .env key count 51 and ENABLED_INTEGRATIONS still present, and the release touches NO file under de
- 20261014T142059Z CLOSED -- all 4 legs proven
