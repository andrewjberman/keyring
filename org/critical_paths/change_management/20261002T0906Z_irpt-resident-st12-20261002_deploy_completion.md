# Deploy Completion Record
**Date opened:** 2026-10-02T09:06:12.905007+00:00
**Status:** OPEN
**Deploy:** st12: the resident st11 -> st12 at CLOUD cf3ae52aee (a cookie the vendor rotates is written back to ycharts/session/current at once, under the lease and fence; CTO batch 127); never-widen packet, both halves; no IAM change (WriteFreshSessionOnly already applied)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | tar and install script on new keys in opal-313476888478-lambda-artifacts ec2/investor-reporting-ycharts/resident | both read back by S3 version with sha256 equal to the built bytes | irpt-resident-cf3ae52aee-st12.tar.gz version dL3uvbQqOjO6W0AyUDiT0Nxwbba_eEvw read back sha256 1d1ca78273d1ae9301bd547bdf8e827865ae07dc12240f8dd41b12a8d4877de1 (765913 bytes, 404 before); resident_host_install_cf3ae52aee-st12.sh version tYs77bo4wZIwujZzpMNR0wiOakEFBQqp read back sha256 9c2b2be6be7f239de2b8a123d2f0260f232d32ff8bed7fd7eaaadd48513e95aa (8705 bytes, 404 before), byte-equal to ST12/resident_host_install_cf3ae52aee-st12.sh; gate ST12/GATE_OUTPUT_20261002.txt PASS (244 members, 1 added, 8 changed) | CLOSED 20261002T090653Z |
| D1 | ec2-baked-asset | install on i-0167fd745ad906a66 through Systems Manager, both halves at HEAD first | the script's output: tar and member checks, factory check, unit restart, poll; or its rollback |  | OPEN |
| V1 | verify | the running root and digests read back on the host | root cf3ae52aee-st12; operation_lease and transport digests equal the packet's; unit active and polling; queue 0/0 |  | OPEN |

## Log

- 20261002T090612Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261002T090653Z LEG U1 closed: irpt-resident-cf3ae52aee-st12.tar.gz version dL3uvbQqOjO6W0AyUDiT0Nxwbba_eEvw read back sha256 1d1ca78273d1ae9301bd547bd
