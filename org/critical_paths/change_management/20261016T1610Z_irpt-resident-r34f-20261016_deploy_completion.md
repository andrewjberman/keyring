# Deploy Completion Record
**Date opened:** 2026-10-16T16:10:55.791954+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T161727Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34F (cell AR-g-132): apply release 34f of the resident (the bounded WAF back-off, 150/300/450 s for a :WAF_CHALLENGE resolve-hop retry) on the resident host: three new S3 keys under ec2/investor-reporting-ycharts/resident/, new root /opt/irpt-resident/0485393f3a-r34f, one restart; rollback = r34e root kept (step 8)
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | the before-read as root: running root r34e (P1 STOP-READ-0 PASS), the changed member at its r34e value, the r34f root absent, library and wrapper unmoved, queue 0 0 | the P1 output | SSM command 42d03703 as root, Success rc 0: P1 STOP-READ-0 PASS running root r34e; worker at its r34e value MATCH; r34f root absent; library and wrapper unmoved; queue 0 0; no sign-in baseline 0 | CLOSED 20261016T161725Z |
| D1 | s3-prefix | the tar, the package sums and the host script uploaded to three r34f keys that read 404 first; each read back with sha256 equal; VersionIds recorded | three VersionIds | three r34f keys read 404 first, then uploaded and read back equal by VersionId: tar 7UMqCueX.. (1121542 bytes), sums 3jUyAjPQ.., host script Lm32w22o..; sha256 equal to the order's values | CLOSED 20261016T161726Z |
| D2 | verify | the signed install sent as root: fetched by key with the sha256 guard, r34e root and library kept, installed, polled, self-rollback on a failed start | the install output and rc | signed install sent as root, SSM command a8b47ab0, Success rc 0: guard passed, install script and sums sha256 verified on the host, package sums 313 OK, install rc=0, running root r34f, MainPID 1110572, restarts 0; r34e root and library kept | CLOSED 20261016T161726Z |
| V1 | verify | the after-reads: running root r34f active restarts 0, 1 of 1 member MATCH, sums 313 of 313, census 3 changed 0 added 0 removed, Opal imports, pool pin and opal_pricing off, queue 0 0 no sign-in | the V1 output | running root r34f active restarts 0; member resident_worker.py MATCH 1 of 1; sums 313 of 313; census package scope 3 changed 0 added 0 removed; imports OK (resident_worker per the install's own P4); pool pin equal and opal_pricing off; producer list unchanged; queue 0 0; no sign-in | CLOSED 20261016T161726Z |
| V2 | verify | V2 in the service's own environment: V2S CONTROLS OK 4 of 4, V2S BACKOFF OK, V2S OK SPY KEPT and ZQXWVK NOT_KEPT (two Yahoo calls and no other vendor call) | the V2 output and rc | SSM command 91fd9a24 as root, Success rc 0, in the service's own environment (ec2-user, r34f workdir, python3.12): V2S CONTROLS OK 4 of 4, V2S BACKOFF OK (150, 300, 450 s for the WAF code, 60 s flat), V2S OK SPY KEPT and ZQXWVK NOT_KEPT; transient unit rc 0 | CLOSED 20261016T161726Z |

## Log

- 20261016T161055Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261016T161725Z LEG P1 closed: SSM command 42d03703 as root, Success rc 0: P1 STOP-READ-0 PASS running root r34e; worker at its r34e value MATCH; r34f 
- 20261016T161726Z LEG D1 closed: three r34f keys read 404 first, then uploaded and read back equal by VersionId: tar 7UMqCueX.. (1121542 bytes), sums 3jU
- 20261016T161726Z LEG D2 closed: signed install sent as root, SSM command a8b47ab0, Success rc 0: guard passed, install script and sums sha256 verified o
- 20261016T161726Z LEG V1 closed: running root r34f active restarts 0; member resident_worker.py MATCH 1 of 1; sums 313 of 313; census package scope 3 cha
- 20261016T161726Z LEG V2 closed: SSM command 91fd9a24 as root, Success rc 0, in the service's own environment (ec2-user, r34f workdir, python3.12): V2S C
- 20261016T161727Z CLOSED -- all 5 legs proven
