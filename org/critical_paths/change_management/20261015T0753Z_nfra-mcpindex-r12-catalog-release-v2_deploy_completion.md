# Deploy Completion Record
**Date opened:** 2026-10-15T07:53:01.299317+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-13 (re-cut): the round 13/14/16 catalog (v0.5, 78 harvest rows, 216 table rows) and the discover fix released onto opal-gateway -- deploy-only commit 1b18b94979 on live ee23dd004c (2 files); the first attempt d020bee315 was rolled back
**Authored by:** 0.7.0_AE_CloudOps~MI
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-1b18b94979.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = 1b18b94979d2ba0e4c6eba8ee4a0a5a0cae52bc0, AND the rollback key opal-gateway-ee23dd004c.tar.gz still 629787 B ETag 3cd90347e472d1b7c0eaa31ad43c9242 -- read BEFORE this leg closes |  | OPEN |
| L2 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200; running bytes sha-equal to the BUILD INPUT (the cut) with the live tree as a discriminating negative control (expect DIFFER 2 = catalog + discover); censuses: tools 93=93 names equal, .env KEY set 57=57, ENABLED_INTEGRATIONS 7=7, MC Portal per-tool link counts EXACTLY 33 tools / 112 links read on the host by real module import |  | OPEN |
| L3 | verify | r13.AC2 on the deployed bytes | bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC2.sh -- RESULT: PASS exit=0 (expected sum 93 of 93, definitions 93 of 93) |  | OPEN |
| L4 | verify | r13.AC3 and r13.AC4 on the deployed bytes | r13.AC3.sh and r13.AC4.sh -- each RESULT: PASS exit=0 (AC4: host catalog version 0.5, harvest 78, table 216, key_template 216, retired 5, host md5 equals the tree md5, no unserved read_tool) |  | OPEN |
| L5 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on box/sitez | deployed_commit=1b18b94979d2ba0e4c6eba8ee4a0a5a0cae52bc0, previous_deployed_commit=ee23dd004c985c46d479908db46d2ad9b4f3b1c8, mcportal 17dcbb28 unmoved, AND a release_note naming MX-r-13 written in the SAME write as the commit fields |  | OPEN |

## Log

- 20261015T075301Z OPENED by 0.7.0_AE_CloudOps~MI with 5 leg(s)
