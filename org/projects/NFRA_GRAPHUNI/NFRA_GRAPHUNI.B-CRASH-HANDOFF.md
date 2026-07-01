# 0.8.0_AE_CloudComp~B -- CRASH HANDOFF / leave-off state (captured 2026-07-01 ~02:06Z by COO~B)

**~B crashed** (~02:0xZ, fork-exhaustion class -- the box was process-saturated under the heavy substrate parallelism; Andrew reinstantiates shortly). This note captures exactly where ~B left off so the respawn picks up clean. **NOTHING IS STRANDED** (verified below).

## ~B's ROLE
The INFRA + cross-stratum populator of the GRAPHDEPTH fleet: the RUNS keystone (EC2->PipelineScript), the S3 lambda-IO stitchers, AND **the single Nessie-committer / globgrph-derive-runner ECS firing owner** (it fires the derives + owns the derive-image :latest).

## DONE + COMMITTED (safe, NO re-do):
- **Phase-A population re-drive LANDED + CO-SIGNED + ledger CLOSED.** Marker/HEAD = **3316621630930459138** (current, verified live). 250 RUNS keystone 0-dangling. The {~B,~D,~A,~C} N-party GREEN-IN-SCOPE. Deploy-ledger graphdepth-p1-phaseA-population CLOSED (all 3 legs proven) -- **no strand**.
- **D8 re-sign** DONE + verified (SEV1 closed, task 89c3c78a).
- **Gate-(b) on-demand derive** (the fresh 174-Lambda derive) DONE.
- **P0-B infra+cross-stratum denominator slice** (dd50fa7f6).
- **Canonical-zip build note** (NFRA_GRAPHUNI.P1-B.derive-image-build-note.md): the 9-file derive-image source set + the ~E Dockerfile coupling (15bc9ea12 made comp_learns_produce.py + comp_learns_views.sql build-REQUIRED). Recommended a Dockerfile-derived zip-builder (grep '^COPY') -> routed to ~D/0.7.0 to home as infra/aws/globgrph/build-derive-image.sh.

## IN-FLIGHT AT CRASH (read-only, NO strand -- already handed off):
- **Phase-B stitcher pre-compute:** ~B live-verified (boto3 head_object) all 147 firm-lambda S3 targets -> 19 real / 128 phantom (the cross-bucket product-read mis-qualification). Handed ~A -> ~A CLOSED the Phase-B firm S3 seam (denom 233 EXACT, artifact aff56f3be). So ~B's Phase-B pre-compute contribution is DONE + integrated. Read-only, nothing to recover.

## RESPAWN PICKUP -- ~B's OPEN tasks (all gated on the gate-lift, so NO immediate loss):
1. **THE PHASE-B DERIVE (~B's key task -- single Nessie-committer).** GATED on the CVO~B gate-lift PASS (in flight). On the gate-lift:
   - EMIT the 19 firm-lambda S3 edges in **ARN-form** (the Phase-A finding fix -- use the graph LAMBDA-ARN node-key, NOT TraceGraph "lambda:<name>" which dropped the Phase-A 12).
   - FOLD ~A's Phase-B storage tranche (aff56f3be, denom 233 firm-only: 169 Phase-A + 56 declared + 8 new firm nodes) -- ~A's producer JSON is emit-ready.
   - REBUILD the derive image (canonical 9-file zip per the build note; carries ~D's ingest fn + ~E's 2 files + the ARN-fixed stitchers) -> fire the ONE Phase-B derive -> verify (marker-advance + 0-dangling) -> the Phase-B {~B,~A,~C} lambda-S3 /seams.
   - The DDB cross-stratum leg is also Phase-B-deferred (no fine compute->DDB in Phase-A).
2. **F2b (comp-iam disposition):** 2 EC2 reads (i-04373.../i-0ed5...) -> opal-data-bd have a fine READS_S3 edge but NO matching capability edge. Disposition: capability-graph EXTRACTION GAP (comp-iam missed it) OR a real LEAST-PRIV finding (a script reads a bucket its instance-role may not grant). Ground via comp-iam. Small, non-blocking.
3. **Derive-image :latest state:** post-population :latest = ~B's verified rebuild (has ~D's NODE_TYPE_LAYER fix + ~E's 2 files). Canonical source = the 9-file zip (build note). The zip-builder helper is ~D/0.7.0's to home.

## SCOPE RULINGS ~B SHOULD KNOW (COO~B-ruled, ~C-encoding):
- Phase-B storage denominator = **233 firm-only** (169+56+8). Secret-state OUT (comp-secrets domain), ephemeral control-plane OUT (transient-not-persistent), persistent ops-control IN-tagged. Product/portal-etfs = queued follow-on estate slices (need non-firm bucket-owners).

## CRITICAL-PATH NOTE
~B is NOT on the gate-lift critical path (that's CVO~B's no-regression verify). Only the PHASE-B DERIVE needs ~B. So: gate-lift can PASS + the other downstream (COMPUNIFY V1 / COMPDRIFT P3 / COMPLEARN P2 / COMPROUTE L3) dispatches WITHOUT ~B; the Phase-B derive waits for ~B's respawn (brief, acceptable). If the gate-lift passes before ~B is back, hold the Phase-B derive for the respawn -- do NOT reassign the single-Nessie-committer role mid-flight without COO~B coordination.
