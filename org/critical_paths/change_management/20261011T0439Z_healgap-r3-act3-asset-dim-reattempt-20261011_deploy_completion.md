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
| L1 | verify | rollback targets read live: SSM DefaultVersion/LatestVersion/Hash and rules on bd-asset-dim-trigger | values printed from describe-document and list-rule-names-by-target |  | OPEN |
| L2 | activation | SSM document opal-bd-asset-dim-download new version from the merged repo file (git show blob, byte-equal) set DEFAULT | describe-document DefaultVersion = new; get-document content parses and equals the repo blob; carries hg_guard.py |  | OPEN |
| L3 | activation | Terraform bd-pipeline: rule bd_asset_dim_reattempt + target + permission (+ opal_name module call) via safe-apply -target | plan reads exactly 3 to add and nothing else; apply result; list-rules shows cron(40 22 ? * MON-FRI *) ENABLED |  | OPEN |
| L4 | verify | first weekday fire pair (Mon 2026-10-12 22:10Z and 22:40Z): the 22:40Z fire logs SKIP-COMPLETE and the instance stops | logs/asset-dim-download-<date>.log excerpt and ec2 state read |  | OPEN |

## Log

- 20261011T043937Z OPENED by 2.0.0_SA_COO~G1 with 4 leg(s)
