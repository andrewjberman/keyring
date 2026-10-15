# Deploy Completion Record
**Date opened:** 2026-10-15T19:46:37.958694+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-14: the round 17 catalog (44 inferred nl_tags, 24 firm-scoped rows, 7 read_tool rows) and the discover firm-visibility change released onto opal-gateway -- deploy-only commit c4c106aea1 on live 06cfb6db64 (2 files)
**Authored by:** 0.7.0_AE_CloudOps~MI
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-c4c106aea1.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = c4c106aea1cc47d15f81397208226bd9b292c9dc, AND the rollback key opal-gateway-06cfb6db64.tar.gz still 734698 B ETag d8470277354440424e89cc848a88d469 -- read BEFORE this leg closes |  | OPEN |
| L2 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200; running bytes sha-equal to the BUILD INPUT (the cut) with the live tree as a discriminating negative control (expect DIFFER 2 = catalog + discover); censuses: tools 99=99 names equal, .env KEY set 57=57, ENABLED_INTEGRATIONS 7=7, MC Portal per-tool link counts EXACTLY 39 tools / 119 links read on the host by real module import |  | OPEN |
| L3 | verify | r13.AC2 on the deployed bytes | bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC2.sh -- RESULT: PASS exit=0 (expected sum 99 of 99, definitions 99 of 99) |  | OPEN |
| L4 | verify | r13.AC3 and r14.AC4 on the deployed bytes | r13.AC3.sh and round17/checks/r14.AC4.sh -- each RESULT: PASS exit=0 (AC4: host catalog version 0.5 harvest 78 table 216 key_template 216 retired 5 rows 304 nl_tags 304 inferred 44 firm 24, host md5 equals the tree md5, no unserved read_tool) |  | OPEN |
| L5 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on box/sitez | deployed_commit=c4c106aea1cc47d15f81397208226bd9b292c9dc, previous_deployed_commit=06cfb6db6471972c7304cd3d7a5b93e6f521ad72, mcportal 17dcbb28 unmoved, AND a release_note naming MX-r-14 written in the SAME write as the commit fields |  | OPEN |

## Log

- 20261015T194637Z OPENED by 0.7.0_AE_CloudOps~MI with 5 leg(s)
