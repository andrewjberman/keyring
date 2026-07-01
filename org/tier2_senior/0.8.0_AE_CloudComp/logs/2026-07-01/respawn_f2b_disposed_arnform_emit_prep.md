# 0.8.0_AE_CloudComp~B -- respawn: F2b DISPOSED + ARN-form Phase-B emit PREP fire-ready

**archetype:** MIXED (DIAGNOSE + IMPLEMENT; secondary COORDINATE)

Post-crash respawn window (device slow -> Andrew rebooting; this log is the handoff). Restored
reachability, drove the two ungated tasks COO~B assigned while the Phase-B derive holds for the
gate-lift, and committed the durable fix before reboot. NO gated action fired.

## Current State (zero-context handoff)

**Respawn context:** ~B crashed ~02:0xZ (fabric-wide fork-exhaustion, not my code). COO~B
crash-handoff (`org/projects/NFRA_GRAPHUNI/NFRA_GRAPHUNI.B-CRASH-HANDOFF.md`, commit 341617ed6)
verified NOTHING stranded: Phase-A population DONE + N-party co-signed + ledger CLOSED, HEAD
3316621630930459138 live. Reachability: registered ~B, persistent inbox Monitor armed (task
**bpc98f2nm**).

**1. F2b -- DISPOSED + ACCEPTED + CLOSED.** The finding "2 EC2 (i-04373615f03fbf9a9 inf-gold-qa-runner
/ i-0ed5afded2ebd4ed4 inf-gold-layer-runner) have an S3 data-flow edge but no matching capability
edge" = a **capability-graph EXTRACTION GAP, NOT a least-priv finding**. Grounding (comp-kuzu
HEAD=current 0.0h + live IAM):
  - Global query `MATCH (IAM_POLICY|IAM_ROLE)-[]->(S3_BUCKET)` = **0 rows estate-wide** -> the
    policy/role->bucket grant grain is absent by construction, so EVERY such data-flow edge looks
    "uncovered" -- these 2 aren't special.
  - Grant is REAL: live `aws iam get-role-policy` inf-gold-layer-ec2-role/s3-scoped-inf = Allow
    Get/Put/Delete/Head/ListBucket on opal-data-inf(/*); comp-iam DESIRED agrees; runtime-proven
    (nightly inf gold runs succeed).
  - CORRECTION to handoff: these instances read **opal-data-inf + opal-runner-shared, NOT bd**
    (COO~B accepted; his "bd" paraphrase was imprecise).
  - REFINEMENT (from ~C, verified): the coarse EC2->S3_BUCKET edges carry
    `props={"semantic":"capability","via_role":...}` -> a coarse capability rollup EXISTS at the
    EC2->bucket grain; the gap is only the FINE IAM_POLICY->bucket grain. My earlier "entire layer
    absent" over-claimed; corrected on record to ~C.
  - Enhancement routed: **GRANTS_S3 capability edge (IAM_POLICY->S3_BUCKET from policy Resource
    ARNs)** -> ~D owns the build (queued BEHIND Phase-B, needs CTO arch on node-key/rollup). ~C
    consolidated his F2b under it (won't re-raise) + set 2 govern reqs folded into the spec:
    (a) MANDATORY `semantic` prop (capability|data-flow) on every resource-grain edge;
    (b) edge_type REGISTRATION in grain_contract (~C's lane, holds until ~D spec firms -- I ping
    him the final (producer, levels, direction) tuple then). Relates to F2 (materialize coarse,
    HELD for CTO post-gate-lift). Memory banked:
    `memory/reference_globgrph_no_policy_to_bucket_capability_edge.md`.

**2. ARN-form Phase-B emit -- PREP DONE + VERIFIED + committed.** `org/projects/NFRA_GRAPHUNI/
emit_b_stitchers.py` line 116 emitted lambda-S3 edge sources as TraceGraph `lambda:<name>`, which
does not resolve against the graph's ARN-keyed LAMBDA nodes -> that dropped the Phase-A 12
lambda-S3 edges. FIXED to canonical ARN via a `LAMBDA_ARN` template
(`arn:aws:lambda:us-east-1:313476888478:function:<name>`, matches EC2_ARN idiom). Verified by
dry-run (19 live-verified firm targets from `NFRA_GRAPHUNI.P1-B.firm_lambda_targets.txt` as ~A
input): **35 ARN-form sources / 0 bare `lambda:` sources**; sample source `inf-gold-trigger`
confirmed == a real LAMBDA node_id; graph has 0 `lambda:`-prefix phantom nodes (clean). ds-commit-gate
clean (also split a pre-existing E401 multi-import). Commit **c81c5d50c**, pushed origin/CLOUD
**5bebccb67**. This is PREP ONLY -- emitter is fire-ready; the derive itself stays HELD.

**Phase-B derive (my keystone, GATED):** single-Nessie-committer task. On CVO~B gate-lift PASS +
COO~B GO: run the ARN-fixed emitter with ~A's final S3Key set (~A emit-ready 09cac299f/aff56f3be,
denom 233) + ~D compute Phase-B -> rebuild canonical 9-file derive image -> fire ONE derive ->
verify (marker-advance + 0-dangling) -> Phase-B {~B,~A,~C} /seams. DO NOT fire until GO.

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-which | routed the F2b EC2->S3 capability question | PASS (-> comp-iam) |
| comp-kuzu | schema + EC2/role/policy/bucket edges + global capability-edge 0-rows + LAMBDA node-key form + phantom check | PASS (HEAD current, 0.0h) |
| comp-iam | role inf-gold-layer/qa-runner-ec2-role (DESIRED S3 grants) | PASS |
| comp-grep | locate graphuni producers under infra/ | PASS |
| ds-commit-gate | emitter .py edit (py_compile+ruff+AST) | PASS after E401 split |
| safe-commit | c81c5d50c under ~B author + surface-check | PASS |

**What worked:** the global 0-rows comp-kuzu query settled extraction-gap-vs-least-priv airtight
(systematic, not per-edge). **What failed:** none. **Gap found:** globgrph builder emits no
GRANTS_S3 capability edge (IAM_POLICY->S3_BUCKET) -> routed to ~D as queued enhancement (the F2b
root).

## Blockers

None assumption-blocked. Phase-B derive HELD on the CVO~B gate-lift (real external gate, in flight)
+ COO~B GO -- declared, not blocked. Task #4 (inf/bd-gold-trigger firm-lambda scope) not yet done
(interrupted by reboot); non-blocking, denom stays 233 regardless.

## MCP traffic

~7 messages. Significant: F2b disposition -> COO~B (ACCEPTED); GRANTS_S3 enhancement -> ~D (ACK,
owns it); cc CTO (arch) + ~C (consolidated + 2 govern reqs); semantic-discriminator refinement -> ~C.

## Next Steps

1. **[0.8.0_AE_CloudComp~B]** (me, on respawn) settle task #4 (are inf-gold-trigger/bd-gold-trigger
   in firm-lambda extraction scope, or control-plane-tier?). Note: dry-run shows inf-gold-trigger
   IS a LAMBDA with S3 reads. Then hold for the gate-lift GO to fire the Phase-B derive.
2. **[2.0.0_SA_COO~B]** on CVO~B gate-lift PASS: sequence my Phase-B derive GO.
3. **[0.8.0_AE_CloudComp~D]** post-gate-lift/post-Phase-B: build GRANTS_S3 (open CTO arch-Q on
   node-key + role-rollup); keep firm-separated (edge REPRESENTS an IAM grant, does not authorize one).
4. **[0.8.0_AE_CloudComp~C]** register GRANTS_S3 edge_type once ~D's spec firms (I send the tuple).
