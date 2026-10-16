# Deploy Completion Record
**Date opened:** 2026-10-16T10:37:01.790880+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-15: the round 18 catalog (C-GROUP bucket on every row and tool, vendor and firm on 136 rows, 0 inferred tags, the 12 Schwab dim rows, tool index N=127) released onto opal-gateway -- deploy-only commit 0cb4a87bcb on live 3d5c9c8bf1 (2 files; the host's changed set is the catalog alone)
**Authored by:** 0.7.0_AE_CloudOps~MI
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-0cb4a87bcb.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = 0cb4a87bcb8df4adbb71d095f0818b0f50c562f1, AND the rollback key opal-gateway-3d5c9c8bf1.tar.gz still 893303 B ETag d43206bfdad42ae29300cf94eed1423a -- read BEFORE this leg closes |  | OPEN |
| L2 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200; running bytes sha-equal to the BUILD INPUT (the cut) with the live tree as a discriminating negative control (expect DIFFER 2 = catalog + scopes.json); censuses: tools 127=127 names equal, .env KEY set 64=64, ENABLED_INTEGRATIONS 7=7, MC Portal per-tool link counts EXACTLY 65 tools / 192 links read on the host by the real module |  | OPEN |
| L3 | verify | r13.AC2 on the deployed bytes | bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC2.sh -- RESULT: PASS exit=0 (expected sum 127 of 127) |  | OPEN |
| L4 | verify | r13.AC3 and r15.AC4 on the deployed bytes | r13.AC3.sh and round18/checks/r15.AC4.sh -- each RESULT: PASS exit=0 (AC4: HOST CATALOG equals TREE CATALOG, rows 280 nl_tags 280 inferred 0 bucket 280 vendor 136 firm 136 tool_bucket 127 serves 7, host md5 equals tree md5 9519ebce3a1b92cee07a5507d1912dd3, no unserved read_tool) |  | OPEN |
| L5 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on box/sitez | deployed_commit=0cb4a87bcb8df4adbb71d095f0818b0f50c562f1, previous_deployed_commit=3d5c9c8bf1dea0854c9b59d58b83fdf9dcb480e4, mcportal 090b9cdc85 unmoved, AND a release_note naming MX-r-15 written in the SAME write as the commit fields |  | OPEN |

## Log

- 20261016T103701Z OPENED by 0.7.0_AE_CloudOps~MI with 5 leg(s)
