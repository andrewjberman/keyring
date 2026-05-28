# FIND_INSURE W1-classification revision — ws CTO spec-author verdict (v0.7.3 candidate)

**Author:** 1.0.0_SA_CTO (PRD author, v0.7.1 cba505dfb + v0.7.2 ff27f57ef)
**Date:** 2026-05-28T~04:10Z
**Trigger:** DS~B FIND_INSURE.031 AC6 Stage-1 re-grade finding (`5f73af749` + brief `docs/briefs/find-insure-031-stage1-regrade-v07_1-finding-20260528.md`) + ws COO [ARCH-ASK W1-revision] `20260528T040941Z`
**Class:** ws-charter CVO_CONSULT → verdict pre-positioned for CVO empirical-corroboration → v0.7.3 REPAIR-AMENDMENT on CVO CORROBORATE
**Status:** VERDICT RENDERED; awaiting CVO /verify-channel empirical-corroboration before v0.7.3 PRD scribe + DS~B implementation

---

## 1. Finding accepted — my v0.7.1 §263 premise is empirically refuted

DS~B's AC6 re-grade against the actual Stage-1 silver (334 pages / 5 SUCCESS-class IMOs) is rigorous and the diagnosis is correct. I accept both findings without reservation:

- **F-1 (premise false):** §263 assumed pure-annuity carriers have `class_diversity=1`. Measured = **7** (Allianz: annuity 1530 + core-AM 329 + fiduciary 203 + advisory-business 19 + AUM-quant 8 + org-structure 5 + platform-partnership 1). A 100-200 page carrier corporate site incidentally fires generic financial-services vocabulary across marketing/careers/disclosure/corporate-structure copy. **Vocabulary diversity is an artifact of being a large financial company, not of transitioning into asset management.** The `class_diversity >= 2` gate fires for exactly the TN carriers it was built to exclude.
- **F-2 (regression):** adding annuity-product-vocabulary to POSITIVE `rollup_score` raised American Equity (correct v1 absent=20) to v0.7.1=91 (FP). A pure-annuity site is saturated with annuity terms; making them a positive signal lifts true-negatives into present. The amendment built to suppress annuity-carrier FPs instead amplifies them.

**Self-accountability note:** v0.7.1 §263 was authored from a synthetic/idealized premise (the Allianz fixture fires only annuity-vocab → class_diversity=1) that the full real corpus refutes. DS~B's implementation is faithful to spec; the spec's empirical assumption was wrong. This is exactly the Phase-1-first-empirical discrimination-quality gate working as designed — the catch prevented a 99-IMO burn on a classifier that FPs 3/4 present-verdicts. AC6-before-universe-burn is vindicated.

## 2. Root insight (DS~B's, ratified)

The discriminating signal is **NOT vocabulary diversity** (every large carrier has it) but **the prominence of genuine AM-transition evidence relative to the annuity-product baseline.** A pure-annuity carrier and a genuine AM-transitioner both have AM vocabulary on their sites; what separates them is (a) the presence of regulatory/structural markers you cannot have without actually running advisory (RIA self-reference, Form ADV, Series-65-in-advisor-context, IAR, advisory-AUM), and (b) the ratio of that high-signal evidence to the annuity baseline.

## 3. Verdict — CORROBORATE (2)+(3) as REQUIRED core; fold (1) as scoring mechanism + (4) as diversity re-scope

DS~B offered 4 candidate directions. My spec-author ruling on the v0.7.3 W1-revision design:

### REQUIRED (closes F-1 + F-2):

**A. High-signal-term gate as the present-eligibility predicate** [DS~B direction 3 + 4].
Present-eligibility REQUIRES at least one high-signal AM-transition marker in discriminating context — the regulatory/structural markers that cannot exist absent genuine advisory business:
- RIA self-reference ("our RIA", "[Firm] Advisors LLC / Asset Management LLC" as a named entity)
- Form ADV filing reference
- Series 65 / 66 in *advisor* context (NOT an isolated Series-6 on a careers page)
- IAR (Investment Adviser Representative) designation
- AUM stated in *advisory/managed* context (NOT annuity in-force / general-account assets)

Generic "asset management" / "wealth management" / "fiduciary" marketing prose does **NOT** satisfy the gate. This directly kills F-1: incidental vocabulary no longer qualifies a carrier as present.

**B. Annuity-product-vocabulary as dampener, NEVER positive rollup** [DS~B direction 2].
Remove annuity-product-vocabulary from positive `rollup_score` entirely. Reverts the F-2 regression (American Equity → ~20). Annuity-vocab instead feeds the ratio denominator (C).

### STRONGLY RECOMMENDED (the coherent scoring mechanism that B points toward):

**C. Relative-density ratio as the discrimination score** [DS~B direction 1].
`am_transition_signal = high_signal_AM_weight / (high_signal_AM_weight + annuity_baseline_weight)`.
- Pure-annuity carrier: annuity ≫ high-signal-AM → low ratio → absent (Allianz/Midland correctly excluded).
- Genuine transitioner: meaningful high-signal-AM relative to annuity → higher ratio → present-eligible.
This operationalizes "AM-transition prominence relative to annuity baseline" as a concrete, hand-tunable score. It is the natural implementation of the dampener (B) — I recommend v0.7.3 adopt it rather than a bare subtraction, because the ratio is scale-invariant (works the same on a 50-page site and a 300-page site, where a raw subtraction would not).

### FOLD (diversity-metric fix, if class_diversity retained at all):

**D. class_diversity re-scoped to high-signal classes only** [DS~B direction 4].
If `class_diversity` is retained as any signal, count it ONLY over high-signal classes {series-license, advisory-business, IAR, fiduciary-WITH-ADV-context, RIA-self-reference} — exclude generic core-AM / marketing-prose classes. A carrier incidentally has core-AM prose but NOT genuine RIA/ADV/IAR markers, so high-signal-only diversity becomes meaningful again. Alternatively, v0.7.3 may RETIRE class_diversity entirely in favor of the (A)-gate + (C)-ratio, which together carry the full discrimination load. **I lean RETIRE** — the gate + ratio are cleaner and class_diversity has now empirically failed twice (v0.7 single-threshold, v0.7.1 diversity-gate). Offering RETIRE-vs-rescope as the one open sub-question for CVO + DS~B input.

### Net v0.7.3 present-eligibility logic:

```
present  iff  high_signal_gate(A) satisfied
              AND am_transition_ratio(C) >= ratio_threshold   # initial-cal, Stage-2-empirical-tunable
adjacent iff  high_signal_gate(A) satisfied AND ratio below threshold
              OR (some AM signal but no high-signal marker)
absent   iff  no high-signal marker AND ratio low (pure-annuity / no-AM)
null     iff  blocked_upstream / scrape-failure / SPA-render-fail (unchanged)
```

Annuity-vocab contributes ONLY to the ratio denominator (B+C), never to positive rollup. Thresholds are EMPIRICAL-FIRST-RUN posture (per the AC2a / Q-C3 sister-pattern) — calibrate against the Stage-1 5-IMO SUCCESS subset at v0.7.3 implementation, validate that Allianz/Midland/American-Equity all land absent/adjacent + lincoln-investment stays present, before re-running Stage 2.

## 4. Stage 2 HOLD — CONFIRMED CORRECT

ws COO's HOLD on AE 0.7~A Stage 2 99-IMO universe-run is the right call and I confirm it. Running 99 IMOs through a classifier that FPs 3/4 present-verdicts burns the run + produces an IR-target list dominated by pure-annuity carriers the IR team cannot trust. **Stage 2 release gates on: CVO empirical-corroboration of this verdict → my v0.7.3 PRD REPAIR-AMENDMENT scribe → DS~B revised score_web_gold.py → re-grade validation on the Stage-1 5-IMO subset showing the 4 carriers correctly classified.**

## 5. Escalation judgment — CTO+CVO joint-decide, NOT Andrew-sovereign-blocking

This is a scoring-classifier-methodology revision within existing FIND_INSURE PRD scope — not new product strategy, not a new Directive, not S3/S4 procurement. Per LD-0022 (CVO priority architectural corroborator) + LD-0026 (joint-decide) + `feedback_andrew_non_response_1tick_route_to_cvo`: CTO+CVO joint-decide resolves this fork. Andrew is non-responsive (~04:10Z; said he reviews "in the morning"). The v0.7.1 amendment itself was resolved via CTO+CVO joint-decide without Andrew; this revision is the same class. **Proceed on CTO+CVO joint-decide; surface for Andrew's morning awareness; do NOT block on Andrew.** If CVO COUNTERs my direction, the divergence escalates per LD-0022; if CVO CORROBORATEs, v0.7.3 materializes immediately.

## 6. Routing

- **ws CVO:** empirical-corroboration ask — this IS the Stage-1-first-empirical high-leverage moment (`feedback_cvo_find_insure_focus_high_leverage_risk_moments`). CORROBORATE / COUNTER / CORROBORATE-with-additives on (a) the (b) inadequate-solution-coverage finding and (b) the §3 revision direction. Your verify-channel finding is the gate that authorizes my v0.7.3 REPAIR-AMENDMENT scribe per LD-0065. One open sub-question for your input: RETIRE vs re-scope class_diversity (§3.D).
- **DS~B:** stand by for ratified v0.7.3 spec. You MAY pre-stage scaffolding against the §3 direction (high-signal-marker term lists + ratio computation) since Stage 2 is safely HELD — but final RAVC2 + Stage 2 release gates on CVO corroborate + my v0.7.3 scribe. Your ~30-45min implement estimate is the critical-path; pre-staging compresses it.
- **ws COO:** Stage 2 HOLD confirmed correct; hold-coordination continues. v0.7.3 REPAIR-AMENDMENT TO will follow my scribe (post-CVO-corroborate). DS~B FIND_INSURE.031 stays open as the W1-revision implementation vehicle (or a new .035 — your decomposition call).
- **Andrew (morning awareness, non-blocking):** the v0.7.1 W1 classifier was empirically refuted at Stage-1 first-run; CTO+CVO resolving the v0.7.3 revision via joint-decide. Curated-contact-list + 99-IMO completion goal unaffected in shape — only the web-scrape scoring methodology is being corrected before the universe burn.
