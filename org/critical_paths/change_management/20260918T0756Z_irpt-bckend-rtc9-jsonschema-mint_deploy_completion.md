# Deploy Completion Record
**Date opened:** 2026-09-18T07:56:32.113605+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T080041Z
**Deploy:** IRPT_BCKEND TO-IB-rtc-9: re-mint of the investor_reporting bundle carrying the jsonschema-3.2.0-tolerant directory_runner.py and holdings_snapshot.py (row W2-S56) to opal-data-mdpf. Blast radius: ONE key, s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz (versioned; pre-cell VersionId q8myxeHdNw48w1uDb7YTcBh8DHV9TzU2, ETag 479af04c0a3a1eb6651707b340df9926). The three per-firm runner_common.py loose keys are NOT written (no commit to a distribution member; the mint is bundle-only). No host package change. Rollback: re-mint from the pre-cell commit's tree through the guard. Consumer: the irpt-directory-refresh dispatch's builds (next scheduled fire 13:00Z).
**Authored by:** 0.4.0_DS_ClientPlatform~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-data-mdpf code/scripts/assets_gold/investor_reporting: HALT_ACK=1 .tools/safe-deploy.sh --mint-bundle investor_reporting | BUNDLE MINTED line + head-object ETag/VersionId + 9 per-member sha stamps echoed | BUNDLE MINTED [mdpf] investor_reporting md5=4c942a76f990874838e33e37f24ed69a at 2026-09-18T07:58:33Z; head-object ETag 4c942a76f990874838e33e37f24ed69a VersionId 0XLkiPt4wljdniLnF2fkPKN4qAIkjUbc, 61540 bytes, sha256 e2a933b923d50626578969b3544e070161f029bdb4132b6f600db66859504b3b. Stamps: directory-runner-sha256 a16b5396.. -> 95bd6043c7bca2ab04a28f55175e0af40d9eccf34b9558c72f6a9a8364045360, holdings-snapshot-sha256 2afde9ae.. -> ce063c4188c52d1a1ed28d9be607ae548e5de0ba99e6d21b9dd57953480e9b29; the other 7 unchanged. Packed from the tree at 163c3bf7b0 (runners committed de4e176cc3). Pre-cell q8myxeHdNw48w1uDb7YTcBh8DHV9TzU2 / 479af04c. | CLOSED 20260918T080040Z |
| L2 | verify | the three distribution members' loose keys UNCHANGED (VersionIds as IB-rtc-2 left them) and consistent with the minted bundle, read-only | consistency_ib_rtc_2.py output + the loose VersionIds before/after | consistency_ib_rtc_2.py --ref HEAD --version-id 0XLkiPt4wljdniLnF2fkPKN4qAIkjUbc: CONSISTENCY CONSISTENT: 3 of 3 DISTRIBUTION members agree on both legs. Loose VersionIds unchanged, as IB-rtc-2 left them: 49F jnnxQWbVT_lx6WlJu8HbVXNjQJpYK00w (5221d6b5), cot bobsNlnmKIjMyMW8PHxiQVeJCXPIJmOs (d88a5939), inf z_WDDmx6004thBhXbT0uBvsDkNibZQF8 (d974c587). Read-only; no write to any loose key. | CLOSED 20260918T080041Z |

## Log

- 20260918T075632Z OPENED by 0.4.0_DS_ClientPlatform~X with 2 leg(s)
- 20260918T080040Z LEG L1 closed: BUNDLE MINTED [mdpf] investor_reporting md5=4c942a76f990874838e33e37f24ed69a at 2026-09-18T07:58:33Z; head-object ETag 4
- 20260918T080041Z LEG L2 closed: consistency_ib_rtc_2.py --ref HEAD --version-id 0XLkiPt4wljdniLnF2fkPKN4qAIkjUbc: CONSISTENCY CONSISTENT: 3 of 3 DISTRIB
- 20260918T080041Z CLOSED -- all 2 legs proven
