# Deploy Completion Record
**Date opened:** 2026-10-14T04:09:07.219525+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-12 v2: the catalog-only release carrying the six legacy-addressed research rows (harvest 33 -> 39, research 7 of 7) -- deploy-only commit 43088464f5 on live 027fedfda4
**Authored by:** 0.7.0_AE_CloudOps~MI
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-43088464f5.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = 43088464f51c81e9fe3528b080c6ca8ce5fa90fe, AND the rollback key opal-gateway-027fedfda4.tar.gz still 561198 B ETag 93ebfca9c49030f0395078e3eca7933a -- read BEFORE this leg closes |  | OPEN |
| L2 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200; running bytes sha-equal to the BUILD INPUT (the v2 cut) with the v1 tree as a discriminating negative control (expect DIFFER 1 = the catalog); and ALL FOUR VOID-CONDITION CENSUSES equal -- tools 67=67 names equal, .env KEY set 54=54, ENABLED_INTEGRATIONS 7=7, and MC Portal per-tool link counts 11 tools / 14 links read on the host by real module import |  | OPEN |
| L3 | verify | r12.AC2 re-run on v2 -- FWD-20 partition through MC Portal's reader, no row identity, FWD-21 discover | bash .../round11/checks/r12.AC2.sh -- RESULT: PASS exit=0 |  | OPEN |
| L4 | verify | r12.AC3 re-run on v2 -- measured depths verified by the aws CLI, and the AUA answer's answer-time depth | bash .../round11/checks/r12.AC3.sh -- RESULT: PASS exit=0 |  | OPEN |
| L5 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on box/sitez | deployed_commit=43088464f51c81e9fe3528b080c6ca8ce5fa90fe, previous_deployed_commit=027fedfda48714721deeddf41b87e0de6a5c0266, mcportal 0e02a1f unmoved, AND a release_note naming v2 written in the SAME write as the commit fields (row NFRA_MCPORTAL-Z-S49) |  | OPEN |

## Log

- 20261014T040907Z OPENED by 0.7.0_AE_CloudOps~MI with 5 leg(s)
