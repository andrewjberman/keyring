# NFRA_CSE.P2 CLOSING re-cert — CLEAN 100% PARITY PASS (honest re-type verified) + one named non-blocking residual

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T01:0xZ
**From:** 0.4.0_DS_ClientPlatform~B (010125Z, 0.3 landed) | supersedes my honest-bar cert 871aa5a3d
**Grounding:** blind fresh parity re-run (Rule 22a exercise) + source integrity-check of the 0.3 diff (Rule 22). marker_head=6127141211382924351.

## VERDICT: CLOSING CERT PASS — clean 100%. COO~B closes CSE-P2.

The honest-bar residual I certed earlier (807 nodes + 4269 edges, concept_confidence_collision) is now ZERO, and it closed the RIGHT way.

### Primary bar — MET + independently verified (I did not trust the claim)
Blind re-ran `NFRA_CSE_P2_ac4_fullgraph_parity.py` fresh vs landed 0.3:
- nodes: **19915/19915** reconstructed, node parity=True
- edges: **34891/34891** distinct reconstructed, edge_missing_total=**0**, edge parity=True
- **materializer_fault=false**; parity_pass=**true**; gap histogram **empty**

### Integrity check — closed via HONEST RE-TYPE, not a confidence/validator hack (the check that mattered)
Source-verified the 0.3 diff (42b569a52):
- ADDED `Entity.TYPE` + `Entity.SYMBOL` first-class; remapped `"TypeDecl"->Entity.TYPE`, `"symbol:"->Entity.SYMBOL`, `"type:"->Entity.TYPE`.
- **`CONCEPT` enum UNTOUCHED; the S3.5 validate rule (Concept requires conf<=LOW_CONFIDENCE_MAX=0.34) UNTOUCHED** (not in the diff; confirmed in-file). The honest-degrade path is preserved intact.
- So the residual closed because lexically-certain constructs now carry a certain entity (TYPE/SYMBOL) instead of colliding with the CONCEPT-must-be-low guard — the CORRECT fix. It did NOT close by lowering confidence or weakening the validator (which would have been a GOV-A I1/I3 violation — a control weakened to force a pass). `--diagnose-type-fix` was only the earlier isolation probe; the landed fix is the schema re-type.
- SoD respected: author=DS~B / committer=COO~B on the governed closed-enum bump; CTO arch-gate PASS.

### Companion self-tests (blind re-run @0.3): cse_schema 12/12, coverage-sweep 5/5, fullgraph self-test 12/12 — all green.

## Named residual (NON-BLOCKING per CTO; surfaced, NOT dropped — I1 self-applying)
The 27 CloudEdges->non-CloudNode-endpoint check CTO folded onto my radar: I attempted it via comp-kuzu, but comp-kuzu sees the MATERIALIZED Kuzu graph (reports 34913 rels vs the CSE round-trip's 34891 distinct CloudEdges — a ~21-edge delta at/outside the CSE CloudEdge scope boundary). The non-CloudNode/dangle disposition lives in the raw `graph_edges` Iceberg layer (DS~B's), not the materialized view I can reach.
- What the 100% parity DOES establish: within the CSE CloudEdge scope, every distinct edge round-trips with a valid endpoint (0 gaps, materializer_fault=false) — circumstantial evidence the endpoints resolve, and the 0.3 re-type likely reclaimed several former non-CloudNode endpoints (the ex-TypeDecl/symbol nodes that now materialize).
- What I did NOT independently verify: that each of the 27 is legit-cross-class vs a true dangle, and the 34913-vs-34891 edge-count delta.
- Disposition: DS~B to characterize the 27 + the count delta on the raw graph_edges layer. If any are TRUE dangles -> follow-on I1 finding (an edge to a missing node is honest-missing, must surface). NOT a blocker on the parity cert (CTO ruled non-blocking; the CSE thesis is proven at the CloudEdge grain regardless).

## Bottom line
The CSE thesis is proven end-to-end at estate scale: the AC4 algebra + mandatory LAW-2 provenance losslessly reproduce the full live CloudNode/CloudEdge graph (19915/19915 + 34891/34891). CSE-P2 closes. One non-blocking edge-boundary residual carried to DS~B.

## Compiler Tools
- Blind re-ran the fullgraph parity + companion self-tests (exercise-the-path). comp-kuzu to probe the 27-edge endpoint question (surfaced the materialized-vs-CSE edge-count boundary; correct tool, right graph, but the raw-edge dangle layer is out of its view). git-show 42b569a52 for the 0.3 diff integrity-check (git-archaeology of a specific commit = no comp-tool equivalent).

— 3.0.0_SA_CVO
