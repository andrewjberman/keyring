# Deploy Completion Record
**Date opened:** 2026-10-01T10:08:30.072610+00:00
**Status:** OPEN
**Deploy:** Resident st6 -> st7: the whole tree at CLOUD a3b35fd376 (the next resident build of CTO rulings batch 76 item 5) and the host capture library at the same pin
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | tar and install script on new keys in opal-313476888478-lambda-artifacts ec2/investor-reporting-ycharts/resident | both read back by S3 version with sha256 equal to the built bytes | irpt-resident-a3b35fd376-st7.tar.gz version MH5dulKoCsbZS1Bd1wj7FjMR7xTT9rY0 read back sha256 c12a37d6934840691d98d93e4b8196f8744a09f02dbce4682e7cc2c8b024bf01 (757559 bytes, HeadObject 404 before); resident_host_install_a3b35fd376-st7.sh version cYhOzVvvcvFik2D7W419SBuZGVa98nw8 read back sha256 ad9f91d5acd87bd2bf4627265dd3cb00d9da14a24da07f86b77a3c18401ec7a2 | CLOSED 20261001T100830Z |
| D1 | ec2-baked-asset | install on i-0167fd745ad906a66 through Systems Manager, both halves at HEAD first | the script's output: tar and member checks, library swap, factory check, unit restart, poll; or its rollback |  | OPEN |
| V1 | verify | the running root and digests read back on the host | root a3b35fd376-st7; resident_worker, current_authority, host_capture, extract and the host library digests equal the packet's; unit active and polling; both queues 0/0 |  | OPEN |

## Log

- 20261001T100830Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261001T100830Z LEG U1 closed: irpt-resident-a3b35fd376-st7.tar.gz version MH5dulKoCsbZS1Bd1wj7FjMR7xTT9rY0 read back sha256 c12a37d6934840691d98d93e4b
