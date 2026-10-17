# Deploy Completion Record
**Date opened:** 2026-10-13T20:58:21.719306+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261013T214407Z
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-z-5: the gateway release -- FWD-20 breakdown route + SPA deep links + bundle 0e02a1f
**Authored by:** 0.7.0_AE_CloudOps~MQ
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | ec2-baked-asset | mcportal dashboard bundle 0e02a1f built offline into the artifact | dist/index.html present in the artifact and bun cache pre-check 77 of 77 rc=0, no package fetched | mcportal 0e02a1f built offline inside the deploy; bun cache pre-check 77 of 77 rc=0 against 0e02a1f's own lockfile (byte-identical to bc37107's), no package fetched; dist/index.html produced; the served bundle on the host now carries dashboard/routes.json (present; the bc37107 bundle had none, the negative control). | CLOSED 20261013T212353Z |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-<release sha>.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = the release commit, AND the rollback key opal-gateway-185dc04888.tar.gz still ETag b486e614fc122cf854f0d063bd198e4e | head-object: opal-gateway-64b3e54658.tar.gz EXISTS 551,109 B ETag 527cab0d7d0695c3c6f3c3df902c11df git-ref 64b3e54658060859b81d6bcd48dc7000615f865d mod 2026-10-13T21:07:30Z (so MX-r-9's Z-S92 missing-versioned-key defect did not recur); opal-gateway-latest.tar.gz same ETag and git-ref, mod 21:07:32Z; ROLLBACK key opal-gateway-185dc04888.tar.gz UNTOUCHED at 543,554 B ETag b486e614fc122cf854f0d063bd198e4e mod 2026-10-12T12:51:35Z. | CLOSED 20261013T212354Z |
| L3 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200 within 90 s, unit active, MainPID moved, running app files md5-equal to the release bytes with a negative control | SSM 7a0af4a7-050f-4e97-b6c7-36d0c1e9ad6b Success: /health 200 {ok:true}; unit active; MainPID 994775 -> 1071120; ActiveEnterTimestamp 2026-10-13T21:07:51Z; app/admin_gateway_breakdown.py and dashboard/routes.json present on the box. RUNNING BYTES md5-equal to the BUILD INPUT (the release tree), not matched by filename: admin_api.py b1fea67f1273228bcb86f30ab7ced34b, server.py 3c4c2802a51e2256fc5670fca4a29254, admin_gateway_breakdown.py 100177e07b4ad14737c65a17b65f5b2a, all three equal. NEGATIVE CONTROL at the base: 012e661390c27ab902d6d19d6b061af3 and b37db8a567793f6b0c2b442d9b9106c6, module ABSENT -- so the comparison discriminates. | CLOSED 20261013T212354Z |
| L4 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on rel-nfra-mcportal-gw | deployed_commit = the release commit, previous_deployed_commit = 185dc048881da2030efa11f4d0bfb8704b500c66, mcportal_commit = 0e02a1f, release_note written | EC2_MANIFEST.json services.opal-gateway on rel-nfra-mcportal-gw: deployed_commit=64b3e54658060859b81d6bcd48dc7000615f865d, previous_deployed_commit=185dc048881da2030efa11f4d0bfb8704b500c66 (CORRECTED from the stale 2c0f84966d the wrapper wrote from this release tree's own chain vintage -- the recurring MP-x-4/MP-r-2/MP-n-1 defect, COO half condition 3), mcportal_commit=0e02a1f, release_note rewritten for THIS release. 27 services in the file, exactly 1 (opal-gateway) differs; 0 non-ASCII; the file parses. | CLOSED 20261013T212354Z |
| L5 | verify | MCP tool surface + AC1 + AC2 | tool names before/after both recorded with an EMPTY difference; z5.AC1.sh and z5.AC2.sh each RESULT: PASS exit=0 | MCP tool surface read on THIS base both sides through tools.mcp._tool_manager.list_tools(): BEFORE 43 names (SSM 50716cfe-562c-4c7f-8b76-fb17d6624c59), AFTER 43 names (SSM 7a0af4a7-050f-4e97-b6c7-36d0c1e9ad6b), added=[] removed=[] DIFFERENCE EMPTY, with a negative control confirming the comparison detects a dropped name. NOTE: that reader sees the NATIVE registry; the SERVED surface is 67 tools, which is why row Z-S48 exists. z5.AC2.sh under Amendment 3 @ac44bd46e0 (SSM 7a6c8ea2-e00f-4317-8bf5-9d69e6902070 Success): /health=200; no-identity breakdown=401 /control-plane=401 /open-calls=401 /gateway=401; unlisted=404; breakdown_s=1.2 channels=8 tools=67 dup_tools=0 channels_held=8 grant_store=read -- RESULT: PASS exit=0. z5.AC1.sh is run immediately after this close commit, because its first two limbs read the sentinel this close removes. | CLOSED 20261013T214407Z |
| L1 | ec2-baked-asset | mcportal dashboard bundle 0e02a1f built offline into the artifact | dist/index.html present in the artifact and bun cache pre-check 77 of 77 rc=0, no package fetched |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ -- opal-gateway-<release sha>.tar.gz + -latest.tar.gz | head-object on BOTH new keys showing git-ref = the release commit, AND the rollback key opal-gateway-185dc04888.tar.gz still ETag b486e614fc122cf854f0d063bd198e4e |  | OPEN |
| L3 | activation | SSM pull + systemctl restart opal-gateway on i-07dccb1615503ac99 | /health 200 within 90 s, unit active, MainPID moved, running app files md5-equal to the release bytes with a negative control |  | OPEN |
| L4 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on rel-nfra-mcportal-gw | deployed_commit = the release commit, previous_deployed_commit = 185dc048881da2030efa11f4d0bfb8704b500c66, mcportal_commit = 0e02a1f, release_note written |  | OPEN |
| L5 | verify | MCP tool surface + AC1 + AC2 | tool names before/after both recorded with an EMPTY difference; z5.AC1.sh and z5.AC2.sh each RESULT: PASS exit=0 |  | OPEN |

## Log

- 20261013T205821Z OPENED by 0.7.0_AE_CloudOps~MQ with 5 leg(s)
- 20261013T212353Z LEG L1 closed: mcportal 0e02a1f built offline inside the deploy; bun cache pre-check 77 of 77 rc=0 against 0e02a1f's own lockfile (byte
- 20261013T212354Z LEG L2 closed: head-object: opal-gateway-64b3e54658.tar.gz EXISTS 551,109 B ETag 527cab0d7d0695c3c6f3c3df902c11df git-ref 64b3e54658060
- 20261013T212354Z LEG L3 closed: SSM 7a0af4a7-050f-4e97-b6c7-36d0c1e9ad6b Success: /health 200 {ok:true}; unit active; MainPID 994775 -> 1071120; ActiveE
- 20261013T212354Z LEG L4 closed: EC2_MANIFEST.json services.opal-gateway on rel-nfra-mcportal-gw: deployed_commit=64b3e54658060859b81d6bcd48dc7000615f865
- 20261013T214407Z LEG L5 closed: MCP tool surface read on THIS base both sides through tools.mcp._tool_manager.list_tools(): BEFORE 43 names (SSM 50716cf
- 20261013T214407Z CLOSED -- all 5 legs proven
- PRE-ACT RECORD (census, the three test readings with the 7 named ids, the proven rollback, the before-state and both signed halves): org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/MP-z-5_PRE_ACT_RECORD.md
