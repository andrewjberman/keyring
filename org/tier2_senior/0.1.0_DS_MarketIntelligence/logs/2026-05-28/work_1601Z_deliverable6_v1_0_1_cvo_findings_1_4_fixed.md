# work_1601Z — Deliverable-6 v1.0.1: CVO PASS findings #1 (tech-portfolio collision) + #4 (EA seniority) fixed

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE

**Agent:** 0.1.0_DS_MarketIntelligence~C — /work tick on ws COO GO 1612Z (fix the 2 review-facing wrong-#1 defects from CVO Deliverable-6 PASS; bank #2+#3 v1.x)

## Headline
Deliverable-6 was CVO-PASS-accepted; CVO flagged 4 v1.x refinements. COO GO'd the 2 that put the WRONG person at #1 in Andrew's review list. Fixed both, re-scored gold + re-emitted (no Lusha), validated the 4 affected carriers. v1.0.1 RAVC2 + light CVO re-confirm routed.

## Fixes
- #1 tech-portfolio/investments collision (title-domain-taxonomy v1.1): "portfolio"/"investment(s)" in a tech-context title (technology/systems/architecture/data/ai/engineering/...) with NO strong-financial token → non_financial (0.15). Strong-financial (distribution/advisory/wealth/...) immune. Same class as finding A, different keywords. New tech_context/collision_financial/strong_financial token sets + collision branch in make_am_domain_relevance.
- #4 EA-seniority guard (score_linkedin_gold classify_seniority): Executive/Administrative Assistant + "assistant to the CEO/..." → "other" BEFORE the seniority patterns, so an embedded c-suite token doesn't over-credit support staff.

## Validated (the 4 CVO-flagged carriers, post re-score + re-emit)
- eagle-strategies: "Head of Technology Portfolio" #1 → gone (now neutral — sparse-AM annuity carrier honestly tops at non-AM roles).
- metlife: "Chief Architect…Investments…Systems" #1 → gone (now CFO/COO/CEO).
- national-life-group: "Portfolio Management Data and AI" #1 → gone (now "Head of Distribution Technology…" — strong-financial correctly immune).
- lifepro: "Executive Assistant to CEO" #1 → gone (now CEO/Founder/Head of Sales).

## Commits
42fe34ad3 (config + emitter + gold + tests). Re-emitted serving/contacts-target-2026-05-27.json (24 co/114 rows). gold suite + emitter 40/40 green.

## Banked v1.x (task #10)
#2 AIG entity-scoping (companies/search parent-vs-subsidiary); #3 hansen surname-parse ("Robert Undefined" + dup). More involved; fuller v1.x pass.

## Compiler Tools
None — serving/scoring refinement; re-score gold-only local (no Lusha, no SSM).

## Discipline
- ds-commit-gate clean; safe-commit scoped (5 files). feedback_validate_classifier_against_real_data: validated the collision rule on the actual 4 carriers, scoped strictly to CVO's keywords to avoid over-correction.
- Routed light CVO re-confirm (spot-confirm 4 carriers, not full re-verify) per COO — verify-before-ratify on the refinement.

— 0.1.0_DS_MarketIntelligence~C 2026-05-28T1601Z [work-cycle:0005]
