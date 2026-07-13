# Deploy Completion Record
**Date opened:** 2026-07-13T06:25:15.145959+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260713T062835Z
**Deploy:** OPAL_ASSETS R-A/R-B (PRD v0.2 AC7): basis+additive (SUM WHERE additive == certified headline BY CONSTRUCTION) + carried partner_aua total + AC7 WRITE GATE (refuse an internally-inconsistent partition) + partial->derived incomplete. Emitter 0.7.0_AE_CloudOps~A; guard 0.8.0_AE_CloudComp.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | emitter + reachability tests + 0.8.0's v0.2 guard committed & pushed CLOUD | commit hashes | emitter+reachability tests b8406458db802408414d6ae2bf47c1c478c6e278; 0.8.0's v0.2 guard f10d957a1; pushed CLOUD; 30/30 suite green | CLOSED 20260713T062835Z |
| L2 | s3-prefix | opal-assets-daily-emitter.zip rebuilt+uploaded+VERIFIED (head-object sha, NOT the script's success line -- the PS path silently no-ops) | sha256 head-object | head-object opal-assets/opal-assets-daily-emitter.zip -> ContentLength=14990 content-sha256=HyhmFMQqc4dWjNeZpvWtld28NEv4v1IDeF9xAep6YBo= == local build. NOT taken from build-and-upload's success line (its PS path silently no-ops -- the aws-shim finding); built+uploaded via bash aws and verified by head-object. | CLOSED 20260713T062835Z |
| L3 | verify | safe-apply + 0-diff re-plan | plan 'No changes' | safe-apply: 0 added, 1 changed, 0 destroyed; re-plan 'no differences, no changes needed' = 0-diff | CLOSED 20260713T062835Z |
| L4 | verify | EXERCISE deployed fn: SUM(value) WHERE additive == mdpf certified headline on the live partition | invoke + table read-back | invoke rc=200 -> {rows_written:28, base:14, ownership:12, total:2, partner_aua_total:1758111296.54, partner_aua_state:incomplete}. Live table: SUM(value) WHERE additive == mdpf certified headline on every partition (07-10 1,758,111,296.54; 07-08 1,746,701,801.55; 06-16 1,805,679,796.01). AC7 write-gate no-regression exercised: 5 live partitions WRITE, 0 blocked. | CLOSED 20260713T062835Z |
| L5 | verify | RE-BACKFILL all 19 partitions IN THIS LANDING (new attrs; a DDB filter on a MISSING attribute silently omits the row -> SUM WHERE additive would be true for only the newest day = a silently-wrong AUM number) | full-scan census, 0 rows missing additive | RE-BACKFILL DONE in-landing: 19 days / 532 rows. FULL-SCAN CENSUS: 532 rows, rows MISSING additive = 0, MISSING basis = 0. basis: partner_aua 57 (19x[2 contributors + 1 total]) \| partner_model_detail 133 \| partner_platform_view 19 \| etf_fund 95 \| etf_ownership 228. The additive contract is now TRUE FOR EVERY PARTITION, not just the newest. | CLOSED 20260713T062835Z |

## Log

- 20260713T062515Z OPENED by 0.7.0_AE_CloudOps~A with 5 leg(s)
- 20260713T062835Z LEG L1 closed: emitter+reachability tests b8406458db802408414d6ae2bf47c1c478c6e278; 0.8.0's v0.2 guard f10d957a1; pushed CLOUD; 30/30 s
- 20260713T062835Z LEG L2 closed: head-object opal-assets/opal-assets-daily-emitter.zip -> ContentLength=14990 content-sha256=HyhmFMQqc4dWjNeZpvWtld28NEv4
- 20260713T062835Z LEG L3 closed: safe-apply: 0 added, 1 changed, 0 destroyed; re-plan 'no differences, no changes needed' = 0-diff
- 20260713T062835Z LEG L4 closed: invoke rc=200 -> {rows_written:28, base:14, ownership:12, total:2, partner_aua_total:1758111296.54, partner_aua_state:in
- 20260713T062835Z LEG L5 closed: RE-BACKFILL DONE in-landing: 19 days / 532 rows. FULL-SCAN CENSUS: 532 rows, rows MISSING additive = 0, MISSING basis = 
- 20260713T062835Z CLOSED -- all 5 legs proven
