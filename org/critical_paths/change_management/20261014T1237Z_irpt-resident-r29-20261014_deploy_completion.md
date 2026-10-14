# Deploy Completion Record
**Date opened:** 2026-10-14T12:37:58.851250+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R29b: install the resident release 29 -- root 0485393f3a-r29 over the running 0485393f3a-r28 on host i-0167fd745ad906a66. Four members differ (intake/uploads.py, ops/status.py, reports/resident_bindings.json package_pin only, SHA256SUMS); none added, none removed; capture library and wrapper NOT moved. Tar 2de2adce622f8bb9bbd5ebc071e862446b056303c0d9ffd7d41b050bd17f51a4, host script 5fd383f9..., package sums eebbf8cf.... Pair: COO half blob 5e8b3cbd95 (verified by hash-object), CTO half @abbfe49feb (msg 7591). GO: L2 closed per COO msg 7629 (irpt-status CodeSha256 yNpw441T... read live by this seat). NO removal leg; rollback_r29.sh not run without a new word.
**Authored by:** 0.7.0_AE_CloudOps~YC2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | s3-prefix | put the tar, host script and package SHA256SUMS under ec2/investor-reporting-ycharts/resident/ in opal-313476888478-lambda-artifacts (3 new keys) | each key 404 before the put, read back with sha256 equal to the order's value; a different sha256 is a STOP |  | OPEN |
| P1 | verify | host_read.py pre_read_r29.sh -- read-only pre-read, expect r28 running and r29 absent, FIVE STOPs | five PASS lines P1 STOP-READ, -2, -3, -4, -5; any FAIL installs nothing |  | OPEN |
| D2 | activation | host_read.py install_r29.sh ONLY when irpt-generation reads 0 visible and 0 in flight | running root 0485393f3a-r29, active, 0 tracebacks, polls at least 1; any failure takes the installer's own rollback to r28, then STOP |  | OPEN |
| V1 | verify | the install read-back, every expectation of order step 5 | uploads.py f85e8c9b..., template_reader.py a61cd0c6..., READER_VERSION irpt-template-reader.r19.3, P2b MATCH every member, sha256sum -c 0 of 298 not OK, imports OK, P4 yfinance_check.py absent, library a1c28801... = bindings, wrapper = bindings, kept library copy a1c28801..., rollback root r28 present, NO SIGN-IN 0 |  | OPEN |

## Log

- 20261014T123758Z OPENED by 0.7.0_AE_CloudOps~YC2 with 4 leg(s)
