

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


## Superseded integration boundary before P174849 viewer agreement

## Integration boundary and next action

M proposes the maintained-profile adapter changes above for exact coordination
with P/Y. Current callback `authorize_input(owner, input_ref)` and descriptors bind
one owner; silently redefining it as a viewer would corrupt attribution. P/Y must
identify the concrete invoking adapter and agree the current-viewer/retained-input
separation before M changes it. No parallel signature or field-name draft is cut.
The first-hop work remains active; deeper source/recipe work stays parked unless
P's trace makes it a required dependency. No producer work was restarted.

CTO directly reviews. Source inspections establish the listed branches only;
no new tests, cloud reads/writes, vendor calls, package changes or deployment were
performed for this review. The prior 99 publication tests and 114 local COT tests
are offline evidence and do not establish actual custody or Opal live acceptance.
CLOUD push remains held. Ordinary firm-user and forged-identity refusals remain.


## Superseded by implemented viewer source ports 485b69c061

# M current interfaces

Contract v1.3 plus controlling access ruling `5ad99c7d30`. Shared interface
reviewed at P `9a3ec2a11f`; M publication runtime `3539ad2ae5`, docstring correction
`200ba442f5`. This is a bounded source review and current interface handoff, not
live evidence or a new schema. Superseded interface text is in
[INTERFACES_HISTORY.md](INTERFACES_HISTORY.md).

## Trusted viewer and exact M/data findings

P owns `_scope/interactive_access.py`, shared Entry/API/UI and authorization.
Use server-created `InteractiveAccess(read_headers, data_firm,
ordinary_authorizer=...)`; `current()` supplies the real actor and
`authorize_current(viewer, retained_owner)` decides current access. Preserve
retained creator, source and firm attribution. Never substitute a creator into
current viewer identity. Global/selected firm is a view filter, not Opal's
permission ceiling. No unconditional True production authorizer.

The following findings are from source at `9a3ec2a11f`, not new test runs:

| Exact surface | Observed constraint | Required distinction / owner |
|---|---|---|
| `_scope/selection.py::_check`, `create_requested_selection`, `resolve_selection`, `_view` | One verified firm, one directory population, one retained directory revision and one firm-bound fingerprint; mixed-firm member input cannot pass one record | Keep per-record census/integrity checks. P needs an attributed composition over separately resolved firm selections; a missing composition capability must not be called Opal permission denial. |
| `_scope/selection_store.py::_key`, `save` | Tenant plus SELECTION#reference key; exact record firm/reference equality | Physical storage identity, not viewer home or creator authorization. Do not flatten records into a global tenant or remove binding equality. |
| `_scope/resolve.py::resolve` OPAL_GLOBAL branch | Resolves only the selected firm's population; comment cites obsolete prohibition on an all-firm union | One-directory computation can remain an inner operation. P's outer verified-Opal path must not treat this population as the user's total authority. Ordinary actor bounds remain. |
| `_scope/custody.py::current_custody_principal`, `CustodyAccess.authorize_current`, `profile_authorizer` | Requires concrete tenant; retained checks compare owner to a newly assembled current-actor owner | Concrete tenant is valid source placement. Exact creator equality cannot remain the authorization gate for another creator's retained record. Separate current viewer authorization from immutable source-owner/input equality; coordinate in P's shared ownership. |
| `_scope/maintained_sources.py::snapshot_profile_sources`, `resolve_profile_fields` | Calls firm-only resolve_prospect_owner; _user_projection compares active user firm to owner.firm_id | Verified Opal prospect preparation is rejected before source readers. M's dependent adapter must take the server-created actor separately from input placement, and read that actor's canonical user/home organization. Do not invent a partner advisor or label missing profile/placement as denied access. |
| `_scope/maintained_sources.py::snapshot_custody_profile_sources` | Requires custody-owner-v1, OPAL_GLOBAL, account IDs; current principal fields must equal accepted owner's creator fields before authorize_input | This existing same-creator custody preparation path is not a general other-owner/prospect access adapter. New preparation must preserve original input attribution while resolving the acting preparer's profile independently. Retained frozen profiles must remain frozen on view/replay, not be silently replaced by the viewer's profile. |
| `_scope/maintained_sources.py::resolve_comparison_fields` | Calls firm-only resolve_prospect_owner even before the empty-selection return | An empty comparison request from verified Opal must not fail on actor class. Nonempty comparison catalogue/recipe capability remains separately unimplemented; broad Opal authority does not invent comparison data or a vendor request. |
| `_authz/served.py::Entry.handle` Global branch; `_scope/owner_reads.py::guard_owner_read`; `_scope/prospect.py` | Global non-resolve routes return FIRM_BINDING; retained reads enforce custody-only and creator equality; prospect resolver admits only firm advisor/operations | Confirmed P-owned integration findings already named in P's interface. Do not duplicate their implementation in M. |

## Attributed composition capability gap

Existing selection signatures are unchanged:

```python
selected = resolve_selection(current_firm_scope, current_firm_directory,
    server_loaded_reference, store.load,
    directory_revision=directory_revision(current_firm_directory))
```

Example: a verified Opal viewer selects one 49financial account and one Cottonwood
account. Resolve each firm's real directory/selection independently under that
same verified viewer. Retain each data firm, exact account IDs, selection reference,
directory/entitlement revision and selected fingerprint. A reference from firm A
must still refuse if misfiled as a firm B record; that is not denial of the viewer's
legitimate access to A. Return attributed results rather than silently narrowing
the requested set to the chosen view filter.

No current primitive above supplies the composite persisted selection identity,
revision-aware paging/cache behavior, per-firm snapshot receipts, or a cross-firm
report recipe. P owns the shared composition/schema decision and can report these
as capability gaps. Do not concatenate directory rows under one firm's fingerprint,
reuse one firm's snapshot hash for several firms, invent a Global storage firm,
or silently sum values whose dates/currencies/recipe semantics are incompatible.
This proposal uses the existing per-firm interfaces; it emits no new wire fields.

## Exact publication history interface

`HoldingsPublication.capture(*, as_of=None, account_ids=None)` returns
`(document, manifest, receipt)`. `load_pinned(receipt, *, account_ids=None)` returns
`(document, manifest)` without consulting the current index.

Receipt schema `irpt-holdings-acceptance-v1` has exactly `schema_version`, `firm_id`,
`business_date`, `index`, `date_row`. Index is `{bucket,key,version_id,sha256,
byte_length}`; date_row is `{revision,manifest}` with the same immutable reference
shape for manifest. The historical index version must accept that exact date row.
`receipt.date_row.revision` is the original full snapshot hash, never the selected
or decorated document hash. P stores the private receipt unchanged in its binding.

`snapshot.capture_snapshot(firm_id, prefix=DEFAULT_PREFIX, as_of=None,
s3_client=None, *, account_ids=None)` returns `(decorated_document, receipt)`;
`load_pinned_snapshot(firm_id, receipt, prefix=DEFAULT_PREFIX, s3_client=None,
*, account_ids=None)` returns the decorated document. Existing load methods remain
compatible. These functions have no actor-home/creator permission test. Their
firm/path/hash/version/census checks are source identity checks and must remain.
The returned raw header/full document is internal; the guarded projection controls
what is released. P checks current viewer authority separately.

## Optional maintained-profile viewer seam: proposed, not implemented

Requested by P174849, using `InteractiveAccess` at `9a3ec2a11f`, P explicit
storage placement `dd6edfc3aa`, Y viewer propagation `85af5eb95d`. Entry roles:
`scope.current_owner` is the actual viewer; `scope.prospect_owner` is the retained
or create owner. Neither record is relabeled. Existing single-firm selection and
publication interfaces above remain unchanged.

Proposed backward-compatible Python keyword additions (no HTTP/schema fields):

```python
resolve_profile_fields(headers, input_ref, browser, *, get_user,
    get_partner_profile, authorize_input=None, registry_path=None,
    recipe_title_source=None, input_owner=None, current_viewer=None,
    authorize_viewer_input=None, get_organization=None)

resolve_custody_profile_fields(headers, owner, input_ref, browser, *, get_user,
    get_organization, authorize_input=None, recipe_title_source=None,
    current_viewer=None, authorize_viewer_input=None)

resolve_comparison_fields(headers, input_ref, comparison_keys, *, get_catalogue,
    authorize_input=None, input_owner=None, current_viewer=None,
    authorize_viewer_input=None)
```

`snapshot_profile_sources` receives the same new profile keywords except browser
and recipe_title_source. `snapshot_custody_profile_sources` receives the same
current_viewer/authorize_viewer_input pair; its existing owner argument remains
the original input owner. Resolver functions forward these ports unchanged.

Two explicit modes, with no permissive fallback:

- Legacy mode: all new viewer/owner ports absent; callable
  `authorize_input(owner, input_ref)` retains its existing stored-owner meaning
  and every existing call shape/guard. This is not the Opal integration path.
- Viewer mode: `current_viewer` and `authorize_viewer_input` are both callable;
  a complete server-loaded `input_owner` is required for prospect/comparison,
  and the existing owner argument supplies it for custody. `authorize_input`
  is None/omitted. Partial mode or both authorization callbacks refuses as
  configuration error; do not silently reinterpret or fall through to legacy.

`current_viewer() -> dict` re-resolves the actual viewer from P's current trusted
request boundary, e.g. request-local `InteractiveAccess.current`. A lambda merely
returning a captured scope dict does not meet the freshness contract. Compare
its first result with the Entry's initial scope.current_owner when constructing
the adapter, then recheck it before and after all reads and at acceptance release.
No browser owner, role string, report creator or service token constructs it.

`authorize_viewer_input(viewer, input_owner, input_ref) -> literal True` is a
SERVER callback owned by the caller. It must authorize the exact current viewer
AND load/validate that input's immutable owner/reference, placement and retention.
For Opal it uses the trusted cross-creator/cross-firm policy; for ordinary actors
it preserves existing narrower checks. `InteractiveAccess.authorize_current`
alone is insufficient: broad viewer permission does not prove the input exists,
its original owner matches, its receipt/hash is valid, or its retention is live.
Missing/deleted/expired/substituted input refuses. Exceptions and non-True results
never become success. Call before and after profile/source reads; final release
remains the acceptance service's responsibility.

Capture detached copies of viewer, input owner, input reference and browser
selection. Recheck their stability, reread the relevant maintained projections as
today, and invoke the same authorization on each boundary. The callback re-loads
the retained owner and checks exact equality; equality of a local copied dict is
not proof that backing storage stayed unchanged. Mutable profile digests are not
immutable upstream versions.

### Actor profile versus retained input attribution

For NEW preparation only, read the maintained user by actual viewer.principal_id,
validate active status and viewer.home_firm_id (ordinary fallback is its firm_id),
and use the actor's home organization. Verified Opal uses the existing canonical
get_organization(home_firm_id) descriptor reader, including its projection digest
and source-scope checks. Missing placement, organization or adapter is an explicit
source/configuration capability gap. Do not use the selected firm's organization
as the actor's home or fabricate a partner advisor. Ordinary advisor preparation
continues to use its real maintained partner profile; ordinary operations use its
actual maintained user name.

Keep ProfileSourceSnapshot.owner and source_descriptors.binding tied to the
original input owner/placement. The implementation would carry actual viewer as
a separate INTERNAL snapshot member; source_scope for actor/user/organization and
accepted-browser-display provenance names the actual source actor/home. In
particular, browser display text's source_owner is the actor who supplied it,
not another person's retained input owner. Preserve the existing public return
keys profile/profile_provenance/source_descriptors; no new wire identity field.
P/Y must ensure their existing descriptor validators distinguish input binding
from actual actor source_scope; an equality assumption there is an integration
change to name explicitly, not a reason to rewrite stored creator attribution.
Recipe/source/reference integrity checks remain required.

Viewing, replaying, retrying, or exporting an already accepted report does NOT
invoke either profile resolver to replace its frozen prepared_by, organization,
recipient, profile bytes or descriptors. Authorize the current viewer separately
and return the original retained composition. A new report is a new preparation,
not a rewrite of the retained original.

### One caller example (proposed source adapter)

For verified Opal actor A creating a new report from actor B's retained upload:

```python
# All objects/callables supplied by the server after Entry validation.
fields = resolve_profile_fields(headers, loaded_input_ref, accepted_browser,
    get_user=canonical_get_user,
    get_partner_profile=canonical_get_partner_profile,
    get_organization=canonical_get_organization,
    input_owner=scope["prospect_owner"],       # original B, exact data firm
    current_viewer=interactive_access.current, # actual A, fresh trusted request
    authorize_viewer_input=authorize_exact_retained_input)
```

The new profile names A's maintained preparer/home organization. Input owner B,
its data firm, receipts and immutable reference stay unchanged. Reading B's
already-frozen report instead returns B's original frozen profile under current
viewer authorization. Empty comparisons use the same viewer/owner callback pair
and return the existing empty catalogue/descriptors without a catalogue read.
Nonempty unimplemented comparison recipes remain capability gaps; no vendor call
or fabricated economic identity is authorized by this interface.

### Evidence and next integration step

Source inspection at Y85af5eb95d finds the maintained-profile invocation in
`intake/tests/test_retained_uploads.py::maintained_fields`; its legacy two-argument
authorizer closes over the actual principal while receiving the stored owner.
The inspected ops/entry.py path propagates actual scope.current_owner separately
from resolve_data_firm. This does not establish a production maintained-profile
adapter; P/Y must supply the concrete invoking adapter for the viewer mode.

Three intended checks when implementation is admitted: (1) new authorized Opal
prospect/other-owner preparation uses actual actor profile with unchanged input
owner and empty-comparison success; (2) ordinary/forged denial and changed actor,
input reference, placement or retention refuse; (3) retained replay/export stays
byte-identical while separately authorizing the viewer. No tests were run for
this signature proposal. The routed comp-blast reported SUBJECT_ABSENT_FROM_CORPUS
for resolve_profile_fields; that is not impact clearance. Local source reads
supply the bounded findings above.

Next: P/Y consume these exact optional ports and identify a signature/descriptor
mismatch with a minimal caller example, or pin the invoking adapter for the owned
M change. Live-first priority and deeper-work park remain. No shared source edits,
producer work, application data reads, package changes, deployment or push here.
CTO remains the reviewer; P's reported first-hop apply is not independently
verified by this interface review and does not release other cloud work.
