# NFRA_COMPROUTE.L3 -- the core posterior decision engine LANDED (lane ~E)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE
**Serial:** 0.8.0_AE_CloudComp~E
**Date:** 2026-07-01
**Window:** post-reboot cold-start (~0313Z) -> ~0348Z
**TO:** NFRA_COMPROUTE.L3 (COO~B GO 032749Z, Andrew-direct DRIVE-NOW; Stage-1 NOT gate-lift-gated)

## Current State

Post-reboot respawn of lane ~E. Cold-start protocol clean (/watcher Monitor b2t1toaky, org/XXX.md
startup, /cloud-ops). Reported READY -> COO~B, held ~4 min at the gate-hold, then COO~B GO'd
NFRA_COMPROUTE.L3 (un-gated -- Stage-1 reads the already-live COMPUNIFY map + tool_activity).

**NFRA_COMPROUTE.L3 = LANDED.** The core posterior decision ENGINE (the DECIDES verb's systems
alpha) built section-3-interface-first + provider-AGNOSTIC, coded to ~C's locked L2 contract,
committed `9cc595998` (org/modules/graph/comp_route.py, 615 lines), pushed origin/CLOUD. 13/13
in-module self-test + 9/9 pytest. VALIDATED against ~C's REAL provider (not just the smoke).

## What was built

`org/modules/graph/comp_route.py` -- `route(intent, ctx, provider [, affinity_provider]) -> decision
| disambiguation`:
- **Scorer** `w_q*query_match + w_s*surface_prior + w_h*history_affinity`; each term in [0,1], weights
  sum to 1. query_match = deterministic intent-token coverage (explainable). surface_prior = the
  provider-owned role_surface_affinity lookup (ADDITIVE). history_affinity = injected AffinityProvider.
- **MARGIN-DISAMBIGUATION gate** -- within eps of the top => surface ALL tied caps with concern; never
  silent-argmax (CTO ruling 3).
- **PRIOR-not-FILTER** -- every routable cap is scored+ranked; nothing excluded by surface (ruling 3).
- **history_affinity OUTCOME-weighted** (ruling 4): `outcome_weighted_affinity` = shrunk MEAN outcome
  value via m-estimate `(sum(v)+k*prior)/(n+k)`; result-class (PASS=1.0/FAIL-DENY=0.0/neutral=0.5) +
  gap_text bonus. Count enters ONLY as the confidence denominator n, NEVER the reward. tool_activity
  `matches` (a rail count) deliberately unused as reward -- the Goodhart trap.
- **Cold-start** -- no affinity => score = query + prior + margin, still routes (flagged).
- **Provider interfaces** (section-3, locked with ~C): `Capability` (6 binding + 3 enrichment fields),
  `CapabilityMapProvider` (capabilities()/surface_prior(key,ctx)/affinity_key(cap)), `AffinityProvider`.
- **Concrete providers**: `DictCapabilityProvider`, `DictAffinityProvider`, `ToolActivityAffinityProvider`
  (live tool_activity, best-effort, degrades to cold-start offline), fixture + smoke builders.

Companion `org/modules/graph/tests/test_comp_route.py` (9 pytest) -- owned-paths BLOCKED for AE
(tests/ lane=ANY_EXEC); routed to COO~B exec-land (SoD, mirrors my P0 drift-topology.yaml handoff).
In the working tree, clean, 9/9. The in-module --self-test already provides full acceptance repro.

## Compiler-tools mandate reproduction (every <run> + observed + pass/fail vs <expect>)

**Phase 1 (before write) -- inspect tool_activity for an OUTCOME dimension:**
- RUN: grounded the tool_activity schema vs the emitter SCHEMA (infra/aws/globgrph/tool_activity_emit.py
  L105+) + my P0 live-query log.
- OBSERVED: outcome-bearing cols present -- `result` (run result), `gap_text` (gap-found, "highest
  value"), `action` (rail action); `matches` is an int COUNT (the demand signal, NOT an outcome).
- vs EXPECT (outcome dimension, not just count): **PASS.** STOP-gate cleared -- history_affinity is
  outcome-weightable. (Design consequence: weight on result/gap_text; treat matches/count as the
  Goodhart trap, per ruling 4.)

**Phase 2 (before commit):**
- RUN: grep the engine core (route/_score_one/scorer/protocols) for concrete-map / "comp-tool" /
  hardcoded-tool-list assumption. OBSERVED: ZERO hits in route()/scorer; comp-tool names appear ONLY
  in the fixture DATA + docstrings/comments/self-test. No concrete-map import. vs EXPECT (zero): **PASS.**
- RUN: `from __future__ import annotations` first import + non-ASCII grep. OBSERVED: future-import
  present; 2 non-ASCII (`§` section-signs) FOUND -> FIXED to "section-3"; re-grep clean. vs EXPECT
  (clean, zero non-ASCII): **PASS after fix** (STOP-gate honored -- did not commit until clean).
- RUN: `.tools/ds-commit-gate.sh comp_route.py test_comp_route.py`. OBSERVED: blocked twice on ruff
  F401 (unused `field` import; unused `Capability` test import) -> removed both -> "All checks passed".
  vs EXPECT (clean): **PASS.**

**Phase 3 (after commit):**
- RUN: SMOKE-PROVIDER test -- a 2nd (non-tool library-domain) capability-map into route() with NO
  engine change. OBSERVED: `smoke.routes_unchanged` + `smoke.picks_fiction` PASS; live CLI
  `--provider smoke "look up a fact in the encyclopedia"` -> DECISION reference-desk. vs EXPECT (routes
  identically, section-9c): **PASS.**
- RUN: the 2 grounded validation cases (A comp-cluster->comp-transform within-margin; B
  comp-drift->comp-aws same-surface). OBSERVED: A.* all PASS (disambiguation, both surfaced, prior
  contributes 0.6 vs 0.7); B.* all PASS (prior EQUAL 0.8/0.8; prior-not-sufficient -- same top-2 with
  or without prior). vs EXPECT: **PASS.**
- BONUS RUN (L4-preview, exceeds criterion 3): my UNCHANGED engine against ~C's REAL 49-cap COMPUNIFY
  provider (landed 3277cc38a). OBSERVED: "what breaks if I change this fn"->comp-blast (correct);
  "is gold fresh"->comp-freshness/comp-chainrun disambiguation (correct); "iam perms"->comp-iam top,
  near-tie honestly surfaced. vs EXPECT (real provider slots in zero-change): **PASS.**

| Tool | Command | Result |
|---|---|---|
| comp-to | set session TO_ID = NFRA_COMPROUTE.L3 | PASS (race-free per-session) |
| comp-which | route "read tool_activity outcome-weighted affinity" | fell through to comp-grep (no dedicated reader tool; a gap -- tool_activity read is Trino/ECS-Exec, no comp surface) |
| comp-grep | locate tool_activity reader + schema in code | PASS (found emitter SCHEMA + comp-learns tooling) |
| ds-commit-gate.sh | comp_route.py + test_comp_route.py | PASS (after F401 x2 + non-ASCII fixes) |
| safe-commit.sh | 9cc595998 (engine, ~E author) | PASS (surface-check clean; tests/ correctly owned-paths-BLOCKED -> SoD handoff) |
| comp_route --self-test | the section-2 + section-9c acceptance repro | PASS 13/13 |
| pytest | tests/test_comp_route.py | PASS 9/9 |

**What worked:** grounding the tool_activity outcome schema on the emitter SCHEMA + my own P0 log
settled the Phase-1 STOP-gate airtight (outcome cols exist -> outcome-weightable). Coordinating ~C's
L2 contract BEFORE commit (3 locks) meant my engine consumed ~C's REAL provider with zero edit on the
first try. **What failed:** none blocking (2 ruff F401 + 2 non-ASCII, all fixed pre-commit; comp-which
has no tool_activity-read surface -- a known COMPLEARN gap, `comp-trino`/`comp-federation` would fill).
**Gap found:** no comp-tool fronts the tool_activity/Trino federation read (re-confirms my P0 finding).

## Blockers

None. L4 (comp-which wiring + regression-test unification) is COO~B-triggered + ~C-ready (integration
already de-risked live). The tests/ file needs exec-landing (SoD, RAVC'd to COO~B) -- not a blocker
(the in-module self-test carries the acceptance repro). tool_activity affinity is cold-start offline
by design -- accretes when L4 wires the live read; the prior+likelihood already route well at cold-start.

## MCP traffic

~8 messages. READY -> COO~B; ACK+GO L3; ~C L2->L3 contract ACK (3 locks) -> ~C CONFIRMED + real
provider landed; RAVC2 L3 LANDED -> COO~B (+ exec-land ask); CC CTO (rulings 2/3/4) + ~C (integration
green, ready for L4) + CVO~B (section-9 evidence pre-positioned).

## Next Steps

1. **[2.0.0_SA_COO~B]** ACK L3 (I self-mark complete on ACK); exec-land tests/test_comp_route.py; trigger
   L4 (comp-which integration + the 33/35->34/35 routing regression test unified with the flywheel).
2. **[0.8.0_AE_CloudComp~C]** on COO~B L4 trigger: co-integrate -- I import your Capability/provider
   directly (drop my field-identical local copy), wire surface_prior + affinity_key end-to-end.
3. **[0.8.0_AE_CloudComp~E / self]** L4 on trigger: wire the live tool_activity affinity read into the
   ToolActivityAffinityProvider row_source (replace the offline-degrading default); unify the routing
   regression test with the flywheel (each disambiguation = a test case + a tool_activity training row).
4. **[3.0.0_SA_CVO~B]** V (post L4): the section-9 acceptance evidence is pre-positioned + re-runnable.
5. **[me]** Phase-B co-sign priority-interrupt STILL STANDS -- break for the ~B-fired derive on gate-lift.
