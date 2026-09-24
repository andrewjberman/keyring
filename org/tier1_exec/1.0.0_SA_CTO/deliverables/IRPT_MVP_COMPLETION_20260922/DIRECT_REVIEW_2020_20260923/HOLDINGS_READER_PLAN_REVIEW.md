# CTO exact Holdings reader cutover disposition

Bounded GO to P for the saved plan reviewed below, under Andrew's existing IRPT
implementation/runtime authority and CTO delegated worker adjudication. No new
scope is inferred from the handoff notification.

Plan: C:/Users/AndrewBerman/Desktop/irpt-smoke-p-backend-20260923/.runtime/holdings-reader-cutover/holdings.tfplan
SHA256: ca2a907770c081a244cb1eddc854db95cdb80523655989093264c9e20f905301
CTO read the actual binary with Terraform1.9.8 from its initialized Holdings root.
One create, three updates, zero deletes: role description, replacement reader
policy, new retained-selection read policy, and function package/environment.

Read grants are bounded to canonical three-firm current holdings indexes and
versioned dated Platinum objects, existing exact directory/ownership scopes, and
GetItem on irpt-requests restricted by tenant leading keys. KMS Decrypt is limited
to the existing key via DynamoDB with the irpt-requests encryption context.
No S3 write, list, Gold/source access, vendor, route, schedule or table mutation
permission. Four actual COT publication versions independently HEAD as AES256;
this reader needs no additional S3 KMS permission for this first thread.

Handler entry.lambda_handler, Python3.12/x86_64, role, common layer5, 1024MB and29s
are unchanged. Contract/registry locations move to packaged /var/task members;
IRPT_REQUESTS_TABLE is irpt-requests. Full measured changes are in the JSON sibling.

Artifact independently GET from exact S3 version and hashed:
- bucket opal-313476888478-lambda-artifacts
- key investor-reporting/irpt-holdings.zip
- version e7XAGneq1_KKe2tnBVK45FsEFNItS2NF
- SHA256 bcb3fb71937ad4958e3a68821a60a39ce338df6f7a8bca83b7584bd5913cc94b
- CodeSha256 vLP7cZN61JWOOmiCGmCjnOM43296i8qDt1hL1ZE8yUs=
- 261038 bytes,33 members; includes entry, selection store, accepted publication,
  schema, registry and naming dependencies. Current S3 version matched at review.

CTO cold-imported this exact extracted artifact outside the repo with Python -I,
read actual COT accepted fe328 publication for account acc_d486fc9455d6b2aa18e13af1
and September22, and asserted schema validity, reconciliation, distinct clocks,
revision and59 nodes (57 securities). This uses reviewer AWS credentials, not the
execution role or authenticated Entry. It is not browser/live-product completion.

## Execution bounds

P runs canonical safe-apply of only this saved plan after verifying its SHA again.
The existing module depends_on defers artifact data lookup: source_code_hash and
s3_object_version are unknown in the plan. This limitation is accepted only with
exact current-object VersionId and content-sha256 preflight matching the above,
no intervening artifact upload by P, and immediate deployed CodeSha256/config/IAM
readback matching this reviewed candidate. Any mismatch stops success/closure;
route the exact drift to CTO, do not accept or replan a different artifact.

Preserve prior code version QHzwDQDRggw06hA4MAwmGgR0NVmGVH5F and saved before-state
for rollback planning if runtime fails. Do not invent successful authenticated
proof or invoke with fabricated authorizer claims. Keep ledger8600 open until
its apply/readback legs are evidenced, then route the exact live reader to M for
real selection/API/screen/reload. M owns Holdings end-to-end proof. All three
products remain incomplete. No additional provider call or publication authorized.
