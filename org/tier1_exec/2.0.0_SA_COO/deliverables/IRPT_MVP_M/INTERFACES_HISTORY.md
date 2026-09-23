

## Superseded M interface text before Opal full-access review 2026-09-23

# M shared interfaces: candidate v1

## Maintained source resolver candidate (2026-09-23)

Authority: IRPT-MAINTAINED-SOURCE-01/02 at `0429af3604` / `51b5d63a81`.
`_scope/maintained_sources.py` implements current owner/input checks and canonical
profile projections. See `MAINTAINED_SOURCE_RESOLVER.md` for the exact signatures,
P schema `d91b2bdd10`, Y catalogue `9daa67433e`, tests and integration limits.
This supersedes the inventory's earlier recipient gap: explicit `prepared_for`
is accepted display text, never legal identity or access. Every currently
selected comparison remains unavailable; empty selection needs no fake entry.
Runtime canonical-reader transport and Y acceptance/worker integration are not
delivered by this local source candidate.

Owner: `2.0.0_SA_COO~M`. Governing authority:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.2.
These are tested Python primitives, not deployed API completion. Existing wire
schemas remain authoritative. The source is on `codex/irpt-m-completion` in
`C:/Users/AndrewBerman/Desktop/ajb_irpt_m`.
Primitives/store pin: `33e630885f`. Current shared prospect entry: `a85e7d6329`.

## Prospect ownership (S1)

Module: `infra/aws/lambda/investor-reporting/_scope/prospect.py`.

```python
owner = resolve_prospect_owner(verified_edge_headers, requested_firm_id=None)
# server-produced example:
# {schema_version: "prospect-owner-v1", firm_id: "49financial",
#  principal_id: "advisor@example.invalid", advisor_id: "advisor-one",
#  principal_class: "FIRM_ADVISOR", ownership_fingerprint: <64 hex>}
require_prospect_owner(current_verified_edge_headers, server_loaded_original_owner)
```

Caller must already enforce the existing edge/origin trust boundary. This module
does not verify JWTs or make arbitrary browser headers trustworthy. Never feed
body-supplied identity or a browser-supplied stored owner into it. It reuses the
existing `trusted_only` and `classify_principal` from `_scope/resolve.py`.
UNKNOWN, CLIENT and RENDER_DELEGATE are refused. Firm operations may own their
own upload; admin is not access to another advisor's prospect. No client/account
IDs are fabricated. Owner equality binds firm, principal, advisor and class.

Y retains this full owner beside its immutable input. On retrieval, load the owner
server-side and call `require_prospect_owner` with current claims. For P's repository
owner, map firm_id and principal_id, set account_ids=[] and the genuine issued
prospect_input_id; its authorization callback loads that input's retained owner
and calls `require_prospect_owner`. Store the full owner in input metadata,
not merely its fingerprint. No raw credentials are retained.

## Exact retained selection (S1)

Module: `infra/aws/lambda/investor-reporting/_scope/selection.py`.

```python
selection = create_selection(current_permitted_scope, current_directory,
                             [canonical_account_a], directory_revision=directory_revision(current_directory),
                             save_selection=store.save)
# save(firm_id, account_set_id, immutable_record) must persist or raise.
selected = resolve_selection(current_permitted_scope, current_directory,
                             selection["account_set_id"], store.load,
                             directory_revision=directory_revision(current_directory))
# load(firm_id, account_set_id) -> immutable_record or None
# selected_account_ids == [canonical_account_a], even if permitted is [a,b].
```

The reference is `sel_<64 hex>` binding schema, verified firm, sorted unique members
and directory revision. It is an identifier, not a bearer grant. Each resolution
requires all members in current permissions AND current firm directory. Missing
references, changed directory binding, cross-firm records, altered members and
revoked members refuse the whole request. No fallback to all permitted accounts.

Result carries `selected_account_ids`, `selected_account_set_fingerprint`,
`permitted_account_set_fingerprint`, `directory_revision`, `entitlement_revision`
and the retained `account_set_id`. The selected fingerprint uses the existing
scope fingerprint algebra over selected members and current entitlement/policy.
The separate directory revision must also be part of downstream request/cache identity.

`selection_store.SelectionStore(dynamodb_client, table_name)` persists immutable
records in the existing request table, keys `tenant` and `request_revision` with
sort prefix `SELECTION#`. `configured_store()` requires `IRPT_REQUESTS_TABLE`.
Save is conditional, identical retry is idempotent, reads are consistent. Storage
uses the registry tenant from `scope._census.tenant`; directory membership uses
`scope.verified_request_firm_id` (the opaque spelling). Never substitute these.
The returned `firm_id` is the registry tenant. P owns service environment/IAM/build.
The creator HTTP route and mounted header state are implemented and bounded-tested:
`POST /api/scoped/investor-reporting/selections`, operation `selection-create`,
body `{scope_kind: ACCOUNT|RELATIONSHIP|CLIENT, scope_ids: [...]}` returns the
tested selection record as `envelope.data`. Partial groups refuse whole.
Source creator pin `54c2ed11dc`; source schema/route composition `0076cad627`;
mounted portal `d4fca0e569` with P composition `52786a7a`. Whole groups are sent to
the server; no custody request is made until a retained `sel_` reference is accepted.
See `BROWSER_SELECTION_EVIDENCE.md` for bounds and independent review status.

## Prospect through actual shared Entry

`Entry(..., prospect_modes={operation: "CREATE_INPUT"|"OWNED_INPUT"},
load_prospect_owner=callback)` at `a85e7d6329` is opt-in per operation. Y configures
analysis-requests as OWNED_INPUT and its upload operation as CREATE_INPUT.
The callback `(verified_registry_tenant, browser_input_id) -> full retained owner`
must resolve normalized input revision to its original issued upload owner in
server storage. Y's proposed UP ownership identity is compatible; browser input_id
still identifies the immutable normalized revision. No body-supplied owner.

OWNED_INPUT uses the prospect guard only for a nonnull input_id; missing/null keeps
the existing custody guard. Mixed account/client/snapshot and prospect basis is
refused. CREATE_INPUT refuses a supplied existing input_id. Compute receives
`scope.prospect_owner`, `ctx.tenant` and canonical firm binding; ctx.directory and
ctx.ownership are None, and the prospect scope has no permitted_account_set.
Retained owner is checked before and after compute. This grants no custody access.
Y supplies compute and durable owner lookup; P packages served/prospect/ids plus
the existing firm registry. Actual deployed boundary remains unproven.

## Accepted custody positions and provider crosswalk (S2)

NOT READY. Full custody census, accepted Gold revisions, positions and historical
SmartX/BD membership are not certified by the current overlay snapshot. No consumer
may sum root/model/security values, treat COT TARGET amounts as actual positions,
infer historical model ownership from a current assignment or broaden a missing map.
M will publish a pinned loader returning the exact selected revision, unique position
rows, quantity/value/currency, source dates and explicit unknown coverage.

The output publication foundation is implemented separately: see
`PUBLICATION_EVIDENCE.md` and `PARTITIONED_PUBLICATION.md`. The first multipart
candidate is `554fc37e998554736ad98ccbfd872d400a9153ff`; the following explicit
limits are enforced by its count-limit follow-up. This remains an overlay
publication, not Y's accepted normalized security-level custody portfolio.

```python
document, manifest = HoldingsPublication(s3, canonical_firm).load(
    as_of="2026-09-22", account_ids=server_resolved_selected_account_ids)
```

The reader captures the current index once and chooses one accepted revision for
the exact business date (or latest accepted date when omitted). It does not choose
an earlier date when the requested date is absent. Same-date correction replaces
the index reference conditionally; retained object versions preserve prior bytes.
An in-flight read uses only its captured complete inventory. There is no page or
continuation token, and no automatic retry onto a different revision.

`irpt-holdings-manifest-v1` has `platinum`; `irpt-holdings-manifest-v2` replaces
that field with `platinum_header` and an ordered `partitions` list. Each partition
is `{account_ids: [...], object: reference}`. Both versions have `firm_id`,
`business_date`, content `revision`, `gold`, `source_set_revision`, and `clocks`.
Each object reference contains canonical `bucket`, `key`, non-null `version_id`,
`sha256`, and `byte_length`. Optional `source_objects` are bound into the content
revision through the `irpt-source-objects` source revision; the actual Gold caller
that captures those receipts remains separately blocked under LEGACY-READ-01.

The v2 header is the snapshot without `nodes`. Each part is
`{firm_id, revision, nodes}` and preserves whole account trees. The manifest pins
the entire inventory, including parts outside the selection. Its account sets
must be disjoint and match the header census. Each selected part must match its
declared account census and accepted revision. The reader never fetches a Gold
object. Missing, corrupted, substituted or incompatible selected data refuses.

| Boundary | Enforced limit |
|---|---:|
| Gold Parquet object | 64 MiB |
| Index JSON | 1 MiB |
| Each manifest, header or part JSON | 4 MiB |
| Packing target | 1 MiB, complete account trees |
| Complete publication account census | 25,000 |
| Complete publication part inventory | 256 |
| Selected part GET calls | 64 |
| Header plus selected part bytes retrieved | 64 MiB |
| Assembled selected raw document | 4 MiB |

A v2 reader invokes at most 67 S3 GET calls: index, manifest, header, and 64 parts.
That is an application-call limit; SDK transport retries are separate. The
64-part count is checked before any part GET. Manifest plus index add at most
5 MiB to the header/part byte budget. A v1 reader makes three GET calls. Bounds
are enforced again by readers; oversized publication, account tree or selection
refuses whole. No successful truncation, pagination or hidden full-firm fallback.

The storage loader is **not an authorization boundary**. It returns an internal
header carrying the full source census and selected trees (v2), or a bounded full
document (v1). Consumers must not return that raw structure. The actual holdings
Entry resolves the retained `accountSetId` using fresh directory, ownership,
policy and selection-store reads before loading; projects only selected trees
and recalculates selected totals; then repeats current selection authorization
and compares the complete result before release. Revocation, directory changes
and retained-reference changes refuse the whole response. Y must use equivalent
current authorization around its eventual accepted custody port; this loader
alone does not supply that port or permission to consume overlay totals.

`snapshot.load_snapshot(canonical_firm, ..., s3_client=..., account_ids=...)`
adds the accepted revision for the guarded HTTP path. No mutable legacy fallback.
Canonical Platinum keys and package dependencies stay as in `62139c3a1a`;
P's separately attributed packaging candidate is `0fb7e56629`. No deployment
or actual-source acceptance follows from these offline interfaces. Independent
review `c462d8b4df` covers v1 only; timeout-after-index-persist and suspended
versioning ambiguity findings remain open. Multipart independent review is owed.

## Reporting destination (S7)

NOT WRITABLE. P agreed `destination(firm, family, artifact_id, sha256) -> (bucket,key)`
and the eleven closed families in STORAGE_POLICY_PROPOSAL.md. IDs are RPT-32lowerhex
or ART-64lowerhex (selection references separately sel_64hex); digest64lowerhex.
CTO conditionally adjudicated placement at `bcd38bba00` and documentary issuance
exception at `90df7a0476`. M issued CRO register order `180ff84558` with real audit
append. Canonical register entry/enforcement and concrete P retention/expiry/IAM
remain prerequisites; no indefinite-storage approval or deployment is inferred.

## Validation

Run each suite in a separate Python process: `_scope/tests` has 68 passes plus
12 subtests; `_authz/tests` has159 passes, including15 new actual Entry cases.
The18 new scope/store tests cover persistence across store recreation, immutable
retry, current access, firm/identity binding and exact subset. Combined discovery
hits existing duplicate module names `fixtures`; it is not a passing invocation.
These proofs do not establish deployed E2E or full S1 acceptance.
# Maintained-source coordination under CTO 0429af3604

M claims sole integration of `infra/aws/lambda/investor-reporting/_scope/maintained_sources.py`
and its focused tests; this is a claim, not a delivered adapter. Concrete source
inventory, immutable code/configuration pins, consumer field agreement and paired
source-to-consumer examples are in `MAINTAINED_SOURCE_INVENTORY.md`. Existing
REQUEST_COMPOSITION remains `irpt-analysis-composition.v1` with browser/resolved/
recipe_version/settings; P owns final schema and source-descriptor placement.
Y owns recipe meaning and freezing/replay. No parallel payload or storage path.

Required prospect recipient display and maintained comparison authority remain
unresolved. Directory display labels also need provenance distinguishing actual
names from generated fallbacks. Those capabilities remain unavailable until their
required source evidence exists. Optional contact/custom absence is explicit in
storage and blank only at Y's vendor edge after canonical contract agreement.
Y confirms operations prepared_by may be the actual maintained acting principal
name, retaining principal class and provenance, without borrowing advisor identity.
