# Deploy Completion Record
**Date opened:** 2026-09-11T12:27:14.156726+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T124255Z
**Deploy:** IRPT_BCKEND TO-IB-rt-5: first-mint of the investor_reporting bundle (directory_runner.py + holdings_snapshot.py) to opal-data-mdpf
**Authored by:** 0.4.0_DS_ClientPlatform~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CODE_TREES gains the investor_reporting bundle on wk-irpt_bckend-2-ds | commit hash | commit 36e4fbf826 on wk-irpt_bckend-2-ds (author 0.4.0_DS_ClientPlatform~X): .tools/safe_deploy_core.py CODE_TREES['mdpf']['bundles'] gains investor_reporting, +35 lines, 0 deletions. LOCAL -- this branch is not pushed; the issuer merges at the drain. | CLOSED 20260911T124254Z |
| L2 | s3-prefix | opal-data-mdpf code/scripts/assets_gold/investor_reporting | the mint's own sha-stamped verify (BUNDLE MINTED line + head-object ETag == local md5 + both per-member sha stamps echoed) -- bundle-routed scripts are EXCLUDED from the per-file comp-pipescript verify by the X-iii design note in safe_deploy_core.py, so the mint verify IS their acceptance surface | BUNDLE MINTED [mdpf] investor_reporting -> s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz (md5=cd188f6edb7270300a7409d66f9a3432), rc=0. Re-derived with a DIFFERENT instrument (aws s3api head-object, not the mint's internal verify): ContentLength=26935, ETag=cd188f6edb7270300a7409d66f9a3432 == the mint's local md5, VersionId=BAv6hA9Iut0wlKFtuq5PsOKfl4hMEKy5; Metadata directory-runner-sha256=431e89285a609fbf3cd695f4cc88722d2f912c37b5e3e88149a9fcd3dff2f491 and holdings-snapshot-sha256=18838c953c4b2c6fb24a83aa546ab7a69a4471dcad7909a4083846e2076b8dc3, each EQUAL to sha256sum of its repo file -- 2 of 2 MEMBERS on 1 of 1 KEY (list-objects-v2 length(Contents)=1; the prefix held 0 before the act). | CLOSED 20260911T124255Z |
| L3 | verify | the push gate routes a later runner commit as a BUNDLE MEMBER, never SKIP-NOT-MEMBER | the gate's own run output | The gate's OWN run over the two real historical commit ranges that ADDED the runners (3654197107~1..3654197107 and 2dbc92e956~1..2dbc92e956) -- the same input that read SKIP-NOT-MEMBER in round 1. Both now read 'BUNDLE-ROUTED: <runner> -> bundle investor_reporting (loose leg frozen 2026-08-11, X-iii)', rc=0, 2 of 2 runners. IN-RUN NEGATIVE CONTROL: each run's sibling tests/*.py still reads 'SKIP-NOT-MEMBER ... 404; prefix ... carries 0 member(s)', so the MEMBER verdict discriminates and tests are excluded from the bundle as declared. No runner was edited (BOUNDS 1); the historical ranges make the no-op-commit probe unnecessary. | CLOSED 20260911T124255Z |

## Log

- 20260911T122714Z OPENED by 0.4.0_DS_ClientPlatform~X with 3 leg(s)
- 20260911T124254Z LEG L1 closed: commit 36e4fbf826 on wk-irpt_bckend-2-ds (author 0.4.0_DS_ClientPlatform~X): .tools/safe_deploy_core.py CODE_TREES['mdpf
- 20260911T124255Z LEG L2 closed: BUNDLE MINTED [mdpf] investor_reporting -> s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-repo
- 20260911T124255Z LEG L3 closed: The gate's OWN run over the two real historical commit ranges that ADDED the runners (3654197107~1..3654197107 and 2dbc9
- 20260911T124255Z CLOSED -- all 3 legs proven
