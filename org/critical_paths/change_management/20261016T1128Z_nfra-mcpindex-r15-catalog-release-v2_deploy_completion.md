# Deploy Completion Record
**Date opened:** 2026-10-16T11:28:24.095656+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-15 v2 (A3): the re-measured round 18 catalog (depth and freshness claims only; 0 of 280 rows change) released onto opal-gateway -- deploy-only commit 1bc2df0b13 on live 0cb4a87bcb (1 file)
**Authored by:** 0.7.0_AE_CloudOps~MI
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-1bc2df0b13.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = 1bc2df0b1383e424571aaa19c195928f449be31b, AND the rollback key opal-gateway-0cb4a87bcb.tar.gz still 883376 B ETag e004131084719990cbe6de019bb4a9cf -- read BEFORE this leg closes | head-object read BEFORE this leg closed (2026-10-16T11:30:45Z; probes_r15/label_readback_r15_v2.txt): opal-gateway-1bc2df0b13.tar.gz and -latest.tar.gz both 883,446 B ETag b21822283e66f7b141bdda5113d5fb77 git-ref 1bc2df0b1383e424571aaa19c195928f449be31b (404 pre-apply); rollback key opal-gateway-0cb4a87bcb.tar.gz untouched 883,376 B ETag e004131084719990cbe6de019bb4a9cf; base guard read declared base == live ref 0cb4a87bcb at both checkpoints | CLOSED 20261016T113140Z |
| L2 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200; running bytes sha-equal to the BUILD INPUT (the cut) with the live tree B as a discriminating negative control (expect DIFFER 1 = catalog); censuses: tools 127=127 names equal, .env KEY set 64=64, ENABLED_INTEGRATIONS 7=7, MC Portal per-tool link counts EXACTLY 65 tools / 192 links read on the host by the real module | Deploy ssm:1021a229-e7b5-4724-973d-b3525e489017 Success (rc=0, 2026-10-16T11:30Z); host read ssm:1e398c6a-adf1-49ba-83f2-ee7a1774cfbe at 11:31:43Z: /health 200; host bytes 141 of 141 equal to the cut 1bc2df0b13 (DIFFER 0); negative control against the prior live tree B 0cb4a87bcb DIFFER 1 = DATA_CATALOG.yaml (host_vs_cut_r15_v2_POST.txt); censuses (four_censuses_r15_v2_POST.txt): tools 127 = 127 names equal, .env KEY set 64 = 64, ENABLED_INTEGRATIONS 7 = 7, MC Portal link counts 65 tools / 192 links read on the host by the real installed module and equal to the cut per tool | CLOSED 20261016T113253Z |
| L3 | verify | r13.AC2 on the deployed bytes | bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC2.sh -- RESULT: PASS exit=0 (expected sum 127 of 127) | r13.AC2 verbatim on the deployed bytes (ssm Success, /health=200; probes_r15/r13.AC2_r13.AC3_r15.AC4_v2_POST.txt): SERVED TOOLS N=127; PARTITION a=11 b=104 c=12, sum 127 of N=127; definitions located 127 of 127; duplicate entries 0; entries naming an unserved tool 0; index rc=0; discover reads good 3 of 3, rc=0 -- RESULT: PASS exit=0 | CLOSED 20261016T113645Z |
| L4 | verify | r13.AC3 and r15.AC4 on the deployed bytes | r13.AC3.sh (the criterion that failed at B) and round18/checks/r15.AC4.sh -- each RESULT: PASS exit=0 (AC4: host md5 983464f80adc45ac51f1f3eebbdf2001 equals the tree md5, rows 280, inferred 0, bucket 280, vendor 136, firm 136, tool_bucket 127, serves 7) |  | OPEN |
| L5 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on box/sitez | deployed_commit=1bc2df0b1383e424571aaa19c195928f449be31b, previous_deployed_commit=0cb4a87bcb8df4adbb71d095f0818b0f50c562f1, mcportal 090b9cdc85 unmoved, AND a release_note naming MX-r-15 v2 prepended in the SAME write as the commit fields | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on box/sitez, committed 7018ac20dc (safe-commit, LOCAL until box-sync): deployed_commit=1bc2df0b1383e424571aaa19c195928f449be31b, previous_deployed_commit=0cb4a87bcb8df4adbb71d095f0818b0f50c562f1, deployed_at 2026-10-16T11:30:12Z, mcportal_commit 090b9cdc85 unmoved, release_note naming MX-r-15 v2 prepended in the SAME write as the commit fields; exactly 4 fields changed (deployed_by already read this seat), 4 insertions / 4 deletions, 1 of 27 services (probes_r15/write_manifest_v2.py) | CLOSED 20261016T113809Z |

## Log

- 20261016T112824Z OPENED by 0.7.0_AE_CloudOps~MI with 5 leg(s)
- 20261016T113140Z LEG L1 closed: head-object read BEFORE this leg closed (2026-10-16T11:30:45Z; probes_r15/label_readback_r15_v2.txt): opal-gateway-1bc2d
- 20261016T113253Z LEG L2 closed: Deploy ssm:1021a229-e7b5-4724-973d-b3525e489017 Success (rc=0, 2026-10-16T11:30Z); host read ssm:1e398c6a-adf1-49ba-83f2
- 20261016T113645Z LEG L3 closed: r13.AC2 verbatim on the deployed bytes (ssm Success, /health=200; probes_r15/r13.AC2_r13.AC3_r15.AC4_v2_POST.txt): SERVE
- 20261016T113809Z LEG L5 closed: infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on box/sitez, committed 7018ac20dc (safe-commit, LOCAL until box-s
