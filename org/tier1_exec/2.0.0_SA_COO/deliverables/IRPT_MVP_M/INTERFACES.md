# M shared interfaces: candidate v1

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
The creator HTTP route and header state are still being implemented. Proposed
`POST /api/scoped/investor-reporting/selections`, operation `selection-create`,
body `{scope_kind: ACCOUNT|RELATIONSHIP|CLIENT, scope_ids: [...]}` returns the
tested selection record as `envelope.data`. Partial groups refuse whole.

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
