# Deploy Completion Record
**Date opened:** 2026-10-01T11:47:28.460565+00:00
**Status:** OPEN
**Deploy:** Resident st7 -> st8: the whole tree at CLOUD 9ac9b56d3c, the settings-row reader's repair (CTO rulings batch 76 item 5, batch 83)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | tar and install script on new keys in opal-313476888478-lambda-artifacts ec2/investor-reporting-ycharts/resident | both read back by S3 version with sha256 equal to the built bytes | irpt-resident-9ac9b56d3c-st8.tar.gz version qMVedUlttPFVVOLsvmsx_mavt03zqkN8 read back sha256 9c640e306f7c760abedf27226c19c349385de0a459dc88816d8148b49effd911 (758484 bytes, HeadObject 404 before); resident_host_install_9ac9b56d3c-st8.sh version cDhKxZNv0XjSxGZ6kjyMfGBcM_Ab7e8L read back sha256 6407b7cac436d264fb84399c57d504b9ecb00395d51ce3d17aeb7c88e8294b53 | CLOSED 20261001T114728Z |
| D1 | ec2-baked-asset | install on i-0167fd745ad906a66 through Systems Manager, both halves at HEAD first | the script's output: tar and member checks, factory check, unit restart, poll; or its rollback |  | OPEN |
| V1 | verify | the running root and digests read back on the host | root 9ac9b56d3c-st8; resident_worker and extract digests equal the packet's; library unchanged; unit active and polling; queue 0/0 |  | OPEN |

## Log

- 20261001T114728Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261001T114728Z LEG U1 closed: irpt-resident-9ac9b56d3c-st8.tar.gz version qMVedUlttPFVVOLsvmsx_mavt03zqkN8 read back sha256 9c640e306f7c760abedf27226c
