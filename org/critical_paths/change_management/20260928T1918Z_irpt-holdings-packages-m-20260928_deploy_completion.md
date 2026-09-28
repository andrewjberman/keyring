# Deploy Completion Record
**Date opened:** 2026-09-28T19:18:46.411839+00:00
**Status:** OPEN
**Deploy:** R4 D.0: re-mint irpt_holdings_{49f,inf,cot} from CLOUD bcf7a6adde+ (cash rule + UIC-16); nothing scheduled runs them
**Authored by:** 0.9.0_WK_IRPT_BCKEND~42
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M1 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_49f | BUNDLE MINTED line + head-object members-sha256 + member-count |  | OPEN |
| M2 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_inf | BUNDLE MINTED line + head-object members-sha256 + member-count |  | OPEN |
| M3 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_cot | BUNDLE MINTED line + head-object members-sha256 + member-count |  | OPEN |

## Log

- 20260928T191846Z OPENED by 0.9.0_WK_IRPT_BCKEND~42 with 3 leg(s)
