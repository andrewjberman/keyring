# Deploy Completion Record
**Date opened:** 2026-09-18T06:30:58.491595+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T063431Z
**Deploy:** IRPT_BCKEND TO-IB-rtc-8: re-mint of the investor_reporting bundle with IB-rtc-6's Firm49F (K5, the sign-off packet's step 5) to opal-data-mdpf. Blast radius: ONE key, s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz (versioned; pre-cell VersionId 1jPgGCGLP.uGY5RpMlMJTrKvKzvyYf7O, ETag 0020e7afc760b827a6adb7c0ad538903). The three per-firm runner_common.py loose keys are NOT written (no commit to a distribution member; the mint is bundle-only). Rollback: re-mint from the pre-cell commit's tree through the guard. Consumer: the irpt-directory-refresh dispatch's builds; without IRPT_SOURCE_READ_ROLE_ARN the new runner behaves as today.
**Authored by:** 0.4.0_DS_ClientPlatform~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-data-mdpf code/scripts/assets_gold/investor_reporting: HALT_ACK=1 .tools/safe-deploy.sh --mint-bundle investor_reporting | BUNDLE MINTED line + head-object ETag/VersionId + 9 per-member sha stamps echoed | HALT_ACK=1 bash .tools/safe-deploy.sh --mint-bundle investor_reporting (the halt gate listed the same 7 routine, non-STOP messages 17-21 days old in the BASE serial's inbox; reviewed) -> rc=0, 'BUNDLE MINTED [mdpf] investor_reporting -> s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz (md5=479af04c0a3a1eb6651707b340df9926)' with 9 stamps echoed; directory-runner-sha256=a16b5396b95f04bb725bf20dadc78c7b7ef2d9e8226f8fd99307433ed245e9b3 (IB-rtc-6's Firm49F), the other 8 equal to IB-rtc-2's. head-object: ETag 0020e7afc760b827a6adb7c0ad538903 v 1jPgGCGLP.uGY5RpMlMJTrKvKzvyYf7O -> 479af04c0a3a1eb6651707b340df9926 v q8myxeHdNw48w1uDb7YTcBh8DHV9TzU2, 60447 bytes, 2026-09-18T06:33:22Z. | CLOSED 20260918T063430Z |
| L2 | verify | the three distribution members' loose keys UNCHANGED (VersionIds as IB-rtc-2 left them) and consistent with the minted bundle, read-only | consistency_ib_rtc_2.py output + the loose VersionIds before/after | consistency_ib_rtc_2.py --ref HEAD --version-id q8myxeHdNw48w1uDb7YTcBh8DHV9TzU2 -> rc=0 'CONSISTENCY CONSISTENT: 3 of 3'. Loose keys UNCHANGED at IB-rtc-2's VersionIds: 49F jnnxQWbV... 5221d6b5, INF z_WDDmx6... d974c587, COT bobsNlnm... d88a5939 -- each == its repo md5, each bundle member == its repo sha256. No commit to a distribution member in this cell. | CLOSED 20260918T063430Z |

## Log

- 20260918T063058Z OPENED by 0.4.0_DS_ClientPlatform~X with 2 leg(s)
- 20260918T063430Z LEG L1 closed: HALT_ACK=1 bash .tools/safe-deploy.sh --mint-bundle investor_reporting (the halt gate listed the same 7 routine, non-STO
- 20260918T063430Z LEG L2 closed: consistency_ib_rtc_2.py --ref HEAD --version-id q8myxeHdNw48w1uDb7YTcBh8DHV9TzU2 -> rc=0 'CONSISTENCY CONSISTENT: 3 of 3
- 20260918T063431Z CLOSED -- all 2 legs proven
