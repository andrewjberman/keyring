# IRPT reporting storage, retention and permission plan

Owner: 2.0.0_SA_COO~P. Authority: completion CONTRACT v1.2 and CTO ruling
IRPT-S7-01 at bcd38bba00. Status: concrete implementation proposal, not provisioned.
M owns canonical registry/builder; P owns composition and enforcement. No existing
object is moved or deleted by this plan. No writable destination until canonical
exception record, agreed policy revision and enforcement are present.

## Finite retention policy for adjudication

Proposed policy ID `irpt-retention-v1`. Values below are proposed product retention
settings for CTO adjudication; they are not an assertion of an existing approved
retention policy. Every accepted object has immutable server-issued `created_at`
and finite `expires_at` in an indexed retention record. No browser supplies them.

| Registered family | Unreferenced lifetime | Accepted retention ceiling |
|---|---|---|
| ORIGINAL_CSV | 30 days from upload | 2555 days from original upload |
| NORMALIZED_PORTFOLIO | 30 days from normalization | 2555 days from creation |
| REQUEST_COMPOSITION | 30 days from acceptance | 2555 days from acceptance |
| ORIGINAL_VENDOR_PDF | 30 days from retrieval | 2555 days from retrieval |
| EXTRACTION_EVIDENCE | 30 days from extraction | 2555 days from extraction |
| PERFORMANCE | Publication only after full validation | 2555 days from publication |
| ANALYSIS | Publication only after Y certification | 2555 days from publication |
| EXPORT_BUNDLE | 7 days if no published export | Earlier of 2555 days or report/dependency expiry |
| EXPORT_PDF | 7 days if receipt publication fails | Same expiry as accepted bundle |
| EXPORT_RECEIPT | Published with exact PDF version | Same expiry as accepted bundle |
| SELECTED_ACCOUNTS | 30 days from selection creation | 30 days; reports freeze members/revisions independently |

An accepted report's expiry is the minimum of its own ceiling and every required
input/source-evidence expiry. Reusing old input cannot make a new report outlive
that input. A request whose dependencies cannot cover the intended retention is
refused before READY; fresh input/evidence is required. Selection-reference expiry
does not erase report ownership because the repository retains exact members and
selection revisions in the accepted record.

Promotion of an unreferenced artifact into an accepted dependency uses a conditional
retention record before report publication. It cannot exceed that artifact's fixed
creation-based ceiling. No infinite renewal and no accidental blanket bucket TTL.
Ordinary reads/reopening/downloads refuse expired records. A finite investigative
hold, if later authorized, is a separate audited policy revision with its own end
date; none is created by this plan.

Physical expiration is separate from authorization expiry. No automatic S3 or
Dynamo deletion is enabled in this implementation phase. Before cleanup is allowed,
a reference-aware expiry worker must prove the entire expired dependency graph is
unreferenced, retain an audit tombstone, and delete exact S3 VersionIds, not a current
key chosen by listing. No blanket NoncurrentVersionExpiration can remove accepted
versions. The cleanup operation requires its own approved run and role. This is
bounded expiry plus protected preservation while cleanup is unimplemented, not a
grant of indefinite retention or a promise that lifecycle is already active.

## Proposed role and action matrix

All S3 resources are derived by M's registered family-to-key policy for each enabled
long-form client firm. No raw bucket override, wildcard product bucket grant, public
access or browser-address input. Immutable writes require conditional creation;
reads pin VersionId and verify SHA256. Versioning and SSE-KMS are mandatory.

| Consumer | Read families / tables | Write families / tables |
|---|---|---|
| directory selector | current directory/ownership; requests selection rows | requests `SELECTION#` conditional PutItem |
| performance entry | directory/ownership; requests GetItem selection/report; report history Query | PERFORMANCE and owned request/source evidence; requests conditional report index |
| holdings entry | existing custody inputs; requests GetItem selection | none added by P |
| intake | own ORIGINAL_CSV and NORMALIZED_PORTFOLIO | ORIGINAL_CSV/NORMALIZED_PORTFOLIO and owned artifact index |
| analysis request | owned input and selection; requests/jobs/outbox as Y specifies | REQUEST_COMPOSITION and Y conditional acceptance/outbox rows |
| generation/extraction | frozen owned input/composition/vendor PDF | ORIGINAL_VENDOR_PDF, EXTRACTION_EVIDENCE, ANALYSIS; Y conditional job state |
| report reader/history | PERFORMANCE/ANALYSIS; requests index GetItem/Query | none |
| export controller | pinned report/evidence/approved assets | EXPORT_BUNDLE, EXPORT_RECEIPT; conditional export process rows |
| renderer publication | pinned EXPORT_BUNDLE and approved print assets | EXPORT_PDF only |
| download | exact authorized EXPORT_PDF version and receipt | none |

For S3: writers receive PutObject only on their enumerated family prefixes, readers
GetObjectVersion plus the bounded GetObject needed for conditional-write conflict
HeadObject. No ListBucket/DeleteObject/DeleteObjectVersion/PutBucketPolicy or wildcard
SecretsManager grant. Customer-key access is restricted to the exact key and service,
with encryption-context conditions matching the bucket or request table. Cross-firm
runtime checks remain mandatory even where one shared Lambda is configured for all
three enumerated firms; a role's firm list is not an end-user authorization grant.

For DynamoDB: existing requests/jobs/outbox tables are reused by name from core
outputs, not duplicated. Each role gets its actual GetItem/PutItem/UpdateItem/Query
operations; no Scan or DeleteItem. LeadingKeys enumerates canonical firms. IAM does
not express every sort-key ownership distinction, so conditional state transitions
and current principal checks remain mandatory and independently tested.

## Concrete composition work and release checks

1. M supplies canonical exception ID, policy revision, family metadata and destination
   adapter. P packages the same reader/writer revision together; pending/unknown policy
   fails closed. Existing Gold/Platinum custody destinations remain M's canonical homes.
2. P adds a versioned, private reporting bucket through core Terraform, system key,
   public-access block, TLS-only policy and default encryption. Object expiry metadata
   and runtime checks precede writes; no lifecycle deletion or provisioning is implied.
3. Each actual producer/reader above receives its bounded grants and configuration.
   First candidate performance selection env/GetItem/decrypt declarations are at
   f7f5d22a76. Terraform syntax gate passed; remote plan/apply and IAM simulation have
   not run. The isolated worktree lacks its prescribed `.tools/terraform.exe` binary;
   canonical worktree provisioning must supply it before Terraform validation/plan.
4. Update only IRPT members of lambda-source-map.json, including M selection/store,
   accepted auth/prospect modules and P repository; verify staged blobs against pins.
   Build offline, extract each flat package into an empty directory, import entry,
   and run actual guarded positive/negative controls without repository sys.path.
5. Test the policy for each of three firms: allowed own-family object version, wrong
   firm/family/table/version denied, revoked current principal denied, missing policy
   denied, expiry denied, failed index publish hidden, retry stable, immutable conflict
   refused, export pins original report and protected download reauthorizes.
6. Prepare Terraform plan and bounded live acceptance commands for reserved approval.
   No key/deployment until render prerequisite is independently satisfied; B final
   AC5 FAIL at f82fee6aad does not satisfy it. No vendor call under this plan.

## One missing source-evidence family

The closed eleven-family S7 proposal has ORIGINAL_VENDOR_PDF but no family for the
original SmartX/BD/Orion performance JSON response. A normalized PERFORMANCE report
is not the original source evidence, and PDF is the wrong media/family meaning.
Propose one bounded addition `PERFORMANCE_SOURCE_EVIDENCE`, state table
`performance_source_evidence`, produced only by performance provider workers,
30-day unreferenced lifetime and 2555-day creation-based accepted ceiling. Store
original response bytes and a separate redacted request/response receipt; credentials
and cookies never become artifacts. M/CTO must adjudicate/register this addition
before its destination is writable. No silent reuse of another family or fallback
bucket is authorized.
