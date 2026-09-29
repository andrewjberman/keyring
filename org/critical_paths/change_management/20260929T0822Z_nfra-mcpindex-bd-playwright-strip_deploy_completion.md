# Deploy Completion Record
**Date opened:** 2026-09-29T08:22:00.992739+00:00
**Status:** OPEN
**Deploy:** MX-s-14 PHASE B (amendment A3): publish the stripped opal-bd-unrealized/realized/transaction-download documents as the next version and DEFAULT (allocation carved out); acceptance = tonight's 21:38, 21:45, 21:53Z scheduled fires. Halves: CTO NEVER_WIDEN_CTO_HALF_MX-s-14_20260929.md, CVO cvoO_NEVER_WIDEN_MX-s-14_SECOND_HALF_20260929.md
**Authored by:** 0.9.0_WK_NFRA_MCPINDEX~17
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 16.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | rollback targets read live: prior DefaultVersion/LatestVersion and content hash of the 3 documents | values printed from live ssm describe-document/get-document, never typed | G1 read live 2026-09-29T08:21Z: opal-bd-unrealized-download Default=2 Latest=2 (content sha256 first-16 e2bbc0febde98668, 3460 chars; rollback = re-publish v2 as next version + set DEFAULT); opal-bd-realized-download Default=2 Latest=2 (cd2bf147c44653f7, 3434 chars; rollback v2); opal-bd-transaction-download Default=1 Latest=2 (v2 content 18f27fcdf008975b, 3261 chars; rollback v2). Allocation Default=3 Latest=4, NOT published (carved out). Rules bd-unrealized/realized/transaction-pipeline-trigger ENABLED cron 38/45/53 21 MON-FRI. Instances i-0800437d1dbb0b5cc and i-00c7568bc510f7423 stopped at 08:2xZ. Repo files sha256 first-16 == the ask: unrealized b33bb4201627f2d8, realized 570538ea79ddfe59, transaction af59a64d5ca315b0. Time 08:2xZ is outside 21:30-22:15Z. Prior v2 contents saved in worker .scratch/before/. | CLOSED 20260929T082242Z |
| L2 | activation | SSM doc opal-bd-unrealized-download: update-document from the CLOUD file (sha256 b33bb4201627f2d8), then update-document-default-version | get-document $LATEST content sha256 first-16 equals the repo file and Default == Latest |  | OPEN |
| L3 | activation | SSM doc opal-bd-realized-download: update-document from the CLOUD file (sha256 570538ea79ddfe59), then update-document-default-version | get-document $LATEST content sha256 first-16 equals the repo file and Default == Latest |  | OPEN |
| L4 | activation | SSM doc opal-bd-transaction-download: update-document from the CLOUD file (sha256 af59a64d5ca315b0), then update-document-default-version | get-document $LATEST content sha256 first-16 equals the repo file and Default == Latest |  | OPEN |
| L5 | verify | acceptance: the next scheduled weekday fires 21:38Z unrealized, 21:45Z realized, 21:53Z transaction each read SSM Success on the new version | ssm list-commands per document (Status Success, DocumentVersion), merge log line, silver partition written |  | OPEN |
| L6 | git | ledger and readback committed on the worker branch (LOCAL, not pushed) | commit hashes |  | OPEN |

## Log

- 20260929T082200Z OPENED by 0.9.0_WK_NFRA_MCPINDEX~17 with 6 leg(s)
- 20260929T082242Z LEG L1 closed: G1 read live 2026-09-29T08:21Z: opal-bd-unrealized-download Default=2 Latest=2 (content sha256 first-16 e2bbc0febde98668
