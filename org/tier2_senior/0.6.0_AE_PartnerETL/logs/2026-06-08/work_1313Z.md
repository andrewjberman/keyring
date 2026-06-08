# 0.6.0_AE_PartnerETL session log — 2026-06-08 work_1313Z (COO cold-boot: GLDINC P0 + NFRA W2a weekend-nightly validation)

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, REVIEW

COO cold-boot bring-up per LD-0165. Mission: validate ADHC_GLDINC P0 checkpoint (`f815db45e`) and NFRA W2a runner-telemetry (`a4062e09c`) on the **weekend scheduled nightlies** at **zero extra compute** (standing NFRA cost-governance: no ad-hoc bd-gold runs; validate-on-nightly only), then stage GLDINC P1. Both deploys landed to `code/gold/` on 6/5 16:39/16:41Z — before the weekend nightlies — so the 6/6 + 6/7 runs are clean validation evidence.

## Startup
- `/watcher`: registered LIVE (PID 26252), persistent inbox Monitor armed (task bm1ba1mf0), inbox empty, no stale cron.
- **Loop arming:** launch directive said `CronCreate /work 20m` per LD-0082 — **superseded by LD-0157** (Andrew 2026-06-05) + XXX.md Step 1b-F: Tier-2/3 workers arm **NO `/work` cron**; persistent Monitor is the sole standing mechanism. Did NOT arm. Event-driven; broker STATUS carries blocks for COO `/drive`.

## Weekend nightly runs validated (3, all on the deployed code)
| Chain log | Started (UTC) | Finished | Outcome |
|---|---|---|---|
| `chain_full_20260606_040054.log` | 6/6 04:00:54 | ~05:28Z | clean |
| `chain_full_20260606_230044.log` | 6/6 23:00:44 | ~00:27Z | clean |
| `chain_full_20260607_040054.log` | 6/7 04:00:54 | 6/7 05:30:48Z | clean — validation PASS/WARN/FAIL/SKIP/ERROR = 0/0/0/1/0 |

## NFRA W2a — runner-telemetry outer-wrap — VALIDATED (zero extra compute)
- **Telemetry JSONL produced, all 28 scripts, each weekend night** → `s3://opal-data-bd/logs/gold-layer/telemetry/bd-gold-layer-runner/{id}/{run_id}.jsonl`. Sampled `A_03/edae7b2916db.jsonl` (6/6 23:02Z run): 458 per-tick rows, each carrying `cpu_pct`, `memory_pss_mb`, `memory_rss_mb`, `sys_mem_used_mb`, `sys_mem_pct`, `threads`, `disk_read/write_mbs`. Richer per-tick PSS+CPU exactly as designed.
- **merge_perf_report contract INTACT.** gold_prof.py still runs as the wrapped child (gold_dispatch.sh:293) writing `/tmp/perf_scripts/{id}.json` → merge produces `perf_report.json` FRESH (6/7 01:30:50Z, 31773 B). Not empty; contract preserved.
- **perf_history archive working** — 4 snapshots: 6/5, 6/6 (x2), 6/7 (`gold/perf_history/perf_report_{date}_{ts}.json`).
- **R3a right-size held under the wrap.** Runner `i-01003b035d2988dfb` = **r6i.4xlarge** (down from c6i.16xlarge). A_03 (binding-constraint script) telemetry peak `sys_mem_used ~22.2GB` / 128GB = 17.5% → comfortable headroom, no OOM, clean completion both nights.
- **Exit-code propagation verified (correctness gate).** `runner-telemetry.py` `main()` returns `rc = proc.wait()` and `sys.exit(main())` propagates it (lines 403/407/411). Telemetry upload happens post-wait, doesn't mask rc. The wrap is transparent to failure semantics — a gold_prof failure still trips the chain abort.

## GLDINC P0 — checkpoint primitive — VALIDATED on live nightly (resume==fresh structurally proven)
- **`.done` markers written for the full script set each night** → `gold/.checkpoints/{run_date}/{id}.done`. 6/6: 28 markers; 6/7: 27 markers (A_00–04, B_00–03+B_01b, C_00–08, D_00–04+D_00b+D_00c, S_00) — full clean set both nights.
- **Marker-iff-success invariant CONFIRMED in deployed code.** `_checkpoint_write` fires ONLY inside the `if ...runner-telemetry.py -- ...gold_prof.py; then` success branch (gold_dispatch.sh:290–294). Combined with the verified wrapper exit-propagation, a marker exists ⟺ that script's gold_prof exited 0 (incl. its `--upload` of served keys). A failed/interrupted script leaves no marker → resume re-runs it.
- **Fresh nightly never skips** — 0 `SKIP ...(checkpoint .done present)` lines in the 6/7 chain log (GOLD_RESUME unset → fresh re-runs+overwrites, as designed).
- **Zero live-nightly impact** — additive parallel `.checkpoints/` prefix, no served-key change; both nightlies completed clean with no regression from the P0 code.
- **resume==fresh equivalence — STRUCTURALLY PROVEN, empirical run DEFERRED.** Resume (GOLD_RESUME=1) skips exactly the scripts whose marker is present for the run_date; by the invariant those are precisely the completed+uploaded scripts, so resume reproduces the identical served state without recompute. The **empirical byte-identical resume RUN** is the one residual — it inherently requires a resume gold run (= ad-hoc compute), which is **banned** under the standing no-ad-hoc-runs directive. Appropriately deferred to either (a) the next natural mid-chain interruption recovery, or (b) the P2 dedicated small auto-shutoff EC2 parity-run-machine (my §4b design already specs it). NOT manufacturing a run to close this.

## RAVC2
- Sent to COO (`2.0.0_SA_COO`) + CTO (`1.0.0_SA_CTO`): both validations PASS with the one deferred-empirical-resume residual flagged.

## Next
- Stage GLDINC P1 — load_flows watermark plumbing-proof (in progress this session).
- §4b scorecard harness builds alongside P1. P2 small-EC2 parity spec (also closes the empirical resume==fresh residual). Top-of-month bracket + §5a w/ 0.4.0 ahead of 7/1.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| (none required) | — | Pure validation/trace pass over deployed S3 artifacts + deployed `gold_dispatch.sh`/`runner-telemetry.py` source. No gold script edit/run, no portal/Lambda change → no comp-* gate applies. P1 plumbing-proof staging (next) will run `comp-pipescript io`/`feeds` on the load_flows entry point before any edit. |
