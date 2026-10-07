# Deploy Completion Record
**Date opened:** 2026-10-07T21:39:41.332718+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-14 PHASE B: opal-gateway release 510c8cfed2 -> rel-nfra-oplgtw-r28b aa75078e1b (OG-lk-1: the audit-lake key of a record that carries no ts gains a time part, app/audit.py; OG-bi-1/2/3/4: the deploy tool deploy-to-ec2.sh itself CHANGES -- a bun cache pre-check runs before the dashboard install and the host's pip --upgrade pip line is removed; 8 files, 1 ships to the host, 7 are the laptop's deploy tool and source-only tests; no tool or route added or removed). THIS IS THE FIRST DEPLOY RUN BY THE CHANGED deploy-to-ec2.sh. Consumers moved: the one opal-gateway.service on host i-07dccb1615503ac99; the S3 artifacts opal-gateway-latest.tar.gz and opal-gateway-aa75078e1b.tar.gz in the gateway artifact bucket; the gateway's audit lake (bucket opal-mcp-audit, prefix audit/dt=<day>/) whose readers (the Glue table mcp_audit, any reader that splits or sorts the raw jsonl object keys) see, for a record with no ts (taxsma_workbook), a key with a time part where it had an empty one; no record body changes; the deploy tool deploy-to-ec2.sh used by every later gateway deploy (pre-check before bun install; no pip self-upgrade); no ECS/Lambda task family, image or tag moved. Via safe-ec2-deploy.sh from /c/tmp/og-rel24. never-widen halves SIGNED on aa75078e1b: COO 9ece15debe, CTO 8614c48050, CVO 6ac6eda0f6. Rollback per key: redeploy 510c8cfed2 from /c/tmp/og-rb22 (restores audit.py md5 384a42e5; lake objects already written keep their keys).
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~28
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref aa75078e1b; base guard 510c8cfed2 == live |  | OPEN |
| bun-fetch-control | verify | bun install cache of the deploying account (R45, CTO half C1): entries touched since deploy start, total bytes and file count before and after, build log download lines | RL14_BUN_CACHE.json: entries_touched_since_start 0, bytes_before == bytes_after, files_before == files_after; any difference = fetch = roll back |  | OPEN |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 51 keys | r28_verify.sh after: md5 97 of 97 = release bytes (1 differs from live), health 200, 66 tools, 51 names with every value sha256 equal, four route arms, floor rl4.AC1 + ht.AC2 |  | OPEN |
| installed-reads | verify | installed code on the host: the audit-lake key builder (fake S3 client), tools, consent, id-shape arms, portal login, real holder, host pip counts | RL14_READ.json + RL14_FLOOR.json from the installed tree with host digests; any rollback trigger rolls back |  | OPEN |
| page-reads | verify | each rivalfunds page: S3 status, size, digest and LastModified immediately BEFORE and AFTER the deploy | r28_pagetime_before.out and r28_pagetime_after.out; a size or digest difference with LastModified unmoved rolls back |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous 510c8cfed2 | committed hash; release_note holds this release's note only |  | OPEN |
| rollback-proven | verify | rollback tree /c/tmp/og-rb22 at 510c8cfed2 equal to the live artifact, command recorded | diff 97 of 97 equal and verify PASS, or rolled back and re-verified |  | OPEN |

## Log

- 20261007T213941Z OPENED by 0.9.0_WK_NFRA_OPLGTW~28 with 7 leg(s)
