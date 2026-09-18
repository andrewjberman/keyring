# Deploy Completion Record
**Date opened:** 2026-09-18T07:56:32.113605+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-rtc-9: re-mint of the investor_reporting bundle carrying the jsonschema-3.2.0-tolerant directory_runner.py and holdings_snapshot.py (row W2-S56) to opal-data-mdpf. Blast radius: ONE key, s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz (versioned; pre-cell VersionId q8myxeHdNw48w1uDb7YTcBh8DHV9TzU2, ETag 479af04c0a3a1eb6651707b340df9926). The three per-firm runner_common.py loose keys are NOT written (no commit to a distribution member; the mint is bundle-only). No host package change. Rollback: re-mint from the pre-cell commit's tree through the guard. Consumer: the irpt-directory-refresh dispatch's builds (next scheduled fire 13:00Z).
**Authored by:** 0.4.0_DS_ClientPlatform~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-data-mdpf code/scripts/assets_gold/investor_reporting: HALT_ACK=1 .tools/safe-deploy.sh --mint-bundle investor_reporting | BUNDLE MINTED line + head-object ETag/VersionId + 9 per-member sha stamps echoed |  | OPEN |
| L2 | verify | the three distribution members' loose keys UNCHANGED (VersionIds as IB-rtc-2 left them) and consistent with the minted bundle, read-only | consistency_ib_rtc_2.py output + the loose VersionIds before/after |  | OPEN |

## Log

- 20260918T075632Z OPENED by 0.4.0_DS_ClientPlatform~X with 2 leg(s)
