# Deploy Completion Record
**Date opened:** 2026-08-30T03:36:44.379074+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260830T040143Z
**Deploy:** M-2: deploy the schwab silver converter carrying the completeness-marker emit + OPAL_BUILD_COMMIT pin
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M-1 | verify | targeted plan is the gate-ruled shape | 2 rows on module.silver_converter[schwab] (code + env), 0 rows on the other five families, 0 destroy | The gate-ruled shape exactly (1.0.0_SA_CTO 85118, 2.0.0_SA_COO 85121). Targeted at module.silver_converter -- ALL SIX instances, so the other five had every chance to appear: Plan 0 to add / 1 to change / 0 to destroy; ONE resource module.silver_converter[schwab].aws_lambda_function.this; complete changed-attribute set = last_modified (known after apply), s3_object_version wsAFSuqnzXP2im2OD3GcXxvvP7gthVW5 -> RigDVPxrZlvI49kyJJrOMk4vXnxEACzs, source_code_hash yMma9jOm8wEdadz1ah3fnsdsNG50/T9u638QWJ7NkDo= -> /Uog2LDpLg42FrCU5MfTrEBaTFJTlVRY97tONxmjhVM=, and environment + OPAL_BUILD_COMMIT = 5c7b2a9a6b. eclipse/orion/blackdiamond/etf/smartx produced ZERO rows -- the sparse per-family map working, proven on the target that covers them. SELF-CORRECTION ON MY OWN EVIDENCE: my first FILTERED read of this plan did not show s3_object_version and I nearly reported the code row as source_code_hash alone; it was a grep spacing miss, not an absent attribute (unfiltered, it is line 48). A filtered view that silently drops a row is how a plan shape gets mis-stated to a gate. | CLOSED 20260830T033953Z |
| M-2v | verify | deployed artifact identity after the apply | get-function-configuration CodeSha256 == the uploaded zip sha /Uog2LDpLg42FrCU5MfTrEBaTFJTlVRY97tONxmjhVM=, LastModified post-dating the apply, live OPAL_BUILD_COMMIT == 5c7b2a9a6b read from the LIVE env | PASSES on the LIVE primitive, not the apply report. get-function-configuration: CodeSha256 /Uog2LDpLg42FrCU5MfTrEBaTFJTlVRY97tONxmjhVM= == the uploaded zip's sha EXACTLY; CHANGED from the prior yMma9jOm8wEdadz1ah3fnsdsNG50/T9u638QWJ7NkDo=; LastModified 2026-08-30T03:37:41Z, against a prior of 2026-07-15T18:40:47Z -- the live converter had been running pre-M-2 bytes since 15 July, so 0.4.0_DS_ClientPlatform~V's marker emit reaches production on THIS apply (the deploy limb 84215 named as open). State Active / LastUpdateStatus Successful. LIVE ENV read rather than assumed: OPAL_BUILD_COMMIT = '5c7b2a9a6b' PRESENT and correct, FAMILY = 'schwab', full key set {DLQ_URL, FAMILY, MONOLITH_BUCKET, OPAL_BUILD_COMMIT} -- so declared_source now renders 'schwab_schemas.SPECS @ 5c7b2a9a6b' instead of '@ UNPINNED'. | CLOSED 20260830T033953Z |
| M-3v | verify | post-apply targeted re-plan 0-diff | No changes. Your infrastructure matches the configuration. | Post-apply targeted re-plan, same 1.9.8 shim, same -target: 'No changes. Your infrastructure matches the configuration.' = 0-diff. | CLOSED 20260830T033953Z |
| M-4v | git | CLOUD commit of the source-map artifact fields + this ledger | commit hash + push state MEASURED by ls-remote; includes the repair of an MSYS-mangled artifact_sha256 | Commit e14b66fa80 -- lambda-source-map.json artifact fields for opal-assets-silver-schwab, this ledger and its sentinel. Authored via .tools/safe-commit.sh -F with the message file written by the Write tool (non-shell writer, Rule 14a); msg-verify MATCH len=4654. The commit ALSO carries the repair of the MSYS-mangled artifact_sha256 that ci/build-and-upload.sh wrote (C:/Program Files/Git/Uog2... -> /Uog2...), with the 162-function census and the 0-of-162 re-census in the message. PUSH STATE MEASURED at 2026-08-30T04:01:16Z: git ls-remote origin refs/heads/CLOUD = 5a0e1df70b2eb190b5a972d284dd32af3663118a; e14b66fa80 reads LOCAL by merge-base --is-ancestor. Publication of a LOCAL commit is 0.0.0_AB_MSTR's integration window, not this seat's push. | CLOSED 20260830T040116Z |
| opal-assets-silver-schwab | tf-lambda | module.silver_converter["schwab"].aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | module.silver_converter[schwab].aws_lambda_function.this applied via .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply m2-schwab.tfplan on the 1.9.8 shim, rc=0, 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Verified by live get-function-configuration (M-2v), not by the apply's own output. 0-diff re-plan at M-3v. | CLOSED 20260830T033954Z |

## Log

- 20260830T033644Z OPENED by 0.7.0_AE_CloudOps with 5 leg(s)
- 20260830T033953Z LEG M-1 closed: The gate-ruled shape exactly (1.0.0_SA_CTO 85118, 2.0.0_SA_COO 85121). Targeted at module.silver_converter -- ALL SIX in
- 20260830T033953Z LEG M-2v closed: PASSES on the LIVE primitive, not the apply report. get-function-configuration: CodeSha256 /Uog2LDpLg42FrCU5MfTrEBaTFJTl
- 20260830T033953Z LEG M-3v closed: Post-apply targeted re-plan, same 1.9.8 shim, same -target: 'No changes. Your infrastructure matches the configuration.'
- 20260830T033954Z LEG opal-assets-silver-schwab closed: module.silver_converter[schwab].aws_lambda_function.this applied via .tools/safe-apply.sh -chdir=infra/aws/terraform/opa
- 20260830T040116Z LEG M-4v closed: Commit e14b66fa80 -- lambda-source-map.json artifact fields for opal-assets-silver-schwab, this ledger and its sentinel.
- 20260830T040143Z CLOSED -- all 5 legs proven
