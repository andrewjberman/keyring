# Deploy Completion Record
**Date opened:** 2026-10-16T02:47:27.659493+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T025751Z
**Deploy:** AMGT_RESAPP bo-2: cand/dell1/amgt-sa-withheld-reasons @01e06415f17f to PROD only (row 9365, Opal-internal Security Analysis, CTO approved; DEV is not a leg)
**Authored by:** 0.4.0_DT_ClientPlatform~H1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD in Opal-Capital/portal fast-forwarded from e0e69da7766d to the one-feature release head | ls-remote PROD hash | ls-remote origin refs/heads/PROD = ab2c43657e7b7bbfd528ec5f06c6ef3f0b45068b (push e0e69da7..ab2c4365, read after push) | CLOSED 20261016T025326Z |
| L2 | verify | CI Deploy to Production on the PROD head by headSha, tag peeled | conclusion success, tag^{commit} = head | gh run 38842687915 Deploy to Production status=completed conclusion=success headSha=ab2c43657e7b; only workflow on that sha in the last 40 runs; tag portal-v2.1.228 peels to ab2c43657e7b7bbfd528ec5f06c6ef3f0b45068b (portal-v2.1.227 peels to e0e69da7766d) | CLOSED 20261016T025551Z |
| L3 | verify | deployed bundle AFTER read: withheld-reasons strings present | string counts with denominator | served read of deployed bundle (opalinvest.dev, CloudFront alias): 68 paths, 62 files OK, 6 x HTTP 403. AFTER: data-model-summary-pe-reason 1 file, 'P/E not shown: ' 1 file, 'research team estimate' 1 file (all index-C3r9t0Ge.js), negative control 0. BEFORE (same crawl, 62 files): data-model-summary-pe-reason 0, 'P/E not shown: ' 0, 'research team estimate' 1 (index-2eRxHeKz.js), Key Figures 1. Chunk moved index-2eRxHeKz -> index-C3r9t0Ge | CLOSED 20261016T025751Z |

## Log

- 20261016T024727Z OPENED by 0.4.0_DT_ClientPlatform~H1 with 3 leg(s)
- 20261016T025326Z LEG L1 closed: ls-remote origin refs/heads/PROD = ab2c43657e7b7bbfd528ec5f06c6ef3f0b45068b (push e0e69da7..ab2c4365, read after push)
- 20261016T025551Z LEG L2 closed: gh run 38842687915 Deploy to Production status=completed conclusion=success headSha=ab2c43657e7b; only workflow on that 
- 20261016T025751Z LEG L3 closed: served read of deployed bundle (opalinvest.dev, CloudFront alias): 68 paths, 62 files OK, 6 x HTTP 403. AFTER: data-mode
- 20261016T025751Z CLOSED -- all 3 legs proven
