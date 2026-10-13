# Deploy Completion Record
**Date opened:** 2026-10-13T20:58:21.719306+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-z-5: the gateway release -- FWD-20 breakdown route + SPA deep links + bundle 0e02a1f
**Authored by:** 0.7.0_AE_CloudOps~MQ
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | ec2-baked-asset | mcportal dashboard bundle 0e02a1f built offline into the artifact | dist/index.html present in the artifact and bun cache pre-check 77 of 77 rc=0, no package fetched |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-<release sha>.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = the release commit, AND the rollback key opal-gateway-185dc04888.tar.gz still ETag b486e614fc122cf854f0d063bd198e4e |  | OPEN |
| L3 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200 within 90 s, unit active, MainPID moved, running app files md5-equal to the release bytes with a negative control |  | OPEN |
| L4 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on rel-nfra-mcportal-gw | deployed_commit = the release commit, previous_deployed_commit = 185dc048881da2030efa11f4d0bfb8704b500c66, mcportal_commit = 0e02a1f, release_note written |  | OPEN |
| L5 | verify | MCP tool surface + AC1 + AC2 | tool names before/after both recorded with an EMPTY difference; z5.AC1.sh and z5.AC2.sh each RESULT: PASS exit=0 |  | OPEN |

## Log

- 20261013T205821Z OPENED by 0.7.0_AE_CloudOps~MQ with 5 leg(s)
- PRE-ACT RECORD (census, the three test readings with the 7 named ids, the proven rollback, the before-state and both signed halves): org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/MP-z-5_PRE_ACT_RECORD.md
