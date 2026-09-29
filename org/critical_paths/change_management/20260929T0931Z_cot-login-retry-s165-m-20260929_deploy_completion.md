# Deploy Completion Record
**Date opened:** 2026-09-29T09:31:55.136937+00:00
**Status:** OPEN
**Deploy:** TO-IB-m21-212 Part 2: the cot login box gets the in-run retry, the F2 persist-binding and the registry-clean naming (rows S165, S199). Two artifacts, ONE act: bd_49f_auto_login.js (md5 7d37465ba68e8ddf44a66c008179d080) + secret-ids.env, deployed together; rollback restores BOTH (js 28dd27a054b826cc3a87f6b4498d3b5a from the running-capture, env 9b55e03c9575d4f6b58d1d239c8409fb as captured on the box)
**Authored by:** 0.6.2_AE_PartnerETL~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/bd-cot-auto-login/ | BLOB bytes (git show CLOUD:<path>) uploaded for BOTH files; head-object ContentLength + ETag match the local blob md5; the env upload verified 0 CR |  | OPEN |
| A2 | ec2-baked-asset | i-0643a5bee8a8feabf /opt/bd-cot-auto-login/ | S3 -> box pull the way the source already deploys, for BOTH files, rc=0 |  | OPEN |
| V1 | verify | the RUNNING path on the box | SSM read: .js md5 = 7d37465b..., secret-ids.env md5, and the env CR count which MUST be 0 |  | OPEN |
| V2 | verify | the first REAL run | the box's own log: the session advanced, or a NAMED failure (exit 2/3 or retries exhausted). Never a silent pass. The 07:30 America/New_York scheduled opal-cot-bd-session-fetch serves if the deploy lands first |  | OPEN |

## Log

- 20260929T093155Z OPENED by 0.6.2_AE_PartnerETL~S with 4 leg(s)
