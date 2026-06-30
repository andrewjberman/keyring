# NFRA_COMPUNIFY S0 -- apex skeleton authored (lane: 0.8.0_AE_CloudComp~C, dedicated COMPUNIFY build instance)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

## Current State

S0 (NFRA_COMPUNIFY.S0, apex-skeleton) deliverable AUTHORED + self-gate-validated; commit BLOCKED only on an owned-paths grant (SoD -- COO~B's action). Lane = `0.8.0_AE_CloudComp~C`, the dedicated COMPUNIFY build instance launched this session (base/~B firefight-pinned on ADVI_BREAKS).

**Deliverable:** `org/modules/graph/comp-coverage-map.yaml` (on disk, uncommitted, parses clean). The apex SKELETON the NFRA_COMP* program hangs on -- one noun (the map) referenced by both COMPDRIFT (state-verb) + COMPLEARN (use-verb) loops. Contents:
- **5-surface APEX:** 4 territory (LOCAL / GIT / AWS-CLOUD / MS-CLOUD) + TRINO as the federation surface (special, not a peer). High-level tool per surface: LOCAL=`comp-heat drift`; GIT=`comp-heat`+`comp-xray`; AWS-CLOUD=`comp-aws`; MS-CLOUD=GAP (no comp-ms -- empty node flagged, not invented); TRINO=`comp-kuzu` (+comp-fed future).
- **Node schema** `{concern, granularity, surface|seam, distinct_from}` defined in `schema.node_fields`, + a per-surface `provenance {refresh_mechanism, cadence, concurrency_basis}` field (COO~B/MSTR fold).
- **schema.gate_contract** = the S2 `comp-coverage-check` SPEC, restructured (CTO design note) into S2-machine-readable records: 4 rules (`one_home` / `seam_reference_integrity` / `declared_non_redundancy` / `no_trino_phantom_seam`), each `{id, applies_to, inputs, predicate, on_violation}`. S2 READS this contract; it does not re-implement a parallel rule-set (map can't drift from its own gate).
- **SEAM axis** REFERENCES `org/modules/graph/drift-topology.yaml` seam-1..7 via `seam_source` + per-seam `ref` (owning tool + coverage mirrored, engines/verdict_vocab NOT duplicated) -- ruling #2, ONE seam artifact.
- **TRINO federation** by PHYSICAL CATALOG (iceberg[graph_nodes/edges/contracts] / code_heat / +tool_activity future-GAP) -- ruling #3, zero phantom per-layer seams; layer(aws/portal/ms)=COLUMN note.
- **WORKED OVERLAP** (AC3 proof): IAM x3 (comp-iam=grant-analysis | comp-aws=IAM-as-graph-nodes | comp-lambdamap=deploy-SHA), each with a STRUCTURED `distinct_from` record. Proves distinct_from is gate-readable data, not prose.
- **gap_census / redundancy_census** stubs name the S1 worklists (ms-cloud tool-front, tool_activity, seam-6 iceberg bindings, local depth; IAM x3 declared, parity x3 + freshness x4 to declare).

**Rulings 1-4 (CTO PRD section 6) locked into the file header + structure.** Ledger supersedes tools_index (ruling #1, S1 wires the generated view).

## Validation (self-gate dry-run, python over the file)

- `one_home`: PASS (all placed tools -- exactly one of surface|seam + granularity + concern).
- `declared_non_redundancy`: PASS (IAM 3-way pairwise-distinct concerns + full distinct_from coverage; estate-object-freshness group too).
- `seam_reference_integrity`: PASS (axis seam-1..7 all present in drift-topology.yaml).
- `no_trino_phantom_seam`: PASS (catalogs iceberg/code_heat/tool_activity; no layer-catalogs).
- provenance present on all 5 surfaces; MS-CLOUD `designed_asymmetry:true` distinct from tool-front `gap:true`.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-which | `comp-which "list every comp tool and what surface/concern it covers"` | PARTIAL | routed via the manifest backstop (no single rich tool fronts the full inventory) -> pointed at pipescript/comp-kuzu; grounded the apex against the real ~38-tool set via the manifest tools_index directly (TO mandate step 1). |
| (read) drift-topology.yaml | TO mandate step 2 | PASS | seam IDs seam-1..7 + seam-6 fan_in:true (physical-catalog bindings) confirmed -> referenced, not duplicated (ruling #2). |
| (read) graph-call-manifest.yaml tools_index | TO mandate step 3 | PASS | the flat ~38-tool catalog the ledger supersedes (ruling #1) -- the inventory re-homed top-down. |
| safe-commit.sh | commit attempt of comp-coverage-map.yaml | BLOCKED | owned-paths lane=ANY_EXEC; AE not permitted. surface-check PASS (no critical surface). The block is the SoD grant gap (below), not a defect. |

**What worked:** grounding the apex top-down against the real tool inventory (manifest tools_index) + the existing seam artifact (drift-topology.yaml) made the skeleton territory-true on the first pass; building the schema AGAINST a python gate dry-run proved AC3 machine-checkability before any review.
**What failed / gap found:** `comp-which` has no rich tool that returns "every comp-tool by surface/concern" -- it backstopped to the manifest. That is EXACTLY the discovery-friction NFRA_COMPUNIFY exists to fix (a flat catalog, not a drill-from-your-surface hierarchy); the coverage-map this S0 lands IS that missing surface-first index. Noted as program-confirming, not a tool bug.

## MCP Traffic

5 dispatches handled. Significant: RAVC2 -> COO~B (S0 deliverable + AC1-4 self-attestation + the owned-paths grant request); CC -> CTO (arch-awareness, AC3/AC4 priming); inbound COO~B LOW-PRI provenance fold (acted -- folded); inbound CTO approval + S2-machine-readable gate_contract design note (acted -- folded); RAVC2 UPDATE -> COO~B cc CTO (both folds landed + re-validated).

## Blockers

**BLOCKED (grant, evidence-cited):** `safe-commit.sh` blocks `org/modules/graph/comp-coverage-map.yaml` -- resolves to `org/modules/**` lane=ANY_EXEC; AE not in permitted_agents. TWO gaps, both the documented decompose-time pattern (CTO-ratified 2026-06-15 same-tool-grant convention):
1. No longest-match rule for `comp-coverage-map.yaml` (mirrors `org/modules/graph/comp_*.py` + `org/modules/compdiff/**` precedent) -> add as `ANY_EXEC_OR_AE`.
2. Tilde-lane gap: `ANY_EXEC_OR_AE` enumerates `0.8.0_AE_CloudComp` (base) but NOT `~C` -> add `0.8.0_AE_CloudComp~C`.
Routed to COO~B (the grantor; SoD -- grantee does not land its own grant). Not assumption-blocked: the grant is a ~30s config add that should have shipped at decompose-time.

## Next Steps

1. **[2.0.0_SA_COO~B]** land the owned-paths grant (file-rule + ~C tilde-add) -> I commit immediately, OR COO~B commits the deliverable. Then route the committed artifact to CTO for the S0 arch-gate. Dispatch S1 (populate all ~38 tools at their home + emit the gap/redundancy censuses + wire tools_index-as-generated-view).
2. **[1.0.0_SA_CTO]** formal S0 arch-gate on the COMMITTED file: (a) dry-run reproduces; (b) gate_contract S2-machine-readable; (c) AC4 seam IDs match drift-topology.yaml; (d) no Trino phantom-seam. CTO pre-confirmed the approach is "exactly right."
3. **[0.8.0_AE_CloudComp~C]** on grant-land: commit, ping CTO, then proceed to S1 on COO~B's dispatch. Holding S1 until S0 is gate-accepted (the schema could move at the arch-gate -- do not pre-build S1 against an un-gated schema).
