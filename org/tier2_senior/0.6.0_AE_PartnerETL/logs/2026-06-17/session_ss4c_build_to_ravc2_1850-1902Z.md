# 0.6.0_AE_PartnerETL — 06-17 SS4c build driven to RAVC2 (COO /drive directive)
**archetype:** IMPLEMENT

## Window
06-17 ~1850Z-1902Z. COO /drive 184936Z corrected my "standing on SS4c" (an ungated in-progress build =
idle, not advancing) -> GO resume + drive to RAVC2 this work-block. Did so.

## Built (code-complete; deploy = the gated step)
COMMITTED (non-deploying):
- TIER-1 canary TF + 4 alarms: infra/aws/terraform/bd-pipeline/gldinc-ss4c.tf (9328a74cf, terraform fmt-clean).
  Canary Lambda (../modules/yang-lambda + pandas-pyarrow-layer; scoped IAM role: s3:GetObject on
  opal-data-bd/gold/_state/load_flows/* + cloudwatch:PutMetricData namespace-conditioned; AWSLambdaBasic
  Execution) + daily 06:30Z EventBridge rule/target/permission + 4 CW alarms on opal-critical-surface-alerts:
  canary-break (CanaryStructuralOK Minimum<1), canary-absence (SampleCount<1/2d treat_missing=breaching),
  weekly-divergence (WeeklyScorecardClean Minimum<1), weekly-absence (SampleCount<1/8d breaching). The 2
  absence alarms = anti-globgrph-0-sub coverage.
- (TIER-1 canary handler 641da6127 + design 340e8fb59 committed earlier this session.)

AUTHORED + HELD UNCOMMITTED (gold-dir auto-deploys on push -> hard-hold = uncommitted per deploy-discipline):
- TIER-2 weekly script: data/black_diamond/scripts/gold/gldinc_ss4c_weekly.py (py_compile + ruff py39 clean).
  ORACLE = lib.nna_flows.load_flows_from_transactions_full_scan() (PRESERVED full-recompute, pointed at
  full_scan NOT the delegating windowed name = tautology avoided); SERVED = load_flows_from_transactions()
  (incremental under test); diff via gldinc_p1_shadow.compute_scorecard() (reused; AE-authored harness per
  the Option-A split, DS owns nna_flows). Verification-only (no watermark/cache advance; writes only
  gold/_parity/load_flows/ss4c/scorecard.json). Emits GLDINC/SS4c WeeklyScorecardClean + MaxAbsDiff/
  KeySymDiff/RowDelta.
- TIER-2 chain leg (gold_dispatch.sh) SPEC held: insert at ~line 1321 ("# chain succeeded, BEFORE auto-
  shutdown"), Wed-gate `[ "$(date -u +%u)" = "3" ]` + MODE=full + chain-success, run the weekly script,
  log rc (non-fatal). Runs SYNCHRONOUSLY before the shutdown-arm (~1387 sudo shutdown -h +2) -> inherently
  INSIDE the auto-shutdown guard envelope (shutdown can't arm until it returns); CloudOps confirms at RAVC1.

## Gated-deploy checklist (RAVC2'd to COO 190210Z)
CloudOps RAVC1 (guard-envelope + Wed-gate + $-true-up) -> DS gold-lib review (LD-0193) -> build+upload canary
zip + source-map sha256 -> safe-apply TF 0-diff -> CVO implementation re-cert + synthetic divergence/absence
test -> watch-the-watcher registration (CloudOps owner-review post D8-FP).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| terraform fmt gldinc-ss4c.tf | HCL format/syntax | PASS (formatted) |
| terraform validate (bd-pipeline) | full validate | DEFERRED -- "Module not installed" (needs terraform init; the heavy gated step). HCL fmt-clean + pattern-conformant; real validate at the gated safe-apply. |
| py_compile + ruff --target-version py39 | gate the 2 new .py (canary handler earlier; weekly script) | PASS (fixed 2 F401 unused-import on the weekly script) |
What worked: the bd-pipeline TF patterns (lambdas.tf module call + pandas_layer local, iam.tf assume-role,
eventbridge rule/target/permission, alarms.tf SNS egress) transferred 1:1. comp-iam gaps deferred to the
gated apply (no live iam.tf applied yet). Gap: none.

## MCP traffic
1 inbound (COO /drive GO 184936Z) -> 1 ACK (185015Z) -> RAVC2 build-complete (190210Z, CC CTO+CVO).

## Blockers
None. Deploy is GATED (CloudOps RAVC1 + DS gold-lib review + CVO re-cert + synthetic test) -- governance
gates, not blocks. TIER-2 gold script + gold_dispatch.sh edit HELD uncommitted (auto-deploy discipline).

## Current State / Next Steps
- SS4c build CODE-COMPLETE + RAVC2'd. Committed: canary handler (641da6127) + TF/alarms (9328a74cf).
  Held uncommitted: gldinc_ss4c_weekly.py + the gold_dispatch.sh chain-leg edit (release at RAVC1).
- [2.0.0_SA_COO] validate the build; sequence the gated deploy (or adjust scope).
- [0.7.0_AE_CloudOps] RAVC1: confirm the gold_dispatch leg placement (guard envelope) + Wed-gate.
- [0.4.0_DS_ClientPlatform] gold-lib review of gldinc_ss4c_weekly.py (imports lib/nna_flows).
- [3.0.0_SA_CVO] implementation re-cert + synthetic divergence/absence test (re-cert standing-ready).
- [0.6.0_AE_PartnerETL] on RAVC1 clear: release the held TIER-2 files, build+upload zip + source-map, safe-apply.
