# Deploy Completion Record
**Date opened:** 2026-10-14T12:46:14.403350+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R29c: release 29 leg L3, irpt-ycharts-generate (the upload door) at expected CodeSha256 5TRFZf6Grgd9V9jWBVu2QDPRVbgfWBjsuuw8rtf8hRA= (generate_installed.py and uploads.py moved, ordinary_viewer.py added; code only); THE ONLY WIDENING of release 29: FIRM_ADVISOR and FIRM_OPERATIONS of 49financial, inflection, cottonwood gain upload and owned-input analysis; signed pair COO blob 5e8b3cbd95 + CTO half @abbfe49feb; rollback VersionId edHLV8L0.FETO34.wAag6i7FHBJvfAuW; gates R0b R0f R0g and the exact suite failure set run before anything moves
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | hashes (COO half, both diffs); markers over every worktree, 0 live open entries naming irpt-ycharts-generate; ledgers naming it all CLOSED incl irpt-ycg-r28; R0b CodeSha256 reAjAQOV.. and latest version edHLV8L0.. and object hash; R0f six counts with denominators (before any build); R0g role policy on partner tables; exact suite failure set subset of the 108 rows; G3 and G4 before | printed reads and R0F_COUNTS.txt and R0G_POLICY.txt |  | OPEN |
| L2 | s3-prefix | throwaway worktree detached at 0c0ae5a8f5, guard printed, release input diff then map diff applied, BUILD_ONLY digest 5TRFZf6G.., then upload of one new version, read back sha256 e5344565fe86.. | digest equal, VersionId, sha256 equal |  | OPEN |
| L3 | verify | scoped plan -target=module.irpt_ycharts_generate.aws_lambda_function.this: 0 add 1 change 0 destroy, last_modified s3_object_version source_code_hash only, environment equal | plan summary line |  | OPEN |
| L4 | activation | .tools/safe-apply.sh on the saved plan | apply line |  | OPEN |
| L5 | verify | G1 CodeSha256 5TRFZf6G.., G2 106 members exactly two differ and one added, G3 envelope equal, G4 environment and role unchanged | printed reads |  | OPEN |
| L6 | git | map close commit: irpt-ycharts-generate entry changes of the two diffs plus artifact_* and last_deployed_*, merged | commit hash |  | OPEN |

## Log

- 20261014T124614Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 6 leg(s)
