# Deploy Completion Record
**Date opened:** 2026-09-18T12:16:14.899984+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-rtd-3: re-mint of the investor_reporting bundle with a 10th member, docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json (bundle-only; row S71), to opal-data-mdpf. Blast radius: ONE key, s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz (versioned; pre-cell VersionId 00PXLyYmM0vJavlwdpUHBKRi3pza0_nS, ETag 4c942a76f990874838e33e37f24ed69a -- byte-identical to IB-rtc-9's 0XLkiPt4..., row S74). The three per-firm runner_common.py loose keys are NOT written (bundle-only mint). No schedule change: irpt-holdings-snapshot stays DISABLED. Rollback: re-mint from the pre-cell commit's tree through the guard. Consumer: the irpt-directory-refresh dispatch's builds (the directory runner's members are unchanged).
**Authored by:** 0.4.0_DS_ClientPlatform~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-data-mdpf code/scripts/assets_gold/investor_reporting: HALT_ACK=1 .tools/safe-deploy.sh --mint-bundle investor_reporting | BUNDLE MINTED line + head-object ETag/VersionId + 10 per-member sha stamps echoed |  | OPEN |
| L2 | verify | the three distribution members' loose keys UNCHANGED at the VersionIds read before the mint (49F jnnxQWbVT_lx6WlJu8HbVXNjQJpYK00w, cot 81mlcZFSpRyiH_OeK0OlWFvEHKYUelj_, inf z_WDDmx6004thBhXbT0uBvsDkNibZQF8) and consistent with the minted bundle, read-only | consistency_ib_rtc_2.py output + the loose VersionIds before/after |  | OPEN |

## Log

- 20260918T121614Z OPENED by 0.4.0_DS_ClientPlatform~X with 2 leg(s)
