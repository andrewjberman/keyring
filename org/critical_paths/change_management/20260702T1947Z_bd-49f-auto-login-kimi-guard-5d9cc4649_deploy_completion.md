# Deploy Completion Record
**Date opened:** 2026-07-02T19:47:20.090084+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260702T195412Z
**Deploy:** Roll out 5d9cc4649 (Kimi-health-guard + DOM-fallback classify) to i-0fa1846f bd-49f-auto-login mint box -- S3-artifact + SSM-pull; CONDITIONAL-GO (COO via 0.6.2 193623Z); box-idle + mint-clear confirmed
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | bd_49f_auto_login.js 5d9cc4649 -> s3://opal-313476888478-lambda-artifacts/ec2/bd-49f-auto-login/ | s3 ls new size/mtime | s3 ls bd_49f_auto_login.js = 41609 bytes (5d9cc4649; was 37675/06-29); local md5 5dafe6db5e2b45199b015a5aa8b2d7ff | CLOSED 20260702T194834Z |
| L2 | ec2-baked-asset | SSM-pull onto /opt/bd-49f-auto-login + on-box verify | box md5==local md5 + node --check OK (ssm:<cmd_id>) | ssm:3543ce8f-ec6d-4b0e-b214-13ff734af43e Success; box /opt/bd-49f-auto-login/bd_49f_auto_login.js md5=5dafe6db5e2b45199b015a5aa8b2d7ff == local md5 (byte-identical to the node-check-validated 5d9cc4649 file) | CLOSED 20260702T195233Z |
| L3 | git | EC2_MANIFEST deployed_commit=5d9cc4649 committed | commit hash | e4f80f856 (EC2_MANIFEST bd-49f-auto-login deployed_commit=5d9cc4649 + file_checksums) | CLOSED 20260702T195412Z |

## Log

- 20260702T194720Z OPENED by 0.7.0_AE_CloudOps~A with 3 leg(s)
- 20260702T194834Z LEG L1 closed: s3 ls bd_49f_auto_login.js = 41609 bytes (5d9cc4649; was 37675/06-29); local md5 5dafe6db5e2b45199b015a5aa8b2d7ff
- 20260702T195233Z LEG L2 closed: ssm:3543ce8f-ec6d-4b0e-b214-13ff734af43e Success; box /opt/bd-49f-auto-login/bd_49f_auto_login.js md5=5dafe6db5e2b45199b
- 20260702T195412Z LEG L3 closed: e4f80f856 (EC2_MANIFEST bd-49f-auto-login deployed_commit=5d9cc4649 + file_checksums)
- 20260702T195412Z CLOSED -- all 3 legs proven
