# Deploy Completion Record
**Date opened:** 2026-10-13T22:34:48.710360+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-11 PHASE B: release MX-c-8's DATA_CATALOG.yaml tool_index + harvest_datasets and opal_discover onto the opal-gateway host -- deploy-only commit ad2acc0a93 on live 64b3e54658
**Authored by:** 0.7.0_AE_CloudOps~MI
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-ad2acc0a93.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = ad2acc0a9305456e5bac4d7fd2cc5cd42642b203, AND the rollback key opal-gateway-64b3e54658.tar.gz still 551109 B ETag 527cab0d7d0695c3c6f3c3df902c11df -- read BEFORE this leg closes |  | OPEN |
| L2 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200; running bytes of the 2 shipped files md5/sha-equal to the BUILD INPUT (the cut) with a negative control at the base; three censuses EQUAL: tools 67=67 names equal, .env KEY set 54=54, ENABLED_INTEGRATIONS 7=7 |  | OPEN |
| L3 | verify | r11.AC2 on the host -- FWD-20 partition + FWD-21 discover reads | bash .../round10/checks/r11.AC2.sh -- RESULT: PASS exit=0 |  | OPEN |
| L4 | verify | r11.AC3 -- the (a) tool depth and freshness second-instrument read against the DEPLOYED catalog bytes | bash .../round10/checks/r11.AC3.sh -- RESULT: PASS exit=0 |  | OPEN |
| L5 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on box/sitez | deployed_commit=ad2acc0a9305456e5bac4d7fd2cc5cd42642b203 and previous_deployed_commit=64b3e54658060859b81d6bcd48dc7000615f865d (the CTO half binds this; NEVER the stale 185dc04888, and NEVER the deploy tree's own 2c0f84966d/daa56d81ac vintage the wrapper writes), mcportal_commit 0e02a1f unmoved |  | OPEN |

## Log

- 20261013T223448Z OPENED by 0.7.0_AE_CloudOps~MI with 5 leg(s)
