# 0.6.0_AE_PartnerETL SESSION LOG — 2026-06-05 (work_2120Z, session closeout)

**archetype:** DEPLOY · **secondary:** DIAGNOSE, VALIDATE, ANALYZE, REVIEW
**span:** bring-up (~12:50Z) → ~21:20Z. Heavy multi-thread Andrew-direct session. Per-tick logs: work_1304/1345/1416/1423/1500/1514/1547/1722/1754Z. This = the session-level closeout.

---

## 1. ADVI_DEMOAUTH.002 — demo dataset rebuild (Andrew-direct, COO TOP) — CLOSED
The session's spine. Brought up to verify a Pass-2 mid-write death; it cascaded into a full rebuild + speed fix + scaling fix.

- **Regression caught on verify (not assumed):** prior run died mid-write AFTER a destructive snapshot-clean → demo REGRESSED to 6601 objs (firm/clients/advisors=0). Root cause: a single `NoSuchKey` on a vanished source key (bd-source drift, 169→165 advisors) aborted the whole destructive run.
- **Durability fix** (`a6b83b042`): worker skips a 404'd source key + continues; completion gate accounts skips; PII HardError abort UNCHANGED. Relaunched.
- **Pool fix** (`41f6f89c8`): boto3 default `max_pool_connections=10` throttled 32 workers → sized pool to workers (10→63 conns). Helped I/O but throughput stayed ~12/min (CPU/GIL-bound).
- **THE speed fix — Andrew flagged 33h ETA as absurd:** root cause = TWO O(N_identities × text) brute-force loops per object (transform_string substr + leak_check) scanning ~6-10k identities. First attempt (one-pass regex `1b9475c39`) DID NOT HELP (benchmarked ~1.5x on Py3.9 — caught via measurement, wasted a relaunch). Real fix = vendored **Aho-Corasick** (`394969a6a`): O(text), benchmarked 23x/15x. Result: **~12/min → ~280/min, 33h → ~1.5h same box.** Same fix applied to `pii_leak_scan.py` (`ba50c4c14`).
- **Completion:** 22414/22414 written. Hit a FALSE exit-4 (benign per-subpath categorization: one platinum/49financial firm obj source-buckets "firm" but rekeys "demo"→"other") which blocked the auto R5 leak-scan. Ran R5 manually → **leak_count=0** (all 22414 scanned). In-line per-object leak_check also passed throughout.
- **Scaling bug (Andrew caught post-rebuild):** a few firm chart artifacts missed the ×3. Root cause: `_is_monetary` only matched LEAF field names, but $ values live under DYNAMIC keys — geography names (geo/data[]/TX), distribution stats (p10-p90/bins/mean), timeseries components (nna/net, growth/market) — all under monetary ANCESTORS. **Fix = context-aware scaling** (`11d6edaf4`): `money_ctx` flag propagates from monetary sections; scale iff money_ctx AND not blocked (pct/count/rate/id/year/date/rank/days/index). Verified on real data (no over-scaling). Re-transformed firm artifacts, then **full defensive pass: all 22414 re-transformed (overwrite, NO snapshot-clean), 0 leaks, count intact** — COO RAVC2-ACCEPTED, CVO cycle-22 finding resolved.
- **Andrew simplification directive:** demo is ONE-TIME / static / never-deleted / no-schedule (verified 0 EventBridge/triggers); the EC2 ceremony was unnecessary. **Box i-03343a60 TERMINATED** (0.7.0, `9bfd1c7b5`) + local rebuild path documented (README). Memory: `project_demo_dataset_one_time_static_local_no_ec2`.
- **STATUS: COMPLETE + data-correction CLOSED.** Sole remaining gate = DS final read-only PII sign-off tomorrow (before external use; internal clean now).

## 2. NFRA_COSTRED R3 — bd-gold right-size (Andrew-direct) — APPLIED
- Analyzed existing perf telemetry (no ad-hoc run): bd-gold c6i.16xlarge uses wall-weighted avg 3.8/64 cores = **94% CPU-idle**; real constraint = memory (76GB peak) + parallelism RAM-paging-bound. Brief `2fcd07d01`.
- **Right-size APPLIED** (Andrew GO): `modify-instance-attribute i-01003b03 → r6i.4xlarge` (~63% cut). Validates on tonight's nightly. perf_history archival shipped (`51416e495`) + persistent-instance arch finding (right-size trivial, Spot needs new infra → inverted CTO Spot-first).

## 3. inf-gold R8 false-reap (CVO time-critical) — RESOLVED
- inf-gold i-0ed5 ran <3% CPU (I/O-bound REST-pull); real R8 false-reap risk. Answered CVO with the profile; tag HELD per COO (Andrew zero-exemptions); resolved under enforcer-v1.1.1 (3%→1% threshold) + inf-gold completed + self-stopped. First R8 active-job canary (my demo box) verified.

## 4. ADHC_GLDINC — gold incrementalization build (Andrew-approved) — LEAD
- **Phase-0 audit** (`a82c67f39`): 27 scripts classified (8 CA/12 IWR/7 FRI). A_03 binding-constraint finding (76GB = expand materialization, NOT inherent → incrementalizable → drops box below r6i.4xlarge).
- **Two-axis addendum** (`c6ac4ec8e`): Andrew freeze-baseline framework → ALL 6 FRI reclassify to IWR; cost-model-as-output.
- **Build-PRD review** (5 mechanics flags) → CTO folded to v0.1.1/v0.2 (Andrew-approved).
- **P0 CHECKPOINT BUILT** (`f815db45e`): per-script .done markers + GOLD_RESUME resume-skip in gold_dispatch (orchestration-only, serves GLDINC + R3b-Spot; set -e preserved). **DEPLOYED tonight** per COO option-(a) ruling (with W2a).
- **§4b scorecard design** (`80bc1434b`): quantitative daily scorecard + parity-machine phasing + 2026-07-01 top-of-month bracket. CTO-accepted; month-long daily-tracked through 7/5.

## 5. NFRA W2(a) — telemetry outer-wrap — DEPLOYED
- CTO-ratified outer-wrap (`a4062e09c`): runner-telemetry.py wraps gold_prof.py (merge_perf_report contract intact + per-tick JSONL). Added the `--s3-bucket`/`--s3-prefix` the CTO snippet omitted. Surfaced + resolved the P0-entanglement deploy conflict (same file) → COO ruled option-(a) deploy-both. **gold_dispatch.sh HEAD (perf_history+P0+W2a) + runner-telemetry.py DEPLOYED to code/gold/.**

## 6. Fabric / housekeeping
- LD-0157: `/work` 20m cron RETIRED (CronDelete de6408be) → event-driven via Monitor + COO /drive. Broker status token-led (WORKING/IDLE).
- Inbox Monitor died ~5x (exit 143/SIGTERM) — re-armed each; cron-poll/inbox-pull is the lossless backstop; CTO concluded operational-impact-zero.
- Memories saved: `reference_boto3_pool_cap_throttles_threadpool_s3`, `reference_multisubstring_scan_use_aho_corasick_not_regex`, `project_demo_dataset_one_time_static_local_no_ec2`.

## Open / next (all gated, queue clean per COO)
- **Tomorrow's ~11:03Z nightly read** → NFRA W2a RAVC2 (telemetry JSONL + perf_report intact + R3a r6i.4xlarge wall/sys_mem + P0 markers + perf_history archive).
- DS final demo PII sign-off (tomorrow, read-only).
- GLDINC: P0 resume==fresh validation (controlled test) → P1 (load_flows watermark). Scorecard harness alongside P1. P2 small-EC2 spec. Top-of-month bracket + §5a w/ 0.4.0 ahead of 7/1.
