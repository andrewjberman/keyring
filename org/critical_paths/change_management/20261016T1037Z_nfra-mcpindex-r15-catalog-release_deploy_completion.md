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
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-0cb4a87bcb.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = 0cb4a87bcb8df4adbb71d095f0818b0f50c562f1, AND the rollback key opal-gateway-3d5c9c8bf1.tar.gz still 893303 B ETag d43206bfdad42ae29300cf94eed1423a -- read BEFORE this leg closes | head-object read BEFORE this leg closed (2026-10-16T10:40:01Z; probes_r15/label_readback_r15.txt): opal-gateway-0cb4a87bcb.tar.gz and -latest.tar.gz both 883,376 B ETag e004131084719990cbe6de019bb4a9cf git-ref 0cb4a87bcb8df4adbb71d095f0818b0f50c562f1 (404 pre-apply); rollback key opal-gateway-3d5c9c8bf1.tar.gz untouched 893,303 B ETag d43206bfdad42ae29300cf94eed1423a git-ref 3d5c9c8bf1; base guard read declared base == live ref 3d5c9c8bf1 immediately before upload | CLOSED 20261016T104043Z |
| L2 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200; running bytes sha-equal to the BUILD INPUT (the cut) with the live tree as a discriminating negative control (expect DIFFER 2 = catalog + scopes.json); censuses: tools 127=127 names equal, .env KEY set 64=64, ENABLED_INTEGRATIONS 7=7, MC Portal per-tool link counts EXACTLY 65 tools / 192 links read on the host by the real module | Deploy ssm:af86ef3c-a8cd-4371-a977-88ab8e822388 Success (rc=0, 2026-10-16T10:38Z); host read ssm:91bc187a-a21b-4ec1-b769-481eb5c24634 at 10:40:47Z: /health 200; host bytes 141 of 141 equal to the cut 0cb4a87bcb (DIFFER 0); negative control against the live tree 3d5c9c8bf1 DIFFER 2 = DATA_CATALOG.yaml + scopes.json (host_vs_cut_r15_POST.txt); censuses (four_censuses_r15_POST.txt): tools 127 = 127 names equal, .env KEY set 64 = 64, ENABLED_INTEGRATIONS 7 = 7, MC Portal link counts 65 tools / 192 links read on the host by the real installed module and equal to the cut per tool | CLOSED 20261016T104310Z |
| L3 | verify | r13.AC2 on the deployed bytes | bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC2.sh -- RESULT: PASS exit=0 (expected sum 127 of 127) | r13.AC2 verbatim on the deployed bytes (ssm 20c334f7-5b12-42db-97d8-3ec4d8fe8e03 Success, /health=200; probes_r15/r13.AC2_r13.AC3_r15.AC4_POST.txt): SERVED TOOLS N=127; PARTITION a=11 (valid 11) b=104 (valid 104) c=12 (valid 12), sum 127 of N=127; definitions located 127 of 127; duplicate entries 0; entries naming an unserved tool 0; index rc=0; discover reads good 3 of 3, rc=0 -- RESULT: PASS exit=0 | CLOSED 20261016T105256Z |
| L4 | verify | r13.AC3 and r15.AC4 on the deployed bytes | r13.AC3.sh and round18/checks/r15.AC4.sh -- each RESULT: PASS exit=0 (AC4: HOST CATALOG equals TREE CATALOG, rows 280 nl_tags 280 inferred 0 bucket 280 vendor 136 firm 136 tool_bucket 127 serves 7, host md5 equals tree md5 9519ebce3a1b92cee07a5507d1912dd3, no unserved read_tool) |  | OPEN |
| L5 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on box/sitez | deployed_commit=0cb4a87bcb8df4adbb71d095f0818b0f50c562f1, previous_deployed_commit=3d5c9c8bf1dea0854c9b59d58b83fdf9dcb480e4, mcportal 090b9cdc85 unmoved, AND a release_note naming MX-r-15 written in the SAME write as the commit fields | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on box/sitez, committed 775351feb0 (safe-commit, LOCAL until box-sync): deployed_commit=0cb4a87bcb8df4adbb71d095f0818b0f50c562f1, previous_deployed_commit=3d5c9c8bf1dea0854c9b59d58b83fdf9dcb480e4, deployed_at 2026-10-16T10:38:53Z, mcportal_commit 090b9cdc85 unmoved, release_note naming MX-r-15 written in the SAME write as the commit fields; exactly 5 fields changed, 5 insertions / 5 deletions, 1 of 27 services (probes_r15/write_manifest.py) | CLOSED 20261016T105513Z |

## Log

- 20261016T103701Z OPENED by 0.7.0_AE_CloudOps~MI with 5 leg(s)
- 20261016T104043Z LEG L1 closed: head-object read BEFORE this leg closed (2026-10-16T10:40:01Z; probes_r15/label_readback_r15.txt): opal-gateway-0cb4a87b
- 20261016T104310Z LEG L2 closed: Deploy ssm:af86ef3c-a8cd-4371-a977-88ab8e822388 Success (rc=0, 2026-10-16T10:38Z); host read ssm:91bc187a-a21b-4ec1-b769
- 20261016T105256Z LEG L3 closed: r13.AC2 verbatim on the deployed bytes (ssm 20c334f7-5b12-42db-97d8-3ec4d8fe8e03 Success, /health=200; probes_r15/r13.AC
- 20261016T105513Z LEG L5 closed: infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on box/sitez, committed 775351feb0 (safe-commit, LOCAL until box-s
