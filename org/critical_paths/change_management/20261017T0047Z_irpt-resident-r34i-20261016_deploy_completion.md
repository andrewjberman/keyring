# Deploy Completion Record
**Date opened:** 2026-10-17T00:47:13.968321+00:00
**Status:** ROLLED-BACK -- r34i rolled back to r34h the same session (V2S FAIL: SPY read NOT_KEPT LAST_CLOSE_NOT_FINITE in the service's own environment); P1, D1, D2, V1 proven; nothing stranded; r34i root and its three S3 objects kept; closed 20261017T005651Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34I (cell AR-g-153): resident release r34i on the resident host: three new S3 objects under ec2/investor-reporting-ycharts/resident/, root /opt/irpt-resident/0485393f3a-r34i, bindings only (opal_pricing tiers estate and yfinance, ycharts tier out), one restart. Worktree union read 2026-10-17T00:4xZ: 100 worktrees, 2078 marker files, 6 naming the resident names: r31, r34b, r34e, yf-pydeps CLOSED, r34d ROLLED-BACK (terminal), and nfra-trnspt-a18 HELD-SOVEREIGN-GATED (names an IAM role refusal on the laptop device, not the host, unit or keys; not a stop).
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read on the resident host: running root r34h, bindings at their r34h value, r34i root absent, queue 0 0 | P1 STOP-READ-0 PASS and STOP-READ-2 PASS | pre_read_r34.sh (sha256 c39094c5 equal) by Systems Manager AS ROOT: STOP-READ-0 PASS running root r34h, bindings MATCH, r34i root absent, library and wrapper unmoved, queue 0 0, sign-in baseline 0 | CLOSED 20261017T005649Z |
| D1 | s3-prefix | three r34i objects (tar, sums, host script) under ec2/investor-reporting-ycharts/resident/, each 404 first, uploaded and read back sha256 equal | VersionIds recorded | three r34i keys read 404 first; tar YQli0K.k.ztK68RqoCfuUB9KchVzBYcI, sums hadHCIV6UdrGD3SGJLshgrmjv6WRaPPJ, host script k69j1H2XIEl8x8Q8AwlEDFxkdSL4tPjO uploaded from C:/dev/irpt-release-r34s and read back sha256 equal | CLOSED 20261017T005650Z |
| D2 | activation | signed install of r34i by install_r34.sh as root, one restart, rolls itself back on a failed start | install rc and output | install_r34.sh (sha256 b54c42cd equal) AS ROOT: install rc=0 at 00:50:16Z, running root r34i active restarts 0, P2b member MATCH, sums 0 of 314 not OK, imports OK, queue 0 0, no sign-in | CLOSED 20261017T005650Z |
| V1 | verify | after-reads: root r34i active restarts 0, 1 of 1 member MATCH, 314 of 314 sums, census 2 changed 0 added 0 removed, imports, pool pinned, queue 0 0 | each line as written | running root r34i active; members 1 of 1 MATCH; sums 314 of 314; census package scope 2 changed 0 added 0 removed; pool pinned equal, pricing estate yfinance only, budget 6 by 390, producer list unchanged; queue 0 0 | CLOSED 20261017T005650Z |
| V2 | verify | V2 read INSIDE the service environment: V2S OK SPY KEPT and ZQXWVK NOT_KEPT with the six sub-lines | V2 script rc 0 | V2 FAILED (v2_service_env_r34i.sh sha256 4e2e8981 equal, AS ROOT, command ec63433b): six sub-lines OK but SPY read NOT_KEPT LAST_CLOSE_NOT_FINITE (rows 22) so V2S FAIL, rc 1; ROLLED BACK the same session: rollback_r34.sh rc 0, r34h running since 00:53:24Z restarts 0, bindings at the P1 value MATCH, queue 0 0, no sign-in; r34i root and three S3 objects kept | CLOSED 20261017T005650Z |

## Log

- 20261017T004713Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261017T005649Z LEG P1 closed: pre_read_r34.sh (sha256 c39094c5 equal) by Systems Manager AS ROOT: STOP-READ-0 PASS running root r34h, bindings MATCH, 
- 20261017T005650Z LEG D1 closed: three r34i keys read 404 first; tar YQli0K.k.ztK68RqoCfuUB9KchVzBYcI, sums hadHCIV6UdrGD3SGJLshgrmjv6WRaPPJ, host script
- 20261017T005650Z LEG D2 closed: install_r34.sh (sha256 b54c42cd equal) AS ROOT: install rc=0 at 00:50:16Z, running root r34i active restarts 0, P2b memb
- 20261017T005650Z LEG V1 closed: running root r34i active; members 1 of 1 MATCH; sums 314 of 314; census package scope 2 changed 0 added 0 removed; pool 
- 20261017T005650Z LEG V2 closed: V2 FAILED (v2_service_env_r34i.sh sha256 4e2e8981 equal, AS ROOT, command ec63433b): six sub-lines OK but SPY read NOT_K
- 20261017T005651Z CLOSED -- all 5 legs proven
