# Deploy Completion Record
**Date opened:** 2026-10-08T18:37:56.892878+00:00
**Status:** OPEN
**Deploy:** portal PROD b06863fe <- merge of DEV dbeb6764 (44 commits, 71 files): DSGN_AMGTV1 rounds 46-52, MDPF_SECCLASS, IRPT_YCDGEN/CUSTDY/BCKEND, TCKT_VNEXT; Andrew 'recs approved' 2026-10-08 (@7eb9750741); pair COO @454754ec7d + CTO @b30f3952c6; rollback git revert -m 1 of the merge to b06863fe's tree
**Authored by:** 2.0.0_SA_COO~D
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal PROD merge pushed | merge sha on origin/PROD (ls-remote); merge tree equals dbeb6764 tree |  | OPEN |
| L2 | activation | deploy.yml run on PROD | gh run view conclusion success, all jobs, matched by headSha |  | OPEN |
| L3 | git | annotated tag portal-vX.Y.Z | tag peeled equals PROD head |  | OPEN |
| L4 | verify | served production site | served index read after deploy; marker data-research-coverage in the served bundle; CTO C1: BP/ LN officers chief executive first and one statement of inputs, read on PROD |  | OPEN |

## Log

- 20261008T183756Z OPENED by 2.0.0_SA_COO~D with 4 leg(s)
