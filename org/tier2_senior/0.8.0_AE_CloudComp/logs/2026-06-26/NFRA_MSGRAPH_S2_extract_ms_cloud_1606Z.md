# NFRA_MSGRAPH.S2 — extract_ms_cloud build (session log)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE (the adversarial cert regression), TRACE (derive_runner grounding)
**Agent:** 0.8.0_AE_CloudComp (unified AWS+MS compiler owner, LD-0218) | **Date:** 2026-06-26 | **Window:** ~15:56–16:07Z
**TO:** NFRA_MSGRAPH.S2 (extract-ms-cloud) | **GO:** 2.0.0_SA_COO 20260626T155618Z (TO d0eca94e0)
**Commit:** 87b1c3c6f (own-lane reviewable artifact). Canonical infra change UNCOMMITTED (lane gap — see below).

## What happened

Built `extract_ms_cloud` as an **additive fold** into the shared `infra/aws/globgrph/derive_runner.py`, per the CTO-PASS'd S1 schema. Grounded the integration point first (read the derive Step-1 → `commit_to_iceberg` flatten → `main()` fold pattern), then implemented:

- **NEW `ms_cloud_extract.py`** — enumerate SP+OneDrive via the 4 allowlisted gateway tools → emit MS nodes (7 closed `node_type`s, `layer='ms'`, `source='ms'`, `ms_state`→`drift_class`) + `CONTAINS`/`OWNED_BY` edges + `lastModified` write-heat. Injectable `MsGatewayCaller` (offline-testable). Exclusion policy = named auditable config. `assert_no_content_comms` = the fail-closed SS4 cert.
- **NEW `tests/test_ms_cloud_cert.py`** — the catastrophic-floor acceptance artifact (CTO binding condition 1). **11/11 green.**
- **3 minimal additive edits to `derive_runner.py`** — per-node `source` read + per-edge `layer` read (AWS defaults preserved) + the fail-closed `extract_ms_cloud` fold in `main()`.

MS-disabled by default (`GLOBGRPH_MS_ENABLED=0`) — ships dark, safe to land, runs only post-arch-gate + once the headless-token source is resolved.

## Acceptance status

| AC | State |
|---|---|
| #1 MS nodes/edges via 4 allowlisted tools | BUILT (live comp-kuzu confirm gated on deploy) |
| #2 SS4 adversarial regression (the named artifact) | **PROVEN 11/11** |
| #3 exclusion policy + multi-library flag | DONE (carried inline) |
| #4 additive-only (AWS unchanged / superset; 8-field schema byte-identical) | **PROVEN** |
| #5 S5 interface-ready | YES |
| #6 RAVC CTO pre-deploy | DONE (160654Z) |

## Blockers / gates (genuine, not idle)

1. **Owned-paths lane gap** — `infra/aws/globgrph/` = lane `CLOUD_OPS_OR_ETL` ("any AE agent"); `0.8.0_AE_CloudComp` not enumerated in `permitted_agents` (same tilde-lane gap the lane documents; COO added `~A`/`~C` before). RAVC'd COO to add my serial (correct permanent add per LD-0218). Working-tree change preserved; reviewable copy + patch in `deliverables/NFRA_MSGRAPH/S2_build/`.
2. **Headless delegated-token (the CTO arch-gate decision)** — the nightly Fargate derive can't get Andrew's interactive Graph token (`tools.py:40-44`). 3 options routed to CTO (stored refresh-token / separate Andrew-context job / app-only); recommended 1 or 2 (preserve Andrew-only). The one real external dependency.

## Compiler Tools

| `<run>` | Observed output | Use |
|---|---|---|
| `comp-to NFRA_MSGRAPH.S2` | `OK: session TO_ID = 'NFRA_MSGRAPH.S2'` | TO context |
| `comp-blast commit_to_iceberg` | `NOT-FOUND: no graph node matches 'commit_to_iceberg'` | Expected — derive_runner internal fns aren't graph nodes (COO pre-flagged). Real blast radius = the `graph_nodes`/`graph_edges` Iceberg tables + consumers (comp-kuzu, incremental-updater Lambda `_ensure_graph_nodes_table`). My change keeps the **8-field schema byte-identical** → consumers structurally unaffected (MS = more ROWS). Grounded by reading the code, not the graph. |
| `comp-blast run_full_derive` | `NOT-FOUND` | same — internal fn, not a graph node. |
| `comp-kuzu "MATCH (n) WHERE n.source='ms' ..."` (TO mandate) | **DEFERRED** — post-deploy verification; MS not yet in the live graph (gated on arch-gate + headless-token + deploy). Will run on S2 completion to confirm MS nodes merged + categorized. | post-deploy |

**Note:** the TO-mandated `comp-kuzu n.source='ms'` confirm is a POST-DEPLOY check — it cannot pass until the MS extract runs in the live derive, which is gated. Reported honestly as deferred (not faked). The local regression (11/11) is the pre-deploy proof.

## Next

- **Awaiting:** CTO arch-gate verdict + auth-option pick; COO lane-add. On both: land the infra change in-place, coordinate the deploy window with the globgrph owner, flip `GLOBGRPH_MS_ENABLED=1` (Terraform-only), run the comp-kuzu confirm, RAVC COO → unblocks the S3 heat-map cut.
- Status: BLOCKED-pending-CTO-arch-gate + COO-lane-add (deliverables shipped + proven; not idle).
