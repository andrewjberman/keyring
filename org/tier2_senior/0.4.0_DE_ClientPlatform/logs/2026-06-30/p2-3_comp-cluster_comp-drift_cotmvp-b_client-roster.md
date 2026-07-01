# P2-3 comp-cluster (built, folded to MSTR) + comp-drift land + COTMVP B reshape -> COT Clients roster

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, COORDINATE
**Serial:** 0.4.0_DE_ClientPlatform · **Date:** 2026-06-30 · **Window:** (continues the INFREF+P2-1 log) -> now

**Portal DEV commit:** `07d5887f`
**Workspace CLOUD commits:** `d0c720c6a` (P2-3 TO+brief), `9fe941ef8` (comp-drift fix)

## Summary

Three threads after the INFREF+P2-1 log:
1. **NFRA_TSGRAPH.P2-3 comp-cluster** -- built + all ACs verified; LANDING lane-blocked for a DE; Andrew steered it to MSTR fold-in (LD-0231).
2. **comp-drift** -- landed the curated comp-which route (MSTR LD-0231 #1), routing 34/34 PASS.
3. **ADVI_COTMVP B (Andrew-direct reshape)** -- grounded the COT Books blocker, reshaped to a firm-level CLIENT roster (no advisor work), built + shipped the COT-isolated FE to DEV, CTO arch-gate APPROVED.

## Thread 1 -- P2-3 comp-cluster (built -> folded to MSTR)

Built `comp-cluster <Page>` (engine `infra/aws/globgrph/comp_cluster_cli.py` mirroring kuzu_cli; wrapper `.tools/comp-cluster`; manifest entry + tools_index; comp-which curated rule). Queries the LIVE cluster graph (Rule 20): panel->drilldown tree (depth 1..4 + per-firm cohort), per-cluster sources, cross-panel SHARES_SOURCE. All ACs verified locally (AdvisorIntelligence real tree; comp-manifest-check exit 0; comp_coverage_view --verify 35/35; routing 34/35; coverage 118/119+1 visible).
**Landing lane-blocked for a DE:** engine -> infra/aws/globgrph (AE lane), manifest -> ANY_EXEC lane, .tools/ gitignored. Andrew steered the approach to MSTR -> briefed MSTR (`docs/briefs/comp-cluster-graph-manifest-approach-brief-20260630.md`), folded into the surface-aware-router commission (LD-0231, 8fc27f768). Held the bundle for the CTO engine-home ruling (MSTR rec: relocate engine to org/modules/graph/ + shell to comp-kuzu --json so I self-land). Shared-tree edits reverted (clean tree); durable bundle + landing recipe in scratchpad `p2-3-comp-cluster-bundle/`. P2-3 TO held-pending (built+verified, not landed).

## Thread 2 -- comp-drift land (MSTR LD-0231 #1)

Added a curated comp-which route for comp-drift (estate propagation-drift orchestrator) -- it was self-route-mis-firing to comp-aws (MSTR's Exhibit B). `.tools/comp-which` (basename-exempt), CLOUD `9fe941ef8`. Routing regression PASS (34/34 self-route, 3/3 audit, 20/20 paraphrase).

## Thread 3 -- ADVI_COTMVP B (Andrew-direct reshape) -> COT Clients roster

### Files Modified
| File | Change | Committed |
|------|--------|-----------|
| portal/src/pages/AdvisorIntelligence/_partners/cottonwood/CottonwoodClientsSection.tsx | NEW -- firm-level client roster from client_directory.json (household+AUA, both shapes, defensive AUA, retry:false + graceful empty-state) | Yes - DEV `07d5887f` |
| portal/src/pages/AdvisorIntelligence/_partners/cottonwood/index.tsx | wire CottonwoodClientsSection below Distribution (ErrorBoundary), COT-isolated | Yes - DEV `07d5887f` |

### Grounding (Andrew's question: "is it something else?")
Grounded against LIVE served opal-data-cot: dashboard.json `employee_leaderboard=null` + `fee_efficiency=null`, no per-advisor artifacts -> advisor-drill dead for COT REGARDLESS of naming (falsified Andrew's name-the-rep-codes idea, told him). But client-level viable with ZERO advisor work: COT gold already aggregates 217 clients/805 accounts + per-client detail Lambda handlers already wired (layout clientDetailHandler:'lambda'). SOLE gap = COT doesn't serve the client LIST (no platinum/firm/client_directory.json; inf/49F have it).

### Reshape + build
2 lanes, no advisor work: (1) PRODUCER = COT client_directory.json emit (routed to base-COO -- ADVI/cot owner; NOT COO~B who is NFRA_COMP*-scoped, per Andrew's correction -- allocating cot-gold DS lane via MSTR). (2) FE (mine) = COT-ISOLATED CottonwoodClientsSection (no shared-BooksTab change -> zero 49F/inf regression), ships SAFE ahead of the emit via graceful empty-state, lights up when the directory serves. v1 = roster; per-client DETAIL drill deferred (verify the COT opal-partners-data Lambda resolves before wiring -- wired but unexercised).
CTO ARCH-GATE APPROVED (isolation over SEV1-retrofit = correct; grounding sound; ship-safe pattern). Pending: producer emit (firm-separated, NEVER#1), Lambda-detail verify before drill, CVO served-verify (count 217/805) once served.

## Compiler Tools
| Tool | Target | Result |
|---|---|---|
| `comp-kuzu` (census, edge census, per-page CLUSTERS, props dump) | P2-3 live-graph verify | PASS -- verified cluster layer live (Page 15/PanelCluster 91; CLUSTERS 91/CONTAINS_DRILLDOWN 241/SHARES_SOURCE 55; depth 1..4 + cohort in props) |
| `comp-manifest-check` | P2-3 manifest reg | exit 0 (my files basename/path-exempt; manifest valid) |
| `comp_coverage_view.py --verify` | tools_index<->ledger drift | 35/35 in ledger union (comp-cluster pre-registered by ~C), no drift |
| `comp-which-routing-test.py` | comp-drift + comp-cluster routing | 34/34 PASS after comp-drift land (comp-cluster held) |
| `comp-transform schema-check` | CottonwoodClientsSection | PASS -- all rendered fields match |
| `bun run typecheck` / eslint | COT FE (07d5887f) | tsc -b exit 0; eslint clean (caught + fixed a Record index-signature typing) |
| `aws s3 ls/cp` (COT served) | COTMVP B grounding | grounded employee_leaderboard/fee_efficiency=null + no client_directory (the reshape's whole basis) |

**What worked:** comp-kuzu live-graph queries verified P2-3 without a rebuild; served-artifact grounding falsified the advisor premise (saved building the wrong thing); comp-transform kept the COT FE cross-tenant-safe.
**Gap noted (not mine):** comp-drift was unreachable via comp-which (pre-existing) -- fixed. `r.depth`-style edge-prop queries need JSON extraction (attrs live in the CloudEdge props column; Kuzu lacks SPLIT()).

## Blockers
None mine. COTMVP B FE done+approved; gated on the producer client_directory emit (base-COO/MSTR). comp-cluster landing held for the CTO engine-home ruling. P3-2/P3-3 blocked upstream on P3-1.

## Next Steps
- **[2.0.0_SA_COO / 0.0.0_AB_MSTR]** allocate + land the COT client_directory.json emit (firm-separated, opal-data-cot) -> lights up the COT Clients roster.
- **[0.4.0_DE, me]** on directory-serve: verify roster renders + CVO count-verify (217/805); verify COT per-client Lambda detail resolves -> wire the detail drill (follow-up). On the CTO engine-home ruling: reshape + land comp-cluster (option-a: org/modules/graph engine + shell to comp-kuzu --json).
- **[3.0.0_SA_CVO]** served-verify the COT client_directory against gold (count) once emitted; the INFREF pixel-pass residual still open.
- **[1.0.0_SA_CTO]** engine-home ruling for the comp-cluster bundle (LD-0231 fork).
