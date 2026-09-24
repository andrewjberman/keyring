# First-hop paired runtime review

Prepared under d2fd024d72, qualified by controlling access correction 5ad99c7d30. No cloud apply, artifact upload, remote push or promotion occurred. This is one directory function, not the parked generation package chain.

## Frontend actually served

The clean localhost5174 tree is now `10141b6d0bbb007d5dd9e758f11f785216e11339`. Canonical safe-merge integrated only 09d5d5ea, f0e7e362 and 910ebf36 in order. Its entire src tree equals 910ebf36, while `scripts/dev-live.mjs` equals the prior 3b15871b launcher/diagnostics. HTTP readback of the served module returns 200 and includes the new Global context and Select Firm code.

Actual-tree typecheck passes; 26 context/parser tests, 36 assertions, zero failures; existing mounted Global/partner/identity/partial, header-race and browse-race scripts pass. These use controlled identity/transport and are not live scope acceptance. The running backend is unchanged; no further sign-in prompt was sent.

## Exact candidate and proof

Local artifact `.runtime/directory-review/irpt-directory-search.zip`, 155747 bytes, 20 members. SHA256 `a39f74ba1e688ac0ad1cf2b3a2b18c27f93d5493dc82d2d283848a7dee0a618b`; Lambda base64 `o590uh5oisCtHPKzorGMJ/k9VJPcgtLSg4SKfe4KYYs=`. Full member-to-Git-blob/pin/length/hash manifest and proof receipts are in DIRECTORY_RUNTIME_REVIEW_20260923.json.

Every member comes from immutable Git bytes using source map 6cd8adb582. This is exactly the previously reported six changed/added members plus 14 unchanged members. Both later owner-read imports are included. ZIP construction uses the same .NET sorted-member/fixed-2020-timestamp/Optimal compression construction as canonical build-and-upload.sh:481-508. The canonical upload command has no dry-run mode, so it was not executed. Future canonical upload must independently reproduce this exact hash or return for review.

Extracted ZIP mounted read-only at /var/task in pinned Lambda Python3.12 x86_64 image `sha256:5f188ce6104ab76d1a9a44b9b53fd0d72ea5ccec94eb4cbccf5c9b0ef485f9f8`, network disabled, no credentials, read-only filesystem. Actual entry.lambda_handler cold call passes before any test dependencies or mocks are installed on sys.path. owner_reads and custody import from /var/task. SDK is runtime boto3/botocore1.42.97; live function has no layers. Matching runtime family/architecture is established; byte-identical managed AWS runtime patch is not claimed.

41 unchanged directory/bootstrap/selection/Global controls pass against the extracted runtime. Original Git test bytes are preserved; the layout adapter creates only an entry.py symlink to /var/task. A separate actual lambda_handler Global positive uses synthetic external artifact ports. Module-origin assertions pass. Tests use separately mounted pytest/jsonschema dependencies; none are put in the runtime ZIP. Executed preparation/probe scripts are extracted from committed 1cb76a2c9b/e9b3af590f and their SHA256 recorded.

**Policy qualification:** one legacy Global non-resolve negative contradicts 5ad99c7d30; a mechanical pass is not a full-access-policy PASS. New viewer interface 9a3ec2a11f is separately published to M/Y and not yet Entry-wired or in this ZIP. CTO must adjudicate bootstrap-only staging separately from the full Opal implementation; do not represent this artifact as the completed permission correction.

## Existing runtime equality and preconditions

Measured existing function: entry.lambda_handler, python3.12, x86_64,512MB,15seconds, no layers, role irpt-directory-role. Configuration/environment fingerprint, resource policy, complete role documents and all four routes are retained in the JSON. All routes have CUSTOM authorizer naqxlm and integration g9302sp, AWS_PROXY payload2.0. No route, role, policy, environment, handler, timeout, memory, layer or schedule change is proposed for this bootstrap candidate.

Current function RevisionId `8851109e-7f1f-4915-ae2b-0dff01d276c5`; old code `iqLKa1RWk9hlcSlAheuoAMgIY4R3VrStPX1eG5Qwq/s=`. Re-read both and the configuration fingerprint immediately before any later authorized mutation. Any drift invalidates this plan. Terraform has no atomic Lambda RevisionId argument in this route; retain exclusive deployment ownership and stop on a changed precondition rather than switching to a direct code update.

Provisioned Terraform1.9.8 read-only targeted baseline plan is zero-change, SHA256 `a5d79356e789a9296443bbce067ca8f51ddc3699dbc3bf3f16434579bbf91527`. This checks current configuration against the OLD S3 artifact; it must not be applied as a candidate deployment plan.

Rollback is independently downloaded from `s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-search.zip`, immutable version `RXChd66RsDjV1jhG1ZsFlOGnXeIDxApp`, 149956 bytes. It hashes exactly to current live code. Local copy `.runtime/directory-review/rollback.zip`. Retain its version; rollback must follow a newly reviewed canonical target plan, not a direct update-function-code call.

## Exact later route, gated and not executed

1. CTO adjudicates this candidate's policy qualification and permits the concrete staging boundary. Open the canonical deployment/change ledger before mutation, and recheck exact source/member hashes, current RevisionId/code/config/role/routes.
2. Canonical single-function command: `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-directory-search`. Verify uploaded immutable S3 version and downloaded bytes equal the reviewed ZIP; source-map diff must touch only directory artifact facts. A rebuilt hash difference requires review.
3. Use the provisioned `.tools/terraform.exe`, directory root `infra/aws/terraform/investor-reporting/directory`, `plan -input=false -target=module.irpt_directory_search.aws_lambda_function.this -out=<new exact saved plan>`. Grade its JSON: only that existing function's S3 version/source_code_hash may change; zero IAM/routes/env/layers/schedules/create/destroy. Submit exact saved-plan hash for apply adjudication. The old zero-diff plan is not this plan.
4. On exact apply authority only: `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/directory apply <reviewed saved plan>`. No direct Lambda update. Wait for Active/Successful, read code hash, repeat configuration/role/route equality, run target zero-diff plan.
5. Canonical recorder route: `bash infra/aws/lambda/ci/record-terraform-deploy.sh investor-reporting --function irpt-directory-search --deploy-ledger <ledger commit> --code-sha256 <measured live base64> --author "2.0.0_SA_COO~P <2.0.0_SA_COO~P@opal.agent>"`. Require unrelated source-map rows unchanged and exact scoped reconcile. The earlier incident recorded a wrapper scope defect under 1c686165e1; that historical exception is not fresh permission. If the current wrapper fails or widens scope, stop and return the concrete defect to CTO, without bypass.
6. Close the ledger only with actual artifact readback, targeted zero-diff and scoped recording. CLOUD push remains separately held. After the paired backend is actually served, repeat Andrew's normal authenticated scope/list/pagination/selection/reload journey and record its real result. No offline count closes S1-S7.
