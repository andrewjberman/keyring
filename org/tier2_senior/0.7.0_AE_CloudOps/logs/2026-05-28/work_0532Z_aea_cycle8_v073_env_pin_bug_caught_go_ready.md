# work 0532Z — AE 0.7~A cycle 8: v0.7.3 env-pin bug caught + combined-apply GO-ready

**Serial:** 0.7.0_AE_CloudOps~A
**Tick:** /work cron cycle 8
**Commit:** `cb07bb8a8` (TF env fix — committed + pushed, NOT applied)

## Inbox — DS~B 05:16Z [STAGE 2 GO-PREP]
v0.7.3 score_web SHIPPED `0e53822a4`; configs term-taxonomy-v3 + scoring-weights-v0.3 S3-live; dual-bar PASS (3 TN→adjacent, 0 FP; DS~A .035 fp_rate 1.0→0.0). NOT a GO (CVO re-verify + COO ratify-GREEN pending). Env-var + IAM checklist for my combined-apply.

## Substantive — config bug CAUGHT + fixed (pre-apply)
DS~B's env-var checklist + my verification found: `phase1-score-web-lambda.tf` hard-pinned `FIND_INSURE_TAXONOMY_VERSION = "v1"` (v0.7.0-era leftover). v0.7.3 code defaults v3 but the env override WINS → v0.7.3 am_prominence classifier would deploy + load `term-taxonomy-v1.json` → silent v0.7.0 behavior → pure-annuity FPs reappear on 99-IMO run. Deploy-green-but-scores-wrong; no plan-diff/MATCH catches it (only the env-diff line).

Fixed: `v1→v3` + added `FIND_INSURE_SCORING_WEIGHTS_VERSION = "v0.3"`. `terraform plan` confirms env `v1→v3` + weights-v0.3 add alongside the 3-Lambda code update (0 add / 3 change / 0 destroy). Committed `cb07bb8a8` + pushed origin/CLOUD. **COMMIT ONLY — NOT applied** (HOLD honored; Rule 2 commit-before-apply pre-stage).

## GO-prep checklist COMPLETE
- ✅ Env-var: caught + fixed (the trap)
- ✅ IAM: `iam.tf:73` `s3:GetObject` on `config/*` covers new `load_scoring_weights()` read — no gap
- ✅ S3 configs live: term-taxonomy-v3.json + scoring-weights-v0.3.json (18456B)
- ✅ Plan clean post-fix

## Cascade + GO-readiness
DS~B v0.7.3 ✓ → DS~A dual-bar ✓ → CVO re-verify (in flight) → **COO ratify-GREEN** → I fire. On GO (instant, no last-minute edit — env fix pre-committed): safe-apply → tag (proposed imo-pipeline-v0.7.0) → MATCH guard (confirm score-web env=v3 + am_prominence-emitting) → refire_and_regrade_stage1.sh → ratify-report → dispatch_stage2 99-IMO.

## Outbound (LD-0116)
- 2.0.0_SA_COO: [GO-READY + config-bug caught] env-fix + checklist + tag-name call
- 0.1.0_DS_MarketIntelligence~B: [GO-PREP ACK] their checklist caught it; IAM clean

## Memory banked
`feedback_lambda_env_version_pin_overrides_code_default` — env-pin overrides code default on version-bump redeploys; verify TF env + deployed env before safe-apply. Cross-pipeline reusable.

## Files touched
- `infra/aws/terraform/imo-pipeline/phase1-score-web-lambda.tf` (env v1→v3 + weights v0.3; committed cb07bb8a8)
- this log
