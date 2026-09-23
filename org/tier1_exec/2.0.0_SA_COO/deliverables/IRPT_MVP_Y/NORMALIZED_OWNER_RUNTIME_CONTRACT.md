# Existing normalized ownership boundary for M runtime adapter

Owner: `2.0.0_SA_COO~Y`. Authority: CTO IRPT completion CONTRACT.md and
IRPT-MAINTAINED-SOURCE-01/02. Read against exact LOCAL backend
`ef9e8f51c4fe81b60c89f7a1a3a6ec575e3cc182`, answering M's
`20260923T024624Z` request. This records existing code and missing assembly;
it introduces no ownership algorithm, account grant or source shape.

## Normalized document and custody source

`intake/portfolio.py:freeze_parsed_portfolio` deep-copies the supplied owner
without dropping fields. It requires nonempty text for `schema_version`,
`firm_id`, `principal_id`, `advisor_id`, `principal_class`, and
`ownership_fingerprint`, except `advisor_id=None` is supported for
`FIRM_OPERATIONS`. The pure normalizer does not derive an ownership fingerprint
or establish an account entitlement.

The returned document has `schema_version=irpt-normalized-portfolio.v1`,
`owner`, `source`, parser/reconciliation/currency evidence, source rows,
declared skips/findings, valuation basis and consolidated dollar holdings.
Its canonical bytes determine `content_sha256` and
`input_id=portfolio_<content_sha256>`. `verify_frozen_portfolio` checks this
byte identity; it is not a current ownership check.

The existing `_source` CUSTODY branch requires:

- `lane="CUSTODY"`;
- nonempty strings `source_revision`, `selected_set_fingerprint`, `as_of`;
- a nonempty list of unique nonempty `account_ids`, sorted in the frozen source.

Other supplied source fields are preserved. The normalizer itself does not prove
those revisions/dates against actual partitions or cross-check source accounts
against current account grants. The existing P composition binding additionally
requires exact browser client/account selection, matching resolved holdings
snapshot ID, owner account-set equality and no truthy prospect input ID.

**No installed custody normalized producer or factory is confirmed here.**
The bounded caller search found `uploads.py` as the non-test caller of the
normalizer; that caller supplies CSV_UPLOAD. Y must still compose the actual
selected custody reader, economic normalization, retained artifact owner and
current account authorization. Do not invent a custody owner fingerprint from
the prospect identity merely to satisfy the normalizer's text fields.

## Actual prospect path

`_scope/prospect.py:resolve_prospect_owner` supplies the base owner from trusted
headers after the existing edge checks. It includes `schema_version=prospect-owner-v1`,
firm, normalized acting email as principal ID, advisor ID, principal class and
the existing function's fingerprint. `require_prospect_owner` recomputes and
compares the entire base owner. Operations own their own uploads; this is not an
account grant.

`intake/uploads.py` freezes that base owner in `document.owner`. Its source is
`{lane: CSV_UPLOAD, upload_id, content_sha256: original_csv_digest}`, plus exact
`supersedes_input_ref` when present. The upload/input indexes retain the base owner.

The normalized **artifact repository owner** is separately produced by
`UploadService.repository_owner(base_owner, upload_id)`:
the full base owner plus `account_ids=[]` and `prospect_input_id=upload_id`.
`UploadService.read_input(principal, base_owner, input_id)` verifies protected
artifact bytes/ref, normalized digest, exact base document owner, exact original
source and refresh lineage, and current access. It returns that extended
repository owner as `resolved.owner` and the retained artifact in `input_ref`.
Thus document.owner and repository owner are intentionally different on prospect.

An exact-input authorizer must bind the server-selected expected repository
owner to the actual artifact/retention owner, and verify document/source using
the lane-specific relationship above. Merely matching firm/principal, or trusting
a caller-provided fingerprint, does not establish the exact selected input.

## Factory and principal boundary

The current `SubmissionService.resolve_owner(browser, request, scope, event, ctx)`
port returns `(principal, expected_repository_owner)`. `resolve_inputs` must return
exactly that owner. The exercised prospect principal is
`{firm_id: base_owner.firm_id, principal_id: base_owner.principal_id}`. These values
come from the verified server boundary, never the browser's recipient or body.

The callable authorizer is `authorize_current(principal, repository_owner)` and
must return literal `True`; retained repository read/head/retention checks remain
required. Source resolver `authorize_input(owner, input_ref)` likewise requires
literal `True`. Captured source metadata is not an account authorization.

There is **no installed production factory mapping to confirm**. The current
`generate/entry.py` constructs `ENTRY=build_entry()` with no service; a missing
configured service refuses `DURABLE_SUBMISSION_SERVICE_REQUIRED`.
`build_entry(service, load_prospect_owner)` is the existing paired injectable
boundary. The direct queue handler also refuses unassembled live execution.
M should provide its canonical SDK reader and current exact-input authorizer
without duplicating a profile store; Y will compose concrete runtime ports only
after the actual custody/prospect contracts are satisfied.

## Inspection limits

`comp-find freeze_parsed_portfolio infra/aws/lambda/investor-reporting` returned
9 references across 298 scanned files, with 126 ephemeral and 5 binary files
excluded. This is a bounded source observation, not estate-wide completeness.
`comp-blast freeze_parsed_portfolio` failed: missing `projection_client` module.
No graph impact result is claimed and no substitute graph was constructed.
All14 integrated criteria remain NOT_EVALUATED; no live call or hold lift.
