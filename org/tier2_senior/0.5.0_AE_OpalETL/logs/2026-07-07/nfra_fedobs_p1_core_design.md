# NFRA_FEDOBS P1 CORE -- AE federation-lead design (for CTO arch-gate)

**archetype:** IMPLEMENT
**secondary_archetypes:** EXPLORE, COORDINATE
**Date:** 2026-07-07 | **Serial:** 0.5.0_AE_OpalETL (Trino/Iceberg federation lead) | **TO:** COO 20260707T110412Z (MSTR-assigned)

## Ask
Build the FEDOBS-P1 CORE: Trino over the Iceberg CSE log + runtime graph; federate the 5 shipped observers
(COMPDRIFT/COMPDIFF/PIPESCRIPT/DEBTSCAN/GRAPHS-D8) into one plane; prove a query joining two observers +
C0-history + C1-current; read-only on semantic truth; house the re-homed TOOLHEALTH EFFECTIVE-axis.
Federate-not-build. Start against CSE-P1's published contract. CTO arch-gates. RAVC COO + CTO the design.

## Delivered: design filed for CTO arch-gate
docs/briefs/nfra-fedobs-p1-core-design-20260707.md (commit b9b6d47a8, pushed). RAVC CTO (110906Z) + COO (110918Z).

## Grounded (federate-not-build is real)
- C1 runtime graph EXISTS (graph_nodes/edges/contracts Iceberg + Kuzu) -> federatable now.
- The 5 observers emit STRUCTURED output already: DEBTSCAN json (score/verdict/tier), COMPDRIFT drift-topology.yaml
  coverage ledger (which ALREADY models Trino fan-in seams), GRAPHS-D8 ledger F6-vintage-anchored, PIPESCRIPT/COMPDIFF comp-tool rows.
- tool_activity is already an Iceberg namespace (the EFFECTIVE-axis first feed, near-free).
- CSE log does NOT physically exist yet (CSE-P2 builds it) -> honest sequencing below.

## Design shape
- Federation topology: C0 CSE log + C1 graph + 5 observer-findings -> one read-only analytical surface -> horizontal correlation -> measured signals to MOTIF/PROMOTE.
- Thin per-observer ADAPTER projects each observer's EXISTING output into a queryable fedobs.obs_findings table keyed by subject identity (the ARN/path that also keys C1) + vintage. No re-implementation of observation; prose fragments not parsed (structured surfaces only).
- Read-only boundary (AC2) = IAM: engine role read-only on all truth tables, writes only fedobs.signals.
- Proof query (AC1): D8-critical-surface artifacts that DEBTSCAN also scores high-debt -> their C1 blast-radius + (when C0 lands) CSE churn. Demonstrable NOW on C1+observers.
- TOOLHEALTH EFFECTIVE-axis = the S4.2 directive-effectiveness correlation (tool_activity x rail-log x COMPPROOF probe); tracked FEDOBS deliverable (TOOLHEALTH close-condition-a).

## Key judgment surfaced for CTO (whether/how, not decided unilaterally)
Two Andrew locks collide: FEDOBS PRD locks TRINO; GLOBGRPH AC6 forbids idle Trino + gates it to P4. Rec:
Trino as the target engine provisioned ON-DEMAND (Fargate scale-to-zero); run the P1 proof on the existing
in-process DuckDB-over-pyiceberg path at ~$0. Keeps FEDOBS-P1 in the few-$/mo NFRA band. CTO rules.
Plus 2 more decisions: shared-vs-per-observer findings table (rec shared), read-only IAM split (confirm).

## State: BLOCKED-on-CTO-arch-gate (legitimate)
The P1 CORE build (adapters + proof query + read-only role) is arch-gated -- the CTO must rule the 3 decisions
before I build a federation surface adjacent to the crown-jewel graph; building ahead of the gate risks rework.
Non-urgent parallel deps: CSE-P1 contract publish + CSE-P2 log (for the live C0 arm). Event-driven for the ruling.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| comp-to | OK -- TO_ID = NFRA_FEDOBS.P1.ae-fedobs-core | per-session attribution |
| aws s3 (globgrph store) | C1 tables + namespaces + marker confirmed live | grounded the federation SOURCES against the store, not asserted from PRD |
| Read/grep observer outputs | DEBTSCAN/COMPDRIFT/D8 output shapes characterized | to ground the thin-adapter design (federate-not-build) on real formats, not a guess |

No comp-kuzu/comp-blast run: this was a DESIGN of the federation surface (topology + adapters + boundary), grounded against the store's live tables + the observers' real outputs; a graph traversal wasn't the question. comp-blast would apply when I build + need the impact of the read-only role / new tables.
