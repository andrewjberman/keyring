# Current-owner reads through shared Entry

Authority: completion CONTRACT S1/S4; Y requests at 23:57:45Z and 00:03:38Z.
This is opt-in source plumbing. No routes are installed or deployed by this change.
The existing custody and CREATE_INPUT/OWNED_INPUT paths retain their prior defaults.

```python
Entry(...,
    owner_read_modes={
        "analysis-request-history": "CURRENT_OWNER_HISTORY",
        "analysis-request-read": "OWNED_RECORD",
        "analysis-report": "OWNED_RECORD",
    },
    record_id_parameters={
        "analysis-request-read": "requestId",
        "analysis-report": "jobId",
    },
    load_record_owner=load_record_owner,
    authorize_record_owner=authorize_record_owner)
```

`load_record_owner(verified_registry_tenant, operation, issued_reference)` returns
the complete retained owner from server storage, or None. The operation disambiguates
request and job stores. The reference is an ASCII alphanumeric/underscore/hyphen
lookup key, at most 200 characters; Y additionally validates its issued ID grammar
and accepted-state binding. No ID or browser-provided owner is authority.

`authorize_record_owner(current_principal, retained_full_owner) -> True` must
re-resolve the service's current authorization, including retained custody scope
where applicable. Any other result refuses. Entry independently requires matching
firm and principal, calls both ports before and after compute, compares complete
owners across the read, and re-resolves the verified principal before release.
Both ports are mandatory for OWNED_RECORD. Callback values passed to compute are
copied so mutation cannot erase the before-read comparison. Missing, changed,
foreign or revoked records release no data.

Compute keeps the ordinary `(request, scope, event, ctx)` signature. It receives
`scope.current_owner` using the established prospect-owner-v1 verified principal
shape and, for an issued read, `scope.retained_record_owner`. `ctx.tenant` is the
registry tenant. `ctx.directory` and `ctx.ownership` are None. No permitted account
set, synthetic client or prospect input is created. An existing custody reader
must never be relabeled an owner-only reader without its service's retained-scope
authorization implementation.

CURRENT_OWNER_HISTORY receives only the current principal. The service owns bounded
querying, exact-owner filtering, record-by-record current grants, accepted state,
retention and final rechecks. Y's OwnedRequestReader at `e93300e34b` is that separate
service; Entry does not confer a blanket record grant. History supports its one
bounded page and opaque continuation hint, not arbitrary scope query parameters.

These modes require GET and refuse supplied body/input, custody object, event params
or ownership/custody query fields. `pathParameters.requestId`/`jobId` supply only
issued lookup references; normal history limit/cursor query parameters remain for
service validation. The outer shared Entry still checks contract version, verified
firm and operation, and the owner guard uses trusted claims/origin checks.

Validation: 19 new actual Entry tests plus 15 existing prospect tests pass. Full
authorization suite: 173 PASS, five FAIL; a fresh pre-change baseline has 154 PASS
and the identical five failures. Two are inherited selection-create positive
fixtures lacking its new required scope; three hard-code 12 routes while the
published table now has 13. All 13 routes report guarded. Those fixtures were
preserved; this result is not labeled an all-green broad suite. Y/P composition,
flat package and independent review remain required before acceptance.
