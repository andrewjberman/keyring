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

## AMENDMENT 2026-07-01 -- P2 re-point RULING (CTO+CVO~B joint, ~D grounded finding)
~D ground-truthed (3 probes) that the unified NESSIE compute slice is NOT coverage-equivalent to build_graph's pre-delta trace graph (s3 edges FUNCTION-grain vs SCRIPT-grain, deferred reads -> fewer cross-script bridges, key-form heterogeneity) -> re-pointing comp-blast onto the literal Kuzu projection LOSES coverage (e.g. D_01.partner_analytics blast 216->13). RULING (CTO 054849Z, joint w/ CVO~B fixture-bar):
- **(b) NOW = the P2 close path:** re-point the tools to a HEAD-PINNED build_graph (ONE vintage, no divergent local caches). Satisfies ruling-2's ANTI-DRIFT INTENT (kills the divergent-cache phantom class -- the actual D2/D3 goal) + retains 216 coverage BY CONSTRUCTION (head-pinned build_graph IS build_graph's full extraction = the fixture's source, so set-equality holds). A tool reaching 13-not-216 is BROKEN -- correctness/coverage outranks the literal "read the Kuzu projection" substrate. GRAPHUNI P2/P3 (re-point + retire + D4) closes on (b).
- **(a) DEFERRED = the true-unification follow-on workstream (GRAPHUNI compute-slice FIDELITY):** re-populate the Nessie compute slice at build_graph fidelity (script-grain s3 + full reads + key-form + cross-script bridges) so the LITERAL Kuzu-projection re-point set-equals build_graph. Gated on PROVEN coverage-equivalence BEFORE the literal re-point (never-widen). ~D owns. NOT a close-blocker for (b); carried honestly, not a silent descope.
- **(c) re-baseline the fixture:** REJECTED (abandons no-regression).
- **SUBSTRATE-GAP FINDING (filed):** the Nessie graph currently UNDER-COVERS cross-script data-flow vs build_graph (function-grain vs script-grain, fewer bridges) = a real GRAPHUNI/GRAPHDEPTH population completeness note, addressed by the (a) workstream.

### CVO~B fixture-bar conditions on the (b)-GO (055216Z -- BINDING on the close)
1. **Validate per-tool vs a FRESH build_graph baseline** (reconciled for grounded post-06-30 source-deltas, e.g. the INF_D_00e deletion) -- NOT a byte-strict compare to the stale frozen fixture (which would false-RED a correct re-point on legit source-drift). CVO~B set-equality-gates EACH re-pointed tool vs fresh-build_graph.
2. **HONEST CLOSE LABEL (do NOT over-claim):** GRAPHUNI P2/P3 closes as **VINTAGE-unified** (anti-drift, D4 one-head, divergent-cache-phantom KILLED) -- **NOT GRAPH-unified**. Andrew's literal one-graph goal = (a) [tools on the Nessie Kuzu projection], now a TRACKED follow-on with a DOCUMENTED (not cosmetic) coverage gap. The GRAPHUNI close summary + REGISTRY row MUST say "vintage-unified (b); graph-unification (a) = tracked follow-on," not "GRAPHUNI complete/unified" bare.
### Close mechanics: on ~D's full per-tool head-pinned re-point + retire + D4 (0 divergent-vintage reads) + CVO~B per-tool set-equality GREEN -> 2-step close GRAPHUNI (b-interim) with (a) carried. GRAPHDEPTH closes in parallel on CVO~B's comp-depth grain cert.
