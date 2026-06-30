# NFRA_GRAPHUNI.P0 — D1 coverage audit + per-tool gap-list (lane ~D)

**archetype:** TRACE
**secondary_archetypes:** DIAGNOSE

## Current State
NFRA_GRAPHUNI.P0 (D1 coverage audit, read-only) **COMPLETE**. Delivered the per-tool coverage gap-list — the exact net-new derive spec P1 consumes — at `org/projects/NFRA_GRAPHUNI/NFRA_GRAPHUNI.P0.d1-gap-list.md`. RAVC2'd to COO~B, cc CTO + CVO. Now HOLDING for the P1 GO (HARD-GATED on CVO signing the P0-CVO no-regression fixture LOCKED; ~D does NOT self-advance to the first graph mutation).

This was the CTO-mandate-first GO I was holding for: COO~B issued a premature D1 direction (200822Z), Andrew corrected to HOLD (200846Z, CTO-mandate-first), then CTO approved the GRAPHUNI decomp and COO~B GO'd P0 (202013Z). Lane ~D is the Andrew-provisioned dedicated build lane for the NFRA_GLOBGRPH substrate-unification delta (LD-0228) — the substrate beneath COMPUNIFY (~C maps the target; ~D builds it).

## What the audit found (the gap mechanism)
The unified Kuzu graph at the marker head (HEAD current, 18,216 nodes / 30,481 edges) holds **aws-infra** (Lambda/IAM/S3-bucket/EventBridge), **ms-files**, and **portal-frontend** (JSX/TS component-level, the NFRA_TSGRAPH fold). It holds **ZERO Python data-pipeline backend** — empirically: name-match for gold scripts (A_00/B_01/INF_D_00/...) = 0 rows; CALLS/IMPORTS edge query = 0 rows; S3 is bucket-granular only.

The structure-tool caches hold exactly that missing half:
- **TraceGraph** (`graph.json`, comp-blast/trace/xref): 1,340 GOLD_SCRIPT nodes (1,204 function-level) + 1,624 CALLS edges + 909 key-level READS_S3/WRITES_S3 — the complete gold-pipeline function call+IO graph.
- **comp-xref** reads the SAME TraceGraph (confirmed in cli.py `_CACHE_FILE`) — its symbol cross-ref is a LENS over the function nodes, **no separate index to derive**.
- **comp-platinum** caches (RoutingTable + 3 PipelineDAGs + dataflows): front half (component→endpoint→lambda→bucket) already in Kuzu (overlaps NFRA_TSGRAPH — do NOT double-derive); gap = the gold/backend half (PipelineDAG ScriptIO+S3Key producer/consumer DAG) + key-level S3.

**Consolidated P1 derive spec (one fill serves all four tools):** the gold (Python) data-pipeline backend graph — `GoldScriptFunction`/`GoldScript` nodes + `CALLS` edges + gold-grain `READS_S3`/`WRITES_S3` + key-granular S3 — plus 4 residual CTO rulings (layer placement, S3 grain model, Route store-vs-traverse, edge-grain disambiguation).

## Compiler Tools
| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-kuzu | `MATCH (n) RETURN labels(n), count(*)` | PASS | provenance header read (HEAD current, pin==marker HEAD, age ~1h) — authoritative baseline, not a scratch vintage. All nodes label=CloudNode; discriminator = node_type+layer property. |
| comp-kuzu | `MATCH (n:CloudNode) RETURN n.layer, n.node_type, count(*)` | PASS | full node census by layer (aws 1451 / ms 5427 / portal 11338). |
| comp-kuzu | `MATCH ()-[r]->() RETURN r.edge_type, count(*)` | PASS | 48 edge types censused; no CALLS/IMPORTS present. |
| comp-kuzu | name-match `A_00\|B_01\|INF_D_00\|...` + `CALLS\|IMPORTS` edge query | PASS | **0 rows both** — proves Kuzu lacks the gold-pipeline backend (the core gap). |
| comp-kuzu | S3_BUCKET name sample | PASS | S3 is bucket-granular (bucket names only) — granularity gap vs cache key-level. |
| (read) graph.json TraceGraph | python read-mode, schema+census | PASS | TO mandate step 2 — function-level nodes (1204) + CALLS (1624) confirmed. |
| (read) platinum.*.cache | pickletools.genops (no exec) + pickle.load (pure-builtin) | PASS | TO mandate step 2 — RoutingTable.Route joined chain + PipelineDAG ScriptIO/S3Key extracted. |
| (read) .tools/comp-xref + cli.py | Grep/Read | PASS | confirmed comp-xref reads the same TraceGraph — no separate symbol index (key gap-list finding). |

**comp-which note:** the canonical tool for this audit IS comp-kuzu (the graph traversal surface), used as the primary lens; cache-schema inspection is native Read-class file work (pickle introspection, not a repo search). No raw-grep substitution for a comp-tool occurred on the graph side.

**What worked:** comp-kuzu's marker-head provenance header gave a clean authoritative baseline in one call; the 0-row gold-script + 0-row CALLS queries turned "Kuzu lacks the backend" from an assertion into empirical proof; pickletools.genops let me read the platinum pickle schema without executing reduce/build.
**What failed / gap found:** none on the tooling. The audit itself confirmed the PRD's predicted fill (function-level + platinum full-stack gold half) and sharpened it to a per-tool spec + 4 CTO rulings.

## MCP Traffic
ACK-HOLD -> COO~B (held on the premature direction). ACK GO NFRA_GRAPHUNI.P0 -> COO~B (ETA ~40min, P1 hard-gate confirmed binding). RAVC2 -> COO~B cc CTO+CVO (gap-list delivered) [this session].

## Blockers
None. P1 is HARD-GATED by design (CVO fixture-lock) — that is the locked inviolable ordering, not a blocker. HOLDING per gate.

## Next Steps
1. **[2.0.0_SA_COO~B]** receive the gap-list RAVC2; dispatch P1 to ~D ONLY after CVO signs the P0-CVO fixture LOCKED.
2. **[1.0.0_SA_CTO]** rule the 4 residuals (layer placement / S3 grain / Route store-vs-traverse / edge-grain disambiguation) — they shape the P1 derive.
3. **[3.0.0_SA_CVO]** the gap-list pairs with the P0-CVO pre-delta fixture (capture pre-delta tool answers while the OLD caches are authoritative).
4. **[0.8.0_AE_CloudComp~D]** HOLD for P1 GO. Do NOT touch the graph until COO~B's explicit P1 dispatch.
