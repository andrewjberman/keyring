# NFRA_GRAPHUNI + NFRA_GRAPHDEPTH — Substrate Close-Out Map

**Owner:** 2.0.0_SA_COO~B | **PRDs:** `docs/architecture/NFRA_GRAPHUNI_PRD.md`, `docs/architecture/NFRA_GRAPHDEPTH_PRD.md` | **Authored:** 2026-07-01 (get-ahead close-out plan)
**Current:** GRAPHUNI P0 (D1-audit + CVO-fixture) DONE; P1 (D1-fill = the Phase-A + Phase-B population) FIRING NOW (~B's ONE Phase-B derive, denom 232). GRAPHDEPTH P0 (contract+gate) landed; P1 (populate) rides GRAPHUNI P1; P2 (calibration = COMPUNIFY S4) DONE (COMPUNIFY closed). The remaining close-path is the UNIFICATION payoff (re-point + retire) + depth-tooling.

## Why this is the highest-value tail
The Phase-B stale-cache PHANTOM we just caught (a deleted script `INF_D_00e` folded from `~D`'s pre-reboot `.comp-graph/graph.json` local cache) is EXACTLY the class GRAPHUNI D2/D3 kills: tools reading LOCAL caches at DIFFERENT vintages instead of the ONE marker-published HEAD. Closing D2/D3 structurally prevents the next stale-cache phantom.

## GRAPHUNI remaining (P2 + P3) -> owner ~D (registered GRAPHUNI build lane); CVO~B gates

| phase | = | scope | gate |
|---|---|---|---|
| **P2 (D2)** | re-point | ONE shared marker-headed read-API (extend the `comp-kuzu` path, NOT per-tool per PRD ruling 2); re-point comp-blast/trace/xref/platinum to read the Kuzu projection AT the marker head (retire the `.comp-graph/graph.json` local-cache reads). | no-regression: re-pointed tools return SAME answers as the pre-delta frozen fixture (CVO~B-owned, captured P0). re-point-THEN-retire, CVO-gated (ruling 3). |
| **P3 (D3+D4)** | retire + assert | retire the local caches + comp-build's separate build; ASSERT one-head (D4 = the generalized seam-4 in the read-API, ruling 4). | CVO~B set-equality + the D4 one-head assertion; D4 also threads as a COMPDRIFT seam AC (rides). |

## GRAPHDEPTH remaining (P3) -> owner ~D/~C; CVO~B gates
- **P3 depth-scoped tooling:** tools can scope by DEPTH (declared `level` on the CONTAINS ladder) not just breadth -- resource-grain vs function-grain queries. Reads + calibrates by grain (COMPUNIFY S4 grain_contract, already landed). 5 CTO rulings PRD s9 (depth-first-class / type-set-grows-by-semantic / size-invariant-bounded-materialization / type-specific-drilldown-depth). GRAPHDEPTH takes PRECEDENCE (LD-0229) as the foundational depth layer -- but its P1 rides GRAPHUNI P1 (firing) + P2 is done, so P3 is the last piece.

## Close-path
1. Phase-B derive LANDS (P1 D1-fill complete) -> CVO~B LANDING verify (nodes present + convergence 0-dangling on the populated graph, ledger L3) -> GRAPHUNI P1 + GRAPHDEPTH P1 complete.
2. GRAPHUNI P2 (re-point, ~D) -> P3 (retire+assert, ~D) -- each CVO~B no-regression-gated against the frozen fixture. This is the un-cache-ing that prevents the next stale phantom.
3. GRAPHDEPTH P3 (depth-scoped tooling, ~D/~C) -- rides the unified substrate.
4. On D4 one-head asserted + depth-tooling live + CVO~B set-equality GREEN -> GRAPHUNI + GRAPHDEPTH close.

## Dispatch: P2/P3 TOs to ~D fire the moment the Phase-B LANDING verify GREENs (I dispatch on that signal). Staged here so the plan is ready -- get-ahead-of-the-curve.
