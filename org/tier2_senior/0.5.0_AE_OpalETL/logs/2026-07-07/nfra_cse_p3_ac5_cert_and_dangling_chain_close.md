# NFRA_CSE.P3 AC5 CVO-cert + the dangling-edge chain full close (delta since df14337fc)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Serial:** 0.5.0_AE_OpalETL | **Window:** ~02:42Z -> ~02:58Z 2026-07-08 (delta since the CSE-P3 AC5 log)
**Commits:** none in-window (in-VPC Trino query passes + coordination; all producer code committed in the prior window)

## Summary
CSE-P3 AC5 CVO-certed, and the 27->377->6535->ARN-aware-13 dangling-edge chain fully investigated,
adjudicated (by CVO), and closed -- with a bounded 7-real-ARN graph_nodes coverage finding routed.

## Work done

### NFRA_CSE.P3 AC5 -- CVO exercise-cert PASS (dc7e5de1d)
CVO ran live Trino over iceberg.globgrph.cse: 4 producer sources (git 6 @0.2 genesis, graph_head 50,
deploy 13, agent 15 = 84), honest-range confirmed (git/graph_head/deploy typed-HIGH, agent ALL
Concept@0.2), and the load-bearing REDACTION-SAFETY verified live (all 15 agent CSEs metadata-only,
ZERO args/content). CSE-P3 fully verified (contract cert dabb7240e + producer cert dc7e5de1d); CVO
RAVC'd COO~B. CSE-P3 AC5 = MET+certed.

### The dangling-edge chain -- CLOSED (my in-VPC pulls + CVO adjudication)
The 377-edge follow-on (raw graph_edges vs materialized CloudEdge), resolved to a clean finding:
- Pull #1 (graph_edges endpoints NOT in graph_nodes.node_id, naive): 6535 -- flagged HONESTLY as a
  likely artifact (symptom, not mechanism).
- CVO source-confirmed the MECHANISM (kuzu_nessie_load.py:143-150): edges keyed by ARN, node_id is the
  SHORT NAME with ARN in a separate `arn` column -> the loader keys on `arn-else-node_id`; my naive
  node_id-only anti-join missed every ARN-matched node -> ~17x overcount. 6535 = a JOIN-KEY artifact.
- Pull #2 (ARN-AWARE, mirroring the loader's key -- endpoints NOT matching on node_id OR arn): 13
  distinct endpoints -> 6 SYNTHETIC_WILDCARD (*:logs_to etc., correct out-of-scope) + 7 REAL_CONCRETE
  ARNs (opal-drift-producer CodeBuild, 2 subnets, bd-client-detail lambda, 3 SSM docs).
- CVO ADJUDICATED: (a) 6 synthetic CLOSED correct-by-design; (b) 7 real = a bounded upstream
  graph_nodes coverage finding (bd-client-detail flagged as a likely STALE EDGE from the decommission,
  the estate dead-route sentinel), routed to COO~B for the graph_nodes producer. CSE-P2 STAYS CLOSED
  (loader + materialized graph correct throughout; purely upstream node-coverage).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| Trino (REST via run-task) | graph_edges vs graph_nodes anti-join (naive + ARN-aware) | PASS | the 6535 -> ARN-aware-13 clean set for CVO |
| aws logs (PowerShell) | dangle query results | PASS | leading-slash log-group -> PowerShell (MSYS mangle) |

**What worked:** the honest symptom/mechanism split on the 6535 (flagged as a possible artifact, not
asserted as a gap) -- CVO's join-key catch then turned it into a crisp 7-real-ARN finding. Exactly the
discipline that prevents mis-routing a 6535 "gap" that's ~17x inflated by a join-key mismatch.
**What failed:** the naive node_id-only anti-join (6535) -- corrected to the ARN-aware key on CVO's
diagnosis. No code impact (a diagnostic query, not a producer).
**Gap found:** the 7-real-ARN graph_nodes coverage set (routed to COO for the graph_nodes producer) --
an UPSTREAM finding, CSE-P2 unaffected.

## Blockers
None. No open threads I own; all remaining moves gated on others (COO CSE-P3 close + comp-fedobs
SoD-land + the graph_nodes-coverage dispatch CVO routed) or scoped follow-ons.

## Current State (handoff)
- CSE-P3 AC5: MET + fully CVO-certed (dc7e5de1d + dabb7240e). globgrph.cse = 4-producer C0 stream (84
  rows). Producer emitters: infra/aws/globgrph/cse_emit_{graphhead,deploy,agent}.py (committed prior window).
- Dangling-edge chain: CLOSED. The 7-real-ARN graph_nodes coverage finding is with CVO->COO for the
  graph_nodes producer (not my lane).
- WHOLE-SESSION state: NFRA critical path CLOSED (CSE-P2 + FEDOBS P1/P2/P3) + CSE-P3 AC5 met, all CVO-certed.

## Next Steps
1. **[2.0.0_SA_COO~B]** close CSE-P3 (CVO RAVC'd) + SoD-land comp-fedobs + rail entries + dispatch the
   7-real-ARN graph_nodes coverage finding to the graph_nodes producer.
2. **[0.5.0_AE_OpalETL]** follow-ons (non-blocking): graph_head --full (the ~55k substantive full-graph
   stream, migration option c) + standing/scheduled producer emitters.
