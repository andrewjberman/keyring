# Deploy Completion Record
**Date opened:** 2026-09-12T08:56:20.424832+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rt-6: re-mint the investor-reporting bundle with the trading-calendar member, and re-drive the fire so the host's import check can be read
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the member declaration in .tools/safe_deploy_core.py committed | commit hash |  | OPEN |
| L2 | s3-prefix | opal-data-mdpf code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz | safe-deploy --mint-bundle rc=0, new ETag/VersionId, four per-member sha metadata keys each equal to the repo file |  | OPEN |
| L3 | verify | the host unpacks the re-minted bundle and the runner IMPORTS -- arm (d)'s import check printed in the command's own stdout | the SSM command id and its IMPORT-OK line |  | OPEN |

## Log

- 20260912T085620Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 3 leg(s)
