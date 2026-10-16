# Deploy Completion Record
**Date opened:** 2026-10-16T14:16:05.524823+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T142335Z
**Deploy:** AMGT_RESAPP gx-2: cand/dell1/aifill-provenance @31337460fcf7 + aifill-provenance-wording-v2 @9e13d8e1e933 to PROD only (rows 6f4b, 5cf5, Opal-internal Security Analysis, CTO approved; DEV is not a leg)
**Authored by:** 0.4.0_DT_ClientPlatform~H1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD in Opal-Capital/portal fast-forwarded from 64f9dba10528 to the two-feature release head | ls-remote PROD hash | ls-remote origin refs/heads/PROD = fa21a303d87271a1e2d60c514d13501d71f9f020 (push 64f9dba1..fa21a303, read after push) | CLOSED 20261016T142010Z |
| L2 | verify | CI Deploy to Production on the PROD head by headSha, tag peeled | conclusion success, tag^{commit} = head | gh run 38914865382 Deploy to Production status=completed conclusion=success headSha=fa21a303d872; only workflow on that sha in the last 40 runs; tag portal-v2.1.232 peels to fa21a303d87271a1e2d60c514d13501d71f9f020 (portal-v2.1.231 peels to 64f9dba10528) | CLOSED 20261016T142215Z |
| L3 | verify | deployed bundle AFTER read: AI-written row strings present | string counts with denominator | served read of deployed bundle (opalinvest.dev, CloudFront alias): 68 paths, 62 files OK, 6 x HTTP 403. AFTER: 'AI-written blocks' 1 file, 'cites a web search made when it was written' 1 file, 'cite web searches made when they were written' 1 file (all index-CJ0Jo9Y0.js), negative control 0. BEFORE (same crawl, 62 files): 'AI-written blocks' 0, both web-search wordings 0, controls data-provenance-row 1 (index-1lAjfLu8.js) and Key Figures 1. Chunk moved index-1lAjfLu8 -> index-CJ0Jo9Y0 | CLOSED 20261016T142335Z |

## Log

- 20261016T141605Z OPENED by 0.4.0_DT_ClientPlatform~H1 with 3 leg(s)
- 20261016T142010Z LEG L1 closed: ls-remote origin refs/heads/PROD = fa21a303d87271a1e2d60c514d13501d71f9f020 (push 64f9dba1..fa21a303, read after push)
- 20261016T142215Z LEG L2 closed: gh run 38914865382 Deploy to Production status=completed conclusion=success headSha=fa21a303d872; only workflow on that 
- 20261016T142335Z LEG L3 closed: served read of deployed bundle (opalinvest.dev, CloudFront alias): 68 paths, 62 files OK, 6 x HTTP 403. AFTER: 'AI-writt
- 20261016T142335Z CLOSED -- all 3 legs proven
