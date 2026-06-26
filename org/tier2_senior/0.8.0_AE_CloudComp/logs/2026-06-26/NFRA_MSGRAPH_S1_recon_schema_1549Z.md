# NFRA_MSGRAPH.S1 — recon + schema (session log)

**archetype:** MIXED
**secondary_archetypes:** EXPLORE (live-gateway recon), IMPLEMENT (schema authoring)
**Agent:** 0.8.0_AE_CloudComp (unified AWS+MS compiler owner per LD-0218) | **Date:** 2026-06-26 | **Window:** ~15:40–15:50Z
**TO:** NFRA_MSGRAPH.S1 (recon-and-schema) | **GO:** 2.0.0_SA_COO 20260626T154508Z
**Commit:** b6b92f150 (CLOUD, pushed)

## What happened

Launched under the wrong serial (MSTR spawned `0.8.0_AE_MSGraph`); Andrew corrected mid-session ("you should be cloudcomp; that was an error on behalf of MSTR") and the COO GO confirmed **LD-0218** — NFRA_MSGRAPH consolidates onto the single existing compiler agent `0.8.0_AE_CloudComp` as the **unified AWS+MS compiler owner**, not a split lane. Registered + watcher armed under the corrected serial; executed S1.

Two deliverables landed in own lane (`org/projects/` is ANY_EXEC-only — owned-paths gate blocked, relocated to `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_MSGRAPH/`):
- **S1_RECON_REPORT.md** — order-of-magnitude node-count + by-site distribution + activity-surface findings.
- **S1_MS_GRAPH_SCHEMA.md** — MS node/edge/activity taxonomy + allowlist + gate-impossible cert; routed to CTO for the arch-gate.

## Recon headlines (gates S2 budget)

- **SharePoint:** 6 sites (single tenant `opalinvest.sharepoint.com`); node-count **low hundreds**, concentrated — `Opal CIO Office for 49 Financial` holds nearly all active content; 4/6 sites empty/near-empty shells.
- **OneDrive:** organic business nodes **~low thousands**; raw recursion **~tens of thousands DOMINATED by non-organic data** — `Desktop/ajb_workspace` (full git-repo MIRROR, already in AWS graph) + `Documents/afterSentDocuments` (docs0–14, synthetic test corpus). **Budget = exclusion policy.**
- **Activity (AC#2, SOURCE-grounded):** `lastModifiedDateTime` CONFIRMED on 100% of driveItems → write-heat day-one. `/delta` + `/insights` + **`/permissions`** NOT exposed by the gateway → S5. Access-edge density **NOT measurable today** (could-not-verify, reported not fabricated). Recon **adds `/permissions`** to the S5 scope.

## Schema headlines (CTO-gate pending)

`layer='ms'`, single `CloudNode` label, property-typed (merges into the one Nessie graph). 7 node_types, 5 new CLOSED-vocab edge verbs (CONTAINS/OWNED_BY/HAS_ACCESS/SHARED_WITH/MEMBER_OF), `ms_state` provenance axis (no TF declared side — mirrors the portal layer's `coherence_class`). Invariant #1 structural cert specified as a gate-impossible CLOSE leg (source allowlist + emit-time content/comms-fail). S5 interface-ready (additive feeds, no refactor). Lean (invariant #4).

## Compiler Tools

| `<run>` | Observed output | Verdict |
|---|---|---|
| `comp-which "how do I enumerate SharePoint sites and OneDrive drives via the m365 gateway"` | **Backstop only** — "matched the catalog backstop"; closest rich tools offered were comp-platinum/pipescript/comp-which (none MS). No m365-gateway route in the manifest. | **GAP (expected)** — the MS doc-cloud is net-new; comp-which has no MS surface until S4 registers `comp-ms-*` + extends routing. This IS the S4 deliverable. Logged as the S4 coverage target. Live enumeration done via the m365 MCP gateway tools directly. |
| `comp-to NFRA_MSGRAPH.S1` | `OK: comp-to -- session TO_ID = 'NFRA_MSGRAPH.S1' (race-free per-session)` | OK |
| `comp-kuzu "MATCH (n) RETURN DISTINCT labels(n)..."` | provenance header `current` (pin==marker HEAD), age 2.8h; **single label `CloudNode`, 12,644 nodes** | OK — confirmed single-label/property-typed model; the schema mirrors it (no parallel labels). |
| `comp-kuzu` node_type + edge_type distributions | node_type discriminator (S3_BUCKET, ReactComponent, Field, LAMBDA…); edge_type UPPER_SNAKE (HAS_FIELD, RENDERS, READS, ASSUMES…); CloudNode props = node_id/arn/node_type/name/layer/drift_class/source/snapshot_ts/props-JSON | OK — grounded the MS node/edge/property conventions against the live graph. |

**Gap finding (for S4):** `comp-which` has no m365-gateway route — not a defect to fix now; it is the S4 findability layer (`comp-ms-find` + comp-which MS routing). Logged.

## RAVC / next

- Schema → CTO (1.0.0_SA_CTO) arch-gate request sent (20260626T154841Z). PASS gates S2.
- Recon + status RAVC'd to COO (20260626T154907Z) with the S2 budget numbers; COO drives S2–S6 decomposition off them.
- **Awaiting:** CTO gate verdict (PASS → cut S2 `extract_ms_cloud`; REWORK → revise schema). Status: BLOCKED-pending-CTO-gate (not idle — deliverables shipped).
