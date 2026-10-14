# Deploy Completion Record
**Date opened:** 2026-10-14T00:00:33.777673+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pr-521: move irpt-export-render to the signed built digest 5/9LZBbTEWOfrnNZufc6Mqz5pbDxTxYAxpWcZVURGs4= (hex e7ff4b64..): ONE member, irpt_contracts/ExportReceipt.schema.json v1.1 to v1.2 (fixes the export status read refusing its own receipts, row D2-S152), 65 of 66 members identical; function irpt-export-render ONLY; Branch B = S3 version _LGUODZLsTpblhaTy2ODlBjRnwdx6cW1 of investor-reporting/irpt-export-render.zip (live K74JEIjw0NKmy4YfEo7Sb7LcRxEII+/yaYtaKJ3qnD8=, hex 2bbe0910..); pair IB-pr-519 packet sha256 7d7888984731, COO @b667f38d96 + CTO @a047ade972 signed; receipt store re-read dry-run: 1 receipt, 1 carries the field, 0 lacking, 0 unreadable; the CTO's after-read is a person's (Andrew's next export), so this ledger is closed only on the issuer's word
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates by the artifact: packet sha256, both halves signed, receipt store dry-run re-read (0 lacking the field, 0 unreadable), ledgers naming the function (0 open), markers over every worktree (0 naming), live CodeSha256 K74JEIjw0NKm..; Branch B version named and hash-matched | the reads in the apply record |  | OPEN |
| L2 | s3-prefix | source-map row edited (pin 8d08ee54.. to e8005582.., sha256 5a7bda2e.. to 118a3575..), BUILD_ONLY digest equals 5/9LZBbTEWOfrnNZufc6Mqz5pbDxTxYAxpWcZVURGs4=, then the same build uploaded and verified by head-object | printed digest, new VersionId |  | OPEN |
| L3 | verify | terraform plan to a planfile (module irpt_export_render, s3_object_version and source_code_hash only): 1 to change, 0 to add, 0 to destroy | plan summary line |  | OPEN |
| L4 | activation | bash .tools/safe-apply.sh on the planfile; live CodeSha256 equals the built digest, re-plan 0 changes, exactly irpt_contracts/ExportReceipt.schema.json differs from the pre-apply zip with the signed member hash; source-map row committed with the release | apply line, digest, re-plan line, member diff, commit |  | OPEN |
| L5 | verify | the one stored receipt validated OFFLINE against the DEPLOYED zip's schema member (scratch copy deleted), then the health proof with NO invoke at least 10 minutes after the apply: Invocations and Errors metrics, log-group error signatures incl ValidationError, START lines as the positive control | receipts_checked, valid, window, invocation count, error count |  | OPEN |
| L6 | verify | THE CTO's AFTER-READ, A PERSON'S: one NEW export reaches a readable status on DEV (Andrew's next export) and the pre-existing receipt is still readable; stays OPEN for the issuer | the issuer's read |  | OPEN |

## Log

- 20261014T000033Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)
