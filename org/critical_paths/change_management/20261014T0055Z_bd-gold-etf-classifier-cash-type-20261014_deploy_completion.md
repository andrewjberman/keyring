# Deploy Completion Record
**Date opened:** 2026-10-14T00:55:08.177156+00:00
**Status:** CLOSED -- REFUSED BY GATE, nothing created -- closed 20261014T010047Z
**Deploy:** IRPT_DASHBD TO-DB-b-183: apply the FDRXX -> CASH classifier release, ONE S3 object s3://opal-data-bd/code/gold/lib/etf_classifier.py from live d2e6aa88086c.. (S3 version 0jhXHH7axm_H934t5s5gVDVNJ6Y_WqI.) to the committed bytes of e340e07f4e (sha256 e7385264668e.., 19496 B) by safe-deploy.sh in explicit-files mode; packet sha256 cfc1dd8d0120 (bound), COO half + CTO half @d3b576bb67 signed; packet, COO half and CTO half read whole before step 0; rollback = copy-object of the version recorded at the apply (PARTIAL for C_06 after a run); the first D_04 run after the upload is read by the issuer (L3), so this ledger stays OPEN
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the code pin: etf_classifier.py at commit e340e07f4e hashes e7385264668e9bf746aeab809c8ff0a869f9091685f86751b1679dfc6ddd81ba and the working tree file equals it | git show hash and working-tree hash |  | OPEN |
| L2 | s3-prefix | before reads (live object equals d2e6aa88.., versioning Enabled, no open entry on the BD gold tree, no gold chain run in flight with the instrument named), tests and import smoke at the pinned bytes, then the ONE explicit-files safe-deploy; read-back equals e7385264.. and comp-pipescript deployed MATCH; after sha256 and version id by own aws s3 cp and head-object | the reads, tests, upload rc and read-back |  | OPEN |
| L3 | verify | THE FIRST D_04 RUN AFTER THE UPLOAD, READ BY THE ISSUER: no position of the 17 moved rows still fixed_income in the advisor positions files, moved count at least the 20 floor or the reason stated; stays OPEN for 2.0.0_SA_COO~D2 (COO half condition 7) | the issuer's read |  | OPEN |

## Log

- 20261014T005508Z OPENED by 0.7.0_AE_CloudOps~IB2 with 3 leg(s)
- 20261014T010047Z CLOSED -- REFUSED BY GATE before apply, world untouched: REFUSAL LINE: the order TO-DB-b-183 step 1(b) 'an open entry on the BD gold tree is a STOP' and the COO half condition 6 'the apply is not made during another seat open ledger entry on the Black Diamond gold code tree'. At 2026-10-14T00:5xZ the trunk ledger 20261013T0837Z_advi-firmbkts-fb-j-3-dispatcher-text-warn-20261013 (0.7.0_AE_CloudOps~FB1, code/gold/gold_dispatch.sh in s3://opal-data-bd) rea
