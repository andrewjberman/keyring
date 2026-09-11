# Deploy Completion Record
**Date opened:** 2026-09-11T14:54:53.555178+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rt-8 arm (g) -- the FOUR synthetic export PDFs deleted on Andrew's word (1.0.0_SA_CTO 95968, 13:48Z, VERBATIM 'yes on synthetic exports')
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | THE INVENTORY RE-READ AT THE MOMENT OF THE ACT: list-objects-v2 under firms/49financial/generations/GENIBS14SYN/attempts/1/exports/ holds EXACTLY the four named keys and nothing else, and head-object reads irpt-synthetic=true on 4 of 4. A FIFTH object is a STOP, not a fifth delete | verbatim CLI output with its denominator |  | OPEN |
| L2 | verify | THE FOUR LITERAL DELETES: s3api delete-object per key, four calls, never a prefix delete and never --recursive; each response captured with its VersionId/DeleteMarker fields | the four delete-object responses verbatim |  | OPEN |
| L3 | verify | THE AFTER-READ: head-object returns 404 on 4 of 4, and list-objects-v2 under the prefix returns 0 objects -- 0 unexpected objects remaining | verbatim CLI output with its denominator |  | OPEN |
| L4 | verify | THE BLAST RADIUS HELD: nothing outside the four keys was touched -- the GENRT8PROOF bundle still heads 200, and the battery re-runs green with arm (g) printing 4 of 4 deleted, 0 of 4 remaining, 0 unexpected objects | battery transcript |  | OPEN |

## Log

- 20260911T145453Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 4 leg(s)
