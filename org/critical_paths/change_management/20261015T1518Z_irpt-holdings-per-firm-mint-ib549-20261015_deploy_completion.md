# Deploy Completion Record
**Date opened:** 2026-10-15T15:18:14.696971+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pr-549: mint the three standalone holdings bundles, each from its firm's pin (49financial closure-fix pin b1d354cfc9, Cottonwood and Inflection pin 2 5fad7eaaa8), packet V3 sha256 94eca88e9071; Branch B bundle versions 49financial UHOCIkWj3QiIzNucG1VjNnk_AufIg6oD, cottonwood oyIYMVdh_l2zCg5ZWvn3ISPPS6_9Q82_, inflection PzhCs97qVBXkZcIjaOklHmzWiFsOFafM
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 32.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | the three bundle keys irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz (opal-data-49financial, opal-data-cottonwood, opal-data-inflection): mint each from its own pin worktree with safe-deploy.sh --mint-bundle, BUNDLE MINTED with MATCH, new version id, landed sha256 equals the bundle built at the digest gate | each firm's head-object, new VersionId and landed==built | 3 mints from their own pins, each BUNDLE MINTED with MATCH, head-object read, landed sha256 equals the digest-gate build: 49financial 5eOkwoqs..(from UHOCIkWj..) 15:19:37Z, cottonwood VmEyGROJ..(from oyIYMVdh..) 15:20:31Z, inflection SngSJHRb..(from PzhCs97q..) 15:21:09Z | CLOSED 20261015T152201Z |
| L2 | verify | each firm's first scheduled fire of irpt-holdings-snapshot after the mints (2026-10-16 14:15Z): current/manifest.json and SSM status, either STAMPED_T_MINUS_1 with a T-1 partition under it, or HELD_NO_NEW_PUBLICATION with the absent partition named and the frontier unchanged | manifest read and SSM status per firm |  | OPEN |
| L3 | verify | the cash rule's after-read: the published snapshot's Cash-sub holdings read asset class Cash, counts only, for each firm that published | counts per firm |  | OPEN |
| L4 | verify | the 49financial index still holds no row for 2026-10-08 (the gap unchanged) | index read |  | OPEN |
| L5 | verify | one read-only kernel-log count (journalctl -k grep -ciE) on the runner host that ran the first fire while Online, or the reason it was not read | count or reason |  | OPEN |

## Log

- 20261015T151814Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261015T152201Z LEG L1 closed: 3 mints from their own pins, each BUNDLE MINTED with MATCH, head-object read, landed sha256 equals the digest-gate build
