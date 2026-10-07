# Deploy Completion Record
**Date opened:** 2026-10-07T16:47:29.329624+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-13 PHASE B: opal-gateway release feddb37244 -> rel-nfra-oplgtw-r27 510c8cfed2 (OG-au-2: the audit record of the four rivalfunds routes GAINS args day, route, fund and bytes; OG-sd-1: opal_data_refresh_status returns the served manifest's generated_at in displayed_date where it returned null; 3 shipped files, 2 source-only; no tool or route added or removed). Consumers moved: the one opal-gateway.service on host i-07dccb1615503ac99; the S3 artifacts opal-gateway-latest.tar.gz and opal-gateway-510c8cfed2.tar.gz in the gateway artifact bucket; the gateway's audit lake (bucket opal-mcp-audit, prefix audit/dt=<day>/) whose readers (the Glue table mcp_audit and any reader of the raw jsonl objects) see four rivalfunds record fields they did not carry before; the CALLERS of the opal_data_refresh_status tool (the scoped concierge through the MCP surface) whose answer's displayed_date changes from null to the manifest's generated_at; no ECS/Lambda task family, image or tag moved. Via safe-ec2-deploy.sh from /c/tmp/og-rel22. never-widen halves SIGNED on 510c8cfed2: COO bda7fb88dc, CTO 04fe936b66, CVO 0dec403dce. Rollback per key: redeploy feddb372443 from /c/tmp/og-rb21.
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~28
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard feddb37244 == live |  | OPEN |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 51 keys | r27_verify.sh after: md5 97 of 97 = release bytes (3 differ from live), health 200, 66 tools, 51 names with every value sha256 equal, four route arms, floor rl4.AC1 + ht.AC2 |  | OPEN |
| installed-reads | verify | installed code on the host: the wrapper exercise, displayed_date, rivalfunds audit args and bytes, id-shape arms, portal login, real holder, audit lake record | RL13_READ.json + RL13_FLOOR.json from the installed tree with host digests; any rollback trigger rolls back |  | OPEN |
| page-reads | verify | each rivalfunds page: served status, size, digest and S3 LastModified immediately BEFORE and AFTER the deploy | r27_pagetime_before.out and r27_pagetime_after.out; a size or digest difference with LastModified unmoved rolls back |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous feddb37244 | committed hash; release_note holds this release's note only, the chain moved to this entry |  | OPEN |
| rollback-proven | verify | rollback tree /c/tmp/og-rb21 at feddb37244 equal to the live artifact, command recorded | diff 97 of 97 equal and verify PASS, or rolled back and re-verified |  | OPEN |

## Log

- 20261007T164729Z OPENED by 0.9.0_WK_NFRA_OPLGTW~28 with 6 leg(s)
