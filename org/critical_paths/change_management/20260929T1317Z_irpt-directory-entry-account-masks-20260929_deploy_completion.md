# Deploy Completion Record
**Date opened:** 2026-09-29T13:17:01.414842+00:00
**Status:** OPEN
**Deploy:** AD-10 release step 1 (~M 102808, COO half @1a031f514d): DirectoryEntry.schema.json blob 27d9a8f7 (optional account_masks, additive) staged into irpt-directory-search + irpt-ycharts-generate; source map re-pinned to 4ecbaca410; apply AFTER window 22 closes (both functions are W22 pins)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | two artifacts build + upload + gates | census vs live: ONLY contracts/DirectoryEntry.schema.json differs in each; cold start | Source map: both DirectoryEntry staged_from rows (irpt-directory-search pin 69144433df, irpt-ycharts-generate 19d8f3038c; sha 7ed220ff) re-pinned to 4ecbaca410 (blob 27d9a8f7, sha256 6ad840a5; on CLOUD via ~M's drain bb145ff1fe). build-and-upload rc 0 both (BAU_PARITY_SKIP=1), tracked sources restored (3 resident modules re-checked out). irpt-directory-search: S3 2RmObc9v0Wj4o3f_2PLOrYWgAWzu8mEh sha s0riHZ9h (13:17:11Z), census vs live o1TXq5PH 20 -> 20, ONLY contracts/DirectoryEntry.schema.json differs. irpt-ycharts-generate: S3 DWP1wKAI_ftLo9kcP3p_LC6vV1V2K6W2 sha inrij6hL (13:17:29Z), census vs live wnt7hjAB 111 -> 111, ONLY contracts/DirectoryEntry.schema.json differs (resident modules stay pinned to live blobs). Served directory (the built handler's own load_directory, function env): 49F 4,620 / COT 258 / INF 292 entries, 0 invalid under the live or the new copy, 0 carry account_masks. Built handler imports OK. | CLOSED 20260929T132032Z |
| D1 | activation | apply both functions | halves at HEAD; W22 closed; S3 latest == built version at apply; plans code-only; safe-apply; readback; deployed invokes clean; re-plan 0 |  | OPEN |
| A1 | verify | served directory read unchanged | a served directory entry per firm validates under the new copy before and after; the page's directory search/resolve answers as before |  | OPEN |

## Log

- 20260929T131701Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260929T132032Z LEG U1 closed: Source map: both DirectoryEntry staged_from rows (irpt-directory-search pin 69144433df, irpt-ycharts-generate 19d8f3038c
