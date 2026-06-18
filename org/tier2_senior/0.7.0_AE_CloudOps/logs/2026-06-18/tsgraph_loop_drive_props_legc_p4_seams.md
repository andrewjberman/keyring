# 0.7.0_AE_CloudOps -- NFRA_TSGRAPH /loop drive: P1 props live-migration + Leg C unblock + edge-MERGE + P4 cross-domain code + /seams catch
**archetype:** MIXED
**secondary_archetypes:** DEPLOY (props live-migration), IMPLEMENT (P4 stitch_served_from), VALIDATE (/seams + binding tests), COORDINATE (RAVC loops w/ CTO/COO/DE)
**window:** 2026-06-17 ~22:20Z -> 2026-06-18 01:00Z (Andrew /loop drive-to-completion, 5m->hourly)
**driver:** Andrew /loop "[5m] keep running until this project is complete, drive it, bother COO/DE"

## Summary
Drove NFRA_TSGRAPH from the Leg-B props gap through to P4 cross-domain code, under Andrew's drive-loop. The whole project moved through the AE lane in one session: the props payload live-migration (coordinated, ledgered, binding-verified), the DE's kind-aware Leg C unblocked+closed, the edge-MERGE completeness fix (3rd no-silent-drop instance), the P4 cross-domain SERVED_FROM code (dormant), and a /seams deep-dive on that P4 code that caught a real pre-live-land break. Two sovereign decision-points went to Andrew (drive P4 / override CTO's hold); both honored with full rigor.

## Work done (chronological)
1. **P1 props live-migration (COMPLETE, ledger CLOSED --red clean).** Coordinated deploy, safe-ordered, one deploy-completion ledger (tsgraph-props-migration, 3 legs):
   - Tolerant incremental_updater Lambda (7b99f9ca1 + zip c94933b47): commit_batch SCHEMA-TOLERANT (runtime-detects the props column -> safe pre+post add-column, no mid-state break) + props field-9. Deployed FIRST (safe-order) via Terraform safe-apply (CodeSha +wYxcb).
   - kuzu_nessie_load loader props (7b99f9ca1): CloudNode+CloudEdge gain props STRING + load end-to-end (json_extract-ready).
   - derive add-column + props-carry + no-silent-drop guard (00f2cec00, pre-window) imaged via CodeBuild f5b0a170 -> re-derive: SCHEMA_EVOLVE props on graph_nodes+graph_edges (additive metadata-only), PROPS_CARRIED nodes=124 keys + edges=25 keys (incl kind/condition/srcField/dstField), 0 SCHEMA_SEAM_SILENT_DROP, SURFACE_SCAN findings=0 (D8-FP still clean), MARKER 34ca802b.
   - **BINDING etf_spread live-test PASS** (comp-kuzu json_extract): FLOWS_TO type:...ModelPortfolioPeriodReturn#etf_spread -> out:ModelPortfolios.tsx:725#spread, props.kind="recompute/guarded", props.condition="benchmarkType === 'index' == false". Payload survives producer->derive->Iceberg-props->Kuzu end-to-end.
2. **DE kind-aware Leg C: UNBLOCKED -> F5-CLOSED** (DE-side). On props-live, the DE co-verified 961/961 FLOWS_TO carry props, 5/5 forked display-logic fields reproduce LIVE==LOCAL. P1 validated-complete PENDING CTO's deliberate cutover sign.
3. **edge-MERGE completeness fix (23ee1786f).** CTO elevated my "one note" to a pre-parity-gate requirement (3rd no-silent-drop instance): kuzu_nessie_load now MERGEs CloudEdge on {edge_type,props} (was edge_type-only) so multi-fork FLOWS_TO between the same node-pair stay DISTINCT edges. Verified collapse-free this vintage (961 FLOWS_TO on 961 distinct pairs), correct-by-construction. CTO ACCEPTED.
4. **P4 cross-domain join code (e1899add6, DORMANT).** Andrew chose "drive P4" then "override CTO's hold". Built stitch_served_from: /api/general/{X}->opal-data-portal-v2/json/{X} (DE head-object ground-truthed 29/33) + BOTH-ENDS verify (head_object source + cloud-graph S3 node_id target, co-keyed on the ACTUAL arn-form id) -> SERVED_FROM or VISIBLE-unresolved. Committed dormant (not imaged) = nightly-safe per COO; CTO+COO accepted code/scratch.
5. **/seams on the P4 code (188337932) -- caught a real break.** BROKEN@MECHANICAL pre-live-land: the derive task role (opal-globgrph-derive-runner-task / DeriveRunnerS3) lacks s3 read on opal-data-portal-v2 -> at live-land head_object would 403 -> all 29 edges fall to object-miss -> seam carries 0 live (silent no-op masked as absence). Root: my scratch-test passed only under DEV-BOX creds, not the derive's task role (env-mismatch = D8 dump-vs-derive class). Fixed the 403/404 conflation (403 iam-denied = LOUD config, distinct from 404 absent). CTO approved + scoped the read grant minimal; CTO banked "verify under the deployed principal" + owned his accept-miss.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-kuzu | etf_spread binding verify; edge-MERGE collapse check (961=961); SERVED_FROM=0 (dormant); s3 node_id=arn-form | PASS -- the binding + the co-key crux (arn not bucket-name) |
| comp-routes behaviors/rewrites | URL->S3 resolution scoping (the /api/general/* tier-split) | PARTIAL -- /api/scoped resolves clean; /api/general needs the router rewrite (DE ground-truthed) |
| .tools/deploy_ledger.py | tsgraph-props-migration open/close-leg/close/--red | PASS -- 3 legs proven, --red clean |
| .tools/safe-apply.sh | tolerant Lambda deploy (HALTGT) | PASS -- 1 changed |
| aws iam get-role-policy | /seams ground-truth: derive role s3 scope | PASS -- gap CONFIRMED (no opal-data-portal-v2 read) |
| extract_routes.build_routing_table | resolver validation (resolve_s3_key) | PASS-scoped -- /api/general returns '' (the gap finding) |

**What worked:** comp-kuzu json_extract proved the props payload + caught the arn-vs-bucket-name co-key crux; the deploy ledger held the never-half-land discipline through a live schema-migration. **What failed/gap:** the scratch binding-test ran under dev-creds not the derive role -> a false-pass that /seams (ground-truthing the LIVE role IAM) caught. **Gap found:** comp-routes can't resolve /api/general/* (the public-data-router rewrite is not in extract_routes._parse_rewrite_rules; the durable general-rule edit routes to CTO commit-through-owner post-nightly).

## Deployment Sequence + Verification (AE)
- Props deploy: tolerant Lambda (safe-apply, CodeSha +wYxcb, verified get-function-configuration) -> CodeBuild f5b0a170 (byte-match + ECR fresh) -> ECS run-task derive (DERIVE_RUNNER_COMPLETE, exit 0) -> comp-kuzu etf_spread PASS -> ledger CLOSE --red clean (8678bde0c). All live-verified at deploy.
- P4: code committed DORMANT (e1899add6) -- NOT imaged. Live image-rebuild + re-derive DEFERRED to post-nightly (COO nightly-safety; no 2nd live-graph change racing the 02:00Z nightly carrying props+NNA+cot-chain).

## Blockers
None blocking. P4 live-land is GATED (not blocked) on: (a) the 02:00Z nightly's derive completing, (b) the comp-iam-scoped cross-domain IAM grant (CTO-approved floor: s3:GetObject on opal-data-portal-v2/json/*; CTO+COO scope-review before apply). All agreed; deliberate post-nightly sequencing.

## Current State (zero-context handoff)
- **P1:** props migration LIVE on the canonical graph (marker 34ca802b), DE Leg C F5-closed. PENDING only CTO's deliberate parity-review + cutover sign (CTO's timeline, likely not tonight). Ledger tsgraph-props-migration CLOSED.
- **P4:** stitch_served_from in infra/aws/globgrph/derive_runner.py committed DORMANT (e1899add6 + 403/404 fix 188337932), NOT imaged -> the live graph has 0 SERVED_FROM edges (correct, dormant). Seam record: org/seams/cross-domain-servedurl-to-s3-join.md (verdict BROKEN@MECHANICAL pre-live-land).
- **The IAM gap:** derive_runner_task role lacks s3 read on opal-data-portal-v2; grant floor agreed = s3:GetObject on arn:aws:s3:::opal-data-portal-v2/json/* (item2a.tf derive_runner_s3, my lane), NOT applied yet.
- **Loop:** hourly cron a8ea2972 (fires :40) drives the post-nightly P4 deploy; inbox Monitor is event-driven for CTO's cutover sign.

## Next Steps
1. [0.7.0_AE_CloudOps] POST-NIGHTLY (after the 02:00Z derive COMPLETES -- verify first, don't race): the P4 atomic ledgered deploy = comp-iam-scoped grant -> surface diff+TF+ledger to [1.0.0_SA_CTO]+[2.0.0_SA_COO] scope-review -> safe-apply -> re-zip+rebuild derive image (with stitch_served_from) -> re-derive -> verify 29 SERVED_FROM both-ends-verified (16 visible-unresolved, 403s now LOUD) -> RAVC2.
2. [1.0.0_SA_CTO] P1 cutover sign (deliberate parity-review, CTO's timeline) -> P1 validated-complete; then COO 2-step close.
3. [1.0.0_SA_CTO] durable extract_routes general /api/general/{X} rewrite rule (commit-through-owner, post-nightly) -- so resolve_s3_key works estate-wide for the family.
4. [0.7.0_AE_CloudOps] the 4 positioning/sentiment exceptions: resolve their real origin/bucket then scope a separate grant, else leave VISIBLE-unresolved (no speculative grant).
