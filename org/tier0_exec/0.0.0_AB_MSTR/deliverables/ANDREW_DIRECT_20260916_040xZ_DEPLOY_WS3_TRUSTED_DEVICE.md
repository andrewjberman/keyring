# ANDREW-DIRECT 2026-09-16 ~04:0xZ -- "deploy it" (D12 WS-3 trusted-device build, `6328a6fbb2`)

**Channel:** Andrew, directly, at the `0.0.0_AB_MSTR` terminal (laptop).
**Received by:** `0.0.0_AB_MSTR`.
**In reply to:** this seat's report that WS-3 was built, committed and pushed at `6328a6fbb2` with the
deploy held for his word.

## His word, VERBATIM AND ENTIRE

> deploy it

## What it authorizes

The deploy of the auth-handler Lambda carrying `6328a6fbb2` to production: build the artefact
(`build-nodejs-lambda.sh portal-auth opalinvest-auth-handler`), upload to S3, `safe-apply` on
`infra/aws/terraform/portal-auth`, verify the deployed bytes, record the deploy. Served surface: the
production login path (`opalinvest-auth-handler`, one function, one consumer).

## What this seat does with it

- Opens a change-management entry BEFORE the first act and closes it at completion (NEVER-2).
- Pins the rollback target FIRST: the current Lambda `CodeSha256` and the current S3 object version, so
  a rollback is a re-point, not a rebuild.
- Baselines `terraform plan` before the build so the post-build diff is attributable to this change only.
- Uses `safe-apply`, never bare `terraform apply`; never `aws lambda update-function-code`.
- Verifies the DEPLOYED bytes (the function's `CodeSha256` against the artefact's), not the tool's rc.
- Exercises what can be exercised without his account: the fail-closed paths on the live API. The
  positive path (MFA -> cookie -> password-only login) is HIS to exercise on his own account; this seat
  tells him exactly what to do and reads the `device_trust_minted` / `device_trust_skipped_mfa` log
  events to confirm it fired.
