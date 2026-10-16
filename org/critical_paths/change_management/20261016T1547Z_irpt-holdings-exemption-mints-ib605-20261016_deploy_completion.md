# Deploy Completion Record
**Date opened:** 2026-10-16T15:47:48.892710+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pr-605: mint the three standalone holdings bundles carrying the absent_at_source exemption (49financial d2eaf305 from pin b1d354cfc9; Cottonwood and Inflection bc2e8f54 from pin 5fad7eaaa8); Branch B bundle versions 49financial 5eOkwoqs3FXzvfIww0.3YIQ2BK.jqPMO, cottonwood VmEyGROJ_3VUTLYkYEWPJujNhmwRy58d, inflection SngSJHRbxbLoOM1GQxY9e1zI.1_1qmUt; ECS sweep: 9 ACTIVE task families, none pulls the bundle keys (the pullers are the scheduled runner commands irpt holdings refresh <firm>)
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 80.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | the three bundle keys irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz (opal-data-49financial, opal-data-cottonwood, opal-data-inflection): mint each FROM its own scratch pin worktree with safe-deploy.sh --mint-bundle, BUNDLE MINTED with MATCH, new version id, landed sha256 equals the built digest | each firm's head-object, new VersionId, landed==built |  | OPEN |
| L2 | verify | each minted firm's first scheduled fire after the mints (Monday 2026-10-19 14:15Z): current/manifest.json and SSM status, STAMPED_T_MINUS_1 with a T-1 partition under it, or HELD_NO_NEW_PUBLICATION with the absent partition named and the frontier unchanged | manifest read and SSM status per firm |  | OPEN |
| L3 | verify | the exemption's after-read: 49financial published or refused and its listed count (2 expected, amount 0, one evidence value per exempted account), Cottonwood listed count and no closed name in the manifest, Inflection listed count | counts per firm |  | OPEN |

## Log

- 20261016T154748Z OPENED by 0.7.0_AE_CloudOps~IB2 with 3 leg(s)
