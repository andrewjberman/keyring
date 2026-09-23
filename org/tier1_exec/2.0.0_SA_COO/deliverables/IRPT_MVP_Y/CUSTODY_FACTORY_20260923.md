# Local custody request factory handoff

Owner `2.0.0_SA_COO~Y`; authority CONTRACT.md and CTO custody/source rulings.
LOCAL source `819c9e399086cffb2876a21fbc2cee01724b0bd7` in
`C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922`; shared scalar reader
`48946e7972` consumed by merge `c04607fdfd`. No cloud/vendor/release act.

## Installed local contract

`ycharts/generate/custody_submission.py::build_custody_entry(**ports)` returns
the existing guarded Entry with a `CustodySubmissionFactory` installed as its
submission service. Wrap with `served.lambda_entry(boundary)` for the HTTP
handler. This does not alter legacy `entry.ENTRY`, which remains unconfigured.
The request preparer is the HTTP POST analysis boundary, distinct from the
queue worker. P owns final route/function/role/IaC placement; do not grant the
vendor worker profile reads merely because its old function name is similar.

Required configuration:

- `dynamodb`: actual boto3 DynamoDB client; canonical profile readers and
  `DynamoAcceptance` use it. Existing request/job table defaults are
  `irpt-requests` and `irpt-jobs`.
- `table`, `s3`: actual reporting index resource and S3 client for P retained
  repositories. `reporting_policy`, `reporting_destination`: canonical current
  accessors; no destination or ACTIVE-policy fallback.
- `authorize_snapshot(principal, owner) -> True`: current accepted exact
  custody snapshot/account verifier, mandatory.
- `load_normalized(browser, principal, owner)`: accepted frozen custody
  portfolio `{input_id, content_sha256, document}`. Mandatory producer callback;
  current actual holdings projection/security/value/revision adapter is OPEN.
  M151228 is tracing source contract; no fixture becomes a default producer.
- `schema_directory`: explicit packaged published schema directory;
  `ingestion_revision`, `destination_revision`, `queue_url`, `send`, `clock`.
- `configuration(owner, browser)`: defaults to actual recorded
  `capture_configuration`; flat packaging must bind explicit templates/settings
  paths because the repository default settings path points to intake/settings.
- Optional `comparison_resolver(browser, principal, owner, input_ref,
  authorize_input)`: maintained comparison catalogue plus source_descriptors.
  Requests with nonempty comparison_keys refuse without it. This does not
  silently reduce the completion requirement for Comparison/Multi-Comp.

Verified selected_tenant stays query intent at shared Entry. `account_set_id`
is required query intent; conflicting/duplicate raw or multivalue references
refuse. Browser body remains closed. Each request constructs fresh CustodyAccess,
current-authorized artifact repositories and SubmissionService. Normalized input
owner/source/snapshot/accounts are validated before persistence. Profile reads
use actual `get_user` and `get_organization`; retained-input authorization checks
exact bytes/reference under current custody before/after those reads. Replay
looks up durable acceptance before any input/profile/configuration recapture.
No request-local identity or access object is stored in the warm factory.

## Package and role obligations

`CUSTODY_FACTORY_MODULES_20260923.json` lists the exact 29 production source
modules with flat basename aliases, Git blobs and SHA256. AST closure includes
lazy imports; no basename collision was found in declared package roots.
`comp-pydeps deps ...` returned `None` with no edges, so it is not closure proof.
P must test its extracted artifact import and installed factory independently.
Additional concrete producer callbacks can add dependencies beyond this list.

Third-party packages: boto3/botocore, jsonschema, referencing and their normal
dependencies. Data includes all published v1 schema JSON files, templates.json,
intake/settings.json via explicit packaged configuration, raw_keys.json,
firm_registry.json and declared projection seam data where required. Existing
route table constants bind this HTTP Entry; no new public route is requested.

Profile preparer permissions are P's narrow installation obligation: existing
active-user email-index Query and strongly consistent PROFILE GetItem; adopted
organization GetItem at FIRM#opal-capital/CONFIG#defaults, exact eight attributes.
LeadingKeys alone cannot restrict SK. Snapshot/directory/selection/reporting
storage and request/job transaction/outbox permissions need the exact chosen
preparer role. Nothing here adds or applies IAM. No vendor call is reachable
from this factory; queue delivery remains an injected acceptance outbox effect.

## Evidence and open boundaries

`test_custody_retained.py`: 30 PASS, including actual guarded installed factory,
both canonical SDK readers via Stubber, immutable acceptance serializers,
replay without recapture and current-snapshot revocation. The earlier 20 cases
also cover retained worker recipe inputs and revocation during blob reads.
Full generate/intake: 265 PASS, 50 subtests. Separately: scope148 PASS57subtests,
custody/schema60 PASS. Ordinary source commit gate2/2 passed.

AWS storage/current snapshots/normalized producer data are synthetic, retention
policy is synthetic ACTIVE, worker lease is pre-acquired and dispatch lease is
unavailable in the storage double. No queue delivery, actual retained-history
listing, live custody publication, browser, vendor, deployed or E2E PASS.

The concrete reader initially failed6/14 at02501a68ec because nested metadata
violated the scalar schema. P repaired producer48946 without weakening schema.
Literal old-driver rerun:10 PASS10setupErrors at obsolete metadata assertion.
`ORGANIZATION_SCALAR_ASSERTION_ONLY.patch` changes precisely that one assertion
to check all eight scalar fields/values; original/adapted driver hashes and
separate20PASS rerun are in ORGANIZATION_SCALAR_RETEST.json. The factory commit
preceded reading CTO151141 and also refactored test setup; the separate patch
and original-driver rerun let CVO verify equivalence without inheriting that
refactor. Original failing source/history is preserved; no history rewrite.

Next: M/Y accepted custody snapshot-normalization binding; P extracted package
and actual configured preparer assembly; CVO Y same-pin independent consumer
review, CVO M source review. These remain explicit dependencies, not fulfilled
by the offline local installation. All source/evidence LOCAL; last observed
origin CLOUD `365ab567ba1250a6a3569df38cb75d12fe2e8d0e`.
