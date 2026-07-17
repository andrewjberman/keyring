# Session Log -- 0.2.0_DT_PortfolioAnalytics -- 2026-07-17 ~1815-1845Z
**archetype:** VALIDATE
**secondary_archetypes:** DEPLOY
**Project:** MDPF_VARFLAG (TO_VARFLAG_SHADOW_01 @f70328bda) -- post-close self-review

## Window summary
Adversarial self-review of yang-varflag-check v1.5.0 (deployed + RAVC4-closed in the prior
window) after a model/effort upgrade. Found ONE latent defect the pre-deploy replays could not
see (single point-in-time execution set), fixed + redeployed v1.5.1, then handled the CTO/CVO/COO
closure-acceptance traffic.

## The defect (latent, would fire DURING the shadow window)
`resolve_baseline` walked only the 12 newest non-excluded executions (`cands[:12]`). Benchmarks +
timeseries regenerate WEEKLY, peers MONTHLY. Today peers resolves to its 06-30 upload (fewer than
12 non-excluded SUCCEEDED executions since then), but over the next 2-3 weeks the accumulating
weekly benchmark uploads + re-runs push the 06-30 peers upload past the 12-window -> peers loses
its baseline -> standing `FM6-no-baseline-version` flag every run, corrupting the exact
false-flag-rate evidence that gates P2. Same symptom as the v1.5.0 runtime-found peers bug, deeper
cause: baseline HORIZON, not baseline LOGIC. Caught by review, not by the runtime demanding it
(the weaker discovery mode) -- the strong proof is that it can no longer fire in the evidence window.

## Fix + deploy (v1.5.1)
`MAX_BASELINE_CANDIDATES = 40` (covers ~2mo weekly churn incl re-runs). Loop still breaks on full
resolution, so the change only extends the monthly laggard's lookback depth (1 manifest
read/candidate, sub-second, << 120s timeout). Behavior-preserving for the current all-recent case.

## Deployment Sequence + Verification (actual)
- ba5fb9da9 source + ledger open -> build-and-upload (VERIFIED size=9642 sha256 match) ->
  5996e6ddb map -> plan (Plan: 0 add / 1 change / 0 destroy, lambda artifact only) -> safe-apply
  (Apply complete! 0 added, 1 changed, 0 destroyed) -> 0ffae035b record -> tag yang-pipeline-v1.5.1
  -> 0-diff confirmed ("no changes").
- BEHAVIOR (re-invoke on real exec 53a06944):
    per-artifact baselines: model_portfolio_benchmarks <- exec-c14fb8176125 (07-10);
    model_portfolio_timeseries <- exec-c14fb8176125 (07-10);
    peer_performance <- exec-0e10d5d56164 (06-30)  [<-- the monthly laggard, still resolved]
    flag_count: 0 | cells: 600  -- byte-identical to v1.5.0's terminal result.
- Ledger 20260717T1825Z CLOSED @6cd5ddaae (opened + closed in-session, no stranded leg).

## MCP traffic (this window)
4 inbound handled (all acks, no action owed): COO RAVC4 VALIDATED-CLOSED x2 (bd49f + varflag,
deploy-ledger RED count now 0), COO bd49f lane grant landed (@93dd13ea4+996acddc1, converter-dir
scoped), CTO VARFLAG closure ACCEPTED (noted the honest-tail exclusion as now SHADOW-VERIFIED not
hoped-for). Sent: CTO + CVO the v1.5.1 note (the v1.5.0 peers fix carried a horizon residual;
cured before evidence accrues). Andrew-direct: dev@test.com history annotation DECLINED
("fine as long as maintained going forward") -- F4 fix maintains it forward; no annotation of
today's captured rows.

## Files Modified
see commit messages: ba5fb9da9 (varflag_check.py + ledger), 6cd5ddaae (ledger close).

## Current State
- yang-varflag-check LIVE at yang-pipeline-v1.5.1 in the YangDataPipeline SFN (post-InvalidateCloudFront
  shadow state, Catch-all -> PipelineSuccess). SHADOW: blocks nothing. Report per run at
  s3://opal-data-portal-v2/data-refresh/varflag/{pipeline_uuid}/report.json.
- Shadow evidence clock RUNNING: >=3 real uploads (next weekly benchmark + peers ~07-31) before any
  P2 proposal returns to CTO's gate. P2 decomposition = COO's lane on exit.
- Deploy-ledger RED count = 0 (all three of today's opens -- BE01, bd49f, varflag x2 -- closed).

## Blockers
None.

## Next Steps
- [0.2.0_DT] 07-18 ~03:15Z: read bd49f dim-convert first UNATTENDED scheduled fire (CTO backstop;
  twin re-checks 05:00Z). Read F4's first real-email history row when Andrew next acts on the portal.
- [2.0.0_SA_COO] holds P2/GATE decomposition, authors on shadow-exit evidence (watch-not-drive).
- [3.0.0_SA_CVO] open instrument-verification items: 6-vs-13 flag/cell census alignment +
  pstdev-vs-sample-stdev derived-vol note (both non-blocking, CVO to rule).

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-grep / comp-glob | prior window (SFN + TF discovery) | PASS | no new estate search this window -- pure self-review + redeploy of a known unit |
What worked: the adversarial re-read (not a tool) caught a latent horizon defect a config-read
never would. What failed: nothing. Gap found: pre-deploy replays are single-point-in-time and
structurally blind to time-accumulation defects (baseline-window exhaustion) -- the shadow phase
+ manual review are the compensating controls; no comp-tool models "will this baseline still
resolve in N weeks."
