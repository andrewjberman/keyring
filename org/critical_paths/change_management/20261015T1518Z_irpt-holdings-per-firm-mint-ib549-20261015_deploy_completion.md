# Deploy Completion Record
**Date opened:** 2026-10-15T15:18:14.696971+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T145350Z
**Deploy:** IRPT_BCKEND TO-IB-pr-549: mint the three standalone holdings bundles, each from its firm's pin (49financial closure-fix pin b1d354cfc9, Cottonwood and Inflection pin 2 5fad7eaaa8), packet V3 sha256 94eca88e9071; Branch B bundle versions 49financial UHOCIkWj3QiIzNucG1VjNnk_AufIg6oD, cottonwood oyIYMVdh_l2zCg5ZWvn3ISPPS6_9Q82_, inflection PzhCs97qVBXkZcIjaOklHmzWiFsOFafM
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 32.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | the three bundle keys irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz (opal-data-49financial, opal-data-cottonwood, opal-data-inflection): mint each from its own pin worktree with safe-deploy.sh --mint-bundle, BUNDLE MINTED with MATCH, new version id, landed sha256 equals the bundle built at the digest gate | each firm's head-object, new VersionId and landed==built | 3 mints from their own pins, each BUNDLE MINTED with MATCH, head-object read, landed sha256 equals the digest-gate build: 49financial 5eOkwoqs..(from UHOCIkWj..) 15:19:37Z, cottonwood VmEyGROJ..(from oyIYMVdh..) 15:20:31Z, inflection SngSJHRb..(from PzhCs97q..) 15:21:09Z | CLOSED 20261015T152201Z |
| L2 | verify | each firm's first scheduled fire of irpt-holdings-snapshot after the mints (2026-10-16 14:15Z): current/manifest.json and SSM status, either STAMPED_T_MINUS_1 with a T-1 partition under it, or HELD_NO_NEW_PUBLICATION with the absent partition named and the frontier unchanged | manifest read and SSM status per firm | read 2026-10-16 14:45Z, SSM Success x3 on one Online host: cottonwood STAMPED_T_MINUS_1 stamp 2026-10-15 (T-1 fact_holdings and fact_allocations date=2026-10-15 under it, index U6IpoTrX.. written 14:18:14Z); inflection STAMPED_T_MINUS_1 stamp 2026-10-15 (gold date=2026-10-15, custody snapshots dated 2026-10-16 hold the 10-15 close, index RS_kgSmu.. 14:18:30Z); 49financial NEITHER accepted outcome: T-1 candidate built (7675 accounts) and REFUSED 14:19:07Z on account_lost count 2 (publish_refusal.json), T-1 custody partitions present, served frontier 2026-10-12 unchanged (index daFZJt6f.. unchanged). Evidence IB199-2_after_read.json | CLOSED 20261016T144427Z |
| L3 | verify | the cash rule's after-read: the published snapshot's Cash-sub holdings read asset class Cash, counts only, for each firm that published | counts per firm | published snapshots only: cottonwood Money Market rows 136 and inflection 1113 all asset class cash, 0 cash-like rows classed otherwise; the four named tickers do not appear as ids (opaque ids), the read is by sub-asset class; 49financial published nothing | CLOSED 20261016T144427Z |
| L4 | verify | the 49financial index still holds no row for 2026-10-08 (the gap unchanged) | index read | 49financial index holds 10 dates, none is 2026-10-08; index version daFZJt6f.. unchanged | CLOSED 20261016T144428Z |
| L5 | verify | one read-only kernel-log count (journalctl -k grep -ciE) on the runner host that ran the first fire while Online, or the reason it was not read | count or reason | ONE read-only host command on the one Online host that ran the three fires, window 2026-10-16 14:14Z to 14:25Z: oom_count 0 (grep -c exit 1 on zero, SSM status Failed for that reason); journal coverage not separately verified, only one host command is allowed | CLOSED 20261016T144428Z |

## Log

- 20261015T151814Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261015T152201Z LEG L1 closed: 3 mints from their own pins, each BUNDLE MINTED with MATCH, head-object read, landed sha256 equals the digest-gate build
- 20261016T144427Z LEG L2 closed: read 2026-10-16 14:45Z, SSM Success x3 on one Online host: cottonwood STAMPED_T_MINUS_1 stamp 2026-10-15 (T-1 fact_holdi
- 20261016T144427Z LEG L3 closed: published snapshots only: cottonwood Money Market rows 136 and inflection 1113 all asset class cash, 0 cash-like rows cl
- 20261016T144428Z LEG L4 closed: 49financial index holds 10 dates, none is 2026-10-08; index version daFZJt6f.. unchanged
- 20261016T144428Z LEG L5 closed: ONE read-only host command on the one Online host that ran the three fires, window 2026-10-16 14:14Z to 14:25Z: oom_coun
- 20261016T145350Z CLOSED -- all 5 legs proven
