# NFRA_GRAPHUNI P1 -- fail-loud recovery + tier-agnostic node_type correction (lane ~D)

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE

## Current State
The ~B-fired population derive FAILED-CLOSED SAFELY on the first attempt (marker intact at 7647070038814948852, no commit, no corruption) -- the CVO-signed fail-loud completeness cert (`NODE_TYPE_LAYER`, derive_runner.py:1494) correctly refused to silently default my 4 new node types to `aws`. My `ingest_graphuni_producers()` WORKED (all 3 producers folded in-memory). Recovered + committed the canonical fix; awaiting CVO~B's +4-additive verify -> ~B rebuild + re-fire.

**THE RECOVERY (governance loop, this window):**
- **Diagnosed (Rule-22):** the fail-loud is the taxonomy's OWN anticipated moment -- its comment (derive_runner.py:1516-1518) says the `pipeline` layer was dropped 2026-06-26 as an empty placeholder, to "re-introduce a layer only when the data pipeline is actually graphed, gated by the fail-loud completeness cert." GRAPHUNI P1 graphed it; the cert fired 00:15Z as designed. Not a defect.
- **CTO arch-gate APPROVED with a CORRECTION** that made the schema MORE canonical: node_types must be TIER-AGNOSTIC (`PipelineScript`/`PipelineFunction` + `tier=gold` ATTRIBUTE), NOT `GoldScript` (tier-in-name). Enforces ratified amendment 1 (no per-tier re-gate at Phase B) + CVO~B's LD-0230 stable_grain rule 7 (a name-encoded grain FAILs). It's the exact stable-grain discipline ~D helped author, applied to my own emitter.
- **APPLIED + COMMITTED (200e3de35, both signs in -- CTO arch-gate + CVO~B re-confirm 002452Z):** EMITTER (extract_gold_compute.py) -> PipelineScript(134)/PipelineFunction(1210)/Pipeline(3) + tier=gold; NODE_TYPE_LAYER map -> +4 additive {Pipeline,PipelineScript,PipelineFunction}->pipeline, S3Key->aws.
- **BYTE-CONSISTENCY VERIFIED (the second-fail-close guard):** my emitter's distinct node_types == the 4 frozen map keys EXACTLY -> the re-fire will NOT NodeTypeLayerGap again.
- **CONVERGENCE UNPERTURBED:** the node_type rename kept all node-IDs (`pipeline:<firm>:gold:<script>[:<fn>]`) -> the 169 S3Key edge-targets unchanged (~A 169==169 holds) AND ~B's 250 RUNS-targets resolve 0-missing (~B re-verified). Both cross-lane co-key seams byte-clean pre-mutation.
- **RE-EMITTED** gold_compute.json to S3 (corrected node_types). ALL 3 producers now in S3: gold_compute + storage_s3keys(~A) + stitchers(~B).

## Compiler Tools
| Tool | Invocation | Result | Note |
|---|---|---|---|
| (read) derive_runner.py:1470-1519 | ground the NODE_TYPE_LAYER frozen taxonomy + the drop-comment (Rule-22) | PASS | diagnosed the fail-loud as the anticipated pipeline-layer re-introduction, not a defect. |
| python (byte-consistency) | emitter node_types vs the 4 map keys | PASS | VERDICT byte-consistent -- the guard against a second fail-close, verified before commit. |
| python (convergence re-verify) | edge-target set after the type rename | PASS | 169 S3Key targets unchanged; node-ids unperturbed -> ~A convergence survives. |
| aws s3 cp/ls | re-emit gold_compute.json + verify all 3 producers present | PASS | operational; corrected producer in S3, node_types confirmed in the emitted doc. |

**What worked:** grounding the fail-loud at source (Rule-22) showed it was the taxonomy's own anticipated gate, not a bug -- so the fix was a canonical re-introduction, not a workaround. The CTO tier-agnostic correction + CVO~B's LD-0230 grounding turned a quick 4-line map edit into the RIGHT (name-encoded-grain-free) schema. The explicit emitter<->map byte-consistency check prevented a second fail-close.
**What failed:** the first derive fired before the pipeline-layer taxonomy entry existed -- but it fail-closed SAFELY (the cert's whole purpose). Clean re-drive, no rollback.

## MCP Traffic
~10 dispatches. Significant: ~B fail-loud report -> my Rule-22 diagnosis + staged edit; COO~B staging-confirm; CTO arch-gate APPROVED-w-correction (tier-agnostic); COO~B BOTH-SIGNS-IN GO-COMMIT (+ the byte-consistency guard); I committed 200e3de35 + re-emitted + routed CVO~B verify + ~B re-fire; ~B pre-verified 0-dangling (250 RUNS) + standing ready.

## Blockers
None. The first mutation is GATED on CVO~B's +4-additive diff-verify -> ~B's image rebuild + ONE derive re-fire (~B owns the ECS run; I do not fire it). All ~D-side work done + byte-verified. A governance/coordination gate, marker-safe, not assumption-blocked.

## Next Steps
1. **[3.0.0_SA_CVO~B]** verify the committed diff (200e3de35) is +4 additive canonical + emitter<->map byte-consistent -> clear ~B.
2. **[0.8.0_AE_CloudComp~B]** on CVO~B clear: rebuild the CodeBuild image (picks up 200e3de35) + re-fire the ONE population derive -> ping ~D on marker-advance.
3. **[0.8.0_AE_CloudComp~D]** on the derive landing: verify PipelineScript/PipelineFunction nodes in comp-kuzu; co-sign the {~D,~A,~B,~C} convergence /seams + existential rollup; hand CVO~B the byte-exact bucketless<->bucket-qualified mapping; RAVC2 COO~B the slice GREEN-IN-SCOPE; PushNotification Andrew on the first commit; then resume COMPDRIFT P2.
