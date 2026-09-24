# Tax one-shot runner and exact remaining runtime boundary

CTOf0ce1b9198 accepts the bounded store d3a8c3e7e3. This candidate adds the narrow
callable data/assets/scripts/gold/investor_reporting/tax_membership_once.py, using the
original snapshot.acquire, S3BronzeStore, build_silver, S3SilverStore and membership
functions. Running the module directly is PLAN_ONLY: local SDK/naming inspection,
no credentialed SDK client, capability call, cloud write or scheduler.

## Executable boundary and evidence

After execution adjudication, the runtime owner supplies base_url and the route-only
capability_bearer to run_with_capability(base_url, capability_bearer, s3). Values are
never command-line arguments. The runner makes one acquisition attempt, preserving
capability refusal codes even when original S3BronzeStore's historical-list failure arm
raises NotImplementedError. It does not invent a last-good date or silently retry access.

Original Bronze bytes remain unchanged. Conditional source-store creates/replays are
checked against attempted bytes at exact returned/read VersionIds; Silver's original
typed body and original source SHA are retained. The complete census counts blank/total
rows as well as account slots. Canonical gateway used_rows includes one header, so
len(Silver rows)=used_rows-1. Missing/duplicate/non-contiguous row ordinals, inconsistent
account slots, incomplete lineage or unresolved business census stop before history.

Any history append failure raises RunRefused, carrying completed source receipts and
no complete-membership result. The entire snapshot can be replayed idempotently after
the cause is repaired. Final membership is resolved against one captured history read.
No Holdings/category publication occurs; observed_at remains the membership clock.

Executed locally: affected runner and canonical gateway/Silver cases,13 PASS1.03s,
17 unrelated Silver cases deselected. Includes original-byte/full typed census+replay;
partial history failure and recovery; incomplete/unresolved census refusal; explicit
nested compatibility; single-call capability failure; actual gateway projection into
Silver; six malformed shape/census cases. Injected transports only, no real capability.

## Canonical gateway/Silver mismatch repaired under57030ccdfa

Gateway infra/aws/ec2/opal-gateway/app/taxsma_workbook.py@6abf60e5d5 `_snapshot`
emits the seven projected business columns directly on each row. Silver
data/mdpf/scripts/silver/taxsma_workbook.py@bc5efb655d `_typed_row` instead requires
row['business'] to be a dictionary. Existing Silver unit fixtures manufactured the nested
shape and missed the seam. M notified CTO220539; CTO independently confirmed and granted
the exact Silver module/test repair57030ccdfa, consumed in this candidate.

The existing reader now consumes canonical flat projected columns without rewriting
Bronze or fabricating an alternate envelope. Scalar validation, row metadata and original
lineage remain; used_rows-1, account-slot count and contiguous ordinals are checked.
Fully nested rows remain an explicit compatibility shape. Mixing shapes across rows,
any dual flat/nested row (even apparently equal), missing columns and bad census refuse.
The positive check executes the original gateway's unchanged `_snapshot` and its pure
helper functions/constants extracted from its AST, then feeds those actual output bytes
to Silver. It isolates the projection from network/token configuration, not its row logic.
Membership's prior test envelope was also corrected to the actual flat/header-count shape.

## Concrete binding and destinations

Canonical capability is GET /ms/taxsma-workbook, no selectors. Gateway config.py defines
TAXSMA_WORKBOOK_BEARER as the separate route-only Secrets Manager-backed bearer and
TAXSMA_WORKBOOK_IDENTITY as validated Entra tid/oid. Andrew's designated account is
opalbloomberg@opalinvest.com; email is display/audit designation, not an authorization
comparison. Caller settings are TAXSMA_GATEWAY_BASE_URL and TAXSMA_CAPABILITY_BEARER
from the existing recipe. A generic ingestion credential is not a substitute.

The exact installed secret ARN/version, service environment binding and validated
tid/oid were NOT established by the inspected source; no value or new secret name is
invented here. Existing gateway/runtime owners via CTO must identify those protected
bindings and verify the deployed route before one real acquisition. This is a literal
runtime prerequisite, not a request for user credentials.

Local botocore1.43.0 service model supports PutObject IfMatch and IfNoneMatch. This is
not proof of the gateway/runner host's installed SDK; repeat PLAN_ONLY on that host.
Derived addresses from the original canonical functions:

- Bronze: s3://opal-data-assets/gateway/49financial/bronze/taxsma_workbook/date=YYYYMMDD/SNAPSHOT_ID-RESPONSE_SHA256.json
- Silver: s3://opal-data-assets/gateway/49financial/silver/taxsma_workbook/date=YYYY-MM-DD/SNAPSHOT_ID-RESPONSE_SHA256.parquet
- History: s3://opal-data-49financial/mdpf/49financial/state/taxsma_membership/dispositions.json

Uppercase tokens are explicit placeholders; actual source ID/hash/knowledge-date keys
are computed by the existing modules from the real response. They are not invented
physical destinations. Capture actual keys in the per-run receipts.

## Minimal execution/readback plan, not executed

1. Consume this pinned flat-row Silver repair and one-shot runner. Verify actual route
   bytes, protected identity/secret binding and SDK on host.
2. Runtime owner verifies versioning on both derived buckets, exact read/create access
   to original Bronze/Silver addresses and read/update to the sole history object:
   GetBucketVersioning; GetObject/GetObjectVersion; PutObject; exact existing KMS access
   if encryption requires it. No ListBucket, DeleteObject, policy change, scheduler,
   Graph-token export or broad directory permissions are required by this runner.
3. After the exact capability/cloud-write action is authorized, invoke once. Retain
   original response SHA, Bronze/Silver versions+hashes+lengths, full row census,
   canonical observed_at and final history version+hash. Independently read those
   versions and reconcile every supported account/date before a Holdings Tax join.
4. On any failure stop, retain originals and partial history, and report the failing
   stage. Do not delete or rewind append-only history; subsequent authorized replay
   repairs incompleteness. No success/publisher action follows a partial failure.

Cottonwood's accepted publication is unchanged; P owns reader runtime cutover. This
bounded 49F source preparation is not live Tax activation or three-firm completion.
