# Deploy Completion Record
**Date opened:** 2026-09-11T12:27:14.156726+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-rt-5: first-mint of the investor_reporting bundle (directory_runner.py + holdings_snapshot.py) to opal-data-mdpf
**Authored by:** 0.4.0_DS_ClientPlatform~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CODE_TREES gains the investor_reporting bundle on wk-irpt_bckend-2-ds | commit hash |  | OPEN |
| L2 | s3-prefix | opal-data-mdpf code/scripts/assets_gold/investor_reporting | the mint's own sha-stamped verify (BUNDLE MINTED line + head-object ETag == local md5 + both per-member sha stamps echoed) -- bundle-routed scripts are EXCLUDED from the per-file comp-pipescript verify by the X-iii design note in safe_deploy_core.py, so the mint verify IS their acceptance surface |  | OPEN |
| L3 | verify | the push gate routes a later runner commit as a BUNDLE MEMBER, never SKIP-NOT-MEMBER | the gate's own run output |  | OPEN |

## Log

- 20260911T122714Z OPENED by 0.4.0_DS_ClientPlatform~X with 3 leg(s)
