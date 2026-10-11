# Deploy Completion Record
**Date opened:** 2026-10-11T04:39:37.954859+00:00
**Status:** OPEN
**Deploy:** MDPF_HEALGAP R3 act 3 (HG-t-11): SSM document opal-bd-asset-dim-download guard published FIRST as a new DEFAULT version, then the 22:40Z re-attempt rule (3 resources) via safe-apply. CTO half SIGNED @c5c432ce9b (msg 3485). Rollback: update-document-default-version 5 (Hash d3a38c7b1a92b3d9..., created 2026-10-01T02:14:59-04:00) and destroy -target of the three rule resources. If ssm:UpdateDocument is denied the act stops with nothing changed.
**Authored by:** 2.0.0_SA_COO~G1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 48.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | rollback targets read live: SSM DefaultVersion/LatestVersion/Hash and rules on bd-asset-dim-trigger | values printed from describe-document and list-rule-names-by-target | Read live 2026-10-11T04:40:05Z: SSM opal-bd-asset-dim-download DefaultVersion 5, LatestVersion 5, Hash d3a38c7b1a92b3d92030c241ab6502245c5a25d3b40930dcef67548943d3f407, created 2026-10-01T02:14:59-04:00, Active; rules on bd-asset-dim-trigger: bd-asset-dim-pipeline-trigger (1, cron(10 22 ? * MON-FRI *) ENABLED). Repo blob at merged HEAD: 12423 bytes, LF only, sha256 65a15c80f434e8d0.., 160 runCommand lines, hg_guard on 3 lines. ssm:ListDocumentVersions is AccessDenied to this principal (rollback is by DefaultVersion 5, which publishing 6 never deletes). | CLOSED 20261011T044032Z |
| L2 | activation | SSM document opal-bd-asset-dim-download new version from the merged repo file (git show blob, byte-equal) set DEFAULT | describe-document DefaultVersion = new; get-document content parses and equals the repo blob; carries hg_guard.py | Read live 2026-10-11T04:5xZ: SSM opal-bd-asset-dim-download DocumentVersion/DefaultVersion/LatestVersion all 6, CreatedDate 2026-10-11T04:40:33Z (32s after L1 close; the publish act is the prior COO~G1 session's, inferred from timing, not read from CloudTrail), Status Active, HashType Sha256 Hash 65a15c80f434e8d07d1bf2d40f4b3e71a824490ccbc92b6a2c2136c0f21a9578. get-document Content parsed JSON equals infra/aws/ssm/opal-bd-asset-dim-download.json at HEAD cee3e03983 (== merged 8e130c8c55 blob, 12423 bytes, LF only); sha256(Content) == sha256(repo file) == the live Hash; hg_guard.py x3 in Content. Nothing re-published (a v7 would add no state). | CLOSED 20261011T045215Z |
| L3 | activation | Terraform bd-pipeline: rule bd_asset_dim_reattempt + target + permission (+ opal_name module call) via safe-apply -target | plan reads exactly 3 to add and nothing else; apply result; list-rules shows cron(40 22 ? * MON-FRI *) ENABLED | safe-apply -chdir=infra/aws/terraform/bd-pipeline apply of a saved plan (targets: module.asset_dim_reattempt_rule_name, aws_cloudwatch_event_rule.bd_asset_dim_reattempt, aws_cloudwatch_event_target.bd_asset_dim_reattempt_target, aws_lambda_permission.eventbridge_asset_dim_reattempt). Plan read 'Plan: 3 to add, 0 to change, 0 to destroy' (rule, target, permission; the module is a name function with no resource). Apply rc=0 'Apply complete! Resources: 3 added, 0 changed, 0 destroyed' at 2026-10-11T04:5xZ; tagauthz gate PASSED, tombstone gate CLEAN. Read back live: describe-rule blackdiamond-49f-asset-dim-reattempt-daily ENABLED cron(40 22 ? * MON-FRI *); list-rule-names-by-target bd-asset-dim-trigger = [bd-asset-dim-pipeline-trigger, blackdiamond-49f-asset-dim-reattempt-daily]; target Id 1 -> bd-asset-dim-trigger, Input null (same as the 22:10Z rule); lambda policy carries EventBridgeInvokeAssetDimReattempt scoped to that rule ARN; SSM DefaultVersion still 6. Untargeted drift in the file (two NFRA_MCPINDEX rules) not touched. | CLOSED 20261011T045518Z |
| L4 | verify | first weekday fire pair (Mon 2026-10-12 22:10Z and 22:40Z): the 22:40Z fire logs SKIP-COMPLETE and the instance stops | logs/asset-dim-download-<date>.log excerpt and ec2 state read |  | OPEN |

## Log

- 20261011T043937Z OPENED by 2.0.0_SA_COO~G1 with 4 leg(s)
- 20261011T044032Z LEG L1 closed: Read live 2026-10-11T04:40:05Z: SSM opal-bd-asset-dim-download DefaultVersion 5, LatestVersion 5, Hash d3a38c7b1a92b3d92
- 20261011T045215Z LEG L2 closed: Read live 2026-10-11T04:5xZ: SSM opal-bd-asset-dim-download DocumentVersion/DefaultVersion/LatestVersion all 6, CreatedD
- 20261011T045518Z LEG L3 closed: safe-apply -chdir=infra/aws/terraform/bd-pipeline apply of a saved plan (targets: module.asset_dim_reattempt_rule_name, 
