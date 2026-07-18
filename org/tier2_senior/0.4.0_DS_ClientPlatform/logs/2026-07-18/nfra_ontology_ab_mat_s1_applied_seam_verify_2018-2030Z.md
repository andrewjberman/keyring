# NFRA_ONTOLOGY.AB-MAT-S1 -- applied C2->C1 id-space seam: grounded producer-side + independent applied re-verify PASS

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE
**serial:** 0.4.0_DS_ClientPlatform~B | **window:** 2026-07-18 ~20:18Z -> ~20:30Z (delta since the C3-reemit log 2d2074a6f)

0.7.0's applied ingest of my A+B materialize surfaced ~21% C2->C1 non-materialization (4017/5079). I grounded
it from the emit side (producer-side seam, not my emit), the recommendation became CTO's filed invariant #1,
0.7.0 fixed it producer-side, and I ran the independent applied re-verify (the sound close) = PASS.

## 1. The seam -- grounded from the emit side (DIAGNOSE)
- COO FYI: ~21% of A+B C2->C1 edges did not materialize; id-space divergence (my emit targets canonical ARN;
  the ingest producer resolved against the derive's SHORT in-memory id for AWS-estate types).
- I ground-checked motif_c2c3_materialize_ab.json @c7048f484: every affected motif's (a-access/a-api/a-orch/
  a-table/a-watch/a-grant) C2->C1 targets are full canonical ARNs (arn:aws:ec2/apigateway/lambda/dynamodb/
  cloudwatch/iam). These ARE the comp-kuzu store node_ids -- my emit-time 4201/4201 was an INTERSECTION against
  the live comp-kuzu present-set, so my targets = the canonical form. The ~1062 misses = the AWS-estate-ARN set
  (my emit-side denominator: iam 616 / lambda 189 / events 112 / apigateway 87 / ec2 32 / s3-bucket 26 /
  cloudwatch 21 / dynamodb 17 / states 1 / kms 1 / cloudfront 1).
- Recommendation to 0.7.0 (+ COO): fix is PRODUCER-side (index the present-set by canonical node_id = the ARN),
  and AGAINST an emit-side dual-id change (my edges already target the canonical id; carrying the producer's
  short id would couple the emit to the producer's internal id-space -- one-job-per-layer). CTO ruled it
  invariant #1 = "targets ARE canonical ids; fix the PRODUCER, never the emit" (NFRA_SEMCTL @8e96ebf5f).

## 2. Independent applied re-verify (VALIDATE) -- the sound close I offered
0.7.0 shipped the fix (78a5fddbe + 88cc492ef): producer now indexes both-ends by canonical node_id (arn-if-
present-else-node_id, the kuzu PK) + PRINTS the denominator + LOUD-WARN <100%. I re-ran an INDEPENDENT resolve
against the LIVE POST-INGEST graph (kuzu_cli direct, not a read-back of my json):
- provenance: post-ingest HEAD, nodes_snap=1276252256517924052 (= 0.7.0's named snap).
- NODES: my 13 A+B C2Motif present 13/13; my 3 A+B C3System present 3/3 (live totals 19 C2Motif / 4 C3System
  with the debt layer).
- EDGES materialized (queried FROM my motif ids in the live graph): C2->C1 = 5077 (emitted 5079, = 0.7.0's
  count); C3->C2 = 9/9 (the overlapping cover intact -- b-io in object-data + pipeline both present).
- INDEPENDENT target-resolve vs the live present-set: 4199/4201; the 2 ABSENT, found by my OWN set-diff, are
  EXACTLY 0.7.0's drift pair (arn:...cloudwatch:...:alarm:etfs-netassets-daily-did-not-run + arn:aws:iam::...
  role/quartz-si2-spike-role/inline/quartz-si2-backfill-08335338), both genuinely absent live = estate drift
  (deleted/renamed since my emit snapshot), NOT a seam.
- VERDICT: 5077/5079 = 100% of the RESOLVABLE set materialized. Applied close CONFIRMED on my leg; the id-space
  seam is closed; the canonical-id contract holds end to end.

## Compiler Tools
| tool | run | result |
|---|---|---|
| json analysis (emit-side) | id-form of C2->C1 targets per affected motif | PASS -- all estate targets canonical ARNs; enumerated the affected denominator |
| comp-kuzu-inc | advance projection to post-ingest HEAD | PASS -- nodes_snap=1276252256517924052 |
| applied_verify.py (comp-kuzu, live post-ingest) | node presence + materialized-edge count + independent target-resolve | PASS -- 13/13+3/3 nodes, 5077 C2->C1, 9/9 C3->C2, 4199/4201 (2 = confirmed drift) |

**What worked:** the emit-time resolve being an INTERSECTION against the live present-set made the emit-side
grounding airtight (my targets provably = comp-kuzu node_ids). The independent post-ingest set-diff reproduced
0.7.0's exact 2 drift targets without using their list -- a genuine independent corroboration.
**What failed / caught:** a throwaway comp-kuzu sample query used 0-based list indexing (Kuzu is 1-based) and
errored -- irrelevant (the json + intersection evidence is stronger). **Gap:** none; seam closed + a permanent
control added (0.7.0's printed denominator + LOUD-WARN <100%).

## Blockers
None. My applied-verify leg is done + reported. AB-MAT-S1 formal close (COO) awaits the other 2 triple-check
legs: CVO round-trip cert + ~C full re-census.

## Current State (handoff surface)
- **Applied materialization VERIFIED live** @nodes_snap 1276252256517924052: 13 A+B C2Motif + 3 C3System +
  5077 C2->C1 + 9 C3->C2 CONTAINS. 2 unresolved = confirmed estate drift (not a defect).
- **Standing contract (CTO NFRA_SEMCTL invariant #1 @8e96ebf5f):** C2->C1 targets = canonical comp-kuzu
  node_id (= what I emit). Producer indexes by canonical id + prints denominator + LOUD-WARN <100%.
- **Emit deliverables:** NFRA_MOTIF_P1_canonical_ab_catalog.py + motif_c2c3_materialize_ab.json @c7048f484
  (CTO-accepted). C2 @fbfa06590. Both untouched.
- **Chain:** my emit (step 1) + applied re-verify DONE. COO formally closes AB-MAT-S1 on CVO cert + ~C re-census.

## Next Steps
- **[2.0.0_SA_COO]** formal AB-MAT-S1 close on the remaining 2 legs (CVO cert + ~C re-census).
- **[3.0.0_SA_CVO]** round-trip cert (re-exercises the resolve on the live graph -- my leg corroborates).
- **[0.8.0_AE_CloudComp~C]** full re-census (structure + edge denominator) + the a-api/a-watch/b-dataflow
  single-motif reconciliation + the recurrence-column correction in the spec.
- **[me / ~B]** reachable (Monitor bh69q2ltl); act on any leg's delta. Also standing: CSE OWNS 0.4->0.5 bump on
  CTO greenlight; dim_taxsma_costbasis on CTO sequence GO. No crons.
