# Deploy Completion Record
**Date opened:** 2026-10-14T01:18:49.740935+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-n-4: the C17 round-2 gateway release -- gitstate _refused reads the per-box last-integrate pointer
**Authored by:** 0.7.0_AE_CloudOps~MQ
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-<release sha>.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = the release commit, AND the rollback key opal-gateway-7eff14b2e6.tar.gz still ETag c8b27c104c2f95a6108eece752ccef66 |  | OPEN |
| L2 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200 within 90 s, unit active, MainPID moved off 1080008, the running module md5-equal to the release bytes with a negative control, and the MCP tool-name difference EMPTY against the 67-name BEFORE read |  | OPEN |
| L3 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on rel-nfra-mcportal-c17r2 | deployed_commit = the release commit, previous_deployed_commit = 7eff14b2e620c8c1f688d41de6f37c09addde7b4, release_note written, mcportal_commit left at 0e02a1f |  | OPEN |

## Log

- 20261014T011849Z OPENED by 0.7.0_AE_CloudOps~MQ with 3 leg(s)
- PRE-ACT RECORD (census, both test readings with their ls-tree counts, the proven rollback, the BEFORE tool surface and the condition B-1 before-table): org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/MP-n-4_PRE_ACT_RECORD.md
