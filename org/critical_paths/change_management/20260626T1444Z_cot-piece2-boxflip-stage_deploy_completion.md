# Deploy Completion Record
**Date opened:** 2026-06-26T14:44:09.747141+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260626T144758Z
**Deploy:** PIECE-2 box-stage: cot-exporter env relay->gateway + self-locating APP_DIR wrapper (STAGE only; production 02:00 re-point is separate, CVO-gated)
**Authored by:** 0.6.0_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit cot wrapper+env artifacts | hash pushed | commit 3f9b43897 on origin/CLOUD (branch -r --contains confirms) | CLOSED 20260626T144634Z |
| L2 | verify | S3 artifacts landed ec2/bd-cot-auto-login/ | s3 ls size+etag | s3 ls ec2/bd-cot-auto-login/: run-bd-auto-login.sh 1760B + secret-ids.env 876B landed | CLOSED 20260626T144635Z |
| L3 | ec2-baked-asset | box /opt/bd-cot-auto-login/ env=gateway + wrapper self-locating APP_DIR | SSM md5/cat of running path | SSM Success: box /opt/bd-cot-auto-login/secret-ids.env = BD_OTP_ADAPTER=gateway + BD_OTP_GATEWAY_URL/SECRET_ID set + BD_FIRM_ID=cot; run-bd-auto-login.sh APP_DIR self-locating (line 15) + node $APP_DIR/bd_49f_auto_login.js; CR-stripped; md5 wrapper da3a5ef1 env 6c4a224f | CLOSED 20260626T144757Z |

## Log

- 20260626T144409Z OPENED by 0.6.0_AE_PartnerETL with 3 leg(s)
- 20260626T144634Z LEG L1 closed: commit 3f9b43897 on origin/CLOUD (branch -r --contains confirms)
- 20260626T144635Z LEG L2 closed: s3 ls ec2/bd-cot-auto-login/: run-bd-auto-login.sh 1760B + secret-ids.env 876B landed
- 20260626T144757Z LEG L3 closed: SSM Success: box /opt/bd-cot-auto-login/secret-ids.env = BD_OTP_ADAPTER=gateway + BD_OTP_GATEWAY_URL/SECRET_ID set + BD_
- 20260626T144758Z CLOSED -- all 3 legs proven
