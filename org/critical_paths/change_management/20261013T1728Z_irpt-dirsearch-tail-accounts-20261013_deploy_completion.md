# Deploy Completion Record
**Date opened:** 2026-10-13T17:28:05.058121+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pr-516: move irpt-directory-search to the signed built digest rXHDDz/ZhY2p.. (handler.py only; tail search returns each permitted account's own ACCOUNT entry) by the module's Terraform path; function irpt-directory-search ONLY (sibling irpt-directory-refresh not moved); Branch B = S3 version aPcJ4jPQL9NheWPRbhhrw0dAM35ywQWc of investor-reporting/irpt-directory-search.zip (live tvrsQ+w820jp1.., hex b6faec43); pair IB-pr-515 packet sha256 3c369b9086b3, COO + CTO signed
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates by the artifact: packet sha256, both halves signed, step 0 MATCH (same three buckets and prefix), marker census over every worktree naming the function = 0 with denominators, live CodeSha256 tvrsQ+w820jp1..; Branch B version named and hash-matched | the reads printed in the apply record |  | OPEN |
| L2 | s3-prefix | BUILD_ONLY digest equals rXHDDz/ZhY2pZFuLDcrPisAs69IuTd6p8Rwflxhvwyw= (hex ad71c30f..), then the same build uploaded, verified by head-object | printed digest, new VersionId |  | OPEN |
| L3 | verify | terraform plan to a planfile (module irpt_directory_search, s3_object_version and source_code_hash only): 1 to change, 0 to add, 0 to destroy | plan summary line |  | OPEN |
| L4 | activation | bash .tools/safe-apply.sh on the planfile; after: live CodeSha256 equals the built digest, re-plan 0 changes, deployed zip vs pre-apply live zip differ in handler.py only | apply line, CodeSha256, re-plan line, member diff |  | OPEN |
| L5 | verify | two direct lambda invokes with a synthetic directory_fixture: tail search returns exactly one ACCOUNT entry with permitted_account_count 1; resolve returns exactly one account; response sha256 of the search recorded | the two results |  | OPEN |

## Log

- 20261013T172805Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
