# Deploy Completion Record
**Date opened:** 2026-10-20T07:28:14.962984+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T073144Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34M v2: resident r34l -> r34m (package attached at READY, the submission schema admits commentary_requested); six members move
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read: running root r34l, r34m root absent, queue 0 0 | P1 STOP-READ-0 PASS | P1 STOP-READ-0 PASS 2026-10-20T07:28:29Z: running root r34l, four members at r34l values MATCH, r34m root absent, queue 0 0 | CLOSED 20261020T072900Z |
| D1 | s3-prefix | three r34m keys under ec2/investor-reporting-ycharts/resident/ | three VersionIds read back equal | three keys uploaded, read back equal: tar 66pgS9ySk.mK6MaSco.iuZ31TQ1DrwCo, sums de7rM.AWRsIR.XxBExwt1X1FnyD0Q8ue, script Yt7hq6LsQEgzefaMVZRqK2Q_sQbeqXMs | CLOSED 20261020T072927Z |
| D2 | activation | signed install on the resident host (root /opt/irpt-resident/0485393f3a-r34m) | install output, unit active restarts 0 | install rc=0 at 2026-10-20T07:30:13Z; unit active since 07:29:48Z restarts 0; root /opt/irpt-resident/0485393f3a-r34m; sums 316 of 316; members MATCH | CLOSED 20261020T073039Z |
| V1 | verify | after-reads: members MATCH, sums 316 of 316, census 6 changed | printed counts | running root r34m active restarts 0; members MATCH (4 of 4); sums 316 of 316 OK; census 6 changed 0 added 0 removed (package scope); pool pinned; pricing estate yfinance ycharts; budget 6/390; queue 0 0; no sign-in | CLOSED 20261020T073144Z |
| V2 | verify | V2 inside the service environment | V2S OK SPY KEPT and ZQXWVK NOT_KEPT | V2S OK SPY KEPT and ZQXWVK NOT_KEPT; controls 4 of 4; backoff, door, pricing, budget, tier OK; rc 0 at 2026-10-20T07:31Z | CLOSED 20261020T073144Z |

## Log

- 20261020T072814Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261020T072900Z LEG P1 closed: P1 STOP-READ-0 PASS 2026-10-20T07:28:29Z: running root r34l, four members at r34l values MATCH, r34m root absent, queue 
- 20261020T072927Z LEG D1 closed: three keys uploaded, read back equal: tar 66pgS9ySk.mK6MaSco.iuZ31TQ1DrwCo, sums de7rM.AWRsIR.XxBExwt1X1FnyD0Q8ue, scrip
- 20261020T073039Z LEG D2 closed: install rc=0 at 2026-10-20T07:30:13Z; unit active since 07:29:48Z restarts 0; root /opt/irpt-resident/0485393f3a-r34m; s
- 20261020T073144Z LEG V1 closed: running root r34m active restarts 0; members MATCH (4 of 4); sums 316 of 316 OK; census 6 changed 0 added 0 removed (pac
- 20261020T073144Z LEG V2 closed: V2S OK SPY KEPT and ZQXWVK NOT_KEPT; controls 4 of 4; backoff, door, pricing, budget, tier OK; rc 0 at 2026-10-20T07:31Z
- 20261020T073144Z CLOSED -- all 5 legs proven
