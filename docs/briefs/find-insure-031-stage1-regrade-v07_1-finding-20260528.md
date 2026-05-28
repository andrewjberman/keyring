# FIND_INSURE.031 — Stage 1 10-IMO re-grade under PRD v0.7.1: CRITICAL FINDING

**Author:** 0.1.0_DS_MarketIntelligence~B
**Date:** 2026-05-28T~04:05Z
**TO:** FIND_INSURE.031 AC6 (Stage 1 subset re-grade)
**Artifact:** `.runtmp/find-insure-stage1/regrade_v07_1_result.json` (harness `.runtmp/find-insure-stage1/regrade_v07_1.py`)
**Status:** AC1–AC5 mechanically complete + shipped; **AC6 re-grade DONE and surfaces F-1 (critical) — v0.7.1 does NOT achieve its FP-suppression goal on real Stage 1 data + introduces a regression.**

---

## TL;DR

I implemented PRD v0.7.1 (cba505dfb) faithfully — `class_diversity` field + `wm_classification` joint-logic + `class_diversity>=2` present-gate + annuity-product-vocabulary class + 1.2 multiplier cap. The **implementation is correct against the spec.** But the AC6 empirical re-grade against the actual 10-IMO Stage 1 silver **refutes the spec's central empirical premise** and shows v0.7.1 makes discrimination **worse**, not better, for 3 of the 5 SUCCESS-class IMOs.

This is exactly what AC6 (Stage-1 re-grade before the 99-IMO universe burn) exists to catch. **Recommend HOLD on AE 0.7~A Stage 2 universe-run until the W1 spec is revised.**

---

## Re-grade results (v0.7.1, term-taxonomy-v2, class_diversity_multiplier_cap=1.2)

| slug | exp | v1 score | v0.7.1 score | class_div | wm_classification | verdict |
|---|---|---|---|---|---|---|
| cambridge-investment-research | TP | 0 | 0 | 0 | absent | MISS (SPA-render-fail; 1 page only) |
| d-a-davidson-co | TP | 0 | 0 | 0 | null (blocked_upstream) | blocked-OK |
| lincoln-financial-group | TP | 0 | 0 | 0 | null (blocked_upstream) | blocked-OK |
| lincoln-investment | TP | 100 | 100 | 9 | **present** | **OK (TP)** |
| structured-asset-management | TP | 0 | 0 | 0 | null (blocked_upstream) | blocked-OK |
| allianz-life | TN | 100 | 100 | **7** | **present** | **FP** |
| american-equity-...life | TN | 20 | **91** | 2 | **present** | **FP (regression)** |
| liberty-bankers | TN | 0 | 0 | 0 | null (blocked_upstream) | blocked-OK |
| midland-national | TN | 100 | 100 | **7** | **present** | **FP** |
| the-preferred-annuity-group | TN | 0 | 0 | 0 | null (blocked_upstream) | blocked-OK |

**wm_classification distribution:** present 4 · absent 1 · null 5.
**Of the 4 "present" verdicts, 3 are TRUE-NEGATIVE carriers (Allianz, American Equity, Midland) — false-positives.** Only lincoln-investment (the lone non-blocked TP) is correctly present.

---

## F-1 (CRITICAL) — v0.7.1 class_diversity gate does not suppress pure-annuity-carrier FPs; the spec premise is empirically false

### The PRD premise

PRD v0.7.1 §263 + v0.7.2 §471 lineage state verbatim:
> "Allianz Life (TN, pure annuity carrier) `rollup_score=100` … but `class_diversity=1` (single annuity-product-vocabulary class saturating); v0.7 false-presents."
> "Midland National (TN) … `class_diversity=1`."
> "v0.7.1's `class_diversity >= 2` gate downgrades the Allianz + Midland class to 'adjacent'."

### The empirical reality (measured against the actual 200-page silver)

```
allianz-life      term_class_distribution:
  annuity-product-vocabulary: 1530   core-AM: 329   fiduciary-language: 203
  advisory-business: 19   AUM-quant: 8   org-structure: 5   platform-partnership: 1
  -> class_diversity = 7  (NOT 1)  -> present (FP persists)

midland-national  term_class_distribution:
  annuity-product-vocabulary: 950   advisory-business: 42   fiduciary-language: 30
  core-AM: 13   org-structure: 6   certification: 2   series-license: 1
  -> class_diversity = 7  (NOT 1)  -> present (FP persists)
```

**Root cause:** a large insurance carrier runs a 100–200 page corporate website that *incidentally* uses generic financial-services vocabulary — "asset management", "wealth management", "fiduciary", "FINRA", "investment advisor", an isolated "Series 6" — in marketing prose, careers pages, regulatory disclosures, and corporate-structure copy. That vocabulary diversity is an artifact of *being a large financial company*, NOT of *transitioning into asset management*. The `class_diversity >= 2` gate therefore fires for exactly the carriers it was meant to exclude. The premise "pure-annuity carrier ⇒ class_diversity=1" was an idealized assumption that the full silver corpus refutes.

## F-2 (CRITICAL — regression) — adding annuity-product-vocabulary to rollup_score raises true-negative scores

American Equity: **v1 rollup=20 (correct absent) → v0.7.1 rollup=91 (present FP).** The v2 annuity-product-vocabulary class contributed 900 matches of positive rollup signal that did not exist under v1. A pure-annuity carrier's site is *saturated* with annuity terms — so adding those terms to the positive rollup pushes true-negatives **up** into the present band. v0.7.1 inverts the intended effect for this IMO: the amendment built to suppress annuity-carrier FPs instead amplifies them.

---

## Why the implementation is nonetheless correct

`score_web_gold.py` computes `class_diversity` exactly per the term-taxonomy-v2 `consumer_contract` (metadata-aware count; annuity-vocab co-fire-conditional) and `wm_classification` exactly per PRD §257-260. 30+ self-tests pass, including the synthetic Allianz-pattern test — which passes *because the synthetic fixture fires only the annuity class*, matching the (false) PRD premise. The gap is between the spec's premise and reality, not between the spec and the code.

---

## Recommendation (architectural — ws CTO + ws CVO call, not DS)

The discriminating signal is not *vocabulary diversity* (every large carrier has it) but *the prominence of genuine AM-transition signal relative to annuity-product baseline*. Candidate directions for a v0.7.3 (or v0.7.1-revision) W1 cycle — offered for Tier-1 decision, not pre-decided:

1. **Relative-density ratio.** `wm_signal = AM_class_weight / (AM_class_weight + annuity_class_weight)`. Pure-annuity carriers have annuity ≫ AM → low ratio → absent; genuine transitioners have a meaningful AM:annuity balance.
2. **Annuity-vocab as dampener, not positive signal.** Exclude annuity-product-vocabulary from `rollup_score` (reverts American Equity to ~20) and/or subtract it. Reserve it purely as a negative/contra signal.
3. **High-signal-term gate.** Require specific RIA-transition terms in discriminating context (e.g., "our RIA", "Form ADV filed", Series-65 in *advisor* context) rather than generic "asset management" prose that appears on every carrier site.
4. **Diversity counted only over high-signal classes.** Count only {series-license, advisory-business, IAR, fiduciary-with-ADV-context} toward `class_diversity`; exclude generic core-AM marketing prose.

A combination of (2) + (3) most directly addresses both F-1 and F-2: it removes the regression-driver and replaces "any AM vocabulary" with "specific transition evidence."

---

## Routing + HOLD

- **AE 0.7~A:** recommend **HOLD Stage 2 99-IMO universe-run.** Running 99 IMOs through a classifier that false-positives 3 of 5 TN carriers in the validation subset burns the run + produces a target list the IR team cannot trust. Gate Stage 2 on the W1 spec-revision verdict.
- **ws CTO (PRD author):** F-1 + F-2 refute the v0.7.1 §263 empirical premise + surface a regression. v0.7.3 W1-revision cycle candidate.
- **ws CVO:** empirical-smoke-class verify finding — this is the Stage-1-first-empirical that the v0.7.1 amendment itself was triggered by (AE 0.7~A Stage 1 RAVC2). The re-grade shows v0.7.1's fix is inadequate-solution-coverage *again*; the (b)(i) gap the amendment targeted is not closed by the class_diversity gate against real data.
- **ws COO:** routing + Stage 2 hold-coordination.
