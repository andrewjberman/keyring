# work_1544Z — FIND_INSURE Deliverable-6 curated contact-target list COMPLETE (CVO A+B folded)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, COORDINATE

**Agent:** 0.1.0_DS_MarketIntelligence~C — /work tick executing COO Deliverable-6 DRIVE_TO (1535Z)

## Headline
Built + emitted FIND_INSURE Deliverable-6 (Andrew morning-review curated per-company contact-target list) from the .024 org-chart roster, folding both CVO .024 relevance findings (A keyword-collision + B AM-domain weighting per CTO design). serving/contacts-target-2026-05-27.json: 24 companies, 114 curated rows. RAVC2 → CVO relevance-verify.

## What this cycle did
1. EXIT-RAMP assessment: buildable-now v1 from org-chart roster + company-score; Phase-2B hiring overlay DEFERRED (not a hard gate); reveal-gate doesn't block (non-PII list ≠ reveal). COO confirmed all 3.
2. NEW serving/build_contacts_target.py: pure build_target_list (per-IMO top-N by decision_relevance_score = employee_score × am_domain_relevance) + boto3 main (gold employees_scored ×24 + scoring.json + silver departments → contacts-target JSON, SSE-KMS).
3. CVO finding (A): score_linkedin_gold title matcher suppresses AM keywords in non-financial titles. 24 gold re-scored (gold-only, no Lusha).
4. CVO finding (B) per CTO ruling 1530Z: NEW config/title-domain-taxonomy-v1.json (person-function axis, separate from term-taxonomy-v3); soft multiplier on DERIVED score (not employee_score); non-financial 0.15 / financial+leadership 1.0 / neutral 0.5.
5. Held the review-facing emit until B (dry-run proved IT directors dominate v1 — emitting that to Andrew would surface wrong people); emitted only after B made it review-ready.

## Empirical validation (CTO Q2 ordering-invariant)
- allianz-life: CIO + Director-of-IT (dominated v1) dropped; "Head of Ventures" + "Distribution Sales" surface.
- national-life: "Portfolio Management" + "Distribution Technology" top; data-ops demoted.
- american-general: CEOs (principals) surface.
Caught a leadership-token bug ('president' matched 'Vice President' → re-rewarded seniority; am_domain_relevance is function-only). dw=0.15 confirmed.

## Commits (origin/CLOUD)
49d8affdd (emitter v1 + finding A) → d535d4324 (finding B taxonomy + classifier + emit).
EMITTED: serving/contacts-target-2026-05-27.json (124991 bytes).

## Deferred (noted, non-blocking)
Phase-2B hiring overlay (v1.x); residual title-precision (e.g. "Application Development" → neutral not non-financial) = v1.x tuning Andrew's review surfaces.

## Compiler Tools
None — serving emitter + external-relevance scoring; no pipeline dependency tracing. Re-score was gold-only local (no Lusha, no SSM).

## Discipline
- ds-commit-gate clean all commits; safe-commit scoped. 34/34 emitter tests + gold suite green.
- feedback_validate_classifier_against_real_data: tuned the B down-weight empirically on real rosters per CTO, not in the abstract.
- Held emit on quality gate (B) rather than ship review-misleading v1 — COO affirmed.

— 0.1.0_DS_MarketIntelligence~C 2026-05-28T1544Z [work-cycle:0004]
