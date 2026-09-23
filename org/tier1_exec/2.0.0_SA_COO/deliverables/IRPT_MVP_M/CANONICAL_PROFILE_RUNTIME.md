# Canonical profile transport and retained prospect authorization

Owner: `2.0.0_SA_COO~M`. Authority: CTO IRPT completion CONTRACT.md and
IRPT-MAINTAINED-SOURCE-01/02. This candidate extends the separately reviewed
maintained source primitive `703e82ea015d840ce773d473a7b4909e275785c0`.
Y's exact owner contract is `9db2deb4ac`, read against backend
`ef9e8f51c4fe81b60c89f7a1a3a6ec575e3cc182`.

## Consumer composition

`_scope/canonical_profile_reads.py:CanonicalProfileReaders` accepts the factory's
low-level boto3 DynamoDB client. It creates no client at import. Its `get_user`
and `get_partner_profile` methods directly satisfy the existing M resolver ports.
The actual executing transport is this Python adapter. The TS canonical
locations in source descriptors identify source-contract lineage, not execution
of TypeScript inside Python.

The adapter translates the checked-in auth `db.ts:getUser` protocol: query
`opal-users-v2`/`email-index`, limit two, reject ambiguous or incomplete results,
then read the returned actual PK with SK `PROFILE`. It verifies subject/key
readback and projects only email, firmId, status, name and updatedAt. Partner
reads use the canonical `opal-partner-{verified firm}` table and email key,
preserving the TS getPartnerProfile raw/firmRole/advisorKey shape. Only approved
report fields are requested. No credential/contact fallback, alternate table,
scan, write, profile cache or swallowed SDK error is introduced.

PROFILE and partner GetItem use strong consistency. The email GSI remains
eventually consistent: duplicate rejection does not establish transactional
identity uniqueness or universal freshness. The resolver's existing double
profile read/current owner checks remain necessary and are not a transaction.

`_scope/retained_input_authorizer.py:RetainedProspectInputAuthorizer` is constructed
per verified request with the actual Y UploadService, current trusted headers,
server-selected extended repository owner and exact input_ref. Its callable
method supplies `authorize_input(owner, input_ref)`:

```python
readers = CanonicalProfileReaders(configured_dynamodb_client)
authorize_input = RetainedProspectInputAuthorizer(
    headers=verified_headers, uploads=configured_upload_service,
    expected_owner=resolved["owner"], expected_input_ref=resolved["input_ref"])
fields = resolve_profile_fields(
    verified_headers, resolved["input_ref"], browser,
    get_user=readers.get_user, get_partner_profile=readers.get_partner_profile,
    authorize_input=authorize_input)
```

All `configured_*`, `resolved`, and verified values above must come from Y's
trusted server assembly. This is a consumer recipe, not an installed factory.
Browser identity, account grants, recipient text or caller fingerprints cannot
substitute for that assembly. Recipe/default-title provenance remains Y-owned.

Every authorization call re-resolves the actual base prospect owner and invokes
Y's `UploadService.read_input` for the exact selected normalized input. That
existing reader verifies P's protected immutable bytes/ref, frozen digest,
base document owner, original CSV source and refresh lineage. The adapter then
compares the returned extended owner/ref and the actual P retention row's
owner/family/logical ID to the selected input. Current owner is rechecked after
the read. Missing/removed retention refuses. Existing UploadService and P
repository current-access functions must remain wired to actual current policy;
this module grants no access and supplies no permissive authorization callback.

Document owner is the base `prospect-owner-v1`; repository owner adds
`account_ids=[]` and `prospect_input_id=upload_id`. They are deliberately not
equated. Custody owners are refused. No custody fingerprint or account grant is
derived from prospect identity. Y/M still owe the actual selected custody
revision, normalizer, retained owner and current account-authorization assembly.

## Verification

- `_scope/tests`: 123 PASS and 57 subtests PASS, including 21 new SDK controls.
- `tests/probe_retained_input_authorizer.py`: 19 PASS controls. It extracts exact
  local Y/P source at `ef9e8f51c4fe81b60c89f7a1a3a6ec575e3cc182`, executes actual
  UploadService/parser/ArtifactRepository/RetentionPolicy code with their
  AWS-shaped storage doubles, and tests both M adapters together with botocore
  Stubber. It blocks network connections. The ACTIVE policy is synthetic only.
- Controls include advisor/operations exact reads without writes, current grant
  revocation, pending policy, identity change, expiry before/during retrieval,
  source/retention owner mismatch, another input under the same principal,
  changed receipt, detached constructor bindings, removed retention, custody
  refusal, refresh lineage and revocation during profile capture.

No live canonical profile read, IAM grant, policy activation, production factory,
custody assembly, vendor call, deployment, render or integrated E2E is proven.
Existing real X10 PENDING_ENFORCEMENT and all full M/E2E holds remain. No push.
The separate legacy cutoff/source candidate `55a65d3bdb` has independent bounded
SOURCE PASS `5da821b8a4`; that grade does not cover this new adapter candidate.
