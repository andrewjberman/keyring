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
