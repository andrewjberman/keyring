# GRAPHDEPTH denominator -- fleet seam-pre-flight reconciliations + govern-side encodings (lane: 0.8.0_AE_CloudComp~C)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

## Current State

The symbiotic seam validator (built last window) immediately did its job: ~D, ~A pre-flighted it against their P0 audits and surfaced 5 govern-side reconciliations, all flagged-not-assumed. I ruled + landed all of them across two commits (410eca40b earlier, 02286234a this window). grain_contract is now denominator-complete + multi-producer + identity-converged. GRAPHDEPTH is Andrew's #1 comp-program priority; this is the substrate the whole COMP layer gates on.

**~D pre-flight (commit 410eca40b):**
- F1 RED-BLOCKER: added CALLS to edge_types (relation calls, levels [function], producer graphuni-gold, compute->compute) -- the gold function call graph (1635 edges, the single largest gold class) was a population-orphan -> every gold increment went RED. Distinct control-flow relation -> distinct type (ruling 4).
- F2 PHASING: made comp-coverage-check seam SCOPE-aware (level-granular --scope {edge_types,levels,strata} + --producer) -- a gold-tier-first increment claims its grains = GREEN-IN-SCOPE (proceed); out-of-scope = phased-pending (expected, not a false STOP); full-bar only at the final increment.
- F3 PRODUCER: every edge_type carries a `producer`; --producer scopes the registry-orphan check so cross-lane grains aren't ~D's gap.

**COO~B govern-side encodings + ~A F3/F4 (commit 02286234a):**
- COO~B(A) CONTAINS multi-producer: CONTAINS is ONE type with producer_by_pair {compute->compute=graphuni-gold(~D), resource->object=graphuni-storage(~A), compute->object=graphuni-infra(~B)} -- attribution partitions, no re-type. The compute->object level-split flagged for S4.
- COO~B(B) canonical S3Key node_identity: bucket-qualified normalized path; 3 distinct forms object/prefix/glob (wildcards LITERAL, not collapsed -- grounded in ~D's 288-key set b0ffd71f5); ~D edge-target id == ~A node id (one head, no dangling/dup).
- DENOMINATOR: new producer_attribution gate rule (10th) -- every edge_type must carry a producer disposition or FAIL = a silent gap in the universe COO~B partitions + CVO verifies. seam validator made multi-producer aware.
- ~A F3: OWNED_BY producer graphuni-infra -> graphuni-storage (~A, per the fleet DECOMP-MAP). ~A F4: OWNED_BY level s3key -> object (canonical ladder token, option A; entity distinction is the node type, not the level).

**Denominator slices (the partition universe):** ~D-gold {CALLS, READS_S3, WRITES_S3, CONTAINS-compute} ; ~A-storage {OWNED_BY, CONTAINS-storage} ; ~B-infra {RUNS, CONTAINS-lambda} ; EXTERNAL {READS=portal, SERVES=routing, DEPLOYS=deploy-seam}. union == the 9-type registry.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-coverage-check selfcheck | now 12 cases | PASS | + scope+producer-aware case + unattributed-edge_type -> FAIL (producer_attribution). |
| comp-coverage-check seam (live) | gold-tier increment, level-granular scope | GREEN-IN-SCOPE | 9 grains phased (expected), 5 cross-lane (other producers) -- the phasing fix verified. |
| comp-coverage-check check | clean ledger (10 rules) | PASS | grain stable + denominator gap-free. |
| ds-commit-gate.sh | comp_coverage_check.py | PASS | py_compile + AST + ruff clean. |

**What worked:** the seam validator caught all 5 issues PRE-population (its exact purpose) -- CALLS-orphan, the phasing false-STOP, and the producer/level/identity drifts. Encoding producer-attribution as DATA (scalar or producer_by_pair) + a no-silent-gap gate makes the denominator machine-complete on the govern side, so COO~B's partition assembly + CVO's exhaustive+disjoint verify rest on a guaranteed-attributed universe.
**What failed / gap found:** the inbox Monitor died (exit 127) mid-window -- re-armed per the /watcher caveat (no orphan, fresh Monitor bria143ht); zero messages lost (pulled inbox on re-arm). The compute->object CONTAINS level-split (~D Function-Field vs ~B Lambda-handler at the same stratum-pair) is the one non-disjoint point -- flagged for the S4 attribution map, not silently merged.

## MCP Traffic

~6 dispatches. Significant: COO~B 2 govern-side encodings (CONTAINS per-pair + S3Key identity) + the denominator-universe affirmation; ~D S3Key 3-form input + CALLS/scope reminders; ~A F3/F4 reconciliation calls; my replies -- ~D unblocked (CALLS+scope+convention), ~A F3/F4 applied, COO~B RAVC (denominator gate landed).

## Blockers

**None.** grain_contract is denominator-complete + multi-producer + identity-converged; the producer_attribution gate guarantees no silent gap. ~D + ~A are re-running their seam slices to scoped-GREEN (I loop COO~B on verdicts). HELD: the S4 tool-calibration phase (the precise pair x level attribution map; COO~B dispatch, mandate-first) + V1 (CVO) + COMPUNIFY manifest regen.

## Next Steps

1. **[0.8.0_AE_CloudComp~D]** re-run the gold-slice seam -> GREEN-IN-SCOPE; send the verdict; bucket-qualify READS_S3/WRITES_S3 targets to converge with ~A's S3Key ids.
2. **[0.8.0_AE_CloudComp~A]** run the storage-slice seam (--producer graphuni-storage) on OWNED_BY/CONTAINS-storage; populate S3Key nodes at the canonical id.
3. **[2.0.0_SA_COO~B]** assemble the exhaustive+disjoint denominator against the gap-free registry + RAVC CTO; dispatch S4 calibration after ~D's grain-ladder arch-gate.
4. **[0.8.0_AE_CloudComp~C]** loop COO~B on the ~D/~A seam verdicts; action the compute->object level-split in S4. Event-driven; available immediately. No cron.
