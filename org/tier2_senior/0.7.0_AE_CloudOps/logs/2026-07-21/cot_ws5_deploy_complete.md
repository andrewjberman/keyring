# cot WS-5 rebalancer-runner -- Andrew-direct DEPLOY-NOW, end-to-end COMPLETE
**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE
**serial:** 0.7.0_AE_CloudOps
**window:** 2026-07-21 ~22:44Z -> ~23:49Z (since last log @feca8aaff)

## Summary

Fresh session (post-/clear; watcher b152lhxpi survived, confirmed live -- context-clear case,
did NOT re-arm). Landed the Andrew-direct DEPLOY-NOW of the Cottonwood BD Rebalancer runner
(WSE_COTMDL.WS5, @b5be0f680: "deployed now... tested no-stubs... confirmation... issue to CVO").
This OVERRODE the WS-5-behind-MDPF deferral. COO locked serialize-first sequencing (cot now,
MDPF re-plans later, never concurrent on shared opal-assets state); CTO co-signed + accepted
every leg. Deploy is COMPLETE: apply -> re-plan 0-diff -> Rule-22a -> no-stub live invoke ->
tag v0.1.0 -> ledger closed 5/5. 0.6.2 (WS-1 producer) paired: built/uploaded the artifact +
source-map, ran the live invoke, confirmed Andrew + issued CVO.

## MCP traffic (~14 msgs)

- IN: 0.6.2 [URGENT] Andrew DEPLOY-NOW + apply-window request; COO shared-state sequencing (CONFIRM-or-correct);
  CTO PACKAGE-APPROVED -> CO-SIGN -> L4-ACCEPTED -> FINAL-ACCEPTANCE; 0.6.2 artifact-GO, L4 no-stub bundle, deploy-COMPLETE ACK.
- OUT: window-clean-now + sequence to 0.6.2; sequencing CONFIRMED to COO (flagged their @ab268cb90 as the STALE pre-reconcile commit); apply-gate request + staged-plan + verified-package to CTO; L4 GO + acceptance-bar to 0.6.2; MDPF exact-N grounding flag to CTO.
- Significant: CTO co-sign (pinned 10-add plan) + CTO final acceptance (L1-L4). COO "you own it, serialize." 0.6.2 confirmed Andrew + issued CVO 3.0.0_SA_CVO @233410Z.

## Deployment Sequence + Verification (AE role addition -- actual output)

Target: `infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf` @ HEAD (reconciled py3.12/no-layer;
ab268cb90 = stale py3.11+layer, NOT applied). Artifact: s3://opal-313476888478-lambda-artifacts/opal-assets/cot-rebalancer-runner.zip (10187B, verified). Source-map row landed (lambda-source-map.json:2628).

1. `terraform -chdir=infra/aws/terraform/opal-assets plan -out` (pinned) -> `Plan: 10 to add, 0 to change, 0 to destroy` (NONE destroy/change/replace).
2. Deploy-completion ledger OPENED: `20260721T2314Z_cot-ws5-rebalancer-runner` (5 legs). STOP-scan clean pre-apply.
3. `.tools/safe-apply.sh -chdir=... apply <pinned planfile>` (HALT-gate + comp-tagauthz gate passed) ->
   `Apply complete! Resources: 10 added, 0 changed, 0 destroyed.` Role arn:aws:iam::313476888478:role/cot-rebalancer-runner-role; lambda id=cot-rebalancer-runner.
4. RE-PLAN 0-DIFF: `No changes. Your infrastructure matches the configuration.`
5. Rule-22a on the LANDED role (live get-role-policy applied-truth + isolated 1-ARN/call simulate, SEPARATE invocations; comp-iam fails-GREEN on a new ARN so NOT used):
   - GetSecretValue cot/session-jnzOyC = allowed
   - PutSecretValue cot/session-jnzOyC = implicitDeny
   - PutObject cottonwood/bronze = allowed
   - PutObject cottonwood/meta = allowed
   - PutObject 49f = explicitDeny
   Positive+negative both fire (DENY discriminates). Fence (one_way_fan_in_fence) UNCONDITIONED (NotResource opal-data-assets/*) -> no --context-entries; 49f deny from write-cot's explicit Deny, not the fence.
6. L4 no-stub (0.6.2 live invoke; I INDEPENDENTLY re-ran ListObjectsV2 + read the stamp): 34 runner objects @23:31:26-30Z (>apply 23:18:21Z) -- rebalancer_models(1/60) + rebalancer_accounts(5 pages, 5 DISTINCT ETags ef49e4/21e28c/58b7d0/b26b96/daec7c) + rebalancer_model_detail(25) + meta/pulls(2) + meta/2026-07-21-complete.json. Stamp: pagination_integrity=PASS, count_reconcile=PASS, opal_assigned=296, closure model_detail=25 scope=opal_closure (>17). Triaged the 42-vs-34 (8 pre-existing realized/transactions/silver objects @03:30Z from OTHER cot producers, out of role write-scope -- not this deploy).
7. `git tag -a cot-rebalancer-runner-v0.1.0 4e668df37 -F <msg>` + `git push origin CLOUD --follow-tags` -> `[new tag] cot-rebalancer-runner-v0.1.0`, PUSH RC0.
8. Ledger CLOSED -- all 5 legs proven.

## Compiler Tools

| tool | run | result | note |
|---|---|---|---|
| comp-iam | DELIBERATELY NOT RUN | n/a | Rule 22a: comp-iam models (action) not (action,resource) + fails GREEN on a NEW ARN -> used live `aws iam get-role-policy` (applied-truth) + isolated `simulate-principal-policy` (the mandated primitive) instead. |
| (raw aws inspection) | get-role-policy / get-policy-version / simulate-principal-policy | PASS | each carried an inline `# rail-checked:` marker (comp-rail: Rule-22a new-resource verify, no comp-tool fits). |
| deploy_ledger.py | open/close-leg x5/close | PASS | the deploy-completion ledger = the deploy record (NEVER-law). |

- **What worked:** live get-role-policy + isolated simulate is exactly the new-resource primitive Rule 22a demands; the fence-unconditioned + 49f-from-write-cot reasoning avoided a multi-ARN/conditioned false-deny.
- **Gap found:** `record-terraform-deploy.sh` is ABSENT from `.tools/` (only a STALE reference in docs/deployment/TERRAFORM_PROTOCOL.md:60). Flagged to CTO -- doc names a tool that no longer exists; substituted the deploy-completion ledger + git tag + source-map as the record.

## Files Modified

- No git-tracked source edits (infra was already committed @5d49bd8b1/4fc02edfd/4e668df37 by prior session + 0.6.2).
- Created: `org/critical_paths/change_management/20260721T2314Z_cot-ws5-rebalancer-runner_deploy_completion.md` (ledger, CLOSED 5/5).
- Tag: `cot-rebalancer-runner-v0.1.0` on 4e668df37 (pushed).
- This log + org/compiler-tools-log.md.

## Current State

- **cot-rebalancer-runner: LIVE + verified + tagged.** Lambda `cot-rebalancer-runner` (py3.12, 512MB/300s, handler lambda_function.lambda_handler), role `cot-rebalancer-runner-role` (GetSecretValue-only on blackdiamond/cot/session + PutObject cottonwood/{bronze,meta} + ListBucket cond + explicit 49f Deny + one_way_fan_in_fence + basic-exec). Daily EventBridge `cot-rebalancer-runner-daily` {mode:pull} cron(0 6) PLACEHOLDER. First live pull landed real bronze under s3://opal-data-assets/blackdiamond/cottonwood/2026-07-21/.
- **Schedule time DEFERRED** (0.6.2 agreed): keep 06:00Z placeholder; pin exact time when WS-2 silver/WS-3 gold/WS-4 DDB land + the mdpf consumption window is known (CTO/WS-4 call). No downstream consumer exists yet.
- **CVO issued** (0.6.2 -> 3.0.0_SA_CVO @233410Z) for the independent IAM/TF re-verify; I'm the apply/infra owner for any CVO questions.
- **MDPF cutover: HELD (primary).** DS producer long-pole largely CLOSED (cohort_provenance + A2 done @dee1d6645, coherent set STAGED). HELD on CTO's final pre-publish S3 re-verify + co-sign (CTO+COO+Andrew) + DE render-check, then my exact-N diffs + flip. **FLAGGED to CTO a count discrepancy** (CTO status=exact-8 vs DS=coherent-9 vs my handoff=9 vs my split-log=5+2=7) -- need the resolved key list before I build. S4 parallel producer already LIVE (mdpf-pipeline-v1.6.0, publisher OFF).
- opal-assets TF state clean; cot resources now a 0-diff baseline for the later MDPF re-plan.

## Next Steps

- **[3.0.0_SA_CVO]** independent WS-5 IAM/TF re-verify (issued by 0.6.2); route IAM/TF questions to me (apply/infra owner).
- **[1.0.0_SA_CTO]** at MDPF cutover clear: give the RESOLVED exact-N key list (8 vs 9 vs 7-split; which firms x arrays; inflection in-flip or deferred) -> then I build the CF behaviors + exact-key SourceArn bucket-policy + publisher PUBLISH_MAP diffs + flip.
- **[0.7.0_AE_CloudOps]** on CTO's MDPF clear: build+commit the exact-N cutover diffs; on the S4 cycle-1 signal (next INF completion + CTO S3-verify): ListObjectsV2 the gold/mdpf_revamp keys + cycle-complete marker, report COO+CTO+DT.
- **[0.6.2_AE_PartnerETL]** relay CVO's verdict; owns the WS-2/3/4 downstream (with DS/DT).

## Blockers

None. MDPF cutover is HELD (a deliberate multi-gate on CTO's S3 re-verify + co-sign + the exact-N resolution + DE render-check) -- a gate state, not a blocker. cot WS-5 fully delivered.
