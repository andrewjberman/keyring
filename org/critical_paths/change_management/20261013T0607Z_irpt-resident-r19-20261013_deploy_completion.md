# Deploy Completion Record
**Date opened:** 2026-10-13T06:07:51.965527+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R19a: install the resident reader release -- root 0485393f3a-r19 over the running 0485393f3a-st32 on host i-0167fd745ad906a66. Two reader members move (intake/uploads.py 176682cb..., intake/template_reader.py 83ab9b45...); 294 of 298 members unchanged; capture library and wrapper NOT moved. Tar 84df6479655c07ae6000af40404e53eb056b4c403aa9134bbe9c1521317d497a, host script 8b53be13..., package sums a3dea4ec.... Pair: COO half blob 2140b9352c, CTO half @6facbbb2d3. NO removal leg: r19 stays unless V1 fails or the issuer orders X1 (rollback_r19.sh, not run without a new word). Lambda leg is IB2's and starts only after V1.
**Authored by:** 0.7.0_AE_CloudOps~YC2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | s3-prefix | put the tar, host script and package SHA256SUMS under ec2/investor-reporting-ycharts/resident/ in opal-313476888478-lambda-artifacts (3 new keys) | each key 404 before the put, read back with sha256 equal to the order's value; a different sha256 is a STOP |  | OPEN |
| P1 | verify | host_read.py pre_read_r19.sh -- read-only pre-read, expect st32 running, FIVE STOPs | five PASS lines P1 STOP-READ, -2, -3, -4, -5; reader members read 47f89e0b... and 76795b75... with 0 READER_VERSION lines; any FAIL installs nothing |  | OPEN |
| D2 | activation | host_read.py install_r19.sh ONLY when irpt-generation reads 0 visible and 0 in flight -- the installer's gate is never forced | running root 0485393f3a-r19, active, 0 tracebacks; any failure takes the installer's own rollback to st32, then STOP |  | OPEN |
| V1 | verify | the install read-back, every expectation of the order step 5 | uploads.py 176682cb..., template_reader.py 83ab9b45..., READER_VERSION irpt-template-reader.r18.1, sha256sum -c 0 of 297 not OK, imports OK, library a1c28801... = bindings, wrapper = bindings, kept library copy a1c28801..., rollback root present, NO SIGN-IN 0 |  | OPEN |

## Log

- 20261013T060751Z OPENED by 0.7.0_AE_CloudOps~YC2 with 4 leg(s)
