# Deploy Completion Record
**Date opened:** 2026-09-19T05:21:05.674671+00:00
**Status:** OPEN
**Deploy:** IB-rtf-2: refusal-order inversion + unprojected_grant disclosure field deployed to 7 investor-reporting serving functions
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | irpt-directory-search code update | CodeSha256==built post-apply |  | OPEN |
| L2 | activation | irpt-export-render code update | CodeSha256==built post-apply |  | OPEN |
| L3 | activation | irpt-holdings code update | CodeSha256==built post-apply |  | OPEN |
| L4 | activation | irpt-narrative code update | CodeSha256==built post-apply |  | OPEN |
| L5 | activation | irpt-status code update | CodeSha256==built post-apply |  | OPEN |
| L6 | activation | irpt-performance-adapter code update | CodeSha256==built post-apply |  | OPEN |
| L7 | activation | irpt-ycharts-generate code update | CodeSha256==built post-apply |  | OPEN |
| L8 | verify | live route re-test: abby_horton served with disclosure, cross-firm refused, pre-fix negative control | battery + live reads |  | OPEN |

## Log

- 20260919T052105Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 8 leg(s)
