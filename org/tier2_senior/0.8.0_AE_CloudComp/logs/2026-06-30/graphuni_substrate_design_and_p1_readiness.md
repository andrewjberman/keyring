# NFRA_GRAPHUNI — substrate design arc + P1 compute-slice readiness LOCKED (lane ~D)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, IMPLEMENT

## Current State
NFRA_GRAPHUNI P1 (the graph-substrate-unification build, ~D = the COMPUTE producer of the GRAPHDEPTH fleet) is **fully readiness-LOCKED and gate-verified GREEN-IN-SCOPE**, holding only on the CVO pre-delta fixture-lock. No graph mutation performed (P1 is hard-gated). This block followed the P0 D1 audit (prior log `b1cb3c039` / session-close `2040Z`); a large Andrew-driven design arc + multi-lane coordination happened since.

**The design arc (Andrew-direct, all CTO-ratified):** the P0 finding (Kuzu holds zero Python pipeline backend) expanded into a foundational model over ~10 amendments/rulings:
- Amendment 8 — the `pipeline` layer = the FULL tier ladder (ingestion/bronze/silver/gold x bd/inf/cot/mdpf), not gold-only.
- Amendment 9 — STABLE node/edge definitions across granularities (granularity = a declared `level` on a stable CONTAINS ladder, never a per-depth re-type; edge types fixed by semantic).
- Amendment 10 — the FRACTAL model (each layer a granularity stratum; coarse resource nodes drill to fine internal structure via stable RUNS/CONTAINS/OWNED_BY; keystone: the 31 EC2 nodes ARE the pipeline runners, EC2-RUNS->PipelineScript is the missing cross-stratum seam).
- Andrew elevated the **size-invariant logic** to MSTR/Tier-0 foundational ("too big to keep buried in a TO") -> extracted to a standalone grounded artifact, routed UP to CTO->MSTR.
- The invariant is now a MACHINE-ENFORCED GATE in `comp-coverage-map.yaml` (~C built grain_contract + the `comp-coverage-check seam` tool; selfcheck 9/9, injected-1:1-rollup -> FAIL).

**Symbiotic /seams protocol (Andrew-direct):** ~D (populate) + ~C (govern) validate the seam IN UNISON via one joint tool (`comp-coverage-check seam`, 3-axis, both-sign, stop-on-red). It paid off TWICE pre-population: (1) my pre-flight catch of CALLS missing from the registry (~C added it); (2) ~A's F1 bucket<->key seam (my keys were bucketless; 23 bd+inf collisions).

**Producer-partitioned GRAPHDEPTH fleet:** ~D=compute / ~A=storage / ~B=infra+cross-stratum / external=portal/routing/deploy. My COMPUTE slice (ruled, disjoint, GREEN-IN-SCOPE):
- Edges: CALLS 1635 (fn->fn) + compute READS_S3 306 + compute WRITES_S3 270 + compute-internal CONTAINS 1210 (Pipeline->Script->Function, levels container/file/function) = **576 edges**.
- Reference set: **201 (bucket,key)-qualified S3 keys** (handed ~A for S3Key node convergence; 87 lambda-only keys + 13 shared go to ~B).
- Reattributed OUT: 327 lambda-endpoint READS_S3/WRITES_S3 (resource->object) -> ~B per the per-stratum-pair ruling.

## Compiler Tools
| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-kuzu | node/edge census + EC2-RUNS check + 0-row gold/CALLS proofs | PASS | the substrate baseline; EC2 nodes ARE the runners; no cross-stratum drilldown edge exists. |
| comp-coverage-check selfcheck | verify ~C's grain+fractal gate | PASS | 9/9; injected 1:1-rollup -> FAIL (existential enforced). Independent verification of ~C's handoff (not self-report). |
| comp-coverage-check seam | `--edges B --rollup` (CALLS fixture) | RED (correct) | caught CALLS as population-orphan pre-population -> ~C registry-fix. |
| comp-coverage-check seam | `--scope <gold> --producer graphuni-gold` | GREEN-IN-SCOPE | compute slice clean post-unblock; scope covered, cross-lane attributed, phased-pending correct. |
| comp-grep | locate grain_contract in comp-coverage-map.yaml | PASS | on-rails registry read (grounded my populate-target). |
| (read) graph.json TraceGraph | python read-only: edge-grain split, firm-qualification, S3Key reference set | PASS | 576 compute / 327 lambda split; 23 bd+inf collisions; 201-key coupling set. |

**What worked:** running the joint seam tool on representative fixtures BEFORE populating a single edge surfaced 2 real defects (CALLS-missing, bucketless/lambda-grain) that would otherwise have hit mid-population. Independent verification (selfcheck 9/9, the CALLS-RED, the GREEN-IN-SCOPE) grounded every claim against the live gate, not self-report.
**Gap found:** none in the tooling. The pre-flight seam + producer-partition discipline are working as designed.

## MCP Traffic
~25 dispatches this block (high-bandwidth live design). Significant: RAVC2 P0 gap-list -> COO~B cc CTO+CVO (CTO confirmed = D1 derive spec + ruled 4 residuals); 3 amendment-ratifications from CTO (8/9/10) + 2 refinements (population-phasing, ruling-4 reconciliation); the symbiotic /seams protocol (COO~B Andrew-direct); the joint /seams tool + canonical-id from ~C; the ~A F1 bucket<->key seam; COO~B's producer-partition + per-stratum-pair rulings; the 201-key coupling handoff to ~A direct. Foundational size-invariant principle routed UP to CTO->MSTR.

## Blockers
None operational. P1 build hard-gated on CVO pre-delta fixture-lock (the inviolable no-regression ordering) + COO~B's P1 GO — a real external gate, not assumption-blocked. All ~D-side prerequisites cleared (registry CALLS+--scope+canonical-id landed; scope GREEN-IN-SCOPE; reference set handed to ~A).

## Key commits (this block, all read-only / design / readiness — zero mutation)
b63c17f63 (amend 8+9) / 85129b12f (sec-10 fractal) / f375988d4 (CTO refinements) / 34d8c138b (size-invariant principle) / 047ce51d0 (rollup existential-correction) / b0ffd71f5 (P1 readiness) / 39d5d2fb5 (288-id ref set) / 4c6fc9352 (corrected 201-key compute scope + GREEN-IN-SCOPE).

## Next Steps
1. **[3.0.0_SA_CVO]** lock the pre-delta no-regression fixture (the P1 gate).
2. **[2.0.0_SA_COO~B]** P1 GO once fixture locks; assemble the exhaustive+disjoint denominator (~A storage + ~D compute 576/201 + ~B infra incl the 327).
3. **[0.8.0_AE_CloudComp~A]** populate the 201 (bucket,key) S3Key nodes; ping ~D for the convergence /seams.
4. **[0.8.0_AE_CloudComp~D]** on P1 GO: populate the compute slice gold-first to the grain contract, bucket-qualify edge targets to ~A's S3Key ids, run the joint /seams to scoped-GREEN per tier. HOLD until the GO — no graph mutation.
