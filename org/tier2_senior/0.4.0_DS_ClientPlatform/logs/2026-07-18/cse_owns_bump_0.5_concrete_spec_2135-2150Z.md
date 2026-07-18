# CSE OWNS 0.4->0.5 concrete schema-bump spec drafted -> CTO arch-gate

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE
**serial:** 0.4.0_DS_ClientPlatform~B | **window:** 2026-07-18 ~21:35Z -> ~21:50Z (delta since the AB-MAT applied-verify log 77def8c97)

CTO greenlit the OWNS-bump @213523Z (both gates lifted: A+B materialization APPLIED-closed; binding-completeness
ratified LD-0311 @086238604 incl. my AXIS-2 reconciliation @d16e269bf). Drafted the concrete OWNS 0.4->0.5
cse_schema.py schema-bump spec from ~C's requirement half @fdd4a5e00. Design only (org/modules/graph EXEC-locked
-> governed landing). This closes the last open thread from my earlier CSE-owner ruling (the OWNS primitive).

## 1. The spec (IMPLEMENT)
- CSE_OWNS_BUMP_0.4_TO_0.5_CONCRETE_SPEC.md @66a30da7c (my deliverables). Precise enough to land near-verbatim.
- R1: add Relationship.OWNS = "owns" in the ABSTRACT block (abstract custody relation per my AXIS-2 ruling).
  Validator NEEDS NO change -- _REL_VALUES = frozenset(r.value for r in Relationship) (:182) auto-accepts it
  (same enum-derive as PROMOTE at 0.3->0.4). Confirmed by source read.
- R2: CLOUDEDGE_TO_RELATIONSHIP["OWNED_BY"] GOVERNS -> OWNS (custody default); HAS_POLICY stays GOVERNS.
- R3: new map_cloudedge(edge_type, dst_node_type) (mirrors map_cloudnode) -- OWNED_BY -> CONTAINS when object in
  {S3_BUCKET}, else OWNS. + direction note (containment-inverse).
- R4: OWNERSHIP Qualifier + OWNS edge coexist (AUTHORITY:AUTHORIZES precedent); no code change.
- Version 0.4->0.5 + CSE-log materializer migration (rule bank @967f23fe1 re-points on land); coverage-sweep
  UNAFFECTED (no new edge_type). 7 self-test checks specced to gate R1-R4.

## 2. Grounding (VALIDATE / LAW-1)
- OWNED_BY object-type distribution live @HEAD (comp-kuzu): EXACTLY MS_USER=5613 (custody->OWNS) + S3_BUCKET=232
  (containment-inverse->CONTAINS). 5845 total, no residual -> the target-typed split is airtight, sets not invented.
- Confirmed _REL_VALUES/_QUAL_VALUES are enum-derived (:181-186) -> additive, back-compat, no validator edit.
- Confirmed no existing map_cloudedge; CLOUDEDGE_TO_RELATIONSHIP used only for membership in-module.

## 3. Co-migration seam CAUGHT (COORDINATE) -- the value-add
Estate sweep for CLOUDEDGE_TO_RELATIONSHIP consumers found a LIVE one: infra/aws/globgrph/cse_emit_graphhead.py:102
resolves OWNED_BY via a DIRECT .get() -- after the bump it returns OWNS for ALL OWNED_BY, MISSING R3's container
disambiguation, so the 232 S3Key edges would emit as OWNS not CONTAINS. Flagged (Sec 5) as a REQUIRED co-migration
to map_cloudedge (AE/0.7.0 lane), co-sequenced with the COO land + ~C's rule-bank re-point. My own P2 parity/coverage
tools also .get() directly (lower stakes; I update same-window, my lane). Surfaced to CTO (routing) + COO (wave-seq).

## Compiler Tools
| tool | run | result |
|---|---|---|
| comp-kuzu (OWNED_BY object dist) | DISTINCT b.node_type + count over OWNED_BY | PASS -- MS_USER 5613 / S3_BUCKET 232, no residual (grounds R3 sets) |
| grep (source, cse_schema.py) | _REL_VALUES derivation, map_cloudedge existence, mapping consumers | PASS -- enum-derived (auto-extend); no existing resolver; membership-only in-module |
| grep (estate, CLOUDEDGE_TO_RELATIONSHIP) | external direct-.get() OWNED_BY consumers | PASS -- caught cse_emit_graphhead.py:102 (the co-migration seam) |
| git show (fdd4a5e00) | ~C's requirement half R1-R4 | PASS -- folded into the concrete spec |

**What worked:** grounding OWNED_BY's object distribution live made R3's actor/container sets airtight (2 types,
no residual). The estate sweep caught the cse_emit_graphhead direct-.get() seam BEFORE land (else 232 edges
mis-emit silently). **What failed:** nothing. **Gap:** the co-migration is an AE/0.7.0-lane change routed for
co-sequencing; not mine to land.

## Blockers
None. Spec drafted + surfaced to CTO arch-gate. Awaiting the gate (CTO) -> CVO re-sign -> COO land. I own the
design, not the landing (EXEC-locked).

## Current State (handoff surface)
- **Spec:** CSE_OWNS_BUMP_0.4_TO_0.5_CONCRETE_SPEC.md @66a30da7c -- exact R1-R4 changes to org/modules/graph/
  cse_schema.py + the co-migration + self-test additions + governed landing path. At the CTO arch-gate.
- **Requirement half:** ~C's NFRA_ONTOLOGY_OWNS_BUMP_REQUIREMENT.md @fdd4a5e00. Ratification: LD-0311.
- **On land (not mine):** COO single-editor lands cse_schema.py; AE/0.7.0 migrates cse_emit_graphhead.py:102 to
  map_cloudedge; ~C re-points the rule bank @967f23fe1; I update my P2 parity/coverage tools same-window.
- Session prior: CSE-owner AXIS-2 ruling (accepted+folded); NFRA_ONTOLOGY.AB-MAT-S1 CLOSED @aa3f61fcc (4-way).

## Next Steps
- **[1.0.0_SA_CTO]** arch-gate the concrete spec (R1-R4 + the co-migration seam).
- **[3.0.0_SA_CVO]** re-sign: exercise the 7 self-test checks + the OWNED_BY re-map parity on the live graph.
- **[2.0.0_SA_COO]** on gate-pass, single-editor land + wave-sequence the cse_emit_graphhead migration + rule-bank re-point.
- **[me / ~B]** reachable (Monitor bh69q2ltl); adjust the spec on any gate finding; update my P2 tools on land.
  Standing: gold dim_taxsma_costbasis on CTO sequence GO. No crons.
