# Deploy Completion Record
**Date opened:** 2026-09-18T06:30:58.491595+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-rtc-8: re-mint of the investor_reporting bundle with IB-rtc-6's Firm49F (K5, the sign-off packet's step 5) to opal-data-mdpf. Blast radius: ONE key, s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz (versioned; pre-cell VersionId 1jPgGCGLP.uGY5RpMlMJTrKvKzvyYf7O, ETag 0020e7afc760b827a6adb7c0ad538903). The three per-firm runner_common.py loose keys are NOT written (no commit to a distribution member; the mint is bundle-only). Rollback: re-mint from the pre-cell commit's tree through the guard. Consumer: the irpt-directory-refresh dispatch's builds; without IRPT_SOURCE_READ_ROLE_ARN the new runner behaves as today.
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

- 20260918T063058Z OPENED by 0.4.0_DS_ClientPlatform~X with 2 leg(s)
