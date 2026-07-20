# Deploy-completion ledger: pm-vident-filter-500fix

- **Opened:** 2026-07-20T21:45Z by 0.0.0_AB_MSTR (Andrew-sovereign; LD-0328)
- **Scope:** opal-portfolio-excel-generator lambda -- held/targeted-only filter + oversubscribed 500->400.
- **Artifact sha (base64):** `US/Y7AqlL2LoKQaO1sQ/l2TzwtqDNNKblWIfRdgw1KE=`
- **TF:** portfolio-management (module.excel_generator), safe-apply.

## Legs
1. [x] Code committed `6efd24904` (lane-override) + source-map `5ea329f32` (CLOUD)
2. [x] Artifact uploaded to lambda-artifacts, content-sha256 read-back verified (`US/Y7AqlL2LoKQaO1sQ/l2TzwtqDNNKblWIfRdgw1KE=`, 9617 B)
3. [x] safe-apply portfolio-management -> Apply complete! 0 added, 1 changed, 0 destroyed (comp-tagauthz PASS)
4. [x] live CodeSha256 == artifact sha (State=Active, Successful, LastModified 21:59:43Z)
5. [x] tag portfolio-management-v2.4.0 + push --follow-tags

## Behavioral verification
Oversubscribed submit (120%) invoke -> statusCode **400** (was 500) with clean message
"Model target weights sum to 120.00% -- over the 100% cap. Reduce ... resubmit." Errors before any
S3/DDB write (no side effect). Filter validated vs Yang's live 503-sec autosave (94 kept / 409 dropped, sum=1).

## Status: CLOSED 2026-07-20T22:01Z (3/3 deploy legs + behavioral proof)
