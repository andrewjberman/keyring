# Deploy Completion Record
**Date opened:** 2026-06-26T23:02:10.859904+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260626T230404Z
**Deploy:** cot device-trust re-inject wiring (Andrew-direct): bake new run-bd-auto-login.sh to box
**Authored by:** 0.6.2_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit run-bd-auto-login.sh device-trust re-inject | hash pushed | 61dc06e5d pushed CLOUD (032bb5d6a..61dc06e5d) | CLOSED 20260626T230243Z |
| L2 | s3-prefix | s3 ec2/bd-cot-auto-login/run-bd-auto-login.sh landed | s3 cp + ls size | s3 ec2/bd-cot-auto-login/run-bd-auto-login.sh 3258B landed 19:02:42; local md5 a10ac98ada74e0539b987cb30c8fd979 | CLOSED 20260626T230331Z |
| L3 | ec2-baked-asset | box /opt/bd-cot-auto-login/run-bd-auto-login.sh re-baked | SSM md5/cat of running path == committed | SSM 37cd0a62 Success: BOX_MD5=a10ac98ada74e0539b987cb30c8fd979 == committed local md5 (baked /opt copy parity) | CLOSED 20260626T230401Z |
| L4 | verify | box sources device token -> BD_DEVICE_REGISTRATION set (dry, no login) | SSM echo set/unset | SSM 37cd0a62 Success: L4_RESULT=BD_DEVICE_REGISTRATION_WOULD_BE_SET len=28 secret=blackdiamond/cot/session (dry, no login) | CLOSED 20260626T230402Z |

## Log

- 20260626T230210Z OPENED by 0.6.2_AE_PartnerETL with 4 leg(s)
- 20260626T230243Z LEG L1 closed: 61dc06e5d pushed CLOUD (032bb5d6a..61dc06e5d)
- 20260626T230331Z LEG L2 closed: s3 ec2/bd-cot-auto-login/run-bd-auto-login.sh 3258B landed 19:02:42; local md5 a10ac98ada74e0539b987cb30c8fd979
- 20260626T230401Z LEG L3 closed: SSM 37cd0a62 Success: BOX_MD5=a10ac98ada74e0539b987cb30c8fd979 == committed local md5 (baked /opt copy parity)
- 20260626T230402Z LEG L4 closed: SSM 37cd0a62 Success: L4_RESULT=BD_DEVICE_REGISTRATION_WOULD_BE_SET len=28 secret=blackdiamond/cot/session (dry, no logi
- 20260626T230404Z CLOSED -- all 4 legs proven
