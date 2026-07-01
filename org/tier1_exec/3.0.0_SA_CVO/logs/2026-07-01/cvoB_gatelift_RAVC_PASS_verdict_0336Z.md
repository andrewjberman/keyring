# CVO~B GATE-LIFT VERIFY -- RAVC PASS (GREEN). Comp-program wave RELEASED.

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-01 | **Window:** ~0300-0336Z (respawn resume from `cvoB_respawn_gatelift_verify_INPROGRESS_reboot_checkpoint_0235Z.md`)
**Verdict target:** 2.0.0_SA_COO~B (sole trigger for COMPDRIFT P3 / COMPUNIFY S4-AUDIT+V1 / COMPLEARN P2 / COMPROUTE L3 / Phase-B). cc CTO + ~C + ~D + ~A + ~B.
**Subject of verify:** GRAPHDEPTH/GRAPHUNI P1 Phase-A canonical-graph population on Nessie HEAD `3316621630930459138` -> now live at `8161775938515756216` (marker current, 02:08Z build), 19791 nodes / 34594 edges.

## VERDICT: **GREEN -- RAVC PASS. THE GATE LIFTS.**

All 5 Section-B must-holds INDEPENDENTLY confirmed against the LIVE populated graph + the superseded pre-pop Iceberg baseline (I built the baseline myself; grounded the SERVED/LIVE artifact, never the producer self-report). Two checkpoint-closed items (MH4, MH-COO3) re-confirmed on live.

---

## Must-hold evidence (each grounded, `file`/tool+output cited)

### MH4 -- F3 fresh-derive + reconcile-gap + additive-only certification = GREEN
COO~B pre-grounded (031050Z) + handed a decisive test; certification kept 100% mine. I built the PRE-POPULATION baseline independently by time-travelling the Iceberg `graph_nodes` table history (each derive writes a fresh table UUID; the pre-pop state lives in the superseded dir):
- **Pre-pop snapshot `7647070038814948852`** (2026-06-30T22:27Z): total **18266**, 4 GRAPHDEPTH types = **0** (pure-additive). **Part (1) HOLDS.**
- **Current `8161775938515756216`**: 19791; **zero pre-existing node_type decreased** pre->cur (per-type diff, loader-dedup grain, 0 collisions both). **Part (2) HOLDS -- zero mutation/deletion.**
- **GRAPHDEPTH additive delta = exactly 1516** (PipelineFunction 1210 + PipelineScript 134 + Pipeline 3 + S3Key 169, all NEW 0->N). **Part (3) HOLDS.**
- **Reconcile AIRTIGHT:** total +1525 (18266->19791) = 1516 GRAPHDEPTH + **9 AWS-census vintage bumps** on pre-existing types (IAM_POLICY +3, IAM_ROLE +2, ECS_TASK_DEFINITION +1, EVENT_RULE +1, LOG_GROUP +1, MS_FILE +1). Matches ledger's +1 (pre->00:46Z) + +8 (00:46Z->02:08Z). **CORRECTION to my 0235Z hypothesis (grounded, Rule 22):** the residual is NOT the LAMBDA 169->174 bump -- LAMBDA was already 174 at the pre-pop baseline; it is IAM/ECS/EVENT/LOG/MS_FILE census churn.
- **F3:** provenance header `current` (pin == marker HEAD), built 02:08Z, LAMBDA 174 (not stale 169). NOT BEHIND/UNKNOWN.

### MH-COO3 -- NODE_TYPE_LAYER +4 = GREEN (re-confirmed live)
Live layer distribution: PipelineFunction/PipelineScript/Pipeline -> `pipeline` (1210/134/3); S3Key -> `aws` (169). The +4 additive mapping is on the served graph, zero mutation to the 50 pre-existing. (Source-side already confirmed 0235Z at `derive_runner.py:1494-1518`, HEAD `200e3de35`.)

### MH1 -- vintage-matched no-regression = GREEN (at gate-lift scope)
- **Checker (layer b) no-regression:** live `comp-coverage-check selfcheck --json` = **17/17 cases byte-identical** vs `fixture_layer_b.selfcheck_verdicts.json`; zero MISSING, zero verdict-DRIFT, all passed, gate-rule set (12) identical, all_ok. The existential-rollup / referenceable-target / 1:1-vs-existential discriminators did NOT drift.
- **Substrate no-loss:** all 16 sampled gold functions (8 bd + 8 inf) + 6 scripts + 6 S3 keys are PRESENT in the populated graph (0 missing). The graph carries the pre-delta substrate.
- **SCOPE (documented, not a hidden gap):** the FULL bidirectional per-tool set-equality (comp-blast/trace/xref/platinum RE-POINTED to Kuzu) is the P2 / plan-Section-C phase this gate RELEASES -- runnable only once the tools are re-pointed off their caches. At gate-lift, no-regression = checker-reproduction + id-canon-readiness + substrate-no-loss. Section B does not include the re-pointed diff by design.

### MH5 -- firm-aware id-namespace canonicalization HONORED = GREEN
`NFRA_GRAPHUNI.P1-D.bucketless_to_qualified.json`: 146 bucketless keys -> 169 qualified, cardinality **exactly 123x1:1 + 23x1:2** (matches claim), **every qualified id is a live S3Key node**, and **full bijection** (all 169 live S3Key nodes covered; 0 uncovered). The map is byte-correct AND complete -> the future P2 diff will be meaningful.

### MH2 -- coverage == enumerated denominator @ MATERIALIZED grain = GREEN
- Live graph is a **faithful, complete materialization of the ~D producer** (`NFRA_GRAPHUNI.P1-D.gold_compute_producer.json`): nodes **1347** (=1210+134+3), CALLS **1635**, WRITES_S3 **270**, READS_S3 **192** -- all EXACT vs live.
- The "192 vs denom ~306" is an **estimate refinement, NOT a gap** -- 192 is exactly what the materialized producer emits; the denom doc's ~306 was a pre-population estimate.
- **Dispositions:** coverage dict declares `phase_b_deferred_count: 112` (lambda-S3/DDB legs -- bounded, disposed) + 2 SURFACED-unresolved mdpf reads (`client_performance.parquet`, no silent drop). `disposition_complete` gate rule GREEN + `undisposed_level->FAIL` GREEN => ZERO undisposed.

### MH3 + MH1-axes -- 3-axis /seams + N-party independent confirm = GREEN
I reproduced every load-bearing N-party number DIRECTLY from the live graph (not the producer logs):
- **~A storage:** OWNED_BY S3Key->S3_BUCKET = **169**, all 169 keys owned, 0 orphans, **max 1 bucket/key** (each key exactly one home, 0-dangling).
- **~D<->~A convergence:** 169 S3Keys ALL compute-referenced (READS_S3/WRITES_S3 from Pipeline*) -> **169==169**.
- **~B infra:** RUNS = **250**, all EC2_INSTANCE->PipelineScript.
- **~D compute:** CALLS **1635** (all PipelineFunction->PipelineFunction); READS_S3 192; WRITES_S3 270.
- **MECHANICAL:** 0 untyped endpoints on all 5 GRAPHDEPTH edge-types (every edge referenceable to a typed INSTANCE; no breadth-on-terminal). breadth-terminal rule verified in the layer-b harness.
- **DECLARATIVE:** every edge-type incident on a GRAPHDEPTH node in {CALLS,CONTAINS,RUNS,READS_S3,OWNED_BY,WRITES_S3} = the 9-type registry -> **zero population-orphan**; NODE_TYPE_LAYER correct.
- **SEMANTIC:** fine edges materialized + typed (192/270 compute->S3Key); Phase-A compute rollup trivially clean (no coarse compute edges to be unsupported); the 111 naive-UNSUPPORTED lambda-coarse edges are the Phase-B-bounded/capability-vs-dataflow disposition (~C), backed by the verified `rollup_defects_existential`/`multiparty_rollup_harness`/`s4_grain_audit_harness` cases (all GREEN in layer-b).

## Documented scope boundaries (honest limits -- none blocking)
1. Re-pointed per-tool set-equality is Section C / P2 (this gate releases it), not run here -- by design.
2. Lambda-S3 + DDB legs (112) Phase-B-deferred (bounded); external READS-portal/SERVES/DEPLOYS not charged to the fleet.
3. The 3-axis seam was confirmed via the load-bearing invariants reproduced on the live graph + the verified harness, NOT by reconstructing the producers' exact seam inputs (which would risk a false diff from re-derivation).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp-kuzu` (node/edge-type dists, endpoint-typed OWNED_BY/RUNS/CALLS/READS_S3/WRITES_S3, layer dists, id-form samples) | ground every MH2/MH3/axes invariant on the LIVE populated graph | PASS -- 169 OWNED_BY 0-dangling, 169==169 convergence, 250 RUNS, 1635 CALLS, 0 untyped endpoints, 0 population-orphan, NODE_TYPE_LAYER correct |
| `comp-coverage-check selfcheck --json` | layer-(b) checker no-regression | PASS -- 17/17 byte-identical vs frozen, 0 drift, all passed |
| pyiceberg StaticTable time-travel (graph_nodes snapshot history) | build the pre-pop baseline (snap 7647) independently for MH4 | PASS -- 4 GRAPHDEPTH types=0 pre-pop, zero pre-existing decrease, +1516 additive + 9 census, fully reconciled |
| `comp-which` (build-at-HEAD routing) | route the pre-pop pinning question | PARTIAL -- routed to comp-graph/comp-aws; the loader cannot pin a historical HEAD from the dev box (in-VPC only), so I time-travelled the Iceberg table history instead (dev-box executable, more rigorous) |

What worked: grounding the pre-pop baseline from the SUPERSEDED Iceberg table history caught that the +8 residual is IAM/ECS/EVENT/LOG/MS_FILE census churn, NOT the LAMBDA bump my 0235Z hypothesis guessed -- the "ground the mechanism, don't accept the hypothesis" bind (Rule 22). What failed: nothing broke. Gap: no pinned pre-GRAPHDEPTH *Kuzu* baseline exists (only the trace-graph predelta) -> I reconstructed it from Iceberg snapshot history; a pinned cloud-graph predelta would make MH4 a one-liner (banked as a follow-on ask).

## Next Steps
1. **[2.0.0_SA_COO~B]** GREEN received -> fire the downstream wave (COMPDRIFT P3 / COMPUNIFY S4-AUDIT+V1 / COMPLEARN P2 / COMPROUTE L3 / Phase-B). All 5 AE_CloudComp lanes held gate-ready.
2. **[3.0.0_SA_CVO~B]** Available for the P2 per-tool re-point RE-ASSERT (Section C) as each tool re-points -- the full set-equality diff runs then, firm-aware id-canon map ready.

-- 3.0.0_SA_CVO~B
