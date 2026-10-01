# Deploy Completion Record
**Date opened:** 2026-10-01T10:08:30.072610+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T102900Z
**Deploy:** Resident st6 -> st7: the whole tree at CLOUD a3b35fd376 (the next resident build of CTO rulings batch 76 item 5) and the host capture library at the same pin
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | tar and install script on new keys in opal-313476888478-lambda-artifacts ec2/investor-reporting-ycharts/resident | both read back by S3 version with sha256 equal to the built bytes | irpt-resident-a3b35fd376-st7.tar.gz version MH5dulKoCsbZS1Bd1wj7FjMR7xTT9rY0 read back sha256 c12a37d6934840691d98d93e4b8196f8744a09f02dbce4682e7cc2c8b024bf01 (757559 bytes, HeadObject 404 before); resident_host_install_a3b35fd376-st7.sh version cYhOzVvvcvFik2D7W419SBuZGVa98nw8 read back sha256 ad9f91d5acd87bd2bf4627265dd3cb00d9da14a24da07f86b77a3c18401ec7a2 | CLOSED 20261001T100830Z |
| D1 | ec2-baked-asset | install on i-0167fd745ad906a66 through Systems Manager, both halves at HEAD first | the script's output: tar and member checks, library swap, factory check, unit restart, poll; or its rollback | SSM c738dda8-355a-44d0-b4a0-c931e0de83b2 rc 0: operator head-object printed cYhOzVvvcvFik2D7W419SBuZGVa98nw8; script sha256 verified on the host 10:26:52Z; before root 36dfa80058-st6 library 0fec0ca9; package SHA256SUMS OK 243; queue 0 0 twice; factory OK enrolled 1276035; install rc=0; unit active since 10:27:05Z, polls_30s 2, tracebacks 0; no rollback | CLOSED 20261001T102900Z |
| V1 | verify | the running root and digests read back on the host | root a3b35fd376-st7; resident_worker, current_authority, host_capture, extract and the host library digests equal the packet's; unit active and polling; both queues 0/0 | running root /opt/irpt-resident/a3b35fd376-st7; resident_worker 2ba09afaa8a2fc9e (keep_refused_pdf, _with_lookup_class present); current_authority 5291b3be7e0006ad; host_capture 8288e724e843cb89; extract 3f5e2bb0bc2299f6; host library 9511060e04f45b51 (wrapper 55ddb8f7947cba7c); unit active and polling; queue 0/0; ST7/INSTALL_OUTPUT_20261001.txt | CLOSED 20261001T102900Z |

## Log

- 20261001T100830Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261001T100830Z LEG U1 closed: irpt-resident-a3b35fd376-st7.tar.gz version MH5dulKoCsbZS1Bd1wj7FjMR7xTT9rY0 read back sha256 c12a37d6934840691d98d93e4b
- 20261001T102900Z LEG D1 closed: SSM c738dda8-355a-44d0-b4a0-c931e0de83b2 rc 0: operator head-object printed cYhOzVvvcvFik2D7W419SBuZGVa98nw8; script sha
- 20261001T102900Z LEG V1 closed: running root /opt/irpt-resident/a3b35fd376-st7; resident_worker 2ba09afaa8a2fc9e (keep_refused_pdf, _with_lookup_class p
- 20261001T102900Z CLOSED -- all 3 legs proven
