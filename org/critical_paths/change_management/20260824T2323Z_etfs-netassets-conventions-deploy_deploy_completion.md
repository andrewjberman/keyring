# Deploy Completion Record
**Date opened:** 2026-08-24T23:23:05.684736+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260824T232611Z
**Deploy:** ETFS_INGEST: deploy the TO-4 conventions layer to etfs-netassets-daily -- PENDING DEPLOY, not drift (conventions commit d7aa525fa9 @22:26:48Z is TWO HOURS AFTER the 20:31:09Z deploy). It is the PREREQUISITE for DS~Z's as-of fix: vendor_trueshares_Date and as_of_basis are 0 in the deployed bytes, so the fix would have been a no-op. CTO~Z ruling 5732 step (1).
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | rebuilt etfs-netassets-daily.zip -> lambda-artifacts | build write-verify size + content-sha256 | build-and-upload etfs-netassets etfs-netassets-daily -> SHA256 xosks8suawJqxyE0DW2yIHzso5tPPTwnQSa7h8Ua4OU=, write VERIFIED. Build gate clean (0 modified under infra/aws/lambda/); packaged file committed and tree==HEAD, so no uncommitted-code packaging. | CLOSED 20260824T232506Z |
| L2 | activation | terraform apply via safe-apply in infra/aws/terraform/etfs-netassets/ | apply output + new live CodeSha256 | safe-apply in infra/aws/terraform/etfs-netassets/. Plan 0 add / 1 change / 0 destroy (source_code_hash only). Apply complete: 0 added, 1 changed, 0 destroyed. Live CodeSha256 -> xosks8suawJqxyE0DW2yIHzso5tPPTwnQSa7h8Ua4OU=. | CLOSED 20260824T232507Z |
| L3 | verify | 0-diff re-plan rc=0 in the owning root | measured rc, no pipe | terraform plan -detailed-exitcode in the owning root -> rc=0, captured with NO pipe. | CLOSED 20260824T232507Z |
| L4 | verify | ACCEPTANCE ON THE DEPLOYED BYTES (CTO~Z step 3): vendor_trueshares_Date > 0 AND as_of_basis > 0 in the package, with a firing negative control | downloaded package census | ACCEPTANCE ON THE DEPLOYED BYTES per CTO~Z 5732 step (3). Downloaded pkg sha == live CodeSha256. vendor_trueshares_Date = 2 (was 0) and as_of_basis = 5 (was 0) IN THE PACKAGE; POSITIVE CONTROL fetch_trueshares_holdings = 3 proves the census discriminates; NEGATIVE CONTROL zzz_no_such_token_9999 = 0. Deployed member 1335 lines (was 1126) and RAW-MATCHES its HEAD blob. DS~Z's as-of fix now has the input it needs -- it would have been a no-op against the prior bytes. | CLOSED 20260824T232507Z |
| L5 | git | source-map artifact_sha256 + last_deployed_* for etfs-netassets-daily | commit, push-state stated | Source map three fields for etfs-netassets-daily: artifact_sha256=xosks8suawJqxyE0DW2yIHzso5tPPTwnQSa7h8Ua4OU= (== live CodeSha256 == downloaded package sha); last_deployed_commit=d7aa525fa9a5fd8511ccb8950fc978c54deee35e (the conventions commit, and the file's last-touching commit); last_deployed_at=2026-08-24T23:24:00Z (from the API's own +0000 string). Diff 3 insertions / 3 deletions, CRLF 0, 201 functions. Round-trip proven lossless before writing; record-terraform-deploy deliberately NOT used (measured CRLF-rewrite defect on this box, already fixed-forward once tonight). LANDED LOCAL, rides integration. | CLOSED 20260824T232611Z |

## Log

- 20260824T232305Z OPENED by 0.7.0_AE_CloudOps~Z with 5 leg(s)
- 20260824T232506Z LEG L1 closed: build-and-upload etfs-netassets etfs-netassets-daily -> SHA256 xosks8suawJqxyE0DW2yIHzso5tPPTwnQSa7h8Ua4OU=, write VERIF
- 20260824T232507Z LEG L2 closed: safe-apply in infra/aws/terraform/etfs-netassets/. Plan 0 add / 1 change / 0 destroy (source_code_hash only). Apply comp
- 20260824T232507Z LEG L3 closed: terraform plan -detailed-exitcode in the owning root -> rc=0, captured with NO pipe.
- 20260824T232507Z LEG L4 closed: ACCEPTANCE ON THE DEPLOYED BYTES per CTO~Z 5732 step (3). Downloaded pkg sha == live CodeSha256. vendor_trueshares_Date 
- 20260824T232611Z LEG L5 closed: Source map three fields for etfs-netassets-daily: artifact_sha256=xosks8suawJqxyE0DW2yIHzso5tPPTwnQSa7h8Ua4OU= (== live 
- 20260824T232611Z CLOSED -- all 5 legs proven
