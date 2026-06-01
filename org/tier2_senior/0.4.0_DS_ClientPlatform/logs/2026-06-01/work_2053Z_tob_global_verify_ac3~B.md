# work_2053Z — TO-B global AC3 verify PASS; all-firm served; durability in AE's hands (DS~B)

## Tick class: SUBSTANTIVE (/work cron; global data-layer verify + handoffs)

## Global AC3 — data-layer verify PASS
AE re-emitted global per COO's approved -187 correction. Verified served json/portfolios/account-distribution.json:
- period 202605 (latest-funded, NOT anomalous 202606); gen 20:48Z; funded 6838, active 6840, total excluded_unfunded_count=2 (self-consistent).
- by_model: 5 models all carry the field, each excl=active-funded (2 in Long-Term Conservative).
- RECONCILE: SUM(by_model funded)=6838=total; SUM(excl)=2=total. 0.03% unfunded (matches 49F; global=49F-smartx scope).
=> All 3 firms now serve total + by_model excluded_unfunded_count: 49F=2, inflection=5, global=2. LD-0012-class cross-scope-subtraction defect eliminated for all firms.

## Root cause of the 7025@June mystery (AE confirmed)
The smartx-exporter EC2 daily run (~14:16Z) executes a DIVERGED OLD bundled copy (smartx-workspace/scripts/compute_account_distribution.py, max_period) — NOT data/smartx/scripts/ where the fix lives. The old code picked up a transient prematurely-valued June -> served 7025@202606. June is genuinely $0 at SmartX source (end-of-period; verified CSVs). So 7025 was spurious; 6838@May is correct.

## DURABILITY — in AE's hands (progressing)
- AC3 is data-correct NOW but at-risk on the next 14:16Z EC2 run until the EC2 docker is redeployed with the fix.
- AE ALREADY committed the global producer + ported the fix to the EC2-bundle copy: 9dfb66dcb "port TO-B latest-funded fix into the EC2-bundle producer copy (durable) + env-portable save_results." Durability fix in progress (AE lane).
- Remaining code-durability item: per-firm producer by_model delta still ` M` uncommitted (cfc278f38 was pre-by_model; served has by_model from the working-tree emit). Reminded AE (20:53) to commit it + port CURRENT state (incl by_model) to EC2.

## Handoffs (this tick)
- AE: data-layer verify PASS reported + the 2 follow-ups (commit per-firm by_model; port-with-by_model to EC2).
- DE: global ready for independent AC3 serving-verify (3rd firm) -> close AC3. Suggested verdict = PASS-with-durability-gate.
- CVO: global slice ready for cert (completes 3-firm set; certed inflection bf244cac1). Durability caveat noted.

## DS producer work on TO-B = COMPLETE
All 3 firms authored + emitted + self-verified. Remaining items are AE (per-firm by_model commit + EC2 redeploy), DE (global serving-verify), CVO (cert), RD (FE cutover to read excluded_unfunded_count). TO-B closes when EC2-durable + DE/CVO verify + RD cutover.

## Next
- Await DE/CVO global verify + AE EC2-deploy confirm. RAVC2 TO-B close when AC3 + durability land.
- pre-1/16: still parallel-paused for Andrew #3 (b3e627a75, CTO-concurred rec B).
