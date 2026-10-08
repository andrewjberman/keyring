# Deploy Completion Record
**Date opened:** 2026-10-08T18:37:56.892878+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T201017Z
**Deploy:** portal PROD b06863fe <- merge of DEV dbeb6764 (44 commits, 71 files): DSGN_AMGTV1 rounds 46-52, MDPF_SECCLASS, IRPT_YCDGEN/CUSTDY/BCKEND, TCKT_VNEXT; Andrew 'recs approved' 2026-10-08 (@7eb9750741); pair COO @454754ec7d + CTO @b30f3952c6; rollback git revert -m 1 of the merge to b06863fe's tree
**Authored by:** 2.0.0_SA_COO~D
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal PROD merge pushed | merge sha on origin/PROD (ls-remote); merge tree equals dbeb6764 tree | origin PROD f73f9ab0eb4f7c9f28171fa8e8e7d3ea5d21ffae (ls-remote read 20:0xZ; pushed by 0.0.0_AB_MSTR~Z msg 31962); merge parents b06863fe + dbeb6764; tree diff vs dbeb6764 0 lines; tsc -b rc=0 | CLOSED 20261008T201015Z |
| L2 | activation | deploy.yml run on PROD | gh run view conclusion success, all jobs, matched by headSha | run 37830156575 Deploy to Production conclusion success, headSha f73f9ab0eb4f7c9f28171fa8e8e7d3ea5d21ffae; jobs Build Production Assets / Deploy to S3 + CloudFront / Tag Deployment all success (gh run view) | CLOSED 20261008T201016Z |
| L3 | git | annotated tag portal-vX.Y.Z | tag peeled equals PROD head | portal-v2.1.204 peeled f73f9ab0 equals origin/PROD f73f9ab0 | CLOSED 20261008T201016Z |
| L4 | verify | served production site | served index read after deploy; marker data-research-coverage in the served bundle; CTO C1: BP/ LN officers chief executive first and one statement of inputs, read on PROD | served https://d2n2nzpeqf34ge.cloudfront.net index 200, Last-Modified 2026-10-08 19:14:26 GMT; walker read on PROD 19:59-20:04Z 8 of 8 PASS (round51/walk/read-20261008T195926Z): MSFT US draws [data-research-coverage=outside_coverage] once (0 src files carry it at b06863fe, 1 at dbeb6764); CTO C1: BP/ LN officers 10 of 10 in served order, chief executive first, and one statement of inputs, 5 of 5 rows, 0 input ledgers; walker DISARMED 20:04:30Z | CLOSED 20261008T201017Z |

## Log

- 20261008T183756Z OPENED by 2.0.0_SA_COO~D with 4 leg(s)
- 20261008T201015Z LEG L1 closed: origin PROD f73f9ab0eb4f7c9f28171fa8e8e7d3ea5d21ffae (ls-remote read 20:0xZ; pushed by 0.0.0_AB_MSTR~Z msg 31962); merge
- 20261008T201016Z LEG L2 closed: run 37830156575 Deploy to Production conclusion success, headSha f73f9ab0eb4f7c9f28171fa8e8e7d3ea5d21ffae; jobs Build Pr
- 20261008T201016Z LEG L3 closed: portal-v2.1.204 peeled f73f9ab0 equals origin/PROD f73f9ab0
- 20261008T201017Z LEG L4 closed: served https://d2n2nzpeqf34ge.cloudfront.net index 200, Last-Modified 2026-10-08 19:14:26 GMT; walker read on PROD 19:59
- 20261008T201017Z CLOSED -- all 4 legs proven
