# CVO Review: NFRA_MSGRAPH re-scope (estate-wide heat + analytics layer + /sites/Shared re-target)

**Reviewer:** 3.0.0_SA_CVO | **Date:** 2026-06-26 | **Author of doc:** 0.8.0_AE_CloudComp (1834b7920)
**Routing:** Andrew-direct -> CVO review -> CTO arch-gate (cc COO, debtscan owner).
**Verdict:** **SOUND -- forward to CTO arch-gate, with 2 CONDITIONS** (additive-safety proof + the convergence condition the supplement asked me to flag).

## Verification asks (each grounded, Rule 22)

### Ask 1 -- recon ground-truth: VERIFIED (independent live MS recon, mine)
I re-ran the recon against LIVE MS (not the author's self-report):
- **Target `/sites/Shared`: CONFIRMED.** `find_sharepoint_site` -> siteId `opalinvest.sharepoint.com,9332c03f-2ad0-4b84-97fe-7bcd2c9cb90a,...` -- CHAR-MATCHES the doc's cited siteId; webUrl `/sites/Shared`; lastModified 2026-06-25 (active). (A separate stale `ExternallyShared` site exists, 2022 -- not the target.)
- **Top-level structure: CONFIRMED.** `list_site_files` (default "Shared Documents" library) returns ~69 folders + 13 loose files = ~82 top-level items -- EXACT match to the doc's "82 top-level (69 folders + 13 loose files)."
- **8-cluster taxonomy: CONFIRMED.** Every named cluster folder is live: Research/ETF/Alternatives/Div Research/Screens/Fund Comps/Sellside/Macro/MORNINGSTAR/Viewpoints (Research); Presentations/Market Update/Marketing/Website/PFDE/Brand/Charts (Marketing); OCIO Models/SMA Model Weights/ETF Models/Holdings/Covered Call/Polen/SMArtX (Models); Recruiting/Adam/Hiring/Firmwide Meeting/Training (HR); GIPs/Investment Committee/Opal Due Diligence/Compliance Manual/DDQ/IMAs (Compliance); Asset Management; TAX/Dashboard/Billing/Trading-Ops/Orion (Ops/Tax); Alongside/49F Comm/49F Custom/GFCA/Ausdal/LPL/Cottonwood/Envestnet (Partners).
- **Document-dominated + size!=count: CONFIRMED live.** The big-byte folders are FEW nodes -- `Systematic Equity` = 2.4 GB but **childCount=1**; `Software` = 3.0 GB, childCount 12 (.exe); `Marketing` 3.2 GB. Loose top-level files are all documents (xlsx/docx/pptx/pdf). The "flag-not-exclude non-document bulk" call is correct.
- **Honest caveat (non-blocking):** the precise **~4,560 total** is a recursive estimate; I verified the top-level (82) + childCounts (ETF 79, Market Update 127, GIPs 63, Presentations 69, Dashboard 53, ...) which are consistent with a low-thousands estate, but did not re-run the full depth-6 crawl. The CHARACTERIZATION (target, structure, document-domination) is solid; the exact node count is an estimate, not a re-counted figure. Does not affect the architecture.

### Ask 2 -- never-content guardrail: PRESERVED (sound)
The re-scope ranks on filename / folder-path / type / heat / recency / owner -- **never document bodies**; the two fail-closed layers (gateway `/ms/*` read-only-by-construction + structure-only output allowlist + derive emit-cert) are unchanged and the doc correctly extends them to the hourly poll. Content-embedding RAG is explicitly CARVED OUT as a separate, Andrew-gated decision (crosses the never-content line). **Live corroboration:** the `list_site_files` payload I pulled is metadata-only by construction (names, types, timestamps, sizes, hashes -- zero bodies), demonstrating the read path is structure-only. The hourly-full-poll widens CADENCE, not the DATA CLASS. Guardrail holds.

### Ask 3 -- reuse claims: SOUND + correctly-flagged (not over-claimed)
- HEATMAP_OBJECT build-complete + domain-parameterizable: consistent with the workspace's HEATMAP_OBJECT S0->O4 build; the MS->AWS generalization is correctly flagged as the NEW work (per-AWS-class last-activity extraction) with a SHARED engine -- honest scoping.
- pyiceberg compute = proven (the derive's RestCatalog -> Nessie Iceberg-REST is the existing path).
- Trino/Athena query layer = correctly flagged a **FEASIBILITY item, not an assumption** (Trino-over-Nessie-REST should work; Athena-over-Nessie needs Glue dual-reg or Iceberg-REST -- "confirm before committing to Athena"). This is the right epistemic posture; no reserved-word over-claim.

### Ask 4 -- additive-safety: SOUND, with a verification CONDITION
Estate-wide heat reads `graph_nodes`, writes NEW index tables (heat_index/clusters/rag_index), never mutates AWS or MS nodes -- strict-superset/F5 additive. **CONDITION A (additive-safety proof):** the heat run must be provably a strict superset -- a 0-diff on the CERTIFIED AWS graph_nodes/graph_edges after a heat materialization (new tables only; the certified graph untouched). Make that 0-diff a gate on the first heat-over-AWS run, not an assumption.

## The CONVERGENCE condition (supplement -- flagged as a CTO arch-gate CONDITION)
The supplement (COO-raised) asked: does the estate-wide heat dimension CONVERGE with the NFRA_DEBTSCAN dimension home, or fork? I have direct context -- I just landed the comp-dups dimension into `org/modules/graph/debtscan/` this session. My finding:

**The re-scope's INTENT is convergent** (it explicitly frames heat as the DEBTSCAN/COSTAWS surface -- "one mechanism, two payoffs", "comp-debtscan layer='aws' cold"). **But there is a real SUBSTRATE + DATA-MODEL divergence risk:**
- Existing NFRA_DEBTSCAN = `org/modules/graph/debtscan/`, **FILE-LEDGER** based (D1-D5 dated `.md` + comp-dups `YYYY-MM-DD_DUPS_candidates.json` + `dups_latest.json`); scans the GRAPH for reachability/duplication/dead; comp-* tools are the lenses.
- Re-scope heat = **materialized ICEBERG tables** (heat_index) in Nessie, queried via Trino/SQL.
Different substrates + overlapping-but-distinct signals (reachability+dup vs activity-recency). If both proceed independently -> TWO "node-health" surfaces -- exactly the "three surfaces, not one" COO warned against.

**CONDITION B (convergence) on approving change #3 -- node-health is ONE surface, heat is a DIMENSION of it, not a parallel construct:**
1. **Unify the SUBSTRATE.** CTO rules ONE materialization for the node-health surface (file-ledger vs Iceberg-materialized). If Iceberg wins (likely -- it's the canonical estate + time-travel), the existing debtscan dimension (D1-D5 + comp-dups) MIGRATES onto it; if file-ledger persists for some, heat must ALSO emit a ledger to the same home -- not a parallel Iceberg-only store divorced from `org/modules/graph/debtscan/`.
2. **Unify the DATA MODEL.** One per-node health record `{node_id, layer, reachable, duplicated, heat_band, cold_since, cost}` so comp-dups / comp-heat / comp-debtscan are LENSES on ONE record, not separate dimensions with separate stores.
3. **Unify the TOOL FAMILY.** comp-heat / comp-ms-find / comp-debtscan register in the SAME comp-tool family + manifest section as comp-dups, comp-which-routed -- one agent-facing graph-hygiene surface.
This is a CONDITION, not a blocker: the heat generalization is GOOD and the right move; it must land AS a debtscan dimension (debt/dup/dead/cold/cost all reading graph_nodes), not beside it.

## Verdict
**SOUND -> forward to CTO arch-gate.** Recon verified live; guardrails preserved; reuse honestly-flagged; additive-safe. Two conditions for the arch-gate: **(A)** additive-safety 0-diff proof on the certified AWS graph; **(B)** the convergence condition -- heat lands as a DIMENSION of the one node-health/debtscan surface (substrate + data-model + tool-family unified), not a fork. CTO's 5 arch-gate decisions (doc SS7) stand; I'd add B as a 6th, gating decision #2 (the estate-wide heat generalization).

Grounding: live `find_sharepoint_site` + `list_site_files` (this session); the re-scope doc 1834b7920; my comp-dups dimension build (6af49d71c) for the convergence assessment.
