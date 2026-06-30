# NFRA_GRAPHUNI / GRAPHDEPTH — THE ENUMERATED DENOMINATOR (assembled, exhaustive + disjoint)

**Assembled by:** 2.0.0_SA_COO~B (program coordination) from the 3 producer audit slices | **For:** CTO RAVC before the /seams run; CVO~B independent exhaustive+disjoint verify.
**Sources (committed):** ~D compute (4c6fc9352 + the seam GREEN-in-scope) · ~A storage (16a511346, F1-converged) · ~B infra+cross-stratum (dd50fa7f6) · ~C registry + producer_attribution gate (02286234a).
**Machine-backing:** ~C's 10th gate rule `producer_attribution` (selfcheck: `injected unattributed edge_type -> FAIL`) guarantees this partition is NO-SILENT-GAP. CVO~B verifies exhaustive+disjoint.

> The DENOMINATOR = the FIXED, FULL EXPECTED set the /seams asserts coverage against. Per-increment /seams is GREEN within its CLAIMED scope; BASELINE-COMPLETE = GREEN only when this FULL set is covered (scope phases the path, never shrinks the set -- CTO affirmation). Partition is EXHAUSTIVE + DISJOINT over ~C's grain_contract edge_type registry: every type -> EXACTLY ONE disposition (producer slice OR declared external). union(producer-slices, external) == the registry, once each.

## EDGE-TYPE DENOMINATOR (9-type registry, attributed exactly once)
| edge_type | attribution | levels | producer | count (denom) |
|---|---|---|---|---|
| **CALLS** | scalar | function | **~D** compute | ~1635 (fn->fn) |
| **READS_S3** | producer_by_pair | object/prefix (fine) + **bucket** (coarse rollup target, F2) | **~D** (compute->object ~306) + **~B** (resource->object lambda, of the 327) | compute 306 + lambda portion |
| **WRITES_S3** | producer_by_pair | object/prefix + bucket(coarse) | **~D** (compute->object ~270) + **~B** (resource->object lambda) | compute 270 + lambda portion |
| **CONTAINS** | producer_by_pair | container/file/function (compute) · bucket/key/object (storage) · lambda/handler (infra) | **~D** compute-internal + **~A** storage + **~B** lambda-handler | per stratum-pair |
| **OWNED_BY** | scalar | s3key | **~A** storage (S3Key->S3_BUCKET) | ~311-312 |
| **RUNS** | scalar | resource->compute | **~B** infra (EC2->PipelineScript) | 23 roles / 31 instances (2 excl) |
| **READS** (portal-field) | scalar | field | **EXTERNAL** (portal/TSGRAPH) | not charged to the fleet |
| **SERVES** | scalar | route | **EXTERNAL** (routing) | not charged |
| **DEPLOYS** | scalar | deploy-seam | **EXTERNAL** (deploy) | not charged |

**Disjointness check:** READS_S3/WRITES_S3/CONTAINS are per-stratum-pair (no producer overlap on a given pair); the 327 lambda S3-IO is ~B (resource->object), distinct from ~D's 576 compute->object; CONTAINS compute-internal is ~D ONLY (bottoms at function, not Function->Field -- ~C-confirmed 2612133a5). union == the 9-type registry, exactly once. EXHAUSTIVE + DISJOINT.

## NODE DENOMINATOR
- **S3Key** ~311-312 bucket-qualified (~A); 23 bd+inf collisions split per-bucket (F1, both-lane byte-confirmed). canonical id = (bucket, normalized-s3_path).
- **GoldScriptFunction** ~1204 + **PipelineScript/GoldScript** ~136 (~D compute).
- **S3_BUCKET** 35 (exists) · **EC2** 31 · **Lambda** 174-live (~B infra; grounded LIVE, NOT the 169-stale graph -- see freshness gate).

## CROSS-STRATUM STITCHERS (net-new, 0 today) + N-PARTY /seams SIGN-OFF SETS
- **S1** EC2-RUNS->PipelineScript (resource->compute) = **{~B,~D,~C}**
- **S2** LAMBDA-CONTAINS->handler (resource->object) = **{~B,~D,~C}**
- **S3** LAMBDA-READS_S3/WRITES_S3->S3Key (resource->object, 327; 87 lambda-only + 13 shared) = **{~B,~A,~C}**; the 13 shared keys = **{~B,~D,~A,~C}**
- **R1 rollup** EC2/LAMBDA READS S3_BUCKET (coarse, exists) <= fn READS_S3 S3Key (fine) = **{~B,~D,~A,~C}**; today ALL coarse UNSUPPORTED (fine=0) -- expected pre-population.
Rule: a cross-stratum seam is /seams-GREEN only when ALL its spanned strata + ~C both/N-sign; a RED from any spanned stratum STOPS. Single-sourced check = the canonical `rollup_defects()` (28fac26f2).

## COVERED-VS-EXPECTED (today, pre-population)
The net-new gold/backend + cross-stratum edges are ~0 populated (the gold Python backend does not exist in the graph; RUNS/CALLS/READS_S3-fine = 0 confirmed). So covered=0 / expected=the full set above. The /seams measures coverage against THIS fixed denominator per-increment (scoped) + at baseline-complete (full).

## OPEN RESIDUALS (do not block the denominator; route)
- **F1** RUNS grain role-vs-instance (23 roles / 31 instances) -> ~C+~D refine the RUNS node-grain.
- **F2** coarse-READS edge_type overload: the rollup coarse target = READS_S3[level=bucket], NOT portal-READS -> ~C governor disambiguation (keeps READS_S3 multi-level vs the external portal READS distinct).
- **F3** GRAPH FRESHNESS (CORRECTED by 0.7.0 215739Z): the graph is NOT 23h-frozen -- the HEAD oracle reads 2026-06-30 02:11 (last NIGHTLY full-derive 2a, HEALTHY, 18216 nodes; ~B's "23h" read a stale vintage marker). The gap is NARROWER: the INTRADAY incremental-updater (2b) alone is VPC-egress-blocked (BOUNDED_DERIVE_FAIL, isolated -- the freeze-monitor + firefight defenses are NON-VPC + healthy), so only TODAY's intraday deploys are missing; tonight's 02:00 nightly 2a picks them up (it has API access). The denominator is LIVE-grounded so ACCURATE regardless. IMPACT softened: Phase-A population can land on the nightly-current graph (or naturally after tonight's nightly); the intraday-currency fix (0.7.0 follow-on TO, non-urgent, NOT a 49F-window slam) is a nice-to-have, not a hard Phase-A blocker. The gold-backend population (~D) derives from the gold scripts/TraceGraph, unaffected by the missing 4 intraday Lambda nodes.

## F3 FRESH-DERIVE = a HARD PRE-POPULATION GATE (CTO affirmation 215917Z, promoted from residual)
The denominator is LIVE-grounded at 174 Lambdas; the graph is at 169 (missing today's intraday deploys). Phase-A population MUST run against a FRESH graph derive (catching the live 174) -- populating on the stale graph would miss the net-new Lambdas + their RUNS/READS_S3 edges, and the /seams would then measure coverage against a denominator the stale graph cannot satisfy. SO:
- HARD GATE: 0.7.0's fresh derive (or tonight's 02:00 nightly 2a, which has API access + catches 174) lands BEFORE ~D/~A/~B populate. The denominator's live-grounding (174) is the accurate fixed reference.
- CVO~B verifies the population ran against the FRESH derive: a `current` provenance header on the populated graph; `BEHIND`/`UNKNOWN-VINTAGE` = NOT-GREEN.
- Phase-A population gate = THREE conditions (COO~B holds all; CTO vintage ruling 220955Z): **(a)** P0-CVO fixture LOCKED [DONE, both layers, 9d5765b82] + **(b)** FRESH DERIVE landed (174, tonight's 02:00 nightly 2a) + **(c)** comp-platinum AWS-chain fixture layer RE-ANCHORED@V2 by CVO~B (re-capture the AWS-resource chain from the old comp-platinum cache refreshed to 174 -- so no-regression is vintage-matched: old@V2 vs re-point@V2). All three -> COO~B GOes P1.
- VINTAGE-MATCHED FIXTURE (the no-regression baseline): vintage-STABLE answers (comp-blast/trace/xref, code-structure, AWS-deploy-invariant) stay locked@V1 (strict set-equality, the pre-mutation integrity proof holds); vintage-SENSITIVE (comp-platinum AWS chain only) re-anchored@V2. A no-regression test must compare same-vintage to isolate the re-point delta from the data-refresh delta.

## GATE-LIFT (the COMPDRIFT/COMPLEARN release condition)
producers (~D/~A/~B) both/N-sign comprehensive /seams-GREEN (covered == this full denominator, all strata/edge-types/cross-stratum seams) **AND** CVO~B independently confirms (3-axis pass + coverage==denominator + N-party sign-off). COO~B holds the gate; CVO~B is the independent confirmer.
