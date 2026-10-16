# Deploy Completion Record
**Date opened:** 2026-10-16T17:43:19.772412+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T174904Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34G (cell AR-g-139): apply release 34g of the resident (PRD v0.22 items 1 and 2: the door asks yfinance first; opal_pricing ON with tiers estate and yfinance) on the resident host: three new S3 keys under ec2/investor-reporting-ycharts/resident/, new root /opt/irpt-resident/0485393f3a-r34g, one restart; rollback = r34f root kept (step 8); stage folder C:/dev/irpt-release-r34m (the order text says r34i; every sha256 verified against the order's values in r34m)
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | the before-read as root: running root r34f, security_resolution.py at its r34f value, the r34g root absent, library and wrapper unmoved, queue 0 0 | the P1 output | SSM command 0bec64d2 as root, Success rc 0: P1 STOP-READ-0 PASS running root r34f; security_resolution.py at its r34f value MATCH; r34g root absent; library and wrapper unmoved; queue 0 0; no sign-in baseline 0 | CLOSED 20261016T174902Z |
| D1 | s3-prefix | the tar, the package sums and the host script uploaded to three r34g keys that read 404 first; each read back with sha256 equal; VersionIds recorded | three VersionIds | three r34g keys read 404 first, then uploaded and read back equal by VersionId: tar AJ4VljOM.. (1122209 bytes), sums cSrQPsJ_.., host script QBVj5vLD..; sha256 equal to the order's values | CLOSED 20261016T174903Z |
| D2 | verify | the signed install sent as root: guard, sha256 guards on the host, r34f root and library kept, installed, polled, self-rollback on a failed start | the install output and rc | signed install as root, SSM command 528c6f4c, Success rc 0: guard passed, install script and sums sha256 verified on the host, package sums 313 OK, install rc=0, running root r34g, MainPID 1114077, restarts 0; r34f root and library kept | CLOSED 20261016T174903Z |
| V1 | verify | the after-reads: running root r34g active restarts 0, 1 of 1 member MATCH, sums 313 of 313, census 3 changed 0 added 0 removed, Opal imports, pool pin and opal_pricing ON, producer list unchanged, queue 0 0, no sign-in | the V1 output | running root r34g active restarts 0; member security_resolution.py MATCH 1 of 1; sums 313 of 313; package census 3 changed 0 added 0 removed; imports OK (resident_worker per the install's own P4); pool pin equal; opal_pricing enabled true tiers estate and yfinance; producer list unchanged; queue 0 0; no sign-in | CLOSED 20261016T174903Z |
| V2 | verify | V2 in the service's own environment: CONTROLS 4 of 4, BACKOFF OK, DOOR OK, PRICING OK, V2S OK SPY KEPT and ZQXWVK NOT_KEPT (two Yahoo calls and no other vendor call) | the V2 output and rc | SSM command 79b82cc8 as root, Success rc 0, in the service's own environment: V2S CONTROLS OK 4 of 4, BACKOFF OK, DOOR OK, PRICING OK, V2S OK SPY KEPT and ZQXWVK NOT_KEPT; transient unit rc 0 | CLOSED 20261016T174904Z |

## Log

- 20261016T174319Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261016T174902Z LEG P1 closed: SSM command 0bec64d2 as root, Success rc 0: P1 STOP-READ-0 PASS running root r34f; security_resolution.py at its r34f va
- 20261016T174903Z LEG D1 closed: three r34g keys read 404 first, then uploaded and read back equal by VersionId: tar AJ4VljOM.. (1122209 bytes), sums cSr
- 20261016T174903Z LEG D2 closed: signed install as root, SSM command 528c6f4c, Success rc 0: guard passed, install script and sums sha256 verified on the
- 20261016T174903Z LEG V1 closed: running root r34g active restarts 0; member security_resolution.py MATCH 1 of 1; sums 313 of 313; package census 3 chang
- 20261016T174904Z LEG V2 closed: SSM command 79b82cc8 as root, Success rc 0, in the service's own environment: V2S CONTROLS OK 4 of 4, BACKOFF OK, DOOR O
- 20261016T174904Z CLOSED -- all 5 legs proven
