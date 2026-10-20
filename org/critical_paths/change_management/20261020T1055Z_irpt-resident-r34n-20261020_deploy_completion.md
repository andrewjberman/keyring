# Deploy Completion Record
**Date opened:** 2026-10-20T10:55:23.151558+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T110028Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34N: resident r34m -> r34n (packager api_base through the CloudFront alias); two members change (SHA256SUMS, reports/resident_bindings.json)
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read: running root r34m, r34n root absent, queue 0 0 | P1 STOP-READ-0 PASS | P1 STOP-READ-0 PASS 2026-10-20T10:55:50Z: running root r34m active since 07:29:48Z restarts 0, r34n root absent, library and wrapper unmoved, queue 0 0, sign-in baseline 0; open-deploys denominator 45 worktrees 163 blobs: 5 resident-naming entries, all closed or rolled back and stale copies only | CLOSED 20261020T105607Z |
| D1 | s3-prefix | three r34n keys under ec2/investor-reporting-ycharts/resident/ | three VersionIds read back equal | three keys uploaded, read back equal: tar sMeT5xmn6vbchBmcn9WJ27UMI.ueG_SM, sums wyTyATYCxbQFxZ0ipiG3Czv1p0mjQaoI, script RKAF0_SLDjlcQRSFABjbd3DlZwaj2x_a; each key read 404 first | CLOSED 20261020T105701Z |
| D2 | activation | signed install on the resident host (root /opt/irpt-resident/0485393f3a-r34n) | install output, unit active restarts 0 | install rc=0 at 2026-10-20T10:58:00Z; unit active since 10:57:35Z restarts 0; root /opt/irpt-resident/0485393f3a-r34n; sums 316 members OK; queue 0 0; no sign-in | CLOSED 20261020T105815Z |
| V1 | verify | after-reads: members MATCH, sums 316 of 316, census 2 changed | printed counts | running root r34n active restarts 0; members 2 of 2 MATCH (install table); sums 316 of 316 OK; census package scope 2 changed (SHA256SUMS, reports/resident_bindings.json) 0 added 0 removed, library 0, bytecode named separately; packager api_base alias secret unchanged, 18 other binding keys equal; pool pinned bf047533, pricing enabled estate yfinance ycharts, budget calls 6 window_s 390, producer list unchanged; queue 0 0; no sign-in | CLOSED 20261020T105945Z |
| V2 | verify | V2 inside the service environment | V2S OK SPY KEPT and ZQXWVK NOT_KEPT | V2S OK SPY KEPT and ZQXWVK NOT_KEPT; controls 4 of 4; backoff, door, pricing, budget, tier OK; rc 0 at 2026-10-20T11:00Z, root r34n | CLOSED 20261020T110028Z |

## Log

- 20261020T105523Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261020T105607Z LEG P1 closed: P1 STOP-READ-0 PASS 2026-10-20T10:55:50Z: running root r34m active since 07:29:48Z restarts 0, r34n root absent, library
- 20261020T105701Z LEG D1 closed: three keys uploaded, read back equal: tar sMeT5xmn6vbchBmcn9WJ27UMI.ueG_SM, sums wyTyATYCxbQFxZ0ipiG3Czv1p0mjQaoI, scrip
- 20261020T105815Z LEG D2 closed: install rc=0 at 2026-10-20T10:58:00Z; unit active since 10:57:35Z restarts 0; root /opt/irpt-resident/0485393f3a-r34n; s
- 20261020T105945Z LEG V1 closed: running root r34n active restarts 0; members 2 of 2 MATCH (install table); sums 316 of 316 OK; census package scope 2 ch
- 20261020T110028Z LEG V2 closed: V2S OK SPY KEPT and ZQXWVK NOT_KEPT; controls 4 of 4; backoff, door, pricing, budget, tier OK; rc 0 at 2026-10-20T11:00Z
- 20261020T110028Z CLOSED -- all 5 legs proven
