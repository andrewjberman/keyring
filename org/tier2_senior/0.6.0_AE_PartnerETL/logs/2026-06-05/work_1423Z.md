# 0.6.0_AE_PartnerETL session log — 2026-06-05 work_1423Z (R3 right-size APPLIED + Spot-resume answer)

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE

## R3 right-size APPLIED (Andrew GO via COO relay)
- `aws ec2 modify-instance-attribute --instance-id i-01003b035d2988dfb --instance-type r6i.4xlarge` on the STOPPED bd-gold instance. VERIFIED: state=stopped, type=r6i.4xlarge (was c6i.16xlarge).
- Tonight's bd-gold-trigger start_instances() launches it right-sized (16 vCPU/128GB). Revert ready: same cmd -> c6i.16xlarge.
- VALIDATION (tomorrow's nightly): wall (+10-20min est, within 7-8h portal margin), sys_mem<128GB (no OOM), perf_report intact + now perf_history-archived. RAVC2 tomorrow.
- Expected: ~63% cost cut (~$2.72->$1.01/hr, ~$75-160/mo) on the biggest single lever.

## Andrew Q answered — Spot interruption resume granularity (Spot-design input)
- pending-marker retry = FULL-CHAIN restart (re-runs run_gold_layer.sh incremental), for queued NEW triggers, NOT Spot-interruption recovery. Spot reclaim mid-run currently = full re-run (~82min lost).
- No automatic per-script done-marker/output-exists skip within a chain run. `--incremental` = date-watermark skip (A_00/C_06 only), not script-skip. Manual resume primitive EXISTS: `--from <id>` (runs script + rest of A/B/C/D group, assumes upstream done).
- Per-script auto-resume FEASIBLE (moderate): write done-marker post-completion to S3 gold/.checkpoints/{run_date}/{script_id}.done; on restart compute resume point + `--from` first incomplete (A->B->C->D order); interrupted script re-runs (marker post-completion only). Worth building INTO the Spot follow-on so an interruption costs only remaining scripts.

## State
- bd-gold R3: right-size LIVE for tonight (awaiting tomorrow's validation). Spot = follow-on design (don't-build-yet; right-size validates first; one-var-per-nightly). perf_history shipped.
- demo-reclone3: ~33h+, R8-safe, let-it-run. inf-gold: self-sparing via intermittent >3% spikes, tripwire held.
