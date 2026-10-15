# Deploy Completion Record
**Date opened:** 2026-10-15T22:30:30.909250+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T223736Z
**Deploy:** AMGT_RESAPP bn-3: cand/dell1/amgt-sa-team-estimate-mark @bb56c53d to PROD only (row a333, Opal-internal Security Analysis, CTO approved; DEV is not a leg)
**Authored by:** 0.4.0_DT_ClientPlatform~H1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD in Opal-Capital/portal fast-forwarded from e0b43076d9 to the one-feature release head | ls-remote PROD hash | ls-remote origin refs/heads/PROD = e0e69da7766d87719571d7e6c0ccf59bf65fcae9 (push e0b43076..e0e69da7, read after push) | CLOSED 20261015T223327Z |
| L2 | verify | CI Deploy to Production on the PROD head by headSha, tag peeled | conclusion success, tag^{commit} = head | gh run 38817882585 Deploy to Production status=completed conclusion=success headSha=e0e69da7766d; only workflow on that sha in the last 40 runs; tag portal-v2.1.227 peels to e0e69da7766d87719571d7e6c0ccf59bf65fcae9 (portal-v2.1.226 peels to e0b43076d9) | CLOSED 20261015T223557Z |
| L3 | verify | deployed bundle AFTER read: 'research team estimate' and data-model-team-mark present | string counts with denominator | served read of deployed bundle (opalinvest.dev, CloudFront alias): 68 paths, 62 files OK, 6 x HTTP 403. AFTER: 'research team estimate' 1 file, data-model-team-mark 1 file (both index-2eRxHeKz.js), negative control 0. BEFORE (same crawl, 62 files): both strings 0 of 62, controls fiscal_unresolved 1 (index-HfuxrtGC.js) and Key Figures 1. Chunk moved index-HfuxrtGC -> index-2eRxHeKz | CLOSED 20261015T223704Z |

## Log

- 20261015T223030Z OPENED by 0.4.0_DT_ClientPlatform~H1 with 3 leg(s)
- 20261015T223327Z LEG L1 closed: ls-remote origin refs/heads/PROD = e0e69da7766d87719571d7e6c0ccf59bf65fcae9 (push e0b43076..e0e69da7, read after push)
- 20261015T223557Z LEG L2 closed: gh run 38817882585 Deploy to Production status=completed conclusion=success headSha=e0e69da7766d; only workflow on that 
- 20261015T223704Z LEG L3 closed: served read of deployed bundle (opalinvest.dev, CloudFront alias): 68 paths, 62 files OK, 6 x HTTP 403. AFTER: 'research
- 20261015T223736Z CLOSED -- all 3 legs proven
