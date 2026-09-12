# Deploy Completion Record
**Date opened:** 2026-09-12T08:21:53.139969+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260912T083119Z
**Deploy:** IRPT_BCKEND IB-rt-6: wire the directory refresh build dispatch (SSM) and its least-privilege IAM
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | source committed on wk-irpt_bckend-2-2c (refresh.py + schedule.tf + tests) | commit hash | d2bffb95c0 on wk-irpt_bckend-2-2c (refresh.py + schedule.tf + tests); git status --porcelain over the five packaged members reads 0 lines, so the built zip IS the committed bytes | CLOSED 20260912T082524Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-directory-refresh.zip | VersionId + content-sha256 metadata equal to the built zip | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip VersionId JhB3XBnfTE24RijwEzFfpmt8ybmLXa2a, 35535 bytes, metadata content-sha256=2NK1XSoSPjdUkkowxaKh3m4inKKboR7ps2EUVqdUEBU= EQUAL to the locally built zip's sha256 (head-object read, recomputed from the file) | CLOSED 20260912T082524Z |
| L3 | activation | terraform apply of the directory root: function env + IAM policy + schedule input | safe-apply rc=0 and the applied resource ids | safe-apply.sh rc=0: 'Apply complete! Resources: 0 added, 3 changed, 0 destroyed.' -- aws_iam_role_policy.irpt_directory_refresh, module.irpt_directory_refresh.aws_lambda_function.this, aws_scheduler_schedule.irpt_directory_refresh; tombstone-gate CLEAN; the saved plan read 0 to add, 3 to change, 0 to destroy with no destroy line | CLOSED 20260912T083119Z |
| L4 | verify | served CodeSha256 == built sha256 AND the role carries the four dispatch statements AND post-apply plan No changes | three-way hash equality + get-role-policy + plan output | THREE-WAY HASH EQUALITY: built zip sha256(b64)=2NK1XSoSPjdUkkowxaKh3m4inKKboR7ps2EUVqdUEBU= == S3 metadata content-sha256 == live CodeSha256 (get-function-configuration), LastUpdateStatus Successful, Timeout 60 UNCHANGED. ROLE: get-role-policy irpt-directory-refresh-role reads 6 statements, the four dispatch ones present -- SendCommand on the ONE instance + AWS-RunShellScript, StartInstances on the ONE instance, and the three read-only no-resource-type actions on *. POST-APPLY PLAN: 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260912T083119Z |

## Log

- 20260912T082153Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 4 leg(s)
- 20260912T082524Z LEG L1 closed: d2bffb95c0 on wk-irpt_bckend-2-2c (refresh.py + schedule.tf + tests); git status --porcelain over the five packaged memb
- 20260912T082524Z LEG L2 closed: s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip VersionId JhB3XBnfTE24RijwEzFfpmt8
- 20260912T083119Z LEG L3 closed: safe-apply.sh rc=0: 'Apply complete! Resources: 0 added, 3 changed, 0 destroyed.' -- aws_iam_role_policy.irpt_directory_
- 20260912T083119Z LEG L4 closed: THREE-WAY HASH EQUALITY: built zip sha256(b64)=2NK1XSoSPjdUkkowxaKh3m4inKKboR7ps2EUVqdUEBU= == S3 metadata content-sha25
- 20260912T083119Z CLOSED -- all 4 legs proven
