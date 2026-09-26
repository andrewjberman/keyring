# Deploy Completion Record
**Date opened:** 2026-09-26T19:00:37.659084+00:00
**Status:** OPEN
**Deploy:** IRPT hop 3: ~Y's P_HOP3_SUBMISSION_FIXES to irpt-ycharts-generate (6 rows re-pinned at a219094b1a) and the resident (f624e8a72f + the 6 patched files); CTO 101438/101441
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | resident package on i-0167fd745ad906a66 = f624e8a72f tree + 6 patched files | SSM install rc 0; unit active; IRPT_RESIDENT_POLL lines; manifest sha; rollback root f624e8a72f retained |  | OPEN |
| L1 | activation | irpt-ycharts-generate artifact + apply | census vs deployed 85TXFzzv (exactly 6 members differ); import closure; safe-apply; readback CodeSha256; 0-diff replan |  | OPEN |
| V1 | verify | content proof (CTO 101441) | every patched file in the served generate zip and the resident host root is byte-equal (sha256) to a219094b1a |  | OPEN |

## Log

- 20260926T190037Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
