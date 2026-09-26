# Deploy Completion Record
**Date opened:** 2026-09-26T22:42:25.551803+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T225825Z
**Deploy:** UIR-07: irpt-directory-search = live o9Qu0Jm7 + directory handler.py + entry.py @49b935c213 (packet v2 a96d2ee0; CTO 101545, CRO @07525238da + the Global-mode arm); rollback o9Qu0Jm7 S3 version 7ENQv_0Nk6WEi5tO0CJBrdtgnBY8yDPF
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | activation | irpt-directory-search artifact + apply | census vs o9Qu0Jm7: exactly handler.py + entry.py; code-only plan; safe-apply; readback; replan 0 | publish 177719486c (directory handler.py + entry.py @49b935c213); artifact o1TXq5PH1+/VVff+hf4U+b+H6Kf1VCJkUJJjAaN+y7Q= 161159 bytes S3 version yxWVUKorLSDlzbSI74E_N8yGcR67rx4y; census vs live o9Qu0Jm7: 20=20, exactly entry.py + handler.py differ. The backend worktree's directory root plans 0/4/11 (it predates M's holdings resources in that root; would destroy irpt_holdings roles/refresh function) -- NOT applied; the main tree's .terraform is bound to another backend config (not reconfigured, shared). Applied with -target=module.irpt_directory_search.aws_lambda_function.this: plan 0/1/0 (source_code_hash + s3_object_version only); safe-apply 22:54:12Z; readback CodeSha256 o1TXq5PH.. Active/Successful | CLOSED 20260926T225825Z |
| A1 | verify | search_rank_arm after + compare | search and browse(q) sets identical; after-rank 1 on both endpoints; Global-mode arm recorded (CRO 101550: a merge without re-rank keeps UIR-07 OPEN, no rollback) | search_rank_arm compare (UIR07_ARM_BEFORE/AFTER_20260926.json): 6 PASS -- same 33 targets; every search SET and every browse(q) SET (all pages) identical; after-rank 1 on search and browse(q) for all (browse(q) before: 49F up to 81, INF up to 35, COT up to 4, the reported case 2/2); no before-rank of 1 lost. GLOBAL arm (CRO 101550): merged set identical; the reported case ranks 2-13 -> 1-12 over the 6 firm orders, because the page concatenates per-firm answers unranked (ClientSearch.tsx:98-106 + search.ts toOptions) -> UIR-07 stays OPEN at the page merge, no rollback (CRO's condition) | CLOSED 20260926T225825Z |

## Log

- 20260926T224225Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260926T225825Z LEG D1 closed: publish 177719486c (directory handler.py + entry.py @49b935c213); artifact o1TXq5PH1+/VVff+hf4U+b+H6Kf1VCJkUJJjAaN+y7Q= 
- 20260926T225825Z LEG A1 closed: search_rank_arm compare (UIR07_ARM_BEFORE/AFTER_20260926.json): 6 PASS -- same 33 targets; every search SET and every br
- 20260926T225825Z CLOSED -- all 2 legs proven
