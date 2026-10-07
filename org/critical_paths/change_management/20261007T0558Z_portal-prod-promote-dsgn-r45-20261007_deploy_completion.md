# Deploy Completion Record
**Date opened:** 2026-10-07T05:58:03.565694+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261007T060817Z
**Deploy:** portal DEV 8ddfe409 -> PROD (base ab3191d0): DSGN_AMGTV1 round 45 (659104f4) + AMGT_RESAPP /freshness round 77 (504ddb3d) + /freshness Dev-only (8ddfe409); Andrew promote it + Do it 2026-10-07; rollback ab3191d0
**Authored by:** 2.0.0_SA_COO~D
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal PROD merge pushed | merge sha on origin/PROD (ls-remote) | origin PROD b06863fe (ls-remote read 06:05Z); merge parents ab3191d0 + 8ddfe409; parity diff vs origin/DEV 0 lines; tsc -b rc=0 | CLOSED 20261007T060816Z |
| L2 | activation | deploy.yml run on PROD | gh run view conclusion success, all jobs, matched by headSha | run 37579269539 Deploy to Production conclusion success, matched by headSha b06863fe; jobs Build/Deploy to S3 + CloudFront/Tag all success | CLOSED 20261007T060816Z |
| L3 | git | annotated tag portal-vX.Y.Z | tag peeled equals PROD head | portal-v2.1.203 peeled b06863fe equals origin/PROD b06863fe | CLOSED 20261007T060816Z |
| L4 | verify | served production site | served index read after deploy | served https://d2n2nzpeqf34ge.cloudfront.net index Last-Modified 2026-10-07 06:03:45 GMT; marker data-input-provenance (0 src files at ab3191d0, 1 at b06863fe) found in assets/index-DcaTeEdJ.js | CLOSED 20261007T060816Z |

## Log

- 20261007T055803Z OPENED by 2.0.0_SA_COO~D with 4 leg(s)
- 20261007T060816Z LEG L1 closed: origin PROD b06863fe (ls-remote read 06:05Z); merge parents ab3191d0 + 8ddfe409; parity diff vs origin/DEV 0 lines; tsc 
- 20261007T060816Z LEG L2 closed: run 37579269539 Deploy to Production conclusion success, matched by headSha b06863fe; jobs Build/Deploy to S3 + CloudFro
- 20261007T060816Z LEG L3 closed: portal-v2.1.203 peeled b06863fe equals origin/PROD b06863fe
- 20261007T060816Z LEG L4 closed: served https://d2n2nzpeqf34ge.cloudfront.net index Last-Modified 2026-10-07 06:03:45 GMT; marker data-input-provenance (
- 20261007T060817Z CLOSED -- all 4 legs proven
