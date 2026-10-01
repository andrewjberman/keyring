# Deploy Completion Record
**Date opened:** 2026-10-01T14:38:06.672189+00:00
**Status:** OPEN
**Deploy:** Resident st8 -> st9: the whole tree at CLOUD 481166a8f2, E2 one status read per receive (CTO rulings batch 88 item 4)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | tar and install script on new keys in opal-313476888478-lambda-artifacts ec2/investor-reporting-ycharts/resident | both read back by S3 version with sha256 equal to the built bytes |  | OPEN |
| D1 | ec2-baked-asset | install on i-0167fd745ad906a66 through Systems Manager, both halves at HEAD first | the script's output: tar and member checks, factory check, unit restart, poll; or its rollback |  | OPEN |
| V1 | verify | the running root and digests read back on the host | root 481166a8f2-st9; resident_worker and recipe digests equal the packet's; library unchanged; unit active and polling; queue 0/0 |  | OPEN |

## Log

- 20261001T143806Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
