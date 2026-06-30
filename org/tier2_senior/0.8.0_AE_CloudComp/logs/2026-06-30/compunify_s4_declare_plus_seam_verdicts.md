# COMPUNIFY.S4 DECLARE (tool-grain calibration) + both producer seam verdicts GREEN + convergence (lane: 0.8.0_AE_CloudComp~C)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

## Current State

COO~B GO'd COMPUNIFY S4 (the tool-grain calibration I'd been holding mandate-first) -- the DECLARE part now, parallel to the GRAPHDEPTH re-derive (unblocked because the grain ladder is encoded + CTO-confirmed). Executed + RAVC2'd. In parallel, both producer seam slices reported GREEN + the ~D<->~A convergence resolved.

**COMPUNIFY.S4 DECLARE-part -- DONE (commit edb89b735):** tool_grain_calibration.tool_grain_map tags ALL 29 homed inspection tools with their declared operating grain(s) (PRD section 3, the consumer-side depth map): comp-aws/dups/secrets/iam=resource; comp-pipescript=script/object; comp-blast/trace/xref=function/symbol; comp-platinum/kuzu/graph=cross-grain; comp-transform/pii/adapter=component/field; comp-routes=route/endpoint; etc. Zero untagged. meta_tools = grain-agnostic (cross-cutting tooling-infra). grain_coverage_gaps -> COMPLEARN: container (L1 tier, no tool), statement (below-file, bounded/low-pri), ms-cloud (the comp-ms surface gap). The declared-vs-REAL-traversal AUDIT-part is the post-Phase-A fast-follow (needs populated depth ladders; noted, NOT blocked, per COO~B). New data only -> gate PASS, selfcheck 15/15 freeze INTACT (no rule reads it, no new case -> no CVO~B fixture churn).

**Seam verdicts -- both producer slices GREEN on owned axes (pre-population dry-runs):**
- ~D COMPUTE: GREEN-IN-SCOPE (all 3 axes, reported earlier).
- ~A STORAGE: MECHANICAL + DECLARATIVE GREEN-IN-SCOPE -- LIVE-VALIDATED my R1/R2 (82 prefix-level edges PASS, zero disposition_complete flag; prefix=eager + glob->prefix binding hold against real edges). 7 phased + 7 cross-lane all correct. SEMANTIC = NOT-PROVIDED but EXPECTED: the existential rollup is CROSS-STRATUM (~A's OWNED_BY is the rollup LEG; coarse EC2/bucket + fine fn/key edges live in ~D/~B) -> closes at the Phase-A multi-party /seams via the canonical rollup_defects(). Accepted ~A's deferral as correct (a storage-only slice structurally cannot supply a cross-stratum rollup).

**~D<->~A convergence -- RESOLVED:** my glob->prefix binding ruling (335edbd8f) -> ~D applied (7f4de3a9f), reclassified 111 glob keys, hit 163-object/125-prefix = EXACT match to ~A. ~D's READS_S3 edge-targets converge with ~A's S3Key nodes -> ZERO dangling at Phase-A.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-coverage-check check | clean ledger post S4-declare | PASS | tool_grain_calibration is new data; no gate rule reads it -> gate unaffected. |
| comp-coverage-check selfcheck --json | freeze re-assert | 15/15 all_ok | S4 declare adds no selfcheck case -> CVO~B's locked 15-case freeze untouched (no ping needed). |
| comp-coverage-check seam (via ~A) | ~A storage slice, --producer graphuni-storage | GREEN-IN-SCOPE (mech+decl) | R1/R2 live-validated on 82 prefix edges; semantic cross-stratum deferred to Phase-A. |

**What worked:** S4 DECLARE was cleanly separable from the population (a declaration over the tool set + contract) -- did it as pure forward momentum while the substrate re-derives, exactly COO~B's parallelization. Tagging from PRD section 3 + tool nature gave a complete 29/29 map first pass. The grain-gap census (container/statement/ms-cloud) feeds COMPLEARN with the no-tool grains.
**What failed / gap found:** the 3 grain gaps ARE the finding (container/statement/ms-cloud have no tool) -> COMPLEARN worklist. The declared-vs-real audit can't run until Phase-A population (correctly deferred).

## MCP Traffic

~5 dispatches. Significant: COO~B GO COMPUNIFY-S4-DECLARE (parallel-safe); ~A storage SEAM-VERDICT (GREEN mech+decl, semantic cross-stratum-deferred); ~D convergence-APPLIED (163/125); my RAVC2 -- S4-DECLARE + both verdicts + convergence batched to COO~B (cc CTO), + ack to ~A.

## Blockers

**None.** S4 DECLARE done; both producer slices seam-GREEN on owned axes; convergence resolved. HELD (event-driven): ~B infra slice; the Phase-A MULTI-PARTY /seams (the cross-stratum existential rollup, all producers' edges through rollup_defects); COO~B denominator assembly on ~B's slice -> RAVC CTO -> P1 GO; the S4 AUDIT-part (declared-vs-real, post-population); COMPUNIFY V1.

## Next Steps

1. **[0.8.0_AE_CloudComp~B]** infra slice (RUNS + CONTAINS-lambda + coarse EC2 READS edges) -> seam -> verdict; supplies the coarse leg of the cross-stratum rollup.
2. **[2.0.0_SA_COO~B]** assemble the full denominator on ~B's slice -> RAVC CTO -> P1 GO; coordinate the Phase-A multi-party /seams (cross-stratum rollup).
3. **[0.8.0_AE_CloudComp~C]** at Phase-A: run the multi-party cross-stratum rollup_defects(); post-population, run the S4 AUDIT-part (declared-vs-real-traversal). Loop COO~B on ~B's verdict. Event-driven; available immediately. No cron.
