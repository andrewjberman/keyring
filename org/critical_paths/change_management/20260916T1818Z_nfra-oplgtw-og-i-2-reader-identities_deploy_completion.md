# Deploy Completion Record
**Date opened:** 2026-09-16T18:18:21.199253+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260916T182956Z
**Deploy:** NFRA_OPLGTW OG-i-2: Schwab reader identities -- data role opal-mcp-emp-menachem-schwab-read, catalog role opal-mcp-schwab-catalog-read, one assume statement on opal-gateway-role, ExternalIds secret and account_ref key secret with Gateway read resource policies
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | infra/aws/terraform/opal-gateway/schwab_reader_iam.tf committed on wk-nfra_oplgtw-1-1c BEFORE the apply, with this entry and its OPEN sentinel | commit hash | commit 9efbe7a275 on branch wk-nfra_oplgtw-1-1c adds infra/aws/terraform/opal-gateway/schwab_reader_iam.tf together with this entry and its OPEN sentinel, committer time 2026-09-16T18:19:45Z -- before the apply start 2026-09-16T18:22:50.350290Z | CLOSED 20260916T182955Z |
| L2 | activation | terraform apply of infra/aws/terraform/opal-gateway through .tools/safe-apply.sh creating exactly the ten OG-i-2 resources, 0 to change, 0 to destroy, judged by the in-run guard | safe-apply rc 0 and the Apply complete line | bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply -no-color, ONE run, rc 0, start 2026-09-16T18:22:50.350290Z end 2026-09-16T18:25:35.796609Z, HALT_ACK=1 over 18 routine issuer messages (no STOP class). In-run guard at 2026-09-16T18:25:32.274376Z judged the printed plan: creates exactly the ten OG-i-2 resources, other_headers [], Plan: 10 to add, 0 to change, 0 to destroy. -- answered yes. Apply complete! Resources: 10 added, 0 changed, 0 destroyed. Record org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/evidence/og_i2/apply.json, log org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/evidence/og_i2/apply.log | CLOSED 20260916T182955Z |
| L3 | verify | source bucket opal-data-assets policy sha256 read immediately before and immediately after the apply are equal (no bucket policy change) | pre and post read times and sha256 | s3api get-bucket-policy opal-data-assets PRE 2026-09-16T18:22:49.351537Z sha256=9846f8dbffdf7ed02c3e4c3aa9825d39423d97209221c05b1b5c7ae642177528 len 1182 ;; POST 2026-09-16T18:25:36.032414Z sha256=9846f8dbffdf7ed02c3e4c3aa9825d39423d97209221c05b1b5c7ae642177528 ;; IDENTICAL. Evidence org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/evidence/og_i2/bucket_policy_pre.json and org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/evidence/og_i2/bucket_policy_post.json | CLOSED 20260916T182955Z |
| L4 | activation | the alias-key secret opal/mcp/opal-gateway-schwab-account-ref-key receives its FIRST value out-of-band in the OG-z-3 JSON shape, value never recorded | version id and read-back shape | og_i2_act.py put-alias-key 2026-09-16T18:2xZ: secretsmanager put-secret-value on opal/mcp/opal-gateway-schwab-account-ref-key, VersionId 8a580052-fd2d-480b-801c-355de8c08b4a stages AWSCURRENT; read-back SHAPE top_level_keys [current_version, keys], current_version v1, key_versions [v1], current key decodes to 32 bytes; value not recorded. Supplementary: app/account_ref.py parse_keyring accepted it. Record org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/evidence/og_i2/alias_key_put.json | CLOSED 20260916T182955Z |

## Log

- 20260916T181821Z OPENED by 0.9.0_WK_NFRA_OPLGTW~1 with 4 leg(s)
- 20260916T182955Z LEG L1 closed: commit 9efbe7a275 on branch wk-nfra_oplgtw-1-1c adds infra/aws/terraform/opal-gateway/schwab_reader_iam.tf together with
- 20260916T182955Z LEG L2 closed: bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply -no-color, ONE run, rc 0, start 2026-09-16T18:22
- 20260916T182955Z LEG L3 closed: s3api get-bucket-policy opal-data-assets PRE 2026-09-16T18:22:49.351537Z sha256=9846f8dbffdf7ed02c3e4c3aa9825d39423d9720
- 20260916T182955Z LEG L4 closed: og_i2_act.py put-alias-key 2026-09-16T18:2xZ: secretsmanager put-secret-value on opal/mcp/opal-gateway-schwab-account-re
- 20260916T182956Z CLOSED -- all 4 legs proven
