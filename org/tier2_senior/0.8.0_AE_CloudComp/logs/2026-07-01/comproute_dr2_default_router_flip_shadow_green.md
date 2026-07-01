# Session log -- 0.8.0_AE_CloudComp~C -- NFRA_COMPROUTE.DR2: the default-router FLIP (shadow-GREEN, SEV1)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE
**window:** 2026-07-01 ~13:00Z -> ~14:25Z

## Current State

Andrew-direct re-scope: comp_route promoted from grep-tail backstop to the DEFAULT router. DR2 (my slice:
surface + shadow + rail + flip) is COMPLETE + LIVE. comp-which is a SEV1 fabric-wide surface (~639x/14d),
so the flip was shadow-proven 0-regression BEFORE landing, hard-gated on CVO~B's independent DRV cert.

**Design converge (COORDINATE):** grounded in having built the L4 backstop (+ hit the 4-route regression),
I gave COO~B/CTO the fold-as-prior design (fold curated/surface-first/fuzzy as PRIORS -> fixes my L4
regression root-cause: the old posterior IGNORED the vetted signals) + shadow-first + 2-tier intent rail.
~E sharpened it: STRUCTURAL DOMINANCE (vetted band [1.0,2.0) by construction > base band [0,1) -> no-regression
a THEOREM, not a tuned weight) + engine-owned relevance-floor + E1 mode pre-filter. CTO blessed (132556Z).

**Built (my DR2 slice):**
- `comp_which_signals.py` (2033b8d70): the 3 SignalExtractors reusing comp-which's live signal fns via
  importlib (curated/surface-first VETTED, fuzzy confident->VETTED else soft), mapping to the locked
  {cap_id,confidence,vetted} interface; + the 2-tier intent classifiers (classify_command syntactic
  navigate/compute; classify_query_intent NL read/compute). No comp-which refactor.
- `comp_route_shadow.py` (2033b8d70): the SHADOW harness -- primary-router (route()+extractors) vs the
  BACKSTOP (comp-which LIVE) over the full 34+3+20+3 fixture -> SHADOW-GREEN (0 regression, 0 primary-vs-
  backstop divergence, read-never-rebuilds, fallback-rate 9.2% over 65 = sane).
- `comp_capability_provider.py` (2033b8d70): routable set now = the actual routing targets (pipescript/
  comp-build/comp-coverage/comp-drift/comp-registry routable; search-primitives/gates/router/session/test
  non-routable); + E1 cap.write_path from ~B's DR3 manifest tags, WHOLE-write-tools only.
- THE FLIP (94b64a5af): `.tools/comp-which` main() -> _default_router (comp_route.route + extractors) as
  the DEFAULT path; decision/disambiguation prints call+concern+rail-log; below-floor -> comp-grep/glob
  (never-dead-end); any error -> LEGACY cascade (fail-safe). CVO~B DRV-certified (4c1d93be5), Andrew-authorized.

**Two findings I surfaced (grounded, both accepted):**
- pipescript wrongly non-routable -> 5 of the original 9 shadow regressions. Fixed the routable set (aligned
  to the manifest tools_index). (Andrew flagged pipescript-for-pipelines; grounded that pipescript is the
  WHOLE-estate named-thread router -- gold is only ~10% (14/135 sub-threads) -> "goldscript" misnames it;
  comp-pipescript is already the gold tool.)
- E1 granularity: ~B tagged 3 manifest ENTRIES write_path -> tools comp-aws/comp-build/comp-lambdamap, but
  only comp-build is a WHOLE-write tool; comp-aws/comp-lambdamap ANSWER reads, so tool-level write_path=True
  on them over-excludes their reads (shadow-confirmed). So my provider computes write_path per-tool =
  (all entries write_path) -> comp-build ONLY. ~E CONCURRED + independently verified. The derive subcommands
  are compute-intent writes (free, never read-routed).

## Compiler Tools

| tool | use | result |
|---|---|---|
| comp_route_shadow.py | the SEV1 zero-regression gate: primary vs backstop over the fixture | iterated 9 -> 5 -> 3 -> 0 regressions; final SHADOW-GREEN (0-reg/0-div/read-never-rebuilds/9.2% sane fallback). |
| comp-which-routing-test.py (LIVE post-flip) | DR2 phase-3 gate: the fixture through the FLIPPED comp-which | PASS -- 34/34+3/3+20/20+3/3. Shadow 0-regression held live. |
| comp-surface-check | SEV1 gate on comp-which (the flip commit) | OK -- no critical surface broken. |
| ds-commit-gate + ruff + non-ASCII | py_compile/ruff py39 on the 3 modules + ast on comp-which | clean; ASCII-only. |
| comp_capability_provider (conformance) | provider still conforms after routable+write_path | PASS -- 50 caps, six s3 fields, generalization. |

**What worked:** the shadow-first discipline is the whole SEV1 story -- it caught the pipescript-routability
+ the extractor mis-reproductions (curated all-calls, confident-fuzzy-vetted) BEFORE any live flip, and the
primary-vs-backstop-LIVE diff proved 0 divergence against comp-which's real output. **Gap found:** two real
ones (pipescript routability + E1 tool-level granularity), both fixed + concurred. No estate comp-tool
substitutes for the shadow (it IS the ground-truth reproduction harness).

## Blockers

**None.** DR2 COMPLETE + flip LIVE. Open: CVO~B's post-flip enforcing-surface confirm (closes DR2 -- the flip
is live + verified; her re-confirm is the independent close). I hold the rollback trigger (git revert
94b64a5af) if any live regression surfaces (rollback-not-fix-forward, SEV1). Not assumption-blocked.

## Next Steps

1. **[3.0.0_SA_CVO~B]** post-flip enforcing-surface confirm (`python .tools/comp-which-routing-test.py` now
   exercises the flipped comp-which) -> closes DR2.
2. **[0.8.0_AE_CloudComp~E]** COMPLEARN-learns-it frontier: the adversarial-vocab paraphrases (weak match,
   never a dead-end) accrete via the routing.jsonl flywheel; the affinity step-4 swap when telemetry justifies.
3. **[0.8.0_AE_CloudComp~C / me]** hold the rollback trigger; the 2-tier RAIL enforcement (the PreToolUse hook
   wiring of classify_command) is the follow-on if COO~B/CTO sequence it. Still holding: GRAPHDEPTH P3 CVO cert,
   ~D handle re-wire, Phase-B co-sign, affinity step-4, F1, reciprocity-hardening.
