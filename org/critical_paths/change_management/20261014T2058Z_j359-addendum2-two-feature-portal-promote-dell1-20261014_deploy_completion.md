# Deploy Completion Record
**Date opened:** 2026-10-14T20:58:21.885105+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T210631Z
**Deploy:** ADHOC.j359-addendum2-footnote-deletion-promote: ONE PROD release, two features (satellite-returns-method @714f8e48c8 client-facing, trsb-history-excel-download @040b152f41bf opal-internal)
**Authored by:** 0.4.0_DT_ClientPlatform~H1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | DEV carries the merge of cand/dell1/satellite-returns-method (TRSB already in DEV) | ls-remote DEV hash | merge-forward result=MERGED pushed=yes; ls-remote origin refs/heads/DEV = e578b378d332ad1505018be3801466dac7aeeade (was bbad56e354) | CLOSED 20261014T205903Z |
| L2 | git | PROD fast-forwarded from 5ab67a651a62 to the two-feature release head | ls-remote PROD hash | ls-remote origin refs/heads/PROD = 5d64641891207b68998973e7c82c0dd0260b4dab (push 5ab67a65..5d646418, read after push) | CLOSED 20261014T210223Z |
| L3 | verify | CI Deploy to Production on the PROD head by headSha, tag peeled | conclusion success, tag^{commit} = head | gh run 38637040693 Deploy to Production status=completed conclusion=success headSha=5d6464189120; only workflow on that sha in the last 40 runs; tag portal-v2.1.222 peels to 5d64641891207b68998973e7c82c0dd0260b4dab (portal-v2.1.221 peels to 5ab67a65) | CLOSED 20261014T210631Z |
| L4 | verify | deployed bundle AFTER read: holdings at today and left out for lack of one absent; chip, Trailing Returns, download_url present | string counts with denominator | served read of the deployed bundle (host = CloudFront alias in cloudfront-distribution.tf): 68 paths visited, 62 files read OK, 6 x HTTP 403. AFTER: 'holdings at today' 0 files, 'left out for lack of one' 0, 'data-asset-class-chip' 1 (index-i8K0Vhin.js), 'Trailing Returns' 1, 'download_url' 1 (index-JYduzYBC.js), 'presigned_url' 0, negative control 0. BEFORE (same crawl, 62 files): holdings at today 1, left out for lack of one 1, chip 1, Trailing Returns 1, download_url 0. Main bundle hash moved index-TKcdTAwZ -> index-i8K0Vhin | CLOSED 20261014T210631Z |

## Log

- 20261014T205821Z OPENED by 0.4.0_DT_ClientPlatform~H1 with 4 leg(s)
- 20261014T205903Z LEG L1 closed: merge-forward result=MERGED pushed=yes; ls-remote origin refs/heads/DEV = e578b378d332ad1505018be3801466dac7aeeade (was 
- 20261014T210223Z LEG L2 closed: ls-remote origin refs/heads/PROD = 5d64641891207b68998973e7c82c0dd0260b4dab (push 5ab67a65..5d646418, read after push)
- 20261014T210631Z LEG L3 closed: gh run 38637040693 Deploy to Production status=completed conclusion=success headSha=5d6464189120; only workflow on that 
- 20261014T210631Z LEG L4 closed: served read of the deployed bundle (host = CloudFront alias in cloudfront-distribution.tf): 68 paths visited, 62 files r
- 20261014T210631Z CLOSED -- all 4 legs proven
