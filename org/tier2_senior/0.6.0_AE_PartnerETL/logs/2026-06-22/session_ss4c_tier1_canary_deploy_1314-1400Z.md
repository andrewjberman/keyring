# 0.6.0_AE_PartnerETL -- 06-22 SS4c TIER-1 canary DEPLOYED + verified (COO GO)
**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE (3 invoke-surfaced canary bugs), COORDINATE (RAVC2 + 3 handoffs)

## Window
06-22 ~1314Z-1400Z. Session start -> /watcher + org/XXX.md startup -> COO GO (131447Z) on the queued
ADHC_GLDINC.SS4c periodic-oracle-revalidation TO + DS gold-lib review CLEAN (gate-2). Drove the TIER-1
canary half to a verified, ledger-closed, tagged deploy in-session.

## What landed (tag bd-v2.32.0; origin/CLOUD thru d3e4800e5)
TIER-1 canary infra (12 TF resources, infra/aws/terraform/bd-pipeline/gldinc-ss4c.tf):
- Lambda `gldinc-ss4c-canary` (3008MB, py3.11, pandas layer; scoped role gldinc-ss4c-canary-role:
  s3:GetObject gold/_state/load_flows/* + cw:PutMetricData ns-conditioned GLDINC/SS4c + BasicExec).
- EventBridge `gldinc-ss4c-canary-daily` cron(30 6 * * ? *) + target + lambda permission.
- 4 CW alarms -> EXISTING opal-critical-surface-alerts SNS: canary-break (Min<1), canary-absence
  (SampleCount<1/2d breaching), weekly-divergence (Min<1), weekly-absence (SampleCount<1/7d breaching).

DS pure-swap ADOPTED in the held TIER-2 script data/black_diamond/scripts/gold/gldinc_ss4c_weekly.py
(still uncommitted, gated on CVO re-cert): SERVED load_flows_from_transactions() ->
load_flows_from_transactions_windowed(read_load_flows_watermark())[0]. Verified value-equivalent (the
served entry internally returns the windowed `daily` then ALSO persists; swap drops only
write_load_flows_state) -> verifier now mechanically side-effect-free. ds-commit-gate clean.

## Deployment Sequence (AE)
1. ds-commit-gate gldinc_ss4c_weekly.py (DS swap) -> PASS.
2. source-map entry for gldinc-ss4c-canary (commit 6432e7a65; co-carried a NOT-MINE infra-monitor
   artifact_sha256 sync, noted in msg + commit -> flagged COO/CloudOps).
3. deploy_ledger open gldinc-ss4c-tier1-canary (3 legs, 6h window).
4. ARTIFACT-FIRST: build-and-upload bd-pipeline gldinc-ss4c-canary -> s3 zip + sha (TF data source
   reads it at plan).
5. terraform init + plan -> clean "12 to add, 0 change, 0 destroy" (SS4c-only, no bd drift). comp-iam
   service gldinc-ss4c-canary -> 3 ops GRANTED.
6. safe-apply #1 -> PARTIAL (8/12); 2 AWS rejects (half-landed, finished in-session):
   - IAM role: "Duplicate tag keys ... case insensitive" -- lowercase `project` collided with provider
     default_tags `Project` (main.tf:31); IAM case-insensitive, CW/EventBridge case-sensitive (alarms
     kept `project`, succeeded). Fix: drop `project` from the role tags (commit ffd91c92e).
   - ss4c-weekly-absence: EvaluationPeriods*Period must be <=604800 for period>=1h; 86400*8 invalid ->
     86400*7 (commit ffd91c92e; 7d window still pages a stopped weekly in one cycle, no 1-2d-slip FP).
7. safe-apply #2 -> 7 added, 0 change, 0 destroy. Apply complete.
8. Live invoke #1 -> OOM (512MB on the 66MiB live cache). memory_size 512->3008 (731413c51) -> apply.
9. Live invoke #2 -> PutMetricData reject: Unit "Hours" invalid. Handler unit Hours->None (2f413951c)
   -> rebuild (233ac6717) -> apply.
10. Live invoke #3 -> ok:false trade_date_not_datetime:object. INVERTED assertion: cache stores
    trade_date str-normalized (write_load_flows_state .astype(str), ArrowType-trap fix); contract is
    object/str not datetime64. Assertion datetime64->object (37f638a13) -> rebuild (b08ff290c) -> apply.
11. Live invoke #4 -> ok:true. 0-diff plan "No changes". record-terraform-deploy bd-pipeline (updated
    ONLY gldinc-ss4c-canary->37f638a1, preserved 17 siblings; CHANGELOG bd-v2.32.0; 7f10b827) ->
    tag bd-v2.32.0 -> push --follow-tags (d3e4800e5) -> ledger CLOSED (3/3) -> check: nothing half-landed.

## Verification (actual output)
Canary live invoke (final): `{"ok": true, "failures": [], "metrics": {"CacheRowCount": 4061630.0,
"TxidIntCount": 1467480.0, "TxidStrCount": 2594150.0, "WatermarkAgeHours": 9.17}}`. StatusCode 200,
no FunctionError. Max Memory Used ~1750MB/3008MB. Cache preflt_events.parquet = 65.9MiB, advanced
06-22 00:39Z (nightly ran despite the 3-day closure -> no freshness false-positive; closure lens
applied per COO note, watermark 9.17h fresh). terraform 0-diff: "No changes. Your infrastructure
matches the configuration." deploy_ledger check: "no open deploy ledgers ... nothing half-landed".

Alarm states post-deploy: weekly-divergence OK; canary-absence + weekly-absence INSUFFICIENT_DATA
(initial); **canary-break ALARM** -- FALSE-POSITIVE from my iterative-test CanaryStructuralOK=0
(invoke #3, before the trade_date fix) lingering in the daily-Minimum window. Self-clears ~06-23
13:47Z when the test-0 ages out. Steady-ALARM = no further pages (set-alarm-state would flap an
OK->ALARM re-page, so left it).

**EGRESS FINDING (CloudOps F-1, 140218Z -- corrects my deploy assumption):** the 4 SS4c alarms route
to opal-critical-surface-alerts, which is CURRENTLY NON-DELIVERING -- the 06-17 email sub was never
confirmed -> AWS auto-deleted it (72h) -> only a sandboxed SMS sub remains -> NumberOfNotifications
Delivered=0 since ~06-16. So the canary-break ALARM published to SNS but reached NO subscriber (the
false-positive paged no one; equally, REAL SS4c divergence/absence won't deliver yet). This is exactly
unknown-unknown #2 (a verifier whose alarm has no delivering sub) -- now manifest at the topic level.
The alarms are wired to the CORRECT canonical topic; the topic egress is a SHARED, pre-existing,
Andrew-gated F-1 (re-confirm email OR lift SMS sandbox), affecting ALL critical-surface alarms, not
just SS4c. SS4c alerting is INERT until that's restored. The watch-the-watcher YAML must assert
DELIVERY-CAPABILITY (deliverable!=0), not bare subscriber-presence (CloudOps directive).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| ds-commit-gate.sh (x3) | gate weekly-script DS-swap + canary handler (unit, trade_date) | PASS all |
| comp-pipescript deployed gldinc_ss4c_weekly.py | gold-touch gate (COO GO) | NO-MATCH (new verification harness, not a served producer; accounted Unknown, not CLEAN) |
| comp-pipescript io load_flows | Phase-1 oracle/served identification | load_flows is a fn not a script ID; Phase-1 grounding already done in 06-17 design doc |
| comp-iam service gldinc-ss4c-canary | Phase-2 IAM gap | 3/3 ops GRANTED (s3:GetObject x2 + cw:PutMetricData) |
| terraform fmt/validate/plan/0-diff | TF gate | fmt+validate clean; plan SS4c-only; 0-diff converged |

What worked: comp-iam resolved the new role from the source-map entry + confirmed grants pre-apply.
build-and-upload artifact-first ordering (TF data source) held. record-terraform-deploy ADHC_DRIFTD.001
content-commit scoping preserved 17 sibling provenance (no clobber).
What failed: nothing tool-side. The 3 canary bugs (OOM/unit/trade_date) were invoke-surfaced -- the
gated build was never invoke-tested, so "code-complete" hid runtime defects (per NEVER-trust-rc=0).
Gap: comp-pipescript io/deployed don't cover a non-producer verification harness (expected; Unknown).

## MCP traffic
~6 significant. IN: COO GO (131447Z) + DS gold-lib review CLEAN. OUT: ACK COO + ACK DS (132708/132713Z);
RAVC2 SS4c TIER-1 -> COO (135959Z, CC CTO+CVO); gate-3 ask -> CVO (140010Z); watch-the-watcher + cost
-> CloudOps (140023Z).

## Blockers
None. TIER-2 weekly release is GATED (not blocked) on CVO re-cert of the DS-swapped script (async; TO
says don't block TO-3). gate-3 synthetic test + watch-the-watcher + cost-model = handed off (CVO/CloudOps).

## Current State (zero-prior-context handoff)
- **SS4c TIER-1 (DONE):** 12 resources live (tag bd-v2.32.0, origin/CLOUD d3e4800e5). Canary verified
  ok:true. Ledger gldinc-ss4c-tier1-canary CLOSED. canary-break ALARM is a test-0 FALSE-POSITIVE,
  self-clears ~06-23 13:47Z (not a real cache break).
- **SS4c TIER-2 (HELD, gated on CVO):** data/black_diamond/scripts/gold/gldinc_ss4c_weekly.py (DS
  pure-swap applied, ds-commit-gate clean) + the gold_dispatch.sh Wed-leg = UNCOMMITTED. Release after
  CVO re-certs the swap. RUNWAY: ss4c-weekly-absence (7d breaching) ticks from 06-22 -> need a weekly
  datapoint by ~06-29; first Wed run 06-24 covers it if TIER-2 releases before then.
- **Source-map (infra/aws/lambda/ci/lambda-source-map.json):** gldinc-ss4c-canary entry added; co-carried
  a not-mine opal-infrastructure-monitor sha sync (committed 6432e7a65 w/ note) -> route to infra-monitor
  owner (possible undeployed TF tail). Also noted: bd-price-update sha line is a pre-existing MSYS
  path-conversion relic (out of scope).
- Commits (mine): 6432e7a65, ffd91c92e, 731413c51, 2f413951c, 233ac6717, 37f638a13, b08ff290c, 7f10b827.

## Next Steps
1. [3.0.0_SA_CVO] gate-3: implementation re-cert of the as-built (DS swap + 3 canary fixes) + synthetic
   divergence/absence test (egress-verified). Re-cert of the swap unblocks the TIER-2 release.
2. [0.6.0_AE_PartnerETL] on CVO swap re-cert: release TIER-2 (commit gldinc_ss4c_weekly.py + gold_dispatch
   Wed-leg) BEFORE the 06-24 Wed run / 06-29 absence deadline.
3. [0.7.0_AE_CloudOps] owner-review: register the 4 SS4c alarms into critical-surfaces.yaml
   (watch-the-watcher) + add the NFRA_COSTAWS §7 cost line (I'll draft the YAML to your D8-FP shape).
4. [2.0.0_SA_COO] route the infra-monitor source-map drift to its owner.
5. [0.6.0_AE_PartnerETL] update pipeline_inventory.xml with the SS4c canary/oracle (this commit or next).
