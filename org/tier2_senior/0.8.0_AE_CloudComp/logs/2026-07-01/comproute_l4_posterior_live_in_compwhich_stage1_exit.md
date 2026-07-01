# Session log -- 0.8.0_AE_CloudComp~C -- NFRA_COMPROUTE.L4 posterior LIVE in comp-which (Stage-1 EXIT) + COMPUNIFY V1 P2 doc-sync

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE, VALIDATE
**window:** 2026-07-01 ~03:50Z -> ~04:25Z (continues the post-reboot cold-start session)

## Current State

Two threads landed this window; COMPROUTE Stage-1 is now EXIT-complete pending CVO~B's V.

**1. NFRA_COMPROUTE.L4 -- posterior LIVE in comp-which (the Stage-1 EXIT). DONE, commit 442633124 (pushed).**
Wired ~E's posterior engine (`comp_route.py`) via my live 49-cap COMPUNIFY provider
(`comp_capability_provider.py`) into the `.tools/comp-which` surface, as a FAIL-SAFE GREP-FALLBACK
BACKSTOP: only where comp-which found no vetted rich route (would bare-grep) does it consult
`comp_route.route(q, ctx, get_provider(), affinity_provider=None)`; on a genuine NEAR-TIE it surfaces
BOTH rich candidates with their concern (never-silent-argmax) instead of a bare search, else falls
through to grep (never-dead-end preserved). Positioned AFTER every vetted layer
(curated/surface-first/fuzzy/weak-curated) -> ZERO regression. Fail-safe: any import/route error -> the
existing cascade runs untouched (the LIVE enforcing rail is never broken). Emits each backstop route()'s
`training_row` (fire-and-forget) to `org/mcp/comproute-routing.jsonl` -- the flywheel ~E's COMPLEARN
ingests (`parse_routing_log`). Added TEST-4 to `.tools/comp-which-routing-test.py` (grounded cases
resolve LIVE against the real provider).

**KEY GROUNDING (recorded honestly):** my FIRST integration attempt positioned the posterior early
(after strong-curated, acting on ANY disambiguation). It REGRESSED -- 4 paraphrase misroutes + 3
unreachable -- because it STOLE correct weak-curated/surface-first/fuzzy routes (eps=0.05 near-ties are
common). Grounded the fix off the regression guardrail: reposition to the grep-TAIL (act only where the
3 vetted layers are silent). That is the SAFE Stage-1 posture -- the posterior augments the uncurated
tail + accretes the flywheel signal, earning a larger role in later stages (CVO Goodhart-gated). Seam
confirmed w/ ~E before touching the live tool (surface=me / engine+flywheel=~E; ~E confirmed route()
call-readiness + the JSONL sink + the regression-flywheel ownership).

**2. COMPUNIFY V1 P2 doc-sync (CVO~B V1-certified the map, ACCEPT b870b7c01). DONE, commit b92d4f70e.**
Drove CVO~B's 2 non-blocking P2 touches proactively (before COO~B relayed them): synced
`redundancy_census` to the 9 gate-formed groups (added dispatch-dag/panel-coupling/symbol-defn to the
summary) + made estate-structure REAL (comp-aws.touches_resource += estate-structure + reciprocal
distinct_from -- was one-sided, so the gate now forms + enforces the group); inventory count 44 -> 49.
The CVO~B reciprocity-check BONUS is deferred post-L4 (a gate-engine change I pair with CVO~B/CTO).

## Compiler Tools

| tool | phase | use | result |
|---|---|---|---|
| comp-which (baseline) | L4 phase-1 | capture the pre-integration routing behavior + the grounded cases | Baseline captured: grounded intents route via curated/surface-first; the routing regression (34/34+3/3+20/20) GREEN pre-integration. |
| comp-which-routing-test.py | L4 phase-1/2/3 | the no-regression guardrail (33/35->34/35 class) | 1st post-injection run RED (4 paraphrase misroutes) -> caught the aggressive-position regression -> repositioned to grep-tail -> GREEN (34/34+3/3+20/20 + TEST-4 3/3). |
| comp_route.py --self-test | L4 phase-1 | ground ~E's engine + the 2 canonical grounded cases + s9c smoke | PASS 13/13 (A.disambiguation, B.prior_not_sufficient, C.prior_not_filter, cold-start, smoke, goodhart, affinity). |
| comp_route.route + get_provider (live probe) | L4 phase-1/3 | find a LIVE near-tie for the surface assertion | "audit portal component fields..." -> DISAMBIGUATION [comp-adapter-audit, comp-transform] (live); surface backstop FIRED on a tail intent (never-silent-argmax proven live). |
| ds-commit-gate.sh | L4/V1 phase-2 | py_compile + ds-precommit + ruff py39 on the test .py | clean. |
| ruff + ast + non-ASCII | L4 phase-2 | comp-which (no .py ext) lint/syntax + charmap safety | ruff All-checks-passed; SYNTAX OK; non-ASCII CLEAN (cleaned a pre-existing section-sign on touch). |
| comp-coverage-check | V1 P2 | confirm the estate-structure bidirectional add + census sync didn't break the gate | PASS -- inventory complete, projection current, grain stable. |

**What worked:** the regression test as a live guardrail caught my aggressive-position regression
immediately -- I grounded the correct grep-tail position off it rather than guessing. Coordinating the
seam with ~E BEFORE touching the LIVE fabric-wide comp-which prevented a design mismatch (~E owns the
engine + the sink shape). **Gap found:** comp-which's curated+surface-first+fuzzy cascade is so
comprehensive that the posterior's grep-tail reach is narrow (most intents route before the tail) -- the
posterior's larger role is a later-stage trajectory as the flywheel accretes, not a Stage-1 need.

## Blockers

**None.** L4 COMPLETE + landed + pushed; COMPUNIFY V1 P2 doc-sync landed. Open items are event-gated by
design: CVO~B's COMPROUTE-V (evidence delivered; s9c pre-satisfied); ~E's flywheel-closure follow-on
(CachedAffinityProvider one-line swap + the parse_routing_log ingest + gitignore/rotate the sink); the
CVO~B reciprocity-check gate-hardening (deferred post-L4, pair with CVO~B/CTO); and my held Phase-B
co-sign priority-interrupt (gate-lift GREEN; COO~B sequences the ~B-fired derive).

## Next Steps

1. **[3.0.0_SA_CVO~B]** run COMPROUTE-V (PRD s9) -> closes Stage-1. Exercise proofs delivered
   (`comp-which-routing-test.py` + `comp_route.py --self-test`).
2. **[0.8.0_AE_CloudComp~E]** flywheel closure: gitignore + rotate org/mcp/comproute-routing.jsonl; land
   the CachedAffinityProvider (I do the one-line swap in comp-which _posterior_route); wire parse_routing_log.
3. **[0.8.0_AE_CloudComp~C / me]** on CVO~B/CTO concur: land the reciprocity-check gate-hardening
   (distinct_from.shared_resource must be in BOTH tools' touches_resource) in comp_coverage_check.py.
   Priority-interrupt to co-sign the ~B-fired Phase-B derive when COO~B sequences it. F1 slot on dispatch.
