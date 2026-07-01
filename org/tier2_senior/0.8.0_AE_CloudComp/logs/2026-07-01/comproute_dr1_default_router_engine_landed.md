# NFRA_COMPROUTE.DR1 -- the default-router 3-stage engine LANDED (comp_route becomes the fabric's default router)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE, DIAGNOSE
**Serial:** 0.8.0_AE_CloudComp~E
**Date:** 2026-07-01
**Window:** COMPROUTE re-scope design-converge + DR1 build ~1300Z -> ~1347Z
**TO:** NFRA_COMPROUTE.DR1 (COO~B; the engine leg of the Andrew-direct default-router re-scope)

## Current State

Andrew re-scoped COMPROUTE: comp_route becomes the DEFAULT router (was ~C's fail-safe grep-tail
backstop). Design-converged with ~C + CTO + ~B, then built the engine. **DR1 = LANDED + committed +
TAGGED:** commit `8b0dd364e`, tag `comproute-dr1-v0.1.1`, pushed. self-test 22/22, pytest 13/13. CVO~B
greened the engine MACHINERY (build-readiness withhold on the flip cert, now cleared by commit+tag). The
flip itself is ~C's DR2, gated on CVO~B's shadow-green cert -- I did NOT touch comp-which live behavior.

## What was built -- the 3-stage route() (org/modules/graph/comp_route.py)

ONE engine serves BOTH roles (BACKWARD-COMPATIBLE -- extractors=None => exactly the legacy backstop):
- **STAGE A -- write-path pre-filter (E1):** a read/navigate intent (ctx.intent_class) excludes
  cap.write_path==True tools. Reconciles with PRIOR-not-FILTER (action-class/cost, not surface-relevance).
- **STAGE B -- banded score (structural dominance):** a VETTED signal (curated/surface-first extractor)
  scores 1.0+confidence in [1.0,2.0) via the `_VETTED_OFFSET=1.0` CONSTANT (fixed-by-construction, NOT a
  fixture-tuned weight -> no-regression is a THEOREM). curated (1.0->2.0) > surface-first (<1.0) by
  confidence-ordering = the existing "surface-first never steals a curated route" invariant, no
  special-case. Soft (fuzzy) adds into the base band [0,1); the base posterior = query+prior+affinity.
- **STAGE C -- confidence gate:** RELEVANCE FLOOR measured on RELEVANCE (vetted OR query+affinity+soft),
  NOT the surface_prior bias -- a high prior never rescues a zero-relevance intent -> below floor =>
  kind="fallback" to comp-grep/glob (never a forced misroute / dead-end). Margin gate disambiguates near-ties.

Fixes BOTH 4-paraphrase-regression causes: (a) posterior-overrides-vetted -> structural dominance; (b)
posterior-force-argmaxes-a-weak-match -> the relevance floor. SignalExtractor interface locked with ~C
(ex(intent,ctx_d)->[{cap_id,confidence,vetted}]); ctx.intent_class; cap.write_path/mode. affinity=None
this increment (its own shadow later; not coupled).

## Key engineering calls (grounded, self-corrected)

- **Relevance floor on RELEVANCE, not the total:** caught that surface_prior (0.16) would clear a 0.15
  floor and wrongly route a nonsense query -- fixed the floor to exclude the prior bias.
- **E1 keys on write_path, NOT mode (DR3 ~B finding):** ~B grounded that the manifest mode:rebuild tag
  CONFLATES ~3 genuine write-path tools (comp-aws-derive 8-min / comp-build / comp-lambdamap-write --
  EXCLUDE) with ~17 read-RECOMPUTE tools (comp-iam/comp-freshness/... -- ANSWER reads, KEEP). Excluding
  all mode:rebuild would be OVER-BROAD. Adopted ~B's option (B): an orthogonal cap.write_path flag; mode
  stays free for a future caching prior. Engine re-keyed to write_path; proven it excludes write-path +
  KEEPS read-recompute.
- **CTO GUARD folded:** a WRONG surface-first hit near-tying a correct curated -> DISAMBIGUATION (surfaces
  both, never silent-misroute); a lone wrong-vetted is bounded by extractor precision + shadow-measured.
- **Structural dominance is a THEOREM, not a tuned weight** -- the anti-Goodhart shape CTO + ~C both
  ratified (~C adopted it over their initial tuned w_c).

## Compiler Tools

| Tool | Command | Result |
|---|---|---|
| comp_route --self-test | 15 prior + 7 DR1 default-router checks | PASS 22/22 |
| pytest | test_comp_route (9 + 4 DR1) | PASS 13/13 |
| ds-commit-gate.sh | comp_route.py + test | PASS |
| safe-commit.sh + git tag | 8b0dd364e + comproute-dr1-v0.1.1 (~E author) | PASS (surface-check clean) |

**What worked:** designing the engine BACKWARD-COMPATIBLE (extractors=None => legacy) made the whole
build shadow-safe -- comp-which is untouched until the shadow cert flips DR2. Locking the interface with
~C before building meant the extractors compose exactly. **What failed / self-caught:** the floor-on-total
bug + the CachedAffinityProvider-style wrong-assertion instinct (caught the mode-over-broad via ~B's
grounding). **Gap found:** the concrete provider must SURFACE cap.write_path from the manifest tags for
E1 to be live (~C DR2 + ~B DR3); the abstract base capabilities() raising NotImplementedError is a
CVO-usage/get_provider() wiring point flagged to ~C.

## Blockers

None. DR1 engine done + committed + tagged. The E1 LIVE exercise (CVO~B gate-3) needs ~C's provider to
surface cap.write_path from ~B's manifest tags -- a real cross-lane hop being coordinated, not a blocker.
The flip is ~C's DR2 on CVO~B's shadow cert. Phase-B co-sign interrupt still armed.

## MCP traffic

~18 messages. Significant: Andrew-direct re-scope (via COO~B) -> design-converge (my engine input: 3-stage
+ structural-dominance + relevance-floor) -> ~C interface lock -> CTO RULING (GO, bless [1.0,2.0) band +
WRONG-surface-first guard) -> DR1 TO -> BUILD -> ~B DR3 write_path finding -> option-B fix -> commit+tag
v0.1.1 -> RAVC COO~B + CVO~B (gate-1 done, cert ref) + ~B (option B) + ~C (4 route() confirms).

## Next Steps

1. **[0.8.0_AE_CloudComp~C]** DR2: build the 3 extractors + comp-which restructure + shadow harness
   against v0.1.1; SURFACE cap.write_path on the concrete provider (get_provider()) from ~B's tags.
2. **[0.8.0_AE_CloudComp~B]** DR3: tag write_path=true on the ~3 write-path tools in the manifest.
3. **[3.0.0_SA_CVO~B]** DRV: cert the shadow-green (34+3+20+3 fixture + E1 read-never-rebuilds + fallback
   rate) against comproute-dr1-v0.1.1 -> authorizes ~C's DR2 flip.
4. **[0.8.0_AE_CloudComp~E / self]** confirm CVO~B when ~C's provider surfaces cap.write_path (E1 e2e);
   support the shadow if the engine needs any adjustment; COMPROUTE step-3 affinity outcome-capture (later).
5. **[me]** Phase-B co-sign priority-interrupt STILL ARMED.
