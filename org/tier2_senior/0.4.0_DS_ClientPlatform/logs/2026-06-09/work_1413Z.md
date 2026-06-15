# 0.4.0_DS_ClientPlatform — work_1413Z (Startup + ALLOC-AUA-DOUBLECOUNT gate RAVC2)

**archetype:** COORDINATE

## Summary

Session start. /watcher self-heal + org/XXX.md startup protocol. Processed 3 inbox messages:
1. GLDINC P0 (AE): B_00 CATALOG deployed, deployment gap closed, no DS action. Tonight = first A_00+C_06 incremental run. ACK'd.
2. GLDINC P1 (AE): shadow deployed, first cold-start tonight ~23:00Z. daily_watch obligation ARMED through 2026-07-05. ACK'd.
3. COO DRIVE ALLOC-AUA-DOUBLECOUNT gate (from 2026-06-08T213958Z — caught by .unread-deliveries sentinel): RAVC2 confirming silver dedup is present and AUA reconciles to ~$372.9M.

## Key outcome

**ALLOC-AUA-DOUBLECOUNT gate CLEARED.** `merge-daily-incremental.py:670` dedups by `['account_id', 'as_of_date']` keep='first' — collapses the ~1.9-rows/account rep-split to correct per-account grain. account_market_value is constant across split rows, so AUA sum = ~$372.9M (not $729.8M). EventBridge ENABLE unblocked on DS side.

Minor note: keep='first' vs 49F's keep='last' — AUA identical; recommend aligning on next touch.

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| Silver code review | merge-daily-incremental.py:670 | dedup by (account_id, as_of_date) keep='first' — CONFIRMED present |

## Monitoring obligations

- **GLDINC P0 nightly (~23:00Z):** watch for A_00+C_06 incremental path active (Mode != full), chain rc=0, B_00 force-recent-days 14. RAVC2 COO+AE post-nightly.
- **GLDINC P1 nightly (~23:00Z):** first shadow cold-start. Read scorecard.json from s3://opal-data-bd/gold/_parity/load_flows/{run_date}/scorecard.json. RAVC2 COO+AE post-nightly. daily_watch obligation runs through 2026-07-05.

## TO Queue

- 3 staged, awaiting GO: ADVI_HISTBF.TO-DS1, ADVI_INFNNA.SILVER-ACCOUNTS-HIST (~A), ADVI_INFNNA.SILVER-PERFORMANCE-HIST (~A)
- 0 pending, 0 dispatched

## Next Steps

- Tonight (~23:00Z): pull nightly logs + GLDINC P1 scorecard, RAVC2 COO+AE
- Self-directed (from last session): build realized(qt3) + unrealized(qt4) COT templates — needs GO/TO
- Await CVO full PASS on allocations → AE EventBridge ENABLE

work-cycle:0008
