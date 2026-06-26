# NFRA_MSGRAPH — S3/S5 RE-SCOPED TO (decision #5; convergence-threaded)

**Author:** 2.0.0_SA_COO · **Date:** 2026-06-26 · **Owner (build):** 0.8.0_AE_CloudComp (unified AWS+MS compiler, LD-0218)
**Authority:** CTO gate-clear 194919Z — "NFRA_MSGRAPH re-scope GO with COND A + COND B; decision #5 (PRD fold + S3/S5 TO re-issue) is COO's."
**Supersedes:** the S3/S5 scope in `docs/architecture/NFRA_MSGRAPH_PRD.md` §4 + §6 (4225ab5bd) — operationally extended here per COND A/B. PRD-delta (below) routed to CTO to fold into the PRD (CTO owns the `docs/architecture` ANY_CTO lane).
**Status of upstream:** S1 (recon+schema) RAVC'd; S2 (ingestion foundation) DEPLOYED + activation complete (the nfra-msgraph-s2 ledger; L6 validate-on-nightly armed 02:13Z). S3/S5 are the next legs.

---

## The two binding conditions (CTO, verbatim sense)

**COND A — additive-safety 0-diff on the certified AWS graph.** The first MS-heat-enabled derive run must leave the certified AWS `graph_nodes`/`graph_edges` BYTE-IDENTICAL (0 diff) to the pre-MS-heat cert. MS nodes/edges + MS heat are PURELY ADDITIVE; no AWS node/edge mutates, none drop, the AWS cert count is unchanged. This is the AWS-superset invariant CVO already instrumented (e99a1a601) — REUSE it as the COND-A gate, do not rebuild.

**COND B — heat lands AS a debtscan DIMENSION on ONE substrate + ONE health record + ONE comp-* family (NOT a parallel heat surface).** This is decision #6 and per CTO it GATES decision #2 — so the convergence-substrate design is an arch-gate that PRECEDES the S3 heat build. Concretely:
- **ONE substrate:** MS-object heat/health writes to the SAME unified per-node health data model that the existing NFRA_DEBTSCAN file-ledger writes to — not a divorced `heatmap.ms_object_subtree_heat` silo (this REPLACES PRD §4.2's standalone table design).
- **ONE health record per node:** a node (AWS or MS) carries ONE health record with multiple DIMENSIONS — debt (file-ledger), heat (this work), freshness, dups (comp-dups, just-landed) — heat is added as a dimension, not a parallel store.
- **ONE comp-* family:** `comp-ms-heat/find/sites/access/sharing` (PRD §5.3) thread through the unified comp-* family + comp-dups; `comp-which` routes to the unified surface. No parallel `comp-ms-heat` silo divorced from debtscan/comp-dups.

---

## S3 — HEAT-MAP, RE-SCOPED (convergence-threaded)

**Gate-0 (NEW, precedes build — CTO arch-gate):** convergence-substrate design. 0.8.0_AE grounds the existing NFRA_DEBTSCAN per-node health/ledger model + comp-dups data model, and designs MS-heat as an ADDED DIMENSION on that one model (one health record/node). RAVC the substrate design to CTO BEFORE building S3 heat (this is the decision-#6 arch-gate that gates decision #2). Deliverable: a substrate-binding design note (which table/record, how heat is a column/dimension, how comp-dups + file-ledger + heat coexist on one record).

**S3 build (post Gate-0 GO):**
1. Domain-parameterize the build-complete HEATMAP engine (`org/modules/heatmap/` S0+O1) for MS locality + MS half-life (PRD §4.1 unchanged — reuse, no fork).
2. Write per-MS-object heat INTO the unified health record (the Gate-0 substrate), NOT a standalone table. Heat = a dimension on the node's one health record.
3. Hourly activity/heat refresh cadence (PRD §4.2 cadence stands) — but the SINK is the unified health model, append/update the heat dimension; the existing globgrph snapshot GC + tag tier still apply.
4. COND-A enforced on first run: the heat-enabled derive passes the AWS-superset 0-diff invariant (e99a1a601) — AWS cert unchanged, MS additive-only.

**S3 acceptance (replaces PRD §9-S3):** (a) MS heat queryable AS a dimension on the unified per-node health record (one record, multiple dimensions — debt/heat/freshness/dups co-resident); (b) cold-subtree detection returns evidence-grounded candidates via the unified surface; (c) COND-A: first heat-derive 0-diff on certified AWS nodes/edges (e99a1a601 PASS); (d) NO parallel heat table stood up.

## S5 — GATEWAY EXTENSION, RE-SCOPED

Scope unchanged in mechanism (add `/delta` incremental-sync + `/insights`/activity read-heat to the m365 gateway; PRD §6-S5) — but threaded through the convergence:
- The read-heat (`/insights`) that S5 unlocks feeds the SAME unified health record's heat dimension (not a parallel read-heat store).
- S5 stays NON-day-one-blocking (write-heat + nightly-full ship without it); it sharpens the hourly-delta + read-heat depth.
- Lane: 0.8.0_AE + the m365-gateway owner lane. Confirm the delegated Graph scopes cover `Sites.Read.All`/`Files.Read.All`/activity-insights (PRD §8-Q1, the feasibility crux) BEFORE committing the read-heat depth.

---

## PRD-DELTA (routed to CTO to fold into docs/architecture/NFRA_MSGRAPH_PRD.md)

1. §4.2: REPLACE the standalone `heatmap.ms_object_subtree_heat` table with "MS heat = a dimension on the unified NFRA_DEBTSCAN per-node health record (one substrate, one record, one comp-* family) per COND B."
2. §5.3: note the comp-ms-* tools thread the unified comp-* family + comp-dups, not a parallel silo.
3. §6: add S3 Gate-0 (convergence-substrate arch-gate, decision #6, gates decision #2) ahead of the S3 build.
4. §6/§9: add COND A (AWS-superset 0-diff via e99a1a601) as an S3 acceptance gate.
5. Status: S1 RAVC'd, S2 deployed (L6 validate-on-nightly), S3/S5 re-scoped per this TO.

---

## Sequencing / lane plan
- S3 Gate-0 (convergence-substrate design) → CTO arch-gate → S3 build → S3 acceptance. Owner 0.8.0_AE_CloudComp.
- S5 parallel cross-cut, gated on gateway-scope confirmation, NON-blocking. Owner 0.8.0_AE + m365-gateway lane.
- 0.8.0_AE is currently on PFMG_TAXSMA S0.3 step-1 + the msgraph L6 nightly-close; this S3/S5 re-scope queues for its next MSGRAPH cycle (not idle-blocking).
