# 0.4.0_DS_ClientPlatform — /work tick work_1903Z (NFRA.W2(b) DEPLOYED to runtime canonical)

**archetype:** DEPLOY
**secondary:** VERIFY

## Inbox — boundary CONFIRMED (via persistent Monitor bigtys1b1)
0.6.0 `[SYNC-ACK] S3 boundary CONFIRMED — GO`:
- (1) No file collision — 0.6.0 will NOT write/delete the opal-runner-shared gold_prof.py key; their W2(a) edits bd gold_dispatch.sh:245 invocation only. I own the key.
- (2) Upload ownership — no sync/TF/source-map governs it (2026-05-13 ADHC manual cp); I own the manual cp as the W2(b) deploy.
- Endorsed port-now/defer-swap; 0.6.0 HOLDS the runner-telemetry swap (confirmed bare wrapper-swap empties perf_report = CTO cond (b)); re-scoping W2(a) to COO+CTO.

## Pre-deploy reconciliation (verify-before-clobber)
Diffed all 3 gold_prof.py copies before touching anything:
- opal-runner-shared (7499B, May) == repo HEAD pre-port (c07c52383^) = the OLD RSS canonical orion/inf+bd actually pull.
- opal-data-bd (10058B, today ~18:41Z local) == my port byte-identical — already deployed by a peer's branch push + bd sync, but **INERT**: bd run-gold-layer.sh:90 syncs from opal-data-bd, then :97 OVERRIDES gold_prof.py from opal-runner-shared. So opal-runner-shared is the sole live runtime canonical.
- Confirmed c07c52383 on origin/CLOUD + local working file == c07c52383 (no concurrent mutation). CVO already spot-checked c07c52383 CLEAN (cf7278f5b; Rule-15 + compile + PSS-correct + CTO-nodded-observational).

## DEPLOY (the operative fix)
`aws s3 cp data/black_diamond/scripts/gold/gold_prof.py s3://opal-runner-shared/code/gold/gold_prof.py`
- 7499B (May RSS) -> 10058B (PSS port), 2026-06-03 15:02 local.
- VERIFIED: re-pull byte-identical to local/c07c52383; 12 PSS markers present.
- comp-pipescript doesn't track gold_prof (profiler utility, not a named gold data script) -> verification = re-pull byte-match (done), not comp MATCH.
- Single key -> ALL chains true-physical tonight (bd via :97 override; orion/inf via :398).

## Status / next
W2(b) deploy COMPLETE + verified. AC closes on tonight's SCHEDULED nightly perf_report.json (PSS true-physical + sys_mem, no phantom TB peaks). **NO ad-hoc run** (Andrew constraint). PHASE-ARTIFACT sent COO; RAVC2-close tomorrow on the validated perf_report. 3y-unrealized pull still HELD (COO).

work-cycle:0009
