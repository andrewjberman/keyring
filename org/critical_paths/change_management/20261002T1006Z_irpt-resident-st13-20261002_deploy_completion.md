# Deploy Completion Record
**Date opened:** 2026-10-02T10:06:46.585848+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T101933Z
**Deploy:** sign-in option A: the resident st12 -> st13 at CLOUD c657a5966d (the capture library's attended hold) and Xvnc on the host, loopback only (CTO batch 131 items 3-4); never-widen packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | tar and install script on new keys in opal-313476888478-lambda-artifacts ec2/investor-reporting-ycharts/resident | both read back by S3 version with sha256 equal to the built bytes | irpt-resident-c657a5966d-st13.tar.gz version 0j0S_Qjp4yITyCLs8shW5MFXqjvVX3.L read back sha256 7c503923adc003a1fb02a8cb88c20bbe471fdb818bf122ee24aee62b0b3c08b9 (767144 bytes, 404 before); resident_host_install_c657a5966d-st13.sh version 79mHrL_O.wRCmmBD2581F98Q6goe2Jow read back sha256 f7b9daba9b8c037696d4967c9d9077f0ffb4faeda662997dfcde7dd302a7ee12 (404 before), byte-equal to SIGNIN_A/resident_host_install_c657a5966d-st13.sh; gate SIGNIN_A/GATE_OUTPUT_ST13_20261002.txt PASS (244 members, changed 2) | CLOSED 20261002T100646Z |
| I1 | verify | install the Xvnc package on i-0167fd745ad906a66 (no service, nothing listening) | Xvnc present; 0 enabled VNC units; 0 listeners on 5900-5910; dnf transaction id | SSM d9ca3517-42fd-4ec2-bab6-9b9fff4ce1fa rc 0 (SIGNIN_A/I1_OUTPUT_20261002.txt) 10:11:43-48Z: tigervnc-server-minimal 1.14.1-3.amzn2023.0.6 installed (16 packages, dnf transaction 6; rollback dnf history undo 6); Xvnc /usr/bin/Xvnc; 0 enabled VNC units; 0 listeners on 5900-5910; resident unit unchanged (active since 09:21:39Z) | CLOSED 20261002T101212Z |
| D1 | ec2-baked-asset | install st13 on i-0167fd745ad906a66 through Systems Manager after window C's job is terminal | the script's output: tar, member and library checks, factory check, unit restart, poll; or its rollback | before-read 10:17:32Z (SIGNIN_A/BEFORE_READ_ST13_20261002.txt): st12 active, irpt-generation 0/0, provider lease holder empty, 0 non-terminal jobs (window C's job READY 10:14:06Z); head-object 10:18:05Z printed 79mHrL_O.wRCmmBD2581F98Q6goe2Jow; SSM 6988babf-9478-42a7-977f-164c779d29c3 rc 0: script sha256 verified on the host 10:18:09Z; SHA256SUMS OK (244); factory OK enrolled 1276035; install c657a5966d-st13 rc=0; tracebacks_30s 0 (SIGNIN_A/INSTALL_OUTPUT_ST13_20261002.txt) | CLOSED 20261002T101933Z |
| V1 | verify | the running root, library and digests read back on the host | root c657a5966d-st13; library 857d90b8 with YC_ATTENDED; resident digests unchanged; unit active; queue 0/0; nothing on 5901 | running root /opt/irpt-resident/c657a5966d-st13; host library 857d90b81960d69a (YC_ATTENDED 3, holdForPerson 2); resident digests unchanged: operation_lease 2519834356b2d7a4, transport d8cdbf3907a7d149, resident_worker 93e50f0f148960ed, broker 96f0e7782c106d49; Xvnc present; listening on 5901: 0; unit active since 2026-10-02T10:18:27Z; queue 0/0 | CLOSED 20261002T101933Z |

## Log

- 20261002T100646Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
- 20261002T100646Z LEG U1 closed: irpt-resident-c657a5966d-st13.tar.gz version 0j0S_Qjp4yITyCLs8shW5MFXqjvVX3.L read back sha256 7c503923adc003a1fb02a8cb8
- 20261002T101212Z LEG I1 closed: SSM d9ca3517-42fd-4ec2-bab6-9b9fff4ce1fa rc 0 (SIGNIN_A/I1_OUTPUT_20261002.txt) 10:11:43-48Z: tigervnc-server-minimal 1.
- 20261002T101933Z LEG D1 closed: before-read 10:17:32Z (SIGNIN_A/BEFORE_READ_ST13_20261002.txt): st12 active, irpt-generation 0/0, provider lease holder 
- 20261002T101933Z LEG V1 closed: running root /opt/irpt-resident/c657a5966d-st13; host library 857d90b81960d69a (YC_ATTENDED 3, holdForPerson 2); residen
- 20261002T101933Z CLOSED -- all 4 legs proven
