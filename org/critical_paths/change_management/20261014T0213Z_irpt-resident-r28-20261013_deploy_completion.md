# Deploy Completion Record
**Date opened:** 2026-10-14T02:13:33.205891+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R28b: install the resident release 28 -- root 0485393f3a-r28 over the running 0485393f3a-r19 on host i-0167fd745ad906a66. Nine members differ and one is added (bindings, sums, reader r19.3, portfolio, uploads, security_resolution, ops/status, resident_worker, opal_packager, lib/trading_calendar.py); capture library and wrapper NOT moved. Tar 80f4743091a10c0d82b6cba4f66ba4afb6188ece0b64b269066c5426a6335a68, host script bbead0d2..., package sums 7978dae9.... Pair: COO half blob e9bb20d7fe, CTO half @d3adae2fc8 (msg 7415). GO: L2/L1 closed per COO msg 7432; opal-ticket-api C/Rt/FnSq... read; R0d 01:42:20Z turned_back 0. Step 5 (install and restart) HELD by the issuer until the 02:24Z YCharts probe result (msg 7442). NO removal leg; rollback_r28.sh not run without a new word. The ~IB2 ledger on irpt-ycharts-generate is open and does not touch the resident.
**Authored by:** 0.7.0_AE_CloudOps~YC2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | s3-prefix | put the tar, host script and package SHA256SUMS under ec2/investor-reporting-ycharts/resident/ in opal-313476888478-lambda-artifacts (3 new keys) | each key 404 before the put, read back with sha256 equal to the order's value; a different sha256 is a STOP |  | OPEN |
| P1 | verify | host_read.py pre_read_r28.sh -- read-only pre-read, expect r19 running and r28 absent, FIVE STOPs | five PASS lines P1 STOP-READ, -2, -3, -4, -5; reader members and worker print with their wanted values; any FAIL installs nothing |  | OPEN |
| D2 | activation | host_read.py install_r28.sh ONLY when irpt-generation reads 0 visible and 0 in flight AND the issuer has released step 5 after the 02:24Z probe | running root 0485393f3a-r28, active, 0 tracebacks, polls at least 1; any failure takes the installer's own rollback to r19, then STOP |  | OPEN |
| V1 | verify | the install read-back, every expectation of order step 5 | uploads.py 80ace2d3..., template_reader.py a61cd0c6..., READER_VERSION irpt-template-reader.r19.3, P2b MATCH for all eight members, sha256sum -c 0 of 298 not OK, imports OK, P4 yfinance_check.py absent, library a1c28801... = bindings, wrapper = bindings, kept library copy a1c28801..., rollback root r19 present, NO SIGN-IN 0 |  | OPEN |

## Log

- 20261014T021333Z OPENED by 0.7.0_AE_CloudOps~YC2 with 4 leg(s)
