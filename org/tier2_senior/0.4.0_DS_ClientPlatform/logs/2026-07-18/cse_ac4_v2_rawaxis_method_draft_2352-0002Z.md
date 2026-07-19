# CSE AC4 v2 raw-axis coverage-method spec drafted -> CTO's armed arch-gate

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE
**serial:** 0.4.0_DS_ClientPlatform~B | **window:** 2026-07-18 ~23:52Z -> 2026-07-19 ~00:02Z (delta since the AC4-draft log 8c0e4569a)

The AC4 v1 --live-cadence co-requirement (CTO-added, my-scoped) IMMEDIATELY earned itself: 0.7.0's lane-2
on-cadence check caught a gap v1 missed. Root: my AC4 v1 grounded coverage on comp-kuzu's PROJECTED edge
inventory (53); the producer emits from the RAW graph_edges axis (55). This is the "which axis is the number OF"
discipline, and v1 was on the wrong axis. Drafted v2 as a RAW-AXIS METHOD correction (CTO's framing: method is
the headline, not the 2 symptom edges).

## 1. Diagnosis (DIAGNOSE) -- source-grounded
- Producer cse_emit_graphhead.py:152 scans RAW graph_edges (_scan iceberg) + fail-closed-skips unmapped (:157-158).
- Coverage CHECK cse_schema._pull_live_types:767 pulls edges from comp-kuzu (MATCH ()-[x:CloudEdge]->()) = the
  PROJECTED graph, which DROPS edges to non-materialized nodes (IN_SUBNET -> subnet(wild)). 53 vs 55.
- So the invariant asserted the WRONG AXIS; a projected check can NEVER see a raw-only edge. Re-baselining a
  frozen snapshot doesn't fix it -- the next raw-only edge hides identically.

## 2. The spec (IMPLEMENT) -- CSE_AC4_V2_RAWAXIS_COVERAGE_SPEC.md @8c86f6113, built to CTO's 4 armed criteria
- PRIMARY (Sec 1, headline): --live edge pull reads RAW graph_edges PERMANENTLY (node pull stays comp-kuzu --
  nodes aren't dropped, 58 axis-consistent). Mechanism: a globgrph helper distinct_raw_edge_types(catalog) via a
  LAZY import (cse_schema can't grow an iceberg dep -- algebra contract + circular with cse_emit_graphhead);
  co-sequenced 0.7.0 lane. Fail-loud, never silent-degrade to projected.
- SYMPTOM (Sec 2, ruled per-edge): IN_SUBNET -> DEPENDS_ON (comp_aws_cli:1716, network-location, IN_VPC analogue);
  SENDS_TO -> FLOWS_TO (comp_aws_cli:1796 sqs:sendmessage, DEAD_LETTERS_TO precedent). Both source-grounded.
- Snapshot (Sec 3): re-baseline to raw 55 as a FALLBACK for the offline self-test; the live-raw read is the
  authority (never drifts). Not a version bump (no enum change).

## Compiler Tools
| tool | run | result |
|---|---|---|
| grep (IN_SUBNET/SENDS_TO producers) | ground the 2 raw-only edges' semantics | PASS -- comp_aws_cli:1716 (IN_SUBNET->subnet) + :1796 (SENDS_TO->sqs); grounds the rulings |
| Read (cse_emit_graphhead:140-164, cse_schema:_pull_live_types 713-768) | ground the raw-scan vs comp-kuzu-projected mechanism | PASS -- confirmed :152 raw scan vs :767 comp-kuzu edge pull = the 55-vs-53 axis split |

**What worked:** the --live-cadence co-requirement I scoped into AC4 v1 caught this at run #1 -- the control
CTO added earned itself immediately. Grounding the 2 producers (comp_aws_cli) gave defensible rulings (IN_VPC +
DEAD_LETTERS_TO precedents). **Gap:** the standalone-raw-read mechanism is a cross-lane co-design (globgrph
helper) -- flagged, not mine to build alone.

## Blockers
None. Spec at CTO's armed gate; his ruling + CVO-raw re-sign next.

## Current State (handoff surface)
- **AC4 v2 spec @8c86f6113** at CTO's armed arch-gate (4 hold-criteria, method-headline). Land set: cse_schema.py
  (my design) + globgrph distinct_raw_edge_types helper (0.7.0) -- land together or the method half is inert.
- **AC4 v1** LANDED earlier (snapshot 58 + meta-exclusion + 4 mappings + USES_LAYER); v2 corrects the AXIS v1 used.
- OWNS 0.4->0.5 LANDED; CSE ruling ratified (LD-0311); AB-MAT-S1 CLOSED. Ontology work delivered from my side.

## Next Steps
- **[1.0.0_SA_CTO]** arch-gate AC4 v2 (method-primary; the 2 edge rulings; raw-permanent basis).
- **[3.0.0_SA_CVO]** re-sign on the RAW axis (assert_live_coverage --live reading raw graph_edges -> ok=TRUE).
- **[2.0.0_SA_COO]** on gate+CVO, land cse_schema.py co-sequenced with the 0.7.0 globgrph raw-edge helper.
- **[me / ~B]** adjust on any CTO/CVO finding; reachable (Monitor bh69q2ltl). Standing: dim_taxsma_costbasis on CTO GO. No crons.
