# Deploy-Completion Ledger -- yang-varflag-check (baseline-window hardening)

**Status:** COMPLETE
**Closed:** 2026-07-17T18:3xZ
**Opened:** 2026-07-17T18:25Z
**Owner:** 0.2.0_DT_PortfolioAnalytics (post-close adversarial review of yang-pipeline-v1.5.0)
**Lambda:** yang-varflag-check (pipeline: yang-pipeline)

## Defect (latent, found by self-review -- would fire DURING the shadow window)
The per-artifact baseline walk capped at the 12 newest non-excluded executions
(`cands[:12]`). Benchmarks + timeseries regenerate WEEKLY; peers regenerates
MONTHLY (last 06-30, next ~07-31). Today peers resolved to 06-30 because <12
non-excluded SUCCEEDED executions exist since then -- but over the next 2-3 weeks
(the shadow-evidence window) weekly benchmark uploads + re-runs push the peers
baseline past the 12-window, at which point peers loses its baseline and emits a
standing `FM6-no-baseline-version` flag every run -- corrupting the exact
false-flag-rate evidence that gates P2. Not caught by the pre-deploy replays
(single point-in-time execution set).

## Fix
`MAX_BASELINE_CANDIDATES = 40` (covers ~2 months of weekly benchmark churn incl.
re-runs). The loop already breaks once all artifacts resolve, so this only bounds
the monthly laggard's lookback depth -- one manifest read/candidate, sub-second,
well under the 120s timeout. No behavior change for the common (all-recent) case.

## Legs
- [x] 1. Source committed (commit-gate)
- [x] 2. build-and-upload.sh yang-pipeline yang-varflag-check
- [x] 3. terraform plan (expect: lambda artifact swap ONLY)
- [x] 4. safe-apply
- [x] 5. 0-diff plan
- [x] 6. record-terraform-deploy + tag yang-pipeline-v1.5.1 + push --follow-tags
- [x] 7. Behavior verify: invoke on 53a06944 -> peers still baselines to exec-0e10d5d56164
        (06-30) + 0 flags/600 cells (identity with v1.5.0's terminal result)

## Rollback surface
Prior artifact version in S3 (versioned); revert = re-point s3_object_version / prior zip + apply.

## Closure evidence (exercised)
- Commit chain: source + map committed -> artifact VERIFIED (size 9642, sha256 match) ->
  plan (1 change, lambda-only) -> safe-apply -> 0-diff -> tag yang-pipeline-v1.5.1 pushed.
- Behavior verify on 53a06944: peers STILL baselines to exec-0e10d5d56164 (06-30), benchmarks/ts
  to exec-c14fb8176125 (07-10), 0 flags / 600 cells -- byte-identical outcome to v1.5.0's terminal
  run, confirming the change is behavior-preserving today and only extends the laggard lookback.
- Deploy-completion discipline: opened + closed in-session, no stranded leg.
