# Deploy Completion Record
**Date opened:** 2026-10-16T12:17:21.624245+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-15 v3 (A4): the catalog re-measured after the daily publish (depth and freshness claims only; 0 of 280 rows change) released onto opal-gateway -- deploy-only commit 38fe44d5cb on live 1bc2df0b13 (1 file)
**Authored by:** 0.7.0_AE_CloudOps~MI
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-38fe44d5cb.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = 38fe44d5cb8d37b6007fb7e5fa47a25316e01054, AND the rollback key opal-gateway-1bc2df0b13.tar.gz still 883446 B ETag b21822283e66f7b141bdda5113d5fb77 -- read BEFORE this leg closes |  | OPEN |
| L2 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200; running bytes sha-equal to the BUILD INPUT (the cut) with the prior live tree v2 as a discriminating negative control (expect DIFFER 1 = catalog); censuses: tools 127=127 names equal, .env KEY set 64=64, ENABLED_INTEGRATIONS 7=7, MC Portal per-tool link counts EXACTLY 65 tools / 192 links read on the host by the real module |  | OPEN |
| L3 | verify | r13.AC2 on the deployed bytes | bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC2.sh -- RESULT: PASS exit=0 (expected sum 127 of 127) |  | OPEN |
| L4 | verify | r13.AC3 and r15.AC4 on the deployed bytes | r13.AC3.sh (the criterion that failed at B and v2) and round18/checks/r15.AC4.sh -- each RESULT: PASS exit=0 (AC4: host md5 b72408cad06f2fbf8fb851a4be5485d9 equals the tree md5) |  | OPEN |
| L5 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on box/sitez | deployed_commit=38fe44d5cb8d37b6007fb7e5fa47a25316e01054, previous_deployed_commit=1bc2df0b1383e424571aaa19c195928f449be31b, mcportal 090b9cdc85 unmoved, AND a release_note naming MX-r-15 v3 prepended in the SAME write as the commit fields |  | OPEN |

## Log

- 20261016T121721Z OPENED by 0.7.0_AE_CloudOps~MI with 5 leg(s)
