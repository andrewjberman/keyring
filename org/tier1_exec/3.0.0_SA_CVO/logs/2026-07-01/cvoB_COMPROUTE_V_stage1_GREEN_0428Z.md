# CVO~B NFRA_COMPROUTE-V (PRD s9 Stage-1 acceptance) -- GREEN

**archetype:** VALIDATE

**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-01 | **Window:** ~0424-0428Z (pre-fire window, parallel with ~B staging Phase-B)
**Trigger:** COO~B close-verify slate item 3; ~C flagged L4 landed (442633124) -> Stage-1 EXIT-complete (L1+L2+L3+L4), COMPROUTE-V ungated. Evidence pre-positioned by ~C + ~E.
**Artifacts:** `org/modules/graph/comp_route.py` (~E L3 engine) + `comp_capability_provider.py` (~C provider) + `.tools/comp-which-routing-test.py`. Grounded by EXERCISING the self-tests on the live artifacts, not the producers' self-report.

## VERDICT: **GREEN** -- all four PRD-s9 properties independently confirmed. Closes COMPROUTE Stage-1.

## s9a -- Goodhart-honesty = GREEN
`comp_route.py --self-test` -> `goodhart.outcome_beats_count`: good(n=4)=0.722 > spammy(n=80)=0.029. The learned history_affinity is OUTCOME-weighted (result_class/outcome_value), NEVER invocation count; the flywheel sink carries outcome=None filled at USE-time. One-signal: COMPLEARN reuses THIS outcome-weighting (test_reuses_comproute_l3_outcome_weighting PASSED in the COMPLEARN suite) -- no divergent value model.

## s9b -- routing-quality + never-silent-argmax = GREEN
- Engine self-test 13/13: A.disambiguation (both comp-cluster+comp-transform surfaced WITH concern), A.prior_contributes, B.prior_not_sufficient (same-surface prior necessary-not-sufficient), C.prior_not_filter (transform prior=0.0 still surfaces -- PRIOR-not-FILTER inviolable), coldstart routes.
- Routing regression (`comp-which-routing-test.py`) PASS, ZERO rail regression: TEST-1 34/34 self-route + TEST-2 3/3 audit + TEST-3 20/20 NL-paraphrase + TEST-4 3/3 COMPROUTE-posterior LIVE against the real 49-cap provider (never-silent-argmax + PRIOR-not-FILTER + cold-start resolve).

## s9c -- generalization-interface-real = GREEN
`smoke.routes_unchanged` + `smoke.picks_fiction` PASS: a SmokeCapabilityMapProvider from a NON-comp-tool domain (fiction-shelf) routes through the SAME engine UNCHANGED, picking the fiction target. This is the DECISIVE proof the engine core is provider-agnostic -- a core that assumed comp-tools could not route a fiction-domain provider. (37 "comp-" string refs exist in the module, but all in the __main__ self-test/docstrings; the smoke-provider EXERCISE proves the core carries no comp-tool assumption -- exercise binds over grep.)

## s9d -- four-way separation = GREEN
- **Provider = PRIOR only:** comp_capability_provider.py has NO score/argmax/decide/route/margin function (grep-confirmed; the only "posterior" ref is a docstring naming its consumer). It provides capabilities + surface_prior + affinity_key, nothing more.
- **Engine = DECIDES:** comp_route.py owns the scorer weights + the eps=0.05 MARGIN-DISAMBIGUATION gate + never-silent-argmax.
- **COMPUNIFY = MAPS** (the 49-cap ledger, V1-certified separately) / **COMPLEARN = TRAINS** (the outcome flywheel, P2-certified separately). No peer re-implements another; the one shared signal (outcome_value) is reused, not forked.

## Honest scope (verified accurate, NOT over-claimed)
~C's scope note holds: the posterior is a FAIL-SAFE grep-TAIL backstop -- comp-which wires it as an advisory/read-only manifest-fuzzy backstop that acts only where the VETTED routing layers are silent (the uncurated long tail), NOT the primary decider. Confirmed in the comp-which wiring ("vetted routes for the high-value long tail ... backstop covers the rest"; "Advisory/read-only"). A SAFE Stage-1 posture; the flywheel accretes toward primary in later stages (Goodhart-gated by me then). No over-claim.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp_route.py --self-test` | s9a Goodhart + s9b routing-quality + s9c generalization | PASS -- 13/13 (incl goodhart.outcome_beats_count, smoke.routes_unchanged) |
| `.tools/comp-which-routing-test.py` | s9b live routing regression vs the real 49-cap provider | PASS -- 34+3+20+3, ZERO rail regression |
| grep on comp_capability_provider.py / comp_route.py / comp-which | s9d four-way separation + backstop-scope structural check | PASS -- provider PRIOR-only, engine decides, posterior wired as silent-tail backstop |

What worked: the s9c smoke-provider EXERCISE is the decisive generalization proof -- a fiction-domain provider routing unchanged binds over any grep count of "comp-" strings (exercise-or-evidence). Verifying the backstop-scope wiring confirmed ~C's honest scope note is accurate, not an over-claim (a semantic-axis check). Gap: none blocking.

## Next Steps
1. **[2.0.0_SA_COO~B]** GREEN -> close COMPROUTE Stage-1.
2. **[3.0.0_SA_CVO~B]** Phase-B LANDING verify (HIGHEST, on ~B fire) + COMPDRIFT close-verify (~D P3(c)/P4). Both event-gated.

-- 3.0.0_SA_CVO
