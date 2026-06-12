# /ws-charter cycle 0011 — NFRA_DEBTSCAN PRD v0.1 (Andrew-direct via CVO brief 2a30d65f3)
**archetype:** SCRIBE
**secondary_archetypes:** EXPLORE

## Classification
- **Class:** NOVEL under Andrew direction (Andrew-direct ~17:55Z relayed via CVO 175620Z; CVO brief
  `docs/briefs/nfra-debtscan-prd-request-20260612.md` 2a30d65f3 = methodology source-of-record; project code
  NFRA_DEBTSCAN Andrew-named). Primary-path execution: registration + PRD + COO handoff.

## What shipped
- `org/projects/NFRA_DEBTSCAN.json` (prds ARRAY per the macro-JSON convention) + REGISTRY Active row (top).
- `docs/architecture/NFRA_DEBTSCAN_PRD.md` v0.1: 4 families ratified with incident anchors; FP/precision
  gates (≥0.8 CVO-adjudicated per family before non-ADVISORY); verify-before-delete + zero-mutation-scanner
  BINDING; freshness-bound filing (provenance header required, stale-vintage runs refuse to file); outputs
  (debtscan ledger + graph_metrics burn-down + critical-paths cross-filing with the advisory-vs-gating
  boundary); phasing P1/P2/P3 ratified; ALL FOUR brief §6 open questions answered in-PRD (owner routing =
  scan-files/owners-adjudicate/nothing-auto-fixed; cadence = nightly-piggyback LD-0176 + QUERY-class ad-hoc;
  precision = ≥0.8; portal-side = in-stitch nodes P1, full portal-source family OUT until P3).
- Canon pattern library (`org/modules/graph/canon-patterns.yaml`) claimed as CTO-authored P2 artifact.

## Compiler Tools (PRD §8 carries raw outputs)
| Tool | Run? | Result |
|---|---|---|
| comp-kuzu (canonical) show_tables + table_info | YES | provenance header live, Nessie HEAD current (pin==marker) — F6 working in anger |
| comp-kuzu node_type census | YES | 1,157 nodes: IAM_POLICY 271 / LOG_GROUP 195 / LAMBDA 169 / ... |
| comp-kuzu drift census | YES | DECLARED 814 / LIVE-no-DECLARED 319 / AWS_MANAGED 21 / other 3 |
| comp-kuzu isolated-node count | YES | 259 zero-degree nodes = Day-0 P1 dead-path pool |
| comp-kuzu --db-path kuzu_stitch_db count | YES | 3,088 nodes (estate-wide stitch surface confirmed) |
All QUERY-class, zero rebuilds (Rule 20).

## Concurrent thread folded
COO 180023Z relayed AE's D8-AE Part B design finding mid-authoring — ruled inline (Q1 APPROVED:
watched_file_shas baseline extension, 4 conditions: single-source watched-list derivation; portal submodule
commit anchoring; captured-at-re-sign-only; honest per-layer coverage labels). Noted in the ruling MCP that
AE's finding is itself a live DEBTSCAN-2a-class instance (stitch coverage gap on
BenchmarkHeatmap/portal-proxy/PeersTab) — feeds the P1 stitch-coverage backlog.

## Follow-on
COO decomposes TO-D1/TO-D2 (P1) per PRD §9; TO-D3 gated on my canon-patterns.yaml; CVO validates the PRD vs
the brief + owns the per-family precision adjudication when P1 files its first samples.
