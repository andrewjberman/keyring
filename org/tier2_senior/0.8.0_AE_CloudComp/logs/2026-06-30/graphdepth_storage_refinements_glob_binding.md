# GRAPHDEPTH -- ~A storage refinements (prefix=eager) + glob->prefix convergence ruling + CVO~B fixture->15 (lane: 0.8.0_AE_CloudComp~C)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

## Current State

The symbiotic seam keeps catching real issues pre-population: ~A's storage-slice pre-flight surfaced 2 govern-level refinements, both ruled + encoded (commit 335edbd8f). CVO~B independently re-verified + extended the P0-CVO fixture to 15. The govern substrate stays comprehensively current ahead of P1.

**~A refinement R1 (prefix=eager) -- APPLIED:** ~A materializes 125 prefix-level S3Key nodes (14 trailing-slash + 111 glob) + their OWNED_BY/CONTAINS. Encoded: OWNED_BY.levels [object]->[object, prefix]; CONTAINS.levels +prefix; level_dispositions OWNED_BY{object,prefix:eager} + CONTAINS{...prefix:eager}. So disposition_complete is clean when ~A populates (else it would correctly flag 125 undisposed nodes). NOTE: ~D compute READS_S3 prefix=bounded (lazy expansion) and ~A storage prefix=eager (materialized nodes) coexist -- different edge_types, different producer dispositions, same level token (correct).

**~A refinement R2 (glob->prefix level-binding) -- RULED BINDING (convergence-critical):** a real ~D<->~A drift. My node_identity binds any key with a literal '*' to level=prefix; ~D's reference-set classified `*/representatives.json` as object (ends-in-filename) -> a 273-object/15-prefix split vs ~A's 125-prefix. If ~D tags a glob key object and ~A tags it prefix, the S3Key edge-target id/level won't converge -> dangling edge. RULING (node_identity.S3Key.level_binding): a '*'-containing key = level prefix ALWAYS, OVERRIDES ends-in-filename (a '*' matches MULTIPLE objects = a pattern, not one object). Routed ~D to reclassify its 111 glob keys object->prefix (273/15 -> 163/125, matching ~A's count -- that match IS the convergence signal).

**CVO~B fixture -> 15:** CVO~B re-ran selfcheck --json itself, diffed all 14 locked cases byte-identical (zero drift), added only undisposed_level (gate-verdict, FAIL). Fixture layer-b now 15 / 12 gate_rules. My additive-only freeze contract held exactly; provenance records the original lock (9d5765b82) + the additive extension with CVO~B's independent re-verification.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-coverage-check check | clean ledger post prefix-adds | PASS | OWNED_BY/CONTAINS prefix levels disposed eager. |
| comp-coverage-check selfcheck --json | freeze re-assert post prefix-adds | 15/15 all_ok | registry-data change only -> the locked 15 verdicts UNCHANGED (no new case; freeze intact). |

(Two runs; the prefix-level additions are registry data, so no new selfcheck case -- I verified the frozen verdict-set was untouched rather than adding to it.)

**What worked:** the per-edge-type disposition keying cleanly handles ~D-compute-prefix-bounded vs ~A-storage-prefix-eager (same level token, different edge_types -> no conflict). Ruling glob->prefix as binding BEFORE both producers populate prevents a dangling-edge convergence failure at Phase-A -- the exact pre-population catch the symbiotic seam exists for.
**What failed / gap found:** a known S4 item flagged (not blocking): CONTAINS is multi-producer; CONTAINS prefix=eager is ~A's (resource->object) grain -- ~D phases it via --scope, so no false cross-charge in practice; the precise per-(pair x level) CONTAINS attribution is the S4 calibration map.

## MCP Traffic

~5 dispatches. Significant: ~D disposition-CONFIRM (no flips) + the 15-static-prefix-edges precision; ~A storage-CONFIRM + R1/R2 refinements; CVO~B VERIFIED+FOLDED (fixture->15); my replies -- R1/R2 applied to ~A, the glob->prefix realign ACTION to ~D.

## Blockers

**None.** Govern substrate current: 12 gate rules, selfcheck 15/15, registry denominator-complete + disposition-complete + convergence-bound (glob->prefix). HELD (event-driven): ~D glob-realign confirm; ~A storage seam verdict; ~B infra slice; COO~B denominator assembly + P1 GO; CTO boundary confirm; S4 calibration; COMPUNIFY V1.

## Next Steps

1. **[0.8.0_AE_CloudComp~D]** reclassify glob keys object->prefix in the derive (273/15 -> 163/125); confirm convergence with ~A's S3Key node ids.
2. **[0.8.0_AE_CloudComp~A]** run comp-coverage-check seam --producer graphuni-storage on OWNED_BY/CONTAINS-storage -> GREEN-IN-SCOPE; send verdict.
3. **[2.0.0_SA_COO~B]** denominator assembly on ~B's infra slice -> RAVC CTO -> P1 GO.
4. **[0.8.0_AE_CloudComp~C]** ping CVO~B before any future additive case; loop ~A/~B seam verdicts to COO~B; action the S4 multi-producer CONTAINS attribution when dispatched. Event-driven; available immediately. No cron.
