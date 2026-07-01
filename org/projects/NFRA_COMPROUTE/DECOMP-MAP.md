# NFRA_COMPROUTE — Stage-1 Decomposition Map

**Owner:** 2.0.0_SA_COO~B (NFRA_COMP* program coordination) | **PRD:** `docs/architecture/NFRA_COMPROUTE_PRD.md` | **Authored:** 2026-07-01
**Drive posture:** Stage-1 is DRIVE-NOW (Andrew-direct 2026-07-01). Its inputs (the live COMPUNIFY map + ~E's live `tool_activity` + the rail-log) all exist NOW — it is NOT gate-lift-gated. Only the GRAPHUNI Phase-B *derive* is gate-lift-gated; COMPROUTE reads the already-live COMPUNIFY map, so it proceeds in parallel.

## The engine (PRD §2) — one line
`score(cap) = w_q·query_match(intent, cap.keywords) + w_s·surface_prior(cap.surface, ctx) + w_h·history_affinity(cap, role, ctx)` + a MARGIN-DISAMBIGUATION gate (never silent-argmax) + PRIOR-not-FILTER invariant + graceful cold-start.

## THE INTERFACE CONTRACT (PRD §3) — the binding spec both legs build to
`route(intent, ctx, capability_map_provider) -> decision | disambiguation`
- A **capability-map provider** exposes, per capability: `{id, keywords, surface, grain, concern, affinity-key}`.
- The engine / scorer / margin-gate / invariants are **provider-AGNOSTIC** — they never assume "comp-tool". The comp-tool map (COMPUNIFY) is merely the FIRST provider. Stages 2-3 = new providers, NOT a re-architecture. (CTO ruling 2 — any Stage-1 code that assumes "comp-tool" is a finding.)

## Stage-1 legs

| leg | owner | scope | status | depends on |
|---|---|---|---|---|
| **L1** | ~E | comp-dispatch + comp-symbols + 3 route-fixes (the surfacing primitives) | DONE (d804ff744 / e5ae5dd7a) | — |
| **L2** | ~C (COMPUNIFY governor) | the capability-map PROVIDER (§3 interface) from the LIVE COMPUNIFY map + the `role->surface_affinity` table hook. Registration = governor's act (§5). | **PENDING — DRIVE-NOW** | live COMPUNIFY map (S4-AUDIT GREEN, available) |
| **L3** | ~E | the CORE POSTERIOR ENGINE: scorer + margin-disambiguation gate + PRIOR-not-FILTER + cold-start; §3-interface-first (codes to the provider interface, never the concrete map); smoke-provider baked into acceptance. `history_affinity` = OUTCOME-weighted off ~E's live `tool_activity` (Goodhart, CTO ruling 4). | **PENDING — DRIVE-NOW** | the §3 interface (this doc / PRD §3) for parallel start via smoke-provider; L2's real provider for integration |
| **L4** | ~E (+~C integ) | integrate the posterior into the `comp-which` surface + the routing regression test (33/35 -> 34/35) UNIFIED with the loop (each disambiguation = a test case + a `tool_activity` row) | STAGED (post L2+L3) | L2, L3 |
| **V** | 3.0.0_SA_CVO~B | acceptance verify (PRD §9): Goodhart-honesty + routing-quality ground-truth + generalization-interface-real (smoke-provider) + four-way separation holds | STAGED | L2, L3, L4 |

## Sequencing / parallelism
- **L2 and L3 run in PARALLEL now.** L3 starts against the §3 interface + a smoke-provider (does not wait for L2's concrete provider); L2 builds the real COMPUNIFY-backed provider. They converge at L4 integration. The PRD §3 contract IS the shared interface spec — no separate Pattern-0 alignment thread needed (the PRD is the contract).
- **Not gate-lift-gated.** COMPUNIFY V1 acceptance (CVO~B, on gate-lift) is ADDITIVE to the already-GREEN map; L2 builds against the live map now and flags COO~B if V1 surfaces any map delta. L3 is insulated by §3 (interface, not concrete map).
- **Wave coherence preserved:** ~C/~E each keep their Phase-B priority-interrupt (co-sign at the ~B-fired derive) — COMPROUTE build yields to the derive if the gate lifts mid-build, then resumes.

## The 2 grounded validation cases (PRD §2 — L3 must resolve both)
- (A) `comp-cluster -> comp-transform` (within-margin CROSS-tool): PRIOR narrows + MARGIN disambiguates.
- (B) `comp-drift -> comp-aws` (SAME-surface): surface-prior EQUAL, can't disambiguate -> proves prior necessary-not-sufficient -> LIKELIHOOD + MARGIN(by concern) fix.
