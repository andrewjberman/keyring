# Deploy Completion Record
**Date opened:** 2026-10-02T10:06:46.585848+00:00
**Status:** OPEN
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
| D1 | ec2-baked-asset | install st13 on i-0167fd745ad906a66 through Systems Manager after window C's job is terminal | the script's output: tar, member and library checks, factory check, unit restart, poll; or its rollback |  | OPEN |
| V1 | verify | the running root, library and digests read back on the host | root c657a5966d-st13; library 857d90b8 with YC_ATTENDED; resident digests unchanged; unit active; queue 0/0; nothing on 5901 |  | OPEN |

## Log

- 20261002T100646Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
- 20261002T100646Z LEG U1 closed: irpt-resident-c657a5966d-st13.tar.gz version 0j0S_Qjp4yITyCLs8shW5MFXqjvVX3.L read back sha256 7c503923adc003a1fb02a8cb8
- 20261002T101212Z LEG I1 closed: SSM d9ca3517-42fd-4ec2-bab6-9b9fff4ce1fa rc 0 (SIGNIN_A/I1_OUTPUT_20261002.txt) 10:11:43-48Z: tigervnc-server-minimal 1.
