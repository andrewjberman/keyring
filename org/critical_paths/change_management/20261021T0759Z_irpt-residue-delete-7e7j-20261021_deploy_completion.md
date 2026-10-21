# Deploy Completion Record
**Date opened:** 2026-10-21T07:59:37.300327+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-RUN-RESIDUE-DELETE-7E7J: delete the 29 synthetic object versions of runs 7e through 7j in opal-data-irpt by exact key and VersionId through three throwaway IAM roles (R22 method), then destroy the six IAM resources
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | reads: 29 manifest versions PRESENT, no lock, audit key exactly its two versions, roles absent, Deny, control object, Andrew's retained objects, retention counts | R0 line |  | OPEN |
| C | verify | scoped plan 6 to add 0 to change 0 to destroy with only s3:DeleteObjectVersion and exact VersionId conditions | plan graded |  | OPEN |
| A | activation | safe-apply of the saved plan (three roles, three policies) | Apply complete 6 added |  | OPEN |
| T | verify | first delete of the manifest's first entry alone: 204 and ABSENT | T line |  | OPEN |
| D | activation | delete the remaining 28 versions by exact key and VersionId in three assumed-role sessions, each read ABSENT, keys' versions empty | D lines |  | OPEN |
| X | activation | destroy the six with a saved destroy plan 0 to add 0 to change 6 to destroy, roles absent, replan, then the whole-root plan after the file is removed | X lines |  | OPEN |
| V | verify | Deny intact, control object present, Andrew's retained objects present before and after | V lines |  | OPEN |

## Log

- 20261021T075937Z OPENED by 0.7.0_AE_CloudOps~IB2 with 7 leg(s)
