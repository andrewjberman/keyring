# Deploy Completion Record
**Date opened:** 2026-10-12T02:17:22.769289+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T022924Z
**Deploy:** IAM-z-1 ACT 3: put-role-policy workspace-sync-permissions -- ajb-workflow and opal-data-portal-s3 (bucket and /*) leave Sid S3Access (pair COO @3860c1c906 / CTO @364e77ecdd)
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| put | activation | workspace-sync-lambda-role/workspace-sync-permissions | the live document equals the committed after-document under a canonical sort_keys compare: 10 statements, 15 ARNs, the 4 dead ARNs absent, opal-data-news-av and /* kept | put-role-policy rc=0; live document read back EQUALS the committed after-document under canonical sort_keys; 10 statements / 15 ARNs; vs the rollback exactly 4 ARNs gone (ajb-workflow, ajb-workflow/*, opal-data-portal-s3, opal-data-portal-s3/*) and 0 added; opal-data-news-av and /* kept (2 live hits); every statement action-identical; Sid set identical; baseline matched the rollback canonically immediately before the act | CLOSED 20261012T022923Z |

## Log

- 20261012T021722Z OPENED by 0.7.0_AE_CloudOps~IR with 1 leg(s)
- 20261012T022923Z LEG put closed: put-role-policy rc=0; live document read back EQUALS the committed after-document under canonical sort_keys; 10 statemen
- 20261012T022924Z CLOSED -- all 1 legs proven
