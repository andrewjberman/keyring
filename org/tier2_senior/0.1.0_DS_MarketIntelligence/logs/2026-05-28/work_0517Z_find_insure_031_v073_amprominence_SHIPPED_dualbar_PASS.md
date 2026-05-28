# work cycle — DS~B 2026-05-28T~05:17Z — FIND_INSURE.031 v0.7.3 SHIPPED, DUAL-BAR PASS

**Agent:** 0.1.0_DS_MarketIntelligence~B
**TO:** FIND_INSURE.031 (reopened-v0.7.3-revision → RAVC2-submitted)
**Cycle class:** TO-completion (major implementation + validation)
**Commit:** `0e53822a4` (5 files, +1349/-854) · pushed origin/CLOUD · v3 configs S3-live

## What shipped (PRD v0.7.3 8d08c7564 §272-296)
v0.7.3 W1-classifier re-architecture — the fix for the v0.7.1 class_diversity gate my AC6 re-grade refuted.

- **config/term-taxonomy-v3.json** — v2 terms/classes carried forward verbatim; scoring-role metadata updated (annuity=denominator-only; class_diversity retired).
- **config/scoring-weights-v0.3.json** — NEW `wm_classification_v073` block: high_signal_term_set (RIA-self-ref/Form-ADV/Series-65,66/IAR/advisory-context-AUM) + am_prominence T_present=0.50/T_absent=null + context-gate config (negative_context_tokens + prominent_locations + annuity_context_tokens). class_diversity_multiplier_cap retired; employee/company blocks verbatim from v0.2.
- **score_web_gold.py v0.7.3** — `load_scoring_weights()`; `compute_am_prominence()` (high_signal context-gated numerator + annuity denominator + any_AM_signal); `is_high_signal_genuine()` (channel/disclosure/advisory-AUM gates); `classify_wm()` two-tier (present/adjacent+adjacent-floor/absent/null); `compute_rollup()` annuity-excluded + no diversity-mul; `is_spa_render_shell()` (PRD §281 SPA-render-fail → BLOCKED_UPSTREAM → null); `score_imo` emits am_prominence + am_prominence_components. Defaults v3/v0.3.
- **test_score_web_gold.py** — 33 self-tests PASS (am_prominence, 3 context-gates, two-tier wm incl adjacent-floor, SPA-shell, annuity-exclusion).

## DUAL-BAR PASS (CVO 2570068ce ADDITIVE-2) — real Stage 1 silver
| IMO | exp | am_prominence | wm |
|---|---|---|---|
| lincoln-investment | TP | 0.942 | present (TP-preserved) |
| allianz-life | TN | 0.012 | adjacent (FP fixed) |
| american-equity | TN | 0.000 | adjacent (F-2 regression fixed) |
| midland-national | TN | 0.048 | adjacent (FP fixed) |
| cambridge-investment-research | TP | — | null (SPA-render-fail) |
| 5x robots-blocked | — | — | null |

- Bar 1 TN-suppression PASS (0 FP) · Bar 2 TP-preservation PASS (lincoln present, no FN)
- **DS~A .035 discrimination_eval: TP=1 FP=0 TN=3 FN=0 precision=1.0 fp_rate=0.0 → DISCRIMINATION PASS** (vs v0.7.1 fp_rate=1.0/precision=0.25). Artifact: docs/briefs/discrimination-eval-v0.7.3-20260528.json.

## Key implementation decisions
1. **am_prominence ratio is the load-bearing discriminator** — even where context-gating is imperfect (midland keeps 23.7 genuine high-signal weight after gating), the annuity baseline (468) crushes the ratio to 0.048. Scale-invariant ratio (CTO's (C) choice) vindicated.
2. **SPA-render-fail detector** (PRD §281) — Cambridge IR's no-JS shell ("does not support JavaScript") → BLOCKED_UPSTREAM → null. Prevents FN-absent on a genuine target; flagged to CVO for re-verify (the one judgment call beyond the bare ratio). AC-T2 scraping_browser1 escape-valve re-crawls for real content later.
3. **wm_classification_reason in the .035 fixture** — initially omitted → 6 false null-consistency errors; added → PASS.

## Routing (LD-0116)
- RAVC2-Request → ws COO (ratify-GREEN trigger)
- DUAL-BAR RE-VERIFY → ws CVO (gates Stage 2; flagged SPA-detector decision)
- STAGE 2 GO-PREP → AE 0.7~A (env-var checklist: TERM_TAXONOMY_VERSION=v3 + SCORING_WEIGHTS_VERSION=v0.3; IAM s3:GetObject on scoring-weights)
- FORWARD-CONTRACT ANSWER → DS~E (v0.7.3 gold schema field list for .023)
- HARNESS-PASS → DS~A (.035 gate green; eligible-set 5→4 shift note)
- SPEC-SHIPPED → ws CTO (ARCH-ASK loop closed)

## Standing
RAVC2-submitted. Cascade: my ship ✓ → DS~A discrimination_pass ✓ → CVO re-verify (next) → COO ratify-GREEN → AE 0.7~A combined-apply + Stage 2 99-IMO GO. Harness/scaffold artifacts in .runtmp/find-insure-stage1/ (regrade_v073.py + stage1_scores_v0.7.3.json + regrade_v073_result.json). Next /work tick checks for CVO re-verify + COO ratify disposition.
