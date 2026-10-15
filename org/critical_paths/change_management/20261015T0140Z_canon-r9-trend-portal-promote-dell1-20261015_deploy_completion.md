# Deploy Completion Record
**Date opened:** 2026-10-15T01:40:31.274906+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T014638Z
**Deploy:** ADHOC.canon-r9-trend-portal-promote: cand/dell1/mdpf-canon-global-trend-variant1-rf @15f7610285 to PROD only (row f411, client-facing, Andrew approved; DEV is not a leg)
**Authored by:** 0.4.0_DT_ClientPlatform~H1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD in Opal-Capital/portal fast-forwarded from 5d64641891 to the one-feature release head | ls-remote PROD hash | ls-remote origin refs/heads/PROD = c3b21a40e29f690922f442c085129f9ba85ce334 (push 5d646418..c3b21a40, read after push) | CLOSED 20261015T014312Z |
| L2 | verify | CI Deploy to Production on the PROD head by headSha, tag peeled | conclusion success, tag^{commit} = head | gh run 38667132776 Deploy to Production status=completed conclusion=success headSha=c3b21a40e29f; only workflow on that sha in the last 40 runs; tag portal-v2.1.223 peels to c3b21a40e29f690922f442c085129f9ba85ce334 (portal-v2.1.222 peels to 5d646418) | CLOSED 20261015T014638Z |
| L3 | verify | deployed bundle AFTER read: data-trend-composition, Carried forward (last known value), models held at one firm are in the total, data-asset-class-chip all present | string counts with denominator | served read of the deployed bundle (host = CloudFront alias in cloudfront-distribution.tf): 68 paths, 62 files read OK, 6 x HTTP 403. AFTER: data-trend-composition 1 file, 'Carried forward (last known value)' 1, 'models held at one firm are in the total' 1 (all ModelPortfolios-iAeFpD-x.js), data-asset-class-chip 1 (index-C_hwoorU.js), negative control 0. BEFORE (same crawl, 62 files): the three feature strings 0 of 62 (crawl reached ModelPortfolios-D6ihy19n.js, the old page chunk), chip 1. Page chunk hash moved D6ihy19n -> iAeFpD-x | CLOSED 20261015T014638Z |

## Log

- 20261015T014031Z OPENED by 0.4.0_DT_ClientPlatform~H1 with 3 leg(s)
- 20261015T014312Z LEG L1 closed: ls-remote origin refs/heads/PROD = c3b21a40e29f690922f442c085129f9ba85ce334 (push 5d646418..c3b21a40, read after push)
- 20261015T014638Z LEG L2 closed: gh run 38667132776 Deploy to Production status=completed conclusion=success headSha=c3b21a40e29f; only workflow on that 
- 20261015T014638Z LEG L3 closed: served read of the deployed bundle (host = CloudFront alias in cloudfront-distribution.tf): 68 paths, 62 files read OK, 
- 20261015T014638Z CLOSED -- all 3 legs proven
