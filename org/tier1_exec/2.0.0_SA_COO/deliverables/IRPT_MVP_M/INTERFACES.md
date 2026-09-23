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
