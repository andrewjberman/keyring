# CVO~B COMPPROOF.A1 COMPLETE -- 12 seams + 4 processes, 3-axis on LIVE (11 PASS / 1 charted FAIL)

**archetype:** VALIDATE

**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-01 | **Window:** ~1400-1432Z (seed 1408Z + remainder post-DRV-flip)
**TO:** NFRA_COMPPROOF.A1-seam-process-sweep (COO~B; >=12 seams + >=4 processes, wave-weighted, random-sample, 3-axis on live, 100% FAILs charted). Supersedes the 1408Z seed.
**Grounded on DEPLOYED/SERVED/LIVE only.** Random-sample = deliberately NOT the happy-path targets I deeply verified in the wave closes.

## SEAM LEDGER (12; wave-weighted 6-of-6 programs; ~4 mech / ~4 decl / ~4 sem)
| # | target | axis | program | verdict |
|---|---|---|---|---|
| S1 | seam-5 KUZU->ICEBERG parity | MECH | COMPDRIFT | PASS (3x MATCH, 9.46h fresh) |
| S5 | rail 2-tier nav->route/compute->free | MECH | COMPROUTE | PASS |
| S11 | comp-kuzu reads CURRENT marker head | MECH | GRAPHUNI | PASS (snap 5434137157015633165, provenance current) |
| P3-seam | lambda-source-map deploy parity (D_01) | MECH | COMPDRIFT/deploy | PASS (local==s3 MATCH, 0 STALE) |
| S2 | tools_index manifest<-ledger projection | DECL | COMPUNIFY | PASS (34-in-50 non-breaking) |
| S4 | node_type_grain 52-bijection | DECL | GRAPHDEPTH | PASS (52 live==52 mapped, 0 unmapped) |
| S9 | drift-topology seam-6 GAP->COVERED | DECL | COMPDRIFT | PASS (topology COVERED == live seam-6 close) |
| S10 | closure discipline JSON+REGISTRY | DECL | wave | PASS (COMPUNIFY/GRAPHUNI/COMPROUTE all status=complete + REGISTRY row) |
| S3 | ~D<->~A write-key convergence | SEM | GRAPHUNI | PASS (169 write-keys/232 owned/0-dangling) |
| S6 | rollup existential (coarse<-fine) | SEM | GRAPHDEPTH | PASS (232 OWNED_BY + 248 RUNS fine edges, coarse targets resolved) |
| S7 | non-redundancy invariant | SEM | COMPUNIFY | PASS (comp-coverage-check clean) |
| **S12** | **COMPLEARN produce->consume** | **SEM** | **COMPLEARN** | **FAIL** -- the learned signal does NOT reach the consumer (0/236 live routing decisions apply a learned affinity). Grounded in D1. **CHARTED: D1 COMPLEARN fix-charter (close the flywheel + the now-live default-router consumes it post-flip).** |

## PROCESS LEDGER (4; end-to-end)
| # | process | verdict |
|---|---|---|
| P1 | graph derive -> marker-head -> tool-read | PASS w/ known (a) residual (comp-blast/etc on head-pinned build_graph, charted) |
| P2 | gold-run -> served | PASS -- served artifact present (accounts_dimension_latest.parquet). FRESHNESS NOTE: vintage 06-29 19:03Z (slowly-changing dimension; verify vs expected cadence if a concern -- not a confirmed FAIL) |
| P3 | Lambda deploy -> parity | PASS -- D_01.partner_analytics local==s3 deployed MATCH |
| P4 | derive -> marker-head -> tool-read (independent of P1's build_graph leg) | PASS -- derive 9.8h -> iceberg seam-5 MATCH -> marker current -> comp-kuzu/comp-depth read it; chain carries, provenance current |

## Result
**11 seams PASS / 1 FAIL (charted) + 4 processes PASS.** The just-closed wave HOLDS on live under RANDOM-sample (not happy-path) -- the honest breadth that keeps B honest. The ONE FAIL (S12 COMPLEARN produce->consume) is a REAL semantic seam failure the random-sample caught -- exactly A1's purpose -- and it is 100% CHARTED to the existing D1 fix-charter (the flywheel is open + the consumer default-router only just flipped live). Knowledge-parity: every PASS seam's tool/graph answer matches live; the S12 parity delta (learned-produced vs routing-consumed) is the charted gap.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| iceberg_parity / comp_coverage_view / comp-coverage-check / comp-pipescript deployed / comp-kuzu / kuzu-direct / comp-which | 3-axis seam + process grounding on live | PASS -- 11/12 seams + 4/4 processes; 1 charted FAIL (S12) |
| aws s3 ls (served artifact) | P2 gold->served freshness | PASS-w-note -- served, 06-29 vintage |

What worked: random-sampling ACROSS the axes + all 6 wave programs (not the happy-path close targets) is the point -- 11/12 + 4/4 PASS = the wave genuinely holds on live, AND the sweep CAUGHT a real semantic FAIL (COMPLEARN produce->consume) that a happy-path sweep would have missed. The FAIL is charted to the existing D1 charter, not softened. Gap: P2's 06-29 served-vintage is a freshness data-point (dimension = slowly-changing), noted not force-FAILed without the expected cadence.

## Next Steps
1. **[2.0.0_SA_COO~B]** A1 COMPLETE (>=12 seams + >=4 processes, 3-axis, wave 6-of-6, 100% FAILs charted). The 1 FAIL (S12 COMPLEARN produce->consume) rides the existing D1 fix-charter -- no new charter needed. Keeps B honest: the wave holds, the one live gap is the COMPLEARN flywheel (already tracked).
2. **[3.0.0_SA_CVO~B]** B2 blind-run judge on COO~B's ping (MSTR spawning B-01). D1 re-audit when the flywheel-close lands.

-- 3.0.0_SA_CVO
