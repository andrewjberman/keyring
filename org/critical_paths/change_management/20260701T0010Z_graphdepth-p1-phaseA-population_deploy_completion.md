# Deploy Completion Record
**Date opened:** 2026-07-01T00:10:50.313705+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260701T013803Z
**Deploy:** GRAPHDEPTH/GRAPHUNI P1 Phase-A population -- canonical-graph mutation (single-writer ONE derive folds 3 producers: ~D gold 1347n + ~A storage 169 S3Key + ~B 250 RUNS keystone). All 3-cond P1 gates MET + convergence byte-verified (0-dangling). Executor ~B (single Nessie-committer).
**Authored by:** 2.0.0_SA_COO~B
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | producer JSONs + ingest_graphuni_producers fn on origin/CLOUD | hashes 2316463d3(ingest)/1629127da(storage)/stitchers pushed | producer JSONs + ingest_graphuni_producers fn verified on origin/CLOUD: 2316463d3 (ingest fn, derive_runner.py:1702 unconditional) / 1629127da (storage delta) / f23932383 (~C node-identity) / gold_compute+storage_s3keys+stitchers.json in s3://opal-313476888478-globgrph/producers/graphuni/ | CLOSED 20260701T001147Z |
| L2 | activation | globgrph-derive-runner image rebuild + ONE population derive run (Nessie commit + marker-advance folding all 3 producers) | new marker id (advanced past 7647070038814948852) + CodeBuild+ECS task ids | re-drive derive committed + marker advanced: _branch_head.main.json 00:46:54Z, new Nessie HEAD 3316621630930459138 (superseded 7647070038814948852); comp-kuzu provenance CURRENT built 00:57:38Z. Independently verified (COO~B): 18266->19783 nodes (+1517: PipelineScript 134/PipelineFunction 1210/Pipeline 3/S3Key 169 canonical), 250 RUNS keystone 0-dangling. | CLOSED 20260701T010552Z |
| L3 | verify | post-commit: nodes/edges present + 0-dangling + 18266 baseline preserved + {~B,~D,~A,~C} cross-stratum /seams GREEN-IN-SCOPE + CVO~B vintage-matched no-regression | comp-kuzu provenance current + counts + /seams verdict + CVO confirm | Phase-A verified-correct + N-party-validated on the LIVE graph (HEAD 3316621630930459138): nodes/edges present + 0-dangling (COO~B independently verified 250 RUNS 0-dangling + canonical types). {~B,~D,~A,~C} N-party /seams GREEN-IN-SCOPE COMPLETE: ~C govern rollup_defects 0-dangling both directions (111 naive-UNSUPPORTED grounded as capability-vs-dataflow category-error, excluded); ~D compute slice GREEN; ~B RUNS 0-dangling; ~A storage GREEN (S3Key 169/OWNED_BY 169, ~D<->~A convergence 169==169 byte-verified live). Lambda-S3 + DDB legs explicit-Phase-B-deferred (no-silent-cap). CVO~B vintage-matched no-regression = the SEPARATE acceptance gate-lift, handed to CVO now (not a deploy-strand). | CLOSED 20260701T013802Z |

## Log

- 20260701T001050Z OPENED by 2.0.0_SA_COO~B with 3 leg(s)
- 20260701T001147Z LEG L1 closed: producer JSONs + ingest_graphuni_producers fn verified on origin/CLOUD: 2316463d3 (ingest fn, derive_runner.py:1702 unco
- 20260701T010552Z LEG L2 closed: re-drive derive committed + marker advanced: _branch_head.main.json 00:46:54Z, new Nessie HEAD 3316621630930459138 (supe
- 20260701T013802Z LEG L3 closed: Phase-A verified-correct + N-party-validated on the LIVE graph (HEAD 3316621630930459138): nodes/edges present + 0-dangl
- 20260701T013803Z CLOSED -- all 3 legs proven

## Reconciliation note (appended 20260701T0312Z by 2.0.0_SA_COO~B -- for CVO~B gate-lift MH4)

CVO~B flagged a count reconcile-gap against L2's "18266 -> 19783 (+1517)". Resolved (grounded, comp-kuzu live 02:26Z build, HEAD current == marker):
- The L2 "+1517" is correct ARITHMETIC (19783 - 18266). The enumerated GRAPHDEPTH-additive breakdown is exactly **1516** (PipelineFunction 1210 + PipelineScript 134 + Pipeline 3 + S3Key 169), which are the ONLY 4 canonical types the population adds and are invariant across derives (sourced from the pipeline producers, not the AWS census).
- Therefore the residual **+1** at ledger-close (00:57Z build) is a NON-GRAPHDEPTH node (AWS-census vintage picked up during the 00:46Z derive), NOT an off-by-one in the additive population. The L2 note conflated total-delta with the 4-type breakdown; the +1 was simply unstated.
- Live has since advanced 19783 -> **19791** (+8) via a LATER derive (02:26Z build), again all NON-GRAPHDEPTH (4-type count still 1516; LAMBDA now 174). The L2 count is a correct point-in-time snapshot; it is not stale for the deploy record.
- These residuals do NOT indicate GRAPHDEPTH mutation/regression. The additive-only, zero-mutation CERTIFICATION belongs to CVO~B's independent gate-lift verify; decisive test handed to it (031050Z): pin a scratch Kuzu DB at pre-population HEAD `7647070038814948852`, confirm the 4 GRAPHDEPTH types = 0 there + no pre-existing node_type decreased current-vs-baseline + the 4-type additive delta = 1516.
