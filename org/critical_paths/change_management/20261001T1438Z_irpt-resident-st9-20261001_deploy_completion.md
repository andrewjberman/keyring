# Deploy Completion Record
**Date opened:** 2026-10-01T14:38:06.672189+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T150401Z
**Deploy:** Resident st8 -> st9: the whole tree at CLOUD 481166a8f2, E2 one status read per receive (CTO rulings batch 88 item 4)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | tar and install script on new keys in opal-313476888478-lambda-artifacts ec2/investor-reporting-ycharts/resident | both read back by S3 version with sha256 equal to the built bytes | irpt-resident-481166a8f2-st9.tar.gz version WCfp.LuKrNtKpv31dANEaOtAebXoGfRw read back sha256 486d0c356c989c58121e6a9f67d3caae04a5c08434cdf8cd1297b289cc88a4ce (758863 bytes, HeadObject 404 before); resident_host_install_481166a8f2-st9.sh version SojZdtkv9FjeiJTIHAWVkG7zCXVRo3LU read back sha256 5350877bd4e1a16537f935d3e68717f5a831bd77f85c68e5c9de6bfe24a53332 | CLOSED 20261001T143807Z |
| D1 | ec2-baked-asset | install on i-0167fd745ad906a66 through Systems Manager, both halves at HEAD first | the script's output: tar and member checks, factory check, unit restart, poll; or its rollback | SSM 2e0a8318-2853-4433-a269-8d9a705d0507 rc 0: operator head-object printed SojZdtkv9FjeiJTIHAWVkG7zCXVRo3LU; script sha256 verified on the host 14:59:06Z; before root 9ac9b56d3c-st8; package SHA256SUMS OK 243; queue 0 0 twice; factory OK; install rc=0; unit active since 14:59:17Z, polls_30s 2, tracebacks 0; no rollback | CLOSED 20261001T150401Z |
| V1 | verify | the running root and digests read back on the host | root 481166a8f2-st9; resident_worker and recipe digests equal the packet's; library unchanged; unit active and polling; queue 0/0 | running root /opt/irpt-resident/481166a8f2-st9; resident_worker 49305eeb90d80034 (READ_BACK_CALCULATING_VISIBILITY_S present); recipe 3a4e58515476b841 (READ_BACK_POLLS = 1); host library 9511060e04f45b51 unchanged; unit active and polling; queue 0/0; ST9/INSTALL_OUTPUT_20261001.txt | CLOSED 20261001T150401Z |

## Log

- 20261001T143806Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261001T143807Z LEG U1 closed: irpt-resident-481166a8f2-st9.tar.gz version WCfp.LuKrNtKpv31dANEaOtAebXoGfRw read back sha256 486d0c356c989c58121e6a9f67
- 20261001T150401Z LEG D1 closed: SSM 2e0a8318-2853-4433-a269-8d9a705d0507 rc 0: operator head-object printed SojZdtkv9FjeiJTIHAWVkG7zCXVRo3LU; script sha
- 20261001T150401Z LEG V1 closed: running root /opt/irpt-resident/481166a8f2-st9; resident_worker 49305eeb90d80034 (READ_BACK_CALCULATING_VISIBILITY_S pre
- 20261001T150401Z CLOSED -- all 3 legs proven
