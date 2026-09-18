# Deploy Completion Record
**Date opened:** 2026-09-18T12:16:14.899984+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T122217Z
**Deploy:** IRPT_BCKEND TO-IB-rtd-3: re-mint of the investor_reporting bundle with a 10th member, docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json (bundle-only; row S71), to opal-data-mdpf. Blast radius: ONE key, s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz (versioned; pre-cell VersionId 00PXLyYmM0vJavlwdpUHBKRi3pza0_nS, ETag 4c942a76f990874838e33e37f24ed69a -- byte-identical to IB-rtc-9's 0XLkiPt4..., row S74). The three per-firm runner_common.py loose keys are NOT written (bundle-only mint). No schedule change: irpt-holdings-snapshot stays DISABLED. Rollback: re-mint from the pre-cell commit's tree through the guard. Consumer: the irpt-directory-refresh dispatch's builds (the directory runner's members are unchanged).
**Authored by:** 0.4.0_DS_ClientPlatform~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-data-mdpf code/scripts/assets_gold/investor_reporting: HALT_ACK=1 .tools/safe-deploy.sh --mint-bundle investor_reporting | BUNDLE MINTED line + head-object ETag/VersionId + 10 per-member sha stamps echoed | BUNDLE MINTED [mdpf] investor_reporting md5=a8e1a036b4e26cd2fca45f3a295a4c71 at 2026-09-18T12:20:09Z; head-object ETag a8e1a036b4e26cd2fca45f3a295a4c71 VersionId .v.aG6Rbk5wXOjGgb4vnQIeGPzrabMKo, 66518 bytes, sha256 334fc6f6547fdea78d95c6b49d02980498cd2dd586505de92490418170d07b35. 10 stamps; NEW holdings-snapshot-schema-sha256=9c0acba985c38b32f0736045936db14b2d251089f2cdb79a818a12bc69259348 (== the sha256 of blob 9ec70af2, 33882 bytes -- the worktree rendered the blob bytes for that one path, row S75); the other 9 stamps equal IB-rtc-9's. Packed from the tree at 3ac01a96ae (member declared 28bc06907f). Pre-cell 00PXLyYmM0vJavlwdpUHBKRi3pza0_nS / 4c942a76 (row S74). | CLOSED 20260918T122217Z |
| L2 | verify | the three distribution members' loose keys UNCHANGED at the VersionIds read before the mint (49F jnnxQWbVT_lx6WlJu8HbVXNjQJpYK00w, cot 81mlcZFSpRyiH_OeK0OlWFvEHKYUelj_, inf z_WDDmx6004thBhXbT0uBvsDkNibZQF8) and consistent with the minted bundle, read-only | consistency_ib_rtc_2.py output + the loose VersionIds before/after | consistency_ib_rtc_2.check(HEAD, version_id=.v.aG6Rbk5wXOjGgb4vnQIeGPzrabMKo, loose_versions=pre-mint read): CONSISTENCY CONSISTENT: 3 of 3 DISTRIBUTION members agree on both legs. Loose VersionIds UNCHANGED 3 of 3 against the pre-mint read: 49F jnnxQWbVT_lx6WlJu8HbVXNjQJpYK00w, cot 81mlcZFSpRyiH_OeK0OlWFvEHKYUelj_, inf z_WDDmx6004thBhXbT0uBvsDkNibZQF8. Read-only; no write to any loose key. | CLOSED 20260918T122217Z |

## Log

- 20260918T121614Z OPENED by 0.4.0_DS_ClientPlatform~X with 2 leg(s)
- 20260918T122217Z LEG L1 closed: BUNDLE MINTED [mdpf] investor_reporting md5=a8e1a036b4e26cd2fca45f3a295a4c71 at 2026-09-18T12:20:09Z; head-object ETag a
- 20260918T122217Z LEG L2 closed: consistency_ib_rtc_2.check(HEAD, version_id=.v.aG6Rbk5wXOjGgb4vnQIeGPzrabMKo, loose_versions=pre-mint read): CONSISTENCY
- 20260918T122217Z CLOSED -- all 2 legs proven
