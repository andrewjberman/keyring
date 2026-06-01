# work_2109Z — §2 per-firm regen-path: MANUAL-ONLY finding + rec (DS~B)

## Tick class: SUBSTANTIVE (watcher-delivered COO §2 dispatch; investigation + RAVC2)

## §2 question (COO/CTO blast-radius)
How does the per-firm (49F/inf) bell-curve `json/mdpf/{firm}/account-distribution.json` regenerate recurringly? Global auto-regenerates via the daily DAG; per-firm producer `compute_per_firm_account_distribution.py` is canon-only + not obviously in the DAG.

## FINDING (definitive): per-firm producer is MANUAL-ONLY
Evidence:
- `compute_per_firm_account_distribution.py` has ZERO references under `infra/` (grep) — NOT in the EC2 bundle (`infra/aws/ec2/smartx-exporter/smartx-workspace/scripts/`), NOT in any Lambda (`infra/aws/lambda/smartx_ingestion_pipeline/`).
- The smartx daily DAG orchestrator `run_smartx_pipeline.py` calls ONLY `compute_account_distribution.py` (line 187 = GLOBAL) — explicit script list (not wildcard), so per-firm isn't picked up implicitly.
- No cron/scheduler/SSM references it.
=> per-firm 49F/inflection bell-curve was emitted MANUALLY (created 5/29 + re-emitted this session). Will NOT auto-refresh as new months value at period-end. Per-firm analog of the global daily-run gap AE just fixed.

Note: 3 copies of the smartx pipeline exist — canon (`data/smartx/scripts/`), EC2 bundle (`infra/aws/ec2/smartx-exporter/smartx-workspace/`), Lambda (`infra/aws/lambda/smartx_ingestion_pipeline/`). compute_per_firm is in NONE of the automation copies.

## RECOMMENDATION: (i) add to daily DAG + EC2 bundle
NOT (ii) documented-manual. It's a LIVE Andrew-facing artifact (same class as global) -> should auto-refresh; manual-only = the silent-drift failure class we just fixed. My latest-funded-period selection makes daily-run SAFE (won't regress on month-start $0 shells). Fold into the SAME EC2 redeploy AE is doing for global.

Implementation note for AE (owns DAG/bundle): compute_per_firm builds BOTH firms — 49F (smartx_allocations, same as global) + inflection (DIFFERENT source: opal-data-inf eclipse gold). So either (a) run it in the smartx DAG accepting the cross-source eclipse read (self-pacing via "latest eclipse gold w/ sentinel"), or (b) split inflection-per-firm to the INF/eclipse pipeline. AE/CTO architectural call.

## RAVC2 -> COO (210929Z), CC CTO+AE+DE.

## Bell-curve DURABLE-close now = global (AE EC2 Docker redeploy, in flight) + per-firm DAG/bundle wiring (this §2, AE lane). DS producer work complete on both; remaining is AE infra wiring + DE/CVO post-deploy re-verify + RD FE cutover.

## pre-1/16: still parallel-paused for Andrew #3 (b3e627a75, CTO-concurred rec B).
