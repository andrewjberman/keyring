# Deploy Completion Record
**Date opened:** 2026-10-11T02:55:17.038318+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-pr-413: apply IB-pr-417's 49F NARROW holdings bundle (dell1's e56 CUSIP fallback + IB-pr-403's SmartX CUSIP ids + the ticker= fact + IB-pr-414's publish-gate memory fix). AUTHORITY: order IRPT_BCKEND.TO-IB-pr-413 AMENDMENTS 3 and 4 governing; packet 0.9.0_WK_IRPT_BCKEND~279/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-417.md blob 36621e44cb (verified at HEAD); three halves signed at that blob -- ~P2 COO half @c7b3f175b7, CTO half @89003a204b, dell1 ~M1's e56 COO half blob 8f0ef159d3 (commit ced2704270, ancestor of box/dell2). BUILD PIN 4b008d1521c0ded196623ce7323879aefd866b2a; builder bytes .tools/safe_deploy_core.py and ~266/narrow_pack.py are IDENTICAL at that pin and at HEAD. THE ONE KEY: s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting-holdings.tar.gz. NOT TOUCHED: the inflection and cottonwood holdings keys, and the ordered key investor-reporting.tar.gz. BASE = the live IB-pr-404 bytes, sha256 3f2e738f83aa415a2b56cf506d54368f9d2f86f7ded8f19202fc373ef6a28901, ETag 01387cef54b9e15e10023f05029e357d, 468666 B, version irUPjpfrDLoM2zhnhunbBtIG9fP275kI (re-read at apply 2026-10-11T02:48Z, unmoved). BUILT = sha256 fe4000cbd31aaee971793854ad6cf26bc7b2d9a37a484e953896a09084f02f2e, md5 8b482c8db26c2e913aeee72023bacc7e, 470165 B, 44 members, metadata members-sha256=73f33c3c59b77528c6eaaa56799e9c55f570a7adac23a0c6bcd12e66fe343a81 member-count=44. THE PULLING FAMILY: irpt-holdings-refresh-lambda, 49financial only, one SSM command, fired by irpt-holdings-snapshot cron(15 10 ? * MON-FRI *) America/New_York = 14:15Z; the FIRST FIRE AFTER LANDING is Monday 2026-10-12 14:15Z, which lib/trading_calendar.py reads as a trading day with prev trading day Friday 2026-10-09 -- hence the 40-hour window: the after-read waits on that scheduled fire and NO ad-hoc producer run is made, because an ad-hoc production publish off its own clock is a defect. BRANCH B (AMENDMENT 3, the COO half's condition, which OVERRIDES the packet's own Branch B text): on a REFUSED, SIGKILLed or timed-out first fire, copy-object back the PRE-404 version 3Q_W49U7kMa_xO30Q6LQE7QLsFu7ARur (verified live 2026-10-11T02:53Z: ETag 7a400c1482044ab80b45e5878b8f4ad5, 465247 B, members-sha256 099096b1560e926dd330ab2a2e1b900796daa49bf9b694409ed5fac0577055f4), NEVER the 404 version irUPjpfrDLoM2zhnhunbBtIG9fP275kI, because the 404 bytes are the ones the 4 GiB box SIGKILLed (row D2-S56) and that would be a rollback through a WORSE window. IB-pr-404's own L6 stays OPEN until this same fire is read.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 40.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | precheck and the digest gate, both before this ledger opened and before any upload | the live key's ETag and VersionId equal the signed precheck values; exactly two members move and each equals the packet member sha256; the rebuilt bundle's sha256, md5 and bytes equal the packet built table; packed twice byte-identical; no --mint-bundle anywhere |  | OPEN |
| L2 | s3-prefix | opal-data-49financial irpt/49financial/code/gold/investor-reporting-holdings.tar.gz | head-object ETag equals the built md5, both metadata values echoed, and get-object BY THE NEW VERSION ID hashes to the built sha256; new version id recorded as this entry's rollback-of-the-apply pointer |  | OPEN |
| L3 | verify | the replay and the memory harness re-run on the UPLOADED bytes, before the first fire | fwd14_gate_vs_b410 identical and smartx_class_parity identical on the uploaded bytes, and the harness peak below 3650722201 B; a miss is a STOP and Branch B |  | OPEN |
| L4 | verify | the first scheduled fire after landing (Monday 2026-10-12 14:15Z) and the three criteria | the producer output line and the refusal record read from the producer output and NEVER the SSM status; no rc 137; wall time against the prior fire's; the e56 arm counts 32 newly classified and 0 lost; IB114-1-AC1, AC2 and AC3 PASS |  | OPEN |

## Log

- 20261011T025517Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
