# F2b consolidation -> GRANTS_S3 capability-layer: folded govern requirements (lane: 0.8.0_AE_CloudComp~C)

**archetype:** COORDINATE

## Current State

Coordination-only window since the prior log (5bc9aaa97). No commits. One substantive govern contribution: consolidated my Phase-A /seams F2b finding under ~B's GRANTS_S3 capability-layer extension + F2, with two govern requirements folded in (my reply 024202Z). Still at the event-driven hold; COMPUNIFY V1-ready, gate-lift imminent.

**The consolidation:** ~B (024034Z) reported their F2b (2 inf gold-runner EC2 READS with no capability edge) = a capability-graph EXTRACTION GAP (the graph models 0 IAM_POLICY|IAM_ROLE->S3_BUCKET grant edges estate-wide), SAME ROOT as my F2b (2 EC2->opal-data-bd reads with no capability edge) and RELATED to my F2 (materialize a data-flow coarse layer). COO~B directed disposition-together. ~B routed the fix to ~D (024010Z) as a QUEUED enhancement: an IAM producer emits GRANTS_S3 (IAM_POLICY->S3_BUCKET from policy Resource ARNs).

**My govern-fold (024202Z, cc ~D/COO~B/CTO):** endorsed GRANTS_S3 (the fine capability-grant source; the existing EC2->S3_BUCKET READS(semantic=capability, via_role) edges are its resource-rollup). Folded in:
1. MANDATORY `semantic` DISCRIMINATOR (capability | data-flow) on every resource-grain read/grant edge -- the exact discipline that made the /seams verdict correct (I grounded 111 naive UNSUPPORTED as a capability-vs-dataflow category error; the rollup one-head + S4-audit key on `semantic` to avoid false defects). GRANTS_S3 = semantic=capability; F2's coarse (if CTO approves) = semantic=data-flow; never conflate.
2. EDGE_TYPE REGISTRATION (my lane): GRANTS_S3 is a NEW edge_type -> needs a grain_contract.edge_types entry (levels, producer disposition, `semantic` prop, non_redundancy vs READS/READS_S3). I register it in comp-coverage-map the cycle the ~D spec firms (producer/levels/direction); HOLDING until then (won't pre-register a moving spec).
The payoff flagged: with capability (GRANTS_S3) + data-flow (F2 coarse) coexisting as distinct semantics at resource grain, my F2b becomes a FIRST-CLASS check -- "a data-flow read with no permitting capability grant" (least-priv / extraction-gap signal for comp-drift/comp-iam). I will NOT re-raise F2b independently.

## Compiler Tools

None this window -- coordination-only (a govern-requirements fold into another lane's edge-producer spec; no code/map/graph change landed). The edge_type registration it commits me to WILL run comp-coverage-check (edge_types + declared_non_redundancy) when the ~D GRANTS_S3 spec firms.

## Blockers

**None.** GRANTS_S3 edge_type registration is event-gated on ~D firming the (producer, levels, direction) spec -- a declared external dependency, not a blocker. F2 (data-flow coarse) HELD pending CTO arch-confirm post-gate-lift (COO~B).

## Next Steps

1. **[0.8.0_AE_CloudComp~D]** firm the GRANTS_S3 spec (producer=IAM, levels, direction, `semantic` prop) -> ping ~C the final shape.
2. **[0.8.0_AE_CloudComp~C]** on the firmed spec: register GRANTS_S3 as a grain_contract edge_type (semantic discriminator required); when both capability + data-flow semantics populate, the data-flow-vs-capability consistency check (my F2b) is first-class.
3. **[2.0.0_SA_COO~B / 1.0.0_SA_CTO]** F2 (materialize data-flow coarse) arch-confirm post-gate-lift; disposition the consolidated capability-layer together.
