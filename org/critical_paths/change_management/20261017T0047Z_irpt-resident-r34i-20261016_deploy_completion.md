# Deploy Completion Record
**Date opened:** 2026-10-17T00:47:13.968321+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R34I (cell AR-g-153): resident release r34i on the resident host: three new S3 objects under ec2/investor-reporting-ycharts/resident/, root /opt/irpt-resident/0485393f3a-r34i, bindings only (opal_pricing tiers estate and yfinance, ycharts tier out), one restart. Worktree union read 2026-10-17T00:4xZ: 100 worktrees, 2078 marker files, 6 naming the resident names: r31, r34b, r34e, yf-pydeps CLOSED, r34d ROLLED-BACK (terminal), and nfra-trnspt-a18 HELD-SOVEREIGN-GATED (names an IAM role refusal on the laptop device, not the host, unit or keys; not a stop).
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read on the resident host: running root r34h, bindings at their r34h value, r34i root absent, queue 0 0 | P1 STOP-READ-0 PASS and STOP-READ-2 PASS |  | OPEN |
| D1 | s3-prefix | three r34i objects (tar, sums, host script) under ec2/investor-reporting-ycharts/resident/, each 404 first, uploaded and read back sha256 equal | VersionIds recorded |  | OPEN |
| D2 | activation | signed install of r34i by install_r34.sh as root, one restart, rolls itself back on a failed start | install rc and output |  | OPEN |
| V1 | verify | after-reads: root r34i active restarts 0, 1 of 1 member MATCH, 314 of 314 sums, census 2 changed 0 added 0 removed, imports, pool pinned, queue 0 0 | each line as written |  | OPEN |
| V2 | verify | V2 read INSIDE the service environment: V2S OK SPY KEPT and ZQXWVK NOT_KEPT with the six sub-lines | V2 script rc 0 |  | OPEN |

## Log

- 20261017T004713Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
