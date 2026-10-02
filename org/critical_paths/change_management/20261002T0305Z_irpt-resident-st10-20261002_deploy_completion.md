# Deploy Completion Record
**Date opened:** 2026-10-02T03:05:13.581005+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T032117Z
**Deploy:** resident st9 -> st10: the whole tree at CLOUD b1db201025 (items 15 and 16: the 900 s calculating release and the WAF header journal line; row S253's vendor_requests ledger); never-widen packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | tar and install script on new keys in opal-313476888478-lambda-artifacts ec2/investor-reporting-ycharts/resident | both read back by S3 version with sha256 equal to the built bytes | irpt-resident-b1db201025-st10.tar.gz version oawr7YMKU1ruCEVE40qxv6ax1Ztt3mXI read back sha256 094989ed4a5bcd6688a0139ac4e13787406ce9d101b749c33358a6d2ae4074be (760925 bytes, HeadObject 404 before); resident_host_install_b1db201025-st10.sh version sKNqaKlpHiqZGOe.xV_kbeZGOGxkoygB read back sha256 1a4a9d2f6954901e1db6e29d7617d52cd2a1aff8ab82745a1faae79e57ae02f4 (8702 bytes, 404 before), byte-equal to ST10/resident_host_install_b1db201025-st10.sh; gate ST10/GATE_OUTPUT_20261002.txt PASS | CLOSED 20261002T030824Z |
| D1 | ec2-baked-asset | install on i-0167fd745ad906a66 through Systems Manager, both halves at HEAD first | the script's output: tar and member checks, factory check, unit restart, poll; or its rollback | SSM 18a59af7-f5f7-4b9d-bff9-94d334ee172a rc 0: operator head-object printed sKNqaKlpHiqZGOe.xV_kbeZGOGxkoygB 03:19:34Z; script sha256 verified on the host 03:19:42Z; before root 481166a8f2-st9; package SHA256SUMS OK (243); factory OK enrolled 1276035; queue 0 0; install b1db201025-st10 rc=0; unit restarted 03:19:51Z, NRestarts 0 (ST10/INSTALL_OUTPUT_20261002.txt) | CLOSED 20261002T032053Z |
| V1 | verify | the running root and digests read back on the host | root b1db201025-st10; resident_worker, recipe and broker digests equal the packet's; library unchanged; unit active and polling; queue 0/0 | running root /opt/irpt-resident/b1db201025-st10; resident_worker 1708fe39caf52621 (READ_BACK_CALCULATING_VISIBILITY_S 0, keep_vendor_requests 2); broker 96f0e7782c106d49; durable_job b5192fa2a1d4d5c0 (append_vendor_requests 1); recipe 80b9e3ff7fe47004 (READ_BACK_POLLS = 1); host library 9511060e04f45b51 unchanged, wrapper 55ddb8f7947cba7c; unit active since 03:19:51Z, IRPT_RESIDENT_POLL handled=0 at 03:20:11Z, tracebacks 0; queue 0/0. Every digest equals the packet's section 4 | CLOSED 20261002T032053Z |

## Log

- 20261002T030513Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261002T030824Z LEG U1 closed: irpt-resident-b1db201025-st10.tar.gz version oawr7YMKU1ruCEVE40qxv6ax1Ztt3mXI read back sha256 094989ed4a5bcd6688a0139ac
- 20261002T032053Z LEG D1 closed: SSM 18a59af7-f5f7-4b9d-bff9-94d334ee172a rc 0: operator head-object printed sKNqaKlpHiqZGOe.xV_kbeZGOGxkoygB 03:19:34Z; 
- 20261002T032053Z LEG V1 closed: running root /opt/irpt-resident/b1db201025-st10; resident_worker 1708fe39caf52621 (READ_BACK_CALCULATING_VISIBILITY_S 0,
- 20261002T032117Z CLOSED -- all 3 legs proven
