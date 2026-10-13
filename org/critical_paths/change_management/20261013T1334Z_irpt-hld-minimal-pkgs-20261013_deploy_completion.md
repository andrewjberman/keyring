# Deploy Completion Record
**Date opened:** 2026-10-13T13:34:04.878714+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pr-512: put the two minimal holdings packages at the runner host's scheduled Online (started_by scheduler: irpt-directory-refresh-role, 13:30:36Z), digest-gated; keys s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting-holdings.tar.gz (rollback VersionId fMLoOI6a8ZwNFWZCJjjP90ZadyRg9nFg) and s3://opal-data-inflection/irpt/inflection/code/gold/investor-reporting-holdings.tar.gz (rollback VersionId qR5sZza4EjUT_cbGA5hLo0ar6zu2NfpI); cottonwood NOT written; pair IB-pr-510 packet sha256 c2b7275939d0
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 0 (both firms: run principal exists, assume ok, admitted by the fence, apply principal may put) and step 1 schedule and started_by scheduler | the reads recorded in the apply record |  | OPEN |
| L2 | s3-prefix | 49financial: start read equals the packet, candidate rebuilt equals the packet, put-object to the same key with the candidate metadata, new VersionId, read-back hash and metadata | new VersionId and read-back sha256 |  | OPEN |
| L3 | s3-prefix | inflection: same four gates, put, new VersionId, read-back | new VersionId and read-back sha256 |  | OPEN |
| L4 | verify | cottonwood ETag unchanged; first read: one read-only SSM count per firm of leftover temp files (49financial pattern, inflection pattern), counts only, no delete | counts and the cottonwood ETag after |  | OPEN |

## Log

- 20261013T133404Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
