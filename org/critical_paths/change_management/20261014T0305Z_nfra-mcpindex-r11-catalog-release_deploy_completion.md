# Deploy Completion Record
**Date opened:** 2026-10-14T03:05:48.415911+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-12: release MX-c-9's catalog (tool_index index keys, AUA depth measured, 33 harvest rows), opal_discover answer-time depth and the MC Portal breakdown reader onto the opal-gateway host -- deploy-only commit 027fedfda4 on live b0c75d24f1
**Authored by:** 0.7.0_AE_CloudOps~MI
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 7.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-027fedfda4.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = 027fedfda48714721deeddf41b87e0de6a5c0266, AND the rollback key opal-gateway-b0c75d24f1.tar.gz still 557415 B ETag c9bce856c6bbf1003f40970a8a9d9fac -- read BEFORE this leg closes |  | OPEN |
| L2 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200; running bytes of the 3 shipped files sha-equal to the BUILD INPUT (the cut) with the live tree as a discriminating negative control; three censuses EQUAL (tools 67=67 names equal, .env KEY set 54=54, ENABLED_INTEGRATIONS 7=7); and A1's MC Portal per-tool link counts EQUAL live vs cut on the host |  | OPEN |
| L3 | verify | r12.AC2 on the host -- FWD-20 partition through MC Portal's reader, no row identity in tool_index, FWD-21 discover | bash .../round11/checks/r12.AC2.sh -- RESULT: PASS exit=0 |  | OPEN |
| L4 | verify | r12.AC3 -- measured depths verified by the aws CLI, and the AUA answer's answer-time depth | bash .../round11/checks/r12.AC3.sh -- RESULT: PASS exit=0 |  | OPEN |
| L5 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on box/sitez | deployed_commit=027fedfda48714721deeddf41b87e0de6a5c0266, previous_deployed_commit=b0c75d24f11808d1de4f70fcca5d39216282054a, mcportal_commit 0e02a1f unmoved, AND release_note naming THIS release (the NFRA_MCPORTAL-Z-S49 defect: never leave the prior release's note beside new commit fields) |  | OPEN |

## Log

- 20261014T030548Z OPENED by 0.7.0_AE_CloudOps~MI with 5 leg(s)
