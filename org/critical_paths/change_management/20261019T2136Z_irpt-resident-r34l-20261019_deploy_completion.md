# Deploy Completion Record
**Date opened:** 2026-10-19T21:36:09.958387+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261019T214323Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34L: resident r34k -> r34l (report sections without value dropped and counted; pricing as-of at the trading-calendar frontier)
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read: running root r34k, r34l root absent, queue 0 0 | P1 STOP-READ-0 PASS | P1 STOP-READ-0 PASS 2026-10-19T21:36:58Z: running root r34k, members MATCH, r34l root absent, queue 0 0 | CLOSED 20261019T213743Z |
| D1 | s3-prefix | three r34l keys under ec2/investor-reporting-ycharts/resident/ | three VersionIds read back equal | three keys uploaded, read back equal: tar VersionId RrJAiRC1aZ1ZfrCutbpY.PdogrH4TjPi, sums ZDHK94f2HAAxT_RnsvfG8Ak0XlqyV3Rt, script P.bj3EI39gF3IJ8zQ0Ee2BDIKWQ65IrK | CLOSED 20261019T213808Z |
| D2 | activation | signed install on the resident host (root /opt/irpt-resident/0485393f3a-r34l) | install output, unit active restarts 0 | install rc=0 at 2026-10-19T21:39:25Z; unit active since 21:39:00Z restarts 0; root /opt/irpt-resident/0485393f3a-r34l | CLOSED 20261019T213951Z |
| V1 | verify | after-reads: members MATCH, sums 316 of 316, census 4 changed | printed counts | running root r34l active restarts 0; members 2 of 2 MATCH; sums 316 of 316 OK; census 4 changed 0 added 0 removed (package scope); pool pinned; pricing estate yfinance ycharts; budget 6/390; queue 0 0; no sign-in | CLOSED 20261019T214322Z |
| V2 | verify | V2 inside the service environment | V2S OK SPY KEPT and ZQXWVK NOT_KEPT | V2S OK SPY KEPT and ZQXWVK NOT_KEPT; controls 4 of 4; backoff, door, pricing, budget, tier OK; rc 0 at 2026-10-19T21:42Z | CLOSED 20261019T214322Z |

## Log

- 20261019T213609Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261019T213743Z LEG P1 closed: P1 STOP-READ-0 PASS 2026-10-19T21:36:58Z: running root r34k, members MATCH, r34l root absent, queue 0 0
- 20261019T213808Z LEG D1 closed: three keys uploaded, read back equal: tar VersionId RrJAiRC1aZ1ZfrCutbpY.PdogrH4TjPi, sums ZDHK94f2HAAxT_RnsvfG8Ak0XlqyV
- 20261019T213951Z LEG D2 closed: install rc=0 at 2026-10-19T21:39:25Z; unit active since 21:39:00Z restarts 0; root /opt/irpt-resident/0485393f3a-r34l
- 20261019T214322Z LEG V1 closed: running root r34l active restarts 0; members 2 of 2 MATCH; sums 316 of 316 OK; census 4 changed 0 added 0 removed (packa
- 20261019T214322Z LEG V2 closed: V2S OK SPY KEPT and ZQXWVK NOT_KEPT; controls 4 of 4; backoff, door, pricing, budget, tier OK; rc 0 at 2026-10-19T21:42Z
- 20261019T214323Z CLOSED -- all 5 legs proven
