# Deploy Completion Record
**Date opened:** 2026-10-16T17:43:19.772412+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R34G (cell AR-g-139): apply release 34g of the resident (PRD v0.22 items 1 and 2: the door asks yfinance first; opal_pricing ON with tiers estate and yfinance) on the resident host: three new S3 keys under ec2/investor-reporting-ycharts/resident/, new root /opt/irpt-resident/0485393f3a-r34g, one restart; rollback = r34f root kept (step 8); stage folder C:/dev/irpt-release-r34m (the order text says r34i; every sha256 verified against the order's values in r34m)
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | the before-read as root: running root r34f, security_resolution.py at its r34f value, the r34g root absent, library and wrapper unmoved, queue 0 0 | the P1 output |  | OPEN |
| D1 | s3-prefix | the tar, the package sums and the host script uploaded to three r34g keys that read 404 first; each read back with sha256 equal; VersionIds recorded | three VersionIds |  | OPEN |
| D2 | verify | the signed install sent as root: guard, sha256 guards on the host, r34f root and library kept, installed, polled, self-rollback on a failed start | the install output and rc |  | OPEN |
| V1 | verify | the after-reads: running root r34g active restarts 0, 1 of 1 member MATCH, sums 313 of 313, census 3 changed 0 added 0 removed, Opal imports, pool pin and opal_pricing ON, producer list unchanged, queue 0 0, no sign-in | the V1 output |  | OPEN |
| V2 | verify | V2 in the service's own environment: CONTROLS 4 of 4, BACKOFF OK, DOOR OK, PRICING OK, V2S OK SPY KEPT and ZQXWVK NOT_KEPT (two Yahoo calls and no other vendor call) | the V2 output and rc |  | OPEN |

## Log

- 20261016T174319Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
