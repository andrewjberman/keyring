# Deploy Completion Record
**Date opened:** 2026-10-14T01:18:49.740935+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T013033Z
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-n-4: the C17 round-2 gateway release -- gitstate _refused reads the per-box last-integrate pointer
**Authored by:** 0.7.0_AE_CloudOps~MQ
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-<release sha>.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = the release commit, AND the rollback key opal-gateway-7eff14b2e6.tar.gz still ETag c8b27c104c2f95a6108eece752ccef66 | head-object: opal-gateway-b0c75d24f1.tar.gz EXISTS 557,415 B ETag c9bce856c6bbf1003f40970a8a9d9fac git-ref b0c75d24f11808d1de4f70fcca5d39216282054a mod 2026-10-14T01:20:57Z, so the VERSIONED key was written (MX-r-9's Z-S92 class did not recur); -latest same ETag and git-ref at 01:20:59Z; ROLLBACK key opal-gateway-7eff14b2e6.tar.gz UNTOUCHED at 557,605 B ETag c8b27c104c2f95a6108eece752ccef66, mod 2026-10-13T23:49:56Z, pre-act. Bundle built offline, bun cache 77 of 77 rc=0, mcportal_commit left at 0e02a1f as the order requires. | CLOSED 20261014T012919Z |
| L2 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200 within 90 s, unit active, MainPID moved off 1080008, the running module md5-equal to the release bytes with a negative control, and the MCP tool-name difference EMPTY against the 67-name BEFORE read | SSM a9298281-c3eb-4c48-8057-436e5a481145 Success: /health 200 {ok:true}; unit active; MainPID 1080008 -> 1084258; ActiveEnterTimestamp 2026-10-14T01:21:19Z. RUNNING BYTES md5-equal to the BUILD INPUT, not matched by filename: /opt/opal-gateway/app/admin_fabric_gitstate.py = a5ac99dc2e4868b207a2d0833fe84a30, equal to the release tree's module; NEGATIVE CONTROL at the base = d946f7fee327ef78cda1c7ce0c50f227, so the comparison discriminates. MCP TOOL SURFACE 67 -> 67, md5 of the sorted name list dbc48e6991b924a380b886da0714ac22 BOTH sides, added=[] removed=[], difference EMPTY -- read through app.server so it is the SERVED registry, not the 43-name native one (row Z-S48). | CLOSED 20261014T012919Z |
| L3 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on rel-nfra-mcportal-c17r2 | deployed_commit = the release commit, previous_deployed_commit = 7eff14b2e620c8c1f688d41de6f37c09addde7b4, release_note written, mcportal_commit left at 0e02a1f | EC2_MANIFEST.json services.opal-gateway on rel-nfra-mcportal-c17r2 (wrapper commit 52da8c3119, then corrected): deployed_commit=b0c75d24f11808d1de4f70fcca5d39216282054a, previous_deployed_commit=7eff14b2e620c8c1f688d41de6f37c09addde7b4 (the base this release was cut on, re-read pre-act), mcportal_commit left at 0e02a1f, release_note written for THIS release. The wrapper again wrote previous from the release tree's stale chain vintage; corrected per the COO half, as on MP-x-4, MP-r-2, MP-n-1 and MP-z-5. | CLOSED 20261014T012919Z |
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-<release sha>.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = the release commit, AND the rollback key opal-gateway-7eff14b2e6.tar.gz still ETag c8b27c104c2f95a6108eece752ccef66 |  | OPEN |
| L2 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200 within 90 s, unit active, MainPID moved off 1080008, the running module md5-equal to the release bytes with a negative control, and the MCP tool-name difference EMPTY against the 67-name BEFORE read |  | OPEN |
| L3 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on rel-nfra-mcportal-c17r2 | deployed_commit = the release commit, previous_deployed_commit = 7eff14b2e620c8c1f688d41de6f37c09addde7b4, release_note written, mcportal_commit left at 0e02a1f |  | OPEN |

## Log

- 20261014T011849Z OPENED by 0.7.0_AE_CloudOps~MQ with 3 leg(s)
- 20261014T012919Z LEG L1 closed: head-object: opal-gateway-b0c75d24f1.tar.gz EXISTS 557,415 B ETag c9bce856c6bbf1003f40970a8a9d9fac git-ref b0c75d24f1180
- 20261014T012919Z LEG L2 closed: SSM a9298281-c3eb-4c48-8057-436e5a481145 Success: /health 200 {ok:true}; unit active; MainPID 1080008 -> 1084258; Active
- 20261014T012919Z LEG L3 closed: EC2_MANIFEST.json services.opal-gateway on rel-nfra-mcportal-c17r2 (wrapper commit 52da8c3119, then corrected): deployed
- 20261014T013033Z CLOSED -- all 3 legs proven
- PRE-ACT RECORD (census, both test readings with their ls-tree counts, the proven rollback, the BEFORE tool surface and the condition B-1 before-table): org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/MP-n-4_PRE_ACT_RECORD.md
