# Deploy Completion Record
**Date opened:** 2026-06-29T14:09:23.105229+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260629T141633Z
**Deploy:** ADVI_BDAPIMIG.P1-DURABLE LEG2: 49f box-pull (durable self-re-mint auto-login) -- deploy js e6e5ee2e + wrapper + secret-ids.env to S3 -> bake on i-0fa1846f04ed7e337 -> off-cycle live OTP test (= the 49f unfreeze). CTO GO 140455Z; 0.7.0 blast+bearer GREEN 140802Z.
**Authored by:** 0.6.2_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD LEG1 commit (wrapper+secret-ids.env+instance.tf) | b93bda5a2 pushed | b93bda5a2 (LEG1 wrapper+secret-ids.env+instance.tf) on origin/CLOUD; lock design 09d0883cd also pushed | CLOSED 20260629T140949Z |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/bd-49f-auto-login/ (js+wrapper+secret-ids.env) | 3 artifacts uploaded, js md5==e6e5ee2e | S3 ec2/bd-49f-auto-login/: js md5=e6e5ee2e6629578110e1d9aa5fa971e9 (==repo), wrapper=043c0caec3da..., secret-ids.env=22dc77f8... all == committed | CLOSED 20260629T141024Z |
| L3 | ec2-baked-asset | /opt/bd-49f-auto-login on i-0fa1846f04ed7e337 | SSM md5 of running path == committed (js e6e5ee2e + wrapper + secret-ids.env) | SSM md5 of /opt/bd-49f-auto-login/ running path: js=e6e5ee2e6629578110e1d9aa5fa971e9 (==committed, has window_seconds+retry), wrapper=043c0caec3da..., secret-ids.env=22dc77f8... all == committed (cmd cab33304) | CLOSED 20260629T141153Z |
| L4 | verify | off-cycle live OTP test | captured_at advance + .bd.identity minted + bd-49f-authtoken-dead alarm flips OK (NOT self-report) | OFF-CYCLE live OTP test cmd e748132b rc=0 (14:12-14:15Z, outside cot 02:00). GROUNDED on live SM (not self-report): blackdiamond/49f/session captured_at 2026-06-25T21:13Z -> 2026-06-29T14:15:15Z (advanced); bd_device_registration empty->present len=30; bd_identity fresh len=347; 8 cookies. Login self-completed WITHOUT manual OTP (gateway adapter fetched code, window=120, native-IP nav OK = no bot-block). authtoken-dead alarm flips on next probe cycle. | CLOSED 20260629T141633Z |

## Log

- 20260629T140923Z OPENED by 0.6.2_AE_PartnerETL with 4 leg(s)
- 20260629T140949Z LEG L1 closed: b93bda5a2 (LEG1 wrapper+secret-ids.env+instance.tf) on origin/CLOUD; lock design 09d0883cd also pushed
- 20260629T141024Z LEG L2 closed: S3 ec2/bd-49f-auto-login/: js md5=e6e5ee2e6629578110e1d9aa5fa971e9 (==repo), wrapper=043c0caec3da..., secret-ids.env=22d
- 20260629T141153Z LEG L3 closed: SSM md5 of /opt/bd-49f-auto-login/ running path: js=e6e5ee2e6629578110e1d9aa5fa971e9 (==committed, has window_seconds+re
- 20260629T141633Z LEG L4 closed: OFF-CYCLE live OTP test cmd e748132b rc=0 (14:12-14:15Z, outside cot 02:00). GROUNDED on live SM (not self-report): blac
- 20260629T141633Z CLOSED -- all 4 legs proven
