# Deploy Completion Record
**Date opened:** 2026-09-29T09:31:55.136937+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / the trigger Lambda's own Lever A cookie-freshness gate: cot-bd-session-trigger SKIPS the OIDC-login mint while the session cookie is POSITIVE-live (age <= 7d). Measured in its 2026-09-29T11:30:15Z log: 'Lever A: cot cookie POSITIVE-live (probe positive (captured_at=2026-09-27T18:42:27.162Z, age 1.7d <= 7d)) -> SKIP OIDC-login mint, direct bronze-run'. So the 11:30Z trigger ran bronze/silver/gold and never invoked opal-cot-bd-session-fetch. V2 needs the login to EXECUTE; it releases early on a negative probe, or on Andrew's explicit per-use word for ONE ad-hoc sign-in through the document (held since 2026-09-29T11:37:14.708158+00:00)
**Deploy:** TO-IB-m21-212 Part 2: the cot login box gets the in-run retry, the F2 persist-binding and the registry-clean naming (rows S165, S199). Two artifacts, ONE act: bd_49f_auto_login.js (md5 7d37465ba68e8ddf44a66c008179d080) + secret-ids.env, deployed together; rollback restores BOTH (js 28dd27a054b826cc3a87f6b4498d3b5a from the running-capture, env 9b55e03c9575d4f6b58d1d239c8409fb as captured on the box)
**Authored by:** 0.6.2_AE_PartnerETL~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/bd-cot-auto-login/ | BLOB bytes (git show CLOUD:<path>) uploaded for BOTH files; head-object ContentLength + ETag match the local blob md5; the env upload verified 0 CR | BLOB bytes uploaded (git show CLOUD:<path>), both files, 0 CR verified BEFORE upload. head-object read-back: bd_49f_auto_login.js ContentLength 40333, single-part ETag 7d37465ba68e8ddf44a66c008179d080 = the blob md5, VersionId WZpnhv6I66AqZYUzsS.d3BVAoU37OMKD; secret-ids.env ContentLength 2525, ETag 8e879af5e8e7a608e34a4864c179ee71 = the blob md5, VersionId lbA4Qva2uA1d67GDfkNpF6SNijwuTsoc. ROLLBACK BASELINE captured first and verified: the prior S3 env was 1200 B md5 9b55e03c9575d4f6b58d1d239c8409fb (VersionId a0xSDh0tLG0Ba5oroOcf8a4kqJG2VzOb) -- byte-identical to the box copy the GO names -- and the prior .js was 35049 B ETag 28dd27a054b826cc3a87f6b4498d3b5a (VersionId yidWek0qE6oJXDpoY_5xF0vimE3tMHXL), which is the running-capture in the repo. | CLOSED 20260929T094044Z |
| A2 | ec2-baked-asset | i-0643a5bee8a8feabf /opt/bd-cot-auto-login/ | S3 -> box pull the way the source already deploys, for BOTH files, rc=0 | SSM deeb49bb-189f-49b2-bb64-7062b4dbcd28 on i-0643a5bee8a8feabf, Status Success, ResponseCode 0, stderr empty: both files pulled S3 -> /opt/bd-cot-auto-login/ (39.4 KiB and 2.5 KiB), then PULL-OK. The box was started to reach SSM; it is a stopped-when-idle batch runner the daily trigger Lambda starts anyway. | CLOSED 20260929T094759Z |
| V1 | verify | the RUNNING path on the box | SSM read: .js md5 = 7d37465b..., secret-ids.env md5, and the env CR count which MUST be 0 | SSM 9d73a0f7-0ea9-4df9-ac6f-ca90221b890e -- a SEPARATE read-only command, so this is an independent read and not the deploy command's self-report. Status Success, ResponseCode 0, stderr empty. RUNNING path: bd_49f_auto_login.js md5 7d37465ba68e8ddf44a66c008179d080 = the committed port exactly; secret-ids.env md5 8e879af5e8e7a608e34a4864c179ee71 = the committed blob exactly, 2525 B; CR_COUNT=0 (the GO's condition 3); 4 of 4 required config lines present (BD_IDENTITY_COOKIE, BD_DEVICE_COOKIE, BD_DEBUG_PREFIX, BD_FIRM_ID); node --check on the BOX's own node -> NODE-CHECK-OK. Output not truncated (its ---END--- marker is present). | CLOSED 20260929T094759Z |
| V2 | verify | the first REAL run | the box's own log: the session advanced, or a NAMED failure (exit 2/3 or retries exhausted). Never a silent pass. The 07:30 America/New_York scheduled opal-cot-bd-session-fetch serves if the deploy lands first |  | OPEN |

## Log

- 20260929T093155Z OPENED by 0.6.2_AE_PartnerETL~S with 4 leg(s)
- 20260929T094044Z LEG A1 closed: BLOB bytes uploaded (git show CLOUD:<path>), both files, 0 CR verified BEFORE upload. head-object read-back: bd_49f_auto
- 20260929T094759Z LEG A2 closed: SSM deeb49bb-189f-49b2-bb64-7062b4dbcd28 on i-0643a5bee8a8feabf, Status Success, ResponseCode 0, stderr empty: both file
- 20260929T094759Z LEG V1 closed: SSM 9d73a0f7-0ea9-4df9-ac6f-ca90221b890e -- a SEPARATE read-only command, so this is an independent read and not the dep
- 20260929T113714Z HELD-SOVEREIGN-GATED gate=external/the trigger Lambda's own Lever A cookie-freshness gate: cot-bd-session-trigger S
