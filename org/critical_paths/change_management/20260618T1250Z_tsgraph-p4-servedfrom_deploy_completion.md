# Deploy Completion Record
**Date opened:** 2026-06-18T12:50:57.799785+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260618T131528Z
**Deploy:** NFRA_TSGRAPH P4 cross-domain SERVED_FROM live-land (IAM grant -> image rebuild -> re-derive -> seam-verify under real task-role)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| grant-commit | git | infra/aws/terraform/globgrph/item2a.tf P4CrossDomainServedRead | CLOUD commit hash pushed | 36231cc50 (item2a.tf ONLY, explicit single-file pathspec, 1 file/15 insertions, surface-check clean). Pushed CLOUD clean FF 5c98df6b7..36231cc50 (no rebase/force). | CLOSED 20260618T125632Z |
| grant-apply | activation | aws_iam_role_policy.derive_runner_s3 | safe-apply 0add/1change/0destroy + comp-iam gaps clean | safe-apply: Apply complete 0 added/1 changed/0 destroyed (derive_runner_s3 modified, id=opal-globgrph-derive-runner-task:DeriveRunnerS3). Post-apply plan = 'No changes' (0-diff). Live get-role-policy ground-truth: P4CrossDomainServedRead present (s3:GetObject only, Resource opal-data-portal-v2/json/*, Effect Allow). comp-iam gaps = 0 missing \| 202 deny-present (bd<->cot firm-sep guardrails, expected) \| 0 unknown -> the derive head_object->GetObject need now covered. | CLOSED 20260618T125624Z |
| image-rebuild | activation | opal-globgrph-derive-runner:latest | re-zip+upload S3 source (stitch_served_from in-zip verified) + CodeBuild build id + resolvedSourceVersion non-null + --dry-run discriminator proves new code in image | CodeBuild globgrph-derive-build SUCCEEDED (build 6f042de0). Re-zip+upload of 6-file source done BEFORE start-build (stitch_served_from + 403/404 verified in-zip; zip-member sha256 == committed d9432c119484351a). resolvedSourceVersion=null NOT trusted (ambiguous -- unversioned bucket). DEFINITIVE image-content discriminator: ECS run-task command-override sha256 of /app/derive_runner.py INSIDE the new :latest container (task 1ee1c60f, exit 0, ZERO graph writes) = d9432c119484351a7ae02fc62ad03de9032cca8520acda68148a8f3c2a78e100 == committed/local/zip-member sha; STITCH_PRESENT=True FIX_403=True FIX_404=True. New code confirmed in image. | CLOSED 20260618T130248Z |
| re-derive | activation | globgrph-graph canonical | ECS run-task exit 0 + marker advanced | ECS run-task 0b915969 (REAL derive task-role, full derive, default cmd) exit 0 -> DERIVE_RUNNER_COMPLETE. ICEBERG_NODES=12500 EDGES=19458, NESSIE_COMMIT branch=main, MARKER_STAMPED f79542e8903df869... committed_at 2026-06-18T13:06:02Z, SURFACE_SCAN findings=0 (D8-FP clean), PROPS_CARRIED intact (nodes 124 keys / edges 28 keys -- props migration preserved). | CLOSED 20260618T131520Z |
| seam-verify | verify | cross-domain SERVED_FROM seam | comp-kuzu ~29 SERVED_FROM both-ends-verified under REAL derive task-role + 403-class empty (16 visible-unresolved LOUD-distinct) | LIVE served graph (comp-kuzu auto-refreshed to marker HEAD 3470176063981055398, provenance=current/pin==HEAD): served_from_edges=29 both-ends-verified -- all 29 src=ServedURL endpointurl:/api/general/*.json, tgt=opal-data-portal-v2 (real node, 0 dangling), props verified=object+node, s3_key correctly api-general-prepend-json mapped incl json/ passthrough. model_portfolio_benchmarks edge present+correct. derive log: SERVED_FROM_STITCH formed=29 object_miss=0 iam_denied=4 node_miss=0 family_deferred=12. 403-class now LOUD-distinct (the /seams silent-no-op catch RESOLVED). The 4 iam_denied = confirmed-ABSENT objects (404 under dev creds w/ ListBucket; stale-FE URLs at non-existent paths) surfacing as 403 to the task-role due to GetObject-without-ListBucket least-priv -- NOT a real IAM gap, correctly left VISIBLE-unresolved (no grant, no widen). Verified under the REAL deployed principal, not scratch. | CLOSED 20260618T131520Z |

## Log

- 20260618T125057Z OPENED by 0.7.0_AE_CloudOps with 5 leg(s)
- 20260618T125624Z LEG grant-apply closed: safe-apply: Apply complete 0 added/1 changed/0 destroyed (derive_runner_s3 modified, id=opal-globgrph-derive-runner-task
- 20260618T125632Z LEG grant-commit closed: 36231cc50 (item2a.tf ONLY, explicit single-file pathspec, 1 file/15 insertions, surface-check clean). Pushed CLOUD clean
- 20260618T130248Z LEG image-rebuild closed: CodeBuild globgrph-derive-build SUCCEEDED (build 6f042de0). Re-zip+upload of 6-file source done BEFORE start-build (stit
- 20260618T131520Z LEG re-derive closed: ECS run-task 0b915969 (REAL derive task-role, full derive, default cmd) exit 0 -> DERIVE_RUNNER_COMPLETE. ICEBERG_NODES=
- 20260618T131520Z LEG seam-verify closed: LIVE served graph (comp-kuzu auto-refreshed to marker HEAD 3470176063981055398, provenance=current/pin==HEAD): served_fr
- 20260618T131528Z CLOSED -- all 5 legs proven
