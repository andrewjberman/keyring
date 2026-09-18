# Deploy Completion Record
**Date opened:** 2026-09-18T08:44:57.673210+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T091046Z
**Deploy:** IRPT_BCKEND IB-rtc-7: the 49 Financial source principal applied under sign-off (K1-K4 directory root create/update, K3 mdpf-pipeline targeted)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | aws_iam_role.irpt_49f_directory_read + aws_iam_role_policy.irpt_49f_directory_read (K1+K2, directory root) | TF apply 0 destroy + post-apply get-role/get-role-policy | TF apply directory root: 2 added, 1 changed, 0 destroyed. Role arn:aws:iam::313476888478:role/irpt-49f-directory-read-role created 2026-09-18T08:49:34Z, trust sha256 7ce5283bfd18ee5770df3de4d8fd4639ae611abf9b775abb21c86eb35b0b23c3, inline policy irpt-49f-directory-read-policy sha256 ab11263f5730a1a4b8b0b12c9cff209adbfeb290e501a853c71fe12648287c29 (5 GetObject prefixes + 1 conditioned ListBucket). Re-plan post-apply: No changes. | CLOSED 20260918T091021Z |
| L2 | activation | aws_iam_role_policy.mdpf_runner (K3, mdpf-pipeline root, TARGETED) | TF targeted apply 1 to change/0 add/0 destroy + post-apply get-role-policy sha256 | TF targeted apply -target=aws_iam_role_policy.mdpf_runner: 0 added, 1 changed, 0 destroyed. mdpf-runner-scoped now 33 statements (was 32), sha256(canon-json) aa94eeb6d0f89977958f66d14c6541fd32be91393e5183ec1aaee9cf45181f4a; new statement IrptDirectory49fAssumeSourcePrincipal sts:AssumeRole on role/irpt-49f-directory-read-role. Targeted plan immediately before apply read exactly 1 to change/0 add/0 destroy naming only aws_iam_role_policy.mdpf_runner. | CLOSED 20260918T091021Z |
| L3 | verify | negative control (N1-N5) + 49f third-directory fire + writer census unchanged | SSM transcripts + writer census output | Negative control (SSM c2b56e39/3b3313e5 on i-02448edb624a7a7cf, host by host, read-only): N1 opal-data-inf AccessDenied, N2 opal-data-assets/blackdiamond/cottonwood AccessDenied, N3 write opal-data-bd/investor-reporting/directory/zz-negative-control AccessDenied -- 3 of 3 DENIED; P1 positive opal-data-49financial/gold/advi/dimensions/dim_relationship READ-OK (sample keys + >=1000 KeyCount page) -- 1 of 1 READ-OK; assumed ARN name-check 0 of 4 denied prefixes matched. Third-directory fire: Lambda invoked twice (dispatch 2026-09-18T09:01Z SSM 6a856ec7/c25a3bdb/e0f6a54c, reconcile 2026-09-18T09:06Z) -- 49financial landed s3://opal-data-bd/investor-reporting/directory/2026-09-16/directory.json entries=4562 ETag fcdf90de75f24a591c1073489ad1b21f sha256 fd0beeca5fb4f785e2db9afeab0bc41e99e1d696368bec5bb8eb9f66e986c6f2 revision irpt-dir/49financial/2026-09-16/1.0 (pending->1.0, first mint); cottonwood landed entries=259 ETag 264e0fbedc24c09bd066ee9eb278ea5f revision .../1.0; inflection landed entries=291 ETag 782324f961078b228a32af9316af9836 revision .../1.0 -- 3 of 3 directories present. Writer census re-run post-apply (writer_census_ib_rtc_6.py): 12 of 263 writers, same membership as IB-rtc-6's 12 of 262 (denominator +1 is the new role itself, implicitDeny, not a writer) -- no STOP triggered. | CLOSED 20260918T091045Z |
| irpt-directory-refresh | tf-lambda | module.irpt_directory_refresh.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | Lambda irpt-directory-refresh rebuilt (K5 refresh.py + IB-rtc-3's dispatch-date fix, via rt6_package.py SHARED_ROOTS resolution): artifact sha256(b64) JkY/lBc2Wucz/XIPzyH0zmJt22ucItxjDehbKJko6i4=, uploaded to s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip (VersionId RcFJ9q4JcX2O4AsoqKLxaS8uKoZqbFEg), verified via head-object size=39227 + content-sha256 metadata match, registered in lambda-source-map.json, TF apply 0 added/1 changed/0 destroyed, served CodeSha256 JkY/lBc2Wucz/XIPzyH0zmJt22ucItxjDehbKJko6i4= confirmed live post-apply. | CLOSED 20260918T091022Z |

## Log

- 20260918T084457Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 4 leg(s)
- 20260918T091021Z LEG L1 closed: TF apply directory root: 2 added, 1 changed, 0 destroyed. Role arn:aws:iam::313476888478:role/irpt-49f-directory-read-ro
- 20260918T091021Z LEG L2 closed: TF targeted apply -target=aws_iam_role_policy.mdpf_runner: 0 added, 1 changed, 0 destroyed. mdpf-runner-scoped now 33 st
- 20260918T091022Z LEG irpt-directory-refresh closed: Lambda irpt-directory-refresh rebuilt (K5 refresh.py + IB-rtc-3's dispatch-date fix, via rt6_package.py SHARED_ROOTS res
- 20260918T091045Z LEG L3 closed: Negative control (SSM c2b56e39/3b3313e5 on i-02448edb624a7a7cf, host by host, read-only): N1 opal-data-inf AccessDenied,
- 20260918T091046Z CLOSED -- all 4 legs proven
