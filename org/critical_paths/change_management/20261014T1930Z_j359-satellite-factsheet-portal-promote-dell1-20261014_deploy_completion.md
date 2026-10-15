# Deploy Completion Record
**Date opened:** 2026-10-14T19:30:15.410834+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T194007Z
**Deploy:** ADHOC.j359-satellite-factsheet-portal-promote: cand/dell1/satellite-factsheet-prod @6e69a05e43 to DEV then PROD (row de27, client-facing, Andrew approved)
**Authored by:** 0.4.0_DT_ClientPlatform~H1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | DEV in Opal-Capital/portal carries the merge of cand/dell1/satellite-factsheet-prod | ls-remote DEV hash | merge-forward result=MERGED pushed=yes; ls-remote origin refs/heads/DEV = 9de7c7e3227c321d45c2b6d3d3ccf72590b20710 (was 9e637fe51e) | CLOSED 20261014T193114Z |
| L2 | git | PROD in Opal-Capital/portal fast-forwarded to the chosen-set release head | ls-remote PROD hash | ls-remote origin refs/heads/PROD = 5ab67a651a626e7224de0a2cf03a2223f99dc15e (push fa10e758..5ab67a65, read after push) | CLOSED 20261014T193344Z |
| L3 | verify | CI Deploy to Production on the PROD head, listed by headSha | conclusion success | gh run 38624676588 Deploy to Production status=completed conclusion=success headSha=5ab67a651a62; only workflow on that sha in the last 40 runs; tag portal-v2.1.221 peels to 5ab67a651a626e7224de0a2cf03a2223f99dc15e | CLOSED 20261014T194006Z |
| L4 | verify | deployed bundle read for data-asset-class-chip and Trailing Returns | both strings present, bundle file count printed | served read of https://opalinvest.dev (alias from cloudfront-distribution.tf): index.html http=200 + crawl of its chunk graph = 68 paths, 62 read OK (6 x HTTP 403, string-literal names not assets); data-asset-class-chip in 1 file and Trailing Returns in 1 file, both index-TKcdTAwZ.js; negative control 0 of 68; both strings absent from old PROD source fa10e75861 and present at 5ab67a651a | CLOSED 20261014T194006Z |

## Log

- 20261014T193015Z OPENED by 0.4.0_DT_ClientPlatform~H1 with 4 leg(s)
- 20261014T193114Z LEG L1 closed: merge-forward result=MERGED pushed=yes; ls-remote origin refs/heads/DEV = 9de7c7e3227c321d45c2b6d3d3ccf72590b20710 (was 
- 20261014T193344Z LEG L2 closed: ls-remote origin refs/heads/PROD = 5ab67a651a626e7224de0a2cf03a2223f99dc15e (push fa10e758..5ab67a65, read after push)
- 20261014T194006Z LEG L3 closed: gh run 38624676588 Deploy to Production status=completed conclusion=success headSha=5ab67a651a62; only workflow on that 
- 20261014T194006Z LEG L4 closed: served read of https://opalinvest.dev (alias from cloudfront-distribution.tf): index.html http=200 + crawl of its chunk 
- 20261014T194007Z CLOSED -- all 4 legs proven
