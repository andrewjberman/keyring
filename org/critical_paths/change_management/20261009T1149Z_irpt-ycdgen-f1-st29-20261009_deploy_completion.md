# Deploy Completion Record
**Date opened:** 2026-10-09T11:49:44.347192+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN TO-APPLY-st29: install st28-plus-the-round-7-research-row on resident host i-0167fd745ad906a66, hand 2.0.0_SA_COO~G2 its F1 re-run, then remove straight to st27 and swap svc back to cottonwood. Artifacts PINNED by measured sha256: tar f0ff4f1653-st29.tar.gz 3bf984a8f752dfbf0d1e450a08b9d05f1174152df1dae2d24f6622c528a0d515 (876768 bytes), installer resident_host_install_f0ff4f1653-st29.sh 9ea64ae53fd81aca7d32662c1e0ade3e8a067f78a532aa9f9f63b958b5291a0f (8659 bytes), both equal to the order declared prefixes. SUPERSEDES TO-APPLY-st28 X1/V2/W2; CTO hard bound 13:09:10Z
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | s3-prefix | put the tar and the installer under ec2/investor-reporting-ycharts/resident/ | each key 404 BEFORE the put, then read back BY VERSION with sha equal to the measured value above |  | OPEN |
| P1 | verify | host_read.py pre_read.sh | st28 running and the st27 root present |  | OPEN |
| D2 | activation | host_read.py install_st29.sh, ONLY when irpt-generation reads 0/0 -- the installer own gate is NEVER forced | root f0ff4f1653-st29, producer_for svc=OPAL, packaged research row firms = 3; re-read the tar and script sha256 at D2 per the CTO half; any failure takes the script own rollback to st28 then STOPS |  | OPEN |
| V1 | verify | the install read-back | the three expectations above, reported to 2.0.0_SA_COO~G2 as V1 closed |  | OPEN |
| F1 | verify | 2.0.0_SA_COO~G2 runs F1 on the installed row | not this seat act; this leg closes when G2 says F1 is done, or at the 13:09:10Z bound |  | OPEN |
| X1 | activation | remove_st29_to_st27.sh at the EARLIER of G2 F1-done or 13:09:10Z, at 0/0 | host on st27 |  | OPEN |
| V2 | verify | the removal read-back | OPAL_PRODUCER_PRINCIPALS = ("andrew@opalinvest.com",) -- Andrew only |  | OPEN |
| W2 | activation | python swap_svc_firm.py 49financial cottonwood, ONE opal-users-v2 item | after: allowedFirmIds cottonwood; then close this ledger and close irpt-ycdgen-f1-st28-20261009 as SUPERSEDED |  | OPEN |

## Log

- 20261009T114944Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 8 leg(s)
